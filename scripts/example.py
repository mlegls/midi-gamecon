"""Extensible main script. Currently only prints controller outputs, but may be connected to an external virtual
controller API for full functionality """

from __future__ import print_function

import logging
import sys
import time

from rtmidi.midiutil import open_midiinput

from lib import keys as k, logic_handler as lh, midi_handler as mh

# For verbose output
log = logging.getLogger('midiin_poll')
logging.basicConfig(level=logging.DEBUG)


def example():
    # Setup midi input port, from
    # https://github.com/SpotlightKid/python-rtmidi/blob/master/examples/basic/midiin_poll.py
    port = sys.argv[1] if len(sys.argv) > 1 else None

    try:
        midiin, port_name = open_midiinput(port)
    except (EOFError, KeyboardInterrupt):
        sys.exit()

    # Main loop, based on
    # https://github.com/SpotlightKid/python-rtmidi/blob/master/examples/basic/midiin_poll.py
    # SHOULD BE GRADED
    print("Entering main loop. Press Control-C to exit.")
    try:
        timer = time.time()

        while True:
            msg = midiin.get_message()  # receives midi message, including null

            if msg:  # checks for any input

                message, deltatime = msg  # msg format is 2 parts, an array [type, note, velocity] and deltatime
                timer += deltatime  # for consistent clock rate

                if message[1] in k.valid_keys:  # checks if input is valid

                    # process buttons
                    if message[1] in k.buttons:
                        if message[0] == 144:  # checks for noteon message only
                            print('Button: ' + lh.process_buttons(message))

                    # process right stick
                    elif message[1] in k.rstick:
                        mh.process_rstick(message)  # edit rinput_array

                        rx = lh.process_rstick(k.rinput_array)[0]
                        ry = lh.process_rstick(k.rinput_array)[1]

                        print('RX: ' + str(rx) + '\nRY: ' + str(ry))

                    # process lstick modifiers
                    elif message[1] in k.modifiers:
                        mh.process_mods(message)  # edits appropriate mod variables in keys.py

                    # process left stick
                    elif message[1] in k.lstick:
                        mh.process_lstick(message)  # edit input_array

                        # return appropriate controller outputs
                        if not k.xmod and not k.mod and not k.ymod:
                            lx = lh.process_lstick_nomod(k.input_array)[0]
                            ly = lh.process_lstick_nomod(k.input_array)[1]
                        elif k.xmod and not k.ymod:
                            lx = lh.process_lstick_xmod(k.input_array)[0]
                            ly = lh.process_lstick_xmod(k.input_array)[1]
                        elif k.ymod and not k.xmod:
                            lx = lh.process_lstick_ymod(k.input_array)[0]
                            ly = lh.process_lstick_ymod(k.input_array)[1]
                        else:  # xmod and ymod held together do the same thing as the general modifier
                            lx = lh.process_lstick_mod(k.input_array)[0]
                            ly = lh.process_lstick_mod(k.input_array)[1]

                        print('LX: ' + str(lx) + '\nLY: ' + str(ly))

            time.sleep(0.001)
    except KeyboardInterrupt:
        print('')
    finally:
        print("Exit.")
        midiin.close_port()
        del midiin
