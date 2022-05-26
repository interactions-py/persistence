class PersistentCustomID:
    def __init__(self, tag: str, payload: str):  # noqa
        self.tag: str = tag
        self.payload = payload

    @property
    def packed(self) -> str:
        return f"persistence_{self.tag}:{self.payload}"

    def __str__(self):
        return self.packed

    @property
    def package(self) -> object:
        return eval(self.payload)

    @classmethod
    def from_string(cls, string: str):
        string = string.removeprefix("persistence_")
        tag, payload = string.split(":")
        return cls(tag, payload)

    @classmethod
    def new(cls, tag: str, package: "SupportsRepr"):
        return cls(tag, repr(package))
