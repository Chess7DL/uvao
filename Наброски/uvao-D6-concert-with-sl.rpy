# Д6 после обеда
# Концерт, ужин и побег со Славей с дискотеки - ветка, где считаем, что Славя нас окучивает с амурными целями

init:
    $ tl_7dl = Character(name=u"Толик", color="#A1752F", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
# TODO: Перекинуть толика куда-нибудь
label alt_day6_uvao_concert_with_sl:
    window hide
    $ alt_chapter(6, u"Юля. Концерт")
    scene bg ext_stage_normal_day
    show mt angry pioneer at center
    with dissolve
    play music music_list["eat_some_trouble"] fadein 4
    play ambience ambience_camp_center_day fadein 4
    window show
    "Уже на подходе к сцене я заметил вожатую, нетерпеливо расхаживающую взад-вперёд по дорожке. Она явно кого-то ждала. Меня, родимого, кого же ещё."
    mt "Семён, ну где ты ходишь ?! Концерт уже начинается."
    "Так и есть."
    me "А чего я-то сразу?"
    "Притворно заныл я."
    me "Мне на сцене не выступать."
    mt "А ведь ты мог бы. Будь ты сознательным пионером, как другие ребята. Посмотри вот хотя бы на Славяну. У неё номер сегодня."
    show mt normal pioneer at center with dspr
    "И она показала на Славю, как раз проходившую мимо."
    show sl smile pioneer far at fleft with dissolve
    "Я посмотрел, отчего же не посмотреть. Славя девочка что надо. Но за этой активисткой мне не угнаться. Нет ни желания, ни сил."
    "Заметив мой взгляд, Славя улыбнулась и помахала рукой."
    hide sl with dissolve
    "Ольга тоже проводила Славю взглядом и продолжила:"
    mt "Мероприятие коллективное, к посещению обязательное."
    mt "А ты, как элемент несознательный, у меня вообще на особом контроле. Поэтому сидеть будешь рядом."
    "Вот так так. Приехали! Весь концерт придётся сидеть рядом с вожатой и усиленно изображать удовольствие от терзания моего слуха, потугами местных сотрясателей воздуха изобразить что-то, отдалённо напоминающее пение."
    dreamgirl "Да ладно, тебе не впервой"
    "Вдруг вмешалась Шиза."
    dreamgirl "Помнишь, как тебя назначили судить конкурс талантов?"
    "Я содрогнулся. Такое не забудешь."
    "Не помню в преддверии чего это было, но скорее всего какой-то праздник. Руководство престижного лицея, в котором я учился, решило провести песенный конкурс талантов среди учащихся. Дабы, так сказать, выявить самых одарённых. С последующей отправкой победителя в область, по пути дальнейшего совершенствования."
    "Не знаю уж, какими соображениями они руководствовались при выборе кандидатов, но из всех десяти участников ни у кого не было ни слуха, ни голоса. Вы можете себе такое представить? Ни у кого!"
    "Возможно свою роль сыграло то, что эти так называемые \"певцы\", все сплошь как один, были детьми педагогов, а победителем – естественно – стала дочка директора лицея."
    "Не знаю, как я выдержал то прослушивание, но в тот момент я понял, что ад для людей с музыкальным слухом существует. Неужели сегодня мне предстоит повторение того кошмара?"
    mt "Ну пойдём, пойдём, Семён, чего застыл."
    "Нетерпеливо подтолкнула меня в сторону сцены Ольга Дмитриевна."
    "Пробравшись между пионерами, мы с вожатой сели в первом ряду, рядом со Славей. На самом освещённом месте, между прочим. Кто же это такой умный догадался на зрителей прожекторы направить? Сцену надо освещать, сцену! Зрителей-то зачем?"
    mt "Ну вот, здесь нам с тобой всё будет хорошо видно и слышно."
    show mt smile pioneer at center with dspr
    "Улыбнулась она."
    me "Ага, и нас тоже будет очень хорошо видно и очень хорошо слышно."
    "Пробурчал я про себя. Вот зачем мне такая публичность?"
    mt "Надеюсь ты не будешь предпринимать попыток побега."
    me "Да я и не собирался."
    "Пожал я плечами."
    "И правда, как уж тут теперь сбежишь, когда под самой рампой сидишь и весь лагерь на тебя пялится."
    mt "Смотри у меня."
    "Шутливо погрозила пальцем вожатая."
    mt "А теперь всё внимание на сцену."
    "Тем временем на сцене, Мику, закончив приветственное слово, начала своё выступление."
    "Из колонок полились первые аккорды бодрой музыки. Она звучала смутно знакомо и это было странно. Где я мог её слышать? Ведь в здешнем репертуаре кроме Юрия Антонова на пару с Леонтьевым ничего и не сыщешь."
    "Ого! А песня-то на японском. Нет, как раз в том, что японка поёт по японски, не было ничего удивительного. Меня удивило то, что вожатая дала добро на такое исполнение. Никто ведь ничего не поймёт."
    mt "Ничего страшного."
    "Улыбнувшись, ответила на мой невысказанный вопрос вожатая."
    mt "Пусть ребята приобщаются к культуре других стран. Красоту песни можно и без понимания смысла понять."
    "Ну что же, ей виднее конечно."
    sl "Семён, а это на японском песня?"
    show sl normal pioneer close at left 
    hide mt
    with dissolve
    "Тронула меня за плечо Славя."
    me "Да, на японском вроде. На английский не похоже."
    "Покивал головой я."
    sl "А о чём она?"
    th "Ну откуда же я знаю? У Мику надо спрашивать."
    "Собрав в кучу все свои скудные знания японского языка, я попытался объяснить."
    me "Это песня про девушку, которая мечтает о любви и романтике и говорит о своих чувствах языком рифмы, просто потому, что не умеет по другому. Она мечтает найти родственную ей душу в другом мире. Песня называется \"Расскажи мне про свой мир\", как-то так."
    show sl surprise pioneer close with dspr
    sl "Ты знаешь японский язык?"
    "С нескрываемым уважением посмотрела на меня Славя."
    me "Есть немного."
    hide sl with dissolve
    "Конечно я знаю японский язык. Как впрочем и английский. И ещё пару-тройку. Правда всё на прикладном уровне."
    "Я и мне подобные - мы дети современной культуры, живущие во всемирной паутине.  Мы нахватались знаний, полученных из разных источников. Мы знаем всё и мы не знаем ничего. Дилетанты широкого профиля."
    "Пионеры, будто заворожённые, слушали песню. Кажется права вожатая. Вот она, сила искусства!"
    "Шквал аплодисментов был наградой певице. Замечательная песня. Надо у Мику потом спросить, про что она на самом деле."
    "Уф, наконец-то приглушили эти дурацкие софиты. А то ведь так и ослепнуть недолго. Ряды погрузились в приятный полумрак."
    "Следующие несколько номеров мне запомнились слабо. Может быть из за того, что после песни Мику, любая самодеятельность воспринималась как нечто смутно-невнятное?"
    "Дуэт незнакомых девчонок, поющих мимо нот. Медведь похоже им по ушам изрядно потоптался. {w}Какая-то Саша Баканова с детскими стихами про сыр. {w}Шурик, играющий на губной гармошке песню крокодила Гены. Я и не знал, что он умеет. {w}Уже знакомый мне взъерошенный пацан с красными глазами, играющий на скрипке. Неожиданно хорошо."
    "Славя сидела преступно близко ко мне и с каждой минутой прижималась всё плотнее. Мне ведь это не показалось? И вожатой ведь не боится."
    "Опа, а где же вожатая?"
    "Обернувшись в другую сторону, я обнаружил, что Ольги и след простыл."
    dreamgirl "Ага. Вот так мы значит следим за пионерами. Ну что же, вожатым тоже надо отдыхать. А то Саныч наверное заждался уже."
    "Ну что же, раз вожатой нет… То у меня есть кое какие мысли по поводу дальнейшего времяпрепровождения. Тем более, что кое кто явно не против."
    dreamgirl "Бьёт копытом, землю роет молодой сперматозоид."
    th "А ты мне здесь не пошли. У меня, может быть, исключительно чистые намерения."
    dreamgirl "Ага, с исключительно грязными последствиями."
    "Но попытавшись обнять Славю, я получил решительный, хоть и мягкий отпор."
    show sl normal pioneer with dissolve
    sl "Сём, давай не здесь."
    "Мягко попросила девочка, убирая мою руку со своей спины."
    sl "Люди же кругом."
    hide sl with dissolve
    "Ох уж эта женская логика! Прижиматься до состояния диффузии значит можно у всех на виду. А руки распускать ни-ни. Ну ладно, подождём. Ещё не вечер."
    "На лагерь опустилась такая стремительная и густая темнота, которая возможна только в южных широтах.  Моё внимание привлекло какое-то шевеление в ближайших кустах."
    "Присмотревшись и заметив подозрительно знакомые уши, я похолодел. Юля! Заметят ведь! Хорошо, что Ольги рядом нет. С её проницательностью, она бы точно запалила контору."
    "Позабыв обо всём на свете, кошкодевочка почти полностью высунулась из кустов и, упиваясь зрелищем, казалось вся была там, на сцене."
    "Чем она там так увлечена? Я не поверил своим глазам, увидев на сцене того, кого меньше всего можно было заподозрить в любви к музыке и массовым мероприятиям, в частности. Ну разве что, исключая круглосуточный приём пищи."
    "Да-да, на сцене отжигал тот самый незнакомый мужик из столовой! Он играл на балалайке, закрыв глаза и полностью отдаваясь процессу. Красота музыки была такова, что я восторженно поинтересовался у соседки:"
    show sl smile pioneer with dissolve
    me "Славь, а что же это за музыкант такой замечательный?"
    sl "А, это Анатолий. Ты его в столовой наверняка видел."
    me "Видеть-то видел. Я не думал даже, что он разговаривать нормально умеет, не то, что так играть."
    sl "Я и сама, честно признаться, не ожидала от него такой мастерской игры. У него, похоже, много скрытых талантов."
    show sl smile2 pioneer with dspr
    "Славя улыбнулась, видимо тоже наслаждаясь струнными переборами."
    hide sl with dissolve
    "Толян закончил с переборами и перешёл к главной части. Зазвучали знакомые аккорды «Яблочка». Что он творил с инструментом, невозможно описать. Это была не просто игра. Это было сложнейшее виртуозное исполнение вкупе с танцем."
    "Толик подпрыгивал и ходил по сцене вприсядку, и всё это не прерывая игры. Он практически жонглировал балалайкой, а под конец забрался на стол и закончил своё выступление там. Вот это да! Удивил так удивил."
    play sound sfx_concert_applause
    "Не сдержавшись, я поднялся вместе со всеми, чтобы поаплодировать виртуозу."
    tl_7dl "А Ф И Ф О   Ф А  Ф Н И М А И Е." # Спасибо за внимание, но всё-равно не понятно. -R #Коверкание - это перебор, кмк - Ленофаг
    "Хорошо, что все отвлеклись на Толяна и Юлю никто не заметил. Но теперь, когда номер закончился, я потихоньку стал подавать ей знаки – мол, спрячься. Юля понятливо кивнула и снова скрылась в кустах. Не слишком, впрочем, глубоко."
    play sound sfx_wind_gust
    "Откуда-то внезапно налетел порыв ветра и слегка похолодало. Подняв глаза к небу, я увидел довольно густые тучи, грозящие сорвать нам всё мероприятие. Хоть бы дождя что ли не было. Я ведь только во вкус начал входить. Объявили небольшой перерыв."
    show mt normal pioneer with dissolve
    "Невероятным образом материализовавшаяся рядом Ольга Дмитриевна толкнула меня в бок локтём и протянула какой-то свёрток."
    mt "На, питайся. И девочку свою не забудь угостить. Я и на неё тоже брала."
    me "Ка… кую девочку?"
    th "Неужели Юлю заметила!?"
    mt "Да вот же, справа от тебя сидит!"
    "Рассмеялась вожатая, кивнув на Славю."
    "Я перевёл дух. Так и инфаркт схватить недолго."
    me "Да она не моя девочка…"
    mt "Вижу-вижу. Вон как прижимаешься."
    "Славя тут же поспешила отодвинуться."
    show sl angry pioneer at left
    show mt laugh pioneer at right 
    with dissolve
    sl "Ольга Дмитриевна!"
    "Видно было, что Славя сильно смущена."
    mt "Ладно- ладно, молчу."
    mt "Ну вы тут наслаждайтесь концертом и дальше, а мне по делам отойти надо."
    show sl normal pioneer close at left
    hide mt
    with dissolve
    "Всё ещё посмеиваясь, она удалилась."
    "Я развернул свёрток и с наслаждением втянул свежий запах сдобы. Свежие булки, класс!"
    "Тут же в соседних кустах раздалось шуршание и я, громче, чем было нужно, сказал Славе:"
    me "Славя, угощайся, пожалуйста!"
    show sl smile pioneer close at left with dissolve
    sl "Спасибо."
    "Улыбнулась девочка."
    hide sl with dissolve
    "Надо эти шанежки побыстрее употребить, чтобы у кое кого соблазна не было. Уминая одну за другой ароматные булки, я мог бы поклясться, что слышу урчание. Причём очень близко."
    "Похоже дождь всё-таки решил не портить нам концерт и благополучно прошёл мимо. Продолжаем."
    "На сцену вышел Электроник с гитарой. Ничего себе. Оказывается, оба кибернетика ещё и музыканты. А я думал они в своей электронике погрязли. А им ничто человеческое тоже не чуждо. Хотя собственно гитара-то электро, так что закон жанра не нарушен."
    "В ночной тишине полились мелодичные звуки и Электроник запел. Чуть хриплый, слегка неуверенный поначалу, но затем набирающий силу голос. А у него неплохой вокал. Сорвав свою порцию оваций, Электроник раскланялся и ушёл. Молодец, Эл!"
    show sl normal pioneer close at left with dissolve
    me "Слушай, Славь, я и не знал, что у нас здесь столько талантов!"
    "Не скрывая восторга, сказал я соседке."
    me "Я ожидал, в лучшем случае, хорошего исполнения от Мику. Ну может от Алисы ещё. А тут ты посмотри – прямо конкурс \"Песня года\" какая-то."
    show sl laugh pioneer close at left with dspr
    "Славя рассмеялась."
    sl "Как ты низко нас ценишь. А я тебе говорила, что ты ещё ничего не знаешь о лагере."
    sl "И тебе предстоит узнать ещё больше."
    "С намёком продолжила она."
    me "Ну в этом я не сомневаюсь."
    show sl smile2 pioneer close at left with dspr
    "В тон ей ответил я."
    me "Буду ждать с нетерпением."
    hide sl with dissolve
    "Ну раз у нас так всё хорошо складывается… Попробовать ещё раз?"
    "И я снова попытался обнять девочку. Хвала рандому, в этот раз она не стала убирать руку и только лукаво посмотрела мне в глаза. Я почувствовал, что краснею. Ну если по мордасам сразу не получил, значит всё в порядке."
    "Украдкой я посмотрел в сторону кустов – вроде всё тихо. Если присмотреться, то уши-то видны конечно. Но к счастью, никому в голову не придёт пялиться в кусты, а не на сцену."
    "На сцене гитарный дуэт Мику с Алисой. Ну за этих переживать вообще смысла нет. Ожидаемо - исполнение по высшему разряду. Вокал Мику отлично дополнялся струнными переборами двух гитар. А песня на этот раз звучала на английском."
    show sl normal pioneer close at left with dissolve
    sl "Сём, а это про что?" 
    "Всё-таки хорошо знать несколько языков. Ну или хотя бы больше, чем один. Слегка поглаживая девочку по спине, я стал объяснять."
    me "Песня называется «Рядом с тобой». Она естественно о чувствах. Чувствах девушки к молодому человеку. Эта девушка хочет всё своё время проводить рядом с ним. Что-то там об ангелах, птицах и звёздах."
    sl "Как романтично…"
    "Прошептала Славя."
    sl "И какая красивая песня."
    play sound sfx_concert_applause
    "Ожидаемо получив шквал аплодисментов, девочки удалились."
    "Славя мягко освободилась от моей руки, по прежнему обнимающей её за плечи."
    sl "Сём, мне надо на сцену, готовиться. Сейчас ещё один номер будет, а потом и мне выступать."
    "С сожалением я выпустил её руку."
    show sl smile pioneer at center with dissolve
    sl "Ты тут не скучай без меня. И похлопать не забудь."
    me "Я уверен, что ты затмишь всех сегодня."
    show sl laugh pioneer at center with dspr
    sl "Не сглазь, смотри."
    "Рассмеялась Славя."
    "Очаровательная улыбка у неё, всё-таки."
    hide sl with dissolve
    "Что это у нас сегодня одна заграница среди музыкантов. Неужели никто по нашей эстраде-то и не пройдётся? А, ну вот, кажется что-то русское народное намечается."
    "На сцену выбежали ребята из второго отряда народных костюмах и принялись долбить по сцене сапогами, видимо изображая таким образом танец. Ну что же, для любительского исполнения вполне, вполне. Не ансамбль Александрова конечно, но для лагеря сойдёт."
    "Ага, вот и наша звёздочка. Для своего выступления Славя надела какой-то совершенно сногсшибательный голубой сарафан с народным орнаментом и сидел он на ней, надо сказать просто м-м-м – пальчики оближешь."
    "Я думал, что после всех этих отличных выступлений, меня уже ничто не способно удивить, но когда Славя начала петь, понял, что ошибался. Её глубокий, невероятный по красоте и силе голос заполнил всё вокруг. Казалось, ей даже не нужен был микрофон; её услышали бы и так в любом уголке лагеря."
    show mt normal pioneer at right with dissolve
    mt "Какой голос, а?"
    "Вожатая снова здесь. И снова незаметно. Похоже у Ульянки уроки скрытности берёт."
    me "Ага."
    "Восторженно кивнул я."
    me "А где вы были, Ольга Дмитриевна?"
    show mt angry pioneer at right with dspr
    mt "А вот это уже не твоё дело."
    "Нахмурилась вожатая."
    me "Ладно, ладно, я просто так спросил."
    play sound sfx_concert_applause
    "И я поднялся, чтобы поаплодировать, без сомнения лучшему номеру сегодняшнего концерта. Ну и разумеется, его исполнительнице."
    show sl normal pioneer
    show mt normal pioneer at right behind sl
    with dissolve
    "Подбежала слегка запыхавшаяся Славя."
    sl "Ну как я выступила?"
    "Явно волнуясь, спросила она."
    me "Ты была просто неподражаема."
    "Совершенно искренне ответил я."
    me "Это самое прекрасное, из всего, что я слышал."
    show sl smile2 pioneer with dspr
    sl "Спасибо, Сём."
    "Зарделась девочка."
    show mt laugh pioneer at right with dspr
    mt "Эй, голубки."
    "В разговор вмешалась  вожатая, всё это время стоящая рядом и наблюдающая за происходящим."
    mt "Не забудьте, вам после концерта ещё аппаратуру на место определить надо."
    sl "Конечно, конечно, Ольга Дмитриевна. Не волнуйтесь, мы с Семёном всё сделаем. Правда, Сём?"
    "Я кивнул головой."
    mt "Ну вот и хорошо. Тогда я пойду заключительную часть проведу."
    hide mt with dissolve
    "И вот ряды лавочек опустели, стихла музыка и о том, что здесь только что в течение двух часов проходил концерт (надо сказать, довольно хороший), напоминала только пустая сцена и куча аппаратуры, которую нам предстояло транспортировать."
    "Часть в клуб, а часть на площадь, для вечерних танцулек. И пульт диджейский ещё надо не забыть."
    
    #####################################################################################################
    # TODO: все в код!
    Где бы ещё силы взять для всего этого ? Мы с Электроником, который тоже остался, чтобы помочь нам, переглянулись и одновременно вздохнули. Опять таскания.
    Но к счастью, в этот раз нам не пришлось особо напрягаться. Мику внезапно вспомнила, что и у колонок, и у усилителя ОКАЗЫВАЕТСЯ есть выдвигающиеся колёсики. Так какого чёрта ты молчала об этом раньше !?
    С: -Мику, дорогая, почему же ты не сказала нам об этом раньше?
    Поинтересовался я у зеленоволосой болтушки.
    М: -Да я забыла, представляешь! Пустая голова.
    Слегка виновато ответила певичка, постучав себя по макушке.
    М: -Вы извините меня, ребята. Надеюсь, вам было не очень тяжело?
    С: -Разве что самую малость.
    За такой голос ей можно простить некоторую рассеянность.
    Теперь, когда мы узнали секрет транспортировки, дело пошло гораздо быстрее и веселее. Пока мы поочерёдно возили и расставляли на площадь аппаратуру, Мику сбегала в музыкальный клуб за своим величайшим сокровищем – диджейским пультом.
    Электроник убежал на ужин. Славя собралась идти вслед за ним.
    Сл: –Сём, ты идёшь?
    С:- Сейчас!
    Сл: -Ладно, пойду пока нам места займу.
    Я подошёл рассмотреть пульт поближе. Красота! Настоящий профессиональный диджейский микшерный пульт со множеством переключателей, лампочек и крутилок. Made in Japan, сразу видно. В обычном советском пионерском лагере о таком могли бы только мечтать, понятное дело.
    С: -Это наверное твой личный?
    М: - Да, я с ним выступаю. Настраиваю всё сама. Правильная настройка очень важна.
    Ответила Мику, уже в наушниках, вовсю колдующая над пультом.
    С: -Ты на ужин сходила бы. А то ещё долго дискач вести.
    М:- Тогда могу не успеть. Ребята вон уже некоторые пришли. Что же, они меня ждать будут?
    В самом деле, несмотря на то, что до дискотеки оставалось ещё порядочно времени, на площадь уже начали подтягиваться особо нетерпеливые пионеры. Да оно и понятно: приличных развлечений в лагере – кот наплакал.
    М: -Так что я потом. А если и не поем – ничего страшного. Нам, девочкам, надо фигуру беречь.
    М: -А ты иди, иди, Сёмочка.
    С милой улыбкой продолжила Мику.
    М:- А то тебя Славя заждалась уже.
    В самом деле.
# ужин
    Славя, сидевшая в опустевшей столовой, хоть и улыбалась, но выглядела слегка недовольной. На столе два полных подноса. Видно не ела ещё, меня ждала. Блин, не хватало мне ещё всё завалить в последний момент!
    С: -Славь, прости-прости !
    С ходу начал я и лёгкая тень недовольства покинула чистый лик девочки.
    С:- Виноват, оправдаю, исправлюсь. Просто мне интересно было на диджейский пульт Мику посмотреть.
    Сл: -Ладно, ешь садись.
    Я не заставил себя упрашивать. С того момента, когда вожатая приносила булочки на концерт, прошло уже порядочно времени и я был голоден как волк.
    Сл: -Чего это тебя так пульт заинтересовал? Готовишься стать профессиональным музыкантом?
    С: Да не то, чтобы. Просто всякими техническими новинками интересуюсь.
    Ответил я, умолчав, что этой «технической новинке» в моём времени самое место в музее.    
    
    Наскоро разделавшись с ужином, мы поспешили на площадь, где уже всё было готово к дрыгоножеству и рукомашеству. Мику в наушниках священнодействовала за пультом. Вожатая вещала в микрофон что-то о прощальном вечере.
# концерт
    Мы со Славей подошли к ней. Ольга отложила микрофон в сторону.
    ОД: -Пришли наконец. Развлекайтесь, ребята, сегодня прощальная дискотека. Повеселитесь как следует. Пусть эта смена запомнится вам.
    Ш: «Да уж запомнится, как без этого. Одна Юлечка чего стоит»
    С: «Вот не надо сейчас о ней. У меня Славя вообще-то есть. И, судя по всему, у нас дело на мази»
    Ш: «А ты и хвост распустил. Посмотрим, как ты это дело провернёшь»
    С: «Ты будешь первым, кто узнает – как именно»
    Сл: -Сём, пойдём прогуляемся.
    Славя схватила меня за руку и повела в сторону от светящихся гирляндами деревьев и постепенно затихающей музыки.
    Нетерпеливая девочка, всё время ускоряя шаг, буквально вихрем протащила меня по лагерю. Мы почти бегом прошагали мимо всех домиков, позади остались Клубы и, наконец, показались ворота лагеря.
    С: -Эй-эй ! А нам обязательно было так бежать ?
    Осведомился я, переводя дыхание и прислоняясь к статуе пионера.
    Сл: -Да в общем-то нет.
    Улыбнулась Славя.
    Сл: -Я просто не хотела, чтобы ты передумал. А то кто тебя знает – взял бы и остался. А девочек много вокруг красивых – уведут ещё. Или всё же хотел потанцевать ?
    С: -Да не собирался я. Разве что исключительно с тобой.
    Славя молча и слегка задумчиво улыбнулась в ответ на мой комплимент. Казалось она о чём-то напряжённо размышляет. Я тоже не знал, как продолжить разговор и стоял молча.
    Спасите меня кто-нибудь из этой дурацкой ситуации. Ведь я сейчас всё испорчу. Славя просто обидится и уйдёт ! А я за столько лет своего затворничества совершенно забыл, как надо общаться с девушками по настоящему.
    И тут в разговор вмешалась Шиза.
    Ш: «Ну и чего ты застыл, как истукан? Давай, решайся уже на что-нибудь ! Понятно ведь, что девочка ждёт от тебя решительных действий. Кто мужчина здесь, в конце концов ? Обними, поцелуй её. Эх, будь у меня физическое тело !»
    Это призыв подействовал на меня, как удар электрическим током. Я отбросил все сомнения, подошёл к Славе, обнял её и попытался поцеловать..
    ТРАХ !! Вечер внезапно перестал быть томным. Щёку обожгло, а в голове зазвенело. Я отшатнулся и, чтобы не упасть, был вынужден опереться на ближайшее дерево. Я помотал головой - в глазах всё ещё плясали разноцветные звёздочки.
    Сл: - Дурак! Я тебя не за этим сюда позвала !
    Сама дура ! А зачем же тогда, чёрт побери ?! #(это не прямая речь, а мысли Семёна)
    Славя виновато смотрела на меня.
    Сл: -Слушай, Сём, тебе очень больно ? Ты извини, у меня рефлекс сработал.
    С: -Славь, если я слишком спешу, ты могла бы просто сказать об этом, без рукоприкладства.
    Потирая щёку, мрачно ответил я.
    Сл: -Извини. Я в самом деле не ожидала, что ты так решительно в бой ринешься.
    Славя силилась улыбнуться. Несмотря на весь драматизм ситуации, я не мог не улыбнуться в ответ. Правда улыбка вышла довольно кривенькой. Ну а я-то – набросился на девочку, как сексуальный маньяк какой. Она ведь явно шокирована моим поведением. Тихоня тихоней, а тут на тебе.
    Ш: «Да, брат. Чего-то мы тут с тобой не додумали»
    Почесала в затылке Шиза.
    С: «Не мы, а ты»
    Ш: «Да маньяк-то ты, а не я. У меня вот и тела даже нет. А из тебя и маньяк так себе - нифига не сексуальный. А какой напор, какая грация. Кстати можно ещё раз попробовать – а ну как повезёт ? Вот будешь знать в другой раз, как девок обжимать по углам»
    С: «Что ?? Да кто меня подстрекал-то ?..»
    Ш: «А ты меня слушай больше. Кстати, можешь утешиться тем, что легко отделался. А то знаешь, какие случаи бывают..»
    Да не отделался ещё.. И как мне теперь вести себя со Славей ?
    Девочка похоже взяла себя в руки и теперь полностью контролировала ситуацию. Ну или почти.
    Сл: -Семён. На самом деле, мне нужно было поговорить с тобой наедине. Подальше от чужих ушей.
    Её сухой деловой тон настолько контрастировал с недавним поведением, что я растерялся.
    С: -Что ? Просто поговорить.. ?
    Сл: -Да, поговорить. Нам нужно обсудить очень важные вещи.
    С: -Да, это я уже слышал. Но я подумал..
    Сл: -Прости меня, если я ненамеренно ввела тебя в заблуждение, относительно моего к тебе отношения. Мне было приятно твоё внимание, не скрою. Но мой интерес к тебе сугубо профессиональный. Ну почти.
    Всё же подсластила пилюлю.
    Моё разочарование казалось можно было ощутить физически. Вот тебе и Очень Важный Разговор.
    С: -Профессиональный интерес ? Это в какой же области ? Может быть ты психолог ? Изучаешь редкие виды Семёнов ?
    Сл: -Семён, ты не обижайся только. Сначала я и правда хотела просто получить от тебя информацию. Она очень важная, в том числе и для меня лично; и касается твоего будущего тоже. Но потом..
    Тут она улыбнулась.
    Сл: -ты стал мне и самом деле симпатичен. Так что, если у нас в дальнейшем всё сложится хорошо, то мы можем попробовать.
    С: -Что попробовать ?
    Славя кивнула головой.
    Сл: -Что-нибудь ещё.
    Я усмехнулся. Вместо синицы в непосредственной близости, мне предлагают журавля в долгосрочной перспективе. Да ещё и с какими-то намёками таинственными. Ну что же, выбора у меня похоже особого и нет..
    Что меня ждёт после окончания этой волшебной, загадочной, мистической смены ? Я просто испарюсь из автобуса ? Или даже из кровати ? А потом проснусь у себя дома ? А может и вообще нигде не проснусь. Распылюсь на атомы и буду вечно летать над нашей голубой планетой, создавая помехи в эфире.
    А здесь Славя, судя по всему, владеет какой-то информацией. Готова обменяться ей, взамен на.. не знаю что. Да и что я такого знаю, в самом деле ? Вряд ли ей пригодится знание того, что я помню имена всех пилотов Евангелиона, или как набрать секретный код Конами с закрытыми глазами.
    Хотя я лукавлю, конечно. На правах пришельца из будущего, я могу рассказать много интересного о своём мире миру этому. Но что об этом может знать Славя ? А самое интересное – откуда ? Надо проявить осторожность.
    Ш: «Да-да, брат, ты поосторожнее. А то сдадут тебя на опыты и будешь до конца своих дней сидеть в белой комнате, сдавать анализы и решать тесты на сообразительность»
    C: -Ладно, я так понимаю, дальнейшая беседа пойдёт не о делах амурных.
    Сл: -Точно. Не знаю даже с чего начать..
    Замялась девочка.
    С: -Начни сначала.
    Поощрил я её.
    Сл: -Ну что же.. Слушай тогда.
    Славя начала свой рассказ и чем больше она рассказывала, тем больше я офигевал.
    Сл: -Я расскажу тебе краткую предысторию, чтобы ты лучше понял мою мысль.
    Сл: -Благодаря многолетним исследованиям советских и зарубежных учёных, такое понятие как «параллельные вселенные» стало уже практически доказанным фактом.
    Сл: -Разумеется, все подобные данные держатся в строжайшей секретности. Но утечки всё же случаются, из за всяких непредвиденных обстоятельств. Например, появление людей, утверждающих, что они прибыли из другого мира, разговаривающих на незнакомом языке, одетых в странную одежду. Думаю, ты наверняка слышал, или читал что-то подобное.
    Сл: -Притом, хоть и ведут они себя странно, они совершенно нормальны, с точки зрения психиатрии. Просто они и самом деле пришельцы из другого мира. Вот как ты, например.
    С: -Славь, ты бы сейчас видела себя со стороны.. Что ты несёшь ?
    Сл: -Спокойно, я уже подхожу к сути. Так вот, к нашей ситуации эта теория о параллельных мирах не имеет никакого отношения. Правда в том, что этого мира на самом деле не существует. Вернее он существует, но только благодаря тебе.
    Сл: -Реален только твой мир. Этот же мир существует, пока ты проецируешь его в своей голове. Здесь всё выдуманное. Тобой.
    Сл: - Это даже не полноценный мир, а вырванный кусок реальности на отдельно взятом отрезке пространства-времени. Этот лагерь, пионеры. Всё это ненастоящее. За пределами лагеря не существует ничего. Кажется ты уже пробовал убежать отсюда в первый день. Ну как, получилось у тебя ?
    С: -Откуда ты знаешь ?!
    Сл: -Неважно. Ты находишься в выдуманном тобой иллюзорном мире. А для твоего подсознания он параллельный. Возможно ты на подсознательном уровне захотел что-то изменить. Я не знаю, что послужило этому причиной. Возможно сильное эмоциональное потрясение, потеря близкого человека, простая неудовлетворённость текущей жизненной ситуацией.
    Сл: -Но желание создать свой собственный мир со своими правилами было очень велико и вот ты здесь. Идеальный мир, идеальный лагерь, идеальные пионеры..
    Тут она сорвалась на крик.
    Сл: -Ты всё это придумал ! И меня тоже !
    Она закрыла лицо руками и заплакала. Я в смятении смотрел на неё, не зная, как реагировать на это заявление.
    С: -Да кто я по твоему – Господь Бог ?!
    Ш: «Падите ниц, жалкие черви ! Иначе величие Семёна Всемогущего испепелит вас!»
    Сл: -Я не знаю, кто ты такой. Я не знаю, кто я такая.
    Всхлипывая, ответила девочка.
    Сл: -Но я знаю, что как только ты исчезнешь отсюда, то исчезну и я тоже.
    Да, такую забористую информацию не так-то просто уложить в моём невеликом умишке.
    С: -Послушай, Славя.
    Медленно начал я.
    С: -Прежде всего – с чего ты это всё взяла ? Откуда такая информация ? Что за бред ? Кошмар приснился ? Книжек фантастических начиталась ?
    Девочка немного успокоилась.
    Сл:- Нет, так получилось, что я случайно подслушала разговор осведомлённых людей. Я не буду их называть, это неважно. Но там много интересного было. О тебе очень много.
    С: -Чего ? Обо мне ? А кому какое до меня может быть дело ?!
    Сл: -А ты думал, никто ничего не заметил ?
    Славя прищурилась.
    Сл: -Твою одежду не по сезону, твои вещи, твоё поведение.
    Сл: -Если ты так думаешь, то очень сильно ошибаешься.
    Сл: -Но вообще, просто не забивай себе голову проблемами мира иллюзорного. Подумай лучше о мире настоящем. О том, что тебе пора бы уже вернуться в него.
    Тут она бросилась ко мне и крепко обняла.
    Сл: -И забери меня с собой, пожалуйста !
    Да, Славя явно знает, о чём говорит. И отпираться мне уже теперь, судя по всему.. бессмысленно ? Да, именно так – бессмысленно. В принципе, я уже ожидал чего-то подобного. Особенно после такой эмоциональной сцены.
    С: -Да куда я тебя заберу-то ?
    Пробормотал я, тщетно делая попытки высвободиться.
    Ш: «Сомневаешься? И правильно делаешь. Я для неё никакой перспективы здесь не вижу. Бредовая теория и бредовая попытка. Не заберёшь ты её с собой, даже если очень захочешь»
    Сл: -С собой забери меня, в свой мир. Выпусти меня в РЕАЛЬНОСТЬ.
    Ответила Славя, умоляюще глядя мне прямо в глаза.
    Её лицо было очень близко от моего. Чувственные губы манили взгляд.
    Не, ну это уже запрещённый приём ! Я отвёл глаза в сторону, чтобы немного успокоить некоторые реакции моего организма. Помогло правда не очень.
    С: -Ну допустим, я бы захотел вернуться. Что мне для этого нужно сделать ?
    Сл: -А вот это как раз очень просто. Нужно просто захотеть вернуться. Очень сильно захотеть.
    С: -А ты как со мной сможешь уйти ?
    Сл: -Тебе нужно думать и обо мне тоже. Тогда мы вернёмся вместе.
    С: -Славя, ты понимаешь, что ты очень сильно рискуешь ? Не говоря уже о полной бредовости этой затеи, ты ведь оставляешь всё, что тебе близко и знакомо. Если, ЕСЛИ всё получится – то что ты будешь делать в моём мире ?
    Сл: -Сейчас главное, чтобы ты вытащил нас отсюда. И как можно скорее. Я не знаю, что произойдёт после окончания этого дня. Скорее всего я просто исчезну. А я не хочу ! Я хочу жить !
    В принципе, вернуться домой было бы неплохой идеей. Я чувствовал, что слегка подустал от этой чересчур идеальной пионерской романтики. Хотелось вернуться в свою знакомую берлогу, за свой компьютер, к своим, хоть и монотонным, но таким спокойным дням.
    Это был неплохой отпуск, но видно пришло время сдавать ключи от номера. И кажется вернусь я домой не только с новыми силами и отдохнувший, но и с приятным бонусом. В виде Слави.
    Ш: «В багаж сдашь, или ручной кладью провезём ?»
    С: «Голубиной почтой. Не мешай, я думаю»
    Ш: «А, ну думай, думай. Мыслитель»
    Славя продолжала с надеждой смотреть на меня.
    Внезапно сзади затрещали кусты и на нас выскочила взъерошенная Юля !
    Славя мгновенье смотрела на неё, открыв рот, а потом взвизгнула и спряталась за меня.
    Ю: -Семён, не верь ей ! Она всё неправильно говорит. Лагерь настоящий. И люди настоящие. И я тоже настоящая !
    Сл: -Сёма, кто это ?
    Опасливо спросила Славя, выглядывая у меня из за спины.
    С: -Ну..это Юля.
    Не придумал ничего более умного я.
    Сл: -Ты её знаешь ? О чём она говорит ?
    С: - Ну можно сказать, что знаю. И похоже она не согласна с тобой насчёт того, что этот мир ненастоящий. Для неё он самый что ни на есть настоящий.
    Ю: -Конечно настоящий ! Я ведь здесь живу, значит он точно настоящий.
    Безупречная логика.
    С: -Значит ты всё слышала. И почему ты так уверена в том, что тут всё взаправду ? Вдруг я и тебя выдумал тоже ?
    Юля насупилась.
    Ю: - Никто меня не выдумывал. Я всегда здесь была. Я точно знаю. И вот эта –
    Она показала пальцем на Славю.
    Ю: - ошибается. Лагерь всегда есть. Даже когда тебя не было, он всё равное был.
    Славя наконец отважилась выйти из за меня.
    Сл: -Во первых, я не «эта». Меня зовут Славяна. Но все зовут меня Славя. И ты тоже зови.
    Ю: -Ладно. Я Юля.
    Сл: -Что ты знаешь о лагере ?
    Ю: -Знаю, что лагерь всегда есть. И когда тепло и людей много. И когда холодно и всё белое, а людей нету. Я тогда сплю много.
    Ю: -А за лагерем нету ничего. Никто не приходит в него и никто не уходит из него. Люди просто появляются и исчезают. И это всегда повторяется. Но они не помнят ничего.
    Славя задумалась.
    Сл: - Да, я смутно помню свою жизнь вне этого лагеря. И это очень странно.
    Сл: -Но кто же ты ? Почему ты всё помнишь ? Ты тоже из другого мира ?
    Ю: - Я не знаю. Я всегда тут была. Люди боятся меня, когда я показываюсь. Кричат. Убегают.
    Ю: - Иногда приходят такие как Семён. Они другие. Они могут помнить. Они не боятся. Я таких во сне иногда вижу, перед тем, как они появляются.
    И тут я снова вспомнил своё видение: девочка, задающая такой просто и такой сложный вопрос – «ты пойдёшь со мной ?» Все кусочки мозаики наконец сложились в единую картину. Я дал своё согласие и Юля перебросила меня в этот лагерь. Как и зачем – совершенно непонятно.
    Славя отвела меня в сторону.
    Сл: -Семён, нам нужно каким-то образом поймать эту… это существо и заставить её вернуть нас в реальный мир.
    Очень тихо прошептала она.
    Сл: -Я уверена, что она каким-то образом связана с этими перемещениями.
    Юля обладала очень тонким слухом.
    Ю: -Не советую. Я кусаться могу. И царапаться. Ты уже пробовала один раз. Ещё хочешь ?
    Сл: Что ?! Я пробовала поймать тебя?
    Ю: -Пробовала. Но ты не помнишь. А я помню. И предупреждаю тебя – будет плохо. Как в прошлый раз.
    Ну вот и приехали. Все хвосты подобраны, все мосты сожжены, Рубикон перейдён. Назад дороги нет.
    Что делать-то ? Где мой внутренний голос, когда он так нужен ?
    Ш: «Да здесь я»
    Очень спокойно и даже как-то лениво отозвалась Шиза.
    Ш: «Что ты хочешь, чтобы я сделал..сделала..сделало ? В общем неважно. Чего надо-то тебе, короче ?»
    С: «Совет нужен, вестимо. Я совершенно запутался и не знаю, что делать»
    Ш: «А какой тут совет тебе может быть ? Вариантов немного – верить или не верить, третьего не дано. Веришь – лови Юлю и катапультируйся. Не веришь – лови Славю и тащи её к вожатой, или доктору.
    menu:
        "К вожатой" if not alt_uvao_true:
            # TODO: текст и jump
        "К Виоле" if alt_uvao_true:
            # TODO: текст и jump
        "Поймать Юлю!":
            pass
    Славя крепко взяла меня за руку и в который раз уже за сегодня заглянула прямо в глаза. В её взгляде читалось: «я буду с тобой, чтобы ни случилось, просто дай мне шанс». И вдруг внезапно я ощутил решимость и поддержку, подобной которой не ощущал уже много лет.
    Наверное с тех самых пор, когда съехал от родителей, в поисках самостоятельности, сразу после окончания школы. Причина конечно была самая банальнейшая - вечная проблема отцов и детей. Надоели постоянные придирки и упрёки. Я просто собрал свои немногочисленные вещи и переехал на съёмную квартиру.
    Ничего у меня, конечно, не вышло – я ничего не добился и ничего не достиг. У меня не получилось даже окончить институт. Единственный, сомнительный в моём случае, плюс – самостоятельность и независимость. Но, как оказалось, я даже не был способен быть самостоятельным.
    Были разрушены и разбиты в прах жестокие иллюзии - мир вовсе не готов был восторженно принять Семёна Персунова. Никто не стремился помогать мне адаптироваться. Я не был никому нужен со своими проблемами.
    Рядом со мной не было никого, кто бы подставил дружеское плечо и протянул руку помощи в трудную минуту. А потом существование такого человека вообще перестало быть критичным.
    Не сразу, но я научился обходиться без посторонней помощи, а в дальнейшем, и вовсе старательно абстрагироваться от любой попытки влезть в мою жизнь.
    Но вот теперь, рядом со мной человек, который говорит: «я тот, кто тебе был нужен все эти годы». Человек, готовый рискнуть разделить со мной все тяготы моего бесцельного существования.
    Пусть и не совсем бескорыстно. Но ведь альтруизм в чистом виде встречается только в сказках, правда ? И как я могу оттолкнуть эту девочку, готовую пойти вместе со мной на сделку с неизвестностью ? Готовую рискнуть ради меня самим своим существованием ?
    И пусть я не знаю, что случится в дальнейшем. Но раз Славя готова рискнуть, то и я тоже. Решено – мы сбежим из этого лагеря вместе. А поможет нам в этом Юля. Хочет она этого, или нет.
    Переглянувшись со Славей, мы начали обходить Юлю с двух сторон. Девочка-кошка страшно зашипела, шерсть встала дыбом, а глаза загорелись. Хвост ходил ходуном. Вид у неё был поистине дьявольский я даже на секунду засомневался в адекватности нашей затеи. Но времени на раздумья больше не было.
    Сл: -Семён, давай !
    Отчаянно крикнула Славя и мы одновременно бросились на Юлю. Но не успели даже коснуться – сверкнула ярчайшая вспышка света, нас отбросило в разные стороны и сознание померкло. 
    if alt_uvao_D5_hentai:
        jump alt_uvao_enving_neutral_bad
    else:
        jump alt_uvao_enving_neutral