# Д6-Утро
#
# Используется флаг alt_uvao_D4_viola_morning
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines
# Устанавливается индикатор степени настойчивости Слави alt_uvao_D6_sl_assert (1-3)
#
label alt_day6_uvao_getting_up:
    #Выясняем степень настойчивости Слави alt_uvao_D6_sl_assert (1, 2, 3)
    #отчего-то в RenPy нет XOR...
    if (alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl): #оба ивента
        $ alt_uvao_D6_sl_assert = 3
    elif (not alt_uvao_D5_evening_sl) and (not alt_uvao_D4_lunch_sl): #ни одного ивента
        $ alt_uvao_D6_sl_assert = 1
    else:
        $ alt_uvao_D6_sl_assert = 2 #только один из ивентов
    #
    window hide
    $ routetag = "uv"
    $ alt_chapter(6, u"Юля. Утро")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg int_house_of_mt_sunset
    # show prologue_dream # оно нужно?
    play music music_list["my_daily_life"] fadein 4
    play ambience ambience_int_cabin_day fadein 4
    window show
    if alt_uvao_true:
# Будит ОД
        "Проснулся я от бесцеремонной тряски. Чья-то рука крепко ухватила меня за плечо и, похоже, просто так отпускать не собиралась."
        "С некоторым трудом глаза удалось открыть."
        scene bg int_house_of_mt_sunset
        show mt normal pioneer close at center
        with dissolve2
        "Рука, как можно было догадаться, принадлежала вожатой."
        th "Кажется, со мной это уже было… Спасибо хоть, сегодня без перегара обошлись."
        "Действительно, в отличие от вчерашнего утра, Ольга была бодра, свежа и вполне довольна жизнью."
        "Убедившись, что я более-менее проснулся, она прекратила наконец свою импровизированную утреннюю разминку и отпустила мою многострадальную руку."
        show mt smile pioneer at center with dissolve
        mt "Семён, хватит дрыхнуть!{w} Времени восемь часов, погода отличная!"
        mt "Тем более, у меня отличные новости для тебя!"
        me "Дайте угадаю - наступил мир во всём мире?"
        "Проворчал я, отчаянно зевая.{w} Кажется, перед самым пробуждением мне что-то снилось… Что-то важное, но что именно - вспомнить никак не получалось."
        show mt laugh pioneer with dspr
        mt "Ну не настолько грандиозно, к моему сожалению. Но от зарядки и утренней линейки я тебя освобождаю."
        show mt normal pioneer with dspr
        mt "Кстати, снова по болезни, как и вчера, так что не забудь заглянуть в медпункт к Виолетте."
        "Она нахмурилась было, но не удержалась и прыснула, махнув рукой."
        show mt laugh pioneer with dspr
        "Вспомнив сцену за вчерашним ужином, я лишь смущённо заёрзал в кровати."
        hide mt with dissolve
        play sound sfx_close_door_1
        "Продолжая посмеиваться, Ольга проворно убежала на улицу, а я вяло принялся выпутываться из хитроумного узла, в который за ночь превратилось моё одеяло.{w} Недосмотренный сон никак не шёл из головы."
        th "И всё-таки, что же мне снилось такое?…"
        menu:
            "Одеваться!":
                # сны - ерунда!
                "Впрочем, и в самом деле пора было уже вставать. Выспался я сегодня вволю, так что хорошенького понемножку."
                dreamgirl "Вот и молодец. Потехе время, а делу - час!{w} Ладно, за целеустремлённость тебе полагается бонус, так что получай свой сон!"
                # Для критиканов особо отмечу, что тру-Семён снов в Д5 не смотрел, так что пусть наверстает хоть немного
                "На меня внезапно обрушился целый ворох каких-то разрозненных смутных образов."
                window hide
                $ set_mode_nvl()
                window show
                # Сон Деимиург-куна
                "Насколько я смог разобрать, мне снилось, будто я проснулся посреди какого-то лагеря, причём никогда в похожем месте раньше не был."
                "Более-менее отчётливыми были образы странной девочки-брюнетки с короткой стрижкой и интересной куклой, которая выглядела как годовалый ребёнок."
                "Девочка постоянно доказывала всем, что это кукла, отрывая ей голову."
                "Ещё была злючка-вожатка, которая сразу принялась меня гнобить из-за всяких мелочей, ну и столовый бойкот запомнился - всё время, что я там провёл, я дежурил в столовой и постоянно недокладывал вожатке жратвы в знак протеста."
                "Ну и периодически подворовывал полдник…"
                "Девочку было немного жалко, она постоянно ходила одна, или сидела в сторонке и наблюдала за куклой, которая ходила сама по себе - никаких механизмов, обычная кукла…"
                "Кажется, я ее подкармливал ворованными булочками. Девочку, не куклу…"
