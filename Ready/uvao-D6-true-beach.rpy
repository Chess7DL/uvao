# Д6-посещение пляжа после допроса Шурика на тру-ветке
#
# Используется флаг сопровождения в Д1 Славей от ворот до домика ОД alt_day1_sl_conv
# Используется флаг разговора в Д5 на пляже со Славей alt_uvao_D5_evening_sl
# Используется флаг танца в день 3 alt_day3_dancing
# Используется флаг Полного Знания alt_uvao_D6_CS_vetrov
# Используется индикатор степени настойчивости Слави alt_uvao_D6_sl_assert
#
label alt_day6_true_beach:
    window hide
    scene bg ext_aidpost_day with fade
    play ambience ambience_camp_center_day fadein 3
    show sh normal pioneer at cright with dissolve
    window show
    "Выйдя из медпункта, мы с Шуриком переглянулись и, не сговариваясь, бодро зашагали в сторону площади."
    window hide
    scene bg ext_square_day with fade
    show sh normal pioneer at cright with dissolve
    window show
    play music music_list["my_daily_life"] fadein 3
    "Однако очень скоро мы сбавили шаг, а обогнув Генду, и вовсе остановились. Следовало решить, что делать дальше."
    "Впрочем, Шурик с этим проблем не испытывал, судя по вороватым взглядам, которые он бросал в сторону главных ворот лагеря, а заодно - и здания клубов."
    sh "Ну, это… Я пойду, наверное…"
    "Он неопределённо помахал в воздухе рукой."
    sh "Отдыхать, и всё такое… Согласно предписаниям…"
    show sh smile pioneer far at cright with dissolve
    "Шурик смущённо улыбнулся и сделал маленький шажок в сторону вожделенной мекки местных кибернетиков."
    "Я нейтрально кивнул."
    me "Ну да, ну да. Последний день, надо оттянуться по полной, всё такое.{w} Будь здоров."
    hide sh with dissolve
    "Я повернулся и вразвалочку направился в сторону, противоположную клубам."
    sh "И да, Семён… Извини ещё раз за вчерашнее…"
    "Не оборачиваясь, я вытянул руку в сторону и, подняв большой палец вверх, буркнул:"
    me "Ноу проблем!"
    "Не знаю, знакомо ли было будущее светило отечественного роботостроения с западными боевиками, но дальнейших реплик не последовало."
    "Осторожно покосившись назад полминуты спустя, я как раз успел увидеть очкарика, входящего в здание клубов."
    dreamgirl "Ну вот, всё в порядке. Отправился дышать свежими парами канифоли.{w} Слушай, может у него канифольная зависимость?"
    th "Да пусть он там нюхает на здоровье что хочет, хоть клей \"Момент\", лишь бы больше не лез не в своё дело!"
    th "Меня вполне устроит, если он там до самого отъезда просидит."
    "Впрочем, пусть и без общества Шурика, мне всё равно следовало найти себе занятие до обеда."
    "В голове после разговора с Виолой царил полный кавардак. Открывающиеся передо мной перспективы одновременно и манили, и пугали."
    dreamgirl "Перспективы, конечно, самые радужные, но что если она тебе всё наврала? Нет никаких проколов, не будет никакой ассимиляции…"
    th "Тьфу на тебя! Ты издеваешься, что ли? То вешаешь мне лапшу на уши про общество взаимовыручки и чуть ли не всеобщего благоденствия, то наоборот, пугаешь."
    dreamgirl "Про благоденствие, кажется, вообще никто ничего не говорил, так что не надо этих инсинуаций в мой адрес."
    dreamgirl "А что до моего непостоянства, так я же, по большому счёту, отражение твоего подсознания, а человеческое подсознание - вообще штука переменчивая."
    "Я судорожно сжал кулаки в бессильной злобе. Кажется, внутреннему пошляку в очередной раз удалось вывести меня из себя.{w} И ведь ничего не сделаешь с этой заразой…"
    "Впрочем, на этот раз моё альтер эго решило не добивать меня окончательно, потому что голос в моей голове прозвучал примиряюще:"
    dreamgirl "Ладно, хочешь хороший совет?"
    th "Не хочу!"
    "Буркнул я себе под нос, но мою карманную шизофрению это, разумеется, не остановило."
    dreamgirl "Так вот, отправляйся-ка ты на пляж. Уже шестой день тут болтаешься, погода всё время стоит отличная, а искупаться до сих пор так ни разу и не удалось."
    dreamgirl "Может быть, хоть сегодня повезёт?{w} Да и вообще, не мешало бы тебе и в гигиенических целях ополоснуться, между нами говоря. Ходишь как бомж какой-то, честное слово."
    "На это возразить мне было нечего, тем более, что пока я препирался с голосами в собственной голове, ноги сами принесли меня ко входу на пляж."
    "Что же, почему бы и нет? Заодно и отвлекусь немного от всех этих откровений про устройство мироздания."
    stop music fadeout 3
    window hide
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_beach_day with fade
    window show
    "Разумеется, на пляже было полным-полно народа. В глазах зарябило от от носящейся туда-сюда и радостно вопящей что-то мелюзги."
    play music music_list["eat_some_trouble"] fadein 3
    show us laugh swim far at fright with dissolve
    "Ребята постарше играли в пионербол - а во что же ещё? {w}Разумеется, заправляла там Ульянка. Мне даже показалось, что она периодически умудрялась оказываться в нескольких местах одновременно."
    show dv normal swim far at fleft
    show mi normal swim far at left
    with dissolve
    "Немного поодаль я увидел сидящих на песке и оживлённо о чём-то болтающих Алису и Мику."
    th "Странно, вот уж не подумал бы, что они вообще между собой общаются. Хотя, что вообще я о них знаю, особенно о Мику?"
    th "Впрочем, какая разница? Заняты своим делом - вот и славно. Не будут лезть с разговорами."
    show mt normal panama swim far at center with dissolve
    "Ну и разумеется, Ольга была на своём боевом посту, как же иначе! Неустанно контролирует безопасность пионеров лёжа на шезлонге, аж глаза закрыла от усердия."
    hide mt
    hide dv
    hide mi
    hide us
    with dissolve
    "Лены нигде видно не было, что меня сейчас вполне устраивало. Разумеется, я ей был обязан за вчерашнее, но в последнее время каждая встреча с ней оборачивалась для меня какой-нибудь нервотрёпкой, а сейчас мне хотелось только одного - покоя."
    "Уже предвкушая, как с разбегу брошусь в воду, я потянулся к пуговицам рубашки… И застыл, чувствуя себя полным идиотом."
    th "Плавок-то у меня нет! Искупался, называется."
    th "Вернее, плавки есть, но благополучно лежат в моём домике, в тумбочке. По такой жаре за ними тащиться через весь лагерь? Увольте."
    dreamgirl "Да, с этим неувязочка вышла. А с другой стороны, подумаешь, условности! Полезай прямо в трусах!"
    if alt_uvao_D5_evening_sl:
        dreamgirl "В конце концов, вчера вечером тебя отсутствие плавок нисколько не смущало."
        th "Так то вчера, на безлюдном пляже. Ну, то есть, я думал, что он безлюдный.{w} А вот эпатировать публику семейниками - увольте. Тем более, здесь дети всё-таки."
    else:
        "Эпатировать публику семейниками? Увольте! Тем более, здесь дети всё-таки."
    dreamgirl "Ой, можно подумать! Ты вспомни, какой год на дворе. Небось, полстраны в трусах купается."
    th "Всё, вопрос закрыт!"
    "Потоптавшись на месте, я окончательно решил махнуть рукой на купание. {w}Ничего, перебьюсь как-нибудь."
    "Впрочем, идти куда-то ещё было тоже лень, так что я решил скоротать время за полезным занятием - поговорить с вожатой. {w}Интересно, что {i}она{/i} скажет про всякие там ассимиляции и тому подобное."
    "Ольга тем временем всё так же вкалывала на благо общества, развалившись на шезлонге с закрытыми глазами."
    "Подойдя поближе, я кашлянул и осторожно позвал:"
    me "Ольга Дмитриевна…"
    show mt normal panama swim with dissolve
    "Та открыла глаза и с неудовольствием посмотрела на меня. Потом, вздохнув, села, спустив ноги с шезлонга, и спросила:"
    mt "Да, Семён. Что случилось?"
    me "Вы понимаете, какое дело…"
    dreamgirl "Вы извините, что я такой молодой к вам обращаюсь!"
    "От внезапного вмешательства внутреннего надоеды я запнулся, но вожатая не стала ждать продолжения."
    show mt smile panama swim with dspr
    mt "Давай, я попробую угадать. Ты решил искупаться, но плавки оставил в домике?"
    me "Плавки? Ну да, так и есть, но я…"
    "Замямлил я в ответ. Усмехнувшись, Ольга открыла было рот, чтобы сказать что-то, но её внезапно перебили."
    show sl normal pioneer at right
    show mt surprise panama swim
    with dissolve
    sl "Ой, Семён, у тебя плавок нет! Точно, ты же без вещей приехал!"
    "Похоже, своим неожиданным появлением Славя застала врасплох не только меня - Ольга даже вздрогнула от неожиданности."
    if alt_uvao_D6_sl_assert < 3:
        sl "Знаешь, а ведь я тебе могу помочь! Жди меня здесь и никуда не уходи!"
        hide sl with dissolve
        "С этими словами Славя немедленно куда-то убежала."
    else:
        sl "Подожди здесь и никуда не уходи, слышишь! Я сейчас!"
        hide sl with dissolve
        "Выпалив это, Славя немедленно куда-то унеслась."
    "Вожатая проводила её озадаченным взглядом и уставилась на меня."
    if alt_uvao_D6_CS_vetrov:
        show mt normal panama swim with dspr
        mt "Ну что, поговорили с Виолой?"
        me "Не то слово - поговорили. У меня, если честно, голова кругом идёт - все эти проколы, попаданцы…"
    else:
        show mt angry panama swim with dissolve
        mt "Тебя с утра Виола искала. Ты где пропадал?"
        "Взглянув на её лицо, я с лёгкостью представил себе, как в и без того недовольном голосе вожатой появляются гневные ноты, и попытался уйти от ответа на опасный вопрос:"
        me "Да я только что из медпункта. У меня, если честно, голова кругом идёт - все эти проколы, попаданцы…"
    stop music fadeout 3
    "Ольга неопределённо хмыкнула. Стараясь не слишком пялиться на её выдающиеся формы, которые купальник не столько прятал, сколько выставлял напоказ, я уселся рядом на песок."
    play music music_list["goodbye_home_shores"] fadein 3
    show mt normal panama swim close with dissolve
    "Оглядевшись и убедившись, что нас никто не подслушивает, я сказал по возможности нейтральным тоном:"
    me "Виола упомянула, что я смогу остаться здесь, если… Ну, в общем, это от меня будет зависеть, останусь я {i}здесь{/i}, или нет."
    show mt surprise panama swim close with dspr
    "Ольга посмотрела на меня как-то растерянно и замялась."
    dreamgirl "Очень даже может быть, что обычно они здесь попаданцам заранее таких вещей не рассказывают. Чтобы нечаянно не отпугнуть, например. Это ты у нас весь такой уникальный, что тебе лекции читают."
    dreamgirl "Так что похоже, Оленьке ты сейчас шаблон-то несколько порвал."
    th "Знаешь, я-то как раз предпочёл бы быть как все и не выделяться."
    "Я уже прикидывал, не смыться ли мне под каким-нибудь благовидным предлогом, но тут вожатая наконец прекратила молча меня разглядывать и улыбнулась неожиданно мягко."
    show mt smile panama swim close with dspr
    mt "Да, по большому счёту, так и есть, останешься ты или нет - будет зависеть от тебя самого. А тебя это и вправду волнует, так?"
    "Я лишь молча кивнул, боясь не совладать с вдруг онемевшим языком."
    "Вожатая вдруг рассмеялась:"
    # show mt laugh panama swim close with dissolve # ЛБ: разобраться с отсутствующим mt laugh panama swim close
    mt "Ой, да не делай ты такое серьёзное лицо, будто у тебя снова живот прихватило, как тогда, на танцах!"
    "Ольга лихо мне подмигнула. Чувствуя, что заливаюсь румянцем, словно девчонка, я смущённо потупился."
    "Отсмеявшись, она продолжила негромко, всё так же мягко улыбаясь:"
    # show mt smile panama swim close with dissolve
    mt "Вот сам-то ты хочешь остаться здесь или, наоборот, вернуться?"
    me "Ну…"
    "Затянул было я, но Ольга меня остановила:"
    show mt normal panama swim close with dspr
    mt "Нет-нет, ты мне ничего не говори, ты сам себе постарайся ответить."
    mt "Не \"хорошо\" или \"плохо\", не \"правильно\" или \"неправильно\", а именно \"хочется\" или \"не хочется\"."
    mt "Всё будет зависеть именно от твоего желания. Если подумать, это ведь так редко бывает в жизни, чтобы что-то делалось строго по нашему желанию!"
    hide mt with dissolve
    "Ольга снова подмигнула мне, на этот раз ободряюще, улеглась поудобнее на шезлонге и закрыла глаза, оставив меня наедине с моими мыслями."
    dreamgirl "Да-а… Умение и опыт, что тут скажешь!"
    "Как обычно, альтер эго было не понять, да я не очень-то и старался."
    th "Тарабарщина какая-то! Хорошо-плохо, хочется-не хочется… Да откуда я знаю, чего мне хочется-то?"
    dreamgirl "А ты подумай, вдруг получится."
    stop music fadeout 2
    "От очередного раунда беззвучных и бессмысленных препирательств меня избавила запыхавшаяся Славя."
    play music music_list["eat_some_trouble"] fadein 3
    show sl normal pioneer with dissolve
    sl "Вот, держи. Думаю, подойдут по размеру."
    "Она сунула мне в руки нечто чёрное, оказавшееся при ближайшем рассмотрении обычными мужскими плавками."
    sl "А даже если и не совсем твой размер, то всё лучше, чем без ничего."
    if alt_uvao_D6_sl_assert = 3:
        show sl shy pioneer close with dissolve
        "Она вдруг наклонилась и бархатистым голосом, от которого разом туго натянулась какая-то струна у меня в животе, шепнула мне на ухо:"
        sl "Хотя я лично так, может быть, и не считаю."
        show sl normal pioneer with dissolve
        me "Э-э…"
        dreamgirl "Что-то ты, барин, в последнее время слишком часто краснеешь, тебе не кажется?"
        "Я неловко кашлянул и, совладав наконец с голосом, искренне, хотя и немного смущённо, поблагодарил девочку:"
    me "Славя, ты просто чудо! Я уже счёт потерял, сколько раз ты меня выручала за эти дни."
    show sl shy pioneer with dissolve
    sl "Ой, да ладно тебе! Мне же не трудно!"
    hide sl with dissolve
    "Она радостно заулыбалась в ответ и, одарив меня взмахом ресниц, от которого у меня внутри толкнулось что-то горячее, вновь убежала куда-то."
    "А я… А что я? Пошёл к кабинкам, переодеваться."
    window hide
    stop music fadeout 3
    scene bg ext_beach_day with fade
    # play music music_list["so_good_to_be_careless"] fadein 3
    window show
    "Вода на жарком июльском солнце успела как следует прогреться, так что я вволю наплавался и наплескался, прежде чем снова выбраться на берег."
    play music music_list["what_do_you_think_of_me"] fadein 3
    "Кажется, купание пошло мне на пользу. Вместе с грязью я словно бы смыл и всю накопившуюся за эти пять безумных дней усталость.{w} Сейчас завтрашний день уже не казался мне таким пугающим."
    "Спрятавшись от чересчур злого, на мой вкус, солнца под одним из \"грибков\", стоящих недалеко от воды, я прислонился спиной к его деревянной ножке, откинув голову назад так, чтобы затылком ощущать шероховатую тёплую поверхность."
    scene bg ext_beach_day:
        xalign 0.0 yalign 0.0 zoom 1.0
        linear 3.0 zoom 2.5 xalign 0.67 yalign 0.65
    "Полузакрыв глаза, я рассеяно любовался серебристыми бликами, пляшущими по водной глади.{w} На душе было непривычно спокойно, мысли в голове больше не толклись суетливыми мухами, а текли плавно, словно нежащаяся под солнцем река передо мной."
    th "В самом деле, что это я распаниковался? Если и вправду всё повернётся так, как мне нужно - чего же ещё желать?"
    th "В сущности, Ольга мне дала неплохой совет - попытаться понять, чего мне хочется на самом деле. Неужели я в собственных желаниях не смогу разобраться?"
    "Однако, моим благим намерениям не было суждено сбыться. Кто-то бесцеремонно нарушил моё уединение, усевшись рядом на песок."
    "Впрочем, мне сейчас было слишком хорошо, чтобы расстраиваться или злиться из-за такой ерунды."
    th "Ну да, а чему удивляться. Всё-таки здесь каждый - в первую очередь член общества, часть единого целого… Во всяком случае, в теории. Наверное, и мне придётся, если останусь…"
    scene bg ext_beach_day
    show sl smile swim close at right
    with dissolve2
    "Я лениво повернул голову, чтобы всё-таки узнать, кого это нелёгкая принесла, и наткнулся на взгляд небесно-голубых глаз."
    "Рядом сидела, мило улыбаясь, раскрасневшаяся после купания Славя. Мокрые волосы, на коже блестят капельки воды. Словно зачарованный, я проследил, как одна из них скатилась с ключицы вниз, на плотно обтянутую купальником высокую…"
    "Спохватившись, я выписал себе мысленного леща и попытался поднять взгляд обратно на лицо."
    "Молчание затягивалось. Впрочем, кажется, тяготило оно в основном меня. Лукаво поглядывающую Славю моё смущение явно забавляло."
    "Наконец она тихонько хихикнула и спросила, откидывая с лица прядь мокрых волос:"
    sl "Ну что, искупался?"
    "Я поспешно ухватился за предложенную соломинку:"
    me "Да, прямо как заново родился!{w} Ещё раз спасибо за плавки!"
    show sl laugh swim close with dissolve
    sl "Да говорю же - ерунда. В конце концов, не голышом же тебе было купаться, {i}при всех-то{/i}!"
    show sl smile2 swim close with dissolve
    "Сделав ударение на последнем слове, она вновь одарила меня лукавым взглядом и, развернув невесть откуда взявшееся полотенце, принялась вытираться."
    "Словно зачарованный, я смотрел, как она не спеша обтёрла плечи, потом закинула полотенце за спину, гибко прогнувшись вперёд…"
    hide sl with dissolve
    "Я отвёл взгляд, чувствуя, что щёки начинают пылают. В голове раздался смешок:"
    dreamgirl "Ай-яй-яй! Девочка старается, а ты отворачиваешься. Нехорошо!"
    th "Что?"
    "Тупо переспросил я."
    "Не зная, куда девать глаза, я отвернулся было от Слави" # здесь точки нет!
    show mi smile swim at left with dissolve
    extend "… Чтобы тут же обнаружить, что с другой стороны, буквально в паре метров от меня, на аккуратно расстеленном полотенце нежится под солнцем Мику."
