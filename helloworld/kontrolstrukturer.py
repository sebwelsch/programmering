alias = None
enemy = None
greeting = None

user = input("What is your name, user? ")

if user == "Bruce Wayne":
    alias = "Batman"
    enemy = "The Joker"
    greeting = "You are the hero Gotham deserves, but not the one it needs right now."
elif user == "Katniss Everdeen":
    alias = "Mockingjay"
    enemy = "President Snow"
    greeting = "May the odds be ever in your favour!"
elif user == "Peter Parker":
    alias = "Spiderman"
    enemy = ""
    greeting = "D"
elif user == "Bruce Banner":
    alias = "Hulk"
    enemy = ""
    greeting = "D"
elif user == "Tony Stark":
    alias = "Jernmanden"
    enemy = ""
    greeting = "D"
elif user == "Alan Scott":
    alias = "The Green Lantern"
    enemy = "Thaal Sinestro"
    greeting = "D"
else:
    alias = "programmer"
    enemy = "the compiler"
    greeting = "You are the 1%."

print("Greetings {}. {} Good luck defeating {}.".format(alias, greeting, enemy))
