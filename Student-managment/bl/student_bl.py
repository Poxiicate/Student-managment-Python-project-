

from random import randint
from typing import Any, Hashable
from dal.text_file_management import load, save, save_iter

FILE_PATH = r"database\student.text"

def _validation(student: dict):
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}

    name = student["name"].strip()
    family = student["family"].strip()
    gender = student["gender"].strip()
    status = student["status"].strip()
    phone = student["phone"].strip()
    national_code = student["national_code"].strip()
    student_code = student["student_code"].strip()
    python_grade = student["python_grade"]
    java_grade = student["java_grade"]
    php_grade = student["php_grade"]

    if name == "":
        func_res["MESSAGE"]["name"] = "Name is empty!"

    elif not name.replace(" ", "").isalpha():
        func_res["MESSAGE"]["name"] = "Name is not alphabetic!"

    if family == "":
        func_res["MESSAGE"]["family"] = "family is empty!"

    elif not family.replace(" ", "").isalpha():
        func_res["MESSAGE"]["family"] = "family is not alphabetic!"

    if gender == "":
        func_res["MESSAGE"]["gender"] = "gender is empty!"

    elif gender not in ("male", "female", "other"):
        func_res["MESSAGE"]["gender"] = "gender is not correct!"

    if status == "":
        func_res["MESSAGE"]["status"] = "status is empty!"

    elif status not in ("active", "deactive"):
        func_res["MESSAGE"]["status"] = "status is not correct!"

    if phone == "":
        func_res["MESSAGE"]["phone"] = "phone is empty!"

    elif not phone.replace(" ", "").isdigit():
        func_res["MESSAGE"]["phone"] = "phone is not digit!"

    if national_code == "":
        func_res["MESSAGE"]["national_code"] = "national code is empty!"

    elif not national_code.replace(" ", "").isdigit():
        func_res["MESSAGE"]["national_code"] = "national code is not digit!"
        
    if student_code == "":
        func_res["MESSAGE"]["student_code"] = "student code is empty!"

    elif not student_code.replace(" ", "").isdigit():
        func_res["MESSAGE"]["student_code"] = "student code is not digit!"

    if python_grade == "":
        func_res["MESSAGE"]["python_grade"] = "python grade is empty!"

    elif not isinstance(python_grade, (int, float)) or python_grade < 0 or python_grade > 100:
        func_res["MESSAGE"]["python_grade"] = "Python grade must be a number between 0 and 100!"

    if java_grade == "":
        func_res["MESSAGE"]["java_grade"] = "java grade is empty!"

    elif not isinstance(java_grade, (int, float)) or java_grade < 0 or java_grade > 100:
        func_res["MESSAGE"]["java_grade"] = "Java grade must be a number between 0 and 100!"

    if php_grade == "":
        func_res["MESSAGE"]["php_grade"] = "php grade is empty!"

    elif not isinstance(php_grade, (int, float)) or php_grade < 0 or php_grade > 100:
        func_res["MESSAGE"]["php_grade"] = "PHP grade must be a number between 0 and 100!"


    if func_res["MESSAGE"]:
        func_res["STATUS"] = False

    return func_res

def get_student():
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}

    res = load(path=FILE_PATH)

    if not res["STATUS"]:
        func_res["STATUS"] = False
        func_res["MESSAGE"]["DatabaseError"] = "Error!"
    else:
        func_res["DATA"] = list(map(lambda student: eval(student.strip()), res["DATA"]))
    
    return func_res

