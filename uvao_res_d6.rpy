﻿init python:
    # функция мерцания кота
    # случайно делаем прозрачным (есл random < down) или непрозрачным - если random > up. Если между up и down - тогда делаем частичную прозрачность в зависимости от r
    blink_threshold_up = 0.5 # верхний порог прозрачности
    blink_threshold_down = 0.5 # нижний порог
    def random_blink(trans, st, at):
        r = renpy.random.random()
        if r < blink_threshold_down:
            trans.alpha = 0.0
        elif r > blink_threshold_up:
            trans.alpha = 1.0
        else:
            trans.alpha = (r - blink_threshold_down) / (blink_threshold_up - blink_threshold_down)
        # return renpy.random.random() * 0.5
        return 0.05
init:

init:
    
#Ресы для кошочки
#bg:
    #ext's
    #int's
    image bg int_isolat_day = get_image_7dl("bg/int_isolat_day.jpg")
    image bg int_isolat_day_uv = get_image_7dl("bg/int_isolat_day_uv.jpg")
    image bg ext_lake_day = get_image_7dl("bg/ext_lake_day.jpg") # У Автора уже есть озеро, с березой. Предлагаю оставить его.
    image bg ext_lake_night = get_image_7dl("bg/ext_lake_night.jpg")
    image bg ext_roof = get_image_7dl("bg/ext_roof.jpg")
#cg
    image cg d6_uv_angry_dv = get_image_7dl("cg/d6_uv_angry_dv.jpg")
    image cg d6_uv_behind_view = get_image_7dl("cg/d6_uv_behind_view.jpg")
    image cg d6_sl_campfire = get_image_7dl("cg/d6_sl_campfire.jpg")
    image cg d6_uv_roofdance = get_image_7dl("cg/d6_uv_roof_dance.jpg")
    image cg d7_uv_loonybin = get_image_7dl("cg/d7_uv_loonybin_nocat.jpg")
    image cg d7_uv_loonybin_blinkcat: #мигающий кот
        contains:
            get_image_7dl("cg/d7_uv_loonybin_nocat.jpg")
        contains:
            get_image_7dl("cg/d7_uv_mystic_cat.png")
            function random_blink
            repeat
#Кусты
    image bush_frame = get_image_7dl("gui/Bush/bush_frame.png")
    image bush_bottom_central = get_image_7dl("gui/Bush/bush_bottom_central.png")
    image bush_left_bottom = get_image_7dl("gui/Bush/bush_left_bottom.png")
    image bush_left_central = get_image_7dl("gui/Bush/bush_left_central.png")
    image bush_left_top = get_image_7dl("gui/Bush/bush_left_top.png")
    image bush_right_bottom = get_image_7dl("gui/Bush/bush_right_bottom.png")
    image bush_right_central = get_image_7dl("gui/Bush/bush_right_central.png")
    image bush_right_top = get_image_7dl("gui/Bush/bush_right_top.png")
# заборы:
    image fence bricks = get_image_7dl("gui/fence_bricks.png")
    image fence bricks hole = get_image_7dl("gui/fence_bricks_hole.png")
#sounds
    $ May_There_Always_Be_Sunshine = "scenario_alt/Sound/music/May_There_Always_Be_Sunshine_minus.mp3" 
    