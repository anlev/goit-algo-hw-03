import turtle


def koch_curve(t, length, level):
    """Draw a Koch curve with given length and recursion level."""
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)


def koch_snowflake(t, length, level):
    """Draw a Koch snowflake by drawing three Koch curves."""
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    # User input for recursion level
    level = int(input("Enter recursion level (e.g., 0-5): "))
    length = 300  # Initial length of the snowflake side

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    koch_snowflake(t, length, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
