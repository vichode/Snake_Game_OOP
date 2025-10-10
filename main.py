import time
from turtle import Screen
from SnakeBody import Snake
from food import Food
from Scoreboard import scoreboard

snake = Snake()

My_screen = Screen()

food = Food()

My_screen.setup(width=600, height=600)
My_screen.bgcolor("light green")
My_screen.title("My Snake Game")
My_screen.tracer(0)

My_screen.listen()
My_screen.onkey(snake.left, "Left")
My_screen.onkey(snake.right, "Right")
My_screen.onkey(snake.up, "Up")
My_screen.onkey(snake.down, "Down")

score = scoreboard()

game_on = True
while game_on:
    My_screen.update()
    time.sleep(0.15)

    snake.move()

    #checking for collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        score.increase_score()

    #game over in collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_on = False
        score.game_over()

    #game over in collision with body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            score.game_over()





My_screen.exitonclick()