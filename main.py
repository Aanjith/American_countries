import turtle
import pandas
data=pandas.read_csv("50_states.csv")
screen=turtle.Screen()
screen.title("state game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

timmy=turtle.Turtle()
timmy.hideturtle()
timmy.penup()

guess=0
def write(text,tup):
    timmy.goto(tup)
    timmy.write(text)

guessed=[]
while guess<51:
    tupx=0
    tupy=0
    input=screen.textinput(title=f"guessed {guess}/50 state(s)", prompt=" en ter state")
    input=input.title()
    for i in data.state:
        if input==i and input not in guessed:
            row=data[data.state==i]
            for x in row.x:
                tupx=x
            for y in row.y:
                tupy=y
            write(input,(tupx,tupy))
            guess+=1
            guessed.append(input)




screen.exitonclick()