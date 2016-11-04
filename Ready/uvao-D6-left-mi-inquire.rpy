# Д6-левая ветка, расспросы Мику о Лене.
# Черновик текста
#
# !!!НЕ!!! Использует флаг отказа Мику на пляже в Д2 alt_day2_mi_rejected
# ЛБ: далее фрагменты с использованием alt_day2_mi_rejected убрать совсем, если только Автор не изменит ещё раз условия для входа на рут. Быть может, заменить на alt_day3_dancing == 4 - танцевали с Мику
#
# Использует флаг вступления в кружок музыки alt_day2_club_join_musc
# Использует флаг девочки-фаворитки в Д2 alt_day2_rendezvous ( == 3 - Алиса)
#
# Устанавливает флаг разговора с Мику о Лене alt_uvao_D6_left_MI_talk
#
label alt_day6_uvao_left_ask_MI_about_UN:
    #Приходим сюда сразу из меню "Поговорить с Мику"
    # сцену не выставляем
# Сборщику - выставляем сцену на время отладки
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 2
# /Сборщику - выставляем сцену на время отладки

    "Решив, что расспросить хорошенько соседку Лены - не такая уж плохая идея, я не стал откладывать дело в долгий ящик."
    "Осторожно заглянув ещё раз в столовую, я убедился, что никого с ультрамариновыми волосами там не наблюдается - похоже, Мику уже успела покончить с обедом и убежала куда-то."
    "В нерешительности я остановился на крыльце."
    th "Ну и где мне теперь её искать?"
    "Впрочем, я довольно быстро пришёл к выводу, что поиски руководителя музыкального кружка надо начинать - правильно, с помещения этого самого кружка!"
    dreamgirl "Гениально! Почтеннейшая публика, перед нами блестящий образец многоуровневого логического постороения! Аплодисменты, пожалуйста!"
    th "Да-да, спасибо, я весьма польщён!"
    "Не стал скромничать я и потопал через пол-лагеря к музыкальному клубу настолько быстро, насколько это позволял мне только что съеденный обед."
# сцена - муз.клуб снаружи днём.
    "Мне повезло - не успел я подняться на крыльцо, как внутри что-то с грохотом обрушилось, а через секунду на крыльцо выскочила Мику."
    # show mi sad
    "Увидев меня, она прямо-таки просияла:"
    # show mi happy
    mi "Ой, Семочка, как хорошо, что ты пришёл! Я уже прямо-таки и не знала, что делать!"
    "Она схватила меня за руку и, не давая опомниться, потащила за собой внутрь, тараторя на ходу."
# сцена - муз.клуб изнутри днём.
    mi "Я тебя совсем последнее время не видела, ты где-то всё пропадал. Ты не болел, нет? Хорошо, если не болел, это так обидно, когда все гуляют, а ты болеешь!"
    "Мику на секунду прервалась, чтобы наклониться и попытаться поднять опрокинутый ряд свинченных вместе стульев с откидными сиденьями - похоже, именно они так звучно только что рухнули."
    "Я поспешил сыграть джентельмена и помог ей вернуть стулья в нормальное положение, попутно подивившись тому, как такое хрупкое существо сумело опрокинуть эдакую тяжесть."
    th "Интересно, неужели она так обрадовалась моему приходу только из-за того, что некому было помочь эти стулья поднять?"
