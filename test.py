ls = ['a', 'b', 'c', 'd', 'e']

i = 0
while i < len(ls):
    if ls[i] == 'b':
        ls.pop(i)
    else:
        print(ls[i])
        i += 1


class C:
    def __init__(self):
        try:
            self.x
        except:
            print("hello")


C()


G = C

G()
del ls[1]
print(ls)
