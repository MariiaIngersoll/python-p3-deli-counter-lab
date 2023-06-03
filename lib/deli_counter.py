
def line(katz_deli):
    if not katz_deli:
       print("The line is currently empty.")
    else:
        line = "The line is currently:"
        for i in range(len(katz_deli)):
            line +=f" {i + 1}. {katz_deli[i]}"
        print(line)


def take_a_number(katz_line, name):
    katz_line.append(name)
    print(f"Welcome, {name}. You are number {len(katz_line)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])
