import string
ascii = list(string.ascii_lowercase)

def anything(check_is_pangram):
    check_is_pangram = check_is_pangram.lower()
    for i in ascii:
        if check_is_pangram.find(i) != -1:
            pass
        else:
            return False
        return True
str_sent = input('')
print(anything(str_sent))