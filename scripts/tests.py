"""Test functions"""

import inspect

from lib import keys, logic_handler as lh, midi_handler as mh


def test_keys():
    """Test that all data structures in keys.py are of the correct type"""
    assert type(keys.keymap) == dict
    assert type(keys.input_array) == list
    assert type(keys.rinput_array) == list
    for i in [keys.xmod, keys.ymod, keys.mod]:
        assert type(i) == int
    for i in [keys.valid_keys, keys.buttons, keys.rstick, keys.lstick, keys.modifiers]:
        assert type(i) == tuple


def test_callable():
    """Test that all functions are inspect.signature on their intended inputs"""
    assert inspect.signature(lh.process_buttons).bind([144, 65, 100])  # midi message [on/off, note, velocity],
    # A Button (F5)
    assert inspect.signature(lh.process_rstick).bind([0, 0, 0, 0])  # array of booleans [right, left, down, up]
    assert inspect.signature(lh.process_lstick_nomod).bind([0, 0, 0, 0])  # array of velocities [right, left, down, up]
    assert inspect.signature(lh.process_lstick_mod).bind([0, 0, 0, 0])  # same as lstick_nomod
    assert inspect.signature(lh.process_lstick_ymod).bind([0, 0, 0, 0])  # same as lstick_nomod
    assert inspect.signature(lh.process_lstick_xmod).bind([0, 0, 0, 0])  # same as lstick_nomod
    assert inspect.signature(mh.process_lstick).bind([144, 48, 100])  # midi message, lstick left (C4)
    assert inspect.signature(mh.process_rstick).bind([144, 60, 100])  # midi message, rstick left (C5)
    assert inspect.signature(mh.process_mods).bind([144, 55, 100])  # midi message, xmod (G4)


def test_rstick():
    """Tests rstick logic"""
    assert lh.process_rstick([0, 0, 0, 0]) == [128, 128]
    assert lh.process_rstick([1, 0, 0, 0]) == [255, 128]
    assert lh.process_rstick([1, 1, 0, 0]) == [128, 128]
    assert lh.process_rstick([1, 0, 1, 0]) == [255, 192]


def test_lstick():
    assert lh.process_lstick_nomod([0, 0, 0, 0]) == [128, 128]
    assert lh.process_lstick_nomod([100, 0, 0, 0]) == [255, 128]  # capped input
    assert lh.process_lstick_nomod([100, 50, 0, 0]) == [185, 128]  # 255-70
    assert lh.process_lstick_nomod([50, 0, 50, 0]) == [198, 198]
    assert lh.process_lstick_mod([100, 0, 0, 0]) == [178, 128]
    assert lh.process_lstick_ymod([100, 0, 100, 0]) == [178, 255]
    assert lh.process_lstick_xmod([100, 0, 100, 0]) == [255, 178]
