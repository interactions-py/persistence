from interactions import Client


def persistent_component(bot: Client, tag: str):
    def inner(coro):
        bot.event(coro, name="component_persistence_" + tag)
        return coro

    return inner


def persistent_modal(bot: Client, tag: str):
    def inner(coro):
        bot.event(coro, name="modal_persistence_" + tag)
        return coro
    
    return inner


def extension_persistent_component(tag: str):
    def inner(coro):
        coro.__persistence_type__ = "component"
        coro.__persistence_tag__ = tag
        return coro

    return inner


def extension_persistent_modal(tag: str):
    def inner(coro):
        coro.__persistence_type__ = "modal"
        coro.__persistence_tag__ = tag
        return coro

    return inner
