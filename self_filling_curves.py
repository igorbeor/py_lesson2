def l_system(axiom, rules, n):
    command_str = axiom
    for i in range(n):
        command_str = "".join(rules.get(c, c) for c in command_str)
    return command_str

def draw_curve(turtle, l_str, angle):
    for c in l_str:
        if c == 'F':
            turtle.forward(5)
        elif c == '+':
            turtle.right(angle)
        elif c == '-':
            turtle.left(angle)