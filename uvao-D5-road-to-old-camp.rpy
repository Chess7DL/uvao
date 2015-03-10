# Д5-Дорога в старый лагерь
#
#
#    $ routetag = "uv"
#    $ alt_chapter(5, u"Юля. Дорога в старый лагерь")
label alt_day5_uvao_road_to_old_camp:
    window hide
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_path_sunset with fade
    play ambience ambience_forest_day fadein 3
    window show
    "Выйдя наружу и хозяйственно прикрыв за собой калитку, я решительно двинулся в сторону деревьев, подступавших здесь к самому забору."
    "Лес становился все гуще. Торчащие из земли корни норовили попасть прямо под ноги - несколько раз я чудом избегал падения."
    "Несмотря на то, что с каждым шагом я отходил от лагеря, тропинка все не кончалась."
    th "Кстати, о тропинке. К ней что, весь лагерь ходит? Понапротаптывали…"
    dreamgirl "Не ты первый, не ты последний, мой дружок."
    th "Не думаю, что все так прозаично, иначе зачем она меня позвала?"
    dreamgirl "Ну как ты думаешь, зачем девушка может позвать юношу в уединенное место?"
    th "Да ну тебя!"
    if alt_day4_uv_viola_evening:
        th "Ещё и Виола эта со своими страшилками. Сама же говорит, что Юля для меня безопасна, а потом - что 'близкие контакты закончатся печально'."
        th "И вот как это понимать? Что, съест она меня?"
        "Я вспомнил остренькие зубки… Всё-таки до волка или даже до собаки ей далеко, да и я не мышь какая-нибудь.{w} Не съест."
        dreamgirl "Разве что понадкусывает немного!"
    "Очередной корешок подвернулся под ногу, но я устоял, практически сев на шпагат."
    th "Главное рюкзак донести. А то буду ползать по лесу и собирать просыпанные конфеты."
    if alt_day4_uv_viola_evening:
        dreamgirl "А ещё при {i}слишком близких{/i} контактах ты можешь заразиться, и у тебя тоже вырастут уши и хвост. А ещё…"
    "Я вздохнул.{w} Тропинка и не думала заканчиваться. Мне даже казалось, что я иду по кругу."
    scene bg ext_path2_day with dissolve
    "Немного подумав, я решил оставить зарубку на дереве."
    th "Если хожу кругами, то хотя бы пойму это."
    "Однако в последующие пятнадцать минут пути метки я не видел.{w} А спустя еще минуты три лес начал редеть."
    "Вскоре показалась небольшая опушка, на которой стояло…"
    dreamgirl "Избушка, избушка, повернись к лесу передом, а к Ивану задом!"
    scene bg ext_old_building_day with dissolve
    "«Избушкой» оказалось здание, судя по всему когда-то бывшее либо собственностью лагеря, либо какого-то детсада."
    "Ржавая ограда, скрипящая детская площадка, прохудившаяся местами крыша. Ночью здесь наверняка страшно."
    th "И она здесь живет?"
    dreamgirl "Хочешь проверить?"
    "Была  - не была."
    "Я открыл скрипящую калитку и вступил на вымощенную плиткой тропинку к входу."
    "Зияющая чернота входа, с валявшейся рядом дверью, словно приглашали меня прогуляться по внутренностям ужасного чудовища."
    dreamgirl "Штанишки не намочил?"
    th "Что, я трус какой? Нас такой ерундой не запугаешь!"
    scene bg int_old_building_night with fade # Я напилил в фотошопе дневной вариант интерьера лагеря, решите использовать его или как. И, соответсвенно, может быть придётся немного под него переписать текст. - Ленофаг
    "Я вошел в здание.{w} Внутри было действительно темно, лишь редкие лучи света пробирались через дыры в потолке и разбитые окна."
    "Внутри здание выглядело необитаемым, но осмотреть его на предмет признаков жизни стоило."
    "Всюду валялся мусор. Толстый слой пыли покрывал старые деревянные столики, подоконники, гардеробные вешалки…"
    "Вокруг царило запустение."
    "Я задумался и не заметил, как под ногу подвернулось что-то мягкое. Я взглянул туда."
    "Старый пыльный плюшевый медведь, без правой задней лапы, печально взирал на меня своим единственным глазом-пуговицей."
    "Возникало ощущение, будто я очутился то ли в каком-то городе-призраке, то ли в низкобюджетном фильме ужасов."
    dreamgirl "Ага. Теперь иди проверь вооон ту тёмную комнату. Главное, не забудь перед этим громко поинтересоваться, есть ли там кто-нибудь."
    th "Очень смешно."
    "Осмотр первого этажа результатов не дал, я лишь наглотался пыли и начихался вдоволь, поэтому решил подняться на второй."
    "На втором этаже было ничуть не лучше, чем внизу.{w} Те же разбросанные пыльные игрушки, вперемешку с книгами, поваленные шкафы и тумбочки."
    "Пару раз под ноги попадались старые куклы, один раз я чуть не упал, наступив на маленькую матрешку."
    "Создавалось впечатление, что это было излюбленное место для вандализма."
