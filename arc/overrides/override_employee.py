from datetime import datetime

def get_months_diff(date1, date2):
    return (date1.year - date2.year) * 12 + date1.month - date2.month

def calculate_number_of_months(doc, method):
    first_experience_str = doc.custom_first_experience_date
   
    today = datetime.now()
    first_experience = datetime.strptime(first_experience_str, "%Y-%m-%d")  # Assuming the format is YYYY-MM-DD
    diff_in_months = get_months_diff(today, first_experience)
    print("Difference in months:", diff_in_months)
    doc.custom_experience_in_months = diff_in_months