#    if alt_day2_mi_rejected: #В Д2 закрутили было с Мику, но на пляже ушли в отказ
#        dreamgirl "А девочка неплохо держится!"
#        th "В каком смысле?"
#        dreamgirl "В том самом - после того, как ты её целый день обхаживал, а потом взял, да и отшил на пляже!"
#        th "Да я не..."
#        dreamgirl "Что \"не-е-е\"? У тебя память отшибло от беготни по туннелям? {w}Девочка тебе доверилась, а ты с ней так обошёлся! Странно, что она вообще с тобой разговаривает после этого."
#        "Одарив напоследок образом захлопывающейся двери, не к месту разлютовавшийся голос временно исчез из моей головы."
    "Мику тем временем тряхнула волосами и продолжила с полуслова:"
    mi "А то концерт уже скоро, а ничего ещё не готово толком! И Славя куда-то запропастилась, я думала, поможет, а она..."
    "Поневоле мне вспомнилась сегодняшняя неловкая сцена на пляже."
    dreamgirl "Ты лучше вспомни, чем эта сцена закончилась."
    # звук удара мяча - как на пляже
    dreamgirl "{b}HEADSHOT!{/b}"
    "Вздрогнув, я обнаружил, что Мику тем временем вовсю продолжает со мной разговаривать:"
    if alt_day2_club_join_musc:
        show mi sad pioneer at cright with dissolve
        mi "...Только ты должен был зайти ко мне в кружок, раз записался! Ну хоть один разок! Мы бы тебе тоже номер какой-нибудь хороший приготовили, а теперь уже времени нет, не успеем никак!"
    show mi smile pioneer at cright with dissolve
    mi "Но так хорошо, что ты сейчас пришёл, ребята не справляются, они стараются, но тут как раз надо отнести..."
    me "Мику, стой!"
    show mi surprise pioneer at cright with dissolve
    "Рявкнул я, пока меня не успели припахать к какому-то Важному Делу. Получилось не слишком вежливо, но зато Мику запнулась посреди своей пулемётной очереди, и я поторопился этим воспользоваться:"
    me "Мику, мне надо с тобой поговорить. Срочно."
    "Девочка с готовностью кивнула и тут же снова открыла было рот, но я немедленно перебил её во второй раз:"
    me "Про Лену."
    "Мику отчего-то замялась и согласилась как-то неуверенно:"
    mi "Ну да, про Лену... Конечно, давай.{w} Только как же усилитель?"
    "Я изумлённо уставился на девочку."
    me "Какой ещё усилитель?"
    mi "Ну так я же говорю - усилитель надо отнести на сцену! Вот же он, вот этот!"
    if (alt_day2_rendezvous == 3):  # В Д2 уже относили этот же усилок на сцену по просьбе Алисы.
        "Она ткнула пальцем в стоящий на полу уже знакомый стальной ящик."
        th "Шо? Опять???"
        th "Я же несколько дней назад уже таскал его туда!"
        dreamgirl "Таскать-то ты таскал, да вот только напрасно - девочка тебе не по зубам оказалась!"
        th "Да не больно-то и хотелось! Эта Двачевская - настоящее извержение вулкана!"
        dreamgirl "Ты ещё скажи, что не по своей воле тогда за ней подволакивался. И сегодня ты с ней обедать сел потому, что очень испугался."
        "С гнусным смешком голос исчез из моей головы." # ЛБ: здесь нет повтора про "голос исчез из головы" с предыдущим ответвлением по alt_day2_mi_rejected - взаимоисключающие флаги.
        "Мику настойчиво подёргала меня за рукав."
    else:
        "Она ткнула пальцем в стоящий на полу стальной ящик, тяжёлый даже на вид."
    mi "Ну Сеееенечка, ну пожаааалуйста! Мне его самой никак не дотащить, а собирать мальчиков из младших отрядов - долго, да и не доверяю я им - разобьют ведь! Если честно, то он просто хлам, усилитель-то, но другого ведь нет! А ты сильный, ты справишься!"
    th "...!"
#    if alt_day2_mi_rejected:
#        "Мику скорчила умилительную рожицу и добавила:"
#    else:
    "Мику вдруг проворно ухватила меня за запястье своими маленькими ручками, скорчила умилительную рожицу и добавила:"
    mi "А по дороге мы с тобой поговорим! Ты ведь хотел про Лену поговорить?"
    th "Надо же, а я-то думал, что у неё в одно ухо влетает, а в другое - вылетает. Похоже, музыканточка-то себе на уме."
#<-    if not alt_day2_mi_rejected:
    "Изо всех сил стараясь делать вид, что прикосновение теплых нежных пальчиков меня нисколько не смутило, я кивнул."
    "Мику немедленно отпустила меня и захлопала в ладоши."
    mi "Ой, Сенечка, какой ты молодец! Я знала, что ты поможешь!"
#->
    "Вздохнув, я кое-как взвалил на себя отчаянно неудобный портативный гроб усилителя, Мику подхватила моток каких-то проводов и распахнула передо мной дверь свободной рукой."
    mi "Пойдём!"
# сцена - муз.клуб снаружи днём.
    "Пока девочка возилась с замком, запирая клуб, я направился было в сторону дорожки, ведущей к площади. Увидем это, Мику замахала руками."
    mi "Нет-нет! Иди за мной, здесь короткий путь есть."
    "Она кивнула на довольно утоптанную тропинку, уводящую в заросли кустов. Секунду посомневавшись, я всё-таки пошёл за Мику, проворчав себе под нос:"
    me "От души надеюсь, что ты не собираешься играть со мной в Сусанина, иначе я так и сгину там вместе с этим сундуком."
