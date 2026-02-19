




if __name__ == '__main__':
    a = 3 # 0011
    b =5  # 0101
    print(a ^  b) # 0110

    wordOne = b"a"
    wordTwo = b"B"
    # wordOneEncode = wordOne.encode("utf-8")
    values = bytearray()
    values.append(wordOne[0])
    values.append(wordTwo[0])
    print(values)