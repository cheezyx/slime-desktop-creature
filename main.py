import tkinter as tk
import random
import pyautogui as pag
from setup import Setup
from assignment import Assignment

setup = Setup()
assignment = Assignment(setup)

assignment.start_program()