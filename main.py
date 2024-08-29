from datetime import datetime

def main():
    #start prograam here
    name = input('What is your name? ')
    birth_month = input('What is your birthday month? ')
    current_month = get_current_month()
    if compare_case_insensitive(birth_month, current_month):
        print(f'Happy birthday month {name}!')

def get_current_month():
    today = datetime.today()
    month_text = today.strftime('%B')
    return month_text

def compare_case_insensitive(st1, st2):
    return st1.lower() == st2.lower()

#rememeber to call main function!
main()