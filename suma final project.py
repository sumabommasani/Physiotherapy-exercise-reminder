from time import sleep
import time
from tkinter import *
from tkinter import ttk
import wave 
import pyaudio
import os

execution_count = 0

def action(win, more):
    global execution_count
    global root
    print('Answer', more)
    if more:
        win.destroy()
        sleep(snooze_time)
        execution_count = execution_count + 1
        ReminderWindow(title, message)
    else:
        win.destroy()
        root.destroy()


def play_bell():
    
    # set things up to play a file
    chunk = 1024        
    # so we can find bell filepath to this_directory 
    path_to_this_directory = os.path.dirname(os.path.realpath(__file__))
    alarm_filepath = path_to_this_directory + "/alarm_bell.wav"
    f = wave.open(alarm_filepath,"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()), channels = f.getnchannels(), rate = f.getframerate(), output = True)
    data = f.readframes(chunk)
    # go through the file and play the file
    while data:
        stream.write(data)
        data = f.readframes(chunk)
    # close things up
    stream.stop_stream()
    stream.close()
    p.terminate()
def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm ringing!")
            play_bell()
            break
        print("Current time: " + current_time)
        time.sleep(1)
        
def ReminderWindow(title, message):
    global root
    print('Execution', execution_count)
    win = Toplevel()
    win.withdraw()
    win.update_idletasks()
    x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
    y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
    win.geometry("+%d+%d" % (x, y))
    win.deiconify()
    win.title(title)
    message1=message
    message2='Current Snooze time={0} seconds'.format(snooze_time)
    message3 = 'Do you want more reminders?'
    ttk.Label(win, text=message1).grid(column=0, row=0)
    ttk.Label(win, text=message2).grid(column=0, row=1)
    ttk.Label(win, text=message3).grid(column=0, row=2)
    yes_btn = ttk.Button(win, text='Yes', command=lambda: action(win, True))
    yes_btn.grid(column=0,row=3)
    play_bell()
    ttk.Button(win, text='No', command=lambda: action(win, False)).grid(column=1, row=3)
    yes_btn.focus()
    win.lift()
    win.attributes('-topmost', True)

set_alarm("13:17:40")
snooze_time = int(input('Enter Snooze interval:'))
title = input('Enter title for reminder window: ')
message = input('Enter message for reminder window: ')
print('\n\nThanks! You will get your first reminder in {0} seconds'.format(snooze_time))
print('\n\n')
print('App started....')

root = Tk()
root.withdraw()
execution_count = 1
ReminderWindow(title, message)   # example title='Eye Exercise Reminder', message='Time for Eye Exercise!'
print('Exiting, bye')

