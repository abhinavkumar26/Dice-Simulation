
#-----------------------------------------------------------------------------------
''' A simple dice rolling simulator '''
#-----------------------------------------------------------------------------------

from tkinter import*
import random

root = Tk()
'''_______________________________________________________________________________________
    Importing all Dice face pictures
_______________________________________________________________________________________'''

one = PhotoImage(file = 'Side images/1.png')
two = PhotoImage(file = 'Side images/2.png')
three = PhotoImage(file = 'Side images/3.png')
four = PhotoImage(file = 'Side images/4.png')
five = PhotoImage(file = 'Side images/5.png')
six = PhotoImage(file = 'Side images/6.png')


'''_________________________________________________________________________
Setting up the window
____________________________________________________________________________'''


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.resizable(False,False)

window_width = 600
window_height = 400

x_coor = (screen_width/2) - (window_width/2)
y_coor = (screen_height/2) - (window_height/2)

root.geometry("%dx%d+%d+%d" % (window_width, window_height,x_coor,y_coor))

root.title("Dice roll simulator by Abhinav Kumar, github.com/abhinavkumar26")


#_____________________________________________________________________________

#Function to generate random number from 1 to 6
def roll_dice(event=0):
    choice = random.choice([1,2,3,4,5,6])
    print(choice)
    update_ui(choice)


def display_face(num,choice):
    dice_face["image"] = num
    dice_no["text"] = "It's a " + str(choice)
    root.update()


def update_ui(choice):
    if choice == 1:
        display_face(one,choice)

    elif choice == 2:
        display_face(two,choice)

    elif choice == 3:
        display_face(three,choice)

    elif choice == 4:
        display_face(four,choice)

    elif choice == 5:
        display_face(five,choice)

    else:
        display_face(six,choice)


#Button to roll the dice

roll_button = Button(root, text = "Let's roll!", command = roll_dice)
roll_button.pack(anchor = CENTER, side = BOTTOM, pady = 30)
#_____________________________________________________________________________
#Setting up display for the dice face
#_____________________________________________________________________________

win_heading = Label(root, text = 'Roll The Dice', font = 'Segoe=ui 20')
win_heading.pack(anchor = CENTER, side = TOP, pady = 20)

dice_frame = LabelFrame(root) #Container for the dice images
dice_frame.pack(anchor = CENTER, side = TOP, pady = 20)

dice_face = Label(dice_frame, image = one)
dice_face.pack(expand = 1, fill = BOTH)

dice_no = Label(root, text = "Press the button to roll")
dice_no.pack(anchor = CENTER, side = TOP, pady = 5)


#Binding Enter Key with roll_dice

root.bind("<Return>", roll_dice)

root.mainloop()


