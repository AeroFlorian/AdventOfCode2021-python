input = """BVBNBVPOKVFHBVCSHCFO

SO -> V
PB -> P
HV -> N
VF -> O
KS -> F
BB -> C
SH -> H
SB -> C
FS -> F
PV -> F
BC -> K
SF -> S
NO -> O
SK -> C
PO -> N
VK -> F
FC -> C
VV -> S
SV -> S
HH -> K
FH -> K
HN -> O
NP -> F
PK -> N
VO -> K
NC -> C
KP -> B
CS -> C
KO -> F
BK -> N
OO -> N
CF -> H
KN -> C
BV -> S
OK -> O
CN -> F
OP -> O
VP -> N
OC -> P
NH -> C
VN -> S
VC -> B
NF -> H
FO -> H
CC -> B
KB -> N
CP -> N
HK -> N
FB -> H
BH -> V
BN -> N
KC -> F
CV -> K
SP -> V
VS -> P
KF -> S
CH -> V
NS -> N
HS -> O
CK -> K
NB -> O
OF -> K
VB -> N
PS -> B
KH -> P
BS -> C
VH -> C
KK -> F
FN -> F
BP -> B
HF -> O
HB -> V
OV -> H
NV -> N
HO -> S
OS -> H
SS -> K
BO -> V
OB -> K
HP -> P
CO -> B
PP -> K
HC -> N
BF -> S
NK -> S
ON -> P
PH -> C
FV -> H
CB -> H
PC -> K
FF -> P
PN -> P
NN -> O
PF -> F
SC -> C
FK -> K
SN -> K
KV -> P
FP -> B
OH -> F"""

input_test = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def answer_for_range(iterations):
    global input
    input_list = input.split('\n')
    input_chain = input_list[0]
    relations = [x.split(" -> ") for x in input_list if len(x.split(" -> ")) == 2]
    d = {}
    for x in relations:
        d[x[0]] = x[1]
    followed_by = {}
    for x in range(len(input_chain) - 1):
        if input_chain[x] not in followed_by.keys():
            followed_by[input_chain[x]] = {}
        if input_chain[x+1] not in followed_by[input_chain[x]].keys():
            followed_by[input_chain[x]][input_chain[x+1]] = 0
        followed_by[input_chain[x]][input_chain[x + 1]]+=1
    for index in range(iterations):
        next_followed_by = {}
        for x,y in followed_by.items():
            if x not in next_followed_by.keys():
                next_followed_by[x] = {}
            for i in y:
                if x+i in d.keys():
                    if d[x+i] not in next_followed_by[x].keys():
                        next_followed_by[x][d[x + i]] = 0
                    next_followed_by[x][d[x+i]] += y[i]
                    if d[x+i] not in next_followed_by.keys():
                        next_followed_by[d[x+i]] = {}
                    if i not in next_followed_by[d[x+i]].keys():
                        next_followed_by[d[x+i]][i] = 0
                    next_followed_by[d[x + i]][i] += y[i]
        followed_by = next_followed_by

    min_element = -1
    max_element = -1
    for x,y in followed_by.items():
        count = 0
        for i,j in y.items():
            count +=j
        if input_chain[-1] == x:
            count+=1
        if count < min_element or min_element == - 1:
            min_element = count
        if count > max_element or max_element == - 1:
            max_element = count

    return max_element-min_element



def first_star():
    print(f"First star: {answer_for_range(10)}")

def second_star():
    print(f"Second star: {answer_for_range(40)}")


if __name__ == '__main__':
    first_star()
    second_star()
