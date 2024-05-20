import customtkinter as ctk
import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

ctk.set_appearance_mode("Dark")

def in_task(task):
    f = ctk.CTkFrame(frame, fg_color='#02031F')
    ctk.CTkCheckBox(f, text=task, font=('Graduate', 20), width=40, height=40, corner_radius=0, border_color='#D4DDE4', fg_color='#02031F').pack(side=LEFT, padx=10)
    ctk.CTkButton(f, image=img_del, text='', width=40, corner_radius=0,
                  fg_color='#02031F',command=lambda:f.pack_forget()).pack(anchor=NW, side=LEFT, padx=10)
    f.pack(anchor=NW, padx=5, pady=5)

def add_task_btn():
     window = ctk.CTkToplevel(root)
     window.title("Add task")
     window.geometry('480x294')
     window.resizable(0, 0)

     image1 = PIL.Image.open('window.jpg')
     bg_img1 = ctk.CTkImage(image, size=(7480, 294))
     bg_lbl1 = ctk.CTkLabel(window, text="", image=bg_img1)
     bg_lbl1.place(x=0, y=0)

     task_entry = ctk.CTkEntry(window, placeholder_text="enter the note...", font=('Graduate', 20), width=400,
                               height=50, fg_color='#02031F', border_color='#D4DDE4', bg_color='#D4DDE4', text_color='#D4DDE4', placeholder_text_color='#D4DDE4')
     task_entry.pack(pady=105, padx=0)

     add_btn = ctk.CTkButton(window, font=ctk.CTkFont(family='Copse', size=16, weight='bold'), text="Ok", width=120,
                             height=40, text_color='#02031F', fg_color='#47E3F9', bg_color='#47E3F9', hover_color='#96F2FF', command=lambda:in_task(task_entry.get()))
     add_btn.place(x=171.5, y=180)
     window.mainloop()


root = ctk.CTk()
root.iconbitmap('main_icon.ico')
root.title("To Do Day")
root.geometry('720x440')
root.resizable(0, 0)


image = PIL.Image.open('main_frame.jpg')
bg_img = ctk.CTkImage(image, size=(720, 440))
bg_lbl = ctk.CTkLabel(root, text="", image=bg_img)
bg_lbl.place(x=0, y=0)

ctk.FontManager.load_font('Copse-Regular.ttf')
ctk.FontManager.load_font('Graduate-Regular.ttf')

img_del = ImageTk.PhotoImage(file='x.png')

frame = ctk.CTkScrollableFrame(root, width=600, height=280, fg_color='#02031F', border_width=2, border_color='#D4DDE4', bg_color='#D4DDE4')
frame.place(x=60, y=80)


task_btn = ctk.CTkButton(root, font=('Copse', 20), text="To Do Day", width=120, height=40, text_color='#02031F',
                         fg_color='#47E3F9', hover_color='#96F2FF',bg_color='#47E3F9', command=add_task_btn)
task_btn.pack(pady=42, padx=0)


root.mainloop()
