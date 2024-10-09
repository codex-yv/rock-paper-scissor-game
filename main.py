from tkinter import*
from PIL import Image, ImageTk
import random
from tkinter import messagebox
up=0
rp=0
c=0


def count():
    global c, rp, up
    c=c+1
    if c==int(bstval.get()):
        rockbtn.config(state=DISABLED)
        paperbtn.config(state=DISABLED)
        scibtn.config(state=DISABLED)
        if int(rp)==int(up):
            statuslbl1.config(text="MATCH DRAW",fg="white",bg="blue")
            statuslbl2.config(text="MATCH DRAW",fg="white",bg="blue")
        elif int(rp)>int(up):
            statuslbl1.config(text="WON",fg="white",bg="Green")
            statuslbl2.config(text="LOST",fg="white",bg="red")
        elif int(rp)<int(up):
            statuslbl1.config(text="LOST",fg="white",bg="red")
            statuslbl2.config(text="WON",fg="white",bg="green")

            




def resize_image(image_path, new_width, new_height=None):
    """
    Resize an image to the specified width and height.
    If only width is provided, it will maintain the aspect ratio.
    
    :param image_path: Path to the image file
    :param new_width: Desired width of the resized image
    :param new_height: (Optional) Desired height of the resized image
    :return: Resized ImageTk.PhotoImage object
    """

    image = Image.open(image_path)

    if new_height is None:
        width, height = image.size
        new_height = int((new_width / width) * height)

    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)
    return photo
def compare(rp,up):
    if int(rp)==int(up):
        statuslbl1.place(x=150,y=400)
        statuslbl1.config(text="Tie",bg="blue",fg="white")

        statuslbl2.place(x=550,y=400)
        statuslbl2.config(text="Tie",bg="blue",fg="white")
    elif int(rp)>int(up):
        statuslbl1.place(x=150,y=400)
        statuslbl1.config(text="Wining",bg="Green",fg="white")

        statuslbl2.place(x=550,y=400)
        statuslbl2.config(text="Losing",bg="red",fg="white")
    elif int(rp)<int(up):
        statuslbl1.place(x=150,y=400)
        statuslbl1.config(text="Losing",bg="red",fg="white")

        statuslbl2.place(x=550,y=400)
        statuslbl2.config(text="Wining",bg="green",fg="white")
    
def change_button_color():

    colors = [ "green", "blue", "purple", "pink", "brown"]

    new_color = random.choice(colors)

    playbtn.config(bg=new_color)

    playbtn.after(500, change_button_color)


def play():
    try:
        int(bstval.get())
        gname.pack_forget()
        label.pack_forget()
        playbtn.pack_forget()
        bsten.place_forget()
        bstlbl.place_forget()

        win.config(bg="#ebdef0")

        seperator=Canvas(win,bg="grey",height=450,width=5)
        seperator.pack()

        robolbl.place(x=150,y=30)
        userlbl.place(x=550,y=30)

        rockbtn.place(x=300,y=455)
        paperbtn.place(x=380,y=455)
        scibtn.place(x=460,y=455)

        rplbl.place(y=130,x=120)

        uplbl.place(y=130,x=520)
    except ValueError:
        messagebox.showerror("Error", "Best of only accepts INTEGER value!")

def r():
    global rp, up
    robopt=['rocks.png','paper.png','scissors.png']
    roboimage=random.choice(robopt)
    image_path = roboimage
    new_width = 100
    new_height = 100

    roboimagech=resize_image(image_path,new_width,new_height)
    
    robochlbl.config(image=roboimagech)
    robochlbl.image=roboimagech
    robochlbl.place(x=120,y=170)
    user=rockval.get()
    
    if user==roboimage:
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        statuslbl1.config(text="Choosen the same thought!!",fg="white",bg="blue")
        statuslbl2.config(text="Choosen the same thought!!",fg="white",bg="blue")
    
    elif user=='rocks.png' and roboimage=='paper.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        rp=rp+1
        rp=str(rp)
        rplbl.config(text=f"Robot Point:{rp}")
        rp=int(rp)

        compare(rp,up)            

    elif user=='rocks.png' and roboimage=='scissors.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        up=up+1
        up=str(up)
        uplbl.config(text=f"User Point:{up}")
        up=int(up)
        compare(rp,up) 

