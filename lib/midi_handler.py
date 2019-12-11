"""Handlers for raw midi data"""

import lib.keys as k


def process_rstick(message):
    if message[1] == 60:  # left
        if message[0] == 144:
            k.rinput_array[1] = 1
        else:  # resets the corresponding array entry on noteoff
            k.rinput_array[1] = 0
    elif message[1] == 61:  # up
        if message[0] == 144:
            k.rinput_array[3] = 1
        else:
            k.rinput_array[3] = 0
    elif message[1] == 62:  # down
        if message[0] == 144:
            k.rinput_array[2] = 1
        else:
            k.rinput_array[2] = 0
    elif message[1] == 63:  # right
        if message[0] == 144:
            k.rinput_array[0] = 1
        else:
            k.rinput_array[0] = 0


def process_mods(message):
    if message[1] == 55:  # xmod
        if message[0] == 144:
            k.xmod = 1
        else:
            k.xmod = 0
    elif message[1] == 57:  # mod
        if message[0] == 144:
            k.mod = 1
        else:
            k.mod = 0
    elif message[1] == 59:  # ymod
        if message[0] == 144:
            k.ymod = 1
        else:
            k.ymod = 0


def process_lstick(message):
    if message[1] == 48:  # left
        if message[0] == 144:
            k.input_array[1] = message[2]
        else:
            k.input_array[1] = 0
    elif message[1] == 49:  # up
        if message[0] == 144:
            k.input_array[3] = message[2]
        else:
            k.input_array[3] = 0
    elif message[1] == 50:  # down
        if message[0] == 144:
            k.input_array[2] = message[2]
        else:
            k.input_array[2] = 0
    elif message[1] == 51:  # right
        if message[0] == 144:
            k.input_array[0] = message[2]
        else:
            k.input_array[0] = 0
