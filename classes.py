# 클래스

class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False
    
    def study(self):
        print(f"{self.name} 학생은 공부 중")

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'{student_1.major}가 {new_major}로 변경됨')

# 인스턴스 - 실체화된 사물

student_1 = Student('현진', '컴퓨터')

student_1.edit_major('기계')
print(student_1.major)

print(student_1) # <__main__.Student object at 0x0000022C22E1FFD0> 객체가 잘 만들어 졌다는 뜻
print(student_1.name)

student_1_graduated = student_1.is_graduated
print(student_1_graduated)

student_1.study()

#상속
class ForeignStudent(Student):
    def __init__(self, name, major, country):
        super().__init__(name, major)
        self.country = country

foreignstudent1 = ForeignStudent('name','Comp. Sci.','Japen')
print(foreignstudent1.name)
print(foreignstudent1.major)
print(foreignstudent1.country)
print(foreignstudent1.is_graduated)