# Д6-Утро
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines
#
label alt_day6_uvao_getting_up:
    window hide
    $ routetag = "uv"
    $ alt_chapter(6, u"Юля. Утро")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg int_house_of_mt_sunset
    show prologue_dream
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
#        dreamgirl ""
#        "Голос Шизы тоже показался мне каким-то заспанным."
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
                "На меня внезапно обрушился целый ворох каких-то разрозненных обрывочных образов."
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
                "Голос Шизы звучал укоризненно. Я беспомощно потряс головой, которую словно бы наполнили ватой."
                th "Что именно я сделал напрасно? Чихнул?"
                dreamgirl "Проснулся ты напрасно, бестолочь! Подождал бы ещё немного - уже пора было бы снова спать ложиться."
                "Я взглянул за часы и охнул, кубарем скатившись с кровати."# две цг-шки с будильником есть в модпаке. Там часы показывают 11:42 и 12:55 соответственно. Можно поправить при желании.
                th "Мама дорогая, вот это я вздремнул! Ещё пару часов, и если не ужинать, то уж обедать-то точно пора будет!{w} Неудивительно, что голова тяжёлая."
                "Наскоро одевшись, я решил, что немного холодной воды на мою бедовую головушку сейчас не помешает, и поскакал к умывальникам."
                jump alt_day6_true_sl_morning
    elif alt_uvao_D5_sh_mines:
        # Спалились накануне вечером ОД, знаем об аномалии немного.
        "Спал я плохо, а проснулся с жуткой головной болью. Наверное сказалась усталость вчерашнего дня – моральная и физическая. Бывает такое: вроде спал, а не отдохнул совсем. Надо будет к Виолетте Церновне зайти, взять какое-нибудь обезболивающее."
        dreamgirl "Да-да, сходи, конечно. Она тебе клизму пропишет целебную, семиведёрную. Враз вся хворь пройдёт. А уж о кошечке и думать забудешь!"
        "Шиза в своём репертуаре. Не успел я глаза открыть, а уже нарвался на комментарий. Интересно, а чем этот внутренний стебок занимается, когда я сплю? Играет в шахматы, после каждого хода переворачивая доску?"
        th "А вот возьму, да и схожу!"
        "Надменно ответил я своему альтер-эго."
        th "Она ведь приглашала меня к себе… {w}для беседы. Информацию какую-то обещала…"
        "Кроме того, меня беспокоила вчерашняя конфронтация с нашей любимой надзирательницей. Что-то подсказывало, что Ольга Дмитриевна этого так не оставит."
        "Я покосился на соседнюю кровать. Она ожидаемо была пуста и заправлена."
        th "Наверное вожатая на планерке у начальника лагеря. Получает заряд бодрости на весь день. За вчерашнее ЧП."
        th "А потом, надо думать, придёт давать заряд бодрости мне.{w} Нет-нет, никакой мести, мессир. Конечно же, исключительно в воспитательных целях. И исключительно методами советской педагогики."
        # ЛБ: Вопрос к размышлению - находится ли вчерашний инцидент у ворот (и не только) в компетенции нач.лагеря, или это внутренние дела ОД и ВЦ? Впрочем, в этой ветке ГГ может и не догадываться об истинной структуре управления в лагере.
        dreamgirl "Не забудет-не простит, можешь не сомневаться. Её здесь не для того поставили, чтобы всякие пионеры беспорядки нарушали и дисциплину хулиганили."
        th "Ладно, шутки в сторону. Пора вставать."
        "И, откинув одеяло, я начал слезать с кровати."
        play sound sfx_open_door_2
        show mt normal panama pioneer far at cright with dissolve
        "На улице послышался шум шагов и в комнату ворвалась вожатая. В который уже раз она застает меня в неглиже?{w} Я-то всего один раз её видел. Какое-то слишком неравноценное соотношение."
        "На языке крутилась фраза: \"Стучаться надо, Ольга Дмитриевна!\", но я сдержался и просто прикрылся. {w}Во первых потому, что это был прежде всего её домик, а во вторых из-за сердитого выражения лица. Видно, у начлагеря всё прошло совсем нехорошо."
        show mt angry panama pioneer with dspr
        "Вожатая остановилась посреди комнаты и вперила в меня грозный взгляд."
        me "Вы что-то хотели, Ольга Дмитриевна?"
        "Робко начал я, и тут же спохватился."
        th "Что я в самом деле рефлексую-то? Надо избавляться от этой привычки. Тварь я дрожащая или право имею?"
        dreamgirl "Тварь-то ты конечно тварь…"
        "Ехидно вставила шиза."
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
        "Я мгновенно оделся, путаясь в шортах и рукавах рубашки. Галстук… ну его к черту!"
        mt "Ну ты всё там?"
        me "Да, можете заходить."
        "Ответствовал я, заканчивая заправлять кровать."
        play sound sfx_open_door_2
        show mt normal panama pioneer close at cright with dissolve
        mt "Так вот, Семён."
        "Начала вожатая, присаживаясь на кровать напротив меня."
        mt "Я надеюсь, что хоть какая-то часть нашей вчерашней беседы в столовой отложилась у тебя в памяти."
        "И Ольга посмотрела на меня, видимо ожидая какой-то реакции. Но поскольку я молчал, она продолжила."
        mt "Ты вообще выводы сделал какие-нибудь?"
        "Я почесал в затылке."
        me "Да, сделал кое-какие.{w} Надо лучше прятаться в следующий раз."
        show mt angry panama pioneer close with dspr
        mt "Семён, хватит паясничать!"
        "Рассердилась Ольга Дмитриевна. Я примиряющее поднял руки."
        me "Ладно-ладно, я пошутил."
        mt "Я тебе ещё раз серьёзно повторяю – эта… это существо опасно. Очень опасно. Мы совершенно не знаем, какой может быть эффект от общения с ним. Ты ведь уже в курсе, что случилось с Александром?"
        #ЛБ: А ГГ точно в курсе, что случилось с Александром? Вроде бы, вечером Д5 это не афишировалось?
        "Я кивнул."
        mt "Скорее всего, это именно воздействие этой твоей… Юли. Мы пока не знаем, как это произошло, и обратим ли эффект.{w} А тебе, думаю, пока просто везло! И неизвестно, сколько продлится такое везение."
        "Я с недоверием смотрел на вожатую. Нет-нет, Юля это никакое не существо. Она живая и теплая. Она веселая и с ней интересно. Нет у меня никакого воздействия. А Шурик просто умственно перетрудился. С гениями такое бывает."
        "Ольга Дмитриевна с какой-то особой серьёзностью посмотрела на меня и медленно проговорила:"
        mt "Запомни самое главное.{w=0.8} Оно не человек.{w=0.8} Ты понял?{w=0.8} Не{w=0.8} человек."
        "Я обхватил голову руками. В ней роились мириады мыслей. Такое количество неприятной, непонятной информации было не так просто воспринять. Кроме того, в виски начало долбить словно молотом."
        "А вдруг вожатая права? Вдруг это началось воздействие на мой бедный, и так не очень здоровый рассудок? Закончить свои дни в комнате, обитой матрасами?{w} Нет, нет… Я отказываюсь принимать такое…"
        show mt normal panama pioneer close with dspr
        "Ольга терпеливо ждала моей реакции."
        mt "Вижу, что ты до сих пор до конца мне не веришь. Что ж, не в моих силах заставить тебя. В таком случае - {w}Будь.{w} Очень.{w} Осторожен."
        mt "Я не знаю всех подробностей, но Виолетта Церновна должна знать больше. Думаю, тебе стоит навестить её."
        show mt smile panama pioneer close with dspr
        mt "Но только после завтрака. Ты ведь помнишь: здоровое питание прежде всего."
        "Она легонько улыбнулась и ушла."
        hide mt with dissolve
        "Линейку, с этой лекцией о паранормальных явлениях, я пропустил. И слава рандому. Интересно, кто её проводил, если вожатка здесь была?{w} Славя наверное, как обычно. Ей не впервой."
        "Остаётся нерешённым лишь один вопрос. Верить или не верить словам вожатой?"
        "С одной стороны, ведь не одна Ольга меня пугает. Виола тоже не остаётся в стороне."
        "С другой стороны, это может быть просто коллективная работа по воспитанию подрастающего поколения. Осталось только Саныча на меня натравить. С каким-нибудь страшным рассказом."
        menu:
            "Пойти на завтрак":
                pass
                # Умываемся ("Неосознанно приобретаю полезные привычки, хех…."), идем в столовую
                # пока стоим в очереди на раздаче, приходит Виола, получает паек без очереди и приглашает на беседу за начальственный стол.
                jump alt_day6_uvao_breakfast_with_viola
                # Завтрак начинается с прихода в столовую, так что умывашки писать в этой ветке.
            "Пойти в медпункт":
                jump alt_day6_uvao_morning_aidpost
    else:
        "Спал я как убитый. А проснулся с ощущением, что мои руки отделили от тела и оставили где-то в другом месте. Наверное, вчерашняя переноска Шурика, будь он неладен, виновата. Вставать не хотелось. Я с наслаждением потянулся."
        "Наши рученьки устали, мы таскали, мы таскали…"
        th "Интересно, как он будет отмазываться сегодня?"
        dreamgirl "Интересно, как сегодня будешь отмазываться ТЫ?"
        "Хихикнула Шиза."
        me "А я-то за что ?"
        dreamgirl "Да ведь тебя вчера с утра никто не видел. И на завтраке ты не был. И на зарядке тоже. И линейку пропустил. И не поучаствовал ни в одном лагерном мероприятии. В общем ты ужасный пионер, Семён."
        "И Шиза снова залилась ехидным смехом."
        #ЛБ: по возможности нейтрализовать пол Шизы
        "Быстро одевшись, я пошёл в сторону умывальников."
        window hide
        scene bg ext_house_of_mt_day with dissolve
        play sound sfx_close_door_1
        $ renpy.pause(1)
        scene bg ext_washstand_day with dissolve
        $ renpy.pause(1)
        scene bg ext_washstand2_day with dissolve
        play sound sfx_open_water_sink
        $ renpy.pause(1)
        play sound_loop sfx_water_sink_stream
        window show
        "Умывание-умывание… Брр… Эту пытку ледяной водой, наверное, Генда придумал, не иначе."
        "И такая экзекуция каждый день. Но результат всё же радует - бодрость духа и тела в наличии. И сон прогоняет на раз-два. Закаляйся, если хочешь быть здоров…"
        "А теперь \"продолжим наши игры, как говорил редактор юмористического журнала, открывая очередное заседание и строго глядя на своих сотрудников\" - то есть пора идти на зарядку."
        #ЛБ: Не заседание, а редколлегию? Если это не цитата, конечно.
        window hide
        play sound sfx_close_water_sink
        stop sound_loop
        play ambience ambience_camp_center_day fadein 4
        scene bg ext_square_day with dissolve
        $ persistent.sprite_time = "day"
        $ day_time()
        window show
        #ЛБ: Далее в тексте желательно хотя бы часть реплик поменять местами с сопроводительным текстом
        "На площади как всегда многолюдно. Традиционные махи и наклоны под предводительством жизнерадостной Слави, невыспавшиеся лица пионеров – всё как обычно. Всё-таки и от ежедневной лагерной рутины есть какая-то польза."
        "А теперь линейка. Я наперёд знал последовательность событий. Вот из толпы выходит Славя, чеканя шаг. Подходит к вожатой, делает салют. Идёт к флагштоку. Кажется сегодня меня не позовут поднимать флаг."
        dreamgirl "Ты расстроен? Я лично очень."
        "И Шиза притворно шмыгнула носом."
        "Алое полотнище взмывает к небу. Всё-таки есть что-то магическое в поднятии флага, есть."
        "А теперь должен быть сигнал на завтрак. Но… похоже сегодня возникли какие-то изменения в привычном лагерном графике."
        show mt normal pioneer far with dissolve
        "На середину площади вышла Ольга Дмитриевна. Я вдруг почувствовал неладное."
        dreamgirl "Готовься, чувак." 
        "Прошептала мне Шиза, подтверждая мои подозрения."
        mt "Пионеры, внимание."
        "Сказала вожатая, обращаясь сразу ко всем."
        "Ребята загалдели, лица их выражали разочарование и недовольство. Похоже они, как и я, не понимали, почему вместо завтрака должны выслушивать какие-то незапланированные речи вожатой."
        "Но у Ольги Дмитриевны очевидно был большой опыт в подавлении мятежей на кораблях."
        show mt angry pioneer far with dspr
        mt "А ну-ка тихо!"
        "Она повысила голос всего лишь слегка, но и этого – удивительное дело - оказалось достаточно: все сразу же замолчали. Всё-таки авторитет это большая сила."
        show mt normal pioneer far with dspr
        mt "Семён." 
        "Теперь она обращалась ко мне."
        play music music_list["eat_some_trouble"] fadein 4
        mt "Выйди-ка сюда."
        show mt normal pioneer with dissolve
        "Мне ничего не оставалось, как выйти в центр площади на подгибающихся ногах. Ненавижу толпу. А если ещё ты знаешь, что тебя сейчас ожидает публичная порка перед этой самой толпой, то дело вообще труба."
        mt "Не потрудишься ли объяснить своё вчерашнее отсутствие на зарядке, линейке и завтраке?"
        "Строго спросила у меня вожатая."
        me "Я это… гулял…"
        "Пролепетал я."
        th "Блин! И почему я её боюсь-то? Мужик я или не мужик, в конце концов? Надо расправить плечи и ответить ей что-нибудь эдакое."
        dreamgirl "Чувак! Это называется субординация. Не ты это придумал, и не тебе это менять."
        me "Я гулял, гулял… и заблудился. Вот!"
        mt "Интересно, где же ты это гулял, что заблудился?"
        "Похоже вожатой моя версия вчерашнего отсутствия ни на минуту не показалась правдоподобной."
        me "А я в лес гулять ходил. Грибы там знаете, ягоды…"
        "Мой голос звучал всё менее уверенно. А Ольга Дмитриевна мрачнела всё больше."
        show mt angry pioneer with dspr
        mt "Так. Значит ты ещё и покидал территорию лагеря."
        "Зловещим тоном начала она."
        mt "Ты ведь знаешь, что пионерам запрещено покидать территорию оздоровительного учреждения. Без сопровождения взрослых."
        #ЛБ: А лагерь - это оздоровительное учреждение? С точки зрения канцелярита вопрос принципиальный. Уточнить.
        "Пионеры молча внимали речам вожатой. Похоже, каждый из них был рад, что не он оказался на моём месте. А я был бы рад отказаться от этой роли и поменяться с кем-нибудь, да только кто бы ещё вызвался."
        show un shy pioneer far at fright with dissolve
        "Краем глаза я заметил сочувственный взгляд Лены. Она, в свою очередь, заметила, что я смотрю на неё и покраснела, но глаза не отвела."
        hide un with dissolve
        "Некоторые пионеры уже начали высказывать недовольство задержкой традиционного кормления, которому я послужил невольной причиной."
        show mt normal pioneer with dspr
        mt "Так. Спокойно, пионеры. Я уже заканчиваю."
        mt "Ты всё понял?"
        "Обратилась ко мне вожатая."
        "Оказалось, что последние пару минут болтовни вожатки я пропустил мимо ушей. Но не признаваться же в этом?"
        me "Да, да, конечно, Ольга Дмитриевна."
        "Соврал я."
        me "Оправдаю и исправлюсь, больше не повторится."
        stop music fadeout 4
        play sound eat_horn fadein 2
        mt "Прекрасно. А теперь все могут идти завтракать."
        hide mt with dissolve
        "И как по заказу раздался сигнал горна. Она что, всё предусмотрела?"
        stop sound fadeout 3
        dreamgirl "Так, а здесь у нас непоняточки."
        "Возмущённо фыркнул мой внутренний собеседник."
        dreamgirl "Почему это тебя допросили с пристрастием, а вчерашнего героя дня Шурика свет Арматуровича - нет? Он-то кажется провинился не меньше, а то и побольше нашего."
        "В кои-то веки я был согласен с Шизой. Но логику вожатой мне, похоже, до конца не понять…"
        jump alt_day6_uvao_breakfast_without_sh

