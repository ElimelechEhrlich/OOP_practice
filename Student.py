class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def add_grade(self, grade): #→ adds a grade
        self.grade = grade
        self.grades.append(grade)

    def average(self):
        sum_of_all_grades = 0
        for i in range(len(self.grades)):
           sum_of_all_grades += self.grades[i]
        return sum_of_all_grades / len(self.grades)


    # def book(self):

           
gradesstudet1 = [90,80,100,70]
student1 = Student('elimelech ehrlich', gradesstudet1)
print (student1.grades)
print (student1.average())
student1.add_grade(100)
print (student1.grades)
print (student1.average())

           

