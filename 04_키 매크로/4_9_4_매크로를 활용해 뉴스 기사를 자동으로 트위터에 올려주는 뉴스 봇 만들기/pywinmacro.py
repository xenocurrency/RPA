#-*-coding:euc-kr
"""
Author : Byunghyun Ban
Book : 6???? ? ?????? ??? ???? ?????? ???? ????
"""
import time

try:
    import pyperclip
    import pyautogui
except ModuleNotFoundError:
    import pip

    pip.main(['install', 'pyautogui'])
    pip.main(['install', 'pillow'])
    pip.main(['install', 'pyperclip'])
    pip.main(['install', 'opencv-python'])
    try:
        import pyperclip
        import pyautogui
    except ModuleNotFoundError:
        time.sleep(2)
        import pyperclip
        import pyautogui

# ??????????? ????? ????? ??? ????????.
KEYMAP = {
    # ???? ?
    "esc": "esc", "window": "win",
    "command": "command", "option": "option",
    "control": "ctrl", "alt": "alt", "kor_eng": "hanguel",
    "print_screen": "prtsc", "scroll_lock": "scrolllock",
    "pause_break": "pause", "vol_up": "volumeup",
    "vol_down": "volumedown", "vol_mute": "volumemute",
    "hanja": "hanja",

    # ??? ?
    "f1": "f1", "f2": "f2", "f3": "f3", "f4": "f4",
    "f5": "f5", "f6": "f6", "f7": "f7", "f8": "f8",
    "f9": "f9", "f10": "f10", "f11": "f11", "f12": "f12",

    # ???? ?
    "left_arrow": "left", "right_arrow": "right",
    "up_arrow": "up", "down_arrow": "down",

    # ??? ?
    "insert": "insert", "home": "home", "page_up": "pageup",
    "delete": "delete", "end": "end", "page_down": "pgdn",

    # ??? ? (????)
    "backspace": "backspace", "enter": "enter", "shift": "shift",
    "tab": "tab", "caps_lock": "capslock", "spacebar": "space",

    # ??? ? (????)
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",

    # ??? ? (?????)
    "a": "a", "b": "b", "c": "c", "d": "d", "e": "e",
    "f": "f", "g": "g", "h": "h", "i": "i", "j": "j",
    "k": "k", "l": "l", "m": "m", "n": "n", "o": "o",
    "p": "p", "q": "q", "r": "r", "s": "s", "t": "t",
    "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",

    # ??? ? (???????)
    ";": ";", "=": "=", ",": ",", "-": "-", ".": ".",
    "/": "/", "`": "`", "[": "[", "\\": "\\", "]": "]",
    "'": "'",

    # ???��?
    "num_lock": "numlock", "numpad_/": "", "numpad_*": "multiply",
    "numpad_-": "-", "numpad_+": "+", "numpad_.": ".",
    "numpad_7": "num7", "numpad_8": "num8", "numpad_9": "num9",
    "numpad_4": "num4", "numpad_5": "num5", "numpad_6": "num6",
    "numpad_1": "num1", "numpad_2": "num2", "numpad_3": "num3",
    "numpad_0": "num0",
}

# ???? ???????? ???? ?????????.
UPPER_SPECIAL = {
    "!": 1, "@": 2, "#": 3, "$": 4, "%": 5, "^": 6,
    "&": 7, "*": 8, "(": 9, ")": 0, "_": "-", "~": '`', "|": '\\',
    "{": "[", "}": "]", ":": ";", '"': "'", "?": "/", "<": ",", ">": "."
}


# ?????? ???????? ???????? ???
def move_mouse(location):
    # location ?? ??��?? ?? ????? ?????? ?????????.
    pyautogui.moveTo(location)


# ?????? ???? ????? ????? ???
def get_mouse_position():
    # ???? ��???? ???? ????? ???????.
    # ????��? ??????? ????????, ?????? ?????? ???? ????????.
    return tuple(pyautogui.position())


# ?????? ????? ???? ��???? ?????? ???? ????? ?????? ???
def click(location):
    # ?????? ???????..
    pyautogui.click(location)


# ?????? ????? ???? ��???? ?????? ?????? ????? ?????? ???
def right_click(location):
    pyautogui.click(location, button='right')


# ???????
def double_click(location):
    pyautogui.click(location, button='left', clicks=2, interval=0.25)


# ??? ?? ?? ??????? ???? ???????.
def key_press_once(key):
    key_on(key)
    key_off(key)


