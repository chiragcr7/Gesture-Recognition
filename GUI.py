from tkinter import *
import time
# from opencvCodes import  aircanva
from PIL import ImageTk, Image


app = Tk()
app.title("opencv project")
app.geometry('1550x800')



heading_text="DEVICE CONTROL USING GESTURE DETECTION"                     #add heading text over there

k='''Gesture recognition can be seen as a way for computers to begin to understand 
the human body.Compared to the primitive users interfaces, such as keyboard and
mouse which allows to build a richer bridge between the computers and humans.
It also allows the physically disabled users to smoothen the functionality of their
devices which also allows a philanthropist side to this project.
'''                            #add text there
def resizer_button(i,l,w):
    open_image=Image.open(i)
    resize_image=open_image.resize((l,w), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resize_image)

#define button image
def normal_image(x):
    return ImageTk.PhotoImage(file=x)

#define ur image for buttons
image_scroller=resizer_button("venv/images/Screenshot 2021-11-09 231551 (2).png",400,103)
image_virtualpen=resizer_button("venv/images/Screenshot 2021-11-09 230952 (3).png",400,103)

#create canvas
my_canvas= Canvas(app,width=1550,height=800)
my_canvas.pack(fill="both", expand=True)
def AircanvaButton():
    from opencvCodes.aircanva import paintcv
def BrowserButton():
    from  opencvCodes.browse_control import controller

#add buttons
def button1():
    return Button(app, image=image_scroller,font=("bold",45),borderwidth=10,command=BrowserButton)
def button2():
    return Button(app, image=image_virtualpen,font=("bold",45),borderwidth=10,command=AircanvaButton)

def button1_window():
    return my_canvas.create_window(160,450, anchor="nw",window=button1())
def button2_window():
    return my_canvas.create_window(850,450, anchor="nw",window=button2())



def resizer():
    global mg,resized_bg,new_bg
    #open our image
    mg= Image.open("istockphoto-895278132-170667a.jpg")

    #resize the image
    resized_bg=mg.resize((1550,800), Image.ANTIALIAS)

    #define ur image
    new_bg= ImageTk.PhotoImage(resized_bg)

    #add it to canvas
    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")

def add_text(n,x,y,z,w,v):
    #add text
    my_canvas.create_text(x, y, text=n, anchor= "nw", font=(v,z), fill= w)
a=resizer()
b=add_text(heading_text, 150,20,45,"white","algerian")
c=add_text(k,10,120,24,"#9f9fa0", "copperplate gothic bold")
button1_window()
button2_window()

app.mainloop()