#СТРАШНЫЙ скрип
    play sound sfx_carousel_squeak
    "Внизу что-то громко и протяжно заскрипело. По моей спине прошел холодок."
    "Перочинный ножик моментально перекочевал из кармана в руку, однако двигаться я все так же не решался."
    "Минуты тянулись долго, и вскоре опять воцарилась тишина."
    "Я набрался храбрости и решился спуститься вниз.{w} Аккуратно, шаг за шагом я двинулся по лестнице.{w} Вот уже преодолел один лестничный поворот…"
    show uv normal far at left with dissolve
    "В дверях я заметил чей-то силуэт и облегченно выдохнул: на пороге, спиной ко мне, стояла Юля и смотрела куда-то вдаль."
    "Я, убрав нож от греха подальше, собрался было окликнуть ее…"
    "Внезапно ступени под моей ногой скрипнули."
    show uv rage far with dspr
    "Хвост Юли тут же распушился и стал напоминать ершик для чистки бутылок. Ушки тут же направились в мою сторону, с кошачьей проворностью Юля развернулась и уже готова была атаковать."
    me "Стой! Это я, Семён!"
    show uv shocked far with dspr
    uv "С-семён? Ты меня напугал. А как ты прошел незаметно?"
    "Она явно успокоилась, но ее распушенный хвост все так же ходил из стороны в сторону."
    show uv normal at center with dissolve
    me "Ты тут живешь?"
    uv "Не совсем. Тут часто бродят ваши… Я живу там."
    "Она указала куда-то под лестницу и снова развернулась к выходу."

    #эти вопросы-ответы следует размазать по тексту
    #- Откуда ты сюда пришла?
    #- Я всегда тут была. Тут интересно. Всегда есть, за кем посмотреть. Только прятаться надо, чтобы не увидели. Я раньше не пряталась, и меня поймать хотели. Пришлось спасаться.

    # - Ты что, прямо тут и живёшь?
    #- Ну да. Удобно очень. Нор много. Есть, где запасы прятать. В лесу не спрячешь, белки и мыши найдут.
     
    #- Ты меня не помнишь?
    #- Я тебя видела, когда спала. Ты раньше идти не хотел, всё в свой квадрат смотрел. А потом согласился. Хорошо. Теперь спокойнее.
     
    #- А ещё с кем-нибудь в лагере ты виделась?
    #- Давно. Ещё когда тут жили. Со мной вожатая говорила. Недолго почему-то. Потом кричать начала и убежала. А потом все туда жить ушли.
     
    #- А зимой ты тут как?
    #- Зимой? Это когда белое всё? Холодно. Хорошо, что недолго. Я в столовой на чердаке зимой. Там тепло, и еда рядом. И площадь видно. Там дерево игрушками обвешивают. Я ночью их рассматриваю. Некоторые себе беру. Они блестят, с ними играть интересно.  
    #- Какие запасы?
    #- Всякие. Зимой холодно, по лесу не походить. А есть хочется.

    show uv dontlike with dspr
    uv "Кажется, ты кого-то привел."
    "В голосе показались нотки угрозы."
    me "Разве? Я шел один."
    show uv upset with dspr
    uv "А кто это тогда?"
    "Она указала куда-то в сторону леса. Я подошел и, сощурившись от яркого солнца, взглянул туда, куда указала Юля."
    "Из кустов показалась шатающаяся фигура, которая тут же принялась себя отряхивать от листьев и налипшего к пионерской форме репейника."
    "Короткие светлые волосы, бликующие на солнце очки…"
    me "Шурик?!"
    me "Он не должен нас видеть!"
    show uv surprise with dspr
    uv "Он не с тобой?"
    me "Нет, он, наверно, шпионил за мной. Тоже тебя ищет, что ли?{w} Наверно, нам лучше спрятаться."
    "Юля проворно скользнула мимо меня и направилась к лестнице."
    show uv smile far at fright with dissolve
    uv "Сюда."
    play sound sfx_carousel_squeak
    "Она поманила меня и с громким скрипом открыла железный люк."
    hide uv with dissolve
    "Ловко прыгнув вниз, она оставила меня возле открытого люка. Выхода не было, я полез за ней."
    play sound sfx_carousel_squeak
    stop ambience fadeout 2
    "Осмотревшись напоследок, я закрыл за собой скрипучий люк и стал спускаться вниз."
