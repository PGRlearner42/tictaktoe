import turtle as t
import random as r

sn = t.Screen()
sn.setup(600,600)
sn.tracer(0)
placea = [-100,0,100]
placeb = [-100,0,100]
row_list = []
for i in placea:
    for j in placeb:
        sq = t.Turtle()
        sq.shape('square')
        sq.color('black','white')
        sq.shapesize(5)
        sq.goto(i,j)
        row_list.append(sq)
colors = ['blue','purple']
r_color = r.choice(colors)

board = t.Turtle()
board.penup()
board.hideturtle()
board.goto(-280,280)

top_row = [2,5,8]
middle_row = [1,4,7]
bottom_row = [0,3,6]

left_col = [0,1,2]
middle_col = [3,4,5]
right_col = [6,7,8]

diag_1 = [0,4,8]
diag_2 = [2,4,6]
def box_color(ind):
    global r_color
    if r_color == 'blue':
        r_color = 'purple'
    elif r_color == 'purple':
        r_color = 'blue'
    
    if row_list[ind].color() == ('black', 'purple'):
        row_list[ind].color() = ('black', 'purple')
    elif row_list[ind].color() == ('black','blue'):
        row_list[ind].color() = ('black', 'blue')
    row_list[ind].color('black', r_color)
    
    row_index = row_list.index(row_list[ind])
    if row_index in top_row:
        top_row.remove(row_index)
        print(top_row)
    elif row_index in middle_row:
        middle_row.remove(row_index)
        print(middle_row)
    elif row_index in bottom_row:
        bottom_row.remove(row_index)
        print(bottom_row)

    if row_index in left_col:
        left_col.remove(row_index)
        print(left_col)
    elif row_index in middle_col:
        middle_col.remove(row_index)
        print(middle_col)
    elif row_index in right_col:
        right_col.remove(row_index)
        print(right_col)

    if row_index in diag_1:
        diag_1.remove(row_index)
        print(diag_1)
    elif row_index in diag_2:
        diag_2.remove(row_index)
        print(diag_2)
    
def change_color(x,y):
    board.clear()
    if x > -150 and x < -50:
        if y > 50 and y < 150:
            board.write('top left')
            num = 2
        elif y < 50 and y > -50:
            board.write('middle left')
            num = 1
        elif y < -50 and y > -150:
            board.write('bottom middle')
            num = 0
    elif x > -50 and x < 50:
        if y > 50 and y < 150:
            board.write('top middle')
            num = 5
        elif y < 50 and y > -50:
            board.write('middle')
            num = 4
        elif y < -50 and y > -150:
            board.write('bottom middle')
            num = 3
    elif x > 50 and x < 150:
        if y > 50 and y < 150:
            board.write('top left')
            num = 8
        elif y < 50 and y > -50:
            board.write('middle left')
            num = 7
        elif y < -50 and y > -150:
            board.write('bottom left')
            num = 6
    if x > 150 or x < -150 or y < -150 or y > 150:
        board.write('out of bounds')
    box_color(num)
sn.onclick(change_color)

while True:
    t.update()