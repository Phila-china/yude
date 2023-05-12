import datetime


def timer(func):
    def inner(*arg):
        start_time = datetime.datetime.now()
        func(*arg)
        end_time = datetime.datetime.now()
        print(f"The duration of the fight is:{end_time - start_time}")
    return inner