from typing import Iterable, Literal, Any
from os.path import isfile 


def save(path: str, data: str, mode: Literal["a", "w"] = "a") -> None:
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}
    file_object = None

    try:
        file_object = open(file=path, mode=mode)
        file_object.write(data)

    except BaseException as err:
        func_res["STATUS"] = False
        func_res["DATA"] = err
        return func_res
    
    else:
        return func_res

    finally:
        if file_object and (not file_object.closed):
            file_object.close()


def save_iter(path: str, data: Iterable[str], mode: Literal["a", "w"] = "a") -> None:
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}
    file_object = None

    try:
        file_object = open(file=path, mode=mode)
        file_object.writelines(data)

    except BaseException as err:
        func_res["STATUS"] = False
        func_res["DATA"] = err
        return func_res
    
    else:
        return func_res

    finally:
        if file_object and (not file_object.closed):
            file_object.close()


def load(path: str) -> list[Any]:
    func_res = {"STATUS":True, "MESSAGE":{}, "DATA":None}
    file_object = None

    try:
        if not isfile(path):
            file_object = open(file=path, mode="x")
            res = []
        else:
            file_object = open(file=path)
            res = file_object.readlines()

    except BaseException as err:
        func_res["STATUS"] = False
        func_res["DATA"] = err
        return func_res
    
    else:
        func_res["DATA"] = res
        return func_res

    finally:
        if file_object and (not file_object.closed):
            file_object.close()
