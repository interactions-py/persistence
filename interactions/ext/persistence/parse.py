"""The file containing the PersistentCustomID class and all of its functionality."""

from json import loads, dumps
from typing import Union, TYPE_CHECKING
from interactions import Client

from .cipher import Cipher

if TYPE_CHECKING:
    from .persistence import Persistence


def pack(obj):
    """
    Packs a compatible object into a string.

    Parameters:
        obj (object): The object to pack.
    """
    if isinstance(obj, (dict, list)):
        return dumps(obj)
    elif isinstance(obj, (str, int, float)):
        # make a list to encode it and then remove brackets
        return dumps([obj])[1:][:-1]


def unpack(encoded):
    """
    Unpacks a string into a compatible object.

    Parameters:
        encoded (str): The string to unpack.
    """
    if encoded.startswith(("{", "[")):
        return loads(encoded)
    else:
        return loads(f"[{encoded}]")[0]


class ParseError(BaseException):
    """Called when there is an error during parsing."""

    pass


class PersistentCustomID:
    """
    The Persistence custom_id parser.

    Used both internally and externally to parse custom_ids. Make sure to convert to a string when used in a component or modal like so: `str(your_custom_id)`.

    Attributes:
        cipher (Cipher): The cipher to use.
        tag (str): The tag to identify the component or modal.
        package (dict, list, str, int, float): The package of the component or modal.
    """

    def __init__(
        self,
        cipher: Union["Persistence", Client, Cipher],
        tag: str,
        package: Union[dict, list, str, int, float],
    ):
        """
        The constructor for the Persistence custom_id parser.

        Parameters:
            cipher (Cipher): The cipher to use.
            tag (str): The tag to identify the component or modal.
            package (dict, list, str, int, float): The package of the component or modal.
        """
        if isinstance(cipher, Client):
            self.cipher = cipher.persistence._cipher
        elif isinstance(cipher, Cipher):
            self.cipher = cipher
        else:
            try:
                self.cipher = cipher._cipher
            except AttributeError as e:
                raise ParseError("Invalid cipher provided.") from e
        self.tag = tag
        self.package = package
        if len(self.encrypt()) > 100:
            raise ParseError("Encoded custom_id is too long.")

    def encrypt(self):
        """
        Encrypts the package.

        Returns:
            str: The encrypted package.
        """
        sep = len(self.tag)
        raw = self.cipher.encrypt(self.tag+pack(self.package))
        return f"p0~{raw[:sep]}~{raw[sep:]}"

    def __str__(self):
        """Returns the encrypted custom_id as a string."""
        return self.encrypt()

    @classmethod
    def from_discord(cls, cipher: Union["Persistence", Client, Cipher], custom_id: str):
        """
        The method used internally to parse custom_ids from Discord.

        Parameters:
            cipher (Cipher): The cipher to use.
            custom_id (str): The custom_id to parse.
        """
        # if its a bot
        if hasattr(cipher, "persistence"):
            cipher = cipher.persistence._cipher
        # if its a cipher object
        elif isinstance(cipher, Cipher):
            cipher = cipher
        # if its a persistence object
        else:
            cipher = cipher._cipher
        
        _version, _tag, _payload = custom_id.split("~")

        sep = len(_tag)
        raw = cipher.decrypt(_tag+_payload, _version)
        tag = raw[:sep]
        payload = raw[sep:]
        
        
        package = unpack(payload)

        return cls(cipher, tag, package)
