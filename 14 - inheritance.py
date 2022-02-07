from mimetypes import init

class Human: #By convenction names begin with capital letter
    def __init__(self, edad) -> None: #In this method can be include all golbal atributes
        self.edad = edad     

    def speak(self, message):
        print(f"Hello, I am a new object, my name is {message} and I am {self.edad} years old.")

class SystemEng(Human):
    
    def programming(self, language):
        print(f"I'm programming in {language}")

class lawyer(Human):

    def studyCase(self, case):
        print(f"Must study the case of {case}")

eder = SystemEng(35)
eder.speak("Eder")
eder.programming("python")

emilia = lawyer(29)
emilia.speak("Emilia")
emilia.studyCase("Papá")
