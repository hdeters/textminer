import re

def binary(string):
    return not re.search(r'^$|[A-Za-z2-9]', string)

def binary_even(string):
    if binary(string) and string[-1] == '0':
        return True
    else:
        return False

def hex(string):
    return not re.search(r'^$|[G-Zg-z]', string)

def word(string):
    return re.search(r'[a-z]+\w[^\*]$', string)

def words(string, count=None):
    if count == 1:
        return re.search(r'^([0-9]+-)?[a-z]+\w(^\*|!)?$', string)
    elif count == 2:
        return re.search(r'^([0-9]+-)?[a-z]+\w(^\*|!)?\s([a-z]+\w[^\*!])$', string)
    elif count == 3:
        return re.search(r'^([0-9]+-)?[a-z]+\w(^\*|!)?\s([a-z]+\w[^\*!])\s([a-z]+\w[^\*!])$', string)
    elif count == None:
        return re.search(r'^([0-9]+-)?[a-z]+\w(^\*|!)?\s?([a-z]+\w[^\*!])?\s?([a-z]+\w[^\*!])?$', string)
    else: return False

def phone_number(string):
    return re.search(r'\(?(\d{3})\)?[\-\.]?\s*(\d{3})[\-\.]?(\d{4})', string)

def money(string):
    return re.search(r'^\${1}\d+(,+\d{3}|\.\d{2})?(,+\d{3}|\.\d{2})?(,+\d{3}|\.\d{2})?$', string)

def zipcode(string):
    return re.search(r'^\d{5}(-\d{4})?$', string)

def date(string):
    return re.search(r'^\d{1,4}(-|/)\d{1,2}(-|/)\d{2,4}$', string)

