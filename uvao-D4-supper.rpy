﻿#День4 Ужин"
#
label uvao_uvao_D4_supper:
# Д4-Ужин
#
# используется флаг посещения медпункта alt_day4_uv_viola_morning
# устанавливает флаг ужина с Виолой uvao_D4_supper_cs
#

    $ uvao_D4_supper_cs = False
    $ alt_chapter(4, u"Юля. Ужин")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    window hide
    scene bg int_dining_hall_people_sunset
    with dissolve
    play ambience ambience_dining_hall_full
    window show
    "Войдя в столовую я огляделся."
    if alt_day4_uv_viola_morning:
# Утром были у Виолы, можем поужинать вместе
        "Свободных мест практически не было. Впрочем, за одним из столиков их было сразу три."
        "Четвёртое занимала Виолетта."
        th "Похоже, не меня одного её общество смущает…"
        "Впрочем, поговорить с ней было надо, так что совместить беседу с Виолой и ужин показалось мне хорошей идеей."
        menu:
            "Подсесть к Виолетте":
                th "По крайней мере, лучше поговорить с ней здесь, чем наедине в медпункте."
                show cs normal with dissolve
                me "Виола? Можно к вам присоединиться?"
                dreamgirl "Неплохой заход. Ужин, потом пара коктейлей - и она вся твоя!"
                "Она неторопливо оглядела меня с ног до головы."
#                $ renpy.music.set_volume(0.7, delay=2, channel='music')
                play music music_list["eternal_longing"] fadein 3
                show cs smile with dspr
                cs "Конечно, {i}пионер{/i}, присаживайся. Я никогда не против интересной компании за ужином."
                "Как обычно, в этой фразе уместился целый ворох двусмысленностей, но отступать было поздно, и я уселся напротив неё."
                show cs normal close with dissolve
                me "Эээ… На самом деле я хотел поговорить, по поводу вашего {i}утреннего приглашения{/i}."
                dreamgirl "Ты что, собрался переиграть её на её же поле?! Без шансов, чувак, без шансов…"
                "Виола понимающе усмехнулась."
                show cs shy close with dspr
                cs "Само собой, приглашение всегда в силе, в {i}любое{/i} время дня и ночи. Только предупреди заранее, чтобы я могла подготовить все {i}необходимое{/i}."
                "Да, кажется, этот противник мне не по зубам."
                show cs smile close with dissolve
                me "Виола, я про местную легенду, девочку-кошку.{w} Я её видел сегодня. И даже парой слов перекинулся."
                $ renpy.music.set_volume(0.3, delay=3, channel='music')
                show cs normal close with dspr
                "Виола поставила стакан с компотом. Никакой томности во взгляде уже не наблюдалось."
                cs "Видел? Где?"
                me "Да возле домика. Услышал треск за окном, думал, опять Ульянка жуками забрасывать собирается, высунулся. А там она."
                "Виола помолчала, о чём-то размышляя."
                cs "И о чём вы беседовали, если не секрет?"
                me "Да ни о чём практически. Сказала, что я неуклюжий. Ещё что раньше меня видела."
                cs "Интересно. Она не представилась?"
                me "Представилась. Говорит, что раньше её Юлей звали.{w} Мне с вами идти, да?"
                cs "Зачем?"
                me "Ну, как… Аминазину покушать, или что там у вас…"
                show cs smile close with dspr
                cs "Успокойся, всё с тобой нормально. Неплохо держишься для четвёртого дня в новом мире."
                th "Она знает?! Откуда?"
                me "Что?"
                show cs normal close with dspr
                cs "Что слышал. Не ты первый, пионер."
                me "А… Вы тоже?…"
                cs "Я? Нет, конечно. Я из команды исследователей."
                th "О чёрт. Парень, ты, кажется, серьёзно влип. Сейчас тебя в такое место потащат, что дурдом раем покажется."
                "Виола, кажется, поняла, почему я вдруг побледнел."
                show cs smile close with dspr
                cs "Успокойся, Семён. Никто тебя на ремни резать не собирается.{w} Изучаем мы точки проколов между реальностями, а не тех, кто сквозь них приходит."
                cs "Смысл тебя потрошить? Такой же человек, как и все. Ну, жил на двадцать пять лет в будущем, подумаешь."
                th "Уф-ф-ф! Отлегло. Может, и вывернуться получится."
                "Я сложил немногие известные мне факты в кучку."
                me "Я правильно понял, что моё появление здесь и эта… Юля как-то взаимосвязаны?"
                show cs normal close with dspr
                cs "Догадливый.{w} Насколько я могу судить, то, что представилось тебе Юлей, одно из проявлений точки прокола. Визуализация,{w} можно сказать."
                cs "Вы ведь с ней договорились где-то встретится, правильно?"
                me "Ну… Да. После ужина на стоянке."
                cs "У тебя ведь есть фотокамера в {i}смарт-фоне{/i}?"
                "Последнее слово она выговорила как-то непривычно."
                me "Откуда вы?… А, ну да. Есть, конечно."
                cs "Попробуй её сфотографировать, и многие вопросы сразу отпадут."
                me "Лад… Подождите, так мне что, к ней идти?"
                cs "А почему нет? Думаю, для {i}тебя{/i} она должна быть безопасна, если специально злить не будешь."
                $ renpy.music.set_volume(0.6, delay=3, channel='music')
                show cs smile close with dspr
                cs "Только хочу сразу предупредить насчёт {i}чересчур{/i} близких контактов — тут тебе и изделие №2 не поможет."
                "Я снова покраснел."
                me "Да я и не думал даже!"
                show cs smile close with dspr
                cs "Ну-ну. Смотри, тут ты не котятами обзавестись рискуешь. Понимаешь меня, {i}пионер{/i}?"
                me "Угу."
                show cs normal close with dspr
                stop music fadeout 9
                cs "Вот и хорошо. Она что-нибудь еще говорила? Не просила чего-нибудь принести?"
                me "Просила. Булку просила. Мышей, говорит, сложно ловить, а булки ещё и вкуснее."
                cs "Ну так бери и иди. И постарайся побольше с ней говорить, всё-таки случай… Редкий, скажем так."
                cs "Если получится к ней в гости напроситься — совсем хорошо. Ольгу я предупрежу, чтобы не искала тебя."
                me "Ольгу Дмитриевну? Она тоже с вами?"
                cs "Да, отвечает за адаптацию.{w} Иди на своё свидание, пионер, не заставляй аномалию ждать. Потом мне все доложишь."
                me "А… Виола, а я вообще где?"
                show cs smile close with dissolve
                cs "Долгий разговор. Да и не в столовой же об этом беседовать?"
                "Покорно кивнув, я сунул в карман сдобную булку с изюмом и встал из-за стола."
                hide cs
                $ renpy.music.set_volume(1, delay=0, channel='music')
                th "Всё равно, ещё немного разговоров в том же духе - и стены столовой придётся отмывать от моих мозгов."
                "Мне явно следовало взять паузу и привести содержимое головы в порядок."
                $ uvao_D4_supper_cs = True
                jump uvao_D4_supper_end
            "Сесть одному":
