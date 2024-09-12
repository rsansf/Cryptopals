hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

def fixed_xor(input1, input2):
    b1 = bytearray(bytes.fromhex(hex1))
    b2 = bytearray(bytes.fromhex(hex2))
    print(b1)
    print(b2)
    if len(b1) != len(b2):
        raise Exception("input lengths are not equal")
    output = bytearray(len(b1))
    for i in range(0, len(b1)):
        output[i] = b1[i] ^ b2[i]
    return bytes(output)

print(fixed_xor(hex1, hex2))
