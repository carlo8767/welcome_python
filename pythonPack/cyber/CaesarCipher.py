import string as st
import heapq as hg
class Caesar:


    def init_alphabet_lover(self):
        return list(st.ascii_lowercase)

    def init_alphabet_upper(self):
        return list(st.ascii_uppercase)

    def convert_to_ASCII(self, value):
        return [ord(x) for x in value]

    # RETURN STRING KEY AND ENCRYPTED VALUES
    def table_encrytpion(self,  keys,  listAlphabet):

        tables_encryption = {x: chr(ord(x)+keys) for x in listAlphabet}
        return tables_encryption

        # RETURN AN ENCRYPTION TABLE WITH ASCCI AND ENCRYPTION


    def decryption_table(self , plaintTextASCCI):
        return { v:  bytearray([k]).decode()  for  k, v in plaintTextASCCI.items()}


    def solutions(self, rotation_number):
        plainToCipher = {}
        cipherToPlain = {}
        sizeOfAlphabet = len(st.ascii_letters)
        for i in range(sizeOfAlphabet):
            plainChar = st.ascii_letters[i]
        cipherChar = st.ascii_letters[(i + rotation_number) % sizeOfAlphabet]
        plainToCipher[plainChar] = cipherChar

        cipherToPlain[cipherChar] = plainChar
        return (plainToCipher, cipherToPlain)





if __name__ == '__main__':

    hello = Caesar()
    hello.solutions(10)
    list_alphabet = hello.init_alphabet()
    letter = "A"
    nd = ord(letter)+10
    sn = chr(nd)
    table  = hello.table_encrytpion(10, list_alphabet)


    """"
    ns = ord(letter)+10
    decode = chr(ns)
    decodeTwo = bytearray([ns]).decode()
    list_values  = list()
    hg.heappush(list_values, ( 0, "A"))
    hg.heappush(list_values, (8, "B"))
    print(list_values)
    k,v  = hg.heappop(list_values)

    
    
    
    """