#부모클래스: 공통 코드를 준비 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식클래스: 보다 구체적으로 구현
class Student(Person):
    #덮어쓰기(override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))     
        print("Info(학과:{0}, 학번: {1})".format(
            self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo() 


