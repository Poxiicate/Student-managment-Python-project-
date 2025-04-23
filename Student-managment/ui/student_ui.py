

from os import system
from random import randint
from time import sleep
from bl import student_bl
from ui.common.utility import get_input, display_list_dict, show_messages, show_top_students


def student_form():

    while True:
        # region menu
        menu = get_input(
            "1.[A]dd student \n2.[D]isplay students \n3.[R]emove student \n4.[E]dit student data \n5.[S]earch student \n6.[B]est students \n7.[Q]uit\n\n Menu =>", "menu", valid_data=("1","2","3","4","5","6","7","a","d","r","e","s","b","q")
        )
        # endregion

        match menu:
            case "1" | "a" | "A":

                while True:
                    if get_input("Do you want to add a student? (yes - no) =>", valid_data=("yes", "no")) == "no":
                        break

                    # region named
                    name = get_input("Enter your first name =>", "name")
                    # endregion

                    # region family
                    family = get_input("Enter your family name =>", "family")
                    # endregion

                    # region gender
                    gender = get_input("Select you gender (male - famale - other) =>", "gender", valid_data = ("male", "female", "other"))
                    # endregion 

                    # region status
                    status = get_input("Select your status (active - deactive) =>", "status", valid_data = ("active", "deactive"))
                    # endregion

                    # region phone number
                    phone = get_input("Please enter your phone number (11 digit) =>", "phone", numeric = True, length = 11)
                    # endregion

                    # region national code
                    national_code = get_input("Enter your national code (10 digit) =>", "national code", numeric = True, length = 10)
                    # endregion

                    # region student code
                    student_code = get_input("Enter your student code (8 digit) =>", "student code", numeric = True, length = 8)
                    # endregion 

                    # region python grade
                    python_grade = get_input("Enter your python grade (0-100) => ", "python grade", validate_grade_flag=True)
                    python_grade = float(python_grade)
                    # endregion

                    # region java grade
                    java_grade = get_input("Enter your java grade (0-100) => ", "java grade", validate_grade_flag=True)
                    java_grade = float(java_grade)
                    # endregion

                    # region php grade
                    php_grade = get_input("Enter your php grade (0-100) => ", "php grade", validate_grade_flag=True)
                    php_grade = float(php_grade)
                    # endregion

                    student = {
                            "name":name,
                            "family":family,
                            "gender":gender,
                            "status":status,
                            "phone":phone,
                            "national_code": national_code,
                            "student_code":student_code,
                            "python_grade":python_grade,
                            "java_grade":java_grade,
                            "php_grade":php_grade
                    }
                    while True:

                        res = student_bl.create(student)

                        if res["STATUS"]:
                            show_messages(messages = res["MESSAGE"])
                            break

                        show_messages(messages = res["MESSAGE"], is_error = True)

                        if "DatabaseError" in res["MESSAGE"]:
                            sleep(2)
                            break

                        if "name" in res["MESSAGE"]:
                            student["name"] = get_input("Enter your first name =>", "name")
                            
                        if "family" in res["MESSAGE"]:
                            student["family"] = get_input("Enter your family name =>", "family")

                        if "gender" in res["MESSAGE"]:
                            student["gender"] = get_input("Select you gender (male - female - other) =>", "gender", valid_data = ("male", "female", "other"))

                        if "status" in res["MESSAGE"]:
                            student["status"] = get_input("Select your status (active - deactive) =>", "status", valid_data = ("active", "deactive"))

                        if "phone" in res["MESSAGE"]:
                            student["phone"] = get_input("Please enter your phone number (11 digit) =>", "phone", numeric = True, length = 11)

                        if "national_code" in res["MESSAGE"]:
                            student["national_code"] = get_input("Enter your national code (10 digit) =>", "national code", numeric = True, length = 10)

                        if "student_code" in res["MESSAGE"]:
                            student["student_code"] = get_input("Enter your student code (8 digit) =>", "student code", numeric = True, length = 8)

                        if "python_grade" in res["MESSAGE"]:
                            grade_input = get_input("Enter your python grade (0-100) => ", "python grade", validate_grade_flag=True)
                            student["python_grade"] = float(grade_input)

                        if "java_grade" in res["MESSAGE"]:
                            grade_input = get_input("Enter your java grade (0-100) => ", "java grade", validate_grade_flag=True)
                            student["java_grade"] = float(grade_input)

                        if "php_grade" in res["MESSAGE"]:
                            grade_input = get_input("Enter your php grade (0-100) => ", "php grade", validate_grade_flag=True)
                            student["php_grade"] = float(grade_input)
                            

            case "2" | "d" | "D":
                
                if get_input("Do you want to display all column? (yes - no) =>", valid_data=("yes", "no")) == "yes":
                    display_col = ("code", "name", "family", "gender", "status", "phone", "national_code", "student_code", "python_grade", "java_grade", "php_grade")

                else:
                    display_col = []

                    # region select column
                    while True:
                        print("-------------------------------------------")
                        print("Display column : ", end="")
                        print(*display_col, sep=" , ")
                        print("-------------------------------------------")

                        input_col = get_input("\n\nColumn code, Name, Family, Gender, Status, Phone, National_code, Student_code, Python_grade, Java_grade, Php_grade, Exit =>", valid_data=("code", "name", "family", "gender", "status", "phone", "national_code", "student_code", "python_grade", "java_grade", "php_grade", "exit"))

                        if input_col == "exit":
                            break

                        if input_col not in display_col:
                            display_col.append(input_col)
                        # endregion
                        
                res = student_bl.read(*display_col)

                if not res["STATUS"]:
                    show_messages(messages = res["MESSAGE"], is_error = True)
                    
                else:
                    display_list_dict(res["DATA"], *display_col)

                    sleep(2)
                    input("Press enter to continue!")
                    system("cls")
                
            
            case "3" | "r" | "R":

                while True:
                    if get_input("Do you want to remove a student? (yes - no) =>", valid_data = ("yes", "no")) == "no":
                        break

                    res = student_bl.read()

                    if not res["STATUS"]:
                        show_messages(messages = res["MESSAGE"], is_error = True)
                        break
                    
                    display_list_dict(res["DATA"])
                    
                    # region select remove column
                    remove_col = get_input("Remove column [code, name, family, gender, status, phone, national code, student code] =>", valid_data = ("code", "name", 'family', "gender", "status", "phone", "national_code", "student_code"))
                    # endregion

                    display_list_dict(res["DATA"])

                    # region set remove base
                    match remove_col:
                        case "code":
                            value = get_input("Enter code key =>")

                        case "name":
                            value = get_input("Enter name key =>")

                        case "family":
                            value = get_input("Enter family key =>")

                        case "gender":
                            value = get_input("Enter gender key =>", valid_data=("female", "male", "other"))

                        case "status":
                            value = get_input("Enter status key =>", valid_data=("active", "deactive"))

                        case "phone":
                            value = get_input("Enter phone key =>")

                        case "national_code":
                            value = get_input("Enter national code key =>")

                        case "student_code":
                            value = get_input("Enter student code key =>")
                    # endregion

                    search_res = student_bl.read(key = remove_col, value = value)

                    if not search_res["STATUS"]:
                        show_messages(messages = search_res["MESSAGE"], is_error = True)
                        break

                    find_remove_student = search_res["DATA"]

                    # region authority
                    if not find_remove_student:
                        print(value, "does not exist!!!")
                        continue

                    for student in find_remove_student:
                        print("----------------------------------")
                        print("Code : ", student["code"])
                        print("Name : ", student["name"])
                        print("Family : ", student["family"])
                        print("Gender : ", student["gender"])
                        print("Status : ", student["status"])
                        print("Phone : ", student["phone"])
                        print("National code : ", student["national_code"])
                        print("Student code : ", student["student_code"])
                        print("Python grade : ", student["python_grade"])
                        print("Java grade : ", student["java_grade"])
                        print("Php grade : ", student["php_grade"])
                        print("----------------------------------")

                        if get_input("Do you want to remove this student (yes - no) =>", valid_data=("yes", "no")) == "yes":
                            res = student_bl.delete(student["code"])

                            if not res["STATUS"]:
                                show_messages(messages = search_res["MESSAGE"], is_error = True)
                            else:
                                show_messages(messages = search_res["MESSAGE"])
                    # endregion


            case "4" | "e" | "E":

                while True:
                    if get_input("Do you want to edit student info? (yes - no) =>", valid_data=("yes", "no")) == "no":
                        break

                    # region get student    
                    res = student_bl.read()

                    if not res["STATUS"]:
                        show_messages(messages = res["MESSAGE"], is_error = True)
                        break

                    student_list = res["DATA"]
                    # endregion
                    
                    display_list_dict(res["DATA"])

                    edit_col = get_input("Edit column [code, phone, national_code, student_code] =>", valid_data = ("code", "phone", "national_code", "student_code"))
                
                    display_list_dict(res["DATA"])

                    # region get edit value , set remove index
                    match edit_col:
                        case "code":
                            value = get_input("Enter code key =>")

                        case "phone":
                            value = get_input("Enter phone key =>")

                        case "national_code":
                            value = get_input("Enter national code key =>")

                        case "student_code":
                            value = get_input("Enter student code key =>")
                    # endregion

                    search_res = student_bl.read(key = edit_col, value = value)

                    if not search_res["STATUS"]:
                        show_messages(messages = search_res["MESSAGE"], is_error = True)
                        break

                    selected_students = search_res["DATA"]

                    if not selected_students:
                        print(value, "does not exist!!!")
                        continue

                    student = selected_students[0]

                    # region edit student
                    while True:
                        print("----------------------------------")
                        print("Code : ", student["code"])
                        print("Name : ", student["name"])
                        print("Family : ", student["family"])
                        print("Gender : ", student["gender"])
                        print("Status : ", student["status"])
                        print("Phone : ", student["phone"])
                        print("National code : ", student["national_code"])
                        print("Student code : ", student["student_code"])
                        print("Python grade : ", student["python_grade"])
                        print("Java grade : ", student["java_grade"])
                        print("Php grade : ", student["php_grade"])
                        print("----------------------------------")

                        edit_item = get_input("Edit item (name, family, gender, status, phone, national_code, student_code, python_grade, java_grade, php_grade, save) =>", valid_data=("name", "family", "gender", "status", "phone", "national_code", "student_code", "python_grade", 'java_grade', "php_grade", "save"))

                        if edit_item == "save":
                            res = student_bl.update(student)

                            if not res["STATUS"]:
                                show_messages(messages = res["MESSAGE"], is_error = True)
                            else:
                                show_messages(messages= res["MESSAGE"])

                            break

                        match edit_item:
                            case "name":
                                student["name"] = get_input("Enter your first name =>", "name")
                            
                            case "family":
                                student["family"] = get_input("Enter your family name =>", "family")
                            
                            case "gender":
                                student["gender"] = get_input("Select you gender (male - famale - other) =>", "gender", valid_data=("male", "female", "other"))

                            case "status":
                                student["status"] = get_input("Select your status (active - deactive) =>", "status", valid_data=("active", "deactive"))

                            case "phone":
                                student["phone"] = get_input("Please enter your phone number =>", "phone", numeric = True, length = 11)

                            case "national_code":
                                student["national_code"] = get_input("Enter your national code =>", "national code", numeric = True, length = 10)

                            case "student_code":
                                student["student_code"] = get_input("Enter your student code =>", "student code", numeric = True, length = 8)

                            case "python_grade":
                                new_python_grade = get_input("Enter your python grade (0-100) =>", "python grade", validate_grade_flag=True)
                                student["python_grade"] = float(new_python_grade)

                            case "java_grade":
                                new_java_grade = get_input("Enter your java grade (0-100) =>", "java grade", validate_grade_flag=True)
                                student["java_grade"] = float(new_java_grade)

                            case "php_grade":
                                new_php_grade = get_input("Enter your php grade (0-100) =>", "php grade", validate_grade_flag=True)
                                student["php_grade"] = float(new_php_grade)

                            case _:
                                print("Error!")
                        # endregion


            case "5" | "s" | "S":

                while True:
                    if get_input("Do you want to search student (yes - no) =>", valid_data=("yes", "no")) == "no":
                        break
                    
                    search_col = get_input("Column code, Name, Family, Gender, Status, Phone, National_code, Student_code, Python_grade, Java_grade, Php_grade =>", valid_data=("name", "family", "gender", "status", "phone", "national_code", "student_code", "python_grade", 'java_grade', "php_grade", "exit"))
                    
                    match search_col:
                        case "code":
                            search_value = get_input("Code : ")

                        case "name":
                            search_value = get_input("Name : ")

                        case "family":
                            search_value = get_input("family : ")

                        case "gender":
                            search_value = get_input("gender : ")

                        case "status":
                            search_value = get_input("status : ")

                        case "phone":
                            search_value = get_input("phone : ")

                        case "national_code":
                            search_value = get_input("national code : ")

                        case "studetn_code":
                            search_value = get_input("student code : ")

                        case "python_grade":
                            search_value = get_input("python grade : ")
                            search_value = float(search_value)

                        case "java_grade":
                            search_value = get_input("java grade : ")
                            search_value = float(search_value)

                        case "php_grade":
                            search_value = get_input("php grade : ")
                            search_value = float(search_value)

                    res = student_bl.read(key = search_col, value = search_value)

                    if not res["STATUS"]:
                        show_messages(messages = res["MESSAGE"], is_error = True)
                        break

                    search_student = res["DATA"]

                    if not search_student:
                        print(search_value, "does not exist!!!")
                        continue
                    
                    display_list_dict(res["DATA"])


            case "6" | "b" | "B":
            
                # region best student 
                while True:
                    if get_input("Do you want to see the best students? (yes - no) =>", valid_data=("yes", "no")) == "no":
                        break
                    
                    while True:
                        which_grade = get_input("\nPython, Java, Php, Average =>", valid_data=("python", "java", "php", "average"))

                        res = student_bl.read()

                        if not res["STATUS"]:
                            show_messages(messages = res["MESSAGE"], is_error = True)
                            break
                        
                        student_list = res["DATA"]

                        if which_grade == "average":
                            show_top_students(student_list, grade_key="", is_average=True)
                            
                        else:
                            grade_key = f"{which_grade}_grade"
                            show_top_students(student_list, grade_key)
                            
                        break 
                # endregion


            case "7" | "q" | "Q":
                break


            case _:
                print("Error!")
