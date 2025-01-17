def add_before_ui_after_ui(func):  # func-->this is custom function where u want extra functionality

    def wrapper():
        print("Before running the UI testacse")
        print("open the browser")
        func()
        print("After running the UI testacse")
        print("close the browser")

    return wrapper()
@add_before_ui_after_ui
def ui_testcase():
    print("I will test UI")