import pyautogui as pg
import tkinter as tk


class Setup:

    def __init__(self):
        self.impath = '.\\assets\\slime'
        self.blue_path = self.impath+'_blue\\'
        self.purple_path = self.impath+'_purple\\'

        self.path_color = self.choose_slime_path()

        self.window = tk.Tk()

        self.idle = [tk.PhotoImage(file=self.path_color+'idle_left.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(7)]
        self.revive = [tk.PhotoImage(file=self.path_color+'revive_right.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(7)]
        self.death = [tk.PhotoImage(file=self.path_color+'death.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(10)]
        self.hurt = [tk.PhotoImage(file=self.path_color+'hurt.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(4)]

        self.attack_right = [tk.PhotoImage(file=self.path_color+'attack_right.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(12)]
        self.attack_left = [tk.PhotoImage(file=self.path_color+'attack_left.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(12)]

        self.start_slide_left = [tk.PhotoImage(file=self.path_color+'start_slide_left.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(6)]
        self.start_slide_right = [tk.PhotoImage(file=self.path_color+'start_slide_right.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(6)]
        self.slide_left = [tk.PhotoImage(file=self.path_color+'slide_left.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(6)]
        self.slide_right = [tk.PhotoImage(file=self.path_color+'slide_right.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(6)]

        self.walk_left = [tk.PhotoImage(file=self.path_color+'walk_left.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(6)]
        self.walk_right = [tk.PhotoImage(file=self.path_color+'walk_right.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(6)]

        self.bounce_up =  [tk.PhotoImage(file=self.path_color+'bounce_displaced_left.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(8)]
        self.bounce_down =  [tk.PhotoImage(file=self.path_color+'bounce_displaced_right.gif', format='gif -index %i' % (i)).zoom(2,2) for i in range(8)]

        

    def choose_slime_path(self):
        choice = input("What color is your slime? ")
        if choice == '1':
            return self.blue_path
        elif choice == '2':
            return self.purple_path



