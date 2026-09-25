# https://cs50.harvard.edu/python/psets/3/outdated/

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}
while True:
    try:
        date = input("Date: ").title()
        if len(date.split("/")) == 3:
            mm, dd, yyyy = date.split("/")
            mm = int(mm)
            dd = int(dd)
            yyyy = int (yyyy)
            if mm < 1 or mm > 12 or dd < 1 or dd > 31 or yyyy < 0:
                raise ValueError
            print(f"{yyyy:04}-{mm:02}-{dd:02}")
        elif len(date.split()) == 3:
            mm, dd, yyyy =  date.split()
            if not dd.endswith(","):
                raise ValueError
            dd = int(dd.removesuffix(","))
            yyyy = int(yyyy)
            if mm not in months or dd < 1 or dd > 31 or int(yyyy)< 0:
                raise ValueError 
            print(f"{yyyy:04}-{months[mm]}-{dd:02}")
        else:
            raise ValueError
    except ValueError:
        continue
    break
