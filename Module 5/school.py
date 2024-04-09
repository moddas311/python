class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
        
    def __repr__(self) -> str:
        return f'Student name with: {self.name}, class: {self.current_class}, id: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.subject} Departmend id: {self.id}'
    
class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
        
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
        
    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is inrolled with id: {id}, extra money: {fee - 6500}'
        
    def __repr__(self) -> str:
        print('Welcome to', self.name)
        
        print('-----OUR TEACHERS-----')
        for teacher in self.teachers:
            print(teacher)
            
        print('-----OUR STUDENTS-----') 
        for student in self.students:
            print(student) 
            
        return 'All done for now'
        
        
ali = Student('Ali', 10, 100)
sahabuddin = Teacher('Sahabuddin', 'Phycal Exercise & Health', 10)

# print(ali)
# print(sahabuddin)

phitron = School('Phitron')
phitron.enroll('Alia', 5200)
phitron.enroll('Junaid', 8000)
phitron.enroll('Sujon', 6500)
phitron.enroll('Mamun', 7000)
phitron.enroll('Arnob', 6700)

phitron.add_teacher('Rahat Khan Pathan', 'C')
phitron.add_teacher('Ramjan Ali', 'C++')
phitron.add_teacher('Abullah All Naim', 'DS')
phitron.add_teacher('Rtin Bhai', 'Algo')

print(phitron)