label alt_day6_uvao_mt_day_talk:
    scene bg ext_house_of_mt_day 
    "Подойдя наконец к своему жилищу, я зачем-то остановился на пороге в нерешительности."
    if alt_uvao_D6_sl_pickup:
        th "Всё-таки не хотелось бы наткнуться на Ольгу."
        if alt_uvao_D5_hentai:
            extend " Хамить ей вчера было совсем необязательно."
        else:
            extend " Не люблю я все эти лишние вопросы."
        th "С другой стороны, узнаю хотя бы, работают ли душевые."
        "Только по пути сюда я понял, что за шесть дней так и не сподобился нормально помыться: тело было отвратительно липким, на ногах кое-где была засохшая грязь после вчерашнего похода к Юле, а о жирных волосах даже вспоминать не стоило."
        if alt_uvao_true:
            "Только по пути сюда я понял, что за шесть дней так и не сподобился нормально помыться: тело было отвратительно липким, а о сальных волосах даже думать не хотелось."
            "Вроде бы, я и был на пляже перед самым обедом, но от купания остались одни воспоминания."
            th "Всё-таки, река плохая замена нормальному душу. Да и без мыла..."
        else:
            "Только по пути сюда я понял, что за шесть дней так и не сподобился нормально помыться: тело было отвратительно липким, на ногах кое-где была засохшая грязь после вчерашнего похода к Юле, а о жирных волосах даже вспоминать не стоило."
            th "За все дни даже в реке не искупался."
        th "Удивительно, что Славя на меня вообще внимание обращает."
        th "Голову я, конечно, помыть не успею, но лучше хоть что-то..."
        dreamgirl "А со всем остальным что делать будешь, чумазоид? Да и рубашка сама собой от травы и бункерной пыли не очистится."
        th "Что есть - то есть. Славю искать ради нового комплекта формы не буду."
    else:
        "С одной стороны, от Слави я до сих пор ничего, кроме добра, не видел, так что кляузничать на неё вожатой было как-то даже не по-человечески."
        dreamgirl "Ку-ку. Ты разве уже забыл, что она в столовой вытворяла?"
        th "Да нет, но..."
        dreamgirl "Никаких «но»! Сейчас она тебя соблазнять взялась, а что потом ей в голову ударит, можешь сказать?"
        dreamgirl "Мне мёртвый носитель не нужен."
        th "А вдруг она и в самом деле того... испытывает ко мне искренний интерес. Как к парню. {w}Я же полным идиотом буду тогда выглядеть."
        dreamgirl "Неподдельный, говоришь? Ты в зеркале-то давно себя видел?"
        "Наверное смотреть на меня со стороны сейчас было забавно: красный как рак, с озадаченным лицом и нервно бегающими глазами пионер в немного драных шортах и перепачканной травой рубашке."
        "На секунду я предствил себе эту картину, и последние сомнения отпали."
        th "Всё-таки Славе я не для дел амурных нужен."
        th "Лучше и правда расскажу всё Ольге - может быть, сама со Славей как-нибудь вопрос решит?"
    mt "Семён, хватит уже топтаться на пороге. Заходи!"
    "Донёсся изнутри голос Ольги, и мне ничего не оставалось, как наконец войти."
    window hide
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_mt_day
    show mt smile pioneer at cleft
    with dissolve
    "Вожатая сидела за столом и аккуратно записывала что-то в свой ежедневник."
    "На столе перед ней я заметил крохотный фарфоровый чайник с олимпийской символикой. Тут же рядом лежал и кипятильник."
    play music lazy_olga fadein 3
    mt "Явился, значит, Сём Сёмыч."
    th "\"Сём Сёмыч\"? Однако, это что-то новенькое."
    "Она вдруг улыбнулась мне мягко-мягко, будто старому доброму знакомому, с которым связаны какие-то далёкие и приятные воспонимания."
    if alt_day2_beach_done:
        dreamgirl "Значит, не только на пляже наша Ленивовна предаётся гедонизму. Гляди какая морда довольная."
    else:
        dreamgirl "Так вот как наша вожатка готовится к концерту. Как всегда, без продыха."
    "По комнате между тем разносился от чайника чуть уловимый аромат мяты."
    me "Не знал, что вы чай любите."
    mt "А хочешь со мной? В такую погоду глотнуть свежего зелёного чая с мятой - то что нужно."
    th "А с вожатой-то что не так?!"
    me "Ольга Дмитриевна... А почему вы меня не ругаете?"
    show mt surprise pioneer at cleft
    mt "А с чего бы это?"
    me "Ну... Я ведь на репетиции наверное должен быть, или к концерту помогать готовиться, или ещё что-нибудь полезное делать."
    show mt smile pioneer at cleft
    mt "И без тебя там вполне справятся. А пока время есть - садись давай."
    if alt_uvao_D6_sl_pickup:
        me "Я вообще-то только на минутку зашёл."
        if alt_day2_phys_done:
            me "Ольга Дмитриевна, а душевые работают?"
            show mt normal pioneer at cleft
            mt "Да, конечно. Вода, правда, только холодная, но это обычное дело, к сожалению."
        else:
            me "Ольга Дмитриевна, а где тут помыться можно?"
            show mt normal pioneer at cleft
            mt "В душевых около спортзала."
        mt "А ты что? Разве ещё ни разу не ходил?"
        me "Да вот как-то не довелось. А сейчас решил сбегать - всё-таки чистым быть приятнее."
        "Я не хотел в деталях рассказывать, с чего бы это мне вздумалось вдруг привести себя в порядок."
        show mt smile pioneer at cleft
        "Ольга улыбнулась."
        mt "Молодец, Сёмчик. Давно пора - мне на тебя такого грязнулю уже смотреть противно. Пионер ведь должен быть чист и опрятен."
        mt "У тебя все банные принадлежности есть?"
        me "Да... Наверное."
        "Я замялся и скромно потупил взгляд. Не говорить же ей, что я пользовался своим комплектом пару раз от силы."
        mt "Если что, в шкафу ещё есть."
        "Продолжение любезностей с раздобревшей не к месту вожатой не входило мои планы, и я решил плавно заканчивать этот разговор."
        me "А сколько у меня есть времени? Не хочу на концерт опоздать."
        show mt laugh pioneer at cleft
        "Ольга Дмитриевна лукаво посмотрела на меня, негромко хихикнула и совсем расплылась в улыбке." 
        "Похоже, сегодня я впервые видел не зануду-комендантшу вся лагеря, а самую обыкновенную и весьма приятную девушку, которая так до конца и не научилась быть серьёзной."
        mt "Ох, Семён Семёныч. Какой сознательный юноша ты, оказывается. И откуда что взялось?"
        show mt smile pioneer at cleft
        mt "Ну да ладно. У тебя ещё почти час. Так что давай не задерживайся."
        show mt smile pioneer at cleft
        mt "И на всякий случай я проверю, чтобы на концерте ты был вовремя."
        "Ольга хитро подмигнула мне, давая понять, что не верит до конца в моё духовное перерождение."
        me "Обязательно буду."
        "Свёрток с мылом и полотенцем по-прежнему лежал в глубине моей тумбочки, и, быстро достав его, я вышел на улицу."
        scene bg ext_house_of_mt_day
        "Я конечно рад был таким переменам в поведении вожатой, но упускать возможность побыть вместе со Славей совершенно не хотелось."
        th "Если я по-быстрому со всем управлюсь, то даже на репетицию к ней успею, пожалуй."
        #ЛБ: дальше, видимо, согласующая связка наподобие "Через каких-нибудь полчаса, буквально хрустящий от чистоты, я уже выходил на площадку перед сценой."
        jump alt_day6_uvao_concert_with_sl
    else:
        "Я не стал спорить с Ольгой и молча уселся напротив, прикидывая, с чего бы начать разговор."
        "Вожатая тем временем прикрыла свою тетрадь и убрала её в тумбочку."
        me "На самом деле, Ольга Дмитриевна, я с вами поговорить хотел."
        "Ольга между тем достала гранёный стакан и налила в него немного кипятка."
        mt "Ты рассказывай-рассказывай. А я пока чай тебе сделаю."
        me "Разговор вообще-то серьёзный..."
        "Я вдруг почувствовал, что мне стыдно выдавать мои догадки о поведении Слави."
        th "Может не надо? Это же подло как-то."
        th "А Славя пока ничего дурного мне и не сделала..."
        dreamgirl "Начинается... Надо, Сёма, надо!"
        "Поняв, что нужно хотя бы начать, я дал себе мысленного леща и выпалил:"
        me "Мне кажется, что со Славей что-то не так."
        mt "Заболела что ли?"
        me "Да нет... не знаю... {w}Но ведёт она себя очень странно."
