# Д5-вечер
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines (Видели Шурика в шахтах/не обедали/спалились на стоянке)
# Используется флаг alt_uvao_D4_concert (Попали на концерт в Д4. Инверсия используется как признак обеда в одиночестве)
# Используется флаг alt_uvao_D5_hentai (крыли кошочку)
#
label alt_day5_uvao_evening:
    $ routetag = "uv"
    $ alt_chapter(5, u"Юля. Вечер")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    window hide
    scene bg int_dining_hall_people_sunset
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    window show
    if (alt_uvao_D5_sh_mines):
        jump alt_day5_uvao_spoiled_supper
    else:
        "Впрочем, идти было очень недалеко, так что в столовую я, впервые за пять дней, попал одним из первых."
        "Получив свою порцию гречневой каши с чем-то, смутно напоминающим гуляш, и стакан неизбежного компота, я замер было в нерешительности с подносом в руках…"
        if (not alt_uvao_true):
            #не-тру охотник
            #(//Про Юлю всё ещё никто не знает)
            "Но потом решительно направился к пустующему пока что столику в углу."
            "Я с облегчением поставил поднос - руки всё ещё здорово ныли после переноски очкарика - и уселся за стол."
            if (not alt_uvao_D4_concert):
                #Д4-обед прошёл в одиночестве
                extend " Кажется, именно здесь я вчера и обедал."
                th "А кстати, вчерашний обед очень даже спокойно прошёл! Надо воспользоваться отработанной техникой."
                "Я снова пристроил на лицо зверскую гримасу серийного убийцы."
            th "В конце концов, я сегодня не только не пообедал толком, так ещё и полдник пропустил за всей этой беготнёй!{w} Непорядок, однако! Так и похудеть можно."
            dreamgirl "Можно подумать, последние несколько лет у тебя было исключительно пятиразовое питание ресторанного уровня, а здесь наоборот, голодом морить начали…"
            "Проигнорировав надменное фырканье Шизы, я перемешал содержимое тарелки в однородную массу и принялся за ужин."
            play music music_list["my_daily_life"] fadein 4
            "Не знаю, еда ли оказалась на вкус лучше, чем на вид, или причиной были физические упражнения на свежем воздухе, но я успел слопать ужин прежде, чем понял, что именно ем.{w} Впрочем, может оно и к лучшему. Главное - желудок наполнился и не слал больше в мозг ультиматумов."
            "Сыто поковырявшись в зубах, я лениво поднялся и не спеша пошёл к выходу."
            stop ambience fadeout 1
        else:
            #тру-ветка
            "Но потом решительно направился к ставшему уже привычному за последние два дня столику, за которым обычно кормилась Виола."
            dreamgirl "Ты в столовую уже как на работу в офис начинаешь ходить.{w} Вернее, как в штаб-квартиру какой-нибудь {i}конторы{/i} из дешёвого триллера."
            dreamgirl "Пришёл, доложился начальству, получил задание - поскакал выполнять."
            th "Знаешь, как учат те же триллеры, пока наше сотрудничество является взаимовыгодным - не стоит от него отказываться."
            "Я с облегчением поставил поднос - руки всё ещё здорово ныли после переноски очкарика - и уселся за стол."
            dreamgirl "Взаимовыгодным? Ну интерес медсестры, или кто там она на самом деле, мне вполне ясен - ты для неё бесплатный полевой агент и объект для троллинга в одном лице."
            dreamgirl "Твой-то интерес здесь какой? Что-то я не вполне улавливаю!"
            th "Информация.{w} Я надеюсь, что она либо сама ей будет делиться, либо проболтается о чём-нибудь случайно."
            th "Кстати, даже если отбросить невнятные объяснения про параллельные миры, её подсказка сфотографировать Юлю была очень даже ничего."
            "Пользуясь тем, что мой внутренний оппонент промедлил с ответом, я взялся наконец за вилку."
            th "В конце концов, я сегодня не только не пообедал толком, так ещё и полдник пропустил за всей этой беготнёй!{w} Непорядок, однако! Так и похудеть можно."
            dreamgirl "Можно подумать, последние несколько лет у тебя было исключительно пятиразовое питание ресторанного уровня, а здесь наоборот, голодом морить начали…"
            "Проигнорировав ехидное фырканье Шизы, я перемешал содержимое тарелки в однородную массу и принялся за ужин."
            play music music_list["my_daily_life"] fadein 4
            "Не знаю, еда ли оказалась на вкус лучше, чем на вид, или причиной были физические упражнения на свежем воздухе, но когда через пару минут напротив уселась Виолетта, моя порция успела уменьшиться как минимум наполовину."
            show cs normal2 close with dissolve
            "Сделав, подобно Портосу, над собой героическое усилие, я разом проглотил всё, что было у меня во рту."
            me "Приятного аппетита, Виолетта Церновна!"
            show cs smile2 close with dspr
            cs "Спасибо, пионер, спасибо…{w} Ну а у тебя, как я вижу, с аппетитом и так всё в порядке."
            "Слегка смутившись, я наконец взял себя в руки и начал всё-таки пережёвывать пищу перед тем как проглотить. Надеюсь, общество оценит мою помощь!"
            show cs normal2 close with dspr
            cs "Итак?"
            "Коротко бросила Виола, принимаясь за ужин. Мысленно вздохнув, я положил вилку и начал вполголоса:"
            me "Да не о чем особенно рассказывать-то. Не успели дойти до староко корпуса, как на нас откуда-то из кустов выскочил этот… Гм… Шурик."
            me "Весь грязный и ободранный, вопил что-то дикое, размахивал железками."
            me "В общем, мы с Сыроежкиным его скрутили, а потом Ольга… э-э… довольно быстро привела Шурика в чувство."
            me "Но она же Вам рассказывала, наверное?"
            show cs smile2 close with dspr
            "Виолетта неопределённо повела бровями. Я предпочёл считать это за знак согласия и продолжил:"
            me "Ну а потом мы его сразу в медпункт потащили, сам идти он не мог."
            "Я немного подумал и закончил решительно."
            show cs normal2 close with dspr
            me "Юля нам на глаза не попадалась, никаких признаков её присутствия замечено не было. Шурик о контактах с ней тоже не упоминал."
            me "Потерь среди личного состава нет, у меня всё."
            "Здесь я позволил себе улыбнуться, но Виолетта моего веселья не разделила."
            show cs normal close with dissolve
            cs "Зря смеёшься, Семён. Очень хорошо, что потерь нет."
            "Видимо, на моём лице что-то такое отразилось, потому что она поспешила добавить:"
            show cs smile2 close with dissolve
            cs "Ой, да не волнуйся ты так. Если бы у меня действительно были опасения насчёт вашей безопасности, никуда бы вы не пошли."
            cs "Во всяком случае, я была вполне уверена, что {i}в твоём присутствии{/i} всё пройдёт нормально, даже если вы столкнётесь с визуализацией. Пардон, с Юлей."
            show cs normal2 close with dissolve
            cs "Кстати, ты сказал, что Шурик кричал что-то. Не помнишь, что именно? Может быть, потом рассказывал что-нибудь?"
            me "Ну… Кажется, сначала он кричал про голоса в голове и что мы не люди. Я как-то больше беспокоился, чтобы он кого-нибудь не укокошил ненароком."
            me "А потом, когда очнулся, он вообще не помнил как туда попал."
            "Медсестра вздохнула:"
            cs "Жаль. Есть у меня некоторые подозрения насчёт того, что с ним могло произойти, но пока что ничем не обоснованные, к сожалению.{w} Что же, делать нечего, подождём до завтра - может и вспомнит что-нибудь."
            "Виола задумалась, покачивая машинально рукой, как и вчера, стакан из-под компота. Тут я обнаружил, что она между делом уже успела как-то незаметно для меня съесть свой ужин и заторопился, навёрстывая упущенное."
            th "А Виола сейчас не слишком-то похожа на какую-то там медсестру из провинциального пионерлагеря - слишком уж интеллектуальное у неё выражение лица."
            dreamgirl "Ага, и про шуточки свои совсем позабыла. Даже неинтересно!"
            "Виолетта тем временем завершила свои размышления и снова обратила на меня внимание:"
            cs "Ладно, шёл бы ты, Семён, отдыхать. Завтра об остальном поговорим."
            "И, словно подслушав Шизу, продолжила с ехидной ухмылкой:"
            show cs smile2 close with dspr
            cs "И знаешь, заходи-ка ты завтра с утра ко мне в медпункт."
            "Голос её словно стал ниже на целую октаву, а от появившейся в нём бархатистой хрипотцы у меня мурашки побежали по спине."
            "Она заговощически наклонилась ко мне и продолжила жарким шёпотом:"
            show cs badgirl2 close with dissolve:
