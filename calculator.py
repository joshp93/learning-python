
def startup():
    print("Hello there. Just type in the equation you with to solve...")
    print_operators()
    print("To see this list of operators, just type 'help'. To close the application type 'exit'")
    solve_equation()


def print_operators():
    print("* times")
    print("/ divide")
    print("+ plus")
    print("- minus")
    print("** power")


def solve_equation():
    equation = '';
    try:
        equation = read_input()
        if equation != 'exit':
            print(eval(equation))
    except ZeroDivisionError as z:
        print("You can't divide by zero, that's a mathmatical nono...")
        print(z)
    except Exception as e:
        print("Looks like something went wrong...")
        print(e)
    finally:
        if equation != 'exit' and equation != '':
            solve_equation()

def read_input():
    equation = input(">> ")
    if equation == 'help':
        print_operators_and_go_again()
        return
    if equation == 'exit':
        return 'exit'
    times_index = equation.find("*")
    divide_index = equation.find("/")
    power_index = equation.find("**")
    plus_index = equation.find("+")
    minus_index = equation.find("-")
    if times_index == -1 and divide_index == -1 and power_index == -1 and plus_index == -1 and minus_index == -1:
        print("Your input isn't supported.")
        print_operators_and_go_again()
        return
    return equation

def print_operators_and_go_again():
    print_operators()
    solve_equation()

startup()
