
def student_subject_combination():
 department_courses = {
     "Math", "Physics", "Computer Science", "Biology", "Chemistry",
     "Statistics", "English", "Economics", "History", "Philosophy",
     "Sociology", "Political Science", "Geography", "Psychology", "Art",
     "Music", "Engineering", "Law", "Medicine", "Business"
    }

students_record = {}
def create_student_record():
    username = input("Enter unique username: ")
    if username in students_record:
        return "name already exists!"

        if student_name.isalpha()
            return student_name
        return "Alphanumeric name not allowed!"

    student_age = int(input("Enter age: "))
    student_home_address = input("Enter home address: ")
    student_email_address = input("Enter email address: ")
    student_date_of_birth = input("Enter date of birth: ")

    student_course_input  =  input("Enter home address: ")

    student_city = input("Enter city: ")
    student_zipcode = input("Enter zipcode: ")

    students_record[username] = {
        "student_name ": name,
        "student_age": age,
        "student_home_address": home_address,
        "student_email_address": email_address,
        "student_date_of_birth": date_of_birth,
        "studet_course_input": course_input,
        # "student_city": city
        # "student_zipcode": zipcode
        "address": {
            "city": student_city,
            "zip_code": student_zipcode
        }
    }



def display_student_record(username):
    student = student_record.get(username)

    if student in students_record:
        student_name = input("Enter student name: ")
        print(student_name)

        student_age = int(input("Enter age: "))
        print(student_age)

        courses
        # "Name": {student['name']}
        # "Age": {student['age']}
        # "Courses": {student['courses']}
        # "City": {student['address']['city']}
        # "Zip Code": {student['address']['zip_code']}

    else:
        return "Student not found, please try again."


def display_the_courses_the_student_is_offering(username):
    student = student_record.get(username)
    if student:
        return f"department_courses: {student['courses']}"
    else:
        return "Student not found."


def display_students_zipcode(username):
    student = student_record.get(username)
    if student in students_record:
        return f"Zipcode: {student['address']['zip_code']}"
    else:
        return "Student not found."

def display_students_city(username):
    student = student_record.get(username)
    if student in students_record:
        return f"City: {student['address']['city']}"
    else:
        return "Student not found."

def add_course(username):
    student = student_record.get(username)
    if stuudent not in student_record:
        return "Student not found."

    new_course = input("Enter course to add: ")

    if new_course not in department_courses:
        return "Course not offered!"

    elif new_course in student["courses"]:
        return "Course already exists!"

    else:
        student["courses"].add(new_course)
        return "Course added successfully!"

def remove_course(username):
    student = student_record.get(username)
    if not student:
        return "Student not found."

    course = input("Enter course to remove: ")

    if course in student["courses"]:
        student["courses"].remove(course)
        return "Course removed!"
    else:
        return "Course not found!"

def update_student_course(username):
    student = student_record.get(username)
    if not student:
        return "Student not found"

    print("1. Update Name")
    print("2. Update Age")
    print("3. Update City")
    print("4. Update Zip Code")

    option = input("Enter an option ")

    match option:
        case "1":
            student["name"] = input("Enter new name: ")
        case "2":
            student["age"] = int(input("Enter new age: "))
        case "3":
            student["address"]["city"] = input("Enter new city: ")
        case "4":
            student["address"]["zip_code"] = input("Enter new zip code: ")
        case _:
            print("Invalid choice")

    return "Update successful!"