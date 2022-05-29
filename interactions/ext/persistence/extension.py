from inspect import getmembers, iscoroutinefunction
from types import MethodType
from interactions import Client, ComponentContext, CommandContext, Extension, extension_listener

from .decor import persistent_component, persistent_modal
from .parse import PersistentCustomID


class PersistenceExtension(Extension):
    """The PersistenceExtension is based off of regular Extensions, but adds callbacks for persistent components and modals"""
    def __new__(cls, client: Client, *args, **kwargs):
        """The extended __new__ dunder method for Persistence Extensions.

        Args:
            client (Client): An `interactions.Client` instance

        Returns:
            Extension: Returns a basic `interactions.Extension`
        """

        self = super().__new__(cls, client, *args, **kwargs)

        for _, func in getmembers(self, predicate=iscoroutinefunction):
            if hasattr(func, "__persistence_type__"):
                if func.__persistence_type__ == "component": 
                    client.event(func, name="component_persistence_" + func.__persistence_tag__)
                elif func.__persistence_type__ == "modal":
                    client.event(func, name="modal_persistence_" + func.__persistence_tag__)

        return self

class Persistence(Extension):
    """The Persistence Extension"""
    def __init__(self, bot: Client):
        """Initializes Persistence.

        Args:
            bot (Client): An `interactions.Client` instance
        """
        bot.persistent_component = MethodType(persistent_component, bot)
        bot.persistent_modal = MethodType(persistent_modal, bot)

    @extension_listener(name="on_component")
    async def _on_component(self, ctx: ComponentContext):
        """The listener for components."""
        if not ctx.custom_id.startswith("persistence_"):
            return
        custom_id = PersistentCustomID.from_string(ctx.custom_id)
        listener = self.client._websocket._dispatch
        for name, funcs in listener.events.items():
            if name == "component_persistence_" + custom_id.tag:
                for func in funcs:
                    await func(ctx, custom_id.package)
                break

    @extension_listener(name="on_modal")
    async def _on_modal(self, ctx: CommandContext):
        """The listener for modals."""
        if not ctx.data.custom_id.startswith("persistence_"):
            return
        custom_id = PersistentCustomID.from_string(ctx.data.custom_id)
        listener = self.client._websocket._dispatch
        answers = []
        if ctx.data._json.get("components"):
            for component in ctx.data.components:
                if component.get("components"):
                    answers.append(
                        [_value["value"] for _value in component["components"]][0]
                    )
                else:
                    answers.append([_value.value for _value in component.components][0])
        for name, funcs in listener.events.items():
            if name == "modal_persistence_" + custom_id.tag:
                for func in funcs:
                    await func(ctx, custom_id.package, *answers)
                break