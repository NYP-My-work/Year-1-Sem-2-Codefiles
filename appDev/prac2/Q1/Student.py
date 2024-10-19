from Person import Person

class Student(Person):
    def ___init__(self,name,nric,admin_no,test_mark,exam_mark):
        super().__init(name,nric)
        self.__admin_no=admin_no
        self.__test_mark=test_mark
        self.__exam_mark=exam_mark
    def get_admin_no(self):
        return self.__admin_no
    def set_admin_no(self,admin_no):
        self.__admin_no=admin_no
    def get_test_mark(self):
        return self.__test_mark
    def set_test_mark(self,testmark):
        self.__test_mark=testmark
    def get_exam_mark(self):
        return self.__exam_mark
    def set_exam_mark(self,exammark):
        self.__exam_mark=exammark
    def compute_final_mark(self,testmark,exammark):
        final_mark=0.5*(testmark+exammark)
        return final_mark
    def __str__(self) :
        pass