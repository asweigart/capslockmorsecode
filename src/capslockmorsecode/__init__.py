"""CapsLockMorseCode
By Al Sweigart al@inventwithpython.com

A fun module to control the keyboard LEDs of the CapsLock and NumLock keys to flash Morse Code on Windows, macOS, and Linux."""

# TODO - do scroll lock and fn lock next

import time, sys, os

# NOTE - While it takes a millisecond to simulate the key press, the actual LEDs on the keyboard are much, much slower. I can flash an LED for about 20 milliseconds, and any less I have trouble seeing individual flashes reliably.

__version__ = '0.1.0'


VK_CAPITAL = 0x14
SC_CAPSLOCK = 0x3A
VK_NUMLOCK = 0x90
SC_NUMLOCK = 0x45

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

_DOT_DURATION = 0.1   # 1 unit length
_DASH_DURATION = 0.3  # 3 units length
_INTRA_CHAR_SPACING = 0.1  # 1 unit length, gap in between dots and dashes in a character
_INTER_CHAR_SPACING = 0.3  # 3 units length, gap between characters in a word
_WORD_SPACING = 0.7   # 7 units length, gap between words


class CapsLockMorseCodeException(Exception):
    pass

def _caps_lock_windows(value=None):
    """Get or set the caps lock LED on Windows. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = bool(ctypes.windll.user32.GetKeyState(VK_CAPITAL))

    if value is None:
        return current_led_state

    if bool(value) ^ current_led_state:
        # Simulate caps lock key press and release:
        ctypes.windll.user32.keybd_event(VK_CAPITAL, SC_CAPSLOCK, 0, 0)
        ctypes.windll.user32.keybd_event(VK_CAPITAL, SC_CAPSLOCK, 2, 0)

def _num_lock_windows(value=None):
    """Get or set the num lock LED on Windows. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""

    current_led_state = bool(ctypes.windll.user32.GetKeyState(VK_NUMLOCK))

    if value is None:
        return current_led_state

    if bool(value) ^ current_led_state:
        # Simulate num lock key press and release:
        ctypes.windll.user32.keybd_event(VK_NUMLOCK, SC_NUMLOCK, 0, 0)
        ctypes.windll.user32.keybd_event(VK_NUMLOCK, SC_NUMLOCK, 2, 0)


def _scroll_lock_windows(value=None):
    """Get or set the scroll lock LED on Windows. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = bool(ctypes.windll.user32.GetKeyState(VK_SCROLL))

    if value is None:
        return current_led_state

    if bool(value) ^ current_led_state:
        # Simulate caps lock key press and release:
        ctypes.windll.user32.keybd_event(VK_SCROLL, SC_SCROLLLOCK, 0, 0)
        ctypes.windll.user32.keybd_event(VK_SCROLL, SC_SCROLLLOCK, 2, 0)


def _caps_lock_x11(value=None):
    """Get or set the caps lock LED on Linux with X11 display server. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    if value is None:
        return True # TODO

    if bool(value) ^ current_led_state:
        fake_input(_display, X.KeyPress, 66)
        _display.sync()
        fake_input(_display, X.KeyRelease, 66)
        _display.sync()



def _num_lock_x11(value=None):
    """Get or set the num lock LED on Linux with X11 display server. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    if value is None:
        return True # TODO

    if bool(value) ^ current_led_state:
        fake_input(_display, X.KeyPress, 77)
        _display.sync()
        fake_input(_display, X.KeyRelease, 77)
        _display.sync()


def _scroll_lock_x11(value=None):
    """Get or set the scroll lock LED on Linux with X11 display server. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    if value is None:
        return True # TODO

    if bool(value) ^ current_led_state:
        fake_input(_display, X.KeyPress, 78)
        _display.sync()
        fake_input(_display, X.KeyRelease, 78)
        _display.sync()



def _caps_lock_wayland(value=None):
    """Get or set the caps lock LED on Linux with Wayland display server. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""

    """TODO
    from evdev import UInput, ecodes as e

    ui = UInput()
    ui.write(e.EV_KEY, e.KEY_CAPSLOCK, 1)  # CapsLock key down
    ui.write(e.EV_KEY, e.KEY_CAPSLOCK, 0)  # CapsLock key up
    ui.syn()
    ui.close()
    """
    current_led_state = ('LED_CAPSL', 1) in dev.leds(verbose=True)

    if value is None:
        return current_led_state

    dev.set_led(ecodes.LED_CAPSL, bool(value))


def _num_lock_wayland(value=None):
    """Get or set the num lock LED on Linux with Wayland display server. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = ('LED_NUML', 1) in dev.leds(verbose=True)

    if value is None:
        return current_led_state

    dev.set_led(ecodes.LED_NUML, bool(value))



def _scroll_lock_wayland(value=None):
    """Get or set the scroll lock LED on Linux with Wayland display server. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = ('LED_SCROLLL', 2) in dev.leds(verbose=True)  # TODO: TEST (LED_SCROLLL, 2)

    if value is None:
        return current_led_state

    dev.set_led(ecodes.LED_SCROLLL, bool(value))


def _caps_lock_macos(value=None):
    """Get or set the caps lock LED on macOS. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = bool(True) # TODO

    if value is None:
        return current_led_state

    if bool(value) ^ current_led_state:
        # Simulate caps lock key press and release:
        pass

