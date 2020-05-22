import time

def some_long_function(some_input):
    with open("database.txt", "a+") as out_file:
        time.sleep(10)
        out_file.write(some_input + "\n")
        return