class Student:
    def __init__(self, name, math, chinese, english, science):
        self.name = name
        self.math = float(math)      # Convert scores to float
        self.chinese = float(chinese)
        self.english = float(english)
        self.science = float(science)
        self.choices = []           # Initialize choices as an empty list

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4

    def set_choice(self, choice):
        # Split the choices string into a list if it's not already a list
        self.choices = choice.split(", ") if isinstance(choice, str) else choice
        return self.choices


def load_result():
    students = []
    try:
        with open('prac3/results.txt', "r") as results:  # Open in read mode
            for line in results:
                data = line.strip().split(',')  # Split the line into data
                if len(data) == 5:
                    student = Student(
                        name=data[0].strip(),
                        math=data[1].strip(),
                        chinese=data[2].strip(),
                        english=data[3].strip(),
                        science=data[4].strip()
                    )
                    students.append(student)
            return students  # Ensure return is outside the loop
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: Invalid data format - {ve}")
    except IOError as ioe:
        print(f"Error: IO Error - {ioe}")
    except PermissionError:
        print("Error: Permission denied.")
    return []  # Return an empty list if an exception occurs


def main():
    students = load_result()
    choice = "ChoiceA, ChoiceB, ChoiceC"  # Choices string
    if students:
        for s in students:
            s.set_choice(choice)  # Assign choices
            print(f"{s.name}, Score: {s.get_score():.2f}, Choices: {s.choices}")
    else:
        print("No students found.")


# Start the program
main()
