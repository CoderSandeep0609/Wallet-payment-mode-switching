
class UnderageStudentError(Exception):
    def __init__(self,message):
        self.message=message
    
    def __str__(self):
        return self.message
class InvalidMarksError(Exception):
    def __init__(self,message):
        self.message=message
    
    def __str__(self):
        return self.message
class DuplicateRollError(Exception):
    def __init__(self,message):
        self.message=message
    
    def __str__(self):
        return self.message
class InvalidExamDataError(Exception):
    def __init__(self,message):
        self.message=message
    
    def __str__(self):
        return self.message

class Student:
    roll_no_registry=[]
    def __init__(self,name,roll_no,age):
        if type(age)!=int:
            raise ValueError('Age would be in numeric')
        if roll_no in Student.roll_no_registry:
            raise DuplicateRollError('Roll no already exists')
        else:
            self.roll_no=roll_no
            Student.roll_no_registry+=[self.roll_no]
        if age < 10:
            raise UnderageStudentError(f'under {age} age is not allowed')
        else:
            self.name=name
            self.age=age
class Exam:
    def __init__(self,subject,date,maximum_marks):
        self.subject=subject
        self.date=date
        if maximum_marks <0 or type(maximum_marks) != int:
            raise InvalidExamDataError('Invalid marks: it would be intiger or non-negative')
        else:
            self.maximum_marks=maximum_marks
class QuizEvaluator:
    def __init__(self,student,exam,marks_score):
        self.student=student
        self.exam=exam
        if marks_score <0 or marks_score > self.exam.maximum_marks:
            raise InvalidMarksError('Quiz marks invalid')
        else:
            self.marks_score=marks_score
    def evaluate(self):
        percentage=(self.marks_score/self.exam.maximum_marks)*100
        if percentage <40:
            print(f'Fail:::{percentage}')
        else:
            print(f'Pass::{self.student.name} score {percentage}')
try:
    s1=Student('sandeep',9013,19)
    s2=Student('sandeep',9013,19)
    exm=Exam('python','12/11/2015',100)
    quiz=QuizEvaluator(s1,exm,80)
    quiz=QuizEvaluator(s2,exm,80)
except ValueError as e:
    print(e)
except UnderageStudentError as e:
    print(e)
except DuplicateRollError as e:
    print(e)
except InvalidExamDataError as e:
    print(e)
except InvalidMarksError as e:
    print(e)
except Exception as e:
    print(e)
else:
    quiz.evaluate()
finally:
    print('Exam over')