#                xalign 0.5 yalign 0.4 zoom 1.3
                xalign 0.5 yalign 0.5 zoom 1.0
                linear 2.0 xalign 0.5 yalign 0.1 zoom 1.3
            cs "В столовой толком не поговоришь - только и ждёшь, что подслушает кто-нибудь.{w} Да и реноме надо поддерживать."
            show cs badgirl2 close with dissolve:
#                xalign 0.5 yalign 0.4 zoom 1.3
                linear 1.5 xalign 0.5 yalign 0.5 zoom 1.0
            "Отстранившись, она неспеша оправила воротник своего белого халата. Пальцы коснулись верхней пуговицы, на мгновенье задержавшись…"
            show cs smile2 with dissolve2
            stop music fadeout 3
            "Поднявшись из-за стола, она томно подмигнула мне, взяла свой поднос и, слегка качнув бёдрами, уплыла к окошку посудомойки."
            hide cs with dissolve2
            stop ambience fadeout 4
            dreamgirl "Да-а… Был неправ. Вспылил. Но теперь считаю свою критику безобразной ошибкой.{w} Кстати, слюни подбери."
            "Я вернулся к реальности. Кажется, половина столовой перестала есть, замерев на месте."
            play ambience ambience_dining_hall_full fadein 4
            play music music_list["my_daily_life"] fadein 4
            "Впрочем, самое большее через минуту всё вернулось на круги своя - ужинающие занялись едой и обычными разговорами, а я наконец смог подняться из-за стола, не шокируя окружающих внешним видом."
            th "И ей это с рук сходит? Похоже, она действительно не последний человек в лагере."
            show dv scared pioneer far at right with dissolve
            "Тут я встретился глазами с Алисой. Та смотрела на меня с неприкрытым ужасом."
            th "Да в самом деле, какого чёрта!"
