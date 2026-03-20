import sys

def add(a, b):
    print("Result:", int(a) + int(b))

def greet(name):
    print(f"Hello, {name}! Welcome to CLI Tool.")

def help_menu():
    print("""
Available commands:
add <num1> <num2>     → Add two numbers
greet <name>          → Greet user
""")

# Main logic
if len(sys.argv) < 2:
    help_menu()
else:
    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 4:
        add(sys.argv[2], sys.argv[3])
    elif command == "greet" and len(sys.argv) == 3:
        greet(sys.argv[2])
    else:
        print("Invalid command")
        help_menu()
