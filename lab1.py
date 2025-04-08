import os

class Student:
    # Functions that are wrapped in "__" like `__init__`, `__str__` etc
    # are called dunder methods. Most of them are called implicitly like
    # `__init__` that is used to initialize (fill with values) the object or
    # `__str__` that defines how our object will be repesented when we try to print it
    # All methods that access or modifies the contents of the object require `self` attribute
    def __init__(self, number, name, lastname, date_of_birth, sex, country_of_birth):
        # Python doesn't have private fields, so in order to tell developers that an attribute
        # is private we prepend "_" to the name. Language doesn't inforce it. It just a guideline
        # NOTE: int(number) and int(date_of_birth) will raise exception if
        # provided value can't be converted to an integer
        self._number = int(number)
        self._name = name
        self._lastname = lastname
        self._date_of_birth = int(date_of_birth)
        self._sex = sex
        self._country_of_birth = country_of_birth

    # Dunder method that we use to define how we want our class to be seen
    # when we print it
    def __str__(self):
        # NOTE: We're using "\" right before we press ENTER to allow our
        # string to span multiple line; otherwise, it would have errored
        return f"Student Data\n\
        Number: {self._number}\n\
        Name: {self._name}\n\
        Lastname: {self._lastname}\n\
        Date of Birth: {self._date_of_birth}\n\
        Age: {2025 - self._date_of_birth}\n\
        Sex: {self._sex}\n\
        Counry of Birth: {self._country_of_birth}\n"

    # Helper function that we're going to use later to write easily to a file
    def as_csv(self):
        return f"{self._number},{self._name},{self._lastname},{self._date_of_birth},{self._sex},{self._country_of_birth}\n"

    # Getter methods
    def get_number(self):
        return self._number
    def get_name(self):
        return self._name
    def get_lastname(self):
        return self._lastname
    def get_date_of_birth(self):
        return self._date_of_birth
    def get_sex(self):
        return self._sex
    def get_country_of_birth(self):
        return self._country_of_birth

    # Setter methods
    def set_number(self, value):
        # Will raise exception if value is non numeric
        self._number = int(value)
    def set_name(self, value):
        self._name = value
    def set_lastname(self, value):
        self._lastname = value
    def set_date_of_birth(self, value):
        # Will raise exception if value is non numeric
        self._date_of_birth = value
    def set_sex(self, value):
        self._sex = value
    def set_country_of_birth(self, value):
        self._country_of_birth = value

def write_to_file(filename, students):
    # Open csv file in write mode
    # NOTE: csv is plain text database files
    # NOTE: Encoding is specified because otherwise Windows can break the encoding
    # NOTE: We're using `with` expression as it guarantees that file will be closed even if
    # error occurs during programs execution
    with open(f"{filename}.csv", "w", encoding="utf-8") as f:
        # csv files need first line to reason about how to interpret data
        f.write("Number,Name,Lastname,Date of Birth,Sex,Country of Birth\n")
        f.writelines(student.as_csv() for student in students)

def read_from_file(filename):
    # Open csv file to read
    # NOTE: Reading is the default option to access the file
    with open(f"{filename}.csv", encoding="utf-8") as f:
        extracted_students=[]
        for line in f.read().splitlines()[1:]:
            data: list[str] = line.split(",")
            number = data[0]
            name = data[1]
            lastname = data[2]
            date_of_birth= data[3]
            sex = data[4]
            country_of_birth = data[5]
            extracted_students.append(Student(number, name, lastname, date_of_birth, sex, country_of_birth))
    return extracted_students

def add_student(students):
    # Prompt user to get student data
    name = input("Please enter the name: ")
    lastname = input("Latname: ")

    # Date of Birth is stored as an int; therefore, user input must be a valid integer
    date_of_birth = input("Date of birth (must be a positive digit): ")
    while not date_of_birth.isdigit():
        print(f"Date of birth you've entered {date_of_birth} is not a valid positive digit")
        date_of_birth = input("Enter date of birth (must be a positive digit): ")
    sex = input("Sex: ")
    country_of_birth = input("Country: ")

    # Determine last student number used
    last_index = students[-1].get_number() + 1 if len(students) > 0 else 1

    # Add new student to students
    students.append(Student(last_index, name, lastname, date_of_birth, sex, country_of_birth))
    # Our program is not parallel that's why it's safe to modify global variable

