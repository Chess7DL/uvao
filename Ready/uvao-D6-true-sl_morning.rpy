# Д6 - завтрак со Славей
#
# Используется флаг встречи со Славей на пляже в Д5 alt_uvao_D5_evening_sl
# Используется флаг обеда со Славей в Д4 alt_uvao_D4_lunch_sl
# Используется индикатор степени настойчивости Слави alt_uvao_D6_sl_assert
#
label alt_day6_true_sl_morning:
    window hide
    play music music_list["get_to_know_me_better"] fadein 3
    scene bg ext_washstand2_day with fade
    play sound sfx_open_water_sink
    $ renpy.pause(1)
    play sound_loop sfx_water_sink_stream
    window show
    "От умывания привычно уже ледяной водой в голове немного прояснилось, и я начал хоть что-то соображать."
    "В частности, обнаружил, что полотенце я с собой не захватил."
    play sound sfx_close_water_sink
    stop sound_loop
    "Утёршись кое-как ладонью, я потряс головой, выгоняя из неё остатки сонного тумана, и принялся соображать, что делать дальше."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_washstand_day with fade
    window show
    "С одной стороны, время уже приближалось чуть ли не к полудню, а Виола велела зайти к ней в медпункт прямо с утра, так что чем позже я приду, тем тем сильнее она рассердится - если вообще станет меня дожидаться."
    "С другой стороны, есть хотелось страшно.{w} Даже нет, не есть - {b}жрать{/b}."
    th "Хотя вряд ли мне сейчас светит что-нибудь в столовой. То самое время, когда время завтрака давно уже миновало, а обед ещё и не думал начинаться…"
    dreamgirl "Вообще-то у Виолы вполне может найтись что-нибудь съестное. Она женщина самостоятельная, в медпункте проводит много времени - не может быть, чтобы у неё хотя бы чаем разжиться нельзя было."
    dreamgirl "А где есть чай, там и к чаю наверняка что-нибудь найдётся."
    "Идея показалась мне вполне резонной, и я потопал к медпункту."
    "Впрочем, вскоре выяснилось, что проснулся я явно не до конца и умудрился пропустить поворот к медпункту."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_square_day with fade
    window show
    "Спохватился я только когда передо мной замаячила спина Генды."
    "Чертыхнувшись, я развернулся было в обратную сторону, как вдруг меня окликнул знакомый голос:"
    sl "Семён! Семён!"
    show sl normal pioneer far at left with dissolve
    "Подбежав ко мне, Славя выпалила:"
    show sl smile pioneer at cleft with dissolve
    sl "Доброе утро, Семён!"
    me "Доброе утро…"
    show sl normal pioneer with dissolve
    "Кажется, приветствие получилось не слишком любезным, так что я поспешил улыбнуться и добавил:"
    me "Рад тебя видеть!"
    show sl happy pioneer with dspr
    if alt_uvao_D6_sl_assert = 1:
        "Славя радостно заулыбалась в ответ."
    elif alt_uvao_D6_sl_assert = 2:
        "Славя буквально расцвела от радости."
    else
        "Простая светская любезность произвела на Славю прямо-таки волшебное действие - она буквально расцвела от радости, только что в ладоши не захлопала."
        th "Что это с ней? Можно подумать, мы год не виделись. Вчера она меня гораздо спокойнее приветствовала."
    if alt_uvao_D5_evening_sl:
        th "Впрочем, вчера вечером она тоже какая-то странная была."
    sl "Я тоже очень рада тебя видеть!"
    show sl smile pioneer with dspr
    sl "Семён, а где ты был-то всё утро? Тебя и на зарядке не было, и на линейке, и на завтраке!"
    me "Да я…"
    "Я замялся, не зная, признаваться ли мне в том, что я проспал, или соврать что-нибудь правдоподобное, но Славя не стала дожидаться ответа."
    sl "Ой, так ты же голодный, наверное, раз на завтраке не был?"
    show sl smile2 pioneer with dspr
    me "Ну, да, если честно."
    show sl laugh pioneer with dspr
    sl "Так пойдём, я тебя покормлю!"
    if alt_uvao_D6_sl_assert < 3:
        "Схватив за руку, она потащила меня за собой в сторону столовой."
    else
        "Одарив ещё одной улыбкой, она схватила меня за руку и потащила за собой в сторону столовой."
    hide sl with dissolve
    "С трудом поспевая за девочкой, я подумал:"
    th "Кажется, не судьба мне сегодня позавтракать с Виолой. Впрочем, лучше синица в руке, чем журавль в небе.{w} Тем более, в исполнении Слави синица наверняка окажется размером с курицу, не меньше."
    if alt_uvao_D5_evening_sl:
        th "Заодно попробую узнать, что происходит с нашей активисткой. То она на пляже плачет, то при виде меня от радости прыгает. Странно всё это."
        dreamgirl "Ты только смотри, осторожнее! Вдруг она психическая!"
        th "Ну конечно! Мне, как человеку с собственной карманной шизой, это очень-очень страшно."
        "Голос самодовольно хмыкнул, но тем и ограничился."
    window hide
    scene bg int_dining_hall_day with fade
    play ambience ambience_dining_hall_empty fadein 4
    window show
    # "Испытывая лёгкое ощущение дежавю, я, как и в самый первый свой день здесь, уселся за столик возле раздачи, а Славя ушла на кухню." #ЛБ: Увы, это теперь в прошлом
    "В столовой Славя усадила меня за столик возле раздачи, а сама ушла на кухню."
    "Не было её довольно долго. Я уже начал сомневаться, не лучше ли было мне пойти всё-таки сразу медпункт, но тут она появилась, нагруженная подносом и солидных размеров общепитовским чайником."
    show sl serious pioneer far at right with dissolve
    "Судя по её недовольному раскрасневшемуся лицу, еду пришлось добывать с боем, но, подойдя к столику, Славя вновь разулыбалась."
    show sl smile pioneer at cright with dissolve
    "Я помог поставить поднос на стол, за ним последовал чайник."
    show sl smile pioneer close at center with dissolve
    "Славя уселась напротив, а я произвёл краткую ревизию добычи. Хлеб, масло, остывший перестоявшийся чай и, почему-то, изрядных размеров кусок варёной говядины."
    "Поймав мой недоумённый взгляд, Славя пояснила:"
    sl "Это мясо предназначалось для супа. Ну, осталось немножко. Будешь есть?"
    me "Буду!"
    if alt_uvao_D6_sl_assert < 3:
        "Несколько минут я был совершенно некоммуникабелен. Оценив весь размах моего сражения с пищей, Славя не стала отвлекать меня разговорами, а с улыбкой наблюдала, как я ем."
    else:
        "Несколько минут я был совершенно некоммуникабелен. Оценив весь размах моего сражения с пищей, Славя не стала отвлекать меня разговорами, а молча наблюдала как я ем, прямо-таки лучась от счастья."
    "Ожесточённо пережёвывая жилистое мясо, я подумал, что всё это похоже на мой поздний ужин в первый день."
    "Вернее, было бы похоже, если бы не одно \"но\". Кое-что явно изменилось. Вернее, {i}кое-кто{/i} - Славя."
    "За эти дни я привык воспринимать её как свою ровесницу. Точнее, как ровесницу своего нынешнего {i}меня{/i}."
    "Пожалуй, даже младше. Эдакая деятельная непосредственная девочка - ураган."
    "Сегодня она была такой же деятельной и непосредственной, но проскальзывало сейчас в её взгляде что-то неожиданно взрослое - я только не мог понять, что."
    "Да и вообще…"
    if alt_uvao_D5_evening_sl:
        extend " Вчерашняя сцена на пляже вдруг вспомнилась во всех подробностях. Ну никак поведение Слави не увязывалось у меня в голове со ставшим привычным уже образом активисточки."
        th "То, что она плакала, неудивительно, в общем-то. В конце концов, она тоже живой человек, проблемы у всех бывают, отчего бы и не поплакать девочке."
        th "Но эти странные разговоры про мечты, которые можно здесь исполнить и всё такое… Это вот очень и очень странно. " # здесь пробел не лишний
    elif alt_uvao_D6_sl_assert > 1:
        extend "Она, конечно, всегда была приветлива, всегда готова прийти на помощь, но сегодня её забота почему-то носит строго направленный характер. Необычно это."
    else:
        extend "Может быть, я только сегодня понял, что она и вправду в чём-то страше своих товарищей. Не годами, нет."
    "Дожевав и проглотив очередной кусок, я почувствовал, что голод начал отступать, и тут вспомнил наконец о правилах приличия:"
    me "Ох, Славя, я даже не знаю, как тебя благодарить! Ты меня уже второй раз от голодной смерти спасаешь!"
    show sl laugh pioneer close with dspr
    sl "Ай, да ладно тебе! Тебя не покормишь, так и будешь ходить голодным!"
    show sl smile pioneer close with dspr
    sl "Кто-то же должен о тебе позаботиться!"
    if alt_uvao_D5_evening_sl:
        "Снова вспомнился вчерашний разговор на пляже. Проглотив очередной кусок, я осторожно поинтересовался:"
        me "Кстати, о заботе… Славя, скажи, а я {i}тебе{/i} точно ничем помочь не могу?"
        show sl surprise pioneer close with dspr
        "Лицо её вдруг дрогнуло, и на нём появилось какое-то сложное выражение" # здесь знака препинания нет!
        show sl smile pioneer close with dspr
        if alt_uvao_D6_sl_assert = 3
            extend ", которое, впрочем, тут же вновь сменилось на радостную улыбку."
        else:
            extend ", которое, впрочем, вновь сменилось привычной улыбкой раньше, чем я успел что-то понять."
        "Чувствуя себя полным дураком, я заторопился:"
        me "Я имею в виду, ты вчера такая грустная была вечером, вот я и подумал…"
        show sl normal pioneer close with dspr
        "Что именно \"подумал\" я сам толком не знал, поэтому замолчал."
        "Славя поколебалась немного, а потом сказала немного смущённо:"
        show sl shy pioneer close with dspr
    else:
        sl "Одним словом, ерунда это всё."
        "Она помолчала секунду и продолжила, слегка понизив голос:"
        show sl normal pioneer close with dspr
