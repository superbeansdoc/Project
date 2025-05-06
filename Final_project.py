import tkinter as tk
import time
global x1,x2
root = tk.Tk()

def start_game():
    global cow1
    cow1.pack_forget()
    button.pack_forget()
    cow = tk.Canvas(root,width=2000,height=1000,bg="blue")
    cow.pack()


    rectangle = cow.create_rectangle(50, 50, 100, 10, fill="tan")
    rectangle2 = cow.create_rectangle(80, 90, 70, 50, fill="tan")
    rectangle3 = cow.create_rectangle(110, 190, 40, 90, fill="red")
    rectangle4  = cow.create_rectangle(70, 20, 60, 30, fill="black")
    rectangle5 = cow.create_rectangle(80, 20, 90, 30, fill="black")
    rectangle6 = cow.create_rectangle(0,610,2000,1000, fill = "green")
    coords2 = cow.coords(rectangle2)
    coords = cow.coords(rectangle)
    coords3 = cow.coords(rectangle3)
    coords4 = cow.coords(rectangle5)
    coords5 = cow.coords(rectangle4)
    def get_bottem_y():
        global y1
        y1 = cow.coords(rectangle3)[3]
    def starting_spot():
        cow.coords(rectangle2,50, 500, 100, 450,)
        cow.coords(rectangle,80, 510, 70, 470,)
        cow.coords(rectangle3,110, 610, 40, 510,)
        cow.coords(rectangle4,70, 470, 60, 460,)
        cow.coords(rectangle5,80, 470, 90, 460,)
    def update_y():
        global y1
        y1 = cow.coords(rectangle3)[3]
        cow.after(100,update_y)

    def move_left():
        cow.move(rectangle, -5, 0)
        cow.move(rectangle2, -5, 0)
        cow.move(rectangle3, -5, 0)
        cow.move(rectangle4, -5, 0)
        cow.move(rectangle5, -5, 0)
    def move_right():
        cow.move(rectangle, 5, 0)
        cow.move(rectangle2, 5, 0)
        cow.move(rectangle3, 5, 0)
        cow.move(rectangle4, 5, 0)
        cow.move(rectangle5, 5, 0)
    def move_up():
        cow.move(rectangle, 0, -120)
        cow.move(rectangle2, 0, -120)
        cow.move(rectangle3, 0, -120)
        cow.move(rectangle4, 0, -120)
        cow.move(rectangle5, 0, -120)
    

    def move_down():
        cow.move(rectangle, 0, 120)
        cow.move(rectangle2, 0, 120)
        cow.move(rectangle3, 0, 120)
        cow.move(rectangle4, 0, 120)
        cow.move(rectangle5, 0, 120)
    def key_pressed(event):
        if event.keysym == 'Left':
            move_left()
        if event.keysym == 'Right':
            move_right()
        if event.keysym == 'Up': 
            if y1 < 610:  
                print("no jump")
                print(y1)
            else:
                move_up()
                cow.after(1000,move_down)
                print(y1)
        if event.keysym == 'r':
            starting_spot()
    starting_spot()
    root.bind("<Key>", key_pressed)
    
    update_y()
    root.mainloop()

button = tk.Button(text= "start_game", width=10, height=10,command= start_game, bg = "Black")
cow1 = tk.Canvas(root,width=2000,height=1000,bg="green", )
cow1.pack()
button.place(x = 1000, y = 1000)
start_game()
root.mainloop()
