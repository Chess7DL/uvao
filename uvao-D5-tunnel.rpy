label alt_day5_uvao_tunnel:
#
# Д5 - Спуск в бункер.
#

    $ routetag = "uv"
    $ alt_chapter(5, u"Юля. Под землёй")
    $ night_time()
    $ persistent.sprite_time = "night"
   
    window hide
# ТЕМНО!
    scene black with fade
    play ambience ambience_catacombs fadein 3
    window show
    dreamgirl "Эй! Да здесь же темно, как в…"
    th "…Наверное, как в подземелье, да? Жаль, фонарика нет!"
    me "И куда теперь дальше?"
# Всё ещё темно!
#    show uv upset at center with dissolve
    uv "Никуда. Подождём здесь."
    uv "Когда твой Шурик уйдёт - вернёмся."
    "Юля замолчала, слышно было лишь её спокойное дыхание где-то рядом. С поверхности не доносилось ни звука."
    th "Интересно, а если он наверху решит поселиться? Будем сидеть здесь вечно?"
    "С минуту я просто стоял на месте столбом, боясь отойти от лестницы."
    "Против ожиданий, воздух в подвале, или где там мы оказались, вовсе не был затхлым, да и под ногами было сухо."
    window hide
    scene bg int_catacombs_entrance with dissolve2
    window show
    "Постепенно зрение адаптировалось, и я понял, что мрак не был вовсе беспросветным.{w} Мы явно стояли в каком-то длинном коридоре или тоннеле, с одной стороны издалека доносился слабый свет."
    show uv normal at left with dissolve2
    me "Юля, а куда коридор ведёт?"
    "Я показал в сторону невидимого источника света."
    uv "Никуда. Там дверь большая. Железная. Не открывается."
    dreamgirl "Вот тебе и возможность убить время. В худшем случае пройдёшься туда-сюда, разомнёшься."
    th "Ну да, а в лучшем - найду новых приключений на свою задницу."
    dreamgirl "Ну и сидел бы тогда в лагере, клинья к девочкам подбивал!{w} Глядишь, и обломилось бы чего."
    "Возразить Шизе было нечего. Действительно, стоя на месте много не узнаешь, и если уж я взялся искать ответы - упускать шанс получить хоть какую-то информацию было глупо."
    "К тому же здесь было ощутимо прохладнее, чем наверху, так что тонкая рубашка помогала слабо. Я зябко поёжился, с тоской вспоминая забытый тёплый свитер, и предложил:"
    me "Слушай, а пойдём, посмотрим эту твою железную дверь? Вдруг вместе получится её открыть?"
    "Юля не заставила себя долго упрашивать."
    show uv grin with dissolve
    uv "Пойдём, попробуем открыть!{w} Узнаем, что там!"
    "Она схватила меня за руку и уверенно потащила куда-то в сторону источника света."
    show uv smile with dissolve
    "По мере того, как становилось светлее, я смог немного осмотреться."
    "Тоннель - а сейчас было уже совершенно ясно, что это никакой не коридор в подвале, а именно тоннель - имел явно заметный уклон вниз."
    show uv normal with dspr
    th "Спуск в бомбоубежище? Серьёзно у них здесь всё организовано было!"
    "Вдоль бетонных стен тянулись аккуратно уложенные кабели, на потолке через равные промежутки были закреплены забранные в сетку светильники."
    "Впрочем, источник света впереди оказался таким же светильником - то ли единственным уцелевшим, то ли это просто было дежурное освещение."
    th "Надо же, сюда питание до сих пор подаётся!"
    "Запоздало удивился я."
    "В желтоватом свете пыльной лампы хорошо было видно, что стенам уже не один десяток лет, но время практически не коснулось их - ни трещин, ни потёков воды."
    th "Прочно же раньше строили!"
    "Тоннель, освещённый редкими работающими светильниками, всё никак не заканчивался, плавно уводя куда-то вглубь."
    th "Что-то это выглядит слишком серьёзным для бомбоубежища в пионерском лагере где-то в глуши."
    "Через несколько минут впереди показался наконец тусклый блеск металла."
    window hide
    scene bg int_catacombs_door with dissolve
    play music music_list["orchid"] fadein 5
    with dissolve
    window show
    "Дойдя до конца, мы оказались перед закрытой гермодверью."
    me "Ого, мощно сделано. Интересно, что там, за этой дверью?"
    show uv normal at right with dissolve
    uv "Не знаю. Говорю же, у меня не получалось открыть."
    "Я попробовал повернуть кремальеру, но - увы, сил не хватало."
    "Немного пошарив глазами по сторонам, я заметил кусок толстой арматуры."
    th "Хмм, а что если?…"
    "Подобрав свою находку, я вставил её в колесо кремальеры."
    me "Дайте мне точку опоры, иииии…"
    "И ни хрена. Я надавил ещё сильнее, потом навалился всем телом, надеясь сдвинуть-таки заржавевший механизм. Тщетно."
    play sound breath fadein 1
    "Переводя дух, я снова огляделся. Глаза остановились на чёрной коробочке сбоку от двери - от кремальеры не дотянуться.{w} Под откидной крышкой обнаружилась кнопка без опознавательных знаков."
    stop sound fadeout 5
    "Немного подумав, я надавил кнопку, преодолевая усилие неожиданно тугой пружины…"
    "Внутри стены что-то глухо щёлкнуло."
    "Я отпустил кнопку - снова щелчок."
    th "Возможно, здесь специально проход для двоих - для сильного и для умного?"
    dreamgirl "Всегда двое их - учитель и ученик…"
    "Я не стал уточнять у Шизы смысл намёка, а вместо этого повернулся к Юле, с интересом наблюдавшей за моими манипуляциями."
    me "Поможешь мне?"
    show uv surprise at center with dissolve
    uv "А что надо делать?"
    me "Я думаю, что дверь можно будет открыть, если держать эту кнопку нажатой. Сможешь её удержать?"
    show uv smile far at fright with dissolve
    "Несмотря на хрупкое телосложение, Юля без особого труда придавила тугую кнопку."
    "Услышав щелчок, я поспешно навалился вновь всем телом на импровизированный рычаг…{w} Это было опрометчиво."
    play sound sfx_carousel_squeak
    me "Уййй!"
    dreamgirl "Сила есть - ум не поможет."
    show uv surprise at center with dissolve
    "Кремальера провернулась неожиданно легко, арматурина сорвалась, и я крепко приложил ей сам себя по правой ноге прямо над коленом."
    "Юля от неожиданности отпрыгнула на пару метров и уставилась на дверь."
    uv "Скрипит. Получилось?"
    "Шипя от боли, я выкрутил колесо до упора и потянул."
    play sound sfx_open_door_mines_metal
    "Дверь очень неторопливо провернулась на петлях."
    me "Похоже, что да."
    show uv normal with dspr
    stop music fadeout 3
    "Находясь под впечатлением от уже увиденного, я рассчитывал оказаться в тамбуре со второй гермодверью."
    window hide
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living with fade
    play music music_list["waltz_of_doubts"] fadein 5
    show uv normal at left with dissolve
    window show
    "Однако, к моему удивлению, сразу за дверью оказалось что-то вроде небольшого убежища. Двухъярусная кровать, какие-то приборы - работающие, что удивительно! - шкафчики с какими-то ящиками. Похоже, именно сюда стремился Шурик."
    "Колено начинало ныть всё сильнее, и я, стараясь не беспокоить его, допрыгал до кровати на одной ноге."
    me "Подожди, давай передохнём. Я, похоже, сильно ногу ушиб и не смогу идти какое-то время."
    uv "Хорошо, давай."
    "Я решил посмотреть, что с ногой. На коленке красовалась небольшая ссадина поверх наливающегося синяка."
    #th "Похоже, повезло. Так можно было и инвалидом стать."
    #dreamgirl "Инвалидом ты бы стал, если бы с разбитым суставом выбрался отсюда! А до тех пор ты бы числился пропавшим без вести."
    uv "Залижи."
    me "A?"
    uv "Залижи. Я всегда так делаю. Мне очень помогает."
    show uv smile with dspr
    "Она задрала ногу и продемонстрировала, кося на меня жёлтым глазом."
    "Я усмехнулся. Ну и кошка!"
    dreamgirl "Может она и тебе коленку полижет, вдруг пройдёт?"
    "Шиза была как всегда в своём репертуаре."
    th "Отвали, не до того сейчас."
    me "Нет, мы так не делаем."
    "С некоторой гордостью сказал я."
    me "Мне бы немного льда. Да только где его тут взять?"
    uv "Вот поэтому зализывать лучше."
    "Но тут с ней не поспоришь. Наверное, в лагере найти лёд не составило бы труда, но в каком-то подземном бункере это не такая уж и лёгкая задача."
    show uv normal with dspr
    "Вставать с кровати не хотелось.{w} Слишком рано встал, слишком много беготни по лесам, руинам и туннелям, а также бесед с этим… существом, Юлей."
    "Должно быть, именно так себя чувствует чересчур разогнанный комп во время серьёзных вычислений - мой мозг практически кипел. Я вытянулся на кровати и закрыл глаза."
    show blink
    $ renpy.pause(2)
    "Толчок в плечо."
    hide blink
    show unblink
    $ renpy.pause(1.5)
    uv "Дверь закрой. А то этот, друг твой, нас найдёт."
    me "И не друг он мне вовсе!"
    "Возмутился я."
    "Но в целом - она была права, тут же ещё Шурик шляется где-то. Не хватало ещё, чтобы он меня нашёл в подземном бункере с девочкой, которая помимо хорошей фигуры имеет пару кошачьих ушей и хвост."
    #"Застонав, я поднялся, доковылял до двери, закрыл её и свалился на кровать. Глаза закрылись сами.{w}"
    "Доковыляв до двери, я закрыл её и свалился на кровать. Глаза закрылись сами."
    show blink
    $ renpy.pause(2)
    "Последнее что я почувствовал - как кто-то тёплый подлез мне под руку и улёгся рядом…"
    window hide
    $ renpy.pause(2, hard=True)
    jump alt_day5_uvao_bunker
