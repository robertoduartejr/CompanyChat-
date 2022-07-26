from tkinter import *


#global variables
flag = x1 = y1 = 0

#CHAT WINDOW
def chat():
    chat_window = Tk()
    chat_window.title("Company Chat")
    chat_window.iconbitmap(default="chatimg.ico")
    print(name.get())
    chat_window.mainloop()

#INITIAL WINDOW AND PARAMETERS
main_window = Tk()
main_window.title("Company Chat")
main_window.iconbitmap(default="chatimg.ico")
main_window.geometry("300x500+457+45")
main_window.resizable(width=False, height=False)


#Creating labels
employee_name = Label(main_window,text="Employee name: ")
employee_department = Label(main_window,text="Department: ")
employee_id = Label(main_window,text="ID: ")

#Positioning labels
employee_name.place(width=113,height=14,x=6,y=6, anchor=E)
employee_name.grid(sticky=W,pady=20)
employee_department.place(width=113,height=14,x=6,y=49)
employee_department.grid(sticky=W,pady=20)
employee_id.place(width=113,height=14,x=6,y=93)
employee_id.grid(sticky=W,pady=20)

#Creating and position button
main_button = Button(main_window, text = "Start Chat", command = chat)
main_button.place(width=93,height=30,x=106,y=439)

#Creating entry boxes
name = Entry(main_window,justify=LEFT)
department = Entry(main_window,justify=LEFT)
user_id = Entry(main_window,justify=LEFT)

#Positioning entry boxes
name.place(width= 171, height = 30, x= 96 , y= 15)
department.place(width= 171, height = 30, x= 96 , y= 79)
user_id.place(width= 171, height = 30, x= 96 , y= 141)



#Pegar posição do cursos
def clique_esquerdo_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:

        print(f'width= {arg.x-x1}, height = {arg.y-y1} x= {x1} , y= {y1}')

main_window.bind("<Button-1>",clique_esquerdo_mouse)

main_window.mainloop()