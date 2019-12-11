# MIDI-Gamecon
Final project for COGS 18 at UCSD Fall 2019. A  modular and extensible framework for turning MIDI keyboards into game controllers, loosely inspired by https://github.com/Hpmason/Switch-UART-Controller-Tools

## Overview
This project is the framework for converting a standard USB MIDI keyboard into a unique game controller with 2 analog sticks and 14 digital buttons, including HOME, START, and a 4-button directional pad.

Currently, example.py only logs the corresponding controller inputs to various MIDI inputs to the console, but it can easily be extended with libraries like [pyvjoy](https://github.com/tidzo/pyvjoy) (for Windows) or [python-uinput](https://pypi.org/project/python-uinput/) (for Linux) to function as a true virtual controller.

In the near future, I am planning on adapting this project for a [Teensy 3.6](https://www.pjrc.com/store/teensy36.html) to make a fully functioning standalone game controller based on [these](https://github.com/progmem/Switch-Fightstick) [projects](https://github.com/fluffymadness/ATMega32U4-Switch-Fightstick).

## Keymappings
Copied over from `keymap.txt`

### Joystick

| Midi Key | Controller Input |
|----------|------------------|
| C4       | LSTICK left      |
| C#4      | LSTICK up        |
| D4       | LSTICK down      |
| D#4      | LSTICK right     |

| Midi Key | Controller Input |
|----------|------------------|
| G4        | LMOD x          |
| A5        | LMOD soft       |
| B5        | LMOD y          |

| Midi Key | Controller Input |
|----------|------------------|
| C5       | RSTICK left      |
| C#5      | RSTICK up        |
| D5       | RSTICK down      |
| D#5      | RSTICK right     |

### Buttons

| Midi Key | Controller Input |
|----------|------------------|
| F5       | A                |
| F#5      | B                |
| G#5      | X                |
| A#5      | Y                |

| Midi Key | Controller Input |
|----------|------------------|
| E5       | ZR               |
| G5       | L                |
| A5       | R                |
| B5       | ZL               |

| Midi Key | Controller Input |
|----------|------------------|
| C#2      | HOME             |
| D#2      | START            |

| Midi Key | Controller Input |
|----------|------------------|
| C3       | DPAD left        |
| C#3      | DPAD up          |
| D3       | DPAD down        |
| D#3      | DPAD right       |

## The Left Analog Stick
The left analog stick is controlled by 4 keys corresponding to the cardinal directions left, up, down, right, in addition to 3 modifier buttons. The strength of input in any particular direction corresponds to the velocity of the midi keypress (how hard you press the key). If opposing directions are pressed at the same time, the opposing velocity vectors are added to each other, and the resultant signal is a weaker signal in the harder-pressed direction.

The 3 modifier keys are respectively a general modifier button, a y-axis modifier, and an x-axis modifier.

The general modifier halves the velocity of all inputs. The y-axis modifier halves the velocity of x-axis inputs (making the final input vector more y-oriented). The x-axis modifier halves the velocity of y-axis inputs.

## The Right Analog Stick
The right analog stick is currently tuned specifically for the *Super Smash Bros.* series of fighting games, where right stick inputs behave as if they are a discrete signal (either on or off) in any direction. In this project, the right stick is controlled by 4 buttons corresponding to the cardinal directions, with combinations of these buttons corresponding to an additional 8 diagonal directions. 

Again because of the specific tuning of this project, the diagonal directions favor the x-axis (i.e. they are mostly rightwards or leftwards, with a slight vertical tilt). However, this can be easily configured in the `process_rstick` function in `lib\logic_handler.py`.