import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep

pt.FAILSAFE = True
mouse = Controller()


def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.8)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.5)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click(clicks=clicks, interval=.1)


def get_message():
    nav_to_image('images/paperclip.png', 0, off_y=-65)
    mouse.click(Button.left, 3)
    pt.rightClick()

    copy = nav_to_image('images/copy.png', 1)
    sleep(.5)
    return pc.paste() if copy != 0 else 0

def send_message(msg):
    nav_to_image('images/paperclip.png',2, off_x=100)
    pt.typewrite(msg, interval=.1)
    pt.typewrite('\n')

def close_reply_box():
    nav_to_image('images/x.png', 2)

def process_message(msg):
    raw_msg = msg.lower()


    if raw_msg == 'hello':
        return 'Hey there!'
    elif raw_msg == 'yes':
        return ' Bot says you wrote yes!'
    elif 'ok' in raw_msg:
        return 'You wrote ok!'
    else:
        return 'I did not understand what you wrote.'
    

delay = 10
last_message = ''

sleep(3)
while True:
    nav_to_image('images/green_dot.png', 2, off_x=-100)
    close_reply_box()


    message = get_message()
    if message != 0 and message != last_message:
        last_message = message
        send_message(process_message(message))
    else:
        print('No new messages...')

print(process_message(' I am ok'))


