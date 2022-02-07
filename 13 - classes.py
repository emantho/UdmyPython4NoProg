from mimetypes import init


class Human: #By convenction names begin with capital letter
    def __init__(self, edad) -> None: #In this method can be include all golbal atributes
        self.edad = edad     

    def speak(self, message):
        print(f"Hello, I am a new object, my name is {message} and I am {self.edad} years old.")

eder = Human(35)
eder.speak("Eder")
#print(f"I am {eder.edad} years old")

emilia = Human(3)
emilia.speak("Emilia")
#print(f"I am {emilia.edad} years old" )

