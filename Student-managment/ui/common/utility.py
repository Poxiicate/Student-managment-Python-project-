

from os import system
from typing import Any, Hashable, Iterable


def show_messages(messages: dict, is_error: bool = False):

    print(f"{("Error") if is_error else "Success":-^50}")

    for key, value in messages.items():
        print(f"{key} : {value}.")

    print("-" * 50, end="\n\n")


def get_input(field: str, err_field="input", /, *, required: bool = True, valid_data: Iterable = (), numeric: bool = False, length: int | None = None, validate_grade_flag : bool = False) -> str:
    err_list = []

    while True:
        value = input(field).lower()
        system("cls")
        
        if required and value == "":
            err_list.append(f"Error, {err_field} is empty!!!")

        if numeric and not value.isdigit():
            err_list.append(f"Error: {err_field} must be numeric!")

        if length is not None and len(value) != length:
            err_list.append(f"Error: {err_field} must be exactly {length} characters!")
        
        if valid_data and value not in valid_data:
            err_list.append(f"Error!, {value} not in {', '.join(map(str, valid_data))}")

        if validate_grade_flag:
            grade_error = _validate_grade(value)  
            if grade_error:
                err_list.append(grade_error)

        if not err_list:
            return value 
        
        print(f"{'Error':-^50}")
        print(*err_list, sep="\n")
        print("-" * 50)
        err_list.clear()


def _validate_grade(grade):
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            return "Error! Grade must be between 0 and 100!"
        
    except ValueError:
        return "Error! Grade must be a valid number!"
    
    return None


def display_list_dict(data_list: list[dict], *keys: Hashable, show_head: bool = True, show_row: bool = True, size: int = 15):

    if (not keys) and data_list:
        keys = tuple(data_list[0].keys())

    if show_head:
        print((f"{'#':<4}" if show_row else ""), *[f"{k:{size}}" for k in keys])

    print("-" * ((len(keys) * size) + (4 if show_row else 0)))

    for row_num, data in enumerate(data_list, 1):
        print((f"{row_num:<4}" if show_row else ""), *[f"{data[key] if key in data else '-':<{size}}" for key in keys])

    if not data_list:
        print(f"is empty")

    print("-" * ((len(keys) * size) + (4 if show_row else 0)))


def search_list_dict(data_list : list[dict], /, *, value: Any, key: Hashable | None):
    res = []

    for data in data_list:
        if key is not None and data[key] == value:
            res.append(data)
        
        elif key is None and value in data.values():
            res.append(data)

    return res


def show_top_students(student_list: list[dict], grade_key: str, is_average: bool = False):

    if is_average:
        max_average_score = max((std["python_grade"] + std["java_grade"] + std["php_grade"]) / 3 for std in student_list)

        top_students = list(filter(lambda std: (std["python_grade"] + std["java_grade"] + std["php_grade"]) / 3 == max_average_score, student_list,))

        for student in top_students:
            student["average"] = f"{(student['python_grade'] + student['java_grade'] + student['php_grade']) / 3:.2f}"
    else:
        max_grade = max(student[grade_key] for student in student_list)
        top_students = list(filter(lambda std: std[grade_key] == max_grade, student_list))

    if is_average:
        display_list_dict(top_students, "code", "name", "family", "gender", "status", "phone", "national_code",
                          "student_code", "python_grade", "java_grade", "php_grade", "average", size=15)
    else:
        display_list_dict(top_students, "code", "name", "family", "gender", "status", "phone", "national_code",
                          "student_code", "python_grade", "java_grade", "php_grade", size=15)