#                nvl clear
                window hide
                $ set_mode_adv()
                window show
                "Всё остальное было совсем уж неразборчивым, так что ничего и понять было нельзя. Я ошарашенно затряс головой."
                th "Подожди, это что, и есть весь мой сон?!"
                dreamgirl "Ну так ведь никто и не обещал, что это будет \"Война и мир\". Хотя, как по мне, довольно креативненько получилось."
                th "Ты думаешь? Ладно, надо будет себя при случае попробовать на писательской стезе."
                "Быстро одевшись и прихватив полотенце, я отправился к умывальникам."
                jump alt_day6_true_CS_talk
            "Попытаться вспомнить сон.":
                # досыпаем…
                "Рассудив, что из-за пятиминутной задержки ничего не случится, я воспользовался проверенной методикой - закрыл глаза и постарался расслабиться, позволяя сну чуть-чуть коснуться меня."
                window hide
                show blinking
                scene black
                window show
                "Здесь главное было удерживать сознание на грани между явью и грёзой, не давая ни одной из них победить…"
                stop ambience fadeout 2
                window hide
                $ renpy.pause(5)
                scene bg int_house_of_mt_sunset
                with vpunch
                play ambience ambience_int_cabin_day fadein 2
                window show
                "…Оглушительно чихнув, я резко сел в постели, пытаясь понять, что происходит."
                dreamgirl "А вот это ты напрасно сделал."
                "Голос внутри моей черепной коробки прозвучал укоризненно. Я беспомощно потряс головой, которую словно бы наполнили ватой."
                th "Что именно я сделал напрасно? Чихнул?"
                dreamgirl "Проснулся ты напрасно, бестолочь! Подождал бы ещё немного - уже пора было бы снова спать ложиться."
                "Я взглянул за часы и охнул, кубарем скатившись с кровати."# две цг-шки с будильником есть в модпаке. Там часы показывают 11:42 и 12:55 соответственно. Можно поправить при желании.
                #ЛБ: По распорядку подъём в 8:00, завтрак в 9:00... На часах надо 10:12
                th "Мама дорогая, вот это я вздремнул! Ещё пару часов, и если не ужинать, то уж обедать-то точно пора будет!{w} Неудивительно, что голова тяжёлая."
                "Наскоро одевшись, я решил, что немного холодной воды на мою бедовую головушку сейчас не помешает, и поскакал к умывальникам."
                jump alt_day6_true_sl_morning
    elif alt_uvao_D5_sh_mines:
        # Спалились накануне вечером ОД, знаем об аномалии немного.
        # Могли Кошочку как отхентаить, так и нет.
        "Спал я плохо, а проснулся с жуткой головной болью. Наверное сказалась усталость вчерашнего дня – моральная и физическая. Бывает такое: вроде спал, а не отдохнул совсем."
        th "А я-то надеялся, что эти проблемы остались в прошлом, вместе со старым телом."
        th "Надо будет к Виолетте зайти, взять какое-нибудь обезболивающее."
        dreamgirl "Да-да, сходи, конечно. Она тебе клизму пропишет целебную, семиведёрную. Враз вся хворь пройдёт. А уж о кошечке и думать забудешь!"
        "Альтер эго было в своём репертуаре - не успел я глаза открыть, а уже нарвался на комментарий."
        "Интересно, а чем этот внутренний стебок занимается, когда я сплю? Играет в шахматы, после каждого хода переворачивая доску?"
        th "А вот возьму, да и схожу!"
        "Надменно ответил я своему мучителю."
        th "Она ведь приглашала меня к себе… {w}для беседы. Информацию какую-то обещала…"
        "Я покосился на соседнюю кровать. Она ожидаемо была пуста и заправлена."
        th "Наверное вожатая на планерке у начальника лагеря. Получает заряд бодрости на весь день. За вчерашнее ЧП."
        th "А потом, надо думать, придёт давать заряд бодрости мне.{w} Нет-нет, никакой мести, мессир. Конечно же, исключительно в воспитательных целях. И исключительно методами советской педагогики."
        # ЛБ: Вопрос к размышлению - находится ли вчерашний инцидент у ворот (и не только) в компетенции нач.лагеря, или это внутренние дела ОД и ВЦ? Впрочем, в этой ветке ГГ может и не догадываться об истинной структуре управления в лагере.
        "Я уныло вздохнул. Что-то подсказывало, что Ольга мой демарш так просто не оставит."
        dreamgirl "Не забудет-не простит, можешь не сомневаться. Её здесь не для того поставили, чтобы всякие пионеры беспорядки нарушали и дисциплину хулиганили."
        "Оставалась слабая надежда, что наш интимный разговор на троих за ужином никто больше не слышал, а Виолетта не станет подставлять вожатую и ябедничать начальству, но шансы на это были невелики."
        th "Ладно, шутки в сторону. Пора вставать."
        "Откинув одеяло, я спустил ноги с кровати."
        play sound sfx_open_door_2
        show mt normal panama pioneer far at cright with dissolve
        "На улице послышался шум шагов и в комнату ворвалась вожатая. В который уже раз она застает меня в неглиже?{w} Я-то всего один раз её видел. Какое-то слишком неравноценное соотношение."
        "На языке крутилась фраза: \"Стучаться надо, Ольга Дмитриевна!\", но я сдержался и просто прикрылся. {w}Во первых потому, что это был прежде всего её домик, а во вторых из-за сердитого выражения лица. Видно, у начлагеря всё прошло совсем нехорошо."
        show mt angry panama pioneer with dspr
        "Вожатая остановилась посреди комнаты и вперила в меня грозный взгляд."
        me "Вы что-то хотели, Ольга Дмитриевна?"
        "Робко начал я, и тут же спохватился."
        th "Что я, в самом деле, рефлексую-то? Надо избавляться от этой привычки. Тварь я дрожащая или право имею?"
        dreamgirl "Тварь-то ты конечно тварь…"
        dreamgirl "Шучу-шучу. Право действительно имеешь. Ты вчера такого туза из рукава достал."
        "Я прокашлялся."
        me "Что вы хотели, Ольга Дмитриевна?"
        "Уже куда более уверенным тоном официально повторил я."
        mt "Семён, нам надо серьёзно поговорить."
        me "А можно я сначала…"
        "И показал на одеяло, обращая внимание вожатой, что я, в общем-то, ещё не одет."
        show mt laugh panama pioneer with dspr
        "Она фыркнула и пошла к выходу."
        mt "Только недолго."
        me "Само собой."
        play sound sfx_open_door_2
        hide mt with dissolve
        "Я торопливо оделся, путаясь в шортах и рукавах рубашки. Галстук… ну его к черту!"
        mt "Ну ты всё там?"
        me "Да, можете заходить."
        "Ответствовал я, заканчивая заправлять кровать."
        play sound sfx_open_door_2
        show mt normal panama pioneer close at cright with dissolve
        mt "Так вот, Семён."
        "Начала вожатая, присаживаясь на кровать напротив меня."
        mt "Я надеюсь, что хоть какая-то часть нашей вчерашней беседы в столовой отложилась у тебя в памяти."
        "Ольга посмотрела на меня, видимо ожидая какой-то реакции. Но поскольку я молчал, она продолжила."
        mt "Ты вообще выводы сделал какие-нибудь?"
        "Я почесал в затылке."
        me "Да, сделал кое-какие.{w} Надо лучше прятаться в следующий раз."
        show mt angry panama pioneer close with dspr
        mt "Семён, хватит паясничать!"
        "Рассердилась вожатая. Я примиряющее поднял руки."
        me "Ладно-ладно, я пошутил."
        mt "Я тебе ещё раз серьёзно повторяю – эта… это существо опасно. Очень опасно. Мы совершенно не представляем, какой может быть эффект от общения с ним. {w}Тот же Трофимов…"
        "Ольга запнулась, скривившись. Вероятно, как и я, вспомнила вчерашний ужин, попытку разузнать у меня про произошедшее с Шуриком - и чем для неё всё в итоге закончилось."
        mt "Одним словом, Александр со вчерашнего дня в медпункте и… слегка не в себе, скажем так."
        mt "Скорее всего, именно эта твоя… Юля что-то с ним сотворила. Мы пока не знаем, как это произошло, и обратим ли эффект. {w}А тебе, думаю, пока просто везло! И неизвестно, сколько продлится такое везение."
        "Я с недоверием посмотрел на вожатую. Определённо, Юля по-прежнему не казалась мне опасной."
        "А что до Шурика… Положим, я-то совершенно точно знал, что именно с ним случилось. {w}Вернее, причастна ли к этому Юля."
        th "Но этот псих сам виноват, нефиг было лезть куда не надо и на меня бросаться. Да и мозги у него явно были набекрень ещё до встречи с Юлей - может, её попытка отпугнуть попросту стала для него последней каплей?"
        th "В общем, если бы не Юля, то он бы меня точно искалечил в этих чёртовых шахтах. Так что если Юля и опасна для кого-то, то уж точно не для меня."
        "Ольга с какой-то особой серьёзностью посмотрела на меня и медленно проговорила чуть ли не по слогам:"
        mt "Запомни самое главное.{w=0.8} Оно не человек.{w=0.8} Ты понял?{w=0.8} Не{w=0.8} человек."
        "Я обхватил раскалывающуюся голову руками. В ней роились мириады мыслей, ни одну из которых не удавалось додумать до конца."
        "Ольга продолжала что-то говорить. Возможно, мне было бы проще её понять, если бы не кузнечные молоты, беспощадно долбившие в виски."
        th "А вдруг вожатая права? Вдруг это началось воздействие на мой бедный, и так не очень здоровый рассудок? Закончить свои дни в комнате, обитой матрасами?"
        dreamgirl "Расслабься. Ты неадекватен ничуть не больше обычного, уж я-то знаю! Мне конкуренты ни к чему."
        show mt normal panama pioneer close with dspr
        "Ольга, так и не дождавшаяся какой-либо реакции на свои слова, восприняла моё молчание по-своему."
        mt "Вижу, что ты до сих пор мне не веришь. Что же, не в моих силах заставить тебя. В таком случае прошу хотя бы об одном. {w=1.5}Будь. {w=1.5}Очень. {w=1.5}Осторожен."
        mt "Я не знаю всех подробностей, но Виолетта Церновна должна знать больше. Думаю, тебе стоит навестить её."
        mt "Так что зарядку и линейку можешь сегодня пропустить - не теряй времени даром."
        show mt smile panama pioneer close with dspr
