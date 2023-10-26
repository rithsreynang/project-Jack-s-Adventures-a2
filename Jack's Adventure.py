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
#  exit game___________
def exitfromgame(event):
    canvas.quit()
#  info___________
def info(event):
    canvas.create_image(0,0 , image=it, anchor='nw')
    canvas.create_text(600,500 , text='How to play', font=('Lucky Coin',30) ,fill='black', anchor='nw')
    canvas.create_text(600,560 , text='Key left = Go left', font=('Lucky Coin',20) ,fill='black', anchor='nw')
    canvas.create_text(600,610 , text='Key right = Go right', font=('Lucky Coin',20) ,fill='black', anchor='nw')
    canvas.create_text(600,650 , text='Space = Jump', font=('Lucky Coin',20) ,fill='black', anchor='nw')

    # go back
    canvas.create_image(20,20 , image=back, anchor='nw' , tags='back')
    canvas.create_text(65,45 , tags='back')

#  choose level___________
def chooslevel(event):
    global isreset
    canvas.delete('all')
    isreset=[False,False,False]
    # interface page level
    canvas.create_image(0,0 , image=page2 , anchor='nw')
    # go back
    canvas.create_image(20,20 , image= back, anchor='nw' , tags='back')
    canvas.create_text(65,45, tags='back')
    # level 1 
    canvas.create_text(365,280 , text='LOW', font = ('Lucky Coin', 40),fill='blue', anchor='nw' , tags='level1')
    # level 2
    canvas.create_text(632,280 , text='MEDIUM', font=('Lucky Coin', 40),fill='blue' , anchor='nw' , tags='level2')
    # level 3
    canvas.create_text(955,280, text='HARD', font=('Lucky Coin', 40),fill='blue' , anchor='nw' , tags='level3')

