# Hurdle #3
```python
def turn_right():
    for i in range(3):
        turn_left()

def walk(step):
    for i in range(step):
        move()

def around():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal()==False:
    if wall_in_front():
        around()
    else:
        move()
```

# Hurdle #4
```python
def turn_right():
    for i in range(3):
        turn_left()

def walk(step):
    for i in range(step):
        move()
      
def pillar():
    turn_left()
    i = 0
    while not right_is_clear():
        move()
        i += 1
    turn_right()
    move()
    turn_right()
    walk(i)
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        pillar()
```

# Maze

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```