# что-нибудь соблазнительное про Мику и её формы -ЛБ
    dreamgirl "А хороша девочка! Хотя фигурка-то у неё, между нами говоря, совсем даже не девчоночья."
# возможно, побольше комментариев Шизы про Мику! -ЛБ
    show mi grin swim with dissolve
#ЛБ: про погруснев - убрать совсем, если только Автор не изменит ещё раз условия для входа на рут
#    if alt_day3_dancing == 4:
#        "Японка открыла глаза и, увидев, что я на неё смотрю, слегка улыбнулась, впрочем, сразу погрустнев."
#    else:
    "Японка открыла глаза и, увидев, что я на неё смотрю, кокетливо улыбнулась."
    hide mi with dissolve
    "Я поспешно перевёл взгляд прямо перед собой."
    scene bg ext_beach_day:
        xalign 0.0 yalign 0.0 zoom 1.0
        linear 1.0 zoom 2.5 xalign 0.67 yalign 0.65
    th "Да, правильно. Буду смотреть на воду, как до этого."
    "Я постарался сконцентрироваться на отбрасываемых рябью солнечных зайчиках и не обращать внимания на шелест полотенца по влажной коже - совсем слабый, но почему-то отчётливо слышимый даже за гомоном носящейся по пляжу малышни."
    dreamgirl "А ведь сейчас Славя, наверное, как раз вытирает…"
    th "Я свеж и спокоен, тело моё расслаблено. Плеск волн радует мой слух, а игра солнца на них - мой взор. Ничто не смущает мой разум."
    "С минуту мне казалось, что импровизированная мантра начала помогать."
    "Я сосредоточенно пялился на воду, даже Славя рядом притихла, перестав шуршать полотенцем - наверное, закончила вытираться."
    th "Нет-нет, никаких полотенец. Тело моё свежо, разум мой расслаблен… {w=1.5}Тьфу ты! Наоборот. Тело моё расслаблено, разум свеж. Речные волны…"
    stop music fadeout 1
    play sound sfx_water_emerge
    scene bg ext_beach_day
    show dv normal swim far at cleft
    with flash
    "С громким всплеском кто-то вынырнул прямо из усердно созерцаемых мной волн, выбросив целое облако брызг, и через несколько секунд уже брёл в воде по направлению к берегу."
    $ volume(0.5, 'sound_loop')
    play sound_loop sfx_head_heartbeat
    "Не отрываясь, я смотрел, как новоявленная Афродита выходит на берег, отряхивая воду с рыжих волос."
    show dv normal swim at center with dissolve2
    "Поймав мой взгляд, Алиса на секунду нахмурилась было, но вдруг озорно ухмыльнулась и, не отводя глаз, повернулась вполоборота."
    "Продолжая смотреть мне прямо в глаза, она плавно провела ладонями по телу сверху вниз, смахивая воду."
    with vpunch
    $ renpy.music.set_volume(1.0, delay=1, channel='sound_loop')
    scene expression im.MatrixColor(ImageReference("bg ext_beach_day"), im.matrix.tint(1.0, 0.6, 0.6))
    show dv normal swim at center
    with dissolve
    "Рядом недовольно хмыкнула Славя, но мне было уже всё равно. Сердце отчаянно колотилось где-то около самого горла, не давая сделать вдох, эхом отдаваясь в висках."
    th "Чёрт!"
    "Плавки внезапно оказались нестерпимо тесны, и со всей ужасающей очевидностью мне стало ясно, что ещё несколько секунд - и я погиб. У меня даже полотенца нет, прикрыться…"
    stop sound_loop
    play sound sfx_soccer_ball_catch
    $ renpy.music.set_volume(0.1, delay=0.5, channel='ambience')
    with hpunch
    hide dv #прячем без перехода
    scene bg black
    with flash_red
    "Что-то с силой ударило меня в голову, так что искры из глаз посыпались…{w=1} И я обнаружил себя уже лежащим на боку."
    "Сквозь шум в ушах до меня донёсся далёкий крик:"
    play sound sfx_angry_ulyana
    sl "{b}УЛЬЯНААААА!!!{/b}"
    scene bg ext_beach_day with fade2
    stop sound fadeout 1
    "Я кое-как сел, отплёвываясь от набившегося в рот песка, и попытался понять, что же произошло."
    "Получалось не очень хорошо - в голове звенело и бубнили какие-то голоса."
    $ renpy.music.set_volume(1.0, delay=5, channel='ambience')
    "Впрочем, звон быстро пошёл на убыль, и я понял, что это не у меня в голове бубнят, а на кого-то неподалёку орут в несколько голосов, а этот кто-то возмущённо огрызается."
    "Я ощупал голову. Кажется, прилетело мне откуда-то сзади. Тут в поле зрения появилось испуганное лицо Слави."
    show sl scared swim close at right with dissolve
    sl "Семён, как ты?"
    "Я осторожно качнул головой из стороны в сторону. Мир вокруг нехорошо качнулся было следом, но устоял."
    me "Ты знаешь, кажется я живой."
    show sl angry swim close with dissolve
    "Славя нахмурилась, и я поторопился её заверить:"
    me "Да в порядке я, в порядке. Кость, что ей сделается."
    show sl normal swim close with dissolve
    "Сделав несколько глубоких вдохов и выдохов, я наконец решился обернуться."
    show mt rage panama swim far at fleft
    show us dontlike swim far at cleft
    show sl normal swim close at right
    with dissolve
    "Картина преступления моментально прояснилась - рядом со мной валялся на песке волейбольный мяч, а в стороне разъярённая Ольга Дмитриевна продолжала отчитывать Ульянку."
    "Та что-то обиженно бурчала в ответ, но уже не так энергично."
    "Славя подтвердила мои догадки:"
    show sl serious swim close with dissolve
    sl "Представляешь, Ульяна взяла и запулила в тебя мячом со всей дури!"
    "Я сопоставил относительно небольшой вес волейбольного меча с силой обрушившегося на меня удара и посмотрел на Ульянку с невольным уважением."
    th "Вот это удар! Ай да малявка!"
    "Ещё раз покрутив головой и убедившись, что та прочно держится на плечах, я решил не нагнетать лишних страстей и буркнул примиряюще:"
    me "Да ладно вам, ведь не убила же она меня. Ну бывает. Наверное, нечаянно получилось, заигрались…"
    show sl angry swim close with dissolve
    sl "Нечаянно? Это с ноги-то? Я сама всё видела, только сделать ничего уже не успела!"
    th "С ноги? Вот ведь зараза мелкая!"
    dreamgirl "Полностью присоединяюсь!"
    show sl serious swim close with dissolve
    "Несмотря на редкостное единодушие, возникшее у нас с альтер эго по данному вопросу, скандалить мне по-прежнему не хотелось."
    show mt angry panama swim far at fleft
    show us dontlike swim far at cleft
    with dissolve
    "Я снова посмотрел в сторону Ульяны. Ольга наконец закончила ей выговаривать - наверное, выдохлась."
    "Мелкая тоже больше не огрызалась, а молча стояла, полуотвернувшись от вожатой и надувшись, как мышь на крупу."
    "Вздохнув, я поднялся и направился к ним."
    show mt angry panama swim at left
    show us dontlike swim at cright
    hide sl
    with dissolve
    "Подойдя поближе, я сказал, глядя куда-то в сторону:"
    me "Ольга Дмитриевна, не сердитесь вы на неё слишком сильно. Ребёнок, что с неё взять."
    show mt surprise panama swim
    show us angry swim
    with dissolve
    "Обе уставились на меня - одна удивлённо, другая возмущённо, но промолчали."
    "Я повернулся и пошёл переодеваться."
    stop ambience fadeout 1
    window hide
    scene bg ext_square_day with fade
    window show
    play ambience ambience_camp_center_day fadein 3
    "Недолго думая, я отправился на пристань. И отсюда идти недалеко, и до столовой рукой подать - привыкший уже к регулярной кормёжке организм подсказывал, что обед не за горами."
    stop ambience fadeout 1
    window hide
    scene bg ext_boathouse_day with fade
    window show
    play ambience ambience_boat_station_day fadein 3
    "Здесь было тихо и спокойно. Никто не носился, не кричал. В волейбол тоже не играли, что давало некоторую надежду не схлопотать повторно мячом по голове."
    "Я ещё раз на всякий случай прислушался к своим ощущениям. Голова хотя и побаливала, но не кружилась, тошноты не чувствовалось."
    th "Кажется, обошлось без сотрясения мозга."
    "Я разулся и уселся на мостки, свесив ноги в воду."
    "Подозрительно помалкивавшее последние несколько минут подсознание вдруг подало голос:"
    dreamgirl "Я тебя прямо-таки не узнаю. Где твоя здоровая мизантропия? Где человек человеку люпус эст? Где око за око?{w=1} Вроде бы тебе по голове не так уж сильно заехали, в чём дело?"
    th "Как будто что-то плохое! Тоже мне, нашли царя Ирода! Что я, пожиратель младенцев какой-нибудь?"
    th "Ну пусто у неё в голове, зато в другом месте играет, что я могу с этим поделать? Не лупить же её мячом в ответ, в самом-то деле!"
    "Голос в голове притворно вздохнул:"
    dreamgirl "Да-а, эк тебя ассимилировало-то, бедолагу."
    dreamgirl "Хотя, надо сказать, Ульяна тебе оказала большую услугу, пусть и невольно, так что свой проступок она отчасти загладила."
    th "Какую ещё услугу?! Вечно ты загадками говоришь, что за манера такая у тебя?"
    "В ответ на моё брюзжание послышался ехидный смешок:"
    dreamgirl "Тебе как, плавки больше не жмут?"
    "Воспоминание обожгло меня жгучим стыдом."
    "Кажется, за всю свою жизнь мне не приходилось краснеть столько, сколько за последние пару часов. Похоже, я только что поставил какой-то безумный рекорд в этой области."
    "Впрочем, спору нет, прилетевший мяч напрочь выбил на какое-то время все гормоны из головы, да и из остального тела тоже."
    dreamgirl "Вот то-то же!"
    play sound eat_horn fadein 3
    "Итог этой поучительной беседе подвёл горн."
    stop sound fadeout 2
    "Я поднялся, не спеша обулся и вразвалочку пошёл к столовой."
    jump alt_day6_lunch_dv_sl
