from interactions import Client


def persistent_component(bot: Client, tag: str):
    """Callback for persistent components.

    Args:
        bot (Client): The Client instance
        tag (str): The tag to identify your component
    """
    def inner(coro):
        bot.event(coro, name="component_persistence_" + tag)
        return coro

    return inner


def persistent_modal(bot: Client, tag: str):
    """Callback for persistent modals.

    Args:
        bot (Client): The Client instance
        tag (str): The tag to identify your modal
    """
    def inner(coro):
        bot.event(coro, name="modal_persistence_" + tag)
        return coro
    
    return inner


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


def extension_persistent_modal(tag: str):
    """Callback for persistent modals in extensions

    Args:
        tag (str): The tag to identify your modal
    """
    def inner(coro):
        coro.__persistence_type__ = "modal"
        coro.__persistence_tag__ = tag
        return coro

    return inner