#  grid level low___________
def gridLevelLow(event):
    global isreset
    canvas.delete('all')
    isreset=[False,False,False]

    canvas.create_image(0,0,image=bg_game, anchor='nw',tags='levellow')
    canvas.create_image(-40,540,image=grash, anchor='nw',tags='levellow')
    canvas.create_image(260,540,image=grash, anchor='nw',tags='levellow')
    canvas.create_image(580,540,image=grash, anchor='nw',tags='levellow')
    canvas.create_image(890,540,image=grash, anchor='nw',tags='levellow')
    canvas.create_image(1100,540,image=grash, anchor='nw',tags='levellow')

    canvas.create_image(100,560,image=wall, anchor='nw',tags='levellow')
    canvas.create_image(320,480,image=wall, anchor='nw',tags='levellow')
    canvas.create_image(490,380,image=wall, anchor='nw',tags='levellow')
    canvas.create_image(740,290,image=wall, anchor='nw',tags='levellow')
    canvas.create_image(940,210,image=wall, anchor='nw',tags='levellow')
   

    canvas.create_image(1150,125,image=wall, anchor='nw',tags='levellow')
   

    canvas.create_image(100,450,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(160,450,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(220,450,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(330,350,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(380,350,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(480,250,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(540,250,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(600,250,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(760,160,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(830,160,image=coin, anchor='nw',tags='levellow')
    canvas.create_image(950,130,image=diamond, anchor='nw',tags='levellow')
    canvas.create_image(1050,130,image=diamond, anchor='nw',tags='levellow')
    canvas.create_image(1275,50,image=door, anchor='nw',tags='levellow')
    canvas.create_image(1275,50,image=door, anchor='nw',tags='levellow')
    canvas.create_image(150,-55,image=hart, anchor='nw',tags='levellow')

    canvas.create_text(500,20, text='Time: 20s', font=('Lucky Coin',20),fill='black' , anchor='nw',tags="levellow")
    canvas.create_text(350,20, text='Score : 00', font=('Lucky Coin',20),fill='black' , anchor='nw',tags="levellow")
# go back
    canvas.create_image(5,5 , image=back, anchor='nw' , tags='bak')
    canvas.tag_bind('bak', '<Button-1>',chooslevel)
    

# #  grid level medium___________
def gridLevelMedium(event):
    global isreset
    canvas.delete('all')
    isreset=[False,False,False]

    canvas.create_image(0,0,image=medium_bg, anchor='nw',tags='levelmedium')
    canvas.create_image(-40,540,image=grash, anchor='nw',tags='levelmedium')
    canvas.create_image(260,540,image=grash, anchor='nw',tags='levelmedium')
    canvas.create_image(580,540,image=grash, anchor='nw',tags='levelmedium')
    canvas.create_image(890,540,image=grash, anchor='nw',tags='levelmedium')
    canvas.create_image(1100,540,image=grash, anchor='nw',tags='levelmedium')

    canvas.create_image(120,560,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(250,440,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(120,320,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(0,200,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(500,200,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(750,440,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(650,320,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1100,500,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1200,380,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1265,260,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1000,180,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1180,80,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1250,80,image=wall, anchor='nw',tags='levelmedium')
    canvas.create_image(1270,7,image=door, anchor='nw',tags='levelmedium')
    canvas.create_image(150,-55,image=hart, anchor='nw',tags='levelmedium')
    canvas.create_text(500,20, text='Time: 20s', font=('Lucky Coin',20),fill='white' , anchor='nw',tags="levelmedium")
    canvas.create_text(350,20, text='Score : 00', font=('Lucky Coin',20),fill='white' , anchor='nw',tags="levelmedium")

    coin_positions = [
                    (120,560), 
                    (250,440), 
                    (100,440), 
                    (120,320), 
                    (420,320), 
                    (200,200), 
                    (150,80), 
                    (750,440),
                    (650,320),
                    (1100,500),
                    (1200,380),
                    (1265,260),
                    (1000,180),
                    (1180,80),
                    (1250,80)
                    ]

    canvas.create_image(500, 280, image=diamond, anchor='nw', tags='levelmedium')

    for position in coin_positions:
        canvas.create_image(position[0], position[1], image=coin, anchor='nw', tags='levelmedium')

    # go back
    canvas.create_image(5,5 , image=back, anchor='nw' , tags='back')

    canvas.create_image(5,5 , image=back, anchor='nw' , tags='bak')
    canvas.tag_bind('bak', '<Button-1>',chooslevel)

def gridLevelHard(event):
    global isreset
    canvas.delete('all')
    isreset=[False,False,False]

    canvas.create_image(0,0,image=hard_bg, anchor='nw',tags='levelhard')


    canvas.create_image(120,560,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(250,440,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(120,320,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(0,200,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(450,200,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(450,300,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(450,600,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(650,340,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(750,540,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(750,440,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(750,640,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1100,500,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1200,380,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1265,260,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1000,180,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1180,80,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1250,80,image=wall, anchor='nw',tags='levelhard')
    canvas.create_image(1270,7,image=door, anchor='nw',tags='levelmedium')


    coin_positions = [
                    (120,560), 
                    (250,440), 
                    (100,440), 
                    (120,320), 
                    (420,320), 
                    (200,200), 
                    (150,80), 
                    (750,440),
                    (650,320),
                    (1100,500),
                    (1200,380),
                    (1265,260),
                    (1000,180),
                    (1180,80),
                    (1250,80)
                    ]

    # canvas.create_image(500, 280, image=diamond, anchor='nw', tags='levelmedium')

    for position in coin_positions:
        canvas.create_image(position[0], position[1], image=coin, anchor='nw', tags='levelhard')


    canvas.create_image(150,-55,image=hart, anchor='nw',tags='levelmedium')
    canvas.create_text(500,20, text='Time: 20s', font=('Lucky Coin',20),fill='white' , anchor='nw',tags="levelmedium")
    canvas.create_text(350,20, text='Score : 00', font=('Lucky Coin',20),fill='white' , anchor='nw',tags="levelmedium")
    canvas.create_image(5,5 , image=back, anchor='nw' , tags='bak')
    canvas.tag_bind('bak', '<Button-1>',chooslevel)
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
wall=ImageTk.PhotoImage(file="images/wall.jpg")
bg_game=ImageTk.PhotoImage(file="images/bg.jpg")
medium_bg=ImageTk.PhotoImage(file="images/medium.jpg")
hard_bg=ImageTk.PhotoImage(file="images/hard.jpg")

back= ImageTk.PhotoImage(file="images/back.png")
enter= ImageTk.PhotoImage(file="images/enter.png")
infor= ImageTk.PhotoImage(file="images/info.png")
exit= ImageTk.PhotoImage(file="images/exit.png")
voo = ImageTk.PhotoImage(file="images/voo.png")

coin= ImageTk.PhotoImage(file="images/coin.png")
it= ImageTk.PhotoImage(file="images/about.png")
grash= ImageTk.PhotoImage(file="images/grash.png")
diamond= ImageTk.PhotoImage(file="images/diamond.png")
door= ImageTk.PhotoImage(file="images/home.png")
hart= ImageTk.PhotoImage(file="images/hart.png")
door2= ImageTk.PhotoImage(file="images/door2.png")


start(event=start) 

canvas.tag_bind('start', '<Button-1>',chooslevel)
canvas.tag_bind('back', '<Button-1>',start)
canvas.tag_bind('info', '<Button-1>',info)
canvas.tag_bind('exit', '<Button-1>',exitfromgame)
canvas.tag_bind('level1', '<Button-1>',gridLevelLow)
canvas.tag_bind('level2', '<Button-1>',gridLevelMedium)
canvas.tag_bind('level3', '<Button-1>',gridLevelHard)


frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()