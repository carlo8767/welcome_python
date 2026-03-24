import os.path
import string
import hashlib
from itertools import permutations
from coverage.execfile import os
from collections import Counter



#--------QUESTION ONE--------#

#--------1.a--------#
"""
Security_Engineering_-_A_Guide_to_Building_Dependable_Distributed_Systems
>> 1.a: Bob will not achieve full authenticity because it relies just on the
      verification of the message without taking into account the sender's genuineness.
      Alternatively, Bob must introduce a Digital Signature or Macs for obtaining authenticity.
"""

#--------1.bi 1.bii 1.biii--------#
"""
>> 1.bi: A hash function must be : Compressed, Efficient, and Secure.
       * Compressed
       The function satisfies the compressed definition because it maps an arbitrary input size
       to a valid digest. For instance,  the input b'\x33', which has a thirty-three-byte size, is
       successfully compressed, even though the SHA256 encryption algorithm has a 32-byte size.
       * Efficient
       The function hash_by_counting_repeating_bits is efficient because it hashes a plain text in a cipher with
       the function h.hexdigest(), which has time complexity of O(1)
       * Secure
        For instance the digest : 4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce is impossible to reverse.
        In fact try to find the input from the digest. That is, its computationally impossible.
       
>> 1.bii: The hash function has strong collision efficiency if we have a larger bucket. In fact, for evaluating a collision, we must take into account the input size and its possible permutations.
        For instance, if we said that the input is 5 numbers with a bucket size of 50.
        The probability will be:
         * Collision Formula collision: % 18.129692469 %
         Alternatively, if we have the same input size of 5 number  with a bucket of 100 , the collision probability will be:
        * Collision: Formula collision will result in % 9.516258196
          https: // kevingal.com / blog / collisions.html
          Piper, F., & Murphy, S. (2002). Cryptography. Oxford University Press. https://ebookcentral.proquest.com/lib/lancaster/detail.action?docID=4964351 page 61 Arbitrary chiper block
          Zoubir Z. Mammeri. (2024). Cryptography. Wiley. Here collision formula
        
"""
">> 1.biii"



#--------METHOD RUN 1.Biii --------#
def hash_by_counting_repeating_bits(message:bytes)-> hex:
    # COVERT BYTES TO BIT  https://realpython.com/python-bytearray/
    conversion = " ".join(format(byte, "08b") for byte in message)
    count = 0
    index=0
    while index < len(conversion)-1:
        if conversion[index] == conversion[(index+1)]:
            index+=1
            count+=1
        else:
            index += 1
    print(f'The repeating bits are : {count}')
    digest = hashlib.sha256(message).hexdigest()
    return  digest

hash_by_counting_repeating_bits(b'\x33')
hash_by_counting_repeating_bits(b'1000')


#--------METHOD RUN 1.ci, 1.cii 1.ciii --------#
"""
>> 1.ci: A valid strategy for  evaluating the plain text is to perform a dictionary attack. That is, with the 
         information related to the hash algorithm ( SHA-256) and the range of five input( lover-case letters of Latin alphabet) 
         We can:
         * Calculate the hash function and create in a dictionary hash table with k (digest value) and the plain text 
           for all the possible permutations.
         * Pass the digest value as key and find the corrisponding plain text.
        Hacking- The Art of Exploitation (2nd ed. 2008) - Erickson 422
        https://medium.com/@makmalsh/exploring-permutations-and-combinations-in-python-6079831e301f 422
   """

">> 1.cii:"

#--------MESSAGE Ciii--------#
def find_message_for_sha256_digest_value():
    table = permutations(string.ascii_lowercase,5)
    list_values = [ ''.join(n).encode('utf-8') for n in table]
    list_hask_key = [hashlib.sha256(m).hexdigest() for m in list_values]
    tables_decode = dict([(k,  v.decode('utf-8')) for k, v in zip(list_hask_key, list_values)])
    plain_text = tables_decode['47c5c28cae2574cdf5a194fe7717de68f8276f4bf83e653830925056aeb32a48']
    print(f'The message is {plain_text}')

