class parrot:
    species="bird"

    def __init__(self, n, a):
        self.name, self.age = n, a

p=parrot("blu", 10)
print(p.species, p.name, p.age)
