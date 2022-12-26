"""
A Timer controller for a Sudoku game.
@author: Edom Maru(eam43)
@author: Souad Yakubu(sny2)
@date: Fall, 2022

"""

from guizero import App, Text, PushButton
from datetime import datetime
from sys import exit

#This code was taken from timer.py
class Timer:
    ''' Counts time for the sudoku game'''
    def __init__(self):
        '''calls the method reset'''
        self.reset()

    def reset(self):
        ''' initializes the time from 0'''
        self.start_time = datetime.now()

    def get_time(self):
        '''runs the time'''
        self.time_since_start = datetime.now() - self.start_time
        return self.time_since_start.total_seconds()

    

