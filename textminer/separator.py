import re

def words(string):
    result = re.findall(r'(\b[^\s]+[a-z]+\b)', string)
    if result == []:
        return None
    else:
        return result

def phone_number(string):
    number = re.match(r'\(?(\d{3})\)?[\-\.]?\s*?(\d{3})[\-\.]?(\d{4})', string)
    if number == None:
        return None
    else:
        return {"area_code": number.group(1),
                "number": number.group(2)+"-"+number.group(3)}

def money(string):
    money = re.match(r'^(\$)(\d+(,?\d{3,})*\.?(\d{2})?)$', string)
    if money == None:
        return None
    else:
        money2 = money.group(2).replace(',','')
        return {"currency": money.group(1),
                "amount": float(money2)}

def zipcode(string):
    zip = re.match(r'^(\d{5})-?(\d{4})?$', string)
    if zip == None:
        return None
    else:
        return {"zip": zip.group(1),
                "plus4": zip.group(2)}

def date(string):
    the_date = re.match(r'^(\d{1,4})[-|/](\d{1,2})[-|/](\d{1,4})$', string)
    if the_date == None:
        return None
    else:
        if int(the_date.group(1)) > 1000:
            year = int(the_date.group(1))
            month = int(the_date.group(2))
            day = int(the_date.group(3))
        elif int(the_date.group(3)) > 1000:
            year = int(the_date.group(3))
            month = int(the_date.group(1))
            day = int(the_date.group(2))
        return {"month": month,
                "day": day,
                "year": year}