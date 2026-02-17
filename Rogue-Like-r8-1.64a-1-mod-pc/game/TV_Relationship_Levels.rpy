# TV relationship levels module
# Used by Study_Session -> "skip study and watch TV" option
# Adds 5 relationship levels for 12 girls based on stats and relationship flags.

label TV_Relationship_Level(Girl=0):
    if not Girl:
        return 1

    # Hard negative
    if "ex" in Girl.Traits:
        return 1

    # Explicit relationship flags (highest priority)
    if "lover" in Girl.Petnames:
        return 5
    if ("sir" in Girl.Petnames) or ("master" in Girl.Petnames) or ("daddy" in Girl.Petnames):
        return 5

    if Girl in Player.Harem or "boyfriend" in Girl.Petnames:
        return 4

    if ("sex friend" in Girl.Petnames) or ("sexfriend" in Girl.Petnames) or ("fuckbuddy" in Girl.Petnames) or ("fuck buddy" in Girl.Petnames):
        return 3

    # Stat-based fallback
    if Girl.Love >= 850 and ApprovalCheck(Girl, 900, "L"):
        return 4
    if Girl.Love >= 650 or Girl.Inbt >= 650 or Girl.Obed >= 650:
        return 3
    if Girl.Love >= 400 or Girl.Inbt >= 400 or Girl.Obed >= 400:
        return 2

    return 1


label TV_SkipStudy_ForParty_Levels:
    # Call this right after the line:
    # "Вместо учебы вы включаете телевизор..."
    if Party:
        call TV_SkipStudy_Event_Level(Party[0])
    if len(Party) >= 2 and Party[1] and Party[1] != Party[0]:
        call TV_SkipStudy_Event_Level(Party[1])
    return


label TV_SkipStudy_Event_Level(Girl=0):
    if not Girl:
        return
    call Shift_Focus(Girl)

    $ lvl = renpy.call_in_new_context("TV_Relationship_Level", Girl) # ensure integer returned
    # renpy.call_in_new_context returns None; so call directly:
    $ lvl = TV_Relationship_Level(Girl)

    if Girl is RogueX:
        call Rogue_TV_Level(lvl)
    elif Girl is KittyX:
        call Kitty_TV_Level(lvl)
    elif Girl is EmmaX:
        call Emma_TV_Level(lvl)
    elif Girl is LauraX:
        call Laura_TV_Level(lvl)
    elif Girl is JeanX:
        call Jean_TV_Level(lvl)
    elif Girl is StormX:
        call Storm_TV_Level(lvl)
    elif Girl is JubesX:
        call Jubes_TV_Level(lvl)
    elif Girl is GwenX:
        call Gwen_TV_Level(lvl)
    elif Girl is BetsyX:
        call Betsy_TV_Level(lvl)
    elif Girl is DoreenX:
        call Doreen_TV_Level(lvl)
    elif Girl is WandaX:
        call Wanda_TV_Level(lvl)
    elif Girl is YanaX:
        call Yana_TV_Level(lvl)
    return


# -------------------- Dispatch per girl --------------------

label Rogue_TV_Level(lvl=1):
    if lvl == 5:
        ch_r "Ммм… так лучше. Иди сюда." 
    elif lvl == 4:
        ch_r "Ладно, одна серия. Но ты мне должен." 
    elif lvl == 3:
        ch_r "Окей, но выбирай что-то нормальное." 
    elif lvl == 2:
        ch_r "ТВ вместо учебы? Ты серьезно?" 
    else:
        ch_r "Нет. Если уж собрались — учись." 
    return

label Kitty_TV_Level(lvl=1):
    if lvl == 5:
        ch_k "Так[KittyX.like]гораздо лучше…" 
    elif lvl == 4:
        ch_k "Ну лааадно… но потом ты мне поможешь." 
    elif lvl == 3:
        ch_k "Окей, но без скукоты." 
    elif lvl == 2:
        ch_k "Эй! Мы же учились…" 
    else:
        ch_k "Не-а. Я не буду прогуливать." 
    return

