# Create a program which takes a sentence as your birth dau (YYYY:MM:DD
# The program should return sum of all numbers, bigest and lowest number
# division and days with power of month (dd ** mm)The code should be structured
# correctly: functions, error handling and logging.
import re
import logging
# from datetime import datetime
from typing import List

logging.basicConfig(level=logging.DEBUG, filename='error.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def check_date_format(birt_date: str):
    date_pattern = r'^\d{4}:\d{2}:\d{2}$'
    if re.match(date_pattern, birt_date):
        return True
    else:
        return False


# def check_date_format(birt_date: str) -> bool:
#     format = '%Y:%m:%d'
#     try:
#         date_form = datetime.strptime(birt_date, format)
#         logging.debug(f"Data entered: {date_form}")
#     except Exception as err:
#         logging.error(f"Problem in check_date_format function {err}")


def sum_date(date_list: List[float]) -> float:
    return sum(date_list)


def divide_num(date_list: List[float]) -> float:
    try:
        div_num = max(date_list)/min(date_list)
        return div_num
    except ZeroDivisionError:
        logging.warning(f"Division from {min(date_list)}")
    except Exception as err:
        logging.error(err)
    

def day_pow_month(text: str) -> float:
    date_list = text.split(":")
    return float(date_list[2]) ** float(date_list[1])

user_date = input("Please enter the birth day with format YYYY:MM:DD: ")

while check_date_format(user_date) == False:
    user_date = input("Please renter the birth day with format YYYY:MM:DD: ")
    logging.debug(check_date_format(user_date))

date_list = []
[date_list.append(float(num)) for num in user_date if num.isalnum()] 
print(f"Sum of date numbers: {sum_date(date_list)}")
print(divide_num(date_list))
print(day_pow_month(user_date))



