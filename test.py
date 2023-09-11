import time


def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


print(get_current_time())

def get_mouse_position():
    import pyautogui
    print(pyautogui.position())



# @@@111111
