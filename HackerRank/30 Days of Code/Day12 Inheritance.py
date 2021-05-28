class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores

    def calculate(self):
        res=''
        avg=sum(scores)/len(scores)
        if 90<=avg<=100:res='O'
        elif 80<=avg<90:res='E'
        elif 70<=avg<80:res='A'
        elif 55<=avg<70:res='P'
        elif 40<=avg<55:res='D'
        else:res='T'

        return res

line=input().split()
firstName=line[0]
lastName=line[1]
idNum=line[2]
numScore=int(input())
scores=list(map(int,input().split()))

s=Student(firstName,lastName,idNum,scores)
s.printPerson()
print("Grade: ", s.calculate())

