import random
N = 0
alphabet = list('ATCG')
dna = [random.choice(alphabet) for i in xrange(N)]
dna = str(dna)

def generate_string(N, alphabet='ATCG'):
    return ''.join([random.choice(alphabet) for i in xrange(N)])
dna = generate_string(20)
st = "ACTG"
base = st[1:3]

def count_pairs(dna, base):
    i = 0
    for c in list(dna):
        if c == base:
            i+=1
    return i

def main():
    generate_string(N, alphabet='ATCG')
    count_pairs (dna, base)
d = count_pairs(dna, base)
main()
print "%s appears %d times in %s" %(base, d, dna)
