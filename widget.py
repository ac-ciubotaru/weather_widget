import tkinter
from tkinter.font import Font
import time


def oraexacta():
    ctime = time.localtime(time.time())
    hours = ctime.tm_hour
    minutes = ctime.tm_min
    sec = ctime.tm_sec
    if minutes < 10:
        minutes = '0' + str(minutes)
    if sec < 10:
        sec = '0' + str(sec)

    return str(hours) + ':' + str(minutes) + ':' + str(sec)


root = tkinter.Tk()
root.wm_attributes('-transparentcolor', 'white')
root.config(bg='white')
root.overrideredirect(True)

r_width = 400
r_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - r_width / 2)
center_y = int(screen_height / 2 - r_height / 2)
root.geometry(f'400x300+{center_x}+{center_y}')

textfont = Font(size=60, family='Bahnschrift')
timeshow = tkinter.Label(root, font=textfont, text=oraexacta(), bg='white', fg='#FFFFFE')
timeshow.pack()

while True:
    timeshow.config(text=oraexacta())
    timeshow.update()

tkinter.root.mainloop()
