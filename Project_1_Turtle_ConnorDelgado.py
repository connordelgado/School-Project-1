#######################################################
# Name:       Connor Delgado
# Class:      CIS-1400
# Assignment: Project 1 - Turtle
# File:       Project_1-turtle.py
# Purpose:    Draw all shapes
#######################################################

# imports for all settings
from turtle import *
from random import randint

# settings for screen
title('Turtle Race')
setup(800, 500)
speed(0)

# sets up a heading stating turtle race
penup()
goto(-30, 200)
color('white')
write("Turtle Race", font=("Arial", "24", "bold"))


# the main module
def main():
    raceLoop()
    print("We're done racing!")


# loop to make the change track option come back up and race again option
def raceLoop():
    changeTrack = True
    raceAgain = True
    while raceAgain:
        if changeTrack:
            quit = raceTrack()  # loop to quit
            if quit:
                return
        race()  # calls race

        raceAgainRaw = input('Do you want to race again? (Enter yes or no): ')
        # note that anything other than 'yes' will indicate false
        raceAgain = True if raceAgainRaw == 'yes' else False
        # three lines turned into one makes race happen if yes
        # or stop if no
        if raceAgain is False:
            return

        changeTrackRaw = input('Do you want to change the track? (yes/no): ')
        # input to get track change
        # note that anything other than 'yes' will indicate false
        changeTrack = True if changeTrackRaw == 'yes' else False
        # changes track unless comes back no will carry on


# Module to decide what track you want to race on
def raceTrack():
    race_track = ""
    while race_track not in ['track', 'desert', 'quit']:

        # Allows the user to select the track they want to race on
        race_track = input(('Where would you like to race? (track/desert) \
            or quit out (quit): '))

        # track settings for track option
        if race_track == 'track':
            print('Creating Racetrack')
            bgcolor('green')  # sets fake grass background

            # sets up the fake dirt track
            goto(-180, 180)
            pendown()
            color('chocolate')
            begin_fill()
            for i in range(2):
                forward(400)
                right(90)
                forward(220)
                right(90)
            end_fill()

            # Finish Line Settings
            gap_size = 20
            shape("square")
            penup()

            # white squares row 1

            color('white')
            for i in range(5):
                goto(200, (150 - (i * gap_size * 2)))
                stamp()

            # white squares row 2

            for i in range(6):
                goto(200 + gap_size, (190 - gap_size) - (i * gap_size * 2))
                stamp()

            # sets up the black squares in row 1
            color('black')
            for i in range(6):
                goto(200, (170 - (i * gap_size * 2)))
                stamp()

            # Sets up the black squares in row 2

            for i in range(5):
                goto(200 + gap_size, ((170 - gap_size) - (i * gap_size * 2)))
                stamp()

            # sets up the race strip
            penup()
            goto(-140, 140)
            shape('arrow')
            color('white')
            for step in range(16):
                write(step, align='center')
                right(90)
                for num in range(8):
                    penup()
                    forward(10)
                    pendown()
                    forward(10)
                penup()
                backward(160)
                left(90)
                forward(20)

        # track settings for desert option
        elif race_track == 'desert':
            print('Creating Racetrack')
            bgcolor('tan')

            # sets up the fake sand track
            goto(-180, 180)
            pendown
            color('khaki')  # creates sand background
            begin_fill()
            for i in range(2):
                forward(400)
                right(90)
                forward(220)
                right(90)
            end_fill()

            # Finish Line Settings
            gap_size = 20
            shape("square")
            penup()

            # white squares row 1

            color('white')
            for i in range(5):
                goto(200, (150 - (i * gap_size * 2)))
                stamp()

            # white squares row 2

            for i in range(6):
                goto(200 + gap_size, (190 - gap_size) - (i * gap_size * 2))
                stamp()

            # sets up the black squares in row 1
            color('black')
            for i in range(6):
                goto(200, (170 - (i * gap_size * 2)))
                stamp()

            # Sets up the black squares in row 2

            for i in range(5):
                goto(200 + gap_size, ((170 - gap_size) - (i * gap_size * 2)))
                stamp()

            # sets up the race strip
            penup()
            goto(-140, 140)
            shape('arrow')
            color('black')
            for step in range(16):
                write(step, align='center')
                right(90)
                for num in range(8):
                    penup()
                    forward(10)
                    pendown()
                    forward(10)
                penup()
                backward(160)
                left(90)
                forward(20)

        elif race_track == 'quit':  # gives an option to quit out
            return True

        else:
            print("That's not an option!")
            # gives an option to re-enter if nonanswers are given
            return raceTrack()
            # return necessary or if entered wrong 3 times it will
            # loop incorrectly returns and
            # value to the wrong spot

        return False  # ends loop