#        mt "Но только после завтрака. Ты ведь помнишь: здоровое питание прежде всего."
        "Она легонько улыбнулась и ушла."
        hide mt with dissolve
        th "И… и всё? Ни слова укоризны за моё вчерашнее выступление за ужином?"
        th "Ни единого упоминания о том, какая я неблагодарная тварь, подорвавшая её карьеру и сломавшая ей жизнь?"
        th "Вот это я понимаю, профессионализм! {w=1.5}Педагог! {w=1.0}Психолух!"
        dreamgirl "Возможно, ты этого не заметил, но вожатка последние минут пятнадцать что-то бубнила про Юлю. Не допускаешь мысли, что она была твоими контактами с ушастой озабочена настолько, что забыла из-за этого про личные невзгоды?"
        "Я с сомнением почесал в затылке. Конечно, существо, запросто способное {i}отпугнуть{/i} агрессивно настроенного человека, может вызывать опасения у окружающих, но чтобы уж до такой степени…"
        me "Ксенофобы чёртовы!"
        "Пожав плечами, я сгрёб умывальные принадлежности и направился к выходу."
        # сцена - домик ОД снаружи утром
        # хлопает дверь
        "Зарядку с этой лекцией о паранормальных явлениях я, хвала рандому, благополучно пропустил."
        th "Интересно, кто её проводил, если вожатая здесь была? Может быть, Славя? Ей не впервой."
        "Подумал я, на автомате направляясь к умывальникам."
        #сцена - дорожка между домиками утром
        th "Неосознанно приобретаю полезные привычки, ха…"
        "Оставался нерешённым лишь один вопрос. Верить или не верить словам вожатой?"
        "С одной стороны, ведь не одна Ольга меня пугает. Виола тоже не остаётся в стороне - что-то она такое говорила мне."
        if alt_uvao_D4_viola_morning:
            "Во всяком случае, у неё есть свой какой-то интерес к Юле, это ясно."
        "С другой стороны, это может быть просто коллективная работа по воспитанию подрастающего поколения. Осталось только Саныча на меня натравить. С каким-нибудь страшным рассказом."
        dreamgirl "Хорошо, если только с рассказом. Как бы он не решил на тебе отыграться, когда узнает, что ты спалил перед начальством его пассию. Да и его самого, кстати."
        "Поёжившись от малоприятной перспективы, я прибавил шагу."
        # сцена - умывальники утром
        "Я наскоро поплескал в лицо ледяной водой, мимолётно порадовавшись тому, что на умывальниках уже никого нет, а значит и нет риска быть облитым."
        # сцена - домик ОД снаружи утром
        "Забросив полотенце в домик, я в нерешительности притормозил на крыльце, потирая ноющие виски."
        menu:
            "Отлежаться немного.":
                "Сказано - сделано."
                "Недолго думая, я улёгся в стоящий тут же рядом шезлонг."
                th "Вряд ли меня здесь кто-то найдёт. Все, включая Ольгу, сейчас на линейке."
                th "Полежу немного, может голова пройдёт…"
                "Я с трудом подавил зевок."
                th "…а там уже решу, что дальше делать."
                # задрёмываем, просыпаемся от звуков горна на завтрак с относительно здоровой головой
                # возможно, видим сон. или сны. Или даже отгоняем дремоту и идём куда-то, например - на умывальники, смотреть Ульяну.
                # идем в столовую
                jump alt_day6_uvao_breakfast_with_viola
            "Пойти в медпункт":
                jump alt_day6_uvao_spoiled_CS_talk
    else:
        # Самостоятельное расследование, о Юле никто не знает.
        # Могли Кошочку как отхентаить, так и нет.
        
        
