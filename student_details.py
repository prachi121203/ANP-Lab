
def get_student_details():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    phone_number = input("Enter Phone Number: ")

    return student_id, name, age, city, phone_number


def display_student_details(student_id, name, age, city, phone_number):
    print("\nStudent Details:")
    print(f"ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Phone Number: {phone_number}")


student_id, name, age, city, phone_number = get_student_details()
display_student_details(student_id, name, age, city, phone_number)
