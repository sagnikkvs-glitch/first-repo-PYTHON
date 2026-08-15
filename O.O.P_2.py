# the following is normal constructor
class Playlist:
    def __init__(self):
        self.name = "My Mix"

p = Playlist()    # __init__ fires here automatically
print(p.name)     # My Mix

# parameterized constructor  ??
# A parameterized constructor is an _init_ that accepts extra arguments so each new object can be customized at birth.
#  Instead of every object starting with the same hard-coded values, you pass in specific data when you create the object.

class Playlist:
    def __init__(self, name, genre):
        self.name  = name
        self.genre = genre
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

rock_mix = Playlist("Road Trip Mix", "Pop")
# Output: Playlist 'Road Trip Mix' (Pop) is ready!

# default  attribute initialization
#  for eg.. every bank acc starts with a default 0 money
# or until ya add a sing the song shows notinh

class Playlist:
    def __init__(self, name, genre):
        self.name  = name       # from parameter
        self.genre = genre      # from parameter
        self.songs = []         # default — always starts empty

p1 = Playlist("Road Trip Mix", "Pop")
p2 = Playlist("Study Beats",   "Lo-fi")
# p1.songs and p2.songs are completely separate lists


# destructors  syntax: __del__(self):  
# a space, double underscore, del, double underscore, self in parentheses, colon
# del can also be used to delete an obj and also show a printing message

class Playlist:
    def __init__(self, name, genre):
        self.name  = name
        self.genre = genre
        self.songs = []

    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")

my_mix = Playlist("Road Trip Mix", "Pop")
del my_mix   # triggers __del__ immediately
# Output: Playlist 'Road Trip Mix' has been deleted. Goodbye!


        # Object Life Cycle: 1. Creation  2. Usage  3. Destruction

# Phase 1 — Birth
my_song = Playlist("paar aab jo aegi tu", "hindi")
# __init__ fires: name, genre, songs=[] set up

# Phase 2 — Life
my_song.append("sage")
my_song.display()

# Phase 3 — Death
del my_song
# __del__ fires: Playlist 'Road Trip Mix' has been deleted. Goodbye!


# ________________________________________________________________________________________________________________________________

#  MENU DRIVEN OBJECT  ORIENTED PROGRAMMING??
# A menu-driven OOP program combines a class (with constructor, methods, and destructor) with a while True loop that shows the user numbered options. 
# USER selects the option and system calls the right method depending on their choice. 
# The class handles the data; the menu handles the interaction.

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print("Account created")

    def deposit(self):
        x = int(input("Enter amount to deposit: "))
        self.balance += x
        print("Money deposited")
    
    def withdraw(self):
        x = int(input("Enter amount to withdraw: "))
        self.balance -= x
        print("Money withdrawed")
       
    def show_balance(self):
        print("Balance:", self.balance)

    def __del__(self):
        print("Account closed")

abc= input("enter your name pls to make the bank account:")
acc = BankAccount(abc)

while True:
    print("WHAT U WANT TO DO NEXT ")
    print ("1. Deposit 2. Balance 3. close account 4. withdraw")
    choice = input("Choose: ")

    if choice == "1":
        acc.deposit()
        
    elif choice == "2":
       print(f"You '{acc.name}' have INR.{acc.balance}")
        
    elif choice == "3":
        del acc
        break

    elif choice =="4":
        acc.withdraw()