#                "Очень СТРАШНО!"
                th "А с другой стороны, рассказывать-то пока особенно и нечего."
                th "Вот поговорю после ужина с этой Юлей ещё раз…"
                dreamgirl "Ой, да ладно! Признайся хотя бы самому себе, ты попросту боишься, что тебя съедят.{w} АМ!"
                th "О! Как раз место свободное есть."
                "Проигнорировав насмешки Шизы, я забился в угол и принялся спешно поглощать еду."
    else:
# Утром не ходили к Виоле
        "Как и за обедом, в столовой было неожиданно много свободных мест."
        "Здраво рассудив, что поддерживать с кем-то беседу всё равно сейчас не в состоянии, я забился в угол и принялся спешно поглощать еду."
# Ужинаем в одиночестве.
    dreamgirl "Эй! Ты булочку-то не сожри, проглот!"
    dreamgirl "И вообще, мало ли, какой случай может приключиться."
    th "И правда… Случаи-то, они разные бывают."
    "На всякий случай, я сунул полагающуюся мне булочку с изюмом в карман."
    "На месте мне не сиделось, очень уж хотелось поскорее убедится, что неожиданное знакомство перед ужином - не плод моего воспалённого воображения."
    "Или, как минимум, в том, что мои галлюцинации достаточно устойчивы."
    "Наконец я решительно отложил вилку и вскочил из-за стола."
label uvao_D4_supper_end:
    th "А нюх-то у хвостатой что надо - действительно, булочки свежие, сегодняшние."
    "Неожиданно для самого себя ухмыльнувшись этой мысли и избавившись от подноса с недоеденным ужином, я вышел из столовой."
    stop ambience fadeout 3
    window hide

    jump uvao_D4_meet_Yulia_at_evening

