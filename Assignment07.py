# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: *The script header includes this text and has
# been updated with your name and the current date.*
# This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
# DLarson,11/25/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Data ------------------------------------------ #
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------  
'''

# Define the Variables
students: list = []
menu_choice: str = ''


# Creating a Person Class (is the Parent Class)
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.

    ChangeLog:
    - DLarson, 11/25/2023: Created the class.
    """

    # Modifying initialization to add first_name and last_name properties to the constructor
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    # Create a "getter" or Accessor for first_name property
    @property  # Decorator for the "getter" or Accessor
    def first_name(self):
        """
        Gets the private "first_name" property on the Student Class instance

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :return: self.__first_name.title()
        """
        return self.__first_name.title()

    # Create a "setter" or Mutator for first_name property
    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the private "first_name" property on the Student Class instance after data validation

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :param value:
        :return: None
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The First Name should only contain letters.")

    # Create a "getter" or Accessor for last_name property
    @property
    def last_name(self):
        """
        Gets the private "last_name" property on the Student Class instance

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :return: self.__last_name.title()
        """
        return self.__last_name.title()

    # Create a "setter" or Mutator for last_name property
    #   Including validation and Error handling
    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the private "course_name" property on the Student Class instance after data validation

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :param value:
        :return: None
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The Last Name should only contain letters.")

    # OVERRIDE default __str__() method's behavior, return comma-separated string
    def __str__(self):
        return f'{self.first_name},{self.last_name}'


# Creating a Student Class (Child of Parent "Person" Class)
class Student(Person):
    """
    A class representing student data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.
    - course_name (str): The course name for student registration.

    ChangeLog:
    - DLarson, 11.25.2023: Created the class.
    """

    # Modify the Student constructor to pass the first_name and last_name and add course_name
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    # Create a "getter" or Accessor for last_name property
    @property
    def course_name(self):
        """
        Gets the private "course_name" property on the Student Class instance

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :return: self.__course_name
        """
        return self.__course_name

    # Create a "setter" or Mutator for last_name property
    @course_name.setter
    def course_name(self, value: str):
        """
        Sets the private "course_name" property on the Student Class instance after data validation

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :param value
        :return: None
        """
        if value.isprintable():
            self.__course_name = value
        else:
            raise ValueError("Course Name must contain letters or numbers.")

    # Override the __str__() method's behavior, return a comma-separated string
    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.course_name}'


# Processing ------------------------------------ #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        Dlarson,11.19.2023,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads the data from the file

            ChangeLog: (Who, When, What)
            DLarson,11.19.2023,Created function
            DLarson,11.25.2023,Updated function to use Class Objects
        :param file_name:
        :param student_data:
        :return: student_data
        """
        # When the program starts, extract the JSON file data into a list of dictionary rows (table)
        # Create a list of Student Class instance objects from dictionary rows
        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)
            for student in list_of_dictionary_data:
                student_obj: Student = Student(first_name=student["FirstName"],
                                               last_name=student["LastName"],
                                               course_name=student["CourseName"])
                student_data.append(student_obj)
            file.close()
            print("Data has been processed!")
        # Provide structured error handling
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data to the file

            ChangeLog: (Who, When, What)
            DLarson,11.19.2023,Created function
            DLarson,11.25.2023,Updated function to use Class Objects
        :param file_name:
        :param student_data:
        :return: None
        """
        # Create a new list to hold JSON data for json.dump() function
        list_of_dictionary_data: list = []

        # Convert the list of Student objects to JSON compatible list of dictionaries
        for student in student_data:
            student_json: dict = {"FirstName": student.first_name,
                                  "LastName": student.last_name,
                                  "CourseName": student.course_name}
            list_of_dictionary_data.append(student_json)

        # Attempt to save the file, otherwise provide structured Error Handling
        try:
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            print(f"Your data has been saved in {file_name}!\n")
            print("*" * 50, "\n")
        except TypeError as e:
            IO.output_error_messages("Please check the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        finally:
            if not file.closed:
                file.close()


# Presentation ------------------------------------ #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        Dlarson,11.19.2023,Created Class
        Dlarson,11.19.2023,Added menu output and input functions
        Dlarson,11.19.2023,Added a function to display the data
        Dlarson,11.19.2023,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param message:
        :param error:
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the Main Menu of options to the user

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param menu:
        :return: None
        """
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function captures the user-selection Menu option

        ChangeLog: (Who, When, What)
        Dlarson,11.19.2023,Created function

        :return: choice
        """
        choice = "0"
        try:
            choice = input("Please enter your Menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("INVALID SELECTION! Please select  1 - 4 from the Menu options.")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays all entered data to the user

            ChangeLog: (Who, When, What)
            DLarson,11.19.2023,Created function
            DLarson,11.25.2023,Updated function to use Class Objects
        :param student_data:
        :return: None
        """
        print()
        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function processes user-input data and adds it to the list of data

            ChangeLog: (Who, When, What)
            DLarson,11.19.2023,Created function
            DLarson,11.25.2023,Updated function to use Class Objects
        :param student_data:
        :return: student_data
        """
        try:
            # Input the data
            # Add the user-input student data to a Student Class object instance
            student = Student()
            student.first_name = input("Please enter the student's First Name: ")
            student.last_name = input("Please enter the student's Last Name: ")
            student.course_name = input("Please enter the Student's Registered Course Name: ")
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is NOT the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# End of function / method definitions

# Beginning of the Main Body of this script
# Read the data from the JSON file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
# Repeat the following tasks
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        # Print Students list with new Student information added
        IO.output_student_courses(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # Print list of data before saving to file
        IO.output_student_courses(student_data=students)
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

print("*" * 50)
print("Exiting Program.")
print("*" * 50)