find_message_for_sha256_digest_value()
"""

>> 1.ciii:
   The plain text decoded is "mouse"
"""

#--------QUESTION TWO--------#

#--------QUESTION 2.ai, 2.aii , 2.aiii--------#
"""
>> 2.ai: The block size must be at least 220 bits. In fact:
        * Input x formed with 26 uppercase letter, which a size of ASCII 
          of 8 bit each. Additionally, we have numbers [0..5], which are one bit for 0 and 1, two bits for 2 and 3, and three bits for 4 and 5.
          Total bits: (8*26) + ((1*2)+(2*2)(2*3)) = 220 bit. 
          That is, 220 bits of a vector of 32 pairwise disjoint characters.
          However, it's relevant to state that the block size might vary based on
          the encryption algorithm, such as 256 bit AES size
          
        Input X
        - 26 LETTER : size in ASCII for one letter 8 bit 
        [0...5] NUMBER = 0 1 I need one bit, 2 3 I need two bit, 4 5 I need 3 bit 
        - Key space: I have 32! permutations. The letter formed a 208 bit block
          ( 26 *8 bit) and the number formed a block of 12 bit. 
        The size of the block size can vary   base one on the block
        size select. In fact, the same disjoint pairs character, such as 
        ABCDEFGHILMNOPQRSTUVZ01235 might be  represented with a block of 220 bit. 
        However, I can as well represented with a block of 256 bit ( round size AES)
        So I need at least a block of 220 bit. 
        If we choose to use AES symmetric algorithm  and a block size of 16 bit 
        we can encrypt a block size  of 8 disjoint character (128 bit size AES divide 16 bit block) every block.
        Alternatively, if we choose a block size of 24 bit we can represent a pair of 5 disjoin character ( 128/ 24 bit)
        https://en.wikipedia.org/wiki/Advanced_Encryption_Standard ROUND SIZE 256 BIT KEYZ
        """

">> 2.aii"
def encrypt(x, k):
    table_encryption_values = table_encryption()
    plain_text_encryption = ''.join([k[int(table_encryption_values[n])] for n in x])
    return plain_text_encryption

def decrypt(y,k):
    table_decryption_values = table_decryption()
    plain_text_decrypt = ''.join([table_decryption_values[k.index(n)] for n in y])
    return plain_text_decrypt

def table_encryption():
    list_keys = list(string.ascii_uppercase+str('012345'))
    list_values = [x for x in range(0,len(list_keys))]
    pairs_key_values = dict([(k,v) for k, v in zip (list_keys,list_values)])
    return pairs_key_values

def table_decryption():
    list_values = list(string.ascii_uppercase + str('012345'))
    list_keys = [(x) for x in range(0, len(list_values))]
    pairs_key_values = dict([(k, v) for k, v in zip(list_keys, list_values)])
    return pairs_key_values

#--------METHOD 2aii-------#
print(encrypt(('A'), "BACDEFGHIJKLMNOPQRSTUVWXYZ325014"))
print(decrypt('BA','BACDEFGHIJKLMNOPQRSTUVWXYZ012345'))


"""
>>aiii: My approach works because I built an encryption table. That is, base on the x input 
        and the key, is calculate what is the output trough the index base on the x input 
        from the encryption table. In the same way, the decryption table calculate the index
        corrisponding to the input. 
"""