# ???? ??? (??????? ???? ?? ??????)
# ????? ??��?? ????????. ????? ???��? ????? ?????? ????????.
def type_in(string):
    # ??????? ??????? ?????????.
    pyperclip.copy(string)
    # Ctrl v?? ?????? ????.
    ctrl_v()


# ????, ????, ???????? ?? ??????? ??? ?????? ???????.
def typing(string):
    pyautogui.write(string)


# ??? ??? ?????? ????? ??? ???????.
def key_on(key):
    # ???????? KEYMAP?? ?????? ?????? ????????.
    global KEYMAP
    # ??��??? ???? ?????? ???????.
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # ?????? ? ??? ??????.
        key_code = KEYMAP[key.lower()]
        pyautogui.keyDown(key_code)
    except KeyError:
        # ???? ??????? ???? ??? ?????????. ??????????? ???????.
        print(key + " is not an available key input.")
        # ???��???? ????????.
        exit(1)


# ?????? ??? ???? ??? ???????.
def key_off(key):
    # ???????? KEYMAP?? ?????? ?????? ????????.
    global KEYMAP
    # ??��??? ???? ?????? ???????.
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # ?????? ? ??? ??????.
        key_code = KEYMAP[key.lower()]
        pyautogui.keyUp(key_code)
    except KeyError:
        # ???? ??????? ???? ??? ?????????. ??????????? ???????.
        print(key + " is not an available key input.")
        # ???��???? ????????.
        exit(1)


# ?????? ???? ??????? ???? ????? ?????? ???
def l_click():
    pyautogui.click()


# ?????? ???? ??????? ?????? ????? ?????? ???
def r_click():
    pyautogui.click(button='right')


# ???? ??????? ?��??? ???
def mouse_upscroll(number=1000):
    x, y = get_mouse_position()
    # ?? ???? ?��??? number?? ??��?????.
    pyautogui.scroll(number, x=x, y=y)


# ???? ??????? ?????? ???
def mouse_downscroll(number=1000):
    x, y = get_mouse_position()
    # ?? ???? ?��??? number?? ??��?????.
    pyautogui.scroll(-1 * number, x=x, y=y)


# ?��???? ???
def drag_drop(frm, to):
    # ??????? ??��?????.
    x, y = to
    # ??? ???????????? ��???? ?????.
    move_mouse(frm)
    # ?��??? ????????
    pyautogui.dragTo(x, y, 0.5, button='left')


# ??? ????? ?????? 16?????? ?��? ???? ???????.
def get_color(location):
    # ????? ??????.
    x, y = location
    # RGB ??????? ??????.
    try:
        pixel = pyautogui.pixel(x, y)
    except OSError:
        print("OS Error ???. ??? ???????.")
        return get_color(location)
    return '0x%02x%02x%02x' % pixel


# Ctrl C (????)
def ctrl_c():
    # Ctrl?? ???????.
    key_on("control")
    # c?? ???????.
    key_on("c")
    # ?? ??? ??? ?????.
    key_off("control")
    key_off("c")


# Ctrl V (??????)
def ctrl_v():
    # Ctrl?? ???????.
    key_on("control")
    # v?? ???????.
    key_on("v")
    # ?? ??? ??? ?????.
    key_off("control")
    key_off("v")


# Ctrl A (??? ????)
def ctrl_a():
    # Ctrl?? ???????.
    key_on("control")
    # a?? ???????.
    key_on("a")
    # ?? ??? ??? ?????.
    key_off("control")
    key_off("a")


# Ctrl F (???)
def ctrl_f():
    # Ctrl?? ???????.
    key_on("control")
    # a?? ???????.
    key_on("f")
    # ?? ??? ??? ?????.
    key_off("control")
    key_off("f")


# Alt F4 (????)
def alt_f4():
    # Alt?? ???????.
    key_on("alt")
    # F4?? ???????.
    key_on("f4")
    # ?? ??? ??? ?????.
    key_off("alt")
    key_off("f4")


# Alt Tab (??? ???)
def alt_tab():
    # Alt?? ???????.
    key_on("alt")
    # F4?? ???????.
    key_on("tab")
    # ?? ??? ??? ?????.
    key_off("alt")
    key_off("tab")


# ??????? ??��?? ????? ????? ???????.
# ????? ??????? ?????? ???? ??? False?? ????????.
def find_on_screen(filename, confidence=0.7):
    a = pyautogui.locateCenterOnScreen(filename, confidence=confidence)
    if not a:
        return False
    else:
        return a[0], a[1]
