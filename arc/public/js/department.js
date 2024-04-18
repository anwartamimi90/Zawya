// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Department", {
	
	refresh: function (frm) {
		frm.set_query("custom_manager_of_the_department", function(){
            return{
                filters: {
                    "department": frm.doc.custom_the_department_manager
                }
            };
        });
	}
});