#--------QUESTION 2.bi, --------#
"""
>>bi The XOR operator is well integrated in the encryption and decryption phases 
     for improving the code efficiency and remove the necessity to create an encryption/decryption table. 
     In fact, XOR is the only logical operator that is return true if two values differ, and it can use in 
     dynamic with the plain text ( encryption) and cipher text (decrypiton) for finding the right answer. 
     My proposal is :
     1. Prepare a list of block cipher base on the input size. That is, if if the 
        input size is larger than the key space, it will separate the input base on the padding
     2. Encode the block cipher and the key space in a list of byte
     3. Perform  the XOR between input and the key space and extract the index
     4. With the index list and we can extract directly from they key vector the encrypted values.
     Additionally, I do not need anymore to create an encryption table and decryption table, because I can use
     the same method for decrypting the input. 

     In fact, in the encryption phase will be generate with:
     M ⊕ K = cipher text in binary, without expose the key every in the output. 
     In fact, the previous encryption scheme was returned in the output, and with the combination
     plain text and cipher is simple to discover the key
     A generates B
     B generates A
     CD generate CD
     In my function I will perform fist the ⊕ XOR  between M and K,
     and after I will calculate the left bit rotation for build an additional security levelÙ
     VERIFY IF I NEED THE LEFT ROTATE AND IF  THE CODE BLOCK REQUIRER TO STORE SOMEWHERE THE PREVIOUS BLOCK
"""

# CREATION BLOCH CIPHER
def block_cipher_creation(a, b)->list:
    result , padding_value = calculating_padding(a, b)
    if  result:
        block_ciper = block_cipher_split(a, b, padding_value)
        return block_ciper
    else:
        block_cipher = list()
        block_cipher.append(a)
        return block_cipher

# VERIFY IF WE HAVE TO CALCULATE THE PADDING
def calculating_padding(a, b):
    pad = len(a) % len(b)
    if pad == 0 or len(a) < len(b):
        return False, 0
    else:
        return  True, pad

# THE METHOD PREPARE THE BLOCK CIPHER AND SPLIT THE STRING BASE ON THE PADDING
def block_cipher_split(a, b, padding)-> list:
    block_cipher = list()
    original_value = a
    keep_pad = True
    values_padding = padding
    while keep_pad:
        # CREATE A SUBSTRING BASE ON THE STRING SIZE
        original_value =  original_value[0: values_padding]
        block_cipher.append(original_value)
        # VERIFY IF I STILL USE THE PADDING
        split_string = a.replace(original_value, "")
        keep_pad, values_padding = calculating_padding(split_string, b)
        # IF IT DOES NOT NEED THE PADDING STORE THE REST
        if not keep_pad:
            block_cipher.append(split_string)
    return  block_cipher



#--------QUESTION 2.bii--------#
"bii"
# MESSAGE AND CIPHER TEXT
def cw_xor ( a, b ) :
    # PREPARING THE BLOCK CIPHER
    block = block_cipher_creation(a, b)
    # CONVERT IN BYTE
    key_bytes = [ord(c) for c in b]
    values_bytes = [ord(c) for n in block for c in n]
    # PERFORM XOR AND KEY
    list_index = [i for x in values_bytes for i, val in enumerate(key_bytes) if x ^ val == 0]
    return list_index


#--------METHOD 2.bii --------#
index_values = cw_xor('A', 'BACDEFGHIJKLMNOPQRSTUVWXYZ325014' )
decryption = cw_xor('B', 'BACDEFGHIJKLMNOPQRSTUVWXYZ325014')


#--------QUESTION 2.biii --------#

"biii"

cipher_block = dict()
size_cipher = 0
def encrypt_cbc (m, k ) :
    global size_cipher, cipher_block
    key_space = list(string.ascii_uppercase + str('012345'))
    if size_cipher ==0:
        index_encryption = cw_xor(m, key_space)
        values_encrypted = ''.join(k[int(v)] for v in index_encryption)
        size_cipher+=1
        cipher_block[size_cipher-1] = values_encrypted
        return values_encrypted
    else:
        # TAKE IN ACCOUNT THE PREVIOUS BLOCK
        previous_cipher = cipher_block[size_cipher-1]
        c1_m1 = previous_cipher+m
        index_encryption= cw_xor(c1_m1, key_space)
        chain_block = ''.join(k[v] for v in index_encryption)
        size_cipher += 1
        cipher_block[size_cipher - 1] = chain_block
        return  chain_block

