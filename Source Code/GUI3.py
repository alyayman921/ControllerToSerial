import time
import threading
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
from serial_communicator import Serial_Communications
from serial_sniffer import serial_ports
from controller_func import Controller

sp=serial_ports()
print(sp)
running=False
expanded=False
currentDIR=os.getcwd()

def start_clicked():
    global running,c,Serial
    refreshSerialPorts()
    if running==True:
        print('nope')
        canvas.itemconfig(toggle_text,text='Start')
        running=False
        Serial.close()

    elif SerialPorts.get()!="":
        running = True
        print('yare yare')
        canvas.itemconfig(toggle_text,text='Stop')
        try:
            COM=SerialPorts.get()
            Serial=Serial_Communications(COM,115200)
            c=Controller()
            controller_thread=threading.Thread(target=controller_start).start()
            pass
        except Exception as e:
            print('Error While Opening Serial Port')

def controller_start(event=None):
    global c,Serial,running
    while running:
        inputs=c.controller()
        active_inputs(inputs)
        serial_send_inputs(inputs)
        print(inputs)
        time.sleep(0.01)

def active_inputs(inp):
    axis_map=["LSH","LSV","RSH","RSV","LTT","RTT"]
    button_map=['x','circle','square','triangle','share','ps','options','L3','R3','LB','RB','dpad_up','dpad_down','dpad_left','dpad_right','touchpad']
    button_bool = [False] * 20
    default=button_bool
    for i in range(12):
        if i % 2 != 0:
            continue
        sticks(i/2, inp[i + 1])
    for i in range(len(inp) - 12):
        if i % 2 != 0:
            continue
        active_button = inp[i + 1 + 12]
        for index, button in enumerate(button_map):  
            if button == active_button:
                button_bool[index] = True
    pressed(button_bool)

    
def pressed(button_bool):
    button_map = ['x', 'circle', 'square', 'triangle', 'share', 'ps', 'options', 'L3', 'R3', 'LB', 'RB', 'dpad_up', 'dpad_down', 'dpad_left', 'dpad_right', 'touchpad']
    global x_positions,y_positions
    for index,value in enumerate(button_bool):
        if value:
            print(button_map[index])
            button_active[index].pack()
            button_active[index].place(x=x_positions[index], y=y_positions[index])
        else:
            button_active[index].place(x=1000, y=1000)
            pass

def serial_send_inputs(inputs):
    string_to_send=""
    for i in range(12):
        if i%2!=0:
            continue
        string_to_send+=inputs[i]
        string_to_send+=":"
        string_to_send+=str(inputs[i+1])
        string_to_send+="|"
    for i in range(len(inputs)-12):
        if i%2!=0:
            continue
        string_to_send+=inputs[i+1+12]
        string_to_send+="|"
    Send(string_to_send)
    #print(string_to_send)
    time.sleep(0.01)


def sticks(ax,val):
    posx=[157,336]  # button_image[19].width
    posy = 222
    v=float(val)
    if ax ==0:
        LS.place(x=posx[0]+v*button_image[19].width/6)
    if ax==1:
        LS.place(y=posy+v*button_image[19].height/6)
    if ax ==2:
        RS.place(x=posx[1]+v*button_image[19].width/6)
    if ax==3:
        RS.place(y=posy+v*button_image[19].height/6)
    if ax==4:
        if v>-0.5:
            button_active[17].pack()
            button_active[17].place(x=x_positions[17], y=y_positions[17])
        else:
            button_active[17].place(x=1000, y=1000)
    if ax==5:
        if v>-0.5:
            button_active[18].pack()
            button_active[18].place(x=x_positions[18], y=y_positions[18])
        else:
            button_active[18].place(x=1000, y=1000)

def on_mouse_down(event):
  global lastx, lasty
  lastx = event.widget.winfo_pointerx()
  lasty = event.widget.winfo_pointery()
def on_mouse_move(event):
  global lastx, lasty
  deltax = event.widget.winfo_pointerx() - lastx
  deltay = event.widget.winfo_pointery() - lasty
  root.geometry("+%d+%d" % (root.winfo_x() + deltax, root.winfo_y() + deltay))
  lastx = event.widget.winfo_pointerx()
  lasty = event.widget.winfo_pointery()
def change_color(feature,new_color):
    feature.itemconfig(Start, outline=new_color)
def SerialMonitor():
    global expanded
    if expanded:
        expanded=False
        root.geometry("1280x720")
        root.after(0, root.update)
    else:
        expanded=True
        root.geometry("1280x905")
        root.after(0, root.update)
        serialThread=threading.Thread(target=SerialMonitorRefresh).start()

def SerialMonitorRefresh():
    global Serial
    while expanded:
        readings=Serial.read()
        if readings!="":
            serial_monitor.insert(tk.END, readings+'\n')
            serial_monitor.see(tk.END)
            #print(readings)
        pass
def Send(a): # Send to Serial Port func
    global Serial
    Serial.send(a)

def Send_text(event=None): # Send to Serial Port from user input
    global b,Serial
    Serial.send(serial_sender.get()) #
    serial_sender.delete(0, tk.END)
def refreshSerialPorts(event=None): # checks if a serial port is connected or disconnected while running
    global sp
    sp=serial_ports()
    SerialPorts['values'] = (sp) 




# WINDOW
normal_color = "#5b3065" #border
hover_color = "#ba5da3"
press_color = "#fffaaa"
fill_color="#001122"
root=tk.Tk()
root.title("Controller")
root.geometry('1280x720+200+10')
root.resizable(False, False)
root.config(bg='#dddddd')

