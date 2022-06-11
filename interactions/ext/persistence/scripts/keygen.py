from random import choice

HEX_ALPHABET = "0123456789ABCDEF"
def generate_key(): 
    print(
    "Random 32 character key: " +
    "".join(choice(HEX_ALPHABET) for _ in range(32))
    )