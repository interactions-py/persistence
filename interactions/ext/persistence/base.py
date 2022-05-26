from types import MethodType
from interactions import (
    Client,
    ComponentContext,
    CommandContext,
    Extension,
    extension_listener,
)
from interactions.ext import Base, Version
from .listener import persistent_component, persistent_modal
from .parse import PersistentCustomID

version = Version(version="0.1.0")

base = Base(
    name="Persistence",
    version=version,
    link=f"https://github.com/dworv/interactions-persistence",
    description="An extension to add simple custom_id encoding to interactions.py.",
    long_description=".",  # TODO
)


class Persistence(Extension):
    def __init__(self, bot: Client):
        bot.persistent_component = MethodType(persistent_component, bot)
        bot.persistent_modal = MethodType(persistent_modal, bot)

    @extension_listener(name="on_component")
    async def _on_component(self, ctx: ComponentContext):
        if not ctx.custom_id.startswith("persistence_"):
            return
        custom_id = PersistentCustomID.from_string(ctx.custom_id)
        listener = self.client._websocket._dispatch
        for name, funcs in listener.events.items():
            if name == "component_persistence_" + custom_id.tag:
                for func in funcs:
                    await func(ctx, custom_id.package)
                break


def setup(bot):
    return Persistence(bot)
