from mimetypes import init

class Human: #By convenction names begin with capital letter
    def __init__(self, edad) -> None: #In this method can be include all golbal atributes
        self.edad = edad     

    def speak(self, message):
        print(f"Hello, I am a new object, my name is {message} and I am {self.edad} years old.")

class SystemEng(Human): #SystemEng inherits all from Human
    
    def programming(self, language):
        print(f"I'm programming in {language}")

'''class System(Human): #SystemEng inherits some methods from Human, but has it own __init__
    def __init__(self):
        pass

    def programming(self, language):
        print(f"I'm programming in {language}")'''

class lawyer(Human): #Lawyer inherits all from Human

    def studyCase(self, case):
        print(f"I'm going to study the case of {case}")

'''class studious(SystemEng, lawyer): #order of inheritance affects in which has __init__
    pass #Using "pass" this class will use all methods from the upper classes'''

class studious(SystemEng, lawyer): #order of inheritance affects in which has __init__
    pass

diana = studious(36)
diana.speak("Diana")
diana.programming("Pearl")
diana.studyCase("Aracataca")
