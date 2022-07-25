"The base of the extension."

from interactions.ext import Base, Version, VersionAuthor
from .persistence import Persistence

version = Version(
    version="2.2.1",
    author=VersionAuthor(
        name="Dworv",
        email="dwarvyt@gmail.com",
    ),
)

base = Base(
    name="Persistence",
    version=version,
    link="https://github.com/dworv/interactions-persistence",
    description="An extension to add simple custom_id encoding to interactions.py.",
    packages="interactions.ext.persistence",
)

def setup(bot, cipher_key=None):
    return Persistence(bot, cipher_key)
