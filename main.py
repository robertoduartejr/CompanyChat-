from tkinter import *
from datetime import datetime
import socket
import threading

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#global variables
flag = x1 = y1 = 0
user_name = ""
user_id = ""

#function to receive. To use thread
def ReceiveMessage(s,T):
    while True:
        data = s.recv(1024)
        message = data.decode()
        T.insert(END, message)


#CHAT WINDOW
def send(user_name, user_id, user_text,T,T2,s):

    #First internal part
    #edited text to send:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    edited_text = f'\n{current_time} {user_name} {user_id} says: {user_text}'
    T.insert(END, edited_text)
    T2.delete("1.0","end")

    #online part
    s.sendall(str.encode(edited_text))

def chat(user_name, user_id):

    #chanigng the picutre.
    main_window.title("Company Chat")
    main_window.iconbitmap(default="chatimg.ico")
    main_window.geometry("816x597+214+23")
    main_window.resizable(width=False, height=False)

    #conversation box
    T = Text(main_window, height=5, width=52)
    T.place(width= 600, height = 389, x= 3 , y= 3)
    #T.config(state=DISABLED)

##################################################################
    # chat_window = Tk()
    # Initiating connection
    HOST = "127.0.0.1"
    PORT = 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    thread = threading.Thread(target=ReceiveMessage, args=[s, T])
    thread.start()
####################################################################


    # message box creating and position
    T2 = Text(main_window, height=5, width=52)
    T2.place(width = 600, height = 140, x = 3, y = 415)

    #send button creating and position
    send_button = Button(main_window, text="Send", command= lambda: send(user_name,user_id,T2.get("1.0",'end-1c'),T,T2,s))
    send_button.place(width= 143, height = 33, x= 459 , y= 560)

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

main_window.mainloop()