def _num_lock_macos(value=None):
    """Get or set the num lock LED on macOS. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = bool(True) # TODO

    if value is None:
        return current_led_state

    if bool(value) ^ current_led_state:
        # Simulate caps lock key press and release:
        pass


def _scroll_lock_macos(value=None):
    """Get or set the scroll lock LED on macOS. Pass True or False to turn on/off the LED. Pass nothing to get the Boolean state of the LED: True for on and False for off."""
    current_led_state = bool(True) # TODO

    if value is None:
        return current_led_state

    if bool(value) ^ current_led_state:
        # Simulate caps lock key press and release:
        pass


def dot(duration=_DOT_DURATION, spacing=_INTRA_CHAR_SPACING, key='caps'):
    """Flash a morse code dot."""
    flash(duration, spacing, 1, key)


def dash(duration=_DASH_DURATION, spacing=_INTRA_CHAR_SPACING, key='caps'):
    """Flash a morse code dash."""
    flash(duration, spacing, 1, key)


def flash(duration=_DOT_DURATION, spacing=_INTRA_CHAR_SPACING, num_flashes=1, key='caps'):
    """Flash a keyboard LED."""
    for i in range(num_flashes):
        if key == 'caps':
            caps_lock(True)
            time.sleep(duration)
            caps_lock(False)
            time.sleep(spacing)
        elif key == 'num':
            num_lock(True)
            time.sleep(duration)
            num_lock(False)
            time.sleep(spacing)
        elif key == 'scroll':
            scroll_lock(True)
            time.sleep(duration)
            scroll_lock(False)

def morse(text, speed=1.0, key='caps'):
    """Flash a keyboard LED in morse code."""

    if all([c in ('.-/ ') for c in text]):
        # If all the characters in text are . - / (space), then just play them as morse code.
        for symbol in text:
            if symbol == '.':
                dot(_DOT_DURATION * (1.0 / speed), _INTRA_CHAR_SPACING * (1.0 / speed))
            elif symbol == '-':
                dash(_DASH_DURATION * (1.0 / speed), _INTRA_CHAR_SPACING * (1.0 / speed))
            elif symbol == '/':
                time.sleep(max(0, (_INTER_CHAR_SPACING - _INTRA_CHAR_SPACING) * (1.0 / speed)))
            elif symbol == ' ':
                time.sleep(max(0, (_WORD_CHAR_SPACING - _INTRA_CHAR_SPACING) * (1.0 / speed)))
        return


    # TODO - need a function to play strings that are just . and -

    last_char_was_alnum = False
    for character in text:
        character = character.upper()
        if character in MORSE_CODE:
            for symbol in MORSE_CODE[character]:
                if symbol == '.':
                    dot(_DOT_DURATION * (1.0 / speed), _INTRA_CHAR_SPACING * (1.0 / speed))
                elif symbol == '-':
                    dash(_DASH_DURATION * (1.0 / speed), _INTRA_CHAR_SPACING * (1.0 / speed))
                else:
                    assert False
            time.sleep(max(0, (_INTER_CHAR_SPACING - _INTRA_CHAR_SPACING) * (1.0 / speed)))
            last_char_was_alnum = True
        else:
            if last_char_was_alnum:
                # Pause in between words:
                time.sleep(max(0, (_WORD_SPACING - _INTER_CHAR_SPACING - _INTRA_CHAR_SPACING) * (1.0 / speed)))
                last_char_was_alnum = False  # Make sure only one space is paused for in case there are multiple spaces


def translate(text):
    if all([c in ('.-/ ') for c in text]):
        # Translate morse code into letters and numbers:
        pass


    translated = []

    words = text.split(' ') # go through and replace all non alnum with spaces
    for i, word in enumerate(words):
        for ii, character in enumerate(word):
            if character in MORSE_CODE:
                translated.append(MORSE_CODE[character])
                if ii < len(word):
                    translated.append('/')
    # TODO


if sys.platform == 'win32':
    import ctypes
    caps_lock = _caps_lock_windows
    num_lock = _num_lock_windows
    scroll_lock = _scroll_lock_windows
elif sys.platform == 'darwin':
    # TODO
    caps_lock = _caps_lock_macos
    num_lock = _num_lock_macos
    scroll_lock = _scroll_lock_macos
elif sys.platform == 'linux':
    display_server = os.environ.get("XDG_SESSION_TYPE", "unknown")
    if display_server == 'x11':
        from Xlib.display import Display
        from Xlib import X
        from Xlib.ext.xtest import fake_input
        _display = Display(os.environ['DISPLAY'])
        caps_lock = _caps_lock_x11
        num_lock = _num_lock_x11
    elif display_server == 'wayland':
        from evdev import InputDevice, ecodes
        try:
            dev = InputDevice('/dev/input/event1')
        except PermissionError:
            raise CapsLockMorseCodeException('Capslockmorsecode requires that Python is run as root.')

        caps_lock = _caps_lock_wayland
        num_lock = _num_lock_wayland
    else:
        raise CapsLockMorseCodeException('Unknown display server. Capslockmorsecode can only run on X11 or Wayland.')
