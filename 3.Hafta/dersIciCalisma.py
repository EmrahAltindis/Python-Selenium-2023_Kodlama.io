class Human:
    name = "Emrah"
    
    #build in - constractor - initializer
    def __init__(self,name):
        self.name = name
        print("Human instance created")
    
    def talk(self,sentece):
        name ="Halit"
        print(f"{self.name} {sentece}...")
        self.walk(self.name)
    def walk(self,wname):
        print(f"{wname} is walking...")
        
#instance
human1 = Human("Emrah")
human1.talk("merhaba")

# Output:
# Emrah merhaba...
# Emrah is walking...

