#-*-coding:utf-8
"""
Author : Byunghyun Ban
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
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

# ���̺귯������ ����� Ű���� �̸� �����մϴ�.
KEYMAP = {
    # ���� Ű
    "esc": "esc", "window": "win",
    "command": "command", "option": "option",
    "control": "ctrl", "alt": "alt", "kor_eng": "hanguel",
    "print_screen": "prtsc", "scroll_lock": "scrolllock",
    "pause_break": "pause", "vol_up": "volumeup",
    "vol_down": "volumedown", "vol_mute": "volumemute",
    "hanja": "hanja",

    # ��� Ű
    "f1": "f1", "f2": "f2", "f3": "f3", "f4": "f4",
    "f5": "f5", "f6": "f6", "f7": "f7", "f8": "f8",
    "f9": "f9", "f10": "f10", "f11": "f11", "f12": "f12",

    # ȭ��ǥ Ű
    "left_arrow": "left", "right_arrow": "right",
    "up_arrow": "up", "down_arrow": "down",

    # Ž�� Ű
    "insert": "insert", "home": "home", "page_up": "pageup",
    "delete": "delete", "end": "end", "page_down": "pgdn",

    # �Է� Ű (����)
    "backspace": "backspace", "enter": "enter", "shift": "shift",
    "tab": "tab", "caps_lock": "capslock", "spacebar": "space",

    # �Է� Ű (����)
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",

    # �Է� Ű (���ĺ�)
    "a": "a", "b": "b", "c": "c", "d": "d", "e": "e",
    "f": "f", "g": "g", "h": "h", "i": "i", "j": "j",
    "k": "k", "l": "l", "m": "m", "n": "n", "o": "o",
    "p": "p", "q": "q", "r": "r", "s": "s", "t": "t",
    "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z",

    # �Է� Ű (Ư������)
    ";": ";", "=": "=", ",": ",", "-": "-", ".": ".",
    "/": "/", "`": "`", "[": "[", "\\": "\\", "]": "]",
    "'": "'",

    # ���е�
    "num_lock": "numlock", "numpad_/": "", "numpad_*": "multiply",
    "numpad_-": "-", "numpad_+": "+", "numpad_.": ".",
    "numpad_7": "num7", "numpad_8": "num8", "numpad_9": "num9",
    "numpad_4": "num4", "numpad_5": "num5", "numpad_6": "num6",
    "numpad_1": "num1", "numpad_2": "num2", "numpad_3": "num3",
    "numpad_0": "num0",
}

# �빮�� Ư�����ڸ� ���� ��ųʸ��Դϴ�.
UPPER_SPECIAL = {
    "!": 1, "@": 2, "#": 3, "$": 4, "%": 5, "^": 6,
    "&": 7, "*": 8, "(": 9, ")": 0, "_": "-", "~": '`', "|": '\\',
    "{": "[", "}": "]", ":": ";", '"': "'", "?": "/", "<": ",", ">": "."
}


# ���콺�� Ư����ġ�� �̵���Ű�� �Լ�
def move_mouse(location):
    # location �� �Է¹޾� �� ��ġ�� ���콺�� �̵���ŵ�ϴ�.
    pyautogui.moveTo(location)


# ���콺�� ���� ��ǥ�� ���ϴ� �Լ�
def get_mouse_position():
    # ���콺 Ŀ���� ���� ��ġ�� ����մϴ�.
    # ��ũ�θ� �����ϴ� ��������, �ֿܼ��� �ҷ��ͼ� ���� �����մϴ�.
    return tuple(pyautogui.position())


# ������ ��ġ�� ���콺 Ŀ���� �̵��ϰ� ���� ��ư�� Ŭ���ϴ� �Լ�
def click(location):
    # ���콺�� Ŭ���մϴ�..
    pyautogui.click(location)


# ������ ��ġ�� ���콺 Ŀ���� �̵��ϰ� ������ ��ư�� Ŭ���ϴ� �Լ�
def right_click(location):
    pyautogui.click(location, button='right')


# ����Ŭ��
def double_click(location):
    pyautogui.click(location, button='left', clicks=2, interval=0.25)


# Ű�� �� �� �����ٰ� ���� �Լ��Դϴ�.
def key_press_once(key):
    key_on(key)
    key_off(key)


# ���� �Է� (Ŭ�����忡 ���� �� �ٿ��ֱ�)
# �ѱ��� ��쿡�� ����ϼ���. �ѱ��� ���¼� ���ذ� ����Ͽ� �׷����ϴ�.
def type_in(string):
    # Ŭ�����忡 ��Ʈ���� ����ֽ��ϴ�.
    pyperclip.copy(string)
    # Ctrl v�� �ٿ��ֱ� �մϴ�.
    ctrl_v()


# ����, ����, Ư�����ڷ� �� ��Ʈ���� �ٷ� �Է��ϴ� �Լ��Դϴ�.
def typing(string):
    pyautogui.write(string)


# Ű�� ��� ������ �ֵ��� �ϴ� �Լ��Դϴ�.
def key_on(key):
    # �������� KEYMAP�� ������ ������ �����մϴ�.
    global KEYMAP
    # �Է¹��� ���� �ҹ��ڷ� ��ȯ�մϴ�.
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # Ű�ʿ��� Ű �ڵ带 �̾ƿɴϴ�.
        key_code = KEYMAP[key.lower()]
        pyautogui.keyDown(key_code)
    except KeyError:
        # Ű�ʿ� ���õ��� ���� Ű�� ��û�߽��ϴ�. �����޽����� ����մϴ�.
        print(key + " is not an available key input.")
        # ���α׷��� �����մϴ�.
        exit(1)


# ������ Ű�� ���� �ϴ� �Լ��Դϴ�.
def key_off(key):
    # �������� KEYMAP�� ������ ������ �����մϴ�.
    global KEYMAP
    # �Է¹��� ���� �ҹ��ڷ� ��ȯ�մϴ�.
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # Ű�ʿ��� Ű �ڵ带 �̾ƿɴϴ�.
        key_code = KEYMAP[key.lower()]
        pyautogui.keyUp(key_code)
    except KeyError:
        # Ű�ʿ� ���õ��� ���� Ű�� ��û�߽��ϴ�. �����޽����� ����մϴ�.
        print(key + " is not an available key input.")
        # ���α׷��� �����մϴ�.
        exit(1)


# ���콺�� ���� �ڸ����� ���� ��ư�� Ŭ���ϴ� �Լ�
def l_click():
    pyautogui.click()


# ���콺�� ���� �ڸ����� ������ ��ư�� Ŭ���ϴ� �Լ�
def r_click():
    pyautogui.click(button='right')


# ���콺 ��ũ���� �ø��� �Լ�
def mouse_upscroll(number=1000):
    x, y = get_mouse_position()
    # �� ĭ�̳� �ø��� number�� �Է¹޽��ϴ�.
    pyautogui.scroll(number, x=x, y=y)


# ���콺 ��ũ���� ������ �Լ�
def mouse_downscroll(number=1000):
    x, y = get_mouse_position()
    # �� ĭ�̳� �ø��� number�� �Է¹޽��ϴ�.
    pyautogui.scroll(-1 * number, x=x, y=y)


# �巡�׵�� �Լ�
def drag_drop(frm, to):
    # ��ǥ���� �Է¹޽��ϴ�.
    x, y = to
    # Ŭ�� ������������ Ŀ���� �ű�ϴ�.
    move_mouse(frm)
    # �巡�׸� �����մϴ�
    pyautogui.dragTo(x, y, 0.5, button='left')


# Ư�� ��ǥ�� ������ 16������ �о� ���� �Լ��Դϴ�.
def get_color(location):
    # ��ǥ�� ���մϴ�.
    x, y = location
    # RGB �ȼ����� ���մϴ�.
    try:
        pixel = pyautogui.pixel(x, y)
    except OSError:
        print("OS Error �߻�. �ٽ� �õ��մϴ�.")
        return get_color(location)
    return '0x%02x%02x%02x' % pixel


# Ctrl C (����)
def ctrl_c():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # c�� �����ϴ�.
    key_on("c")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("c")


# Ctrl V (�ٿ��ֱ�)
def ctrl_v():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # v�� �����ϴ�.
    key_on("v")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("v")


# Ctrl A (��� ����)
def ctrl_a():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # a�� �����ϴ�.
    key_on("a")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("a")


# Ctrl F (ã��)
def ctrl_f():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # a�� �����ϴ�.
    key_on("f")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("f")


# Alt F4 (����)
def alt_f4():
    # Alt�� �����ϴ�.
    key_on("alt")
    # F4�� �����ϴ�.
    key_on("f4")
    # �� Ű�� ��� ���ϴ�.
    key_off("alt")
    key_off("f4")


# Alt Tab (ȭ�� ��ȯ)
def alt_tab():
    # Alt�� �����ϴ�.
    key_on("alt")
    # F4�� �����ϴ�.
    key_on("tab")
    # �� Ű�� ��� ���ϴ�.
    key_off("alt")
    key_off("tab")


# �̹����� �Է¹޾� ȭ�鿡�� ��ġ�� Ž���մϴ�.
# ȭ�鿡�� �̹����� �߰ߵ��� ���� ��� False�� �����մϴ�.
def find_on_screen(filename, confidence=0.7):
    a = pyautogui.locateCenterOnScreen(filename, confidence=confidence)
    if not a:
        return False
    else:
        return a[0], a[1]
