import frappe

def cron():

    employees = frappe.get_all("Employee", fields=["name", "custom_experience_in_months"])

    for employee in employees:
        employee_name = employee.name
        employee_exp = employee.custom_experience_in_months
        new_exp = employee_exp + 1
        
        frappe.db.set_value("Employee", employee_name, "custom_experience_in_months", new_exp)

    frappe.db.commit()