label Emma_TV_Level(lvl=1):
    if lvl == 5:
        ch_e "Хорошо. Сегодня я закрою на это глаза." 
    elif lvl == 4:
        ch_e "Одна передышка допустима." 
    elif lvl == 3:
        ch_e "Если это поможет тебе сосредоточиться потом — ладно." 
    elif lvl == 2:
        ch_e "Мы здесь не для развлечений." 
    else:
        ch_e "Нет. Продолжай заниматься." 
    return

label Laura_TV_Level(lvl=1):
    if lvl == 5:
        ch_l "…Ладно. Только ближе." 
    elif lvl == 4:
        ch_l "Хорошо. Но потом — без отмазок." 
    elif lvl == 3:
        ch_l "Окей. Но недолго." 
    elif lvl == 2:
        ch_l "ТВ? Серьезно?" 
    else:
        ch_l "Нет." 
    return

label Jean_TV_Level(lvl=1):
    if lvl == 5:
        ch_j "Ммм. Хороший выбор." 
    elif lvl == 4:
        ch_j "Ладно, я с тобой." 
    elif lvl == 3:
        ch_j "Окей, включай." 
    elif lvl == 2:
        ch_j "Пфф. Ну ты и лентяй." 
    else:
        ch_j "Нет. Учись." 
    return

label Storm_TV_Level(lvl=1):
    if lvl == 5:
        ch_s "Давай. Я хочу просто быть рядом." 
    elif lvl == 4:
        ch_s "Хорошо… один эпизод." 
    elif lvl == 3:
        ch_s "Окей. Что будем смотреть?" 
    elif lvl == 2:
        ch_s "Мы теряем время." 
    else:
        ch_s "Нет, давай закончим учебу." 
    return

label Jubes_TV_Level(lvl=1):
    if lvl == 5:
        ch_v "Окей! Но я выбираю!" 
    elif lvl == 4:
        ch_v "Ладно… но потом обратно к делу." 
    elif lvl == 3:
        ch_v "Ну… недолго." 
    elif lvl == 2:
        ch_v "Ох… может не стоит?" 
    else:
        ch_v "Нет. Лучше учиться." 
    return

label Gwen_TV_Level(lvl=1):
    if lvl == 5:
        ch_g "Одна серия… и обнимашки." 
    elif lvl == 4:
        ch_g "Ладно, выбирай."
    elif lvl == 3:
        ch_g "Окей, но не что-то тупое." 
    elif lvl == 2:
        ch_g "Эм… мы же учились…" 
    else:
        ch_g "Нет, я не хочу." 
    return

label Betsy_TV_Level(lvl=1):
    if lvl == 5:
        ch_b "Устроимся поудобнее, дорогуша." 
    elif lvl == 4:
        ch_b "Хорошо. Но ты мне должен." 
    elif lvl == 3:
        ch_b "О, прогуливаем? Забавно." 
    elif lvl == 2:
        ch_b "Телевизор? Хм." 
    else:
        ch_b "Нет. Учеба — значит учеба." 
    return

label Doreen_TV_Level(lvl=1):
    if lvl == 5:
        ch_d "Оу! Давай смотреть вместе!" 
    elif lvl == 4:
        ch_d "Ладно, но потом мы продолжим, да?" 
    elif lvl == 3:
        ch_d "Окей!" 
    elif lvl == 2:
        ch_d "Эм… мы отвлекаемся…" 
    else:
        ch_d "Нет, давай учиться." 
    return

label Wanda_TV_Level(lvl=1):
    if lvl == 5:
        ch_w "Хорошо. Я хочу, чтобы ты расслабилась." 
    elif lvl == 4:
        ch_w "Ладно. Только не делай из этого привычку." 
    elif lvl == 3:
        ch_w "Окей." 
    elif lvl == 2:
        ch_w "Серьезно?" 
    else:
        ch_w "Нет." 
    return

label Yana_TV_Level(lvl=1):
    if lvl == 5:
        ch_y "Хорошо. Но ты слушаешь меня." 
    elif lvl == 4:
        ch_y "Ладно. Один раз." 
    elif lvl == 3:
        ch_y "Окей, включай." 
    elif lvl == 2:
        ch_y "Тебе правда не хочется учиться?" 
    else:
        ch_y "Нет. Продолжай." 
    return