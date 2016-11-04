# План-набросок на утро Д7 гуд (тру и фальш)
#
# Используется флаг тру-ветки alt_uvao_D6_CS_vetrov
# Используется флаг alt_uvao_D6_left_MI_talk (true=медпункт / false=карьер)
# Используется флаг ... (про Славю)
#
label label alt_day7_uvao_getting_up:

    #эффект ряби, за ней - что-то похожее на звёздное небо
    "Я лежал в шезлонге и смотрел на звёздное небо."
    "Звёзды тихонько перешёптывались между собой о чём-то, ласково мне подмигивая и иногда улыбаясь."
    "Одно только было плохо - они никак не хотели складываться в знакомый с детства рисунок созвездий."
    "В какой-то момент я заприметил было Полярную звезду, но Ольга возразила мне:"
    #проявляется через dissolve по центру увеличенный и размытый голый спрайт ОД. Грудь по большей части или скрывается за нижним краем экрана, или вовсе уж размыта или затемнена. 
    mt "Какая же это Полярная звезда, Семён, ты что! Её только из Северного полушария видно!"
    mt "Вот, смотри - Южный крест. Правда, красиво?"
    #появляется небольшой анимированный Южный крест у неё над грудью
    "И в самом деле, на шее у Ольги на тонкой цепочке таинственно переливался россыпью звёзд Южный крест."
    "Она вдруг наклонилась ко мне."
    #blink-unblink
    #сцена - домик ОД изнутри утром.
    #with hpunch
    show mt pioneer panama surprised close
    mt "Семён, какой Южный крест, ты о чём вообще?"
    "Я попытался сесть в кровати, но запутался в одеяле."
    mt "С добрым утром, фантазёр!"
    show mt pioneer panama smile
    "Улыбнулась мне Ольга, выпрямляясь."
    me "Фачему фафтазёр?"
    "Кое-как промямлил я деревянным со сна языком."
    "Чувствовал я себя отвратительно невыспавшимся."
    mt "Потому что непременно надо быть фантазёром, чтобы видеть сны!"
    "Рассмеялась вожатая."
    show mt pioneer panama normal
    mt "Вставай, Семён. Полседьмого уже!"
    "Я отчаянно зевнул, чуть не вывихнув челюсть, и тут до меня дошло наконец."
    me "Как полседьмого?"
    "Я сел на краю кровати, кутаясь в одеяло."
    me "Что-то случилось?"
#    show mt pioneer panama normal
    "Ольга отрицательно покачала головой."
    mt "Да нет, ничего не случилось, не волнуйся так. {w}Во всяком случае, ничего нового."
    mt "Одевайся и выходи скорее, я тебя снаружи жду."
    "Торопливо распутывая брошенную вчера как попало одежду и отчаянно борясь с раздирающей рот зевотой я мучительно пытался понять, чего ради Ольга подняла меня в такую рань."
    "Опыт предыдущих дней не давал мне никаких поводов для оптимизма."
    th "Не иначе, Юля кого-то ещё ошарашила. Или в медпункте что-то не так. Или..."
    "Одним словом, от силы через пару минут я уже выскочил из домика, на ходу застёгивая рубашку и ёжась от утренней прохлады."
    #сцена - домик ОД снаружи утром
    show mt pioneer panama normal
    "А ты быстро сегодня."
    "Вымученно улыбнулась мне Ольга."
    "Только сейчас я заметил, что она выглядит помятой и какой-то взъерошенной, а судя по мешкам под глазами, спала она сегодня куда меньше моего."
    me "Не томите, Ольга Дмитриевна. Что случилось-то?"
    "Ольга вновь покачала головой."
    mt "Говорю же тебе, ничего не случилось."
    mt "Просто сегодня последний день смены. Надо успеть сделать целую кучу дел, а я осталась без помощницы."
    mt "Так что если ты мне не поможешь, то не знаю, что и делать тогда."
    show mt pioneer panama sad
    "Наверное, взгляд мой был более, чем красноречив, потому что она виновато потупила глаза и как-то беспомощно развела руками."
    mt "Дел и вправду невпроворот, а рассчитывать мне в отряде больше не на кого."
    mt "Вернее... Я хочу сказать, остальным можно попытаться поручить что-то несложное, но надо будет стоять рядом и контролировать непрерывно, а у меня совсем нет на это времени. {w}Мне нужен человек с головой на плечах, самостоя...."
    "Тут Ольга отчаянно зевнула, не сдержавшись, и помотала головой."
    show mt pioneer panama normal
    mt "У Виолы отличный растворимый кофе есть..."
    "Мечтательно пробормотала она."
    mt "Жаль только, сейчас в медпункт..."
    "Вожатая посмотрела на меня чуть ли не умоляюще."
    mt "Ну так как, поможешь мне?"
    #наверное, здесь или текст на весь экран (но текста маловато), или затенить картинку
    th "Помочь Ленивовне закрыть смену? Вот это номер!"
    th "Что же, отличная возможность отыграться за все её придирки да насмешки!"
    th "Тоже мне, нашла дурака, помогать я ей стану. Пусть сама вертится, как хочет - на то она и вожатая, а я пойду досыпать!"
    #конец полного экрана/визуального эфффекта
    "Вздохнув, я спросил:"
    me "Что делать-то надо? Умыться хоть успею?"

#На входе имеем диспозицию:
# Славя гарантированно в медпункте
# alt_uvao_D6_left_MI_talk - левый вечерний медпункт - Лена в медпункте
# через карьер - Лена в медпункте
# через где-то ещё - Лена уехала на Саныче в ночь
# через врезку - alt_uvao_D6_CS_vetrov - Лена свободна, но ненавязчива (тру-ГГ не дал облить на шезлонгах и уболтал)
               # not alt_uvao_D6_CS_vetrov - Лена свободна и навязчива (облита на шезлонгах. фальш-ГГ вынужден уворачиваться всё утро. В какой-то момент Лена его загонит-таки в угол для Окончательного Выяснения Вопросов, но нечаянно набижит ОД и спасёт ГГ)
               # un "Семён! Мы должны поговорить!"
               # me "..."
               # выскакивает ОД
               # mt "Вот вы где! Лена, подожди, со мной пойдёшь, а ты, Семён, беги скорее..."
               # "Не дожидаясь продолжения, я повернулся и побежал что есть духу."
               # "Ольга что-то кричала мне вслед, но я не стал возвращаться, и выяснять, что именно."
               # минут через пятнадцать ГГ снова пересекается с ОД. Та отправляет его куда-то ещё Делать Полезное, но не выдерживает и ржёт: "Да не бойся ты, наказание моё, нет там Лены!"
# ГГ мечется как ошпаренный с судорожным перерывом на завтрак урывками.
# Возможно, в какой-то момент его отлавливает Юля. Опять же, возможно, она вручает ему наивный подарок (стеклянный шарик, кулёчек с сахаром, банка консервов) - от сердца оторвала!
# Ближе к полудню наконец-то всё заканчивается, детям выдают сухой паёк и грузят в автобус.