def get_students_in_year(students):
    # Get the array filled with students born in the prompted year
    year = input("Please enter the year: ")
    while not year.isdigit():
        year = input("Year must be a valid positive digit")
    return [student for student in students if student.get_date_of_birth() == int(year)]

def get_student(number, students):
    for student in students:
        if student.get_number() == number:
            return student

def change_attr(student, attr):
    print("Student to be modified")
    print(student)

    value = input("What value shall it be?\n")

    if attr == "name":
        student.set_name(value)
    elif attr =="lastname":
        student.set_lastname(value)
    elif attr =="date of birth":
        if not value.isdigit():
            print(f"Date of birth should be a valid postive digit")
            return 
        student.set_date_of_birth(value)
    elif attr =="sex":
        student.set_sex(value)
    elif attr == "country":
        student.set_country_of_birth(value)

    print(student)

students = []
while True:
    print("\
    1) Write entered students to a csv file\n\
    2) Read/Load students from existing file\n\
    3) Find a student from loaded file\n\
    4) Show all students\n\
    5) Show all students born in a given year\n\
    6) Modify a student record\n\
    7) Delete student\n\
    8) Add a student\n\
    9) Quit\n\
    Enter operation number:\n")
    option = input()

    print("-"*20)
    # Write to file
    if option == "1":
        if len(students) == 0:
            print("You haven't entered any student yet\nAdd students or read from existing file")
            continue

        filename = input("Please enter filename to write\n")
        write_to_file(filename, students)
        print("Data was written to the file")
    # Read/Load file
    elif option == "2":
        filename = input("Please enter filename (without extension) to read\n")
        # Check if the file exists
        if not os.path.exists(filename + ".csv"):
            print("Program could not find file named %s" % filename)
            continue
        try:
            students = read_from_file(filename)
        except Exception:
            print("Error occured during file reading\nAborting...")
            continue
    # Print specific student
    elif option == "3":
        id = input("Please enter student number\n")
        while not id.isdigit():
            id = input("Student Number must be a positive digit\nPlease enter student number\n")
        student = get_student(int(id), students)

        if student is None:
            print(f"Student with id '{id}' wasn't found")
            continue
        print(student)
    # Print all students
    elif option == "4":
        for student in students:
            print(student)
    # Print students born in some year
    elif option == "5":
        born_in_xxxx = get_students_in_year(students)

        if len(born_in_xxxx) == 0:
            print("There are no students born in the provided year")
            continue

        for student in born_in_xxxx:
            print(student)
    # Modify student
    elif option == "6":
        id = input("Please enter student number to modify\n")
        while not id.isdigit():
            id = input("Student Number must be a positive digit\nPlease enter student number to modify\n")
        student = get_student(int(id), students)

        if student is None:
            print(f"Student with id '{id}' wasn't found")
            continue

        while True:
            attribute = input("Please enter attribute to modify\n(Name, Lastname, Date of Birth, Sex, Country)\n").lower()
            if attribute not in ("name", "lastname", "date of birth", "sex", "country"):
                print("Entered attribute does not exist")
                continue
            break
        change_attr(student, attribute)
    # Delete student
    elif option == "7":
        id = input("Please enter student number to delete\n")
        while not id.isdigit():
            id = input("Student Number must be a positive digit\nPlease enter student number to delete\n")
        student = get_student(int(id), students)

        if student is None:
            print(f"Student with id '{id}' wasn't found")
            continue

        students.pop(students.index(student))
    # Add Student
    elif option == "8":
        add_student(students)
        print("Student added")
        print(students[-1])
    # Quit
    elif option == "9":
        break
    # Invalid Input
    else:
        print("Option must be a number between 1 and 9 inclusive")

    print("-"*20)
