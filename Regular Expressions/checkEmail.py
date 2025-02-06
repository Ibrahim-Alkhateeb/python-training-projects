import re


def check_email_patten(email):
    # pattern= re.search(r'^[A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$', email)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    email= input('please enter your email: \n')

    if check_email_patten(email):
        print('valid email')
        print(email)
    else:
        print(f'not valid email \n', 'ex: example_email-1@mail.com')
if __name__ == "__main__":
    main()