# 사람을 나타내는 Person 클래스 정의
class Person:
    def __init__(self, id, name):
        # id와 이름을 설정하는 생성자
        self.id = id
        self.name = name
    
    def printInfo(self):
        # id와 이름을 출력하는 메서드
        print(f"ID: {self.id}, Name: {self.name}")

# 관리자를 나타내는 Manager 클래스 정의 (Person 클래스를 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        # 상위 클래스인 Person의 생성자를 호출하여 id와 이름을 설정
        super().__init__(id, name)
        # 추가로 직함을 설정
        self.title = title
    
    def printInfo(self):
        # 상위 클래스의 printInfo를 호출하여 id와 이름을 출력
        super().printInfo()
        # 추가로 직함을 출력
        print(f"Title: {self.title}")

# 직원을 나타내는 Employee 클래스 정의 (Person 클래스를 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        # 상위 클래스인 Person의 생성자를 호출하여 id와 이름을 설정
        super().__init__(id, name)
        # 추가로 기술을 설정
        self.skill = skill
    
    def printInfo(self):
        # 상위 클래스의 printInfo를 호출하여 id와 이름을 출력
        super().printInfo()
        # 추가로 기술을 출력
        print(f"Skill: {self.skill}")

# 각 클래스를 테스트하는 함수 정의
def test_classes():
    # Person 클래스 테스트
    person1 = Person(1, "Alice")  # id가 1이고 이름이 Alice인 사람 생성
    person1.printInfo()  # 정보 출력
    
    person2 = Person(2, "Bob")  # id가 2이고 이름이 Bob인 사람 생성
    person2.printInfo()  # 정보 출력

    # Manager 클래스 테스트
    manager1 = Manager(3, "Charlie", "HR Manager")  # id가 3이고 이름이 Charlie이며 직함이 HR Manager인 관리자 생성
    manager1.printInfo()  # 정보 출력
    
    manager2 = Manager(4, "Diana", "IT Manager")  # id가 4이고 이름이 Diana이며 직함이 IT Manager인 관리자 생성
    manager2.printInfo()  # 정보 출력

    # Employee 클래스 테스트
    employee1 = Employee(5, "Eve", "Python")  # id가 5이고 이름이 Eve이며 기술이 Python인 직원 생성
    employee1.printInfo()  # 정보 출력
    
    employee2 = Employee(6, "Frank", "Java")  # id가 6이고 이름이 Frank이며 기술이 Java인 직원 생성
    employee2.printInfo()  # 정보 출력

    # 추가 테스트
    manager3 = Manager(7, "Grace", "Marketing Manager")  # id가 7이고 이름이 Grace이며 직함이 Marketing Manager인 관리자 생성
    manager3.printInfo()  # 정보 출력

    employee3 = Employee(8, "Heidi", "JavaScript")  # id가 8이고 이름이 Heidi이며 기술이 JavaScript인 직원 생성
    employee3.printInfo()  # 정보 출력

    person3 = Person(9, "Ivan")  # id가 9이고 이름이 Ivan인 사람 생성
    person3.printInfo()  # 정보 출력

    manager4 = Manager(10, "Judy", "Sales Manager")  # id가 10이고 이름이 Judy이며 직함이 Sales Manager인 관리자 생성
    manager4.printInfo()  # 정보 출력

# 테스트 실행
test_classes()