# сцена - ближняя тропинка в лесу.
    "Мику звонко рассмеялась - словно серебряные колокольчики прозвенели:"
    mi "Ну что ты, конечно же нет! Хотя опера мне очень понравилась, я ведь не только современную музыку люблю, жаль только, что я её в записи слышала, а не вживую! Зато у вас, наверное, часто её театрах ставят, да?"
    "Следующие несколько минут были полностью посвящены болтовне на тему русской классики."
    "Вернее, болтала Мику, демонстрирующая изрядную осведомлённость в этом вопросе - не иначе, специально готовилась к поездке в Союз. {w}А может, и вправду увлекалась - всякое бывает."
    "Я же лишь поддакивал изредка что-то невнятное, прячась за усилителем. Отчего-то мне неловко было признаваться Мику в степени своей приобщённости к русской музыкальной культуре в целом и к творчеству Глинки - в частности."
    th "И вообще, надо эту музыкальную тематику сворачивать."
    dreamgirl "Ага, пока Мику тебя не раскусила. Небось, и разговаривать-то с тобой потом не захочет, с неучем."
    me "Да, так вот, насчёт Лены."
    "Пропыхтел я из-под усилителя, когда обнаружил, что от Глинки мы уже перешли к Мусоргскому."
    "Мику, будто только этого и ждала, охотно переключилась на новую тему."
    mi "Лена? Ой, Лена - она такая славная! Она, правда, нелюдимая немножко, но с ней всегда так интересно поговорить!"
    th "Могу себе представить такую {i}беседу{/i}. У Лены, должно быть, ангельское терпение."
    # dreamgirl "А может, она только с тобой такая молчаливая, а на самом деле - та ещё болтушка?"
    me "Скажи, ты за ней ничего необычного не замечала в последнее время?"
    mi "Ну, как сказать... Леночка, она же такая тихая, скромная. Всё больше одна где-нибудь с книжками сидит, или рисует. Ой, а ты видел её рисунки? Она настоящая художница, у неё прямо как живые все получаются!"
    "Тут Мику запнулась, как мне показалось, немного виновато, и вдруг сбавила темп."
    mi "Хотя, вот ты сейчас меня спросил, даже странно... Последние несколько дней она и впрямь сама не своя стала. Совсем задумчивая стала и какая-то, не знаю как сказать... грустная, наверное, но пару раз я видела, как она сидит, и улыбается так хорошо, так славно! Ты знаешь, будто что-то очень хорошее вспомнила."
    "Мику вдруг смутилась и спросила меня с подозрением:"
    mi "Сеня, а ты почему вдруг меня про Лену спрашиваешь, а?"
    "Я постарался сделать вид, что не понял вопроса:"
    me "Ну ты же её соседка, кого же мне ещё про неё спрашивать?"
    mi "Да нет, я... Осторожнее, здесь корень!"
    "Перешагнув через вовремя замеченное Мику препятствие и пользуясь тем, что та на секунду отвлеклась от мыслей о причинах моих расспросов, я поинтересовался:"
    me "Скажи, а когда всё это с Леной началось? Ну вот грустить она начала и всё такое?"
    mi "Ну я не знаю, с неделю назад, наверное.{w} Да, точно! До этого всё так ровно было, что даже скучно, а потом накануне того дня, как вы в столовой в карты играли, она совсем поздно пришла спать. Как раз, когда ты приехал."
    mi "Ну что поздно - это ладно, она часто поздно приходит, в библиотеке с Женей сидит, но в тот раз спать не легла, а всю ночь сидела и рисовала до самого утра, ты представляешь? И рисунки показывать не захотела, сразу спрятала, хотя раньше всегда показывала! И потом тоже много рисовала, и прятала!"
    "Девушка вдруг покраснела и, потупив глаза, смущённо призналась:"
    mi "Ты знаешь, Сёма, я вчера посмотрела эти рисунки после обеда, пока вы все в лес за Александром ходили."
    "На фоне всех этих \"Сёмочек\" и \"Леночек\" то, как она произнесла имя \"Александр\", прозвучало неожиданно сухо, но мне сейчас не было дела до того, чем очкарик сумел ей досадить. Мику тем временем принялась оправдываться:"
    mi "Нет-нет, я конечно знаю, так нельзя делать, у всех могут быть свои секреты, а тем более тут искусства касается, я-то понимаю..."
    "Мику запнулась и, стрельнув лукаво глазками, призналась:"
    mi "Если честно, мне очень интересно было. Я нечаянно подсмотрела, что Лена их под матрасом прячет. Ну и не удержалась."
    me "Ну, и что там оказалось, на этих рисунках-то?"
    "Не вытерпел я, сам себе поражаясь - торопить девочку пулемёт, это надо же!"
    "Мику пристально на меня посмотрела."
    mi "Ты."
    me "Не понял... Что \"я\"?"
    mi "На рисунках был ты.{w} Почти на всех."
    "Мику больше не улыбалась, глядя на меня непривычно серьёзно. Она даже тараторить перестала, вместо этого говоря медленно, тщательно подбирая слова:"
    mi "Там почти на всех рисунках был ты. Только на некоторых был именно ты, такой как сейчас вот, а на некоторых словно старше, что ли. И, знаешь... отстранённый какой-то, недобрый. Лена вообще ведь очень хорошо рисует, а тут сразу видно, что с чувством рисовала. Ты там как живой получился." # ЛБ Возможно, Мику, слегка хихикая, упоминает пару рисунков в стиле ню.
    mi "И ещё, ты знаешь... среди этих рисунков была пара особенно странных. На них какой-то большой город, незнакомый, но только... только я думаю, что это где-то не у вас, не в Союзе. Но выглядит очень реально, не похоже на выдумку."
    th "Мои портреты и большой город, но не в СССР? Это-то здесь при чём? Ничего не понимаю."
    dreamgirl "Возьми, да спроси. Может, Мику что-то напутала. Почему-то я сомневаюсь, что Лена бывала за границей. Не те времена."
    me "Мику, скажи, а почему ты решила, что город заграничный?"
    "Мику остановилась на несколько секунд и задумалась, старательно наморщив лоб, покусывая губу. Я ждал, затаив дыхание."
    # mi "Я не уверена, но... На одном рисунке был вид из окна на город. Зимний город. Там вблизи обычные многоэтажные дома, я такие в Москве у вас видела, в жилых районах на окраине. А вот вдали, на горизонте - небоскрёбы. А папа мне говорил, что таких у вас не строят."
    mi "Я не уверена, но... Например, на одном рисунке - какая-то городская улица, или перекрёсток. Там всё другое - и дома не такие, и машин полным-полно, не как у вас, да и сами машины совсем не похожи на ваши, эти... \"Жигули\", да? Я, конечно, не знаток, но всё-таки..."
    mi "И ещё там на улице везде реклама, реклама - на стенах домов, поперёк тротуара... Совсек как у нас. Были даже нарисованы... эти... не знаю, как по-русски... щиты такие большие с рекламой, на столбе..."
    me "Баннеры? Или билборды?"
    "Неуверенно подсказал я. Мику обрадованно кивнула."
    mi "Точно, билборды - только ведь это они так по-английски называются. А ты откуда знаешь?"
    "Не дожидаясь моего ответа, девочка упрямо дёрнула головой, заставив ультрамариновые волосы качнутся упругой волной."
    mi "В общем, я такое в Америке ещё ожидала бы увидеть, ну или в Японии, хотя у нас там не совсем так всё, конечно, но никак не здесь. Я, может, и мало где в Союзе была, но всё-таки телевизор смотрю и кино ваши видела многие, и папа мне много рассказывал и разные альбомы с фотографиями показывал..."
    "Здесь Мику почему-то погруснела и подытожила:"
    mi "Словом, я не знаю, где Лена такое могла увидеть. У вас ведь с этим не очень, с поездками за границу, да?"
    "Я молча кивнул. Насколько я знал, в конце восьмидесятых с поездками {i}туда{/i} в стране действительно всё ещё было {i}не очень{/i}."
    "Мику вдруг озадаченно подняла брови."
    mi "Хотя подожди, я только сейчас сообразила!{w} Там же вывеска была такая заметная, светящаяся, на ней \"Торговый центр\" было написано!"
    "Видя, что я ничего не понимаю, девочка с досадой топнула ножкой."
    mi "Ну по-русски было написано! Тогда получается, что всё-таки это ваш какой-то город..."
    "Мику озадаченно замолчала, а я крепко задумался."
    $ set_mode_nvl()
    th "Итак, что у нас есть? А есть у нас тихая девочка Лена, которая неделю назад вдруг принимается рисовать меня по ночам - если верить Мику, а кроме того заводит со мной странные разговоры и, в довершение всего, признаётся подруге, что влюблена. {w}И что из этого следует?"
    dreamgirl "Да, что из этого следует, шеф?"
    th "А вот не знаю пока. Что девочка влюбилась - это ясно. {w}Как там Алиса сказала? \"Любовь зла\"."
    dreamgirl "\"...полюбишь и козла\"!"
    th "Да, большое спасибо, ты как всегда кстати."