label alt_day6_uvao_morning_aidpost:
    window hide
    scene bg ext_aidpost_sunset with dissolve
    play ambience ambience_camp_center_day fadein 4
    $ persistent.sprite_time = "day"
    $ day_time()
    window show
#ЛБ: Далее в тексте желательно хотя бы часть реплик поменять местами с сопроводительным текстом
    "Голова беспокоила меня всё больше и больше, а звон в ушах всё усиливался. Что ж, придётся видимо и правда навестить доктора Виолу. Столовая подождёт – голова важнее."
    "Дорога до медпункта, обычно недолгая, сегодня заняла у меня раза в три больше времени. Я шел медленно, пытаясь собрать мысли в кучу. Да и как иначе, когда твоё мироздание кто-то пытается препарировать и выпотрошить!"
    th "Юля… Как же так. Что же она такое, в самом деле?"
    th "Эй, ты здесь?"
    "Без особой надежды позвал я, решив провести консультацию со своим внутренним голосом."
    dreamgirl "Здесь конечно. Я всегда здесь. Чего изволите-с?"
    th "Можно хоть иногда без твоих шуточек обойтись?"
    dreamgirl "В принципе можно, конечно… Но нужен ли тебе будет такой скучный внутренний собеседник?"
    dreamgirl "Кажется тебе себя самого должно быть достаточно!"
    "И Шиза захохотала, видимо донельзя довольная собственной шуткой."
    # ЛБ: Нейтрализовать пол Шизы
    "И тут же резко оборвала себя."
    dreamgirl "Ладно, чего хотел-то?"
    th "Мне по Юле консультация нужна"
    dreamgirl "Ну если судить по словам и поведению вожатой, которая, похоже, боится данного явления до… гкхм… в общем сильно боится, то опасаться стоит и тебе."
    dreamgirl "Вопрос в том, чего именно тебе следует опасаться? Думаю ответ на этот вопрос может дать наш милый доктор."
    "Как говорится, одна голова хорошо, а две…? Одна у меня, а другая… тоже у меня."
    play sound sfx_knock_door7_polite
    "Вот и медпункт. Глубоко вздохнув, я постучался."
    cs "Заходи, пионер, заходи."
    th "Интересно, как она узнала, что это я? Ах, да! Она же ко всем так обращается."
    "Моя паранойя, помноженная на шизофрению, иногда позволяла делать парадоксальные выводы."
    dreamgirl "Эй, ты кого шизофренией обозвал!?"
    "Возмущённо фыркнула Шиза."
    # ЛБ: Нейтрализовать пол Шизы
    window hide
    scene bg int_aidpost_day
    show cs normal glasses far
    with dissolve
    play music music_list["eternal_longing"] fadein 4
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 4
    window show
    "Виолетта Церновна сидела за столом и заполняла какие-то бланки."
    cs "А, Семён. Присядь пока."
    "И она приглашающим жестом показала на кушетку."
    show cs normal glasses with dissolve
    "Присев, я от нечего делать стал рассматривать кабинет. Раньше как-то возможности не было. Весы, шкаф с лекарствами, пара кушеток, ничего необычного. На стене плакат с бодрой надписью, призывающей разводить овощи. Зачем он здесь?"
    "Рядом плакат со схематичным  изображением какого-то создания, самого, что ни на есть гуманоидного вида. А это здесь для чего? Какие-то безумные эксперименты доктора Коллайдер? Что вы скрываете, Виолетта Церновна?"
    "Мои глаза блуждали по комнате и наконец остановились на таблице Сивцева по научному, а в просторечии просто таблицы для проверки зрения. Что-то в ней не так…"
    "Виолетта закончила писать и повернулась ко мне."
    cs "Ну так что там у тебя?"
    me "Голова меня беспокоит."
    cs "В каком смысле?"
    me "Шум, гул, звон в ушах…"
    "Виола с любопытством смотрела на меня."
    cs "Что ж, давай проведём осмотр."
    show cs smile glasses with dspr
    cs "Да не бойся!"
    "Рассмеялась она, заметив как я сжался."
    cs "Сегодня просто обычный осмотр."
    "Оказывается она может и нормально разговаривать."
    cs "Можешь даже рубашку не снимать… пионер." #Виола не коверкает слова, это занятие Семёна
    "А, нет, показалось."
    show cs normal glasses with dspr
    "Виола поочерёдно посветила мне фонариком в глаза, послушала пульс, смерила давление и задумалась."
    cs "Ну что я могу сказать. По первичным результатам обследования, все медицинские показатели у тебя в норме."
    cs "Хорошо бы ещё конечно томограмму головного мозга сделать, но аппараты такого серьёзного уровня есть только в райцентре." 
    # ЛБ: Томограф, кмк, в 1989г. можно было бы найти В Москве, в Ленинграде, м.б. ещё в Новосибирске каком-нибудь и _некоторых_ республиканских столицах. Причём томограф рентгеновский, не МЯР... Лучше бы про томографы убрать долой. Или приправить фразу такой ударной дозой сарказма, чтобы до каждого дошло, что до томографа как до Луны.
    cs "Я думаю, ты просто переутомился. Возможно, перегрелся на солнце."
    cs "А пока – вот тебе таблетка болеутоляющего."
    "Она достала таблетку анальгина и налила стакан воды."
    cs "После окончания смены я отвезу тебя на обследование. Не беспокойся, всё будет в порядке."
    # ЛБ: Кмк, фраза про "отвезу после окончания смены" должна вызвать у ГГ бурные реакции, как минимум - внутренние.
    "Слова Виолы почти успокоили меня, но я не дал себе расслабиться."
    me "Виолетта Церновна."
    cs "Что-нибудь ещё?"
    me "Да. На самом деле, у меня есть подозрения, что моё ухудшившееся состояние связано с… с Юлей."
    "Виола снова вздрогнула, хоть и мгновенно взяла себя в руки. Как и в прошлый раз, когда я упомянул это имя."
    # ЛБ: "Виола снова вздрогнула" - кажется, Виола пока что не вздрагивала до этого...
    cs "Да, это очень вероятно."
    "Спокойно кивнула головой она."
    cs "А я всё ждала, когда ты сам придёшь с этим вопросом."
    cs "Ты ведь помнишь, что случилось с Трофимовым? Боюсь, что подобный кризис может повториться. И он будет повторяться всё чаще и чаще, пока психика данного субъекта не будет полностью разрушена."
    # ЛБ: Разве тема про Трофимова уже где-то обсуждалась ранее подробно?
    me "Что!?"
    "Я вскочил с кровати."
    me "Шурик полностью сойдёт с ума?"
    cs "Это один из вариантов развития событий."
    "Всё с тем же убийственным спокойствием ответила Виола."
    cs "Как только он будет попадать в зону воздействия этой… аномалии, его психика будет страдать."
    cs "И с каждым разом всё сильнее."
    me "Что же делать?"
    cs "Единственный известный мне способ, который позволит избежать воздействия, это полностью исключить контакт с аномалией."
    me "Значит надежда всё-таки есть."
    "С облегчением сказал я, снова усаживаясь."
    cs "Я пока не настроена столь оптимистично."
    cs "Подобное предупреждение и тебя касается тоже, Семён."
    "Тут она посмотрела прямо мне в глаза своим разноцветными глазищами."
    cs "Я не хочу тебя пугать… но твоя кошкодевочка опасна.{w} Очень опасна."
    cs "То, что у тебя воздействие проявляется в другой форме, нежели у Трофимова, возможно ещё хуже."
    cs "Ты, как более спокойный человек, в конечном итоге, окончишь свои дни полностью в вегетативном состоянии."
    play sound eat_horn fadein 2
    cs "Подумай о моих словах, а сейчас иди завтракать."
    hide cs
    "И в самом деле, по лагерю разносился сигнал горна."
    window hide
    stop sound fadeout 3
    scene bg ext_aidpost_sunset with dissolve
    play ambience ambience_camp_center_day fadein 4
    play sound sfx_open_door_1
    window show
    "Я вышел из медпункта полностью опустошённым. Одна новость хлеще другой."
    "Что же мне делать? Поверить Ольге? Поверить Виоле? Но не могли же они сговориться? Или могли? Да и зачем всё это? Разыграть такой спектакль ради меня одного. Вопросов как всегда больше, чем ответов…"
    "Меня обгоняли беззаботные пионеры, спеша занять лучшие места в столовой. Что же у меня за пионерлагерь такой получается? Все дети, как дети – отдыхают, веселятся. А у меня сплошные думы и непонятки."
    dreamgirl "А что ты, собственно удивляешься, дружок? Ты сам-то, что – обычный пионер? Или ты из соседнего города приехал на летний отдых? {w}Вот и я о том же."
    dreamgirl "Необычному пионеру – и отдых необычный."
    menu:
        "Поверить словам Виолы":
            th "Дыма без огня не бывает, как говорится. Наверное, мне действительно стоит прислушаться к её словам."
            "И я не спеша отправился к столовой."
            jump alt_day6_uvao_breakfast_with_sh
        "Да это же какой-то бред":
            #TODO Текст
            "Если я правильно понимаю, тут должна быть катапульта. Нейтрал."
