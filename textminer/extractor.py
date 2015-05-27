import re

def phone_numbers(string):
    number = re.findall(r'(\(?\d{3}\)?[\-\.]?\s*?\d{3}[\-\.]?\d{4})', string)
    return number

def emails(string):
    emails = re.findall(r'(\w+?\.?\w+@\w+\.\w{2,3})', string)
    return emails