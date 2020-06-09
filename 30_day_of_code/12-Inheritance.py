from statistics import mean
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
 
    def __init__(self,fName, lName, idNum, scores):
        super().__init__(fName, lName, idNum)
        self.scores = scores
    
    def calculate(self):
        avg = mean(self.scores)
        if avg>=90 and avg<=100:
            return "O"
        elif avg>=80:
            return "E"
        elif avg>=70:
            return "A"
        elif avg>=55:
            return "P"
        elif avg>=40:
            return "D"
        else:
            return "T"
   
    

  
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())