# School

# Make a class structure in python representing people at school. Make a base class called Person, a class called Student, and another one called Teacher. 
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not. 
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person():
    def __init__(self, name, age, place_of_living):
        self.name = name
        self.age = age
        self.pleace_of_living = place_of_living
    
    def person_info(self):
        print(f'The name is {self.name}, age -- {self.age}')


class Student(Person):
    def __init__(self, name, age, place_of_living, year, discipline):
        super().__init__(name, age, place_of_living)
        self.studing_year = year
        self.discipline = discipline
    
    def student_info(self):
        graduation = 6 - self.studing_year + 2023
        print(f'{self.name} should be graduated in {graduation} as Master in {self.discipline}')

class Teacher(Person):
    def __init__(self, name, age, place_of_living, disciplins: list, degree):
        super().__init__(name, age, place_of_living)
        self.disciplins = disciplins
        self.degree = degree

    def teacher_info(self):
        print(f'{self.name} is a very good specialist in {self.disciplins}. He got {self.degree}!')


person1 = Person('James Brown', 55 , 'New York')
student1 =Student('James Brown', 55 , 'New York', 3, 'Applied Science')
teacher1 =Teacher('John Randson', 77 , 'York', ['Math', 'Physics'], 'PhD')

student1.person_info()
teacher1.person_info()

student1.student_info()
teacher1.teacher_info()