# the function that controls the race
def race():
    # player 1 turtle settings
    player_1 = Turtle()
    player_1.color('yellow')
    player_1.shape('turtle')

    # sets player 1 at starting race point
    player_1.penup()
    player_1.goto(-160, 100)
    player_1.pendown()

    # makes the turtle do a spin
    for turn in range(10):
        player_1.right(36)

    # player 2 turtle settings
    player_2 = Turtle()
    player_2.color('blue')
    player_2.shape('turtle')

    # sets player 2 at starting race point
    player_2.penup()
    player_2.goto(-160, 70)
    player_2.pendown()

    # makes the turtle do a spin
    for turn in range(10):
        player_2.right(36)

    # player 3 turtle settings
    player_3 = Turtle()
    player_3.color('black')
    player_3.shape('turtle')

    # sets player 3 at starting race point
    player_3.penup()
    player_3.goto(-160, 40)
    player_3.pendown()

    # makes the turtle do a  spin
    for turn in range(10):
        player_3.right(36)

    # player 4 turtle settings
    player_4 = Turtle()
    player_4.color('green')
    player_4.shape('turtle')

    # sets player 4 turtle at race point
    player_4.penup()
    player_4.goto(-160, 10)
    player_4.pendown()

    # makes the rutle do a spin
    for turn in range(10):
        player_4.right(36)

    # prints a message that the race in starting
    print('Time to race!')

    # sets up the actual race by giving turtles random values for speed trying
    # to hit 205 to determine winner
    while (player_1.xcor() <= 205 and player_2.xcor() <= 205 and
           player_3.xcor() <= 205 and player_4.xcor() <= 205):
        player_1.forward(randint(1, 5))
        player_2.forward(randint(1, 5))
        player_3.forward(randint(1, 5))
        player_4.forward(randint(1, 5))

    # determines the winner and allows a celebration
    # yellow turtle wins
    if (player_1.xcor() > player_2.xcor() and player_1.xcor() >
            player_3.xcor() and player_1.xcor() > player_4.xcor()):
        print('Yellow Turtle Wins!')
        player_1.shapesize(2)
        player_1.backward(100)
        player_1.right(90)
        player_1.forward(30)
        player_1.right(60)
        player_1.forward(50)

    # blue turtle wins
    elif (player_2.xcor() > player_1.xcor() and player_2.xcor() >
          player_3.xcor() and player_2.xcor() > player_4.xcor()):
        print('Blue Turtle Wins!')
        player_2.shapesize(2)
        player_2.backward(100)
        player_2.right(90)
        player_2.forward(100)
        player_2.right(90)
        player_2.forward(100)
        player_2.right(90)
        player_2.forward(100)
        player_2.right(90)
        player_2.forward(100)

    # black turtle wins
    elif (player_3.xcor() > player_1.xcor() and player_3.xcor() >
          player_2.xcor() and player_3.xcor() > player_4.xcor()):
        print('Black Turtle Wins!')
        player_3.shapesize(2)
        player_3.backward(100)
        for i in range(5):
            player_3.forward(100)
            player_3.right(144)

    # green turtle wins
    elif (player_4.xcor() > player_1.xcor() and player_4.xcor() >
          player_2.xcor() and player_4.xcor() > player_3.xcor()):
        print('Green Turtle Wins!')
        player_4.shapesize(2)
        player_4.backward(100)
        r = 10
        n = 10
        for i in range(1, n + 1, 1):
            player_4.circle(r * i)

    # resets the race clears turtles
    player_1.clear()
    player_1.hideturtle()
    player_2.clear()
    player_2.hideturtle()
    player_3.clear()
    player_3.hideturtle()
    player_4.clear()
    player_4.hideturtle()


main()

# allows you to exit program by clicking
exitonclick()