# какое-нибудь “Нас утро встречает прохладой”? 
# Из объятий сна меня выдернула до отвращения бодрая музыка, доносящаяся откуда-то с улицы. Бравурные трели с лёгкостью пронзали как фанерные стены, так и нахлобученную на ухо подушку.
# “ Это что за хреновы новшества?! Раньше же только горн играл!”
# Ш: “Так ведь радио починили. А раз работает - значит надо пользоваться.”
# “Это теперь каждый день будет?!”
# if Славя-эвент в д5:
# Ш: “Алё, проснись. Завтра уже отъезд, какое ещё каждый день?”
# Да, действительно. 
# else:
# Ш: "Слушай… ты только не волнуйся, но мне надо тебе кое-что сказать."
# Ш: "На самом деле…"
# Ш: "Смена заканчивается завтра."
# "Что?! Откуда знаешь?"
# Ш: "Линейка. Там иногда полезное говорят."
# Ш: "Но у тебя непревзойдённый талант игнорировать происходящее вокруг."
# Ш: "Короче, завтра всех рассадят по автобусам и отправят по домам."
# /if
# Но что будут делать со мной? Посадят в автобус вместе с остальными? А потом - что?
# “Неделя прошла, а ответов нет. Только еще больше вопросов.”
# Бодрая песня сменилась фортепианным проигрышем с периодическим отсчетом тактов. Кажется, на зарядку я опоздал…
# Ш: “Зато к линейке еще успеваешь. Давай-давай, нечего разлёживаться. Нас ждут великие дела!"
# Когда твоё раздвоение личности вознамерилось вытащить тебя в люди… С трудом орудуя негнущимися руками, я кое-как оделся и направился наружу - сначала умыться, а потом уже вливаться в общественную жизнь.

