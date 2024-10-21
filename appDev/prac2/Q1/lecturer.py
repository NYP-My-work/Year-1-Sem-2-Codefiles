from Person import Person

class Lecturer(Person):
    def __init__(self, name, nric,admin_no,total_teaching_hours):
        super().__init__(name, nric)
        self.__admin_no=admin_no
        self.__total_teaching_hours=total_teaching_hours
    def set_admin_no(self,adminno):
        self.__admin_no=adminno
    def get_admin_no(self):
        return self.__admin_no
    def set_total_teaching_hours(self,teachingno):
        self.__total_teaching_hours=teachingno
    def get_teaching_hours(self):
        return self.__total_teaching_hours
    def compute_salary(self):
        return self.get_teaching_hours()*90
    def __str__(self):
        return f"The total salary is {self.compute_salary()} with teaching hours of {self.get_teaching_hours()}"