def p():
    global rp, up

    robopt=['rocks.png','paper.png','scissors.png']
    roboimage=random.choice(robopt)
    image_path = roboimage
    new_width = 100
    new_height = 100

    roboimagech=resize_image(image_path,new_width,new_height)
    robochlbl.config(image=roboimagech)
    robochlbl.image=roboimagech
    robochlbl.place(x=120,y=170)
    user=paperval.get()

    if user==roboimage:
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        statuslbl1.config(text="Choosen the same thought!!",fg="white",bg="blue")
        statuslbl2.config(text="Choosen the same thought!!",fg="white",bg="blue")
    
    elif user=='paper.png' and roboimage=='rocks.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        up=up+1
        up=str(up)
        uplbl.config(text=f"User Point:{up}")
        up=int(up)
        compare(rp,up) 

    elif user=='paper.png' and roboimage=='scissors.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        rp=rp+1
        rp=str(rp)
        rplbl.config(text=f"Robot Point:{rp}")
        rp=int(rp)
        compare(rp,up) 

def s():
    global rp, up

    robopt=['rocks.png','paper.png','scissors.png']
    roboimage=random.choice(robopt)
    image_path = roboimage
    new_width = 100
    new_height = 100

    roboimagech=resize_image(image_path,new_width,new_height)
    
    robochlbl.config(image=roboimagech)
    robochlbl.image=roboimagech
    robochlbl.place(x=120,y=170)
    user=scival.get()

    if user==roboimage:
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        statuslbl1.config(text="Choosen the same thought!!",fg="white",bg="blue")
        statuslbl2.config(text="Choosen the same thought!!",fg="white",bg="blue")

    elif user=='scissors.png' and roboimage=='rocks.png':
 
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        rp=rp+1
        rp=str(rp)
        rplbl.config(text=f"Robot Point:{rp}")
        rp=int(rp)
        compare(rp,up) 

    elif user=='scissors.png' and roboimage=='paper.png':
 
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        up=up+1
        up=str(up)
        uplbl.config(text=f"User Point:{up}")
        up=int(up)
        compare(rp,up) 


win =Tk()
win.title("Rock,Paper,Scissor")
win.geometry("800x500")
win.config(bg="white")
win.iconbitmap("title.ico")

image_path = "robot.png"
new_width = 100
new_height = 100  


resized_image = resize_image(image_path, new_width, new_height)

gname=Label(win,text="Rock,Paper,Scissor!",font=("Jokerman",20),fg="red",bg="white")
gname.pack(side=TOP,pady=70)

bstlbl=Label(win,text="Best of:",font=("Bahnschrift",12),bg="white")
bstlbl.place(x=300,y=130)

bstval=StringVar()
bsten=Entry(win,textvariable=bstval,relief='sunken',bd=3)
bsten.place(x=380,y=130)

label = Label(win, image=resized_image)
label.pack()
label.image = resized_image

playbtn=Button(win,text="PLAY",font=("ROG Fonts",12),bg="green",fg="white",cursor="hand2",command=play)
playbtn.pack(pady=30)
change_button_color()

image_path1 = "robot.png"
new_width1 = 70
new_height1 = 70
roboimg=resize_image(image_path1,new_width1,new_height1)

robolbl=Label(win,image=roboimg,bg="#ebdef0")

image_path11 = "man.png"
new_width11 = 70
new_height11 = 70
userimg=resize_image(image_path11,new_width11,new_height11)

userlbl=Label(win,image=userimg,bg="#ebdef0")

image_path2 = "rocks.png"
new_width2 = 40
new_height2 = 40
rockimg=resize_image(image_path2,new_width2,new_height2)

rockval=StringVar()
rockbtn=Button(win,image=rockimg,relief="raised",textvariable=rockval,command=lambda:(r(),count()))
rockval.set(value="rocks.png")

image_path3 = "paper.png"
new_width3 = 40
new_height3 = 40
paperimg=resize_image(image_path3,new_width3,new_height3)

paperval=StringVar()
paperbtn=Button(win,image=paperimg,relief="raised",textvariable=paperval,command=lambda:(p(),count()))
paperval.set(value="paper.png")

image_path4 = "scissors.png"
new_width4 = 40
new_height4 = 40
sciimg=resize_image(image_path4,new_width4,new_height4)

scival=StringVar()
scibtn=Button(win,image=sciimg,relief="raised",textvariable=scival,command=lambda:(s(),count()))
scival.set(value="scissors.png")

robochlbl=Label(win,bg="#ebdef0")

userchlbl=Label(win,bg="#ebdef0")


rplbl=Label(win,text="Robot Point:0",font=("ROG Fonts",12),bg="#ebdef0")

uplbl=Label(win,text="User Point:0",font=("ROG Fonts",12),bg="#ebdef0")



statuslbl1=Label(win,text="Bahnschrift",font=("Bahnschrift",12),bg="#ebdef0")
statuslbl2=Label(win,text="Bahnschrift",font=("Bahnschrift",12),bg="#ebdef0")


win.mainloop()