##пропускаем умывальники, там все равно ничего интересного.
##разве что Ульяну с Алисой в лифчиках позырить =)

##площадь
# Весь лагерь уже был выстроен на площади в кривоватые шеренги, я едва успел занять своё привычное место рядом со Славей.
# "Смотри-ка, своё место. Вживаюсь, однако."
# На центр площади выдвинулась Ольга Дмитриевна, с неизменной панамой на голове и чрезвычайно одухотворённым лицом. Не иначе, сейчас будет очередная воодушевляющая речь.
# Од: - Дорогие пионеры! Вторая смена 86-го года в лагере Совёнок подходит к концу. В связи с чем позвольте подвести некоторые итоги, с которыми…
# Дальше я не слушал, привычно отключившись от внешнего шума.
# "Всё ещё больше запутывается, не знаю что и делать. Юлю дальше расспрашивать?"
# if hentai:
# Ш: "Расспрашивать ли?"
# "Ой, заткнись."
# /if
# Мысль встретиться с Юлей почему-то казалась самой правильной. С ней было приятно, спокойно… 
# "Решено. После завтрака улизну от присмотра Ольги и поищу Юлю. Погуляем по лесу, может искупаться сходим, только подальше, чтоб не нашли. Во, еды надо какой-нибудь раздобыть, она булочки любит…"
# О: "...Персунов, выйти из строя!"
# "А? Что происходит?"
# Славя пихнула меня в бок.
# Сл: - Семён, не спи. Тебя зовут. 
# "Блин, кажется, я что-то пропустил. Знать бы ещё - что."
# Нехотя я сделал шаг вперёд и вопросительно уставился на вожатую. Что дальше-то?
# А ведь я не один такой, вызваный на всеобщее обозрение. Рядом со мной - грудь колесом, одухотворенная физиономия, хоть сейчас на плакат! - стоял Сыроежкин. А за ним, опустив очи долу - Лена.
##я знаю, что Лена по сценарию должна убежать на мыс Уныния, но пусть ОД её вовремя выловила и потребовала поприсутствовать хотя бы на линейке. "Должны присутствовать все трое - ты, Сыроежкин и Семён!" "Семён? Х-хорошо…"

