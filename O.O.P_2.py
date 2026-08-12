class playlist:
    def __init__(self, n, g):
        self.n, self.g, self.s = n , g , []
    def add(self, x):
        self.s.appens(x)
    def remove(self,x):
        if x in self.s:
            self.s.remove(x)
    def show(self):
        print(self.n, self.g, *self.s, sep="\n")
    def __del__(self):
        print("deleted")

p= playlist("road trip  mix ", "pop")

while 1:
    c=input("1. add 2.remove 3. veiw 4. exit  ")
    if c=="1":
        p.add(input("song: "))
    elif c==2:
        p.remove(input("song: "))
    elif c== "2":
        p.show()
    elif c== "4":
        del p 
        break