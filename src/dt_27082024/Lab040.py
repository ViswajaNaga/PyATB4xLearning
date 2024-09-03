# Decorators are used to add extra functionality
# Decorators are also used for logging purpose (add logs to the automation like program started and program ended)
import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"time taken by function is {end_time - start_time}")

    return wrapper()


@time_decorator
def test_ui1():
    print("Time taken by test_ui1 function")
    time.sleep(2)
@time_decorator
def test_ui2():
    print("Time taken by test_ui2 function")
    time.sleep(5)