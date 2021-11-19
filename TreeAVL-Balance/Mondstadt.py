class MT:
    def __init__(self):
        self.tree = []
    
    def insert(self, data):
        self.tree.append(data)
    
    def sum(self):
        return sum(self.tree)

    def size(self):
        return len(self.tree)

    def compare(self, g1, g2):
        sg1 = self.tree[g1] + self.tree[2*g1+1] + self.tree[2*g1+2]
        sg2 = self.tree[g2] + self.tree[2*g2+1] + self.tree[2*g2+2]
        if sg1 > sg2:
            print("{}>{}".format(g1, g2))
        elif sg1 == sg2:
            print("{}={}".format(g1, g2))
        else:
            print("{}<{}".format(g1, g2))
    
inp, comp = input("Enter Input : ").split("/")
inp = [int(i) for i in inp.split(" ")]
comp = comp.split(",")
T = MT()
for i in inp:
    T.insert(i)
for i in range(30):
    T.insert(0)
print(T.sum())
for i in comp:
    num1, num2 = i.split(" ")
    T.compare(int(num1), int(num2))