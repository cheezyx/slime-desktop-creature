import random
import pyautogui as pag
import tkinter as tk
from setup import Setup

class Assignment:

    def __init__(self, setup):
        self.window = setup.window

        self.idle_fr = setup.idle
        self.attack_right_fr = setup.attack_right
        self.attack_left_fr = setup.attack_left
        self.revive_fr = setup.revive
        self.walk_left_fr = setup.walk_left
        self.walk_right_fr = setup.walk_right
        self.bounce_up_fr = setup.bounce_up
        self.bounce_down_fr = setup.bounce_down
        self.death_fr = setup.death
        self.slide_left_fr = setup.slide_left
        self.slide_right_fr = setup.slide_right
        self.start_slide_left_fr = setup.start_slide_left
        self.start_slide_right_fr = setup.start_slide_right
        self.hurt_fr = setup.hurt

        self.dragging = False
        self.drag_frame = 0

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.slime_width = 150
        self.slime_height = 150
        self.x = self.window.winfo_screenwidth() // 2
        self.y = self.window.winfo_screenheight() // 2

        
        self.animations = {
            self.idle_slime: self.idle_fr,
            self.walk_left_slime: self.walk_left_fr,
            self.walk_right_slime: self.walk_right_fr,
            self.bounce_up_slime: self.bounce_up_fr,
            self.bounce_down_slime: self.bounce_down_fr,
            self.attack_right_slime: self.attack_right_fr,
            self.attack_left_slime: self.attack_left_fr,
            self.slide_left_slime: self.slide_left_fr,
            self.slide_right_slime: self.slide_right_fr,
            self.start_slide_left_slime: self.start_slide_left_fr,
            self.start_slide_right_slime: self.start_slide_right_fr,            
            self.hurt_slime: self.hurt_fr
        }

        self.deathandrevive = {
            self.revive_slime: self.revive_fr,
            self.death_slime: self.death_fr
        }

        self.slide_transition = {
            self.start_slide_left_slime: self.slide_left_slime,
            self.start_slide_right_slime: self.slide_right_slime
        }

    def revive_slime(self):
        return 0

    def idle_slime(self):
        pass

    def walk_left_slime(self):
        self.x -= 3
        self.window.geometry(f"+{self.x}+{self.y}")

    def walk_right_slime(self):
        self.x += 3
        self.window.geometry(f"+{self.x}+{self.y}")

    def bounce_up_slime(self):
        self.y -= 3
        self.x -= random.choice([0, 1, 2])
        self.window.geometry(f"+{self.x}+{self.y}")

    def bounce_down_slime(self):
        self.y += 3
        self.x += random.choice([0, 1, 2])
        self.window.geometry(f"+{self.x}+{self.y}")

    def attack_right_slime(self):
        return

    def attack_left_slime(self):
        return

    def hurt_slime(self):
        return

    def slide_left_slime(self):
        self.x -= 20
        self.window.geometry(f"+{self.x}+{self.y}")

    def slide_right_slime(self):
        self.x += 20
        self.window.geometry(f"+{self.x}+{self.y}")

    def start_slide_left_slime(self):
        pass

    def start_slide_right_slime(self):
        pass

    def death_slime(self):
        return 0

    def check_borders(self):
        if self.x <= 0:
            self.x = 0
            return self.attack_left_slime
        
        elif self.x >= self.screen_width - self.slime_width:
            self.x = self.screen_width - self.slime_width
            return self.attack_right_slime

        elif self.y <= 0:
            self.y = 0
            return self.hurt_slime

        elif self.y >= self.screen_height - self.slime_height:
            self.y = self.screen_height - self.slime_height
            return self.hurt_slime

        return None


    def choose_animation(self):
        #this is fucked
        choices = [
            self.idle_slime,
            self.walk_left_slime,
            self.walk_right_slime,
            self.bounce_up_slime,
            self.bounce_down_slime,
            self.idle_slime,
            self.idle_slime,
            self.idle_slime,
            self.start_slide_right_slime,
            self.start_slide_left_slime,
        ]
        return random.choice(choices)

    def play_animation(self, cycle, behavior):
        if self.dragging:
            self.window.after(100, self.play_animation, cycle, behavior)
            return

        if behavior in self.deathandrevive:
            frames = self.deathandrevive[behavior]
        else:
            frames = self.animations[behavior]

        frame = frames[cycle]
        self.label.configure(image=frame)

        behavior()

        new_behavior = self.check_borders()
        if new_behavior is not None and new_behavior != behavior:
            behavior = new_behavior
            frames = self.animations[behavior]
            cycle = 0
            frame = frames[cycle]
            self.label.configure(image=frame)

        cycle += 1
        if cycle >= len(frames):
            cycle = 0

            if behavior == self.revive_slime:
                behavior = self.choose_animation()
            elif behavior == self.death_slime:
                self.window.destroy()
                return
            elif behavior in self.slide_transition:
                behavior = self.slide_transition[behavior]
            else:
                behavior = self.choose_animation()

        self.window.after(100, self.play_animation, cycle, behavior)

    def on_close(self):
        self.play_animation(0, self.death_slime)

    def exit_on_escape(self, _mouse_event):  
        self.play_animation(0, self.death_slime)
        self.close_program()

    def close_program(self):
        if not getattr(self.window, 'closing', False):
            self.window.closing = True

    def drag_slime_animation(self, frame=0):
        if not self.dragging:
            return

        self.label.configure(image=self.hurt_fr[frame])

        frame = (frame + 1) % len(self.hurt_fr)
        self.window.after(100, self.drag_slime_animation, frame)

    def start_drag(self, event):
        self.dragging = True
        self.drag_offset_x = event.x_root - self.x
        self.drag_offset_y = event.y_root - self.y
        self.drag_slime_animation()

    def drag_slime(self, event):
        if self.dragging:
            self.x = event.x_root - self.drag_offset_x
            self.y = event.y_root - self.drag_offset_y
            self.window.geometry(f"+{self.x}+{self.y}")
    
    def stop_drag(self, event):
        self.dragging = False


    def start_program(self):
        self.window.config(bg='black', highlightthickness=0)
        self.label = tk.Label(self.window, bd=0, bg='black', highlightthickness=0)
        self.window.attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)

        self.label.place(x=0, y=0)
        self.label.bind('<Button-1>', self.start_drag)
        self.label.bind('<B1-Motion>', self.drag_slime)
        self.label.bind('<ButtonRelease-1>', self.stop_drag)
        self.window.geometry(f"150x150+{self.x}+{self.y}")        
        self.window.after(1, self.play_animation, 0, self.revive_slime)
        self.window.protocol('WM_DELETE_WINDOW', self.close_program)
        self.window.bind_all('<Escape>', self.exit_on_escape)
        self.window.mainloop()