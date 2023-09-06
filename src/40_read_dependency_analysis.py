import Cabocha

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show(self):
        print(self.surface, self.base, self.pos, self.pos1)

path = 'neko.txt.cabocha'
with open(path) as f:
    text = f.read().split('\n')
result = []
morphs = []
for line in test[:-1]:
    if line == 'EOS':
        result.append(morphs)
        morphs = []
    elif line[0] == '*':
        continue
    else:
        ls = line.split('\t')
        d = {}
        tmp = ls[1].split(',')
        morph = Morph(ls[0], tmp[6], tmp[0], tmp[1])
        morph.append(morph)
for morphs in result[2]:
    morphs.show()
