import re
# # 415-555-1234
#
# def isPhoneNumber(text):
#
#     if len(text) != 12:
#         return False
#
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#
#     if text[3] != '-':
#        return False
#
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#
#     if text[7] != '-':
#         return False
#
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#
#     return True
#
# print('Is 415-555-4242 a phone number?')
# print(isPhoneNumber('415-555-4242'))
# print('Is Hello hello a phone number?')
# print(isPhoneNumber('Hello hello'))

# //////////////////////////////////////////////
# //////////////////////////////////////////////
# //////////////////////////////////////////////

def isPhoneNmber(text):
    is_phone= re.search(r'\d{3}-\d{3}-\d{4}', text)

    if is_phone:
        return f'the {text} is valid phone number'
    else:
        return f'the {text} is NOT valid phone number'

phoneNumber = input('please enter your phone number: \n')

print(f'is {phoneNumber} a phone number?')
print(isPhoneNmber(phoneNumber))

