


if __name__ == '__main__':

    unsigned  = 3
    x = b'\x10'
    txt = "My name is Ståle"
    x = txt.encode(encoding='ASCII')
    y = int.from_bytes(x, byteorder='little', signed=False)
    print(type(x), x)
    print(type(y), y)
    # The outcome is 16 because 10 is hexedecimal is 16

    # Convert integer to bytes MAX REPRESENTATION 256
    x = 256
    y = x.to_bytes(byteorder='little', signed=False, length=2)
    print(x, y)
    print(type(x), type(y))

    # Little Indian
    x = b'\x01\x03'
    y = int.from_bytes(x, byteorder='little', signed=False)
    z = int.from_bytes(x, byteorder='big', signed=False)
    print(x, y, z)
    print(bin(y), bin(z))

    # Sign and unsigned
    x = b'\x80'
    y = int.from_bytes(x, byteorder='little', signed=False)
    z = int.from_bytes(x, byteorder='little', signed=True)
    print(x, y, z)