root.iconbitmap(f"{currentDIR}/controller_assets/icon.ico")

#Start button
canvas = Canvas(root,width=320*0.75,height=75*0.75, bg="#dddddd",borderwidth=0,highlightthickness=0)
p1 = (10*0.75, 10*0.75)
p2=(10*0.75,35*0.75)
p3=(15*0.75,45*0.75)
p4=(15*0.75,70*0.75)
p5=(310*0.75,70*0.75)
p6=(310*0.75,25*0.75)
p7=(295*0.75,10*0.75)
Start = canvas.create_polygon(
p1,p2,p3,p4,p5,p6,p7,
outline=normal_color, width=3,
fill=fill_color
)
toggle_text=canvas.create_text((160*0.75,40*0.75), text="Start", font="Play 12 bold",fill="white")
canvas.place(x=1025,y=620)
canvas.bind("<Enter>", lambda event: change_color(canvas,hover_color))
canvas.bind("<Leave>", lambda event: change_color(canvas,normal_color))
canvas.bind("<Button-1>", lambda event: change_color(canvas,press_color))
canvas.bind("<ButtonRelease-1>", lambda event: start_clicked())


# Serial port picker
port_frame=tk.Frame(root,bg='#dddddd')
port_frame.pack()
port_frame.place(y=575,x=1045)
port_frame.bind("<Enter>",refreshSerialPorts)
serial_title=tk.Label(port_frame,font=('Play',14),fg='#001122',bg="#dddddd",text="Serial Port :")
serial_title.pack(side="left")
n = tk.StringVar() 
SerialPorts = ttk.Combobox(port_frame, width = 7, textvariable = n) 
SerialPorts['values'] = (sp) 
SerialPorts.pack(pady=15,padx=20,side=("right"))
SerialPorts.current() 

#Title
Label1=tk.Label(root,text='SSTL Rover Project',font="play 18 bold",fg="#001122", bg="#dddddd",highlightthickness=0)
Label1.pack()
Label1.place(x=40,y=40)



# Serial monitor
sm_button = Canvas(root,width=320*0.75,height=75*0.75, bg="#dddddd",borderwidth=0,highlightthickness=0) #button
Start = sm_button.create_polygon(
p1,p2,p3,p4,p5,p6,p7,
outline=normal_color, width=2,
fill=fill_color
)
sm_button.create_text((160*0.75,40*0.75), text="Serial Monitor", font="Play 12 bold",fill="white")
sm_button.place(x=30,y=620)
sm_button.bind("<Enter>", lambda event: change_color(sm_button,hover_color))
sm_button.bind("<Leave>", lambda event: change_color(sm_button,normal_color))
sm_button.bind("<Button-1>", lambda event: change_color(sm_button,press_color))
sm_button.bind("<ButtonRelease-1>", lambda event: SerialMonitor())

serial_frame=Frame(width=1280,height=180)
serial_frame.place(y=720)

serial_monitor = scrolledtext.ScrolledText(serial_frame, 
                            width = 114,  
                            height = 7,  
                            font = ("Arial", 
                                    15)) 
serial_monitor.pack(padx=4)
serial_sender=tk.Entry(root,width=1280)
serial_sender.pack(side='bottom')
serial_sender.bind('<Return>',Send_text)


#Controller Overlay

x_positions = [437 , 478 , 396 , 437 , 157 , 267 , 385 , # X positions of each button
               157 , 336 , 74 , 418 , 93 , 93 , 64 , 
               115 , 192,16,76,419,157,336]

y_positions = [193 , 152 , 152 , 112 , 99 , 238 , 99 ,  # Y positions of each button
               222 , 222 , 64 , 64 , 126 , 177 , 158 , 
               158, 86 ,16,4,4,222,222]

controller_frame=tk.Frame(width=806*.7,height=598*.7,bg="#dddddd")
button_path=[]
button_image=[]
resized=[]
button=[]
button_active=[]
for i in range(20):
    button_path.append(f"{currentDIR}/controller_assets/{i}.png")
    button_image.append(Image.open(button_path[i]))
    width = int(button_image[i].width * (70 / 100))
    height = int(button_image[i].height * (70 / 100))
    resized.append(button_image[i].resize((width, height)))
    button.append(ImageTk.PhotoImage(resized[i]))
    button_active.append(Canvas(controller_frame, bg="#dddddd", width=button_image[i].width*.7, height=button_image[i].height*.7,borderwidth=0,highlightthickness=0))
    button_active[i].create_image(button_image[i].width*.7/2,button_image[i].height*.7/2,image=button[i])

LS=Canvas(controller_frame, bg="#0f1015", width=button_image[19].width*.7, height=button_image[19].height*.7,borderwidth=0,highlightthickness=0)
LS.create_image(button_image[19].width*.7/2,button_image[19].height*.7/2,image=button[19])
LS.pack()
LS.place(x=x_positions[19], y=y_positions[19])
RS=Canvas(controller_frame, bg="#0f1015", width=button_image[19].width*.7, height=button_image[19].height*.7,borderwidth=0,highlightthickness=0)
RS.create_image(button_image[19].width*.7/2,button_image[19].height*.7/2,image=button[19])
RS.pack()
RS.place(x=x_positions[20], y=y_positions[20])

controller_image=Label(controller_frame,image=button[16],bg='#dddddd')
controller_image.pack()
controller_image.lower()

controller_frame.pack()
controller_frame.place(y=100,x=350)

root.mainloop()