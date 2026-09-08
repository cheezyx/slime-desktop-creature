import random
import pyautogui as pag
import tkinter as tk

x = 1400
y = 700
vertical_speed = 0
cycle = 0
check = 4
revive_num = [0]
idle_num = [1, 2, 3, 4]
attack_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
bounce_up_num = [5]
bounce_down_num = [14]
death_num = [16]
event_num = random.randrange(1,3,1) # start stop step // why 3 ?
impath = '.\\assets\\slime'
blue_path = impath+'_blue\\'
purple_path = impath+'_purple\\'

def choose_slime_color():  # main.py material - menu items
    print("Choose slime color:")
    print("1. Blue")
    print("2. Purple")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        return blue_path
    elif choice == '2':
        return purple_path

path_color = choose_slime_color()

window = tk.Tk()


idle = [tk.PhotoImage(file=path_color+'idle_left.gif', format='gif -index %i' % (i)) for i in range(7)]
attack = [tk.PhotoImage(file=path_color+'attack_left.gif', format='gif -index %i' % (i)) for i in range(12)]
# slide_left = [tk.PhotoImage(file=path_color+'slide_left.gif', format='gif -index %i' % (i)) for i in range(6)]
# slide_right = [tk.PhotoImage(file=path_color+'slide_right.gif', format='gif -index %i' % (i)) for i in range(6)]
revive = [tk.PhotoImage(file=path_color+'revive_right.gif', format='gif -index %i' % (i)) for i in range(7)]
walk_left = [tk.PhotoImage(file=path_color+'walk_left.gif', format='gif -index %i' % (i)) for i in range(6)]
walk_right = [tk.PhotoImage(file=path_color+'walk_right.gif', format='gif -index %i' % (i)) for i in range(6)]
bounce_up =  [tk.PhotoImage(file=path_color+'bounce_displaced_left.gif', format='gif -index %i' % (i)) for i in range(8)]
bounce_down =  [tk.PhotoImage(file=path_color+'bounce_displaced_right.gif', format='gif -index %i' % (i)) for i in range(8)]
death = [tk.PhotoImage(file=path_color+'death.gif', format='gif -index %i' % (i)) for i in range(10)]

def event(cycle, check, event_num, x):
    # optimize. maybe switch case or dictionary mapping
    if check == 0: #this is not used right ? 
        frame = revive[cycle]
        cycle, event_num = gif_loop(cycle, revive, event_num, 0, 0)
    elif event_num in idle_num:
        check = 0
        window.after(400, update, cycle, event_num, check, x)
    elif event_num in attack_num:
        check = 1
        window.after(400, update, cycle, event_num, check, x)
    elif event_num in walk_left:
        check = 2
        window.after(400, update, cycle, event_num, check, x)
    elif event_num in walk_right:
        check = 3
        window.after(400, update, cycle, event_num, check, x)
    elif event_num in bounce_up_num:
        check = 4
        window.after(400, update, cycle, event_num, check, x)
    elif event_num in bounce_down_num:
        check = 5
        window.after(400, update, cycle, event_num, check, x)
    elif event_num in death_num:
        check = 6
        window.after(400, update, cycle, event_num, check, x)

def gif_loop(cycle, frames, event_num, first_num, last_num):
    if cycle < len(frames) - 1: # what does this do ?
        cycle += 1
    else:
        cycle = 0
        event_num = random.randrange(first_num, last_num+1, 1)
    return cycle, event_num

def choose_state():
    return random.choices([0, 1, 2, 3, 5, 6], weights=[70, 5, 12, 13, 4, 4])[0]

def update(cycle, check, event_num, x, y, vertical_speed):
    if getattr(window, 'closing', False) and check != 7:
        cycle = 0
        check = 7
        vertical_speed = 0
 # highkey hating this elif saga
    if check == 0: #idle
        frame = idle[cycle]
        cycle, event_num = gif_loop(cycle, idle, event_num, 1, 9)
    elif check == 1: #attack
        frame = attack[cycle]
        cycle, event_num = gif_loop(cycle, attack, event_num, 10, 10)
    elif check == 2: #walk left
        frame = walk_left[cycle]
        cycle, event_num = gif_loop(cycle, walk_left, event_num, 1, 9)
        x -= 3
    elif check == 3: #walk right
        frame = walk_right[cycle]
        cycle, event_num = gif_loop(cycle, walk_right, event_num, 1, 9)
        x += 3
    elif check == 4: #revive
        frame = revive[cycle]
        cycle, event_num = gif_loop(cycle, revive, event_num, 0, 0)
    elif check == 5: #bounce up
        frame = bounce_up[cycle]
        cycle, event_num = gif_loop(cycle, bounce_up, event_num, 0, 0)
        y -= 3
        x -= random.choice([0, 1, 2])
    elif check == 6: #bounce down
        frame = bounce_down[cycle]
        cycle, event_num = gif_loop(cycle, bounce_down, event_num, 0, 0)
        y += 3
        x += random.choice([0, 1, 2])
    elif check == 7: #death
        frame = death[cycle]
        cycle, event_num = gif_loop(cycle, death, event_num, 0, 0)

    if cycle == 0 and check == 7:
        window.after(100, window.destroy)
        return
    elif cycle == 0:
        check = choose_state()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = max(0, min(x, screen_width - 100))
    y += vertical_speed
    if y <= 0 or y >= screen_height - 100:
        vertical_speed *= -1
        y = max(0, min(y, screen_height - 100))

    window.geometry('100x100+' + str(x) + '+' + str(y))

    label.config(image=frame)
    window.after(100, update, cycle, check, event_num, x, y, vertical_speed)

def close_program():
    if not getattr(window, 'closing', False): # unnecessary if not - can do just straight to if window closing
        window.closing = True

def exit_on_escape(_mouse_event):
    close_program()

def start_drag(mouse_event):
    window.drag_start_x = mouse_event.x_root - window.winfo_x() # not working
    window.drag_start_y = mouse_event.y_root - window.winfo_y()

def drag_window(mouse_event):
    x = mouse_event.x_root - window.drag_start_x
    y = mouse_event.y_root - window.drag_start_y
    window.geometry('100x100+' + str(x) + '+' + str(y))


window.config(bg='black', highlightthickness=0)
label = tk.Label(window, bd=0, bg='black', highlightthickness=0)
window.overrideredirect(True)
#window.wm_attributes('-transparentcolor', 'black')
window.attributes('-topmost', True)

label.pack()
label.bind('<Button-1>', start_drag)
label.bind('<B1-Motion>', drag_window)
window.protocol('WM_DELETE_WINDOW', close_program)
window.bind_all('<Escape>', exit_on_escape)
window.after(1, update, cycle, check, event_num, x, y, vertical_speed)
window.mainloop()
