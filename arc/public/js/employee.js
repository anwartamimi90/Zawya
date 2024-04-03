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
