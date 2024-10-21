from Person import Person

class Student(Person):
    def __init__(self,name,nric,admin_no,test_mark,exam_mark):
        super().__init__(name,nric)
        self.__admin_no=admin_no
        self.__test_mark=float(test_mark)
        self.__exam_mark=float(exam_mark)
    def get_admin_no(self):
        return self.__admin_no
    def set_admin_no(self,admin_no):
        self.__admin_no=admin_no
    def get_test_mark(self):
        return self.__test_mark
    def set_test_mark(self,testmark):
        self.__test_mark=float(testmark)
    def get_exam_mark(self):
        return self.__exam_mark
    def set_exam_mark(self,exammark):
        self.__exam_mark=float(exammark)
    def compute_final_mark(self):
        final_mark=0.5*((self.get_exam_mark())+self.get_test_mark())
        return final_mark
    def __str__(self) :
        return f"Final Mark {self.compute_final_mark()} for test mark {self.get_test_mark()} and exam mark {self.get_exam_mark()}"