import frappe
from hrms.hr.doctype.employee_transfer.employee_transfer import EmployeeTransfer
from hrms.hr.utils import (update_to_date_in_work_history,
                           delete_employee_work_history,
                           get_formatted_value)

class CustomEmployeeTransfer(EmployeeTransfer):
 
    def validate(self):
        employee = frappe.get_doc("Employee", self.employee)
        if self.create_new_employee_id:
            new_employee = frappe.copy_doc(employee)
            new_employee.name = None
            new_employee.employee_number = None
            self.override_update_employee_work_history(
                new_employee, self.transfer_details, date=self.transfer_date
            )
            if self.new_company and self.company != self.new_company:
                new_employee.internal_work_history = []
                new_employee.date_of_joining = self.transfer_date
                new_employee.company = self.new_company
            # move user_id to new employee before insert
            if employee.user_id and not self.validate_user_in_details():
                new_employee.user_id = employee.user_id
                employee.db_set("user_id", "")
            new_employee.insert()
            self.db_set("new_employee_id", new_employee.name)
            # relieve the old employee
            employee.db_set("relieving_date", self.transfer_date)
            employee.db_set("status", "Left")
        else:
            self.override_update_employee_work_history(
                employee, self.transfer_details, date=self.transfer_date
            )
            if self.new_company and self.company != self.new_company:
                employee.company = self.new_company
                employee.date_of_joining = self.transfer_date
            employee.save()

    def override_update_employee_work_history(self, employee, details, date=None, cancel=False):
        # Implementation of override_update_employee_work_history
        if not details:
            return employee
    
        if not employee.internal_work_history and not cancel:
            employee.append(
                "internal_work_history",
                {
                    "branch": employee.branch,
                    "designation": employee.designation,
                    "department": employee.department,
                    "from_date": employee.date_of_joining,
                    "grade": employee.grade #changed
                }
            )
        
        internal_work_history = {}
        for item in details:
            field = frappe.get_meta("Employee").get_field(item.fieldname)
            if not field:
                continue

            new_value = item.new if not cancel else item.current
            new_value = get_formatted_value(new_value, field.fieldtype)
            setattr(employee, item.fieldname, new_value)

            if item.fieldname in ["department", "designation", "branch", "grade"]:
                internal_work_history[item.fieldname] = item.new

        if internal_work_history and not cancel:
            internal_work_history["from_date"] = date
            employee.append("internal_work_history", internal_work_history)

        if cancel:
            delete_employee_work_history(details, employee, date)

        update_to_date_in_work_history(employee, cancel)

        return employee

             