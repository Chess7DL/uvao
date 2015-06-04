###############
# Д6 Беспалевная ветка
# Разговор в домике и заключение в изоляторе. 
# TODO: спрайты, звуки, музыка.
#
# Используется флаг alt_uvao_D4_viola_morning
# Используется флаг alt_day2_sl_keys_kept
# Используется флаг alt_day1_sl_keys_took
# Используется флаг alt_uvao_D5_evening_sl
# Используется флаг alt_day2_us_escape
# Используется флаг alt_uvao_D6_trust_uv
# Устанавливает флаг alt_uvao_D6_trust_uv
#
label alt_day6_uvao_isolator_house:
    window hide
    scene bg int_house_of_mt_sunset
    play ambience ambience_int_cabin_day fadein 4
    play music music_list["what_do_you_think_of_me"] fadein 4
    window show
    "Я зашёл в наш с вожатой домик."
    me "Вы меня искали, Ольга Дмитриевна?"
    "Вожатая лежала на кровати с книгой в руках. Интересно, что читают вожатые? Не любовные же романы? Хотя с нашей станется."
    show mt normal pioneer with dissolve
    mt "Да, Семён. У меня к тебе серьёзный разговор."
    "Сказала Ольга Дмитриевна, откладывая книгу в сторону. Я присмотрелся к обложке. Так я и думал. \"Унесённые ветром\", Маргарет Митчелл. После дамского чтива серьёзные разговоры самое то."
    mt "Семён."
    "Мягко начала вожатая, принимая сидячее положение."
    mt "Я ведь всё равно узнаю, где ты был вчера. Лучше расскажи всё сам. Как говорится, признание своей вины смягчает наказание."
    me "Опять начинается?"
    "Возмутился я. Впрочем не очень сильно."
    show mt angry pioneer with dspr
    mt "Да, Семён, да. Начинается. Это моя обязанность - знать всё обо всех."
    show mt normal pioneer with dspr
    mt "А также моя обязанность заботиться обо всех. Вот ты отсутствовал половину дня."
    mt "Усталый, голодный. А потом твои родители с меня спрашивать будут ведь, почему их мальчик так исхудал."
    me "Да не был я голодный."
    "Возмутился я."
    me "Мы с Юлей булочками перекусили…"
    show mt surprise pioneer with dspr
    "И тут же зажал себе рот рукой. Блин! Что же я наделал?!"
    mt "Это кто такая?"
    "Нахмурилась вожатая."
    me "Девочка одна знакомая."
    "Вяло попытался отбрыкиваться я. Но вожатую было уже не остановить."
    show mt angry pioneer with dspr
    mt "Семён, не ври мне хоть в этот раз. Я знаю всех детей в этом лагере. Никакой \"Юли\" среди них нет."
    th "Что же делать? Эх, была – не была. Да и что мне теперь уже остаётся, загнанному в угол?"
    if not alt_uvao_D4_viola_morning: #в 4 дне проговорились ОД
        me "Помните, я вам рассказывал про своё видение - девочка с кошачьими ушами и хвостом?{w} Так вот она на самом деле существует. Да-да!"
    else: # в 4 дне с утра беседовали с Виолой
        me "Я про легенду лагерную - девочку-кошку. Мне Виола рассказала тогда, и я её встретил!"
    me "Её зовут Юля. Она живёт в катакомбах под старым корпусом, ловит мышей и делает запасы грибов на зиму.{w} Вчера я ходил к ней в гости провёл там всю первую половину дня."
    show mt surprise pioneer with dspr
    "Видимо это невероятное объяснение произвело впечатление на вожатую, потому что глаза её округлялись всё больше и больше с каждой моей фразой. А в конце этой пространной речи она смотрела на меня уже с неподдельным испугом. Более того – я мог бы поклясться, что вожатая была в ужасе!"
    show mt angry pioneer with dspr
    mt "Семён! Ты, с этой…{w} кошкой!{w} Никогда не смей больше подходить к ней! Она опасна!"
    mt "Ты с ней контактировал! Ты мог пострадать!"
    "Кажется она немного успокоилась."
    mt "Сейчас мы немедленно пойдём к доктору Виоле. Тебя надо обследовать."
    show mt normal pioneer far with dissolve
    "И она вскочила с кровати, направившись в сторону двери."
    me "Да со мной всё нормально!"
    "Но к сожалению, слова мои не возымели никакого эффекта. Пришлось встать и пойти вслед за вожатой."
    window hide
    scene bg ext_house_of_mt_day
    show mt normal pioneer at cright
    with dissolve
    window show
    "Вожатая буквально проволокла меня по лагерю, от домика "
    window hide
    scene bg ext_square_day
    show mt normal pioneer at cright
    with dissolve
    window show
    extend "через площадь "
    window hide
    scene bg ext_aidpost_day
    show mt normal pioneer at cright
    with dissolve
    window show
    extend "к медпункту. Все мои попытки объяснить, что поводов для паники и спешки нет, были мастерски проигнорированы."
    window hide
    play music music_list["eternal_longing"] fadein 5
    play sound sfx_open_door_1
    scene bg int_aidpost_day
    show cs normal glasses_thru at cleft #очки на глазах
    show mt normal pioneer at cright #без панамы, ибо неслась от домика. Может заодно shocked?
    show el surprise pioneer far at fleft behind cs
    with dissolve
    window show
    "В строение с красным крестом мы вломились, не утруждая себя буржуазными пережитками в виде стука в дверь."
    cs "Вообще-то неплохо бы стучаться."
    "Сказала Виола, не оборачиваясь. Лежащий на кушетке Электроник попытался смущенно натянуть рубашку…"
    # Кого обрабатывать Виолой будем - Шурика или Электроника после его очередного общения с Женей? У Электроника есть голый спрайт, наденем ему одни штаны для приличия... --перегаррет
    cs "Лежи, лежи… {i}пионер.{/i} Я ещё не закончила обработку твоих… ран."
    mt "Виола, у нас ЧП."
    cs "Пять минут подождёт?"
    mt "Нет."
    cs "Ладно, пионер. Свободен. Впредь будь осторожнее."
    hide el with dissolve
    "Выпущенный на свободу Сыроежкин не заставил просить себя дважды - оделся в две секунды и испарился. В другое время я б полюбопытствовал, где это он умудрился так интересно пораниться, но сейчас…"
    cs "Ну и с чего вдруг такая спешка? Что случилось?"
    mt "Кошка наша случилась. Помнишь, Семён вчера с утра куда-то пропал? А он, оказывается, все утро с ней по старым шахтам бегал!"
    show cs normal glasses with dspr
    "Виола пристально посмотрела на меня, покусывая дужку очков."
    cs "Ну, пионер… Это правда?"
    th "Может, соврать? Скажу, что все придумал, чтобы вожатую позлить… Да какого черта, вообще?!"
    me "Да, правда!"
    "Виола неопределённо хмыкнула, Ольга же снова напустилась на меня."
    show mt angry pioneer at cright with dspr
    mt "Вот! Слышала?! И что теперь с ним делать? Это же… это… просто катастрофа!"
    cs "Пока ещё ничего страшного не произошло, так что не сгущай краски, Ольга."
    mt "Не сгущай?! У меня тут шестьдесят человек детей под опекой, ты понимаешь, чем это все грозит?!"
    th "Это она к чему вообще?…"
    cs "Понимаю, понимаю. Ну и что ты предлагаешь делать? Звонить и срочно всех эвакуировать? Пока повода нет."
    mt "Когда повод будет - будет уже поздно!"
    th "Какая ещё эвакуация?!"
    cs "И тем не менее, панику разводить рано. Ты ведь понимаешь, общая эвакуация - это необратимо? Объект будет загажен с концами, только закрывать."
    mt "А что делать-то?!"
    cs "Снимать штаны и бегать!{w} У нас всего два дня осталось. Закроем смену как обычно, к следующему периоду все устаканится."
    mt "А с ним-то что предлагаешь делать?"
    cs "Да ничего. Выпороть его, конечно, не мешало бы, но это не наш метод.{w} Посидит тут, завтра вместе со всеми сядет в автобус и прости-прощай."
    me "Да вы… это же… Вы не имеете права!"
    "От подобной перспективы я даже стал заикаться, но мои возмущённые тирады не произвели ровно никакого впечатления."
    cs "Помолчи, пионер. Ты даже не понимаешь, что происходит, и чем чреваты твои эскапады с аномалией."
    me "С кем? Это с Юлей-то?!"
    mt "Это он её так окрестил. Юля её зовут, говорит…"
    cs "Интересно…{w} впрочем, неважно.{w} Семён, здесь у нас кое-что посерьёзнее обычного пионерского лагеря, как ты понял. Весьма важный научный проект, мирового уровня."
    cs "И мне совершенно не улыбается все закрывать по вине бестолкового попаданца.{w} Посидишь в изоляторе сегодня-завтра, ничего с тобой не случится."
    if alt_uvao_D4_viola_morning:
        cs "Надо было тебе, пионер, сразу мне все рассказать. Сам виноват."
    me "Эээ… Попаданца?"
    cs "Ну да. Жаргонное название для пришельцев из параллельного мира."
    me "Так что же получается… "
    extend "ВЫ ВСЁ ЗНАЛИ?! " with vpunch
    extend "С самого начала знали, что я никакой не пионер?!"
    cs "Не кричи, пионер. Да, мы двое знали. И делали вид, чтобы избежать лишних вопросов, и ещё по некоторым причинам."
    me "И по каким же?"
    cs "Вечером расскажу. Если хорошо себя вести будешь."
    "Она отперла дверь изолятора и приглашающе взмахнула рукой."
    dreamgirl "Ваш номер, сэр! Не угодно ли чаю? Кофе? Девочек?"
    cs "К сожалению, придётся тебе тут поскучать. Вроде там какие-то журналы оставались, Трофимов не забрал. А обед тебе кто-нибудь принесёт."
    window hide
    hide cs
    hide mt
    with dissolve
    play sound sfx_open_door_kick 
    with fade
    play music music_list["trapped_in_dreams"] fadein 4
    window show
    "Дверь захлопнулась, щелчок замка утвердил мой новый статус арестанта. Из-за двери донеслось - "
    mt "Виола, дай чего-нибудь, а то меня аж трясёт. А мне ещё с концертом этим…"
    cs "Валерьянки? Сейчас…"
    "Что-то стукнуло, звякнуло, булькнуло…"
    mt "Что ж за смена-то такая… Все она, чтоб её… Мало того, что Шурик едва жив остался, так ещё и это…{w} Виола, ты уверена, что до эффекта не дойдёт?"
    cs "Уверена. Может он вообще - {i}того{/i}? Пока мы ходим…" # намекает, что Семен котопультируется оттуда.
    th "Он? {i}Того{/i}? О чем это они?"
    "Я повалился на кровать. Простыни источали крепкий больничный запах - стерильность, стерильность и ещё раз стерильность."
    dreamgirl "Ну что, заловили нас с тобой, волк{b}и{/b} позорные! Ты из блатняка что-нибудь знаешь? \"Владимирский централ\" смогёшь?{w} Если будем достаточно громко завывать, кто-нибудь удивится, что тут происходит."
    th "Или Виола вколет какого-нибудь успокоительного. Карательная психиатрия, знаешь ли…{w} Хотя может хоть они меня от тебя избавят…"
    dreamgirl "О, как высоко меня оценили! Это льстит."
    "Повалявшись немного и погрузившись в бездны отчаянья, я взялся за журналы - \"Юные Техники\" за январь и февраль 85-го года. К сожалению, повесть Кира Булычева обрывалась на самом интересном месте, а все остальное мне было малоинтересно."
    "Делать было абсолютно нечего. От скуки я начал обдумывать планы побега, но, как оказалось, дверь была довольно прочной, а окна были забраны решётками."
    if (alt_day2_sl_keys_kept or alt_day1_sl_keys_took == 1):
        "Даже всесильный артефакт, открывающий любые двери в лагере, не мог помочь - замочной скважины с моей стороны не было."
    th "Это же пионерлагерь, а не СИЗО, не колония малолетних! Зачем здесь решётки-то на окнах?!"
    dreamgirl "По-видимому, специально для таких вот - как она назвала? - попаданцев. Расслабьтесь, граф, ещё не время копать подкоп ложкой."
    play sound sfx_knocking_door_outside
    "Моё заточение нарушил сначала щелчок замка внешней двери, а затем стук в мою дверь."
    me "Да-да! Входите пожалуйста, прошу вас!"
    "Ответил я, даже не пытаясь скрыть сарказм."
    play sound sfx_open_door_1
    show sl normal pioneer with dissolve
    sl "Привет, Семён. Как ты тут?"
    me "Замечательно! Веселюсь от души."
    "Яд моих слов можно было сцеживать в мензурку. Впрочем, Славя никак не отреагировала."
    sl "А я тебе покушать принесла. Обед сегодня очень вкусный!"
    "И вправду, в руках она держала авоську с металлическими посудинами. Из-под крышек просачивался умопомрачительный запах. Я внезапно ощутил, насколько же я проголодался!"
    play sound sfx_stomach_growl
    me "О! Это очень кстати!"
    "Я забрал у неё судки и расставил на столе. Солянка! Густая, нажористая, как в лучших домах! И макароны с котлетой."
    dreamgirl "Одно хорошо, кормят на здешней зоне от пуза!"
    "Я не нашёл, чем возразить, и зачерпнул первую ложку, самую вкусную, самую полную. Славя присела на кушетку возле двери, пристально глядя на меня."
    dreamgirl "Смотри, а выход все же пасёт. Может, её - того? И на волю?" # "Того" - у каждого человека разное. Лучше уточнить, кмк -R
    "Я чуть не подавился."
    th "ТОГО?!" with hpunch
    dreamgirl "Ну вон, под кроватью железное судно. Увесистая вещь, должно быть. Такой по башке огреть…"
    th "…"
    th "Ты что несёшь, идиота кусок?! На мокруху меня подбива… тьфу."
    stop music fadeout 4
    "Ощущение, проявившееся у меня в голове, больше всего походило на громогласное лошадиное ржание. Зарёкшись ещё хоть как-то реагировать на выходки внутреннего придурка, я проглотил все, что у меня было во рту и повернулся к Славе."
    me "Очень вкусно! Спасибо тебе."
    show sl smile pioneer with dspr
    sl "На здоровье!{w} Послушай, Семён…{w} А хочешь, я тебя выпущу?"
    play music music_list["you_lost_me"] fadein 4
    me "Что?"
    sl "Хочешь, я тебя отсюда выпущу?"
    " - повторила она, как для идиота."
    th "Славя просто так возьмёт - и нарушит порядок? Невероятно!"
    if alt_uvao_D5_evening_sl:
        extend " Вчерашние странности продолжаются…"
    me "В чем подвох?{w} Это на тебя не похоже."
    show sl smile2 pioneer with dspr
    sl "Может быть, ты просто плохо меня знаешь?{w} Так что? Ты согласен?"
    me "То есть ты просто так возьмёшь и выпустишь меня? Без всяких условий?"
    sl "Ну не совсем.{w} Одно условие все-таки будет."
    me "Ага, я так и подозревал.{w} И что я буду должен взамен?"
    sl "Пообещай мне сделать кое-то для меня."
    me "Что именно?"
    sl "Не могу сейчас сказать. Просто пообещай."
    me "Кота в мешке, значит…"
    sl "Не волнуйся, ничего невыполнимого я от тебя не потребую. Просто… одну вещь."
    menu:
        "Согласиться":
            me "Но ведь… меня сразу искать начнут. Что мне, пешком по шоссе убегать?"
            if alt_day2_us_escape:
                me "Или опять поезд ловить?"
            sl "Да не обязательно. Тебе всего-то до вечера надо спрятаться, а там я тебя найду."
            me "И что, потом вместе сбежим? Как романтично…"
            show sl laugh pioneer with dspr
            "Славя рассмеялась."
            sl "Там все увидишь! Ну давай, выходи скорее, а то кто-нибудь придёт."
            show sl normal pioneer with dspr
            th "Ну, хватит нерешительности. Пора действовать! Кстати, надо обед захватить с собой. Мало ли, сколько партизанить придётся…"
            "Я шустро сложил судки обратно в авоську и пошёл вслед за Славей."
            sl "Я выгляну, если никого нет - позову тебя."
            play sound sfx_close_door_1
            "- сказала она, запирая дверь в пустой изолятор."
            play sound sfx_open_door_1
            sl "Выходи, никого нет!"
            window hide
            scene bg ext_aidpost_day
            show sl normal pioneer
            with dissolve
            window show
            me "Так, что дальше? Прятаться в лесу?"
            # уходим на дикий пляж, где тонул в Славя-руте. Там же рядом Унылкин схрон
            sl "Дальше - через забор за футбольным полем, и выходи к реке, там заброшенный пляж есть. Там никто искать не будет."
            sl "А я тебя там потом найду."
            # Перелезаем забор, проливаем на себя солянку из кастрюли в силу косорукости. Пичаль-беда.
            # Отмываемся от супа на пляже. Встречаемся с Юлей, купаемся, делим обед на двоих. Шорох, Юля прячется.
            # Приходит Славя и толкает речь про то, что все ненастоящее, что это Семен все придумал, и он должен проснуться и взять ее с собой. Семен охреневает
            # Приходит Лена, видит Славю, сцена ревности, мерянье тем, кому Семен больше нужен. Семен охреневает вторично.
            # К этому балагану присоединяется Юля. 
            jump alt_day6_uvao_isolator_sl_escape
        "Отказаться":
            pass
    th "Очень уж это подозрительно. Не может всё быть так просто."
    th "Ей что-то от меня надо, о чем я впоследствии определённо пожалею."
    me "Нет, спасибо. Я не люблю, когда со мной играют втёмную."
    show sl surprise pioneer with dspr
    me "Я лучше подожду, пока Виола вернётся. Все это - просто огромное недоразумение!"
    dreamgirl "Нас выпустят, это точно!" 
    # Славя удивлена, что Семен не ломанулся приключаться, в  собственном вымышленном мире-то
    sl "Но, Семён… почему?"
    sl "Ты разве за этим сюда приехал, чтобы скучать взаперти?!"
    me "Поскучаю, ничего страшного."
    sl "Я не понимаю… "
    "Она собиралась ещё что-то сказать, но я перебил."
    me "Благодарю за предложение, но нет. Подумать только, самая примерная активистка, помощница вожатой предлагает мне удрать из лагеря!"
    show sl angry pioneer with dspr
    "Кажется, это её задело за живое. Она вскочила, кипя от злости…"
    sl "Ладно же! Вот и сиди тут один, как сыч!"
    hide sl with dissolve
    play sound sfx_open_door_kick
    "…и стремительно вышла, не забыв захлопнуть и запереть дверь."
    th "И что это такое сейчас было?"
    th "Сначала запирают.{w} Намекают на какую-то катастрофу из-за Юли.{w} Потом приходит Славя и предлагает просто выпустить."
    th "Да что за херня здесь происходит?!" with hpunch
    "Машинально черпая ложкой суп, я почти не чувствовал вкуса."
    #th "Ну давай разберём по частям мною сказанное." # Не стареющая классика
    th "Давай попробуем разложить все по полочкам."
    dreamgirl "Не то чтоб это была твоя сильная сторона, но попытка не пытка."
    th "Намёки Ольги про какую-то непонятную опасность…"
    if not alt_uvao_D4_viola_morning:
        th "А позавчера утром она просто наорала на меня, стоило мне упомянуть о хвостатой тени!"
        th "От реальной опасности не будут так отмахиваться!"
    else:
        th "А Виола наоборот была не против, чтобы я поискал это лагерное привидение."
    stop music fadeout 4
    th "А теперь - какая-то сплошная паника.{w} Научный проект на грани катастрофы, грядёт эвакуация лагеря… {i}Эффект{/i} какой-то ещё…"
    th "Психоз Шурика - это тоже Юля виновата, что ли? Да он всегда ненормальный был!"
    window hide
    play music music_list["memories"] fadein 4
    scene anim prolog_1
    show prologue_dream
    show uv normal behind prologue_dream
    with dissolve
    window show
    "Юля.{w} Смешная, наивная девочка-кошка…"
    "Перед мысленным взором всплыли воспоминания."
    window hide
    show bg ext_house_of_mt_day behind prologue_dream
    show uv dontlike close at center behind prologue_dream
    with dissolve
    window show
    "Первая встреча в окошке домика…"
    window hide
    hide bg ext_house_of_mt_day
    hide uv
    show bg ext_no_bus_sunset behind prologue_dream
    show uv smile at center behind prologue_dream
    with dissolve
    window show
    "Вечерний перекус булочками…"
    window hide
    hide bg ext_no_bus_sunset
    hide uv
    show int_old_building_day_uvao behind prologue_dream
    show uv normal at center behind prologue_dream
    with dissolve
    window show
    "Беседа в старом лагере…"
    window hide
    hide bg int_old_building_day_uvao
    hide uv
    show bg int_catacombs_living behind prologue_dream
    show uv smile close at center behind prologue_dream
    with dissolve
    window show
    "Странный бункер… "
    if alt_uvao_D5_hentai:
        extend "И наша животная страсть на пыльных матрасах."
    window hide
    hide bg int_catacombs_living
    hide uv
    show bg int_mine_crossroad behind prologue_dream
    show uv normal at center behind prologue_dream
    with dissolve
    window show
    "Короткое путешествие по заброшенным шахтам…"
    window hide
    scene anim prolog_1
    show prologue_dream
    show uv normal behind prologue_dream
    with dissolve
    window show
    th "Юля, конечно, странная…{w} эээ…{w} странное существо, но ожидать от неё каких-то катаклизмов… По-моему, она вполне безобидна." # котоклизмов, ага
    dreamgirl "Если, конечно, не считать той вожатой, с которой Юля {i}поговорила{/i}… Как она сказала - «Она почему-то бегала и кричала»?{w} Кажется, очень похоже на Шурика."
    dreamgirl "В общем, даже и не знаю, что тебе посоветовать."
    menu:
        "Поверить Ольге и Виоле":
            $ alt_uvao_D6_trust_uv = False
        "Юля - не опасна!":
            $ alt_uvao_D6_trust_uv = True
    window hide
    stop music fadeout 4
    scene bg int_aidpost_day with dissolve
    window show
    "От глубоких размышлений меня отвлекла чья-то тень в окне. Я обернулся."
    show uv normal far at center with dissolve
    uv "Привет. Это у тебя котлета? А мне?"
    "Это было так неожиданно, что я отшатнулся назад."
    if alt_uvao_D6_trust_uv:
        pass
        # Просим раздобыть ключи, Юля удивляется - а зачем - выйди так
        # в зависимости от флага хентая либо сбегаем, либо остаемся сидеть
    else:
        pass
        # Юля обижается
        # "Уходи, видишь, что из-за тебя получилось?"
        
