from turtle import Screen, Turtle

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

if __name__ == '__main__':

    # drow gosper curve
    gosper_axiom = 'XF'
    gosper_rules = {
        'X': 'X-YF--YF+FX++FXFX+YF-',
        'Y': '+FX-YFYF--YF-FX++FX+Y'
        }
    gosper_curve = l_system(gosper_axiom, gosper_rules, 4)
    gosper_screen = Screen()
    gosper_screen.title('Gosper curve')
    gosper_turtle = Turtle()
    gosper_turtle.speed('fastest')
    draw_curve(gosper_turtle, gosper_curve, 60)
    gosper_screen.exitonclick()