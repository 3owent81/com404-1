class Person:
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield
        
    def display_name(self):
        print("I am {}.".format(self.name))
    
    def display_age(self):
        print("I am {} years old.".format(self.age))

    def display_energy(self):
        print("My energy level is {}%".format(self.energy))

    def display_shield(self):
        print("My shield level is {}%".format(self.shield))

    def display_summary(self):
        print("I am {}. I am {} years old. My energy level is {}% and shield is {}%".format(self.name, self.age, self.energy, self.shield))

    def __str__(self):
        return

bot = Person("bot", 34, 85, 50)
bot.display_name()
bot.display_age()
bot.display_energy()
bot.display_shield()
bot.display_summary() 
