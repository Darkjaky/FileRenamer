#!/usr/bin/python
import tkinter
from .settings import window_name, frame_size


def create_window():
    main_frame = tkinter.Tk()
    main_frame.title(window_name)
    main_frame.geometry(frame_size)
    # Code to add widgets will go here...
    main_frame.mainloop()