#ЛБ: Семён сбивчиво, но честно излагает амурные факты, лишь из скромности избегая некоторых подробностей
        "Ольга, по ходу моего сбивчивого рассказа всё выше поднимавшая брови, вдруг улыбнулась."
        mt "Ох, Семён, извини, но вы такими смешными иногда бываете. Особенно - ребята."
        "Всё ещё улыбаясь, она покачала головой."
        mt "Чего ты так переполошился-то, скажи мне?"
        mt "Ну понравился ты девушке, случается такое."
        "Она негромко вздохнула."
        mt "Ещё как случается, ты уж поверь мне."
        mt "Ты парень видный - ещё какой видный, где уж бедной девушке устоять перед таким кавалером."
        "Ольга чуть усмехнулась."
        mt "Просто чуть поувереннее в себе надо быть, вот что я тебе скажу, Семён. {w=1.5}Поувереннее."
# Ещё немного просвещения среди подростков на подобные темы. Лучшая девушка лагеря - так что же такого! Интерес полов, последний день, девушка торопится открыть свои чувства...
# ГГ сидит, открыв рот, и пытается собрать мысли в кучку. Самая адекватная из них - что ОД не знает про его истинный возраст, вот и воспринимает вместе со всеми его откровениями соответственно - как несколько наивного мальчика. Пробует ещё раз произвести самооценку - "...да нет, чушь это всё! Видный, не видный... Кавалера нашла."
# ОД тем временем мягко и доходчиво объясняет, что Сэму самому надо решать, что с этим делать - нравится ли ему Славя или нет, хочет ли он развития отношений с этой славной девушкой. И разумеется, она, ОД, ничего такого ему не говорила, здесь пионерский лагерь всё-таки! Облико морале, ферштеен?!
# Если ГГ палевный - ОД срывается с Педагогического Ритма и не удерживается от ехидного замечания, что уж всяко Славя лучше, чем "эта кошка".
# ГГ окончательно осознаёт бесперспективность дальнейшего разговора с ОД, благодарит за науку и откланивается, чтобы идти раскалывать Славю самостоятельно.
        
        
#
#
#
#        
        me "По-моему, она мне что-то плохое сделать хочет."
        show mt serious pioneer at cleft
        "Ольга переменилась в лице, нахмурилась и внимательно посмотрела на меня."
        "Домашнее настроение вожатой в миг растворилось и по её взгляду я понял, что если сейчас не приведу веских доводов, то одному Семёну здорово не поздоровится."
        mt "Персунов. «Что-то не так» - это с тобой."
        mt "И что тебе на сей раз причудилось?"
        me "Всё началось вчера вечером..."
        me "Я встретил Славю на пляже, а она плакала... и ещё про лагерь спрашивала."
        mt "Она по твоему не человек, что ли? Или ты думаешь, что она и не девочка вовсе?"
        "Вожатая ехидно усмехнулась. Трудно было ожидать от неё иной реакции на неприятный разговор о лучшем пионере её отряда."
        me "Это далеко не всё."
        mt "Ну давай. Послушаю сколько ещё ерунды ты напридумывал."
        "Я не стал обращать внимание на этот желчный комментарий и продолжил:"
        if alt_uvao_true:
            me "Сегодня на пляже она мне как-то странно намекала на купание в неглиже."
        me "А только что в столовой пыталась меня соблазнить! Даже предложила заняться кое-чем {i}интересным{/i} после танцев."
        me "Вас это не удивляет, Ольга Дмитриевна?"
        if alt_uvao_true:
            extend " Это вы к такому будущие кадры готовите? Ассимилировать, так сказать, попаданца {i}посильнее{/i}, чтоб не убёг случаем?"
        else:
            extend " Или это ваше задание такое? Приобщить меня, так сказать, к культурно-массовым любыми средствами?"
        show mt angry pioneer at cleft
        mt "Подерзи мне тут! Ты вообще соображаешь, что несёшь?!"
        if not alt_uvao_true:
            mt "И зачем я тебя вообще слушать стала."
            mt "Славя - честь и гордость нашего лагеря. А ты тут на неё поклёп наводишь - так не поступают товарищи."
            show mt serious pioneer at cleft
            "Постепенно вожатая успокаивалась, хотя и продолжала часто и глубоко дышать."
            me "Но ведь это правда..."
            mt "Славя - порядочная девушка и не позволит никогда себе такого. А ты, Сём Сёмыч, наверное, всё не так понял и сочинил глупостей с три короба."
            me "Тогда зачем ей куда-то приглашать меня вечером?"
            show mt normal pioneer at cleft
            "Наконец Ольга замялась. Всё-таки мне удалось найти правильный вопрос, пробивший брешь в железобетонном постулате о непогрешимости нашей активисточки."
            mt "Я... Я не знаю."
            show mt serious pioneer at cleft
            mt "Но это не повод верить тебе, пока не будет каких-то настоящих доказательств."
        else:
            mt "Никаких {i}посильнее{/i}. Она вообще всего лишь стажёр, которому доверяют только наблюдение."
            show mt serious pioneer at cleft
            mt "Хотя я тебе этого и не должна была говорить."
            show mt normal pioneer at cleft
            "Вожатая довольно быстро успокоилась и продолжила спокойным и заинтересованным тоном:"
            mt "Ты, наверное, не так понял что-то. Ты же понимаешь серьёзность своих обвинений?"
            me "Конечно, понимаю. Но намёки были предельно однозначными, Ольга Дмитриевна. Я не знаю, что ей там чудится, но рядом с ней я не могу чувствовать себя в безопасности."
            "Вожатая ещё раз молчаливо оглядела меня и тяжело вздохнула:"
            mt "Ну не могу я тебе так поверить, понимаешь? Не{w=0.2} мо-{w=0.2}гу."
            mt "У Слави такая замечательная характеристика, и я к ней привязалась... Мне нужны серьёзные доказательства."
            mt "Если хочешь поговори со Славей, но меня не приплетай к этим разборкам, пока не будешь уверен полностью."
        me "Не сомневайтесь, Ольга Дмитриевна. Я обязательно докажу что прав."
        th "Мне бы самому, правда, толику этой уверенности..."
        mt "А сейчас вон с глаз моих. Утомил ты меня."
        "Залпом выпив уже остывший чай, я наскоро вышел из домика."
        #sfx хлопания дверью
        scene bg ext_house_of_mt_day 
        th "Как бы то ни было, а серьёзный разговор со Славей уже назрел."
        "Решив не откладывать столь серьёзное мероприятие, я направился в сторону эстрады."
        jump alt_day6_uvao_prufung_sl
        #Далее мы его сразу телепортнем на подготовку к концерту и заставим вытягивать клешнями "истинные мотивы" (с) Слави.
