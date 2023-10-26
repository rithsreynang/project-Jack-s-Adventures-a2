import tkinter as tk
import winsound 
from PIL import Image, ImageTk

# _____________________________Constant___________________________________
WIN_WIDTH = 1370
WIN_HEIGHT = 780
coin= 5
diamond=20

# _____________________________Variables__________________________________
levelGrid = []
isreset=[False,False,False]
iswin=[True,False,False]
swtict = True
isAllowtomove = True
countwin = 0
numcoin = 0
numdiamond=0
colorTime = 'black'

# _____________________________Function____________________________________
#  start game___________
def start(event):

    canvas.delete('all')
    canvas.create_image(0,0 , image=page1 , anchor='nw')
    canvas.create_text(500,40 , text="Jack's", font=("Lucky Coin", 100, "bold") ,fill='#223BC9', anchor='nw' )
    canvas.create_text(455,155 , text="Adventure", font=('Lucky Coin', 75) ,fill='#067FD0', anchor='nw' )


    canvas.create_text(635,365 , text='START', font=('Lucky Coin', 40) ,fill='#067FD0', anchor='nw' , tags='start')
    canvas.create_text(635,465 , text='About', font=('Lucky Coin', 40) ,fill='#067FD0', anchor='nw' , tags='info')
    canvas.create_text(645,565 , text='EXIT', font=('Lucky Coin', 40) ,fill='#067FD0', anchor='nw' , tags='exit')

def info(event):
    canvas.create_image(0,0 , image=it, anchor='nw')
    canvas.create_text(600,500 , text='How to play', font=('Lucky Coin',30) ,fill='black', anchor='nw')
    canvas.create_text(600,560 , text='Key left = Go left', font=('Lucky Coin',20) ,fill='black', anchor='nw')
    canvas.create_text(600,610 , text='Key right = Go right', font=('Lucky Coin',20) ,fill='black', anchor='nw')
    canvas.create_text(600,650 , text='Space = Jump', font=('Lucky Coin',20) ,fill='black', anchor='nw')

    # go back
    canvas.create_image(20,20 , image=back, anchor='nw' , tags='back')
    canvas.create_text(65,45 , tags='back')

# ______________________________sound__________________________________
def songGame():
    winsound.PlaySound("sounds/game-procces.wav", winsound.SND_ASYNC | winsound.SND_LOOP )
songGame()

# ____________________Main_________________________
root = tk.Tk()
root.geometry(str(WIN_WIDTH)+ 'x' + str(WIN_HEIGHT))
frame = tk.Frame(root)
canvas = tk.Canvas(frame)
root.title("Jack's Adventure")

icon = tk.PhotoImage(file='images/icon.png')
root.iconphoto(True,icon)
root.resizable(0,0)



# _____________________________Image_________________________________________

page1= ImageTk.PhotoImage(file="images/page1.jpg")
page2= ImageTk.PhotoImage(file="images/page2.jpg")
wall=ImageTk.PhotoImage(file="images/wall.png")
bg_game=ImageTk.PhotoImage(file="images/bg.jpg")

back= ImageTk.PhotoImage(file="images/back.png")
enter= ImageTk.PhotoImage(file="images/enter.png")
infor= ImageTk.PhotoImage(file="images/info.png")
exit= ImageTk.PhotoImage(file="images/exit.png")
voo = ImageTk.PhotoImage(file="images/voo.png")

coin= ImageTk.PhotoImage(file="images/coin.png")
it= ImageTk.PhotoImage(file="images/about.png")
grash= ImageTk.PhotoImage(file="images/grash.png")
diamond= ImageTk.PhotoImage(file="images/diamond.png")


start(event=start) 


canvas.tag_bind('back', '<Button-1>',start)

frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()