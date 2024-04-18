frappe.ui.form.on('Employee External Work History', {
	custom_start_date: function(frm, cdt, cdn) {

        let row = locals[cdt][cdn];
        if (row.custom_start_date && row.custom_end_date){
            var date1 = new Date(row.custom_start_date);
            var date2 = new Date(row.custom_end_date);

            var date_diff = date2.getFullYear() - date1.getFullYear();
        }
        row.total_experience = date_diff;
        refresh_field("total_experience", cdn, "external_work_history");
	},

    custom_end_date: function(frm, cdt, cdn) {

        let row = locals[cdt][cdn];
        if (row.custom_start_date && row.custom_end_date){
            var date1 = new Date(row.custom_start_date);
            var date2 = new Date(row.custom_end_date);

            var date_diff = date2.getFullYear() - date1.getFullYear();
        }
        row.total_experience = date_diff;
        refresh_field("total_experience", cdn, "external_work_history");
	},

});


frappe.ui.form.on('Employee', {
    custom_first_experience_date: function(frm) {
        let employee = frm.doc; 

        if (employee.custom_first_experience_date) {
            let firstExperienceDate = new Date(employee.custom_first_experience_date);
            let today = new Date();

            let date1_year = firstExperienceDate.getFullYear();
            let date2_year = today.getFullYear();
            let date1_month = firstExperienceDate.getMonth();
            let date2_month = today.getMonth();

            let diff_in_months = (date2_year - date1_year) * 12 + (date2_month - date1_month);

            console.log(diff_in_months);

            frm.set_value('custom_experience_in_months', diff_in_months);
        }
    }
});