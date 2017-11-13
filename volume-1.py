# Created by Andre on Nov 2017
# Calculates volume


import ui
import math


def cal_volume(radius, height):
    # calculates volume
    volume = 2*math.pi*radius**2*height
    return volume

def cal_button_touch_up_inside(sender):
    input_radius =int(view['radius_textfield'].text)
    input_height =int(view['height_textfield'].text)
    answer = cal_volume(input_radius, input_height)
    view['answers_label'].text = str(answer)
    
view = ui.load_view()
view.present('sheet')
