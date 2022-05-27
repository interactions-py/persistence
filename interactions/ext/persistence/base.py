from interactions.ext import Base, Version
from .extension import Persistence

version = Version(version="0.1.0")

base = Base(
    name="Persistence",
    version=version,
    link=f"https://github.com/dworv/interactions-persistence",
    description="An extension to add simple custom_id encoding to interactions.py.",
    long_description=".",  # TODO
)

def setup(bot):
    return Persistence(bot)