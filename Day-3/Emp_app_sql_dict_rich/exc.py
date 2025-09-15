class EmployeeException(Exception):
    pass

class EmployeeNotFound(EmployeeException):
    pass

class EmpoyeeAlreadyExist(EmployeeException):
    pass

class DatabaseError(EmployeeException):
    pass
    