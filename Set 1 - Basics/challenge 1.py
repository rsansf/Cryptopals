import base64

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_base64(input):
    return base64.b64encode(bytes.fromhex(input))

print(hex_to_base64(hex))