def decrypt_cbc(c, k):
    key_space = list(string.ascii_uppercase + str('012345'))
    for key, v in cipher_block.items():
         if v == c:
             if key ==0:
                 # EXCEPT FOR THE FIRST ONE
                 index_plain = cw_xor(c, key_space)
                 plaintext = ''.join(k[i] for i in index_plain)
                 return plaintext
             # FIND THE PREVIOUS WITH THE KEY SPACE
             else:
                index_plain = cw_xor(c, key_space)
                plaintext = ''.join(k[i] for i in index_plain)
                 # SUBSTITUTE
                previous_cipher = cipher_block[key-1]
                substitution = plaintext.replace(previous_cipher,"")
                return substitution
    return "not present"

#--------METHOD 2.biii --------#
print(encrypt_cbc('RBFEQEFEDFQFDFASDFUIOFUQOGEQWUFQGEDUFAGSDFOGADSFFASGDFAISFGIASDGF', 'BACDEFGHIJKLMNOPQRSTUVWXYZ325014')) # AA
print(encrypt_cbc('B', 'BACDEFGHIJKLMNOPQRSTUVWXYZ325014'))
print(decrypt_cbc('RAFEQEFEDFQFDFBSDFUIOFUQOGEQWUFQGEDUFBGSDFOGBDSFFBSGDFBISFGIBSDGF',  'BACDEFGHIJKLMNOPQRSTUVWXYZ325014'))
print(decrypt_cbc('RBFEQEFEDFQFDFASDFUIOFUQOGEQWUFQGEDUFAGSDFOGADSFFASGDFAISFGIASDGFA',  'BACDEFGHIJKLMNOPQRSTUVWXYZ325014'))
print(decrypt_cbc('RA',  'BACDEFGHIJKLMNOPQRSTUVWXYZ325014'))
print(decrypt_cbc('RBA',  'BACDEFGHIJKLMNOPQRSTUVWXYZ325014'))





#--------QUESTION 2.ci, 2cii, 2.ciii, 2ciiii --------#
"""
>>Ci
https://en.wikipedia.org/wiki/Frequency_analysis 
https://www.101computing.net/frequency-analysis/
"""

def relative_frequency_letter():
    path_file = os.path.join("./file", "LZSCC.252_25-26_CW_Q2c_ciphertext.txt")
    order_values = ""
    with (open(path_file) as f):
        order_values += f.read()
    size_values = len(order_values)
    dictionary_occurrence = dict()
    letter = ""
    for x in range(0, len(order_values)-1):
        count_occ = sum( 1 for n in order_values if n == order_values[x])
        calculation = (count_occ / size_values)
        dictionary_occurrence[order_values[x]] = (count_occ,calculation)
        "https://realpython.com/sort-python-dictionary/"
    dictionary_occurrence = dict(sorted(dictionary_occurrence.items(), key=lambda item: item[1], reverse=True))
    print(f"The relative frequency of letter is {dictionary_occurrence}")
    return dictionary_occurrence


relative_frequency_letter()
"""
>>Cii: We can analysed that the five top letters with largest occurrences in the cipher text are:
       ('Z', (78, 15.234375))
       ('A', (50, 9.765625)))
       ('U', (41, 8.0078125))
       ('M', (39, 7.6171875))
       ('R', (38, 7.421875))
       Comparing with the  five largest letter frequency in english we might formulate that :
        ('Z', (78, 15.234375)) --> Corresponds to the letter E 12.702 %
        ('A', (50, 9.765625))) --> Corresponds  to the letter T  9.056 %
        ('U', (41, 8.0078125))   --> Corresponds  to the letter A  8.167 %
        ('M', (39, 7.6171875))  --> Corresponds  to the letter O  7.507 %
        ('R', (38, 7.421875))  --> Corresponds  to the letter I  6.966 %
        ZZRMURVSZZDAUZZVBTZVU ---> Z->  E V-> T U->A
>>Ciii:
      The main limit of  the previous approach is that it does not evaluate the size of the message sent, and that in certain types of context, such as in a book or letter,
      The frequency of the message might vary (Ahmed, 2016)
      Alternatively, we can evaluate the probability distribution over the ciphertext, and in combination with the index of coincidence 
      we can determine the rate of substitution.
      Reference
      https://en.wikipedia.org/wiki/Index_of_coincidence
      Ahmed, S. N. (2016). Physics and engineering of radiation detection (2nd ed.). Elsevier.
"""

"""
>>Ciiii: The result of the index of coincidence illustrates that the ciphertext in a monoalphabetic cipher might be decrypted by verifying a common pattern. 
   Through the visual analysis and the relative frequency of the ciphertext, a common pattern is AUZ (12 occurrences).
    We can suppose that the CIPHER letter AUZ is THE. After that, we can use some simple words to detect ( see the method combination)
         https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
         .
 """

#-------CALCULATION INDEX OF COINCIDENCE-------#
def split_values(values, max_splits):
    max_split = len(values) / max_splits
    separator = 0
    letters = ""
    count_key = 0
    values_split = dict()
    for ns in range(0,len(values)):
        separator+=1
        letters+=values[ns]
        values_split[count_key] = letters
        if separator > max_split:
            separator =0
            count_key+=1
            letters = ""
    return  values_split

def index_coincidence():
    path_file = os.path.join("./file", "LZSCC.252_25-26_CW_Q2c_ciphertext.txt")
    values = ""
    with (open(path_file) as f):
        values += f.read()
    dictionary_coincidence = dict()
    for n in range(1,2):
        split_dictionary = split_values(values, n)
        dictionary_coincidence [n] = coincidence_grouping_dicti(split_dictionary)

def coincidence_grouping_dicti(split_dictionary):
    index_coincidence = 0
    dictionary_occurrence = dict()
    value_counted = ''
    for x, v in split_dictionary.items():
        sorted_item = sorted(v)
        length_word = len(sorted_item)
        for n in  sorted_item:
            if value_counted == n:
                continue
            else:
                value_counted = n
                count_occ = sum( 1 for p in sorted_item if p == value_counted)
                # PROBABILITY OF DRAW TWO LETTER OF THE SAME TYPE
                index_coincidence += (float(count_occ*(count_occ-1))) / float((length_word * (length_word-1)))
            # CALCULATE INDEX OF COINCIDENCE https://en.wikipedia.org/wiki/Index_of_coincidence
        print(f'The index of coincidence is {index_coincidence}')
        index_coincidence = 0
        value_counted = ''
        dictionary_occurrence[x] = (v,index_coincidence)

        "https://realpython.com/sort-python-dictionary/"
    dictionary_occurrence = dict(sorted(dictionary_occurrence.items(), key=lambda item: item[1], reverse=True))
    print(dictionary_occurrence)
    for key, values  in dictionary_occurrence.items():
        finals = (values, split_dictionary[key])
        return  finals
    return ""


#------- COMBINATION LETTER  #-------

def combination():
    path_file = os.path.join("./file", "LZSCC.252_25-26_CW_Q2c_ciphertext.txt")

    with open(path_file) as f:
        values = f.read()
    length = 2
    list_pattern = [values[i:i + length] for i in range(len(values) - length + 1)]
    counter = Counter(list_pattern)
    values_length_path = [(item, count) for item, count in counter.items() if count > 1]
    occurrence = sorted(values_length_path, key=lambda item: item[1], reverse=True)
    print(occurrence)
    # REPLACE THE LETTER

    replace = values.replace("AUZ", "the").replace("A", "t").replace("U", "h").replace("Z", "e").replace("M", "r").replace("K", 'n')
    print(replace)

    length = 2
    list_pattern = [replace[i:i + length] for i in range(len(replace) - length + 1)]
    counter = Counter(list_pattern)
    values_length_path = [(item, count) for item, count in counter.items() if count > 1]
    occurrence = sorted(values_length_path, key=lambda item: item[1], reverse=True)
    print(occurrence)

"""
>>ci
ABCDEFGHIJKLMNOPQRSTUVWXYZ
T         R         H____E 
Unfortunately, I was not able to decrypt further combinations. 
 """
"""
>>>"Cvi"  
In consideration that the cipher length is constant (26 letters ), if we had applied 
the cipher two times it would not make it harder to discover the key.
"""


combination()
index_coincidence()




