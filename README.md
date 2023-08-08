# CapsLockMorseCode


A silly module to control the keyboard LEDs of the CapsLock, NumLock, and ScrollLock keys to flash Morse Code on Windows, macOS, and Linux.

## Installation

To install with pip on macOS or Linux, run:

    python3 -m pip install capslockmorsecode

To install with pip on Windows, run:

    py -m pip install capslockmorsecode

## Quickstart Guide

You can pass a string to `morse()` to flash morse code with the CapsLock key. The string can either be text or morse code written with . for dots, - for dashes, / for intercharacter spacing, and a space character for word spacing:

    >>> import capslockmorsecode as mc
    >>> mc.morse('sos')
    >>> morse('.../---/...')

You can also flash individual dots and dashes with `dot()` and `dash()`:

    >>> import capslockmorsecode as mc
    >>> mc.dot()
    >>> mc.dash()

You can directly control the CapsLock and NumLock LEDs by passing `True` (on) or `False` (off) to `caps_lock()`, or just call `caps_lock()` to get the current state of it:

    >>> import capslockmorsecode as mc
    >>> mc.caps_lock(True)  # Turn on caps lock.
    >>> mc.caps_lock()
    True
    >>> mc.caps_lock(False) # Turn off caps lock.

Same for NumLock with the `num_lock()` function:

    >>> import capslockmorsecode as mc
    >>> mc.num_lock(True)  # Turn on caps lock.
    >>> mc.num_lock()
    True
    >>> mc.num_lock(False) # Turn off caps lock.





## Contribute

If you'd like to contribute to CapsLockMorseCode, check out https://github.com/asweigart/capslockmorsecode
