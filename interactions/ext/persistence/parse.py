def persistent_custom_id(tag: str, package: "SupportsRepr"):
    return str(PersistentCustomID.new(tag, package))

class ParseError(BaseException):
    pass

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
        try:
            tested = eval(repr(package))
            if type(tested) != type(package):
                raise ParseError(
                    "Evaluation the repr of the package did not return the same type."
                )
            if len(tag) + 1 + len(repr(package)) > 100:
                raise ParseError("The tag and payload combined are longer than 100 characters.")
            return cls(tag, repr(package))
        except:
            raise ParseError("The package could not be evaluated because it didn't properly implement __repr__.")