#            "Наверное, лучше всего было бы сейчас развернуть плечи, выставить грудь колесом и прошествовать мимо с ухмылкой прожжёного донжуана…"
            dreamgirl "А вот теперь самое время позаботиться и о собственном реноме. Плечи расправить, грудь колесом, на лицо ухмылку прожжёного донжуана, и не спеша иди мимо…"
            "…Вздохнув, я смущённо пожал плечами и, ссутулившись, поплёлся относить грязную посуду."
            hide dv with dissolve
            stop ambience fadeout 1
label alt_day5_uvao_evening_dining_hall_exit:
    stop ambience fadeout 3
    window hide
    $ renpy.pause(1)
    scene bg ext_dining_hall_near_sunset with fade
    play ambience ambience_camp_center_evening fadein 3
    play sound sfx_close_door_1
    play sound_loop ambience_medium_crowd_outdoors fadein 2
#
    "До отбоя оставалась ещё уйма времени, следовало решить, куда идти дальше."
#
# Безнадёжная карта
#
    $ disable_all_zones()
    $ disable_all_chibi()
    $ set_zone('music_club', 'alt_day5_uvao_evening_map_strange')
    $ set_zone('clubs', 'alt_day5_uvao_evening_map_strange')
    $ set_zone('camp_entrance', 'alt_day5_uvao_evening_map_strange')
    $ set_zone('sport_area', 'alt_day5_uvao_evening_map_strange')
    $ set_zone('library', 'alt_day5_uvao_evening_map_strange')
    $ set_zone('medic_house', 'alt_day5_uvao_evening_map_strange')
    $ set_zone('square', 'alt_day5_uvao_evening_dv_un')
    $ set_zone('beach', 'alt_day5_uvao_evening_map_peaceful')
    $ set_zone('boat_station', 'alt_day5_uvao_evening_map_peaceful')
    $ set_zone('me_mt_house', 'alt_day5_uvao_evening_go_house')
    play sound sfx_paper_bag
    $ show_map()
    window show
    
label alt_day5_uvao_evening_map_strange:
    scene bg ext_dining_hall_away_sunset with fade
    "Мягко говоря, идея странная, но почему бы и нет? Тоже способ убить время…"
    jump alt_day5_uvao_evening_miss
label alt_day5_uvao_evening_map_peaceful:
    scene bg ext_dining_hall_away_sunset with fade
    th "Что же, неплохая идея. Посижу там спокойно - глядишь, и вечер пройдёт."
