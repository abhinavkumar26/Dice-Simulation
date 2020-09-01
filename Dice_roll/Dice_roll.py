
#-----------------------------------------------------------------------------------
''' A simple dice rolling simulater '''
#-----------------------------------------------------------------------------------

from tkinter import*
import random

root = Tk()

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

root.title("Youtube Downloader by Abhinav Kumar, github.com/abhinavkumar26")

root.config(bg= '#242424')
#_____________________________________________________________________________

dice_frame = LabelFrame(root) #Container for the dice images





root.mainloop()