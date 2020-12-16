from turtle import *
shape("turtle")

speed(5)  # draw faster

fd(80)  # bottom of the house
lt(90)
fd(80)  # straight wall

# the roof
lt(30)
fd(80)
lt(120)
fd(80)

lt(120)
fd(80)  # height
lt(180)
fd(80)

lt(90)
fd(80)  # left wall
lt(90)
fd(20)
lt(90)

fd(40)  # door (left wall)
rt(90)
fd(40)  # door (top)
rt(90)
fd(40)  # door (right wall)