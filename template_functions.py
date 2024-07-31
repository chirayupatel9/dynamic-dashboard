# Write functions are can be later with other functions
from decimal import Decimal
from datetime import datetime

ALLOWED_EXTENSIONS = {'txt', 'csv', 'CSV'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def convert_to_yyyy_mm_dd(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                print("Unrecognized date format", date_str)
                return None
