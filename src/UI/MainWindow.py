#!/usr/bin/python
from tkinter import Tk, scrolledtext

from src.UI.settings import window_name, frame_size
import src.UI.FileRenamer


def create_window():
    src.UI.FileRenamer.vp_start_gui()
