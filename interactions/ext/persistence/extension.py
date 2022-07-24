"""The file holding the PersistenceExension class and all of its functionality."""

from inspect import getmembers, iscoroutinefunction
from interactions import Extension, Client


class PersistenceExtension(Extension):
    """The PersistenceExtension is based off of regular Extensions, but adds callbacks for persistent components and modals"""

    def __new__(cls, client: Client, *args, **kwargs):
        """
        The extended __new__ dunder method for Persistence Extensions.

        Args:
            client (Client): An `interactions.Client` instance

        Returns:
            Extension: Returns a basic `interactions.Extension`
        """

        self = super().__new__(cls, client, *args, **kwargs)

        for _, func in getmembers(
            self, predicate=iscoroutinefunction
        ):  # credits to toricane for the inspect stuff
            if hasattr(func, "__persistence_type__"):
                if func.__persistence_type__ == "component":
                    client.persistence.component(func.__persistence_tag__)(func)
                elif func.__persistence_type__ == "modal":
                    client.persistence.modal(
                        func.__persistence_tag__, func.__persistence_use_kwargs__
                    )(func)

        return self

class PersistenceExt:
    """
    The PersistenceExt class is meant to be placed before `interactions.Extension` in the inheritences of a user Ext like so:
    ```py
    class MyExt(
        PersistenceExt,
        Extension
    )
    ```
    It adds callbacks for persistent components and modals
    """
    def __new__(cls, client, *args, **kwargs):

        self = super().__new__(cls, client, *args, **kwargs)

        for _, func in getmembers(
            self, predicate=iscoroutinefunction
        ):  # credits to toricane for the inspect stuff
            if hasattr(func, "__persistence_type__"):
                if func.__persistence_type__ == "component":
                    client.persistence.component(func.__persistence_tag__)(func)
                elif func.__persistence_type__ == "modal":
                    client.persistence.modal(
                        func.__persistence_tag__, func.__persistence_use_kwargs__
                    )(func)

        return self

def extension_persistent_component(tag: str):
    """Callback for persistent components in extensions

    Args:
        tag (str): The tag to identify your component
    """

    def inner(coro):
        coro.__persistence_type__ = "component"
        coro.__persistence_tag__ = tag
        return coro

    return inner


def extension_persistent_modal(tag: str, use_kwargs: bool = False):
    """Callback for persistent modals in extensions

    Args:
        tag (str): The tag to identify your modal
        use_kwargs (bool): Whether to return key word arguments mapped with the custom_ids of the individual text inputs. Not recommended.
                (defaults to False)
    """

    def inner(coro):
        coro.__persistence_type__ = "modal"
        coro.__persistence_tag__ = tag
        coro.__persistence_use_kwargs__ = use_kwargs
        return coro

    return inner
