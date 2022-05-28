from interactions.ext import Base, Version
from .extension import Persistence

version = Version(version="1.0.0-beta.1")

base = Base(
    name="Persistence",
    version=version,
    link=f"https://github.com/dworv/interactions-persistence",
    description="An extension to add simple custom_id encoding to interactions.py.",
    packages="interactions.ext.persistence"
)

def setup(bot):
    return Persistence(bot)