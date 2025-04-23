
from os import system
from random import randint
from time import sleep
from note.Utility import get_input, display_list_dict, search_list_dict, validate_grade, show_top_students


student_list = [
    {"code":"13132", "name":"pooria", "family":"kia", "gender":"male", "status":"active", "phone":"21", "national_code":"1214", "student_code":"1315", "python_grade":100.0, "java_grade":90.0, "php_grade":90.0},
    {"code":"13133", "name":"pooria", "family":"kia", "gender":"male", "status":"active", "phone":"21", "national_code":"1214", "student_code":"1315", "python_grade":99.0, "java_grade":90.0, "php_grade":90.0},
    {"code":"13134", "name":"pooria", "family":"kia", "gender":"male", "status":"active", "phone":"21", "national_code":"1214", "student_code":"1315", "python_grade":100.0, "java_grade":90.0, "php_grade":90.0},
    {"code":"13145", "name":"pooria", "family":"kia", "gender":"male", "status":"active", "phone":"21", "national_code":"1214", "student_code":"1315", "python_grade":80.0, "java_grade":90.0, "php_grade":90.0},
    {"code":"13136", "name":"pooria", "family":"kia", "gender":"male", "status":"active", "phone":"21", "national_code":"1214", "student_code":"1315", "python_grade":90.0, "java_grade":90.0, "php_grade":90.0}
]

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

                # region code
                while True:
                    code = str(randint(10000, 99999))

                    result = search_list_dict(student_list, key="code", value=code)
                    
                    if not result:
                        break   
                # endregion
                
                # region named
                name = get_input("Enter your first name =>", "name")
                # endregion

                # region family
                family = get_input("Enter your family name =>", "family")
                # endregion

                # region gender
                gender = get_input("Select you gender (male - famale - other) =>", "gender", valid_data=("male", "female", "other"))
                # endregion 

                # region status
                status = get_input("Select your status (active - deactive) =>", "status", valid_data=("active", "deactive"))
                # endregion

                # region phone number
                while True:
                    phone = get_input("Please enter your phone number =>", "phone", numeric = True, length = 11)

                    result = search_list_dict(student_list, key="phone", value=phone)

                    if not result:
                        break

                    print("Error!,", phone, "exist")
                # endregion

                # region national code
                while True: 
                    national_code = get_input("Enter your national code =>", "national code", numeric = True, length = 10)

                    result = search_list_dict(student_list, key="national_code", value=national_code)
                    
                    if not result:
                        break

                    print("Error!,", national_code, "exist")
                # endregion

                # region student code
                while True: 
                    student_code = get_input("Enter your student code =>", "student code", numeric = True, length = 8)

                    result = search_list_dict(student_list, key="student_code", value=student_code)
                    
                    if not result:
                        break

                    print("Error!,", student_code, "exist")
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

                student = {"code":code, "name":name, "family":family, "gender":gender, "status":status, "phone":phone, "national_code": national_code, "student_code":student_code, "python_grade":python_grade, "java_grade":java_grade, "php_grade":php_grade}
                student_list.append(student) 


        case "2" | "d" | "D":
            
            if get_input("Do you want to display all column? yes-etc =>", valid_data=("yes", "no")) == "yes":
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

            # region show contact
            display_list_dict(student_list, *display_col)

            sleep(2)
            input("Press enter to continue!")
            system("cls")
            # endregion


        case "3" | "r" | "R":

            while True:
                if get_input("Do you want to remove a student? (yes - etc) =>", valid_data = ("yes", "no")) == "no":
                    break

                display_list_dict(student_list)
                
                # region select remove column
                remove_col = get_input("Remove column [code, name, family, gender, status, phone, national code, student code]", valid_data = ("code", "name", 'family', "gender", "status", "phone", "national_code", "student_code"))
                # endregion

                display_list_dict(student_list)

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

                # region authority
                find_remove_student = search_list_dict(student_list, key=remove_col, value=value)

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

                    if get_input("Do you want to remove this student yes-etc =>", valid_data=("yes", "no")) == "yes":
                        student_list.remove(student)

                    print("Done!")
                # endregion

        case "4" | "e" | "E":

            while True:
                if get_input("Do you want to edit student info? yes-etc =>", valid_data=("yes", "no")) == "no":
                    break

                display_list_dict(student_list)

                # region select edit column
                edit_student = get_input("Edit column [code, phone, national code, student code]", valid_data = ("code", "phone", "national_code", "student_code"))
                # endregion

                display_list_dict(student_list)

                # region get edit value , set remove index
                match edit_student:
                    case "code":
                        value = get_input("Enter code key =>")

                    case "phone":
                        value = get_input("Enter phone key =>")

                    case "national code":
                        value = get_input("Enter national code key =>")

                    case "student code":
                        value = get_input("Enter student code key =>")
                # endregion

                edit_student = search_list_dict(student_list, key=edit_student, value=value)

                if not edit_student:
                    print(value, "does not exist!!!")
                    continue

                student = edit_student[0]

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

                    edit_item = get_input("Edit item (name, family, gender, status, phone, national_code, student_code, python_grade, java_grade, php_grade, exit) =>", valid_data=("name", "family", "gender", "status", "phone", "national_code", "student_code", "python_grade", 'java_grade', "php_grade", "exit"))

                    match edit_item:
                        case "name":
                            # region new name
                            new_name = get_input("Enter your first name =>", "name")
                            # endregion

                            student["name"] = new_name

                        case "family":
                            # region new family
                            new_family = get_input("Enter your family name =>", "family")
                            # endregion

                            student["family"] = new_family

                        case "gender":
                            # region new gender
                            new_gender = get_input("Select you gender (male - famale - other) =>", "gender", valid_data=("male", "female", "other"))
                            # endregion

                            student["gender"] = new_gender

                        case "status":
                            # region new status
                            status = get_input("Select your status (active - deactive) =>", "status", valid_data=("active", "deactive"))
                            # endregion

                        case "phone":
                            # region new phone number
                            while True:
                                new_phone = get_input("Please enter your phone number =>", "phone", numeric = True, length = 11)

                                result = search_list_dict(student_list, key="phone", value=phone)

                                if not result:
                                    break

                                print("Error!,", phone, "exist")
                            # endregion

                            student["phone"] = new_phone

                        case "national_code":
                            # region new national code
                            while True: 
                                new_national_code = get_input("Enter your national code =>", "national code", numeric = True, length = 10)

                                result = search_list_dict(student_list, key="national_code", value=national_code)
                                
                                if not result:
                                    break

                                print("Error!,", national_code, "exist")
                            # endregion

                            student["national_code"] = new_national_code

                        case "student_code":
                            # region new student code
                            while True: 
                                new_student_code = get_input("Enter your student code =>", "student code", numeric = True, length = 8)

                                result = search_list_dict(student_list, key="student_code", value=student_code)
                                
                                if not result:
                                    break

                                print("Error!,", student_code, "exist")
                            # endregion

                            student["student_code"] = new_student_code

                        case "python_grade":
                            # region new python grade
                            new_python_grade = get_input("Enter your python grade (0-100) => ", "python grade", validate_grade_flag=True)
                            new_python_grade = float(new_python_grade)
                            # endregion  

                            student["python_grade"] = new_python_grade

                        case "java_grade":
                            # region new java grade
                            new_java_grade = get_input("Enter your java grade (0-100) => ", "java grade", validate_grade_flag=True)
                            new_java_grade = float(new_java_grade)
                            # endregion  

                            student["java_grade"] = new_java_grade

                        case "php_grade":
                            # region new php grade
                            new_php_grade = get_input("Enter your php grade (0-100) => ", "php grade", validate_grade_flag=True)
                            new_php_grade = float(new_php_grade)
                            # endregion  

                            student["php_grade"] = new_php_grade

                        case "exit":
                            break

                        case _:
                            print("Error!")


        case "5" | "s" | "S":

            while True:
                if get_input("Do you want to search student =>", valid_data=("yes", "no")) == "no":
                    break
                
                # region select search column
                search_col = get_input("Column code, Name, Family, Gender, Status, Phone, National_code, Student_code, Python_grade, Java_grade, Php_grade =>", valid_data=("name", "family", "gender", "status", "phone", "national_code", "student_code", "python_grade", 'java_grade', "php_grade", "exit"))
                # endregion

                # region get search value , set remove index
                match search_col:
                    case "code":
                        value = get_input("Code : ")

                    case "name":
                        value = get_input("Name : ")

                    case "family":
                        value = get_input("family : ")

                    case "gender":
                        value = get_input("gender : ")

                    case "status":
                        value = get_input("status : ")

                    case "phone":
                        value = get_input("phone : ")

                    case "national_code":
                        value = get_input("national code : ")

                    case "studetn_code":
                        value = get_input("student code : ")

                    case "python_grade":
                        value = get_input("python grade : ")
                        value = float(value)

                    case "java_grade":
                        value = get_input("java grade : ")
                        value = float(value)

                    case "php_grade":
                        value = get_input("php grade : ")
                        value = float(value)
                # endregion
                
                # region search contact
                search_res = search_list_dict(student_list, value=search_col)
                display_list_dict(search_res)
                # endregion
        
        case "6" | "b" | "B":
            
            # region best student 
            while True:
                if get_input("Do you want to see the best students? (yes - etc) =>", valid_data=("yes", "no")) == "no":
                    break
                
                while True:
                    which_grade = get_input("\nPython, Java, Php, Average =>", valid_data=("python", "java", "php", "average"))

                    if which_grade == "average":
                        show_top_students(student_list, grade_key="", is_average=True)
                        break
                    else:
                        grade_key = f"{which_grade}_grade"
                        show_top_students(student_list, grade_key)
                        break
            # endregion

        case "7" | "Q" | "q":
            break

        case _:
            print("Error!!!")
