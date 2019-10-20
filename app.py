from turtle import Screen, Turtle
from self_filling_curves import l_system, draw_curve

if __name__ == '__main__':

    # drow gosper curve
    gosper_axiom = 'XF'
    gosper_rules = {
        'X': 'X-YF--YF+FX++FXFX+YF-',
        'Y': '+FX-YFYF--YF-FX++FX+Y'
        }
    gosper_curve = l_system(gosper_axiom, gosper_rules, 4)
    screen = Screen()
    screen.title('Gosper curve')
    turtle = Turtle()
    turtle.speed('fastest')
    draw_curve(turtle, gosper_curve, 60)
    screen.exitonclick()