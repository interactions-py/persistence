from interactions.ext import Base, Version, VersionAuthor

_name = "unnamed" # TODO: change when i think of something lmao
version = Version(version="0.0.0")

base = Base(
    name=_name, 
    version=version, 
    link=f"https://github.com/dworv/interactions-{_name}",
    description="An extension to add simple custom_id encoding to interactions.py.",
    long_description="Remind me to make this",
)

def setup(bot):
    print('WTF IT WORKED')