"""
attendence.py

Draw a bar chart of the weekly attendence.
"""

import tkinter

root = tkinter.Tk()
root.title("Python INFO1-CE9990 Summer 2017 Section 2 Attendence")

attendence = [
    20, #week  1
    18, #week  2
    17, #week  3
    16, #week  4
     0, #week  5
     0, #week  6
     0, #week  7
     0, #week  8
     0, #week  9
     0  #week 10
]

n = len(attendence) #number of lectures
enrollment = 20     #number of students

barWidth = 30                     #in pixels
gap = int(barWidth / 2)           #between bars
studentHeight = int(barWidth / 2) #height of one student
barHeight = enrollment * studentHeight

#Dimenensions of root.
width = gap + n * (barWidth + gap)
height = barHeight + 2 * gap
root.geometry(str(width) + "x" + str(height))

background = "yellow"
canvas = tkinter.Canvas(root, background = background, highlightthickness = 0)
#distance from top edge of root to bottom edge of each bar
bottom = gap + barHeight

for i, a in enumerate(attendence):
    #distance from left edge of root to left edge of this bar
    left = gap + i * (barWidth + gap)
    #distance from left edge of root to right edge of this bar
    right = left + barWidth

    average = (left + right) / 2
    canvas.create_text(average, bottom, text = str(i + 1), anchor = tkinter.N)

    if a > 0:
        #distance from top edge of root to top edge of this bar
        top = gap + (enrollment - a) * studentHeight
        canvas.create_rectangle(left, top, right, bottom, fill = "black")
        canvas.create_text(average, top, text = str(a), anchor = tkinter.N,
            fill = background)

canvas.pack(expand = tkinter.YES, fill = "both")
root.mainloop()