def create(student: dict):
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}

    # region check field validation
    res = _validation(student)

    if not res["STATUS"]:
        func_res["STATUS"] = False
        func_res["MESSAGE"] = res["MESSAGE"]
        return func_res
    # endregion
    
    # region get student 
    res = get_student()

    if not res["STATUS"]:
        func_res["STATUS"] = False
        func_res["MESSAGE"] = res["MESSAGE"]
        return func_res
    
    student_list = res["DATA"]
    # endregion

    # region check unique phone/student code/national code
    for item in student_list:
        if item["phone"] == student["phone"]:
            func_res["MESSAGE"]["phone"] = f"{student['phone']} exists"
            func_res["STATUS"] = False
            return func_res
        
    for item in student_list:
        if item["national_code"] == student["national_code"]:
            func_res["MESSAGE"]["national_code"] = f"{student['national_code']} exists"
            func_res["STATUS"] = False
            return func_res
        
    for item in student_list:
        if item["student_code"] == student["student_code"]:
            func_res["MESSAGE"]["student_code"] = f"{student['student_code']} exists"
            func_res["STATUS"] = False
            return func_res
    # endregion 
        
    # region generate code
    while True:
        code = str(randint(10000, 99999))

        for item in student_list:
            if item["code"] == code:
                break
        else:
            student['code'] = code
            break
    # endregion
                
    # region save
    res = save(path=FILE_PATH, data=f"{student}\n")

    if res["STATUS"]:
        func_res["MESSAGE"]["Success"] = "Yeah men"
        
    else: 
        func_res["STATUS"] = False
        func_res["MESSAGE"]["DatabaseError"] = "Error!"

    return func_res
    # endregion

def read(*columns: Hashable, count: int | None = None, key: Hashable | None = None, value: Any = None):
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}

    # region get student
    res = get_student()

    if not res["STATUS"]:
        func_res["STATUS"] = False
        func_res["MESSAGE"] = res["MESSAGE"]
        return func_res
    
    student_list = res["DATA"]
    # endregion

    if key:
        student_list = list(filter(lambda student: student[key] == value, student_list))

    if count: 
        student_list = student_list[:count]

    if columns:
        func_res["DATA"] = [{col : (student[col] if col in student else '---') for col in columns} for student in student_list]

    else:
        func_res["DATA"] = student_list

    return func_res

def update(student: dict):
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}

    # region get student
    res = get_student()

    if not res["STATUS"]:
        func_res["STATUS"] = False
        func_res["MESSAGE"] = res["MESSAGE"]
        return func_res
    
    student_list = res["DATA"]
    # endregion

    # region remove operation
    for item in student_list:
        
        if item["phone"] == student["phone"] and item["code"] != student["code"]:
            func_res["MESSAGE"]["phone"] = f"{student['phone']} exists"
            func_res["STATUS"] = False

        if item["national_code"] == student["national_code"] and item["code"] != student["code"]:
            func_res["MESSAGE"]["national_code"] = f"{student['national_code']} exists"
            func_res["STATUS"] = False

        if item["student_code"] == student["student_code"] and item["code"] != student["code"]:
            func_res["MESSAGE"]["student_code"] = f"{student['student_code']} exists"
            func_res["STATUS"] = False

    if not func_res["STATUS"]:
        return func_res
        
    for item in student_list:
        if item["code"] == student["code"]:
            item.update(student)
            break
    else:
        func_res["STATUS"] = False
        func_res["MESSAGE"]["Error!"] = f"{student["code"]} does not exist"
        return func_res

    student_list_str = list(map(lambda student: f"{student}\n", student_list))
    # endregion

    # region save
    res = save_iter(path = FILE_PATH, data = student_list_str, mode = "w")

    if res["STATUS"]:
        func_res["MESSAGE"]["Success"] = "Yeah men"
        
    else: 
        func_res["STATUS"] = False
        func_res["MESSAGE"]["DatabaseError"] = "Error!"

    return func_res
    # endregion

def delete(code: str):
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}

    # region get student
    res = get_student()

    if not res["STATUS"]:
        func_res["STATUS"] = False
        func_res["MESSAGE"] = res["MESSAGE"]
        return func_res
    
    student_list = res["DATA"]
    # endregion

    # region remove operation
    for student in student_list:
        if student["code"] == code:
            student_list.remove(student)
            break
    else:
        func_res["STATUS"] = False
        func_res["MESSAGE"] = res["Error!"] = f"{code} does not exist"
        return func_res
    
    student_list_str = list(map(lambda student: f"{student}\n", student_list))
    # endregion

    # region save
    res = save_iter(path = FILE_PATH, data = student_list_str, mode = "w")

    if res["STATUS"]:
        func_res["MESSAGE"]["Success"] = "Yeah men"
        
    else: 
        func_res["STATUS"] = False
        func_res["MESSAGE"]["DatabaseError"] = "Error!"

    return func_res
    # endregion