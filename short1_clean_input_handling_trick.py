def do_this():
    print("Do this")

def do_that():
    print("Do that")

# clean input handling
match input("Do this or that?"):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print("Invalid input")