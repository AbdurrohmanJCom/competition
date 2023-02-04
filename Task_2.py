def string(given_str, search_str):
    if search_str.find(given_str):
        return '\nThe word you wrote is in this sentence!'
    else:
        return '\nthe word you wrote isn\'t in this sentence!!\n search another one! '


search_str = input('Write word which you want to find : ')
print(string('Hi, my name is Abdurahmon, and this is my friend Firdavs', search_str))


