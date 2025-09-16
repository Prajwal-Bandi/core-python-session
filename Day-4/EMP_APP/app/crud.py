from app.models import  db,Employee


def create_employee(employee):
    employee_model=Employee(
        id=employee['id'],
        name=employee['name'],
        age=employee['age'],
        salary=employee['salary'],
        is_active=employee['is_active']
    )
    db.session.add(employee_model) # Insert statement to db 
    db.session.commit()

def read_all_employee():
    employees=db.session.query(Employee).all()
    dict_employee=[]
    for employee in employees:
        employee_dict=employee.to_dict()
        dict_employee.append(employee_dict)
    return dict_employee



def read_model_by_id(id):
    employee=db.session.query(Employee).filter_by(id=id).first()    
    return employee


def read_by_id(id):
    employee=read_model_by_id(id)
    if not employee:
        return None
        
    
    employee_dict=employee.to_dict()
    return employee_dict
    

def update(id, new_employee):#new_employee is update at id
    employee=read_all_employee(id)
    if not employee:
        return None
    employee.salary=new_employee['salary']
    db.session.commit()
    
def delete_employee(id):
  employee=read_all_employee(id)
  if not employee:
      return None
  db.session.delete(employee)
  db.session.commit()