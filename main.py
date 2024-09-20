from customtkinter import*
from PIL import Image

root=CTk()
root.geometry("930x478")
root.resizable(0,0)
root.title('login page')
image= CTkImage(Image.open('cover.jpg'),size=(930,478))
imagelabel=CTkLabel(root,image=image,text='')
imagelabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text="EMPLOYEE MANAGEMENT SYSTEM")
headinglabel.place(x=20,y=100)