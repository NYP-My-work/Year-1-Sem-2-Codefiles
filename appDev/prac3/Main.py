class Student:
    def __init__(self, name, math, chinese, english, science ):
        self.name = name
        self.math = float(math)      # Need to convert to float
        self.chinese = float(chinese)
        self.english = float(english)
        self.science = float(science)
        self.choices = []

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4
    def set_choice(self, choice ):
        self.choices=choice
        return(self.choices)


def main():
    students = load_result()
    choice="the choices are ChoiceA, ChoiceB, ChoiceC"
    if students:
        for s in students:
            s.set_choice(choice)
            print(f"{s.name}, Score: {s.get_score():.2f}, Choices: {s.choices}")



def load_result():
    students = []
    try:
        with open('prac3/results.txt', "r") as results:
            for line in results:
                data = line.strip().split(',')  # strip() is a method, needs ()
                if len(data) == 5:
                    student = Student(
                        name=data[0].strip(),
                        math=data[1].strip(),
                        chinese=data[2].strip(),
                        english=data[3].strip(),
                        science=data[4].strip()
                    )
                    students.append(student)
            return students  # Move return outside the for loop
    except FileNotFoundError:  # Correct exception name
        print("File Not Found!")
    except ValueError:
        print("Hey, valueerror")
    except IOError:
        print("IOError")
    except PermissionError:
        print("Permissions Error")


# start the test program
main()