from lecturer import Lecturer
from Student import Student

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    Lec_name_input = input("Enter Lecturer Name: ")
    Lec_NRIC_input = input("Enter Lecturer NRIC: ")
    
    while True:
        Lec_StaffID_input = input("Enter Lecturer Staff ID: ")
        if Lec_NRIC_input == Lec_StaffID_input:
            break
        print("StaffID must be NRIC!")
    
    Lec_teachinghours_input = get_valid_input("Enter Lecturer's total teaching hours: ", 0, float('inf'))
    
    Student_name_input = input("Enter Student Name: ")
    Student_NRIC_input = input("Enter Student NRIC: ")
    Student_Admin_no_input = input("Enter Student's admin no: ")
    
    test_mark = get_valid_input("Enter test mark: ", 0, 100)
    exam_mark = get_valid_input("Enter exam mark: ", 0, 100)
    
    break  

Main_input = Lecturer(Lec_name_input, Lec_NRIC_input, Lec_StaffID_input, Lec_teachinghours_input)
Side_input = Student(Student_name_input, Student_NRIC_input, Student_Admin_no_input, test_mark, exam_mark)

print(Main_input)
print(Side_input)