"""Handlers for processed midi data"""

from lib.keys import keymap


# processor functions for the left analog stick
# input_array format is [int right_velocity, int left_velocity, int down_velocity, int up_velocity]

def process_lstick_nomod(input_array):
    """Process the analog lstick when no modifier key is pressed"""
    input_array[:] = [min(127, int(i * 1.4)) for i in
                      input_array]  # this is to make strong rstick inputs easier without
    # having to smash the keyboard

    lx = 128 + input_array[0] - input_array[1]  # x axis values range from 0 to 255, right is positive
    ly = 128 + input_array[2] - input_array[3]  # y axis values range from 0 to 255, down is positive

    return [lx, ly]


def process_lstick_mod(input_array):
    """Process the analog lstick when the general modifier key is pressed"""
    input_array[:] = [int(i / 2) for i in input_array]  # halves all input velocities

    lx = 128 + input_array[0] - input_array[1]
    ly = 128 + input_array[2] - input_array[3]

    return [lx, ly]


def process_lstick_xmod(input_array):
    """Process the analog lstick when the x-axis modifier key is pressed"""
    input_array[0:1] = [min(127, int(i * 1.4)) for i in input_array[0:1]]  # as normal for down and up
    input_array[2:3] = [int(i / 2) for i in input_array[2:3]]  # softened for right and left

    lx = 128 + input_array[0] - input_array[1]
    ly = 128 + input_array[2] - input_array[3]

    return [lx, ly]


def process_lstick_ymod(input_array):
    """Process the analog lstick when the y-axis modifier key is pressed"""
    input_array[2:3] = [min(127, int(i * 1.4)) for i in input_array[2:3]]  # as normal for right and left
    input_array[0:1] = [int(i / 2) for i in input_array[0:1]]  # softened for down and up

    lx = 128 + input_array[0] - input_array[1]
    ly = 128 + input_array[2] - input_array[3]

    return [lx, ly]


# processor functions for button-like inputs, including the right analog stick

def process_rstick(rinput_array):  # the right analog stick behaves like a set of 8 buttons
    """Process the right analog stick"""
    if rinput_array[0] and not rinput_array[1]:
        if rinput_array[2] and not rinput_array[3]:  # right, with slight down tilt
            rx = 255
            ry = 192
        elif rinput_array[3] and not rinput_array[2]:  # right, with slight up tilt
            rx = 255
            ry = 64
        else:  # right, no tilt
            rx = 255
            ry = 128
    elif rinput_array[1] and not rinput_array[0]:
        if rinput_array[2] and not rinput_array[3]:  # left, with slight down tilt
            rx = 0
            ry = 192
        elif rinput_array[3] and not rinput_array[2]:  # left, with slight up tilt
            rx = 0
            ry = 64
        else:  # left, no tilt
            rx = 0
            ry = 128
    elif rinput_array[2] and not rinput_array[3]:  # down only
        rx = 128
        ry = 255
    elif rinput_array[3] and not rinput_array[2]:  # up only
        rx = 128
        ry = 0
    else:  # conflicting or null input
        rx = 128
        ry = 128

    return [rx, ry]


def process_buttons(message):  # msg is a rtmidi midiin message
    """Process digital buttons"""
    return keymap[message[1]]  # returns button from midi key based on keymap dictionary
