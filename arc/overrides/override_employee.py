import frappe
from datetime import datetime

# def get_months_diff(date1, date2):
#     return (date1.year - date2.year) * 12 + date1.month - date2.month

# def calculate_number_of_months(doc, method):
#     first_experience_str = doc.custom_first_experience_date
   
#     today = datetime.now()
#     first_experience = datetime.strptime(first_experience_str, "%Y-%m-%d")
#     diff_in_months = get_months_diff(today, first_experience)
#     doc.custom_experience_in_months = diff_in_months
#     frappe.db.commit()


# Get all employees and insert new employee
def get_and_insert_employee(doc, method):

    #Get Employees
    emp = frappe.db.sql("""
        SELECT name FROM `tabEmployee` WHERE gender = 'Female' || gender = 'Male'""", as_dict=1)
    
    #Insert Employee
    # new_emp = frappe.db.sql("""
    #     INSERT INTO tabEmployee (first_name, gender, date_of_birth, date_of_joining,
    #                         status, company, name) VALUES ('Mahmoud', 'Male', '2001-1-2',
    #                         '2024-04-03', 'Active', 'S', 'HR-EMP-00003');""", as_dict=1)
    
    # print("\n\n")
    # print(emp)