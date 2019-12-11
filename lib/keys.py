"""Helper data structures that have to do with keys"""

# mutable global variables

input_array = [0, 0, 0, 0]  # right, left, down, up
rinput_array = [0, 0, 0, 0]

mod = 0
xmod = 0
ymod = 0

# immutable
keymap = {  # maps midi keys to controller buttons
    65: 'A',  # F5
    66: 'B',  # F#5
    68: 'X',  # G#5
    70: 'Y',  # A#5
    64: 'ZR',  # E5
    67: 'L',  # G5
    69: 'R',  # A5
    71: 'ZL',  # B5
    25: 'HOME',  # C#2
    27: 'START',  # D#2
    36: 'DL',  # C3
    37: 'DU',  # C#3
    38: 'DD',  # D3
    39: 'DR',  # D#3
}

valid_keys = (65, 66, 68, 70,  # A, B, X, Y
              64, 67, 69, 71,  # ZR, L, R, ZL
              25, 27,  # HOME, START
              36, 37, 38, 39,  # directional pad
              48, 49, 50, 51,  # left analog stick
              60, 61, 62, 63,  # right analog stick
              55, 57, 59  # left analog stick modifiers
              )
buttons = (65, 66, 68, 70,  # A, B, X, Y
           64, 67, 69, 71,  # ZR, L, R, ZL
           25, 27,  # HOME, START
           36, 37, 38, 39,  # directional pad
           )

rstick = (60, 61, 62, 63)  # left, up, down, right

lstick = (48, 49, 50, 51)

modifiers = (55, 57, 59)  # xmod, mod, ymod
