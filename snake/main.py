from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.move_right, 'Right')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_up, 'Up')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 18:
        food.is_eaten()
        speed = snake.head.speed()
        snake.add_square()
        scoreboard.update_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        is_game_on = False
        scoreboard.defeat()

    if snake.head.distance(snake.tail) < 15:
        is_game_on = False
        scoreboard.defeat()


screen.exitonclick()
