import datetime as date

# Error codes
YEAR_OUT_OF_RANGE  = 0b1
MONTH_OUT_OF_RANGE = 0b01
DAY_OUT_OF_RANGE   = 0b001

def validate_date(m, d, y, future_ok=False):
    errors = 0

    if m < 1 or m > 12:
        errors = errors | MONTH_OUT_OF_RANGE
    
    if d < 1  or m > 31:
        errors = errors | DAY_OUT_OF_RANGE
    
    if future_ok and y > date.date.today().year:
        errors = errors | YEAR_OUT_OF_RANGE

    return errors

def parse_date(datestr):
    date_vals = datestr.split("/")
    for i in range(len(date_vals)):
        try:
            date_vals[i] = int(date_vals[i])
        except ValueError:
            date_vals[i] = 0
            
    return date_vals



def main():
    indate = input("Enter a date (dd/mm/yyyy) ")

    indate = parse_date(indate)

    error = validate_date(indate[1], indate[0], indate[2])

    if error:
        error_str = "Invalid value for the following input:\n"
        if error & YEAR_OUT_OF_RANGE:
            error_str += "- year\n"
        if error & MONTH_OUT_OF_RANGE:
            error_str += "- month\n"
        if error & DAY_OUT_OF_RANGE:
            error_str += "- day\n"
    
        print(error_str, end="")



if __name__ == "__main__":
    main()