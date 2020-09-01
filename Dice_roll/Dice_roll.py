
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
def roll_dice():
        
    choice = random.choice([1,2,3,4,5,6])
    
    print(choice)
    update_ui(choice)
    

def update_ui(choice):
    if choice == 1:
        dice_face["image"] = one
        dice_no["text"] = "It's a " + str(choice)
        root.update()

    elif choice == 2:
        dice_face["image"] = two
        dice_no["text"] = "It's a " + str(choice)
        root.update()
        
    elif choice == 3:
        dice_face["image"] = three
        dice_no["text"] = "It's a " + str(choice)
        root.update()
        
    elif choice == 4:
        dice_face["image"] = four
        dice_no["text"] = "It's a " + str(choice)
        root.update()
        
    elif choice == 5:
        dice_face["image"] = five
        dice_no["text"] = "It's a " + str(choice)
        root.update()
        
    else:
        dice_face["image"] = six
        dice_no["text"] = "It's a " + str(choice)
        root.update()
        

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



root.mainloop()
