#Разговор в домике и заключение в изоляторе
# TODO: спрайты, звуки, музыка.
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
    show mt normal pioneer with dspr
    mt "Семён, не ври мне хоть в этот раз. Я знаю всех детей в этом лагере. Никакой \"Юли\" среди них нет."
    th "Что же делать? Эх, была – не была. Да и что мне теперь уже остаётся, загнанному в угол?"
    if not alt_uvao_D4_viola_morning: #в 4 дне проговорились ОД
        me "Помните, я вам рассказывал про своё видение - девочка с кошачьими ушами и хвостом? {w}Так вот она на самом деле существует. Да-да!"
    else: # в 4 дне с утра беседовали с Виолой
        me "Я про легенду лагерную - девочку-кошку. Мне Виола рассказала тогда, и я ее встретил!"
    me "Её зовут Юля. Она живёт в катакомбах под старым корпусом, ловит мышей и делает запасы грибов на зиму.{w} Вчера я ходил к ней в гости провёл там всю первую половину дня."
    show mt surprise pioneer with dspr
    "Видимо это невероятное объяснение произвело впечатление на вожатую, потому что глаза её округлялись всё больше и больше с каждой моей фразой. А в конце этой пространной речи она смотрела на меня уже с неподдельным испугом. Более того – я мог бы поклясться, что вожатая была в ужасе!"
    show mt angry pioneer with dspr
    mt "Семён! Ты, с этой кошкой! Никогда не смей больше подходить к ней! Она опасна!"
    mt "Ты с ней контактировал! Ты мог пострадать!"
    "Кажется она немного успокоилась."
    mt "Сейчас мы немедленно пойдём к доктору Виоле. Тебя надо обследовать."
    show mt normal pioneer far with dissolve
    "И она вскочила с кровати, направившись в сторону двери."
    me "Да со мной всё нормально!"
    "Но к сожалению, слова мои не возымели никакого эффекта. Пришлось встать и пойти вслед за вожатой."
    scene bg ext_house_of_mt_day
    "Вожатая буквально проволокла меня по лагерю, от домика "
    scene bg ext_square_day
    extend "через площадь "
    scene bg ext_aidpost_day
    extend " к медпункту. Все мои попытки объяснить, что поводов для паники и спешки нет, были мастерски проигнорированы."
    scene bg int_aidpost_day
    "В строение с красным крестом мы вломились, не утруждая себя буржуазными пережитками в виде стука в дверь."
    #show cs normal glasses_thru # очки на глазах
    #show mt normal pioneer #без панамы, ибо неслась от домика. Может заодно shocked?
    cs "Вообще-то неплохо бы стучаться."
    "Сказала Виола, не оборачиваясь. Лежащий на кушетке Электроник попытался смущенно натянуть рубашку…"
    # Кого обрабатывать Виолой будем - Шурика или Электроника после его очередного общения с Женей? У Электроника есть голый спрайт, наденем ему одни штаны для приличия... --перегаррет
    cs "Лежи, лежи… {i}пионер.{/i} Я еще не закончила обработку твоих… ран."
    mt "Виола, у нас ЧП."
    cs "Пять минут подождёт?"
    mt "Нет."
    cs "Ладно, пионер. Свободен. В следующий раз будь осторожнее."
    "Выпущенный на свободу Сыроежкин не заставил просить себя дважды - оделся в две секунды и испарился. В другое время я б полюбопытствовал, где это он умудрился так интересно пораниться, но сейчас…"
    cs "Ну и с чего вдруг такая спешка? Что случилось?"
    mt "Кошка наша случилась. Помнишь, Семён вчера с утра куда-то пропал? А он, оказывается, все утро с ней по старым шахтам бегал!"
    #show cs normal glasses
    "Виола пристально посмотрела на меня, покусывая дужку очков."
    cs "Ну, пионер… Это правда?"
    th "Может, соврать? Скажу, что все придумал, чтобы вожатую позлить… Да какого черта, вообще?!"
    me "Да, правда!"
    "Виола неопределенно хмыкнула, Ольга же снова напустилась на меня."
    mt "Вот! Слышала?! И что теперь с ним делать? Это же… это… просто катастрофа!"
    cs "Пока еще ничего страшного не произошло, так что не сгущай краски, Ольга."
    mt "Не сгущай?! У меня тут шестьдесят человек детей под опекой, ты понимаешь, чем это все грозит?!"
    th "Это она к чему вообще?…"
    cs "Понимаю, понимаю. Ну и что ты предлагаешь делать? Звонить и срочно всех эвакуировать? Пока повода нет."
    mt "Когда повод будет - будет уже поздно!"
    th "Какая еще эвакуация?!"
    cs "И тем не менее, панику разводить рано. Ты ведь понимаешь, общая эвакуация - это необратимо? Объект будет загажен с концами, только закрывать."
    mt "А что делать-то?!"
    cs "Снимать штаны и бегать!{w} У нас всего два дня осталось. Закроем смену как обычно, к следующему периоду все устаканится."
    mt "А с ним-то что предлагаешь делать?"
    cs "Да ничего. Выпороть его, конечно, не мешало бы, но это не наш метод.{w} Посидит тут, завтра вместе со всеми сядет в автобус и прости-прощай."
    me "Да вы… это же… Вы не имеете права!"
    "От подобной перспективы я даже стал заикаться, но мои возмущеные тирады не произвели ровно никакого впечатления."
    cs "Помолчи, пионер. Ты даже не понимаешь, что происходит, и чем чреваты твои эскапады с аномалией."
    me "С кем? Это с Юлей-то?!"
    mt "Это он ее так окрестил. Юля её зовут, говорит…"
    cs "Интересно… впрочем, неважно.{w} Семён, здесь у нас кое-что посерьезнее обычного пионерского лагеря, как ты понял. Весьма важный научный проект, мирового уровня."
    cs "И мне совершенно не улыбается все закрывать по вине бестолкового попаданца.{w} Посидишь в изоляторе сегодня-завтра, ничего с тобой не случится."
    if alt_uvao_D4_viola_morning:
        cs "Надо было тебе, пионер, сразу мне все рассказать. Сам виноват."
    me "Эээ… Попаданца?"
    cs "Ну да. Жаргонное название для пришельцев из параллельного мира."
    me "Так что же получается… "
    extend "ВЫ ВСЁ ЗНАЛИ?! " with vpunch
    extend "С самого начала знали, что я никакой не пионер?!"
    cs "Не кричи, пионер. Да, мы двое знали. И делали вид, чтобы избежать лишних вопросов, и еще по некоторым причинам."
    me "И по каким же?"
    cs "Вечером расскажу. Если хорошо себя вести будешь."
    "Она отперла дверь изолятора и приглашающе взмахнула рукой."
    dreamgirl "Ваш номер, сэр! Не угодно ли чаю? Кофе? Девочек?"
    cs "К сожалению, придется тебе тут поскучать. Вроде там какие-то журналы оставались, Трофимов не забрал. А обед тебе кто-нибудь принесет."
    hide cs
    hide mt
    with dissolve
    "Дверь захлопнулась, щелчок замка утвердил мой новый статус арестанта. Из-за двери донеслось - "
    mt "Виола, дай чего-нибудь, а то меня аж трясет. А мне еще с концертом этим…"
    cs "Валерьянки? Сейчас…"
    "Я повалился на кровать. Простыни источали крепкий больничный запах - стерильность, стерильность и еще раз стерильность."
    dreamgirl "Ну что, заловили нас с тобой, волк{b}и{/b} позорные! Ты из блатняка что-нибудь знаешь? \"Владимирский централ\" смогёшь?{w} Если будем достаточно громко завывать, кто-нибудь удивится, что тут происходит."
    th "Или Виола вколет какого-нибудь успокоительного. Карательная психиатрия, знаешь ли…{w} Хотя может хоть они меня от тебя избавят…"
    dreamgirl "О, как высоко меня оценили! Это льстит."
    "Повалявшись немного и погрузившись в бездны отчаянья, я взялся за журналы - \"Юные Техники\" за январь и февраль 85-го года. К сожалению, повесть Кира Булычева обрывалась на самом интересном месте, а все остальное мне было малоинтересно."
    "Делать было абсолютно нечего. От скуки я начал обдумывать планы побега, но, как оказалось, дверь была довольно прочной, а окна были забраны решетками."
    if (keys_keep or keys_take == 1):
        "Даже всесильный артефакт, открывающий любые двери в лагере, не мог помочь - замочной скважины с моей стороны не было."
    th "Это же пионерлагерь, а не СИЗО, не колония малолетних! Зачем здесь решетки-то на окнах?!"
    dreamgirl "По-видимому, специально для таких вот - как она назвала? - попаданцев. Расслабьтесь, граф, еще не время копать подкоп ложкой."
    "Мое вот уже двухчасовое заточение нарушил сначала щелчок внешнего замка, а затем стук в мою дверь."
    me "Да-да! Входите пожалуйста, прошу вас!"
    " ответил я, даже не пытаясь скрыть сарказм."
    show sl normal pioneer
    sl "Привет, Семён. Как ты тут?"
    me "Замечательно! Веселюсь от души."
    "Яд моих слов можно было сцеживать в мензурку. Впрочем, Славя никак не отреагировала."
    sl "А я тебе покушать принесла. Обед сегодня очень вкусный!"
    "И вправду, в руках она держала авоську с металлическими посудинами. Из-под крышек просачивался умопомрачительный запах. Я внезапно ощутил, насколько же я проголодался!"
    # звук урчания?
    me "О! Это очень кстати!"
    "Я забрал у нее судки и расставил на столе. Солянка! Густая, нажористая, как в лучших домах! И макароны по-флотски."
    dreamgirl "Одно хорошо, кормят на здешней зоне от пуза!"
    "Я не нашел, чем возразить, и зачерпнул первую ложку, самую вкусную, самую полную. Славя присела на кушетку возле двери, пристально глядя на меня."
    dreamgirl "Смотри, а выход все же пасёт. Может, её - того? И на волю?"
    "Я чуть не подавился."
    th "ТОГО?!" with hpunch
    dreamgirl "Ну вон, под кроватью железное судно. Увесистая вещь, должно быть. Такой по башке огреть…"
    th "…"
    th "Ты что несешь, идиота кусок?! На мокруху меня подбива… тьфу."
    "Ощущение, проявившееся у меня в голове, больше всего походило на громогласное лошадиное ржание. Зарекшись еще хоть как-то реагировать на выходки внутреннего придурка, я проглотил все, что у меня было во рту и повернулся к Славе."
    me "Очень вкусно! Спасибо тебе."
    sl "На здоровье! Послушай, Семен…{w} А хочешь, я тебя выпущу?"
    # тишину, а потом музыку, знаменующую поворот сюжета
    me "Что?"
    sl "Хочешь, я тебя отсюда выпущу?"
    " - повторила она, как для идиота."
    th "Славя просто так возьмет - и нарушит порядок? Невероятно!"
    if alt_uvao_D5_evening_sl:
        extend " Вчерашние странности продолжаются…"
    me "В чем подвох?{w} Это на тебя непохоже."
    # Славя хитро улыбается
    sl "Может быть, ты просто плохо меня знаешь?{w} Так что? Ты согласен?"
    me "То есть ты просто так возьмешь и выпустишь меня? Без всяких условий?"
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
            "Славя рассмеялась."
            sl "Там все увидишь! Ну давай, выходи скорее, а то кто-нибудь придет."
            th "Ну, хватит нерешительности. Пора действовать! Кстати, надо обед захватить с собой. Мало ли, сколько партизанить придется…"
            "Я шустро сложил судки обратно в авоську и вышел вслед за Славей."
            sl "Я выгляну, если никого нет - позову тебя."
            # щелчок замка
            "- сказала она, запирая дверь в пустой изолятор."
            # скрип двери
            sl "Выходи, никого нет!"
            scene bg ext_aidpost_day
            me "Так, что дальше? Прятаться в лесу?"
            # уходим на дикий пляж, где тонул в Славя-руте
            sl "Дальше - через забор за футбольным полем, и выходи к реке, там заброшеный пляж есть. Там никто искать не будет."
            sl "А я тебя там потом найду."
            # Перелезаем забор, проливаем на себя солянку из кастрюли в силу косорукости. Пичаль-беда.
            # Отмываемся от супа на пляже. Встречаемся с Юлей, купаемся, делим обед на двоих. Шорох, Юля прячется.
            # Приходит Славя и толкает речь про то, что все ненастоящее, что это Семен все придумал, и он должен проснуться и взять ее с собой
            # голос из кустов сзади Слави - Не верь ей.
            jump alt_day6_uvao_isolator_sl_escape
        "Отказаться":
            pass
    th "Очень уж это подозрительно. Не может всё быть так просто."
    th "Ей что-то от меня надо, о чем я впоследствии определенно пожалею."
    me "Нет, спасибо. Я не люблю, когда со мной играют втемную."
    me "Я лучше подожду, пока Виола вернется. Все это - просто огромное недоразумение!"
    dreamgirl "Нас выпустят, это точно!" 
    # Славя удивлена, что Семен не ломанулся приключаться, в  собственном вымышленном мире-то
    sl "Но, Семён… Ты разве за этим сюда приехал, чтобы скучать взаперти?!"
    me "Поскучаю, ничего страшного."
    # TODO: Славя продолжает настойчиво окучивать, в стиле вербовщиков МЛМ и Кирби, но Семен непреклонен
    "Она собиралась еще что-то сказать, но я перебил."
    me "Благодарю за предложение, но нет. Подумать только, самая примерная активистка, помощница вожатой предлагает мне удрать из лагеря!"
    # Славя злится, что планы обломались
    "Кажется, это ее задело за живое."
    sl "Ладно же! Вот и сиди тут один, как сыч!"
    "Она стремительно вышла, не забыв захлопнуть и запереть дверь."
    
    # Сидим, скучаем дальше
    # Юля в окне. "Ты там булку ешь? А мне?"
    # Семен пугается - из-за этой кошки чуть весь лагерь не эвакуировали
    # Потом постепенно успокаивается, выбор - попросить принести ключи или "уходи, ушастая, видишь что из-за тебя делается"