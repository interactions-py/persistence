# Persistence

![PyPI - Downloads](https://img.shields.io/pypi/dm/interactions-persistence?color=red)

An extension for interactions.py that dynamically places and returns objects in and from Discord's `custom_ids` so you don't have to. Check the [wiki](https://github.com/Dworv/interactions-persistence/wiki) to learn how to use it!

## How it works
The most popular [interactions.py](https://github.com/interactions-py) extension, [Wait-For](https://github.com/interactions-py/wait_for) is an easy and effective way to simplify complex component chains by preserving the objects used during interaction.
However, this means that any components created before the bot restarts become unresponsive.
This could be solved by saving all previous needed interaction details to the disk, but that may not be an ideal solution for everyone. Luckily, there is another option.

## The solution
The solution, originally conceived and executed by [Toricane](https://github.com/Toricane), was to place information in Discord's custom_ids. In the vanilla library, this requires some `on_component` or `on_modal` logic. [Enhanced](https://github.com/interactions-py/enhanced) simplifies this by adding `startswith` and `regex` args to the `bot.component` and `bot.modal` decorators. However, even this is more complicated than necessary.

## Further abstraction
Interactions-Persistence further simplifies placing objects in custom_ids using the `repr` method from objects and evaluating them to return the right type. Using this ext is not only incredibly simple, but also reliable and lightweight. Taking a similar approach to [Enhanced](https://github.com/interactions-py/enhanced), Persistence uses `on_component` and `on_modal` listeners to identify and properly call persistent decorators.

Enjoy!