label alt_day5_uvao_evening_miss:
# Ошибаемся и внезапно приходим к димику. Обалдеваем и остаёмся там.
    "Я побрёл нога за ногу к намеченной цели, наслаждаясь тем, что вместе с уходящим солнцем дневная жара понемногу начала сдавать свои позиции."
    window hide
    scene black with dissolve2
    $ renpy.pause(2)
    window show
    "Впрочем, ноги оказались куда практичнее головы…"
    window hide
    scene bg ext_house_of_mt_sunset with dissolve2
    window show
    stop music fadeout 3
    "…Так что через несколько минут я с некоторым удивлением обнаружил себя прямо перед приютившим меня треугольным домиком."
    th "Минуточку!{w} Разве я сюда шёл?"
    dreamgirl "Можно подумать, ты всё ещё помнишь, куда собирался идти.{w} Неужели за день не набегался? Если уж тело столь бесцеремонно берёт инициативу в свои руки - самое время к нему прислушаться."
    "Немного подумав, я решительно махнул на всё рукой."
    th "В конце концов, здесь ничем не хуже, чем в любом другом месте.{w} Спокойно, никто не шляется туда-сюда."
    jump alt_day5_uvao_evening_headlong_already_here
label alt_day5_uvao_evening_go_house:
    scene bg ext_dining_hall_away_sunset with fade
    th "Действительно, что тут думать? Как будто я за день недостаточно набегался.{w} Пойду-ка я домой, посижу там спокойно до отбоя."
label alt_day5_uvao_evening_headlong:
    window hide
    $ renpy.pause(1)
    scene bg ext_house_of_mt_sunset with dissolve2
    window show
label alt_day5_uvao_evening_headlong_already_here:
    stop sound_loop fadeout 7
    stop music fadeout 5
    "Впрочем, особого желания сидеть в прогревшемся за день домике у меня не было."
    if (alt_uvao_D5_sh_mines):
        "Вместо этого я с удовольствием развалился на стоящем у входа шезлонге и уставился в наливающееся закатным румянцем небо."
    else:
        "Вместо этого я с удовольствием развалился на стоящем у входа шезлонге и, с лёгким смущением вспомнив послеобеденную сцену на площади, уставился в наливающееся закатным румянцем небо."
    "Ласковый ветерок чуть шевелил над головой ветви уже отцветающей, но всё ещё душистой сирени."
