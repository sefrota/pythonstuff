def solve_eq(eq_input):
    a_list = eq_input.split()
    print("X =", int(a_list[4]) - int(a_list[2]))


equation = input("Enter the equation (i.e. X + 5 = 3) :")
solve_eq(equation)