# TODO: Спрайты
        sl "Странное место этот лагерь, правда ведь?"
        "Я замер с недожёванным куском мяса во рту."
        th "Да не то слово!"
        me "Странное? О чем ты?"
        sl "Здесь кажется, будто возможно всё.{w} Будто бы тут можно исполнить любую мечту - или, по крайней мере, сделать первый шаг к ней…{w} Так ведь?"
        "Вопрос застал меня врасплох. Впрочем, с момента появления здесь я и впрямь чувствовал себя так, будто получил второй шанс."
        me "Ну… наверное. Да."
        #ЛБ: про конец смены ГГ узнает позже у ВЦ в медпункте, про год теперь знает ещё с Д1
        me "А почему ты об этом…"
    sl "Знаешь, это долгий разговор…"
    show sl smile pioneer close with dspr
    sl "Давай лучше пообедаем сегодня вместе, а там видно будет!"
    show sl laugh pioneer with dissolve
    "Рассмеявшись как ни в чём ни бывало, она вскочила из-за стола " # здесь пробел не лишний!
    hide sl with dissolve
    extend "и, махнув мне на прощание рукой, убежала из столовой."
    "Озадаченно почесав в затылке, я с удвоенными силами принялся уничтожать остатки позднего завтрака."
    th "Если я сейчас не поспешу, Виола меня самого съест и не подавится!"
    jump alt_day6_true_CS_talk_short