#    th "Интересно, разве сирень цветёт в июле, а не в самом начале лета?"
    th "Странно, лето уже явно за середину перевалило, а сирень всё ещё цветёт."
    "Лениво подумал я, бездумно пытаясь дотянуться рукой до ближайшей ветки, не отрывая при этом спины от шезлонга."
    dreamgirl "Тебе-то какая разница? Тоже мне, ботаник-любитель выискался."
    "Разницы особой и в самом деле не было, так что я просто добавил ещё один пункт к длинному списку местных странностей."
    "Впечатлений за день и так набралось предостаточно."
    "Утренний поход к старому корпусу и попытка открыть дверь в конце тоннеля…{w} Я осторожно ощупал колено и удовлетворённо отметил, что дела явно идут на поправку."
    "Короткий отдых в бункере"
    if alt_uvao_D5_hentai:
        extend " и последовавшая за ним сцена, от воспоминания о которой я мечтательно улыбнулся."
    elif alt_uvao_true:
        extend " и ошеломившая меня фотография на экране смартфона."
    else:
        extend "…"
    if alt_uvao_D5_sh_mines:
        "Блуждание вслепую по тёмным шахтам и беготня за спятившим Шуриком."
    else:
        "Чудом не приключившаяся со мной трепанация черепа… И странное поведение Лены, кстати говоря."
    "За всеми этими мыслями я и не заметил, как роскошный закатный пожар в небе подёрнулся пеплом, и вечер по-южному быстро уступил место ночи."
    stop ambience fadeout 2
    window hide
    scene bg ext_house_of_mt_night with dissolve2
    play ambience ambience_camp_center_night fadein 3
    $ persistent.sprite_time = "night"
    $ night_time()
    window show
    "Глаза уже безнадёжно слипались, когда рядом хрустнул гравий."
    show mt angry pioneer at cleft with dissolve
    play music music_list["always_ready"] fadein 3
    "Я приподнял голову. Рядом с сердитым видом стояла вожатая."
    mt "Скажите пожалуйста! Все люди как люди, один ты опять бездельничаешь и отрываешься от коллектива!"
    "Я аж задохнулся от возмущения:"
    if alt_uvao_D5_sh_mines:
        th "Ну да, конечно. Сама-то переработала прошлой ночью на пользу обществу, вот теперь на меня и срываешься."
        "Глядя на меня исподлобья она сварливо осведомилась:"
        mt "Ты почему в дом-то не идёшь спать? Стесняешься после сегодняшнего, что ли?"
        mt "Кстати, насчёт сегодняшнего - не думай, что ты победил. В моих силах сделать твоё пребывание в этом лагере не то, что более комфортным, но и вообще невыносимым.{w} Ты меня хорошо понимаешь, Семён?"
        "В её голосе не прозвучало явной угрозы, но сомневаться в серьёзности сказанных слов не приходилось. Я постарался ответить как можно спокойнее:"
        me "Я понимаю, Ольга Дмитриевна."
        show mt normal pioneer with dissolve
        mt "Вот и славно. Взаимопонимание - прекрасная вещь."
        hide mt with dissolve
        "С этими словами она повернулась и скрылась в домике."
        dreamgirl "Кажется, сегодняшние полежалки с Санычем отменяются."
        th "Кажется, да. Впрочем, ну её, пусть себе злится на здоровье. Мне с ней детей не крестить."
        "Я огляделся и почесал в затылке."
    else:
        th "Ну да, конечно! Особенно после обеда я сегодня бездельничал, аж чуть не помер от скуки!"
        "Кажется, эмоции ясно отразились на моём лице, потому что она вдруг усмехнулась:"
        show mt smile pioneer with dissolve
        mt "Ладно, горе ты моё луковое, ты почему в дом-то не идёшь спать? Под звёздами приятнее, что ли?"
        hide mt with dissolve
        "Пока я растерянно хлопал глазами, вожатая скрылась внутри домика."
    th "В самом деле, с чего это я здесь разлёгся? В постели-то оно и вправду спать приятнее."
    "Не успел я выбраться из шезлонга, как Ольга уже выбежала наружу."
    show mt normal pioneer far at cleft with dissolve
    mt "Спокойной ночи!"
    "Бросила она, деловито проносясь мимо меня."
    dreamgirl "Ну да, очередной сеанс самоотверженной работы на благо общества."
    if alt_uvao_D5_sh_mines:
        extend " По крайней мере, хоть перегаром она завтра на нас дышать точно не будет."
    else:
        extend " Надеюсь, хоть перегаром она завтра на нас дышать не будет."
    show mt normal pioneer far at left with ease
    me "Ольга Дмитриевна, а Вы куда на ночь-то глядя?"
    show mt rage pioneer far at left with dspr
    "Увидев лицо вожатой, я поспешил добавить:"
    me "Ой, извините. Я имею в виду, случилось что-то?"
    show mt angry pioneer far with dspr
    "Она смерила меня крайне недовольным взглядом, но всё-таки соблаговолила ответить:"
    mt "Да ничего не случилось. Хочу в медпункт зайти, проведать Шурика."
    if alt_uvao_true:
        "Она поколебалась немного и добавила:"
        show mt normal pioneer far with dspr
        mt "Да и с Виолеттой обсужу кое-что по нашей тематике."
    "Кивнув на прощание, Ольга заторопилась было дальше, но, сделав несколько шагов, внезапно притормозила и снова обернулась."
    show mt normal pioneer far at fleft with ease
    mt "А кстати, Семён, ты в библиотеку записывался?"
    me "Нет…"
    "Растерянно ответил я, совершенно сбитый с толку таким неожиданным поворотом."
    mt "Вот и я знаю, что нет. Поэтому учебник, который у тебя на тумбочке лежал, я сегодня отнесла обратно в библиотеку."
    show mt smile pioneer far with dspr
    mt "Нет у тебя читательского билета - нет и книжек!"
    show mt laugh pioneer far with dspr
    "Тут она самым легкомысленным образом показала мне язык и скрылась в темноте."
    hide mt with easeoutleft
    stop music fadeout 5
    "Ни злиться, ни расстраиваться сил уже совершенно не было, поэтому я махнул на всё рукой и пошёл спать."
    window hide
    play sound sfx_open_dooor_campus_1
    stop ambience fadeout 1
    scene bg int_house_of_mt_noitem_night with dissolve
    play ambience ambience_int_cabin_night fadein 1
    play sound sfx_close_door_campus_1
    window show
    "Кажется, раздеваться я начал уже на ходу, но не могу утверждать этого наверняка.{w} Единственное, что чётко отложилось у меня в памяти - это прикосновение прохладной подушки к щеке."
#    stop music fadeout 2
    window hide
    stop ambience fadeout 5
    scene bg black with fade2
    $ renpy.pause (2)