# "Ааа… это нас сейчас за вчерашнее героическое спасение Шурика чествовать будут?"
# Ш: "Ну. Ты как, преисполнился гордости? Щас тебя на доску почёта вешать будут, и благодарность объявлять."
# "Я лучше б деньгами взял."
# По команде мы втроём, пародируя строевой шаг, выстроились у флага. Повторялась история с моего приезда - весь лагерь опять глазел на меня! 
# О: - За проявленный героизм и взаимовыручку пионерам Сыроежкину, Персунову, Тихоновой объявляется благодарность, и дается право поднять флаг! Ура!
# "Ну офигеть теперь."
# Под троекратное ура мы повернулись к флагштоку.
# Эл: - По очереди? Семён, давай ты первый, потом Лена.
# Л: - Л-ладно...
# "Опять! Да пусть бы гриб его один поднимал, а мы просто рядом постоим."
# Нехотя, со стократно возросшей неуклюжестью, я перехватывал руками тросик. Вот вам церемония, раз она вам так нужна, пож-ж-жалуйста, мне не сложно!
# Отмотав треть высоты, я передал трос Лене. Та, вздрогнув, оторвалась от созерцания трещинок гранитных плит и взглянула на меня. В огромных зеленых глазах плескалась паника, рука судорожно сжала трос, как утопающий - спасательный конец...
# "Бедный ребёнок. Похоже, ей эти почести - хуже смерти. Я удивляюсь, что она вообще согласилась выйти!"
# На её фоне моя скованность казалась не более чем мелким неудобством, о котором даже стыдно упоминать.
# - Лен… не бойся. Ничего страшного же! Всего-то пару метров прокрутить. 
# Под мой ободряющий шепот она подняла этот несчастный флаг и отдала трос Сыроежкину. На мгновение мне показалось, что она сейчас бросит всё и убежит. Ну или спрячется куда-нибудь… к примеру, мне за спину.
# Как бы то ни было, Электроник молодцевато, явно перед кем-то рисуясь, поднял флаг до финальной высоты и лихо взмахнул рукой в салюте.
# "Аа. Ещё ж и это."
# Чуть помедлив, мы с Леной тоже подняли руки, и строй пионеров ответил нам - и свежеподнятому флагу - тем же. Сейчас на площади стояла не разрозненная толпа, а объединенный общими идеалами коллектив.
# Ш: "И продлится это единство аж до самого завтрака."
# Славя, возглавлявшая строй, как-то чрезмерно радостно смотрела на меня. Как будто - и откуда вдруг это всплыло? - на своего щенка, занявшего призовое место на выставке породы. "Молодец!" - ясно прочел я по губам.
# "Если б не построение, она б, наверно, обниматься кинулась."
# Ш: "Что, желаешь припасть к пышной груди активистки? Одобряю!"
# Ш: "Или можешь, наоборот, послужить укрытием от посторонних взглядов для нашей стесняши. Она только этого и ждёт, гарантирую!"
# "Чтоб тебя."
# Как нельзя вовремя протрубил горн, подводя итог как построению, так и нашей внутренней перепалке.
# О: - Разойтись! Семён, Сергей, Лена, задержитесь.
# "Ну что ещё?!"
# О: - Вы ведь знаете, что сегодня у нас - отчетный концерт? 
# "Не, даже не подозревали."
# О: - Так вот. Позавчера, во время выступления, обнаружилось много накладок, и их необходимо исправить. Всё проверить, всё настроить, чтоб прошло без сучка и задоринки!
# - Так а мы-то тут при чём?
# Ш: "А вот догадайся…"
# if вступил к кибернетикам:
# О: - Как это при чём? Вы, как члены клуба кибернетики, лучше всех разбираетесь в электричестве, сигналах, проводах, и всём таком прочем.
# else:
# О: - Для Сергея, как члена клуба кибернетики, это профессиональная вотчина. 
# О: - А ты ему поможешь!
# - Я?!
# О: - Да, именно ты, Семён. Как примерный пионер.
# "Очень примерный."
# /if
# О: - Александр по медицинским показаниям освобожден от общественной работы, придется вам справляться вдвоём. Справитесь?
# Эл: - Да!
# - Нет.
# буркнул я, но, кажется, вопрос был риторическим.
# Л: - А я… тоже? 
# Лена, которая всё ещё пряталась у меня за спиной, подала тихий голос.
# О: - Нет, у меня для тебя другое задание. Надо вчерашнее происшествие - и, само собой, ваш героизм! - отразить в стенгазете.
# О: - Только лучше знаешь… без ненужных подробностей. Понимаешь?
# Л: - Я? Н-не знаю… Может, лучше…?
# О: - Сейчас объясню. Лучше тебя все равно никто не справится!
# Ольга, приобняв недоумевающую Лену за плечи и взмахом руки отпустив нас питаться, повлекла ее куда-то в сторону библиотеки.

# Эл: - Ну что, Семён, поработаем?
# - Сработаемся.
# "Повторяемся. Операцию Ы мы уже разыгрывали, неужели больше сюжетов нет?"
# С настроением, стремительно идущим ко дну, я направился питаться.

