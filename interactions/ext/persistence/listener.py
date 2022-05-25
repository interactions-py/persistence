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
