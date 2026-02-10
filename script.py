# this is my new learning python file which i created in my repository
# go to files and click add file then enter  the name of file for python file add .py 
#then commit the cahnges to save it
print("this is my first gitHub python file")
# Program to print the table of 2

def print_table(number):
    print("Multiplication Table of", number)
    print("---------------------------")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Main program
if __name__ == "__main__":
    num = 2
    print_table(num)
