import os.path



def index_coincidence ():
    path_file = "/home/robothg/PycharmProjects/welcome_python/pythonPack/cyber/coursework/file/LZSCC.252_25-26_CW_Q2c_ciphertext.txt"
    values = ""
    with (open(path_file) as f):
        values += f.read()
    group = length_keyword(values, 3)
    coincidence_grouping_dicti(group)
# CALCULATE LENGTH KEYWORDS

def length_keyword(values):
    dictionary_group  = {0:list(), 1:list(), 2:list(), 3:list()}
    # GROUPING LETTER SIZE
    index = 0
    for v in values:
        dictionary_group[index].append(v)
        index += 1
        if index > 3:
            index =0

    return dictionary_group

def coincidence_grouping_dicti(group):
    index_coincidence = 0
    dictionary_occurrence = dict()
    value_counted = ''
    for x, v in group.items():
        sorted_item = sorted(v)
        length_word = len(sorted_item)
        # ERROR HERE
        for n in  sorted_item:
            if value_counted == n:
                continue
            else:
                value_counted = n
                count_occ = sum( 1 for p in sorted_item if p == value_counted)
                # PROBABILITY OF DRAW TWO LETTER OF THE SAME TYPE
                index_coincidence += (float(count_occ*(count_occ-1))) / float((length_word * (length_word-1)))
            # CALCULATE INDEX OF COINCIDENCE CARLO https://en.wikipedia.org/wiki/Index_of_coincidence
        # INDEX OF COINCIDENCE : # 0.0718948752446184 It likely
        value_counted = ''
        dictionary_occurrence[x] = (index_coincidence)

        index_coincidence = 0
    print(dictionary_occurrence)
    average = 0
    for kk, vv in dictionary_occurrence.items():
        average+= float(vv)
    average_index = average/ 4
    print(average_index)
    print(group[3])

    # CALCULATE THE SUM:
    only_values = [x for x in group[3]]
    list_combining = list()
    count = 0
    set_count = set()
    for nss in only_values:
        if nss in set_count:
            continue
        for ts in group[3]:
            if ts == nss:
                count+=1
        set_count.add(nss)
        print(f'{nss} numbers {count}')
        count = 0

index_coincidence()


"""
Group first R 16 Z 16 
Group Second  Z 16 T 
Group with key size 3
{0: 0.07334021327829376, 1: 0.07093223254213965, 2: 0.06877828054298643}
0.07101690878780662

Group with key size 4
{0: 0.0749261811023622, 1: 0.06299212598425195, 2: 0.06938976377952756, 3: 0.08329232283464566}
AVERAGE 0.07265009842519685

Group with key size 5
{0: 0.0805254140491148, 1: 0.0774795355035218, 2: 0.0681421083284799, 3: 0.0708600271791885, 4: 0.0671714230246554}
0.07283570161699207 average

Group with key size 6
{0: 0.07715458276333789, 1: 0.07441860465116279, 2: 0.06330532212885154, 3: 0.07198879551820728, 4: 0.07198879551820728, 5: 0.07310924369747898}
0.07199422404620763 average 
  ('Z', (78, 15.234375)) --> Corresponds to the letter E 12.702 %
        ('A', (50, 9.765625))) --> Corresponds  to the letter T  9.056 %
        ('U', (41, 8.0078125))   --> Corresponds  to the letter A  8.167 %
        ('M', (39, 7.6171875))  --> Corresponds  to the letter O  7.507 %
        ('R', (38, 7.421875))  --> Corresponds  to the letter I  6.966 %
I can assume that it should strongest ist the group with size 4 3: 0.08329232283464566}
The couunter of word find
K numbers 7 -> F
R numbers 8 -> J
Z numbers 26 --> Assuming is  E
E numbers 1 
N numbers 2
W numbers 5
Y numbers 4
L numbers 2
H numbers 3
B numbers 6
U numbers 15 --> P
X numbers 9 --> S
A numbers 8
T numbers 8
O numbers 1
V numbers 5
S numbers 6
M numbers 10 -> H
D numbers 1
G numbers 1
"""
partion =['K', 'R', 'Z',
 'E','N', 'W', 'Y', 'L',
 'L', 'H', 'H', 'Z',
 'R', 'B', 'U', 'X',
 'U', 'A', 'T', 'W',
 'K', 'B', 'U', 'Z',
 'N', 'T', 'Y', 'Z',
 'U', 'U', 'Y', 'U',
 'Z', 'Z', 'O', 'H',
 'U', 'V', 'T', 'S',
'M', 'B', 'T', 'T',
 'W', 'W', 'A', 'R',
 'V', 'D', 'Z', 'Z',
 'V', 'S', 'R', 'X',
 'B', 'U', 'X', 'M',
 'A', 'Z', 'M', 'X',
 'Z', 'U', 'V', 'Z',
 'B', 'W', 'A', 'R',
 'S', 'U', 'K', 'K',
 'V', 'U', 'A', 'K',
 'M', 'Z', 'X', 'M',
 'Z', 'M', 'S', 'Z',
 'Z', 'X', 'X', 'R',
 'Z', 'S', 'Z', 'T',
 'A', 'K', 'Z', 'Y',
 'T', 'U', 'A', 'K',
 'R', 'U', 'B', 'M',
 'Z', 'R', 'U', 'G',
 'M', 'U', 'Z', 'M',
 'X', 'M', 'Z', 'T',
 'Z', 'Z', 'Z', 'A',
 'Z', 'X', 'S', 'Z']




def index_coincidence_partition ():
    group = length_keyword(partion, 3)
    coincidence_grouping_dicti(group)
# CALCULATE LENGTH KEYWORDS
"""
Z IS E 100
U 


"""