# сцена - домик mi_un снаружи днём
    $ set_mode_adv()
    mi "Семён, ты не против, если я на пару минут к себе заскочу, раз уж мы всё равно мимо идём?"
    "Вырванный Мику из потока размышлений, я с удивлением обнаружил, что мы уже успели выбраться из кустов и топаем по дорожке мимо домиков - на один из них как раз и показывала Мику."
    me "А, ну да, конечно. Конечно, заскочи."
    mi "Я быстро, честное слово. Ты пока отдохни, а то умаялся совсем. Или к сцене иди, если хочешь, а я тебя догоню. Сцена во-он там!"
    "Мику взмахом руки показала направление и проворно взбежала на крыльцо, роясь в карманах в поисках ключа."
    me "Мику, подожди!"
    "Окликнул я девочку и, как мог проворно, поспешил за ней."
    dreamgirl "Стой, псих! Ты что затеял?"
    th "Отстань, я мысль придумал!"
    me "Мику, а ты можешь показать мне рисунки, про которые говорила?"
    "Негромко попросил я девочку."
   # отыгрываем спрайтами mi с эмоциями
    mi "Ой, Сенечка, ты что! Это же личное! Раз Лена их не показывает никому, то и тебе..."
    me "Но {i}ты{/i} же их посмотрела, хотя это и личное!"
    "У Мику вдруг подозрительно задрожала нижняя губа и я почувствовал, что она, того и гляди, заплачет."
    me "Нет-нет, Мику, ты не подумай, я ничего такого... Простое любопытство, я понимаю! {w}Да никто бы на твоём месте не устоял, честное слово! Я бы точно не удержался."
    me "Но ведь ты же сама говоришь, Лена {i}меня{/i} почти всё время рисует, так что, как-никак, это ко мне тоже имеет отношение. И ещё... понимаешь..."
    "Девочка всё ещё смотрела на меня исподлобья, но хоть плакать больше не собиралась - и то хлеб."
    me "Понимаешь... Я ведь не просто так с тобой про Лену заговорил. Дело в том, что у неё, похоже, возникли некоторые проблемы, и я..."
    mi "Сеня, а тебе что, Лена и в самом деле нравится?"
    "Спросила вдруг Мику, глядя мне прямо в глаза. От неожиданности я чуть не уронил драгоценный усилитель на землю."
    me "Э-э-э, ну я..."
    dreamgirl "Да что ты мычишь, как телёнок? Неужели считаешь, что Мику такая же бестолочь, как ты сам?"
    dreamgirl "Сначала девочка начинает по ночам рисовать одного мальчика, потом этот самый мальчик является и заводит разговоры про ту самую девочку. {w}Что, по-твоему, она должна была подумать?"
    dreamgirl "И поставь ты уже этот усилитель, что ты с ним маешься!"
    "Я ещё раз посмотрел в глаза девушке, на лице которой застыла сложная смесь смущения, любопытства и чего-то ещё, и ответил, изо всех сил стараясь не отвести взгляд:"
    me "Ты, знаешь, я и вправду к Лене хорошо отношусь. Очень."
    dreamgirl "Молодец, врёшь и не краснеешь!"
    th "Ничего я не вру! Тем более, убедительно лгать человеку в глаза - это настоящее искусство, которым я не владею. Слегка преувеличить намного проще."
#    if alt_day2_mi_rejected:
#        mi "Ну что же, я так и подумала, если честно..."
    "Мику обречённо вздохнула и кивнула на дверь."
    mi "А если там Лена? Сейчас же тихий час, по идее."
    dreamgirl "Тогда, моя милая, она давно уже вас услышала и сейчас спешно уничтожает улики. {w}Путём пережёвывания."
    me "Тогда мы извинимся, что помешали ей отдыхать, и я пойду восвояси."
    mi "А если..."
    me "Мику, я никому про тебя не скажу. Честное пионерское, обещаю!"
    "Мику поколебалась ещё секунду, но потом решилась. {w}Воровато оглянувшись по сторонам - не видит ли нас кто - она отперла наконец дверь и мы вошли в домик."
 # сцена - домик mi_un изнутри днём
    "Войдя, я с облегчением поставил наконец усилок на пол и огляделся по сторонам."
    th "Что тут можно сказать - бардак он и есть бардак. Впрочем, чего ещё ожидать от подростков."
    dreamgirl "Ну конечно, что с детишек взять. Ты-то взрослый - у тебя и бардак дома намного основательнее. Сочетание опыта и таланта."
    me "А у вас здесь довольно... уютно."
    "Мику смущённо хихикнула."
    me "Ну что, ты не передумала?"
#    if alt_day2_mi_rejected:
#        dreamgirl "Ты смотри, поосторожнее со своими двусмысленностями. Мику не в совке выросла, про {i}отношения{/i} побольше твоего знает. Поймёт тебя превратно, решит, что ты передумал и решился-таки составить её счастье..."
#    else:
    dreamgirl "Ты смотри, поосторожнее со своими двусмысленностями. Мику не в совке выросла, про отношения мальчиков с девочками побольше твоего, небось, знает, даже если и теоретически. Поймёт тебя превратно..."
    th "А что я такого сказал?"
    "Мику тем временем подошла к одной из кроватей и обернулась ко мне."
    mi "Семён, если уж ты меня в это дело втравливаешь, так помоги хоть! Матрас приподними у изголовья."
    "Я поспешил выполнить просьбу девочки. {w} В голову вдруг полезли непрошенные мысли о том, что она сейчас совсем рядом от меня, что мы одни в этом домике, а ещё я могу явственно уловить нежный запах, исходящий от её волнистых волос, рассыпавшихся по плечам и..."
    "Поспешно уставившись в стену перед собой, я старательно попытался думать о чём-то отвлечённом."
    th "Дважды два - четыре, пятью пять - двадцать пять, семью восемь - э-э-э - сорок два..."
    "Покопавшись под тощим матрасиком, Мику извлекла наконец оттуда картонную папку и нерешительно посмотрела на меня."
    mi "Может быть, всё-таки..."
    me "Мику, не тяни, показывай уже! {w}Ну... рисунки, то есть."
#<-    if alt_day2_mi_rejected:
#        "Кажется, предупреждения незримого советчика были не так уж беспочвенны - Мику окинула меня неожиданно холодным взглядом, но развивать тему не стала."
#        "Впрочем, через несколько секунд, когда я склонился над раскрытой на столе папкой, мне стало не до того."
#    else:
    "Кажется, предупреждения незримого советчика были не так уж беспочвенны - Мику явственно хихикнула, но развивать тему не стала."
    "Впрочем, через несколько секунд, когда я склонился над раскрытой на столе папкой, мне стало не до хиханек."
#->
    $ set_mode_nvl()
    "Рисунки и впрямь были хороши - не какие-нибудь детские каракули, совсем нет. Здесь чувствовались уверенная рука и свой, вполне сформировавшийся стиль, по которому всегда можно отличить одного художника от другого."
    "А ещё на рисунках и вправду был я."
    "С целого вороха листов ватмана, писчей бумаги, тетрадочных листов в клеточку - на меня смотрело моё собственное лицо."
    "Хмурое, улыбающееся, скучающее, удивлённое."
    "Часть - простые наброски, часть - тщательно проработанные рисунки со сложными тенями. Некоторые - забавные шаржи, некоторые - очень реалистичные. Большая часть была выполнена простым карандашом, но попалась и пара акварелей."
    th "Никогда бы не подумал, что всего за несколько дней можно столько нарисовать. Тем более, Лена всё-таки не только рисовала с утра до вечера - были же и ещё какие-то дела у неё."
    dreamgirl "За несколько дней, может, и вправду сложновато, но ведь тебе же сказали - по ночам тоже рисовала."
    nvl clear
    "Как зачарованный, я перебирал шуршащие листы. Вот - я анфас, а вот - в профиль. Я, в пионерской форме с галстуком, на скамеечке возле Генды. Я, клюющий носом над тарелкой с завтраком."
    "Снова я, с картами веером в левой руке. Губы азартно сжаты, хитрый взгляд немного исподлобья."
    "Я, сидящий верхом на поверженном Шурике и выкручивающий ему руки. Рисунок резкий, пронзительный, оставляющий острый привкус беспокойства."
    "Снова скамейка на площади, и на ней - мы с Леной, сидящие рядом и пялящиеся в небо. У Лены лицо едва обозначено, но почему-то чувствуется, что спокойное-спокойное. Моё - тщательно прорисованное, с выражением лёгкого недоумения, рот чуть приоткрыт простодушно."
    "А вот на этом шарже, раскрашенном цветными карандашами, я спиной вперёд совершаю забег на четвереньках по полу столовой, отчаянно пытаясь спастись от слишком резвой добавки к ужину."
    nvl clear
    "Я смущённо улыбнулся, но, по мере того, как перебирал рисунки, улыбка становилась всё более растерянной, а брови лезли всё выше на лоб."
    "Вот - взъерошенный мальчишка лет двенадцати, явно с моим лицом, несётся по знакомому до замирания сердца крутому склону среди взмывающих в небо сосен, размахивая руками, и орёт что-то во всё горло. Что-то по-детски радостное и искреннее..."
    "Вот - карапуз лет трёх, не больше, на плечах у шупловатого мужины. Мальчик кажется смутно знакомым - да ведь это тоже я! - взгляд восторженно-открытый, какой бывает только у маленьких детей, которые ещё не отравлены подлостью жизни. Контур мужчины намечен несколькими небрежными штрихами, лица нет."
    "А вот -... {w}Комната, контуры которой теряются в полумраке. Стол, на нём системник, клавиатура и монитор. За столом человек. Сутулая спина, заношенная футболка, растрёпанные давно не стриженные волосы, правая рука привычно вцепилась в мышь."
    "В холодном свете от монитора лицо кажется призрачным, но глаза видны совершенно отчётливо. Взгляд остановившийся, пустой. {w=1.5} Мёртвый."
    "Да. {w=1.0} Я знаю этого человека. {w=2.0} Это тоже я. Это уже несколько лет я."
    $ set_mode_adv()
    mi "А вот этот я не очень поняла. Если это компьютер, то странный какой-то. Разве такие дисплеи бывают? {w}И, если честно, мне этот рисунок... не очень понравился."
    "Прозвучавший словно бы откуда-то сверху, голос Мику заставил разжаться стиснувшие сердце ледяные пальцы."
    "Судорожно переведя дыхание, я благодарно покосился на девочку и отложил листок в сторону, только сейчас заметив, что он весь измят и надорван с одного краю. {w}Похоже, изображённое на нём {i}не очень понравилось{/i} не одной только Мику."
    mi "Вот эти рисунки, на которых тот странный город."
    "Мику показала на остававшиеся в папке два листа, лежащие почему-то \"спиной\" к остальным."
    "Собравшись с духом, я перевернул разом оба."
    "..."
    $ set_mode_nvl()
    "Одного взгляда было достаточно, чтобы понять, почему они показались Мику \"странными\"."
    "На одном - смутно знакомый мне заснеженный перекрёсток - не то где-то на Лиговке, не то, наоборот, на Московском. В любом случае, чутьё горожанина подсказывало мне, что это он, мой родной город."
    "И перекрёсток этот - явно не из 89-го, а из {i}моего{/i} времени. Одежда людей, вывески, реклама, тысяча других деталей, неочевидных сознанию, но чётко дающих привязку к середине {i}десятых{/i}. {w}Да те же автомобили, в конце концов - какие уж там \"жЫгули\"..."
    "На втором рисунке был изображён вполне себе ничем не примечательный вид на город. Немного даже привлекательные в своём однообразии панельные многоэтажки, снег на улицах."
    "Пейзаж, каких в любом большом городе найдутся сотни, за одним исключением - вид из собственного окна не спутаешь ни с каким другим, даже если выглядываешь в это самое окно лишь для того, чтобы узнать, снег идёт на улице, или дождь."
    $ set_mode_adv()
    "Мику, последние пару минут ёрзавшая, как на иголках, нетерпеливо потянула у меня папку."
    mi "Ну всё, посмотрел? Давай скорее их спрячем, а то не ровен час, Лена придёт, и что я ей тогда скажу?"
    dreamgirl "Это ещё что! Что-то вы, голубчики, запоёте, если вас здесь Олька вдвоём застукает!"
    th "Ой, можно подумать!"
    dreamgirl "Да уж будь уверен, {i}эта{/i} найдёт, что подумать. И не спасёт тебя тогда, Сёмочка, даже твоё происхождение."
    "Вдвоём с Мику мы быстро уничтожили все следы своей шпионской деятельности, и папка отправилась на своё законное место под матрас."
    mi "Уф! Заставил ты меня, Сёмочка, поволноваться! Я всё время так и дрожала от страха, что кто-нибудь нас с этими рисунками застанет."
    mi "Но только, смотри, ты мне обещал..."
    me "Никому ни слова про твоё участие, чесслово!"
    mi "Особенно Лене!"
    me "Сказал же, никому!"
    "Отрезал я и кивнул в сторону двери."
    me "Ну что, мавр сделал своё дело, мавр может гулять смело?"
    # show mi недовольная какая-нибудь
    mi "Это ты, Сенечка, сделал своё дело, а я сюда, вообще-то, не за тем шла."
    mi "Так что иди-ка ты к сцене, а я тебя догоню, как договаривались."
    "С этими словами она без видимых усилий подхватила усилок, взгромоздила на меня и не успел я глазом моргнуть, как оказался на крыльце, а за спиной моей захлопнулась дверь."
    dreamgirl "А вот интересно, что она там сейчас такое делает, что тебя пришлось выпроваживать?"
    "Я мысленно пожал плечами - сделать это по-настоящему мешал драгоценный груз, он же - \"полный хлам\" по словам самой Мику."
    th "Да мало ли что она может делать? Переодеться ей надо, например."
    dreamgirl "Что-о-о? И ты об этом так спокойно говоришь?! Ты только подумай, может быть, в этот самый момент она как раз снимает..."
    th "Послушай, давай когда-нибудь потом пофантазируем, а? Можем даже вместе, если захочешь. Сейчас самое время о другом подумать, тебе не кажется?"
#<-    if alt_day2_mi_rejected:
#        dreamgirl "Ну ладно, ладно. Свой шанс ты всё равно упустил ещё на пляже. А ведь мог, мог увидеть всё и даже сверх того."
#        dreamgirl "Впрочем, пусть ты и растяпа, но по-своему прав сейчас. Действительно, портреты портретами, но откуда наша стесняша может знать разные интимные факты из твоей биографии? Да и дома она у тебя вряд ли бывала - его даже и не построили ещё."
#    else:
    dreamgirl "Ну ладно, ладно. Пусть ты и зануда, но по-своему прав сейчас. Действительно, портреты портретами, но откуда наша стесняша может знать разные интимные факты из твоей биографии? Да и дома она у тебя вряд ли бывала - его даже и не построили ещё."
#->
    th "Знаешь, я тут подумал..."
    dreamgirl "Вау, это начинает входить у тебя в привычку!"
    th "...что во всей этой истории Юля может быть и ни при чём. У того же Шурика после её воздействия попросту крыша съехала без каких-то сложных фантазий. Помахал немного железякой, отоспался, и все дела."
    dreamgirl "А с чего ты взял, что \"без сложных фантазий\"? Рассказать-то он ничего не может, не помнит-с, но вчера ведь вопил что-то про то, что вы - не люди и про голоса в голове! А тихоня наша - человек творческий, вот у неё и галлюцинации посложнее да поинтереснее."
    th "Ну тогда я не знаю. Может и так."
    dreamgirl "Подожди, а что если Лена тоже того... Визуализация?" #Персонификация? # ЛБ: Специально оба варианта термина - надо определяться
    th "Что? Нет, конечно же! {w} Хотя... {w} Да нет, ерунда какая-то. В конце концов, её местные знают, та же Алиса, например."
    th "Вот в чём я наверняка уверен, так это в том, что видения Лены связаны с местным... этим... аномальным переходом. В конце, концов, она ведь за {i}моей{/i} жизнью подглядывала вольно или невольно, а Виола говорила, что переход именно на меня завязан, если я правильно понял."
    th "А поскольку Юля, вроде бы, часть аномалии... Пожалуй, стоит мне всё-таки с ней поговорить. Интуиция так подсказывает."
    dreamgirl "Эй, это наглая ложь, я ничего подобного тебе не подсказываю!"
    th "Я про настоящую интуицию, а не про сексуально озабоченного самозванца в моей голове."
    th "Во всяком случае, других идей у меня всё равно нет. Так что сейчас я отнесу этот проклятый ящик, если, конечно, не умру раньше от изнеможения, и попробую хорошенько расспросить Юлю."
    dreamgirl "И где ты её искать собираешься?"
    th "Немного там, немного здесь. Будем решать вопросы по мере их поступления, а сейчас у меня на повестке дня удерживать равновесие и не падать - Мику меня точно прикончит, если я усилок грохну. Сил ей явно не занимать - вон как она его одной левой кантовала. {w}Могла бы и сама донести, кстати, так нет же, нашла вьючного дурака..."
    if (alt_day2_rendezvous == 3):
        dreamgirl "И не одна она, кстати! {w}Ничего, держись, вьючный! Кажется, уже сцену видно!"
    else:
        dreamgirl "Держись, вьючный, кажется, уже сцену видно!"
# сцена - сцена вблизи днём
    # далее спрайты Мику в платье - таки ГГ угадал, она заранее переоделась к концерту.
    "До сцены мы с Мику добрались одновременно - она как раз подоспела вовремя, чтобы снять наконец с утомлённого меня этот железный минигроб."
    "Я плюхнулся на скамейку в первом ряду, а девочка затрещала:"
    mi "Ой, Сенечка, большое тебе спасибо! Ты мне так помог, так помог!"
    voice "Мику, куда ставить-то?!"
    "Задушенно прохрипели вдруг прямо у меня над ухом."
    mi "Ой, как хорошо, какие вы молодцы ребята! Колонки на сцену надо поднять!{w} Сенечка, ты не поможешь мальчикам?"
    "Я покосился на четвёрку отдувающихся пионеров помладше, обессиленно привалившихся к объёмистым корпусам колонок."
    th "Кажется, пора делать ноги, иначе я отсюда уже не вырвусь."
    mi "Мику, извини, не могу! Надо бежать срочно, меня ждут!{w} И спасибо тебе ещё раз! Ты тоже очень помогла сама знаешь кому!"
    "Я вскочил - откуда только силы взялись! - и с максимально доступной мне скоростью рванул прочь."
    "Кажется, мне что-то кричали вслед, но я не стал останавливаться и выяснять, что именно."

    $ alt_uvao_D6_left_MI_talk = True
    stop sound_loop fadeout 1

    jump alt_day6_uvao_left_ask_UV_about_UN
