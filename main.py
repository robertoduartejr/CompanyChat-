from tkinter import *
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#global variables
flag = x1 = y1 = 0
user_name = ""
user_id = ""


#CHAT WINDOW
def send(user_name, user_id, user_text,T,T2):

    #First internal part
    #edited text to send:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    edited_text = f'\n{current_time} {user_name} {user_id} says: {user_text}'
    T.insert(END, edited_text)
    print(user_text)
    T2.delete("1.0","end")

    #Now online part


def chat(user_name, user_id):
    #chat_window = Tk()
    main_window.title("Company Chat")
    main_window.iconbitmap(default="chatimg.ico")
    main_window.geometry("816x597+214+23")
    main_window.resizable(width=False, height=False)
    print(user_id,user_name,"ok")

    #conversation box
    T = Text(main_window, height=5, width=52)
    T.place(width= 600, height = 389, x= 3 , y= 3)
    #T.config(state=DISABLED)
    print(T.get("1.0",'end-1c')) # a way to get information from a text box

    # message box
    T2 = Text(main_window, height=5, width=52)
    T2.place(width = 600, height = 140, x = 3, y = 415)

    #send button
    send_button = Button(main_window, text="Send", command= lambda: send(user_name,user_id,T2.get("1.0",'end-1c'),T,T2))
    send_button.place(width= 143, height = 33, x= 459 , y= 560)

    main_window.bind("<Button-1>", clique_esquerdo_mouse)
    main_window.mainloop()

#INITIAL WINDOW AND PARAMETERS
main_window = Tk()
main_window.title("Company Chat")
main_window.iconbitmap(default="chatimg.ico")
main_window.geometry("300x500+457+45")
#main_window.resizable(width=False, height=False)


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
#lambda used so we can send args within the function
main_button = Button(main_window, text = "Start Chat", command = lambda: chat(name.get(),user_id.get()))
main_button.place(width=93,height=30,x=106,y=439)

#Creating entry boxes
name = Entry(main_window,justify=LEFT)
department = Entry(main_window,justify=LEFT)
user_id = Entry(main_window,justify=LEFT)

#Positioning entry boxes
name.place(width= 171, height = 30, x= 96 , y= 15)
department.place(width= 171, height = 30, x= 96 , y= 79)
user_id.place(width= 171, height = 30, x= 96 , y= 141)



#get mouse position
def clique_esquerdo_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:

        print(f'width= {arg.x-x1}, height = {arg.y-y1}, x= {x1} , y= {y1}, GEO: {main_window.geometry()}')

main_window.bind("<Button-1>",clique_esquerdo_mouse)

main_window.mainloop()