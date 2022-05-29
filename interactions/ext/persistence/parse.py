def persistent_custom_id(tag: str, package: "SupportsRepr"): # noqa
    """Builds a brand new persistent custom_id.

        Args:
            tag (str): The identifier for the custom_id
            package (SupportsRepr): An object to be placed in the custom_id (must support proper repr)

        Raises:
            ParseError: Evaluation the repr of the package did not return the same type.
            ParseError: The tag and payload combined are longer than 100 characters.
            ParseError: The package could not be evaluated because it didn't properly implement __repr__.

        Returns:
            str: The custom_id to be used in the custom_id arg for components and modals
    """
    return str(PersistentCustomID.new(tag, package))

class ParseError(BaseException):
    """Called when there is an error during parsing."""
    pass

class PersistentCustomID:
    """An internal class for managing persistent custom_ids"""
    def __init__(self, tag: str, payload: str):
        """Creates a PersistentCustomID.

        Args:
            tag (str): The identifyer for the custom_id
            payload (str): The dynamic payload of what you send to discord
        """
        self.tag: str = tag
        self.payload = payload

    @property
    def packed(self) -> str:
        """Packs the tag and payload and prepares them to be sent to Discord.

        Returns:
            str: A custom_id to be used in your component or modal.
        """
        return f"persistence_{self.tag}:{self.payload}"

    def __str__(self):
        return self.packed

    @property
    def package(self) -> object:
        """Evaluates the payload and returns an object.

        Returns:
            object: Your object that you placed in the custom_id
        """
        return eval(self.payload)

    @classmethod
    def from_string(cls, string: str):
        """A classmethod for unpacking a custom_id from Discord into a PersistentCustomID object.

        Args:
            string (str): The custom_id from Discord

        Returns:
            PersistentCustomID: A new PersistentCustomID object.
        """
        string = string.removeprefix("persistence_")
        tag, payload = string.split(":")
        return cls(tag, payload)

    @classmethod
    def new(cls, tag: str, package: "SupportsRepr"): # noqa
        """Builds a brand new PersistentCustomID object.

        Args:
            tag (str): The identifier for the custom_id
            package (SupportsRepr): An object to be placed in the custom_id (must support proper repr)

        Raises:
            ParseError: Evaluation the repr of the package did not return the same type.
            ParseError: The tag and payload combined are longer than 100 characters.
            ParseError: The package could not be evaluated because it didn't properly implement __repr__.

        Returns:
            PersistentCustomID: A new PersistentCustomID
        """
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