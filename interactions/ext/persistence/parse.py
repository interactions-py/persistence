from json import loads
from .error import ParseError


def unpack_string(with_brackets):
    return with_brackets[1:1]


payload_types = {
    "(": str,
    "[": loads,
    "{": loads,
}


class PersistentCustomID:
    def __init__(self, tag: str, payload: dict | list | str):
        self.tag: str = tag
        for bracket in payload_types:
            if bracket in self.tag:
                raise ParseError
        if isinstance(payload, (dict, list)):
            self._payload = payload
        else:
            self._payload = f"({payload})"

    @property
    def packed(self) -> str:
        return f"persistence_{self.tag}{self._payload}"

    def __str__(self):
        return self.packed

    @property
    def package(self) -> dict | list | str:
        if self._payload[0] == "{":
            return loads(self._payload)
        if self._payload[0] == "[":
            return loads(self._payload)
        return self._payload.strip("()")

    @classmethod
    def from_string(cls, string: str):
        string = string.removeprefix("persistence_")
        print("string is", string)
        bracket_indexes = []
        for bracket in payload_types:
            try:
                bracket_indexes.append(string.index(bracket))
            except:
                pass
        payload_start = min(bracket_indexes)
        tag = string[:payload_start]
        print("TAG IS:", tag)
        payload = string[payload_start:]
        return cls(tag, payload)
