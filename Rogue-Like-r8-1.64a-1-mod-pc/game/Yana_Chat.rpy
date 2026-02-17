# star Yana chat interface
#Yana Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label Yana_Relationship: #rkeljsvgbdw
    while True:
        menu:
            ch_y "О чем ты хочешь поговорить?"
            "Хочешь стать моей девушкой?" if YanaX not in Player.Harem and "ex" not in YanaX.Traits:
                    $ YanaX.DailyActions.append("relationship")
                    if "asked boyfriend" in YanaX.DailyActions and "angry" in YanaX.DailyActions:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in YanaX.DailyActions:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "И снова нет."
                            return
                    elif YanaX.Break[0]:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Я не буду делить тебя ни с кем."
                            if Player.Harem:
                                    $ YanaX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    if not Player.Male:
                                        ch_p "Я серьезна как никогда."
                                    else:
                                        ch_p "Я серьезен как никогда."

                    $ YanaX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "YanaYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_y "Другие согласны?"
                        else:
                            ch_y "[Player.Harem[0].Name] не против?"
                        return

                    if YanaX.Event[5]:
                            $ YanaX.FaceChange("bemused", 1)
                            ch_y "Мне показалось, тебе это не интересно."
                    else:
                            $ YanaX.FaceChange("surprised", 2)
                            ch_y "Что?"
                            $ YanaX.FaceChange("smile", 1)

                    call Yana_OtherWoman

                    if YanaX.Love >= 800:
                            $ YanaX.FaceChange("surprised", 1)
                            $ YanaX.Mouth = "smile"
                            if not YanaX.Event[5]:
                                    $ YanaX.Statup("Love", 200, 10)
                                    call Yana_BF
                                    return
                            $ YanaX.Statup("Love", 200, 40)
                            ch_y "Без проблем."
                            if "boyfriend" not in YanaX.Petnames:
                                    $ YanaX.Petnames.append("boyfriend")
                            if "YanaYes" in Player.Traits:
                                    $ Player.Traits.remove("YanaYes")
                            $ Player.Harem.append(YanaX)
                            call Harem_Initiation
                            "[YanaX.Name] подходит и страстно целует вас."
                            $ YanaX.FaceChange("kiss", 1)
                            $ YanaX.Kissed += 1
                    elif YanaX.Obed >= 500:
                            $ YanaX.FaceChange("perplexed")
                            ch_y "Я не уверена. Думаю, наши текущие отношения лучше."
                    elif YanaX.Inbt >= 500:
                            $ YanaX.FaceChange("smile")
                            ch_y "Расслабься."
                    else:
                            $ YanaX.FaceChange("perplexed", 1)
                            ch_y "Меня это больше не интересует, [YanaX.Petname]."

            "Может, начнем все сначала?" if "ex" in YanaX.Traits:
                    $ YanaX.DailyActions.append("relationship")
                    if "asked boyfriend" in YanaX.DailyActions and "angry" in YanaX.DailyActions:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Перестань спрашивать."
                            return
                    elif "asked boyfriend" in YanaX.DailyActions:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Нет."
                            return

                    $ YanaX.DailyActions.append("asked boyfriend")

                    if Player.Harem and "YanaYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_y "Другие согласны?"
                            else:
                                ch_y "[Player.Harem[0].Name] не против?"
                            return

                    $ Cnt = 0
                    call Yana_OtherWoman

                    if YanaX.Love >= 800:
                            $ YanaX.FaceChange("surprised", 1)
                            $ YanaX.Mouth = "smile"
                            $ YanaX.Statup("Love", 90, 5)
                            ch_y "Я моу дать тебе еще один шанс."
                            if "boyfriend" not in YanaX.Petnames:
                                        $ YanaX.Petnames.append("boyfriend")
                            $ YanaX.Traits.remove("ex")
                            if "YanaYes" in Player.Traits:
                                    $ Player.Traits.remove("YanaYes")
                            $ Player.Harem.append(YanaX)
                            call Harem_Initiation
                            "[YanaX.Name] подходит и страстно целует вас."
                            $ YanaX.FaceChange("kiss", 1)
                            $ YanaX.Kissed += 1
                    elif YanaX.Love >= 600 and ApprovalCheck(YanaX, 1500):
                            $ YanaX.FaceChange("smile", 1)
                            $ YanaX.Statup("Love", 90, 5)
                            ch_y ". . . почему нет."
                            if "boyfriend" not in YanaX.Petnames:
                                    $ YanaX.Petnames.append("boyfriend")
                            $ YanaX.Traits.remove("ex")
                            if "YanaYes" in Player.Traits:
                                    $ Player.Traits.remove("YanaYes")
                            $ Player.Harem.append(YanaX)
                            call Harem_Initiation
                            $ YanaX.FaceChange("kiss", 1)
                            "[YanaX.Name] дарит вам легкий поцелуй."
                            $ YanaX.FaceChange("sly", 1)
                            $ YanaX.Kissed += 1
                    elif YanaX.Obed >= 500:
                            $ YanaX.FaceChange("sad")
                            ch_y "Я не думаю, что у нас \"все получится\". . ."
                    elif YanaX.Inbt >= 500:
                            $ YanaX.FaceChange("perplexed")
                            ch_y "Есть вещи и повеселее."
                    else:
                            $ YanaX.FaceChange("sadside", 1)
                            ch_y "Я не хочу проходить через это снова. . ."

                    # End Back Together

            "Я хочу поговорить о. . . [[разговор про другую девушку]" if YanaX in Player.Harem:
                            call AskDateOther

            "Думаю, мы должны расстаться." if YanaX in Player.Harem:
                            if "breakup talk" in YanaX.RecentActions:
                                    ch_y "Прекрати уже."
                            elif "breakup talk" in YanaX.DailyActions:
                                    ch_y "Опять эта  \"драма?\""
                                    ch_y "Оставь меня в покое, [YanaX.Petname]."
                            else:
                                    call Breakup(YanaX)

            "О разговоре, который у нас был ранее. . .":
                menu:
                    "Помнишь, ты признавалась мне в любви. . ." if "lover" not in YanaX.Traits and YanaX.Event[6] >= 20 and YanaX.Event[6] != 23:
                            call Yana_Love_Redux

                    "Помнишь, ты рассказывала мне о себе. . ." if "lover" not in YanaX.Traits and YanaX.Event[6] == 23:
                            call Yana_Love_Redux

                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировал?" if "sir" not in YanaX.Petnames and "sir" in YanaX.History and Player.Male:
                            if "asked sub" in YanaX.RecentActions:
                                    ch_y "Перестань об этом спрашивать."
                            elif "asked sub" in YanaX.DailyActions:
                                    ch_y "Оставь меня в покое, [YanaX.Petname]."
                            else:
                                    call Yana_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я больше тебя контролировала?" if "sir" not in YanaX.Petnames and "sir" in YanaX.History and not Player.Male:
                            if "asked sub" in YanaX.RecentActions:
                                    ch_y "Перестань об этом спрашивать."
                            elif "asked sub" in YanaX.DailyActions:
                                    ch_y "Оставь меня в покое, [YanaX.Petname]."
                            else:
                                    call Yana_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоим хозяйкой?" if "master" not in YanaX.Petnames and "master" in YanaX.History and not Player.Male:
                            if "asked sub" in YanaX.RecentActions:
                                    ch_y "Перестань об этом спрашивать."
                            elif "asked sub" in YanaX.DailyActions:
                                    ch_y "Оставь меня в покое, [YanaX.Petname]."
                            else:
                                    call Yana_Sub_Asked
                    "Помнишь, ты говорила, что хочешь, чтобы я стала твоим хозяином?" if "master" not in YanaX.Petnames and "master" in YanaX.History and Player.Male:
                            if "asked sub" in YanaX.RecentActions:
                                    ch_y "Перестань об этом спрашивать."
                            elif "asked sub" in YanaX.DailyActions:
                                    ch_y "Оставь меня в покое, [YanaX.Petname]."
                            else:
                                    call Yana_Sub_Asked
                    "Неважно":
                            pass

            "О твоей демонической форме. . ." if "master" in YanaX.Petnames:
                    call Yana_Demon

            "Неважно":
                return

    return

label Yana_OtherWoman(Cnt = 0): #rkeljsvgbdw
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ Cnt = int((YanaX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ YanaX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_y "Ты ведь сейчас с [Player.Harem[0].Name_tvo] и другими?"
    else:
        ch_y "Ты ведь сейчас с [Player.Harem[0].Name_tvo]?"
    menu:
        extend ""
        "Она сказала, что я могу быть и с тобой тоже." if "YanaYes" in Player.Traits:
                if ApprovalCheck(YanaX, 1800, Bonus = Cnt):
                        $ YanaX.FaceChange("smile", 1)
                        if YanaX.Love >= YanaX.Obed:
                                ch_y ". . . Тогда я не против."
                        elif YanaX.Obed >= YanaX.Inbt:
                                ch_y ". . . Тогда я не против."
                        else:
                                ch_y ". . . Тогда я не против."
                else:
                        $ YanaX.FaceChange("sad", 1)
                        ch_y "Я не могу на это пойти."
                        $ renpy.pop_call()
                        #This causes it to jump past the previous menu on the return

        "Я могу спросить, не будет ли она против, чтобы я встречалась с вами обеими." if "YanaYes" not in Player.Traits and not Player.Male:
                if ApprovalCheck(YanaX, 1800, Bonus = Cnt):
                        $ YanaX.FaceChange("smile", 1)
#                        if YanaX.Love >= YanaX.Obed:
#                            ch_y "Then I may consider it. . ."
#                        elif YanaX.Obed >= YanaX.Inbt:
#                            ch_y "Then I may consider it. . ."
#                        else:
#                            ch_y "Then sure, why not."
                        ch_y ". . ."
                        ch_y "Тогда поговорим после твоего разговора с ней."
                else:
                        $ YanaX.FaceChange("sad", 1)
                        ch_y ". . . Но даже в этом случае я не могу на это пойти."
                $ renpy.pop_call()

        "Я могу спросить, не будет ли она против, чтобы я встречался с вами обеими." if "YanaYes" not in Player.Traits and Player.Male:
                if ApprovalCheck(YanaX, 1800, Bonus = Cnt):
                        $ YanaX.FaceChange("smile", 1)
#                        if YanaX.Love >= YanaX.Obed:
#                            ch_y "Then I may consider it. . ."
#                        elif YanaX.Obed >= YanaX.Inbt:
#                            ch_y "Then I may consider it. . ."
#                        else:
#                            ch_y "Then sure, why not."
                        ch_y ". . ."
                        ch_y "Тогда поговорим после твоего разговора с ней."
                else:
                        $ YanaX.FaceChange("sad", 1)
                        ch_y ". . . Но даже в этом случае я не могу на это пойти."
                $ renpy.pop_call()

        "Если она не узнает, ничего плохого не случится.":
                if ApprovalCheck(YanaX, 1800, Bonus = -Cnt): #checks if Yana likes you more than the other girl
                        $ YanaX.FaceChange("smile", 1)
                        if YanaX.Love >= YanaX.Obed:
                                ch_y ". . . да. . ."
                        elif YanaX.Obed >= YanaX.Inbt:
                                ch_y "Раз ты настаиваешь. . ."
                        else:
                                ch_y "Это правда. . ."
                        $ YanaX.Traits.append("downlow")
                else:
                        $ YanaX.FaceChange("angry", 1)
                        if ApprovalCheck(YanaX, 1800):
                                ch_y "Но я не могу на это пойти."
                        else:
                                ch_y "Как жаль, что ты так думаешь."
                        $ renpy.pop_call()

        "Я могу порвать с ней.":
                    $ YanaX.FaceChange("sad")
                    ch_y "Потом дай мне знать, как все прошло."
                    $ renpy.pop_call()

        "Ты права, зря спросила." if not Player.Male:
                    $ YanaX.FaceChange("sad")
                    ch_y "Ага."
                    $ renpy.pop_call()

        "Ты права, зря спросил." if Player.Male:
                    $ YanaX.FaceChange("sad")
                    ch_y "Ага."
                    $ renpy.pop_call()

    return


label Yana_About(Check=0): #rkeljsvgbdw
    if Check not in TotalGirls:
            ch_y "Это кто?"
            return
    ch_y "Что я думаю о ней?"
    if Check == RogueX:
            if "poly Rogue" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeRogue >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeRogue >= 800:
                ch_y "Она чрезвычайно привлекательна, ты так не думаешь?"
            elif YanaX.LikeRogue >= 700:
                ch_y "Она очень хорошая подруга."
            elif YanaX.LikeRogue >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeRogue >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeRogue >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeRogue >= 300:
                ch_y "Я не выношу ее."
            else:
                ch_y "Она сука."
    elif Check == KittyX:
            if "poly Kitty" in YanaX.Traits:
                ch_y "У нас. . . очень близкие отношения. . ."
            elif YanaX.LikeKitty >= 900:
                ch_y "Надеюсь, мы с ней сможем стать больше, чем подругами. . ."
            elif YanaX.LikeKitty >= 800:
                ch_y "Она мне как сестра."
            elif YanaX.LikeKitty >= 700:
                ch_y "Она моя лучшая подруга."
            elif YanaX.LikeKitty >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeKitty >= 500:
                ch_y "Мы. . . друг другу безразличны. . ."
            elif YanaX.LikeKitty >= 400:
                ch_y "Мы. . . толком не общались. . ."
            else:
                ch_y "Она та еще шлюха."
    elif Check == LauraX:
            if "poly Laura" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeLaura >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeLaura >= 800:
                ch_y "Она чрезвычайно привлекательна, ты так не думаешь?"
            elif YanaX.LikeLaura >= 700:
                ch_y "Она очень хорошая подруга."
            elif YanaX.LikeLaura >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeLaura >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeLaura >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeLaura >= 300:
                ch_y "Мне с ней тяжело."
            else:
                ch_y "Она сука."
    elif Check == EmmaX:
            if "poly Emma" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeEmma >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeEmma >= 800:
                ch_y "Она замечательный человек, тебе так не кажется?"
            elif YanaX.LikeEmma >= 700:
                ch_y "She is a an excellent instructor."
            elif YanaX.LikeEmma >= 600:
                ch_y "Она достойный преподаватель."
            elif YanaX.LikeEmma >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeEmma >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeEmma >= 300:
                ch_y "Я не выношу эту женщину."
            else:
                ch_y "Она сука."
    elif Check == JeanX:
            if "poly Jean" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeJean >= 900:
                ch_y "Наверное, мне бы хотелось ее трахнуть, и даже больше."
            elif YanaX.LikeJean >= 800:
                ch_y "Я изо всех сил стараюсь ей сопереживать. . ."
            elif YanaX.LikeJean >= 700:
                ch_y "Мы. . . стараемся находить компромисс. . ."
            elif YanaX.LikeJean >= 600:
                ch_y "Она хорошая студентка, когда не выеживается."
            elif YanaX.LikeJean >= 500:
                ch_y "Мы. . . безразличны друг другу. Пока."
            elif YanaX.LikeJean >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeJean >= 300:
                ch_y "Я не выношу эту женщину."
            else:
                ch_y "Она сука."
    elif Check == StormX:
            if "poly Storm" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeStorm >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeStorm >= 800:
                ch_y "Она заботится обо мне. . ."
            elif YanaX.LikeStorm >= 700:
                ch_y "Она мой любимый преподаватель!"
            elif YanaX.LikeStorm >= 600:
                ch_y "Она достойный преподаватель."
            elif YanaX.LikeStorm >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeStorm >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeStorm >= 300:
                ch_y "Я не выношу эту женщину."
            else:
                ch_y "Она сука."
    elif Check == JubesX:
            if "poly Jubes" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeJubes >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeJubes >= 800:
                ch_y "Она очень милая, тебе так не кажется?"
            elif YanaX.LikeJubes >= 700:
                ch_y "Она очень хорошая подруга."
            elif YanaX.LikeJubes >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeJubes >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeJubes >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeJubes >= 300:
                ch_y "Я не выношу ее."
            else:
                ch_y "Она сука."
    elif Check == GwenX:
            if "poly Gwen" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeGwen >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeGwen >= 800:
                ch_y "Она очень милая, тебе так не кажется?"
            elif YanaX.LikeGwen >= 700:
                ch_y "Она довольно. . . милая. . ."
            elif YanaX.LikeGwen >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeGwen >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeGwen >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeGwen >= 300:
                ch_y "Я не выношу ее."
            else:
                ch_y "Она сука."
    elif Check == BetsyX:
            if "poly Betsy" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeBetsy >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeBetsy >= 800:
                ch_y "Она чрезвычайно привлекательна, ты так не думаешь?"
            elif YanaX.LikeBetsy >= 700:
                ch_y "Она очень стильная."
            elif YanaX.LikeBetsy >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeBetsy >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeBetsy >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeBetsy >= 300:
                ch_y "Я не выношу эту женщину."
            else:
                ch_y "Она сука."
    elif Check == DoreenX:
            if "poly Doreen" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeDoreen >= 900:
                ch_y "Я очень надеюсь стать с ней еще ближе."
            elif YanaX.LikeDoreen >= 800:
                ch_y "Она очень мягонькая, тебе так не кажется?"
            elif YanaX.LikeDoreen >= 700:
                ch_y "Она офигенная подруга."
            elif YanaX.LikeDoreen >= 600:
                ch_y "Она хорошая студентка."
            elif YanaX.LikeDoreen >= 500:
                ch_y "Мы. . . друг другу безразличны."
            elif YanaX.LikeDoreen >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeDoreen >= 300:
                ch_y "Я не выношу эту женщину."
            else:
                ch_y "Она сука."
    elif Check == WandaX:
            if "poly Wanda" in YanaX.Traits:
                ch_y "Мы. . . в отношениях. . ."
            elif YanaX.LikeWanda >= 900:
                ch_y "Возможно, я бы хотела как-нибудь ее трахнуть."
            elif YanaX.LikeWanda >= 800:
                ch_y "Мне бы хотелось с ней сблизиться. . ."
            elif YanaX.LikeWanda >= 700:
                ch_y "Я учусь у нее нескольким интересным заклинаниям. . ."
            elif YanaX.LikeWanda >= 600:
                ch_y "Мы. . . стараемся найти компромисс. . ."
            elif YanaX.LikeWanda >= 500:
                ch_y "Мы. . . безразличны друг другу. Пока."
            elif YanaX.LikeWanda >= 400:
                ch_y "Мы. . . толком не общались. . ."
            elif YanaX.LikeWanda >= 300:
                ch_y "Я не выношу эту женщину."
            else:
                ch_y "Она сука."
    else:
                ch_y "Я не знаю эту женщину."
    return
#End Yana_AboutEmma

label Yana_Monogamy: #rkeljsvgbdw
        #called from Yana_Settings to ask her not to hook up with other girls
        menu:
            "Не могла бы ты не встречаться с другими девушками?" if "mono" not in YanaX.Traits:
                    if YanaX.Thirst >= 60 and not ApprovalCheck(YanaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ YanaX.FaceChange("sly",1)
                            if "mono" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Obed", 90, -2)
                            ch_y "Если только я сама этого не захочу."
                            return
                    elif ApprovalCheck(YanaX, 1200, "LO", TabM=0) and YanaX.Love >= YanaX.Obed:
                            #she cares
                            $ YanaX.FaceChange("sly",1)
                            if "mono" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Love", 90, 1)
                            ch_y "Тогда мне нужно твое внимание. . ."
                    elif ApprovalCheck(YanaX, 700, "O", TabM=0):
                            #she is obedient
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y "Я. . . попробую. . ."
                    else:
                            #she doesn't care
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Если только я сама этого не захочу."
                            return
                    if "mono" not in YanaX.DailyActions:
                            $ YanaX.Statup("Obed", 90, 3)
                    $ YanaX.AddWord(1,0,"mono") #Daily
                    $ YanaX.Traits.append("mono")
            "Не встречайся с другими девушками." if "mono" not in YanaX.Traits:
                    if ApprovalCheck(YanaX, 900, "O", TabM=0):
                            #she is obedient
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y "Я. . . попробую. . ."
                    elif YanaX.Thirst >= 60 and not ApprovalCheck(YanaX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ YanaX.FaceChange("sly",1)
                            if "mono" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Obed", 90, -2)
                            ch_y "Если только я сама этого не захочу."
                            return
                    elif ApprovalCheck(YanaX, 600, "O", TabM=0):
                            #she is obedient
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y "Я. . . попробую. . ."
                    elif ApprovalCheck(YanaX, 1400, "LO", TabM=0):
                            #she cares
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Тогда мне нужно твое внимание. . ."
                    else:
                            #she doesn't care
                            $ YanaX.FaceChange("sly",1,Brows="confused")
                            ch_y "Если только я сама этого не захочу."
                            return
                    if "mono" not in YanaX.DailyActions:
                            $ YanaX.Statup("Obed", 90, 3)
                    $ YanaX.AddWord(1,0,"mono") #Daily
                    $ YanaX.Traits.append("mono")
            "Ничего страшного, если ты будешь встречаться с другими девушками." if "mono" in YanaX.Traits:
                    if ApprovalCheck(YanaX, 700, "O", TabM=0):
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y "Хорошо."
                    elif ApprovalCheck(YanaX, 800, "L", TabM=0):
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Конечно. . ."
                    else:
                            $ YanaX.FaceChange("sly",1,Brows="confused")
                            if "mono" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Love", 90, -2)
                            ch_y "Хорошо."
                    if "mono" not in YanaX.DailyActions:
                            $ YanaX.Statup("Obed", 90, 3)
                    if "mono" in YanaX.Traits:
                            $ YanaX.Traits.remove("mono")
                    $ YanaX.AddWord(1,0,"mono") #Daily
            "Неважно.":
                pass
        return

# end Yana monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Yana_Jumped: #rkeljsvgbdw
        #called from Yana_Settings to ask her not to jump you
        ch_p "Слушай, помнишь, как ты накинулась на меня?"
        $ YanaX.FaceChange("sly",1,Brows="confused")
        menu:
            ch_y "Ты что-то хочешь сказать по этому поводу?"
            "На будущее, можешь сначала спрашивать?" if "chill" not in YanaX.Traits:
                    if YanaX.Thirst >= 60 and not ApprovalCheck(YanaX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ YanaX.FaceChange("sly",1)
                            if "chill" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Obed", 90, -2)
                            ch_y "Это зависит от многого. . ."
                            return
                    elif ApprovalCheck(YanaX, 1000, "LO", TabM=0) and YanaX.Love >= YanaX.Obed:
                            #she cares
                            $ YanaX.FaceChange("surprised",1)
                            if "chill" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Love", 90, 1)
                            ch_y "Мне нужно удовлетворять свои потребности. . ."
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y "-но я попробую. . ."
                    elif ApprovalCheck(YanaX, 500, "O", TabM=0):
                            #she is obedient
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y ". . . что ж, хорошо. . ."
                    else:
                            #she doesn't care
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Посмотрим . ."
                            return
                    if "chill" not in YanaX.DailyActions:
                            $ YanaX.Statup("Obed", 90, 3)
                    $ YanaX.AddWord(1,0,"chill") #Daily
                    $ YanaX.Traits.append("chill")
            "Больше так не делай." if "chill" not in YanaX.Traits:
                    if ApprovalCheck(YanaX, 800, "O", TabM=0):
                            #she is obedient
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            ch_y ". . . что ж, хорошо. . ."
                    elif YanaX.Thirst >= 60 and not ApprovalCheck(YanaX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ YanaX.FaceChange("sly",1)
                            if "chill" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Obed", 90, -2)
                            ch_y "Это зависит от многого. . ."
                            return
                    elif ApprovalCheck(YanaX, 400, "O", TabM=0):
                            #she is obedient
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_y "Да, госпожа . ."
                            else:
                                ch_y "Да, господин. . ."
                    elif ApprovalCheck(YanaX, 500, "LO", TabM=0) and not ApprovalCheck(YanaX, 500, "I", TabM=0):
                            #she cares
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Ах. . ."
                            ch_y "Тогда извини."
                    else:
                            #she doesn't care
                            $ YanaX.FaceChange("sly",1)
                            ch_y "О, чепуха, ты привыкнешь."
                            return
                    if "chill" not in YanaX.DailyActions:
                            $ YanaX.Statup("Obed", 90, 3)
                    $ YanaX.AddWord(1,0,"chill") #Daily
                    $ YanaX.Traits.append("chill")
            "Делай что хочешь.":
                    if ApprovalCheck(YanaX, 800, "L", TabM=0):
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Замечательно!"
                    elif ApprovalCheck(YanaX, 700, "O", TabM=0):
                            $ YanaX.FaceChange("sly",1,Eyes="side")
                            if not Player.Male:
                                ch_y "Конечно, госпожа."
                            else:
                                ch_y "Конечно, господин."
                    else:
                            $ YanaX.FaceChange("sly",1,Brows="confused")
                            if "chill" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Love", 90, -2)
                            ch_y "Посмотрим. . ."
                    if "chill" not in YanaX.DailyActions:
                            $ YanaX.Statup("Obed", 90, 3)
                    if "chill" in YanaX.Traits:
                            $ YanaX.Traits.remove("chill")
                    $ YanaX.AddWord(1,0,"chill") #Daily
            "Эм, неважно.":
                pass
        return

# end Yana jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start Yana hungry //////////////////////////////////////////////////////////
label Yana_Hungry: #rkeljsvgbdw
    if YanaX.Chat[3]:
        ch_y "И снова я жажду добавки. . ."
    elif YanaX.Chat[2]:
        ch_y "Твоя \"сыворотка\" очень вкусная. . ."
    else:
        ch_y "Я жажду попробовать еще раз. . ."
        ch_y "Не заставляй меня ждать. . ."
    $ YanaX.Traits.append("hungry")
return


# end Yana hungry //////////////////////////////////////////////////////////

# Yana Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Yana_SexChat: #rkeljsvgbdw
    $ Line = "Что ты желаешь обсудить?" if not Line else Line
    while True:
            menu:
                ch_y "[Line]"
                "Мое любимое занятие - это. . .":
                    if "setfav" in YanaX.DailyActions:
                        ch_y "Конечно."
                    else:
                        menu:
                            "Вагинальный секс.":
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "sex":
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "Я знаю. . ."
                                        elif YanaX.Favorite == "sex":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 10)
                                            ch_y "Я понимаю."
                                        elif YanaX.Sex >= 5:
                                            ch_y "Что ж, ничего не имею против."
                                        elif not YanaX.Sex:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "С кем ты занимаешься сексом?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "О, да. . ."
                                        $ YanaX.PlayerFav = "sex"

                            "Анальный секс.":
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "anal":
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "anal":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 10)
                                            ch_y "У меня тоже!"
                                        elif YanaX.Anal >= 10:
                                            ch_y "Да. . ."
                                        elif not YanaX.Anal:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто был не против этого?"
                                        else:
                                            $ YanaX.FaceChange("bemused",Eyes="side")
                                            ch_y "О, да. . ."
                                        $ YanaX.PlayerFav = "anal"

                            "Минет." if Player.Male:
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "blow":
                                            $ YanaX.Statup("Lust", 80, 3)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "blow":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "У меня тоже!"
                                        elif YanaX.Blow >= 10:
                                            ch_y "Да, ты -очень- вкусный."
                                        elif not YanaX.Blow:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто сосет твой член?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Конечно. . ."
                                        $ YanaX.PlayerFav = "blow"
                            "Куни." if not Player.Male:
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "cun":
                                            $ YanaX.Statup("Lust", 80, 3)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "cun":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "У меня тоже!"
                                        elif YanaX.CUN >= 10:
                                            ch_y "Да, ты -очень- вкусная."
                                        elif not YanaX.CUN:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто лижет твою киску?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Конечно. . ."
                                        $ YanaX.PlayerFav = "cun"

                            "Сиськотрах." if Player.Male:
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "titjob":
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "titjob":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 7)
                                            ch_y "У меня тоже!"
                                        elif YanaX.Tit >= 10:
                                            ch_y "Это очень весело. . ."
                                        elif not YanaX.Tit:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто занимается этим с тобой?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Конечно. . ."
                                            $ YanaX.Statup("Love", 80, 5)
                                            $ YanaX.Statup("Inbt", 50, 10)
                                        $ YanaX.PlayerFav = "titjob"

                            "Дрочка ногами.":
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "foot":
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "foot":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 7)
                                            ch_y "У меня тоже!"
                                        elif YanaX.Foot >= 10:
                                            ch_y "Мне очень нравится это делать с тобой. . ."
                                        elif not YanaX.Foot:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто занимается этим с тобой?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Да, это довольно интересно. . ."
                                        $ YanaX.PlayerFav = "foot"

                            "Дрочка рукой." if Player.Male:
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "hand":
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "hand":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 7)
                                            ch_y "У меня тоже."
                                        elif YanaX.Hand >= 10:
                                            ch_y "Мне тоже это нравится. . ."
                                        elif not YanaX.Hand:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто занимается этим с тобой?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Да, это довольно интересно. . ."
                                        $ YanaX.PlayerFav = "hand"
                            "Когда ласкают пальчиками мою киску." if not Player.Male:
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "finger":
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite == "finger":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 7)
                                            ch_y "Мне тоже это очень нравится."
                                        elif YanaX.Finger >= 10:
                                            ch_y "Мне тоже это нравится. . ."
                                        elif not YanaX.Finger:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Кто занимается этим с тобой?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Да, это довольно интересно. . ."
                                        $ YanaX.PlayerFav = "finger"

                            "Ласкать тебя.":
                                        $ Cnt = YanaX.FondleB + YanaX.FondleT + YanaX.SuckB + YanaX.Hotdog
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "fondle":
                                            $ YanaX.Statup("Lust", 80, 3)
                                            ch_y "Я это знаю. . ."
                                        elif YanaX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "А мне нравится, когда ты ласкаешь меня!"
                                        elif Cnt >= 10:
                                            ch_y "Мне тоже это нравится. . ."
                                        elif not Cnt:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "Мне тяжело это представить."
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Да, это довольно приятно. . ."
                                        $ YanaX.PlayerFav = "fondle"
                                        $ Cnt = 0

                            "Поцелуи.":
                                        $ YanaX.FaceChange("sly")
                                        if YanaX.PlayerFav == "kiss you":
                                            $ YanaX.Statup("Love", 90, 3)
                                            if not Player.Male:
                                                ch_y "Ты очаровательна. . ."
                                            else:
                                                ch_y "Ты очарователен. . ."
                                        elif YanaX.Favorite == "kiss you":
                                            $ YanaX.Statup("Love", 90, 5)
                                            $ YanaX.Statup("Lust", 80, 5)
                                            ch_y "У тебя это неплохо получается."
                                        elif YanaX.Kissed >= 10:
                                            ch_y "Мне это тоже нравится. . ."
                                        elif not YanaX.Kissed:
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y "С кем ты целуешься?"
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            ch_y "Мне это тоже нравится. . ."
                                        $ YanaX.PlayerFav = "kiss you"

                        $ YanaX.DailyActions.append("setfav")

                "Что тебе больше всего нравится?":
                                if not ApprovalCheck(YanaX, 800):
                                            $ YanaX.FaceChange("perplexed")
                                            ch_y ". . ."
                                else:
                                        if YanaX.SEXP >= 50:
                                            $ YanaX.FaceChange("sly")
                                            if not Player.Male:
                                                ch_y "Ты должна уже это знать. . ."
                                            else:
                                                ch_y "Ты должен уже это знать. . ."
                                        else:
                                            $ YanaX.FaceChange("bemused")
                                            $ YanaX.Eyes = "side"
                                            ch_y "Хмм. . ."


                                        if not YanaX.Favorite or YanaX.Favorite == "kiss":
                                                ch_y "Поцелуи. . ."
                                        elif YanaX.Favorite == "anal":
                                                ch_y "Анальный секс, пожалуй?"
                                        elif YanaX.Favorite == "lick ass":
                                                ch_y "Когда ты. . . вылизываешь мой анус, пожалуй?"
                                        elif YanaX.Favorite == "insert ass":
                                                ch_y "Когда ты вставляешь палец мне в попку. . ."
                                        elif YanaX.Favorite == "sex":
                                                ch_y "Обожаю, когда ты входишь в меня."
                                        elif YanaX.Favorite == "lick pussy":
                                                ch_y "Ты -очень- хорошо лижешь киску."
                                        elif YanaX.Favorite == "fondle pussy":
                                                ch_y "Ты -очень- хорошо работаешь пальцами."
                                        elif YanaX.Favorite == "blow":
                                                ch_y "Обожаю сосать твой член."
                                        elif YanaX.Favorite == "cun":
                                                ch_y "Обожаю лизать твою киску."
                                        elif YanaX.Favorite == "tit":
                                                ch_y "Дрочить сиськами очень весело."
                                        elif YanaX.Favorite == "foot":
                                                ch_y "Обожаю дрочить ногами."
                                        elif YanaX.Favorite == "hand":
                                                ch_y "Мне нравится дрочить тебе."
                                        elif YanaX.Favorite == "finger":
                                                ch_y "Мне нравится ласкать твою киску."
                                        elif YanaX.Favorite == "hotdog":
                                                ch_y "Мне нравится, когда ты трешься о меня."
                                        elif YanaX.Favorite == "suck breasts":
                                                ch_y "Мне нравится, когда ты сосешь мои сиськи."
                                        elif YanaX.Favorite == "fondle breasts":
                                                ch_y "Мне нравится, когда ты мнешь мои сиськи."
                                        elif YanaX.Favorite == "fondle thighs":
                                                ch_y "Мне нравится, когда ты гладишь мои ноги."
                                        else:
                                                ch_y "Я. . . не хочу отвечать на этот вопрос. . ."

                                # End Yana's favorite things.

                "Не болтай так много во время секса." if "vocal" in YanaX.Traits:
                        if "setvocal" in YanaX.DailyActions:
                                $ YanaX.FaceChange("perplexed")
                                ch_y "Разберись, чего ты хочешь."
                        else:
                            if ApprovalCheck(YanaX, 1000) and YanaX.Obed <= YanaX.Love:
                                $ YanaX.FaceChange("bemused")
                                $ YanaX.Statup("Obed", 90, 1)
                                ch_y ". . ."
                                $ YanaX.Traits.remove("vocal")
                            elif ApprovalCheck(YanaX, 700, "O"):
                                $ YanaX.FaceChange("sadside")
                                $ YanaX.Statup("Obed", 90, 1)
                                ch_y ". . ."
                                $ YanaX.Traits.remove("vocal")
                            elif ApprovalCheck(YanaX, 600):
                                $ YanaX.FaceChange("sly")
                                $ YanaX.Statup("Love", 90, -3)
                                $ YanaX.Statup("Obed", 50, -1)
                                $ YanaX.Statup("Inbt", 90, 5)
                                ch_y "Я буду говорить то, что захочу."
                            else:
                                $ YanaX.FaceChange("angry")
                                $ YanaX.Statup("Love", 90, -5)
                                $ YanaX.Statup("Obed", 60, -3)
                                $ YanaX.Statup("Inbt", 90, 10)
                                ch_y "Я буду говорить то, что захочу."

                            $ YanaX.DailyActions.append("setvocal")
                "Говори мне пошлости во время секса." if "vocal" not in YanaX.Traits:
                        if "setvocal" in YanaX.DailyActions:
                                $ YanaX.FaceChange("perplexed")
                                ch_y "Прими решение."
                        else:
                            if ApprovalCheck(YanaX, 1000) and YanaX.Obed <= YanaX.Love:
                                $ YanaX.FaceChange("sly")
                                $ YanaX.Statup("Obed", 90, 2)
                                ch_y "Это я могу."
                                $ YanaX.Traits.append("vocal")
                            elif ApprovalCheck(YanaX, 700, "O"):
                                $ YanaX.FaceChange("sadside")
                                $ YanaX.Statup("Obed", 90, 2)
                                ch_y "Это я могу."
                                $ YanaX.Traits.append("vocal")
                            elif ApprovalCheck(YanaX, 600):
                                $ YanaX.FaceChange("sly")
                                $ YanaX.Statup("Obed", 90, 3)
                                ch_y "Ладно?"
                                $ YanaX.Traits.append("vocal")
                            else:
                                $ YanaX.FaceChange("angry")
                                $ YanaX.Statup("Inbt", 90, 5)
                                ch_y ". . ."

                            $ YanaX.DailyActions.append("setvocal")
                        # End Yana Dirty Talk

                "Проявляй меньше инициативы во время секса." if "passive" not in YanaX.Traits:
                        if "initiative" in YanaX.DailyActions:
                                $ YanaX.FaceChange("perplexed")
                                ch_y "Прими решение."
                        else:
                            if ApprovalCheck(YanaX, 1200) and YanaX.Obed <= YanaX.Love:
                                $ YanaX.FaceChange("bemused")
                                $ YanaX.Statup("Obed", 90, 1)
                                ch_y "Тогда делай мне приятно."
                                $ YanaX.Traits.append("passive")
                            elif ApprovalCheck(YanaX, 700, "O"):
                                $ YanaX.FaceChange("sadside")
                                $ YanaX.Statup("Obed", 90, 1)
                                ch_y "Тогда все на тебе."
                                $ YanaX.Traits.append("passive")
                            elif ApprovalCheck(YanaX, 600):
                                $ YanaX.FaceChange("sly")
                                $ YanaX.Statup("Love", 90, -3)
                                $ YanaX.Statup("Obed", 50, -1)
                                $ YanaX.Statup("Inbt", 90, 5)
                                ch_y "Посмотрим."
                            else:
                                $ YanaX.FaceChange("angry")
                                $ YanaX.Statup("Love", 90, -5)
                                $ YanaX.Statup("Obed", 60, -3)
                                $ YanaX.Statup("Inbt", 90, 10)
                                ch_y "Посмотрим."

                            $ YanaX.DailyActions.append("initiative")
                "Проявляй больше инициативы во время секса." if "passive" in YanaX.Traits:
                        if "initiative" in YanaX.DailyActions:
                                $ YanaX.FaceChange("perplexed")
                                ch_y "Прими решение."
                        else:
                            if ApprovalCheck(YanaX, 1000) and YanaX.Obed <= YanaX.Love:
                                $ YanaX.FaceChange("bemused")
                                $ YanaX.Statup("Obed", 90, 1)
                                ch_y "Это я могу."
                                $ YanaX.Traits.remove("passive")
                            elif ApprovalCheck(YanaX, 700, "O"):
                                $ YanaX.FaceChange("sadside")
                                $ YanaX.Statup("Obed", 90, 1)
                                ch_y "Это я могу."
                                $ YanaX.Traits.remove("passive")
                            elif ApprovalCheck(YanaX, 600):
                                $ YanaX.FaceChange("sly")
                                $ YanaX.Statup("Obed", 90, 3)
                                ch_y "Посмотрим."
                                $ YanaX.Traits.remove("passive")
                            else:
                                $ YanaX.FaceChange("angry")
                                $ YanaX.Statup("Inbt", 90, 5)
                                ch_y "Посмотрим."

                            $ YanaX.DailyActions.append("initiative")

                "О том, как ты накидываешься" if "jumped" in YanaX.History:
                        call Yana_Jumped
                "О твоей мастурбации":
                        call NoFap(YanaX)

                "Всегда носи вибратор" if "dailyvibe" not in YanaX.Traits:
                        call Daily_Vibrator(YanaX)
                "Перестань всегда носить вибратор" if "dailyvibe" in YanaX.Traits:
                        ch_y "Что ж, хорошо. . ."
                        $ YanaX.DrainWord("dailyvibe",0,0,1) #removes from traits

                "Всегда носи анальную пробку" if "dailyplug" not in YanaX.Traits:
                        call Daily_Plug(YanaX)
                "Перестань всегда носить анальную пробку" if "dailyplug" in YanaX.Traits:
                        ch_y "Что ж, хорошо. . ."
                        $ YanaX.DrainWord("dailyplug",0,0,1) #removes from traits

                "Неважно" if Line == "Что ты желаешь обсудить?":
                        return
                "На этом все." if Line != "Что ты желаешь обсудить?":
                        return
            if Line == "Что ты желаешь обсудить?":
                $ Line = "Что-нибудь еще?"
    return
# End Yana Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Yana Chitchat /////////////////// #Work in progress
label Yana_Chitchat(O=0, Options = ["default","default","default"]): #rkeljsvg
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if YanaX not in Digits:
                if ApprovalCheck(YanaX, 500, "L") or ApprovalCheck(YanaX, 250, "I"):
                    ch_y "У тебя должен быть мой номер телефона."
                    $ Digits.append(YanaX)
                    return
                elif ApprovalCheck(YanaX, 250, "O"):
                    ch_y "У тебя должен быть мой номер телефона."
                    $ Digits.append(YanaX)
                    return

        if "hungry" not in YanaX.Traits and (YanaX.Swallow + YanaX.Chat[2]) >= 10 and YanaX.Loc == bg_current:  #She's swallowed a lot
                    call Yana_Hungry
                    return

        if bg_current != "bg restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(YanaX, 700, "I")):
                    if YanaX.Loc == bg_current and YanaX.Thirst >= 30 and "refused" not in YanaX.DailyActions and "quicksex" not in YanaX.DailyActions:
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Может, развлечемся?"
                            call Quick_Sex(YanaX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
        if PunishmentX and "caught chat" not in YanaX.DailyActions:
            $ Options.append("caught")
        if YanaX.Event[0] and "key" not in YanaX.Chat:
            $ Options.append("key")

        if "mandrill" in Player.Traits and "cologne chat" not in YanaX.DailyActions:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in YanaX.DailyActions:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in YanaX.DailyActions:
            $ Options.append("corruption")

#        if "Yana" not in YanaX.Names:
#            $ Options.append("yana")

        if YanaX.Date >= 1 and bg_current != "bg restaurant":
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in YanaX.DailyActions and "cheek" not in YanaX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if YanaX.Kissed >= 5 and YanaX.Loc == bg_current:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in YanaX.DailyActions and (Player.Male or "girltalk" in YanaX.History):
            #If you've caught Yana showering today
            $ Options.append("showercaught")
        if "fondle breasts" in YanaX.DailyActions or "fondle pussy" in YanaX.DailyActions or "fondle ass" in YanaX.DailyActions:
            #If you've fondled Yana today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in YanaX.Inventory and "256 Shades of Grey" in YanaX.Inventory and "Avengers Tower Penthouse" in YanaX.Inventory:
            #If you've given Yana the books
            if "book" not in YanaX.Chat:
                $ Options.append("booked")
        if "lace bra" in YanaX.Inventory or "lace panties" in YanaX.Inventory:
            #If you've given Yana the lingerie
            if "lingerie" not in YanaX.Chat:
                $ Options.append("lingerie")
        if YanaX.Hand and Player.Male:
            #If Yana's given a handjob
            $ Options.append("handy")
        if YanaX.Blow and Player.Male:
            #If Yana's given a blowjob
            $ Options.append("blow")
        if YanaX.Swallow:
            #If Yana's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in YanaX.DailyActions or "painted" in YanaX.DailyActions:
            #If Yana's been facialed
            $ Options.append("facial")
        if YanaX.Sleep:
            #If Yana's slept over
            $ Options.append("sleep")
        if (YanaX.CreamP or YanaX.CreamA) and Player.Male:
            #If Yana's been creampied
            $ Options.append("creampie")
        if YanaX.Sex or YanaX.Anal:
            #If Yana's been sexed
            $ Options.append("sexed")
        if YanaX.Anal:
            #If Yana's been analed
            $ Options.append("anal")

        if "seenpeen" in YanaX.History and Player.Male:
            $ Options.append("seenpeen")
        if "topless" in YanaX.History:
            $ Options.append("topless")
        if "bottomless" in YanaX.History:
            $ Options.append("bottomless")

#        if not YanaX.Chat[0] and YanaX.Sex:
#            $ Options.append("virgin")

#        if (bg_current == "bg yana" or bg_current == "bg player") and "relationship" not in YanaX.DailyActions:
#            if "lover" not in YanaX.Petnames and ApprovalCheck(YanaX, 900, "L"): # YanaX.Event[6]
#                $ Options.append("lover?")
#            elif "sir" not in YanaX.Petnames and ApprovalCheck(YanaX, 500, "O"): # YanaX.Event[7]
#                $ Options.append("sir?")
#            elif "daddy" not in YanaX.Petnames and ApprovalCheck(YanaX, 750, "L") and ApprovalCheck(YanaX, 500, "O") and ApprovalCheck(YanaX, 500, "I"): # YanaX.Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in YanaX.Petnames and ApprovalCheck(YanaX, 900, "O"): # YanaX.Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in YanaX.Petnames and ApprovalCheck(YanaX, 500, "I"): # YanaX.Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in YanaX.Petnames and ApprovalCheck(YanaX, 900, "I"): # YanaX.Event[10]
#                $ Options.append("fuckbuddy?")


        if not ApprovalCheck(YanaX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ YanaX.DailyActions.append("cologne chat")
        $ YanaX.FaceChange("confused")
        ch_y "(нюх, нюх). . . отдает. . . мускусом . . ."
        $ YanaX.FaceChange("sexy", 2)
        ch_y ". . . пожалуй. . . я ничего не имею против? . ."
    elif Options[0] == "purple":
        $ YanaX.DailyActions.append("cologne chat")
        $ YanaX.FaceChange("sly",1)
        ch_y "(нюх, нюх). . . что это за запах? . ."
        $ YanaX.FaceChange("normal",0)
        ch_y ". . . ты чего-то от меня хочешь?"
    elif Options[0] == "corruption":
        $ YanaX.DailyActions.append("cologne chat")
        $ YanaX.FaceChange("confused")
        ch_y "(нюх, нюх). . . сильный запах. . ."
        $ YanaX.FaceChange("angry",Eyes="psychic")
        ch_y ". . . Напоминает мне о. . . Беласко. . ."
        $ YanaX.FaceChange("sly")

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in YanaX.Chat:
                    ch_y "Я не хочу, чтобы у меня здесь были проблемы!"
                    if not ApprovalCheck(YanaX, 500, "I"):
                         ch_y "Хотя это напомнило мне о моей молодости. . ."
            else:
                    ch_y "Я не хочу, чтобы у меня здесь были проблемы!"
                    if not ApprovalCheck(YanaX, 500, "I"):
                        ch_y "Пожалуй, нам не стоит заниматься подобным в общественных местах. . ."
                    else:
                         ch_y "-но это было весело. . ."
                    $ YanaX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if YanaX.SEXP <= 15:
                ch_y "Ты навещаешь меня недостаточно часто. . ."
            else:
                ch_y "Ты навещаешь меня недостаточно часто. . ."
            $ YanaX.Chat.append("key")

    elif Options[0] == "dated":
            #Yana's response to having gone on a date with the Player.
            call Girl_Ask_Date #asks if you want to go on another date sometime.

    elif Options[0] == "kissed":
            #Yana's response to having been kissed by the Player.
            $ YanaX.FaceChange("normal",1)
            ch_y "Тебе понравилось целовать меня, [YanaX.Petname]?"
            menu:
                extend ""
                "Наверное?":
                        $ YanaX.FaceChange("smile",1)
                        ch_y "Что ж, хорошо."
                        call SexAct("kissing")
                "Конечно.":
                        $ YanaX.FaceChange("smile",1)
                        ch_y ". . ."
                        call SexAct("kissing")
                "Думаю, с тебя хватит.":
                        $ YanaX.FaceChange("sad",1)
                        ch_y "Жаль."

    elif Options[0] == "dangerroom":
            #Yana's response to Player working out in the Danger Room while Yana is present
            $ YanaX.FaceChange("sly",1)
            ch_y "Я видела твою тренировку."
            ch_y "У тебя впечатляющая форма."

    elif Options[0] == "showercaught":
            #Yana's response to being caught in the shower.
            if "shower" in YanaX.Chat:
                ch_y "Я постоянно натыкаюсь на тебя в душе. . ."
            else:
                ch_y "Я постоянно натыкаюсь на тебя в душе. . ."
                ch_y "Ты. . . заходишь намеренно?"
                $ YanaX.Chat.append("shower")
                menu:
                    extend ""
                    "Это была чистая случайность! Клянусь!":
                            $ YanaX.Statup("Love", 50, 5)
                            $ YanaX.Statup("Love", 90, 2)
                            if ApprovalCheck(YanaX, 1200):
                                $ YanaX.FaceChange("sly",1)
                                ch_y "Конечно. . ."
                                ch_y "К слову, я ничего против не имею. . ."
                            else:
                                $ YanaX.FaceChange("smile")
                                ch_y "Понятно. . ."
                    "Только, если там ты.":
                            $ YanaX.Statup("Obed", 40, 5)
                            if ApprovalCheck(YanaX, 1000) or ApprovalCheck(YanaX, 700, "L"):
                                    $ YanaX.Statup("Love", 90, 3)
                                    $ YanaX.FaceChange("surprised",2,Mouth="normal")
                                    ch_y "Ах. . ."
                                    $ YanaX.FaceChange("sly",1)
                                    ch_y ". . . спасибо?"
                            else:
                                    $ YanaX.Statup("Love", 70, -5)
                                    $ YanaX.FaceChange("angry")
                                    ch_y "Я не нахожу твой комментарий \"милым\". . ."
                    "Я заглянула умышленно. Но я ни о чем не жалею." if not Player.Male:
                            if ApprovalCheck(YanaX, 1200):
                                    $ YanaX.Statup("Love", 90, 3)
                                    $ YanaX.Statup("Obed", 70, 10)
                                    $ YanaX.Statup("Inbt", 50, 5)
                                    $ YanaX.FaceChange("sly",1)
                                    ch_y "Я впечатлена."
                            elif ApprovalCheck(YanaX, 800):
                                    $ YanaX.Statup("Obed", 60, 5)
                                    $ YanaX.Statup("Inbt", 50, 5)
                                    $ YanaX.FaceChange("perplexed",2)
                                    ch_y ". . . что ж, хорошо. . ."
                                    $ YanaX.Blush = 1
                            else:
                                    $ YanaX.Statup("Love", 50, -10)
                                    $ YanaX.Statup("Love", 80, -10)
                                    $ YanaX.Statup("Obed", 50, 10)
                                    $ YanaX.FaceChange("angry")
                                    ch_y "Ты странно рассуждаешь."
                    "Я заглянул умышленно. Но я ни о чем не жалею." if Player.Male:
                            if ApprovalCheck(YanaX, 1200):
                                    $ YanaX.Statup("Love", 90, 3)
                                    $ YanaX.Statup("Obed", 70, 10)
                                    $ YanaX.Statup("Inbt", 50, 5)
                                    $ YanaX.FaceChange("sly",1)
                                    ch_y "Я впечатлена."
                            elif ApprovalCheck(YanaX, 800):
                                    $ YanaX.Statup("Obed", 60, 5)
                                    $ YanaX.Statup("Inbt", 50, 5)
                                    $ YanaX.FaceChange("perplexed",2)
                                    ch_y ". . . что ж, хорошо. . ."
                                    $ YanaX.Blush = 1
                            else:
                                    $ YanaX.Statup("Love", 50, -10)
                                    $ YanaX.Statup("Love", 80, -10)
                                    $ YanaX.Statup("Obed", 50, 10)
                                    $ YanaX.FaceChange("angry")
                                    ch_y "Ты странно рассуждаешь."

    elif Options[0] == "fondled":
            #Yana's response to being felt up.
            if YanaX.FondleB + YanaX.FondleP + YanaX.FondleA >= 15:
                ch_y "Я не буду возражать, если ты захочешь прикасаться ко мне чаще. . ."
            else:
                ch_y "Тебе бы хотелось снова прикоснуться к моему телу?"

    elif Options[0] == "booked":
            #Yana's response after a Player gives her the books from the shop.
            if not Player.Male:
                ch_y "Я прочитала книги, которые ты мне дала. . ."
            else:
                ch_y "Я прочитала книги, которые ты мне дал. . ."
            menu:
                extend ""
                "Да? Они тебе понравились?":
                        $ YanaX.FaceChange("sly",1)
                        ch_y "Они были очень занимательными. . ."
                "Хорошо. Пожалуй, ты могла бы чему-нибудь из них научиться.":
                        $ YanaX.Statup("Obed", 70, 5)
                        $ YanaX.Statup("Inbt", 50, 5)
                        $ YanaX.FaceChange("surprised",1)
                        ch_y "Я. . . не уверена, насколько информация в них достоверна."
#            $ YanaX.Blush = 1
            $ YanaX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Yana's response to being given lingerie.
            $ YanaX.FaceChange("sly",1)
            if not Player.Male:
                ch_y "Мне нравится нижнее белье, которое ты купила."
            else:
                ch_y "Мне нравится нижнее белье, которое ты купил."
            ch_y "Оно такое откровенное. . ."
            $ YanaX.Blush = 1
            $ YanaX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Yana's response after giving the Player a handjob.
            $ YanaX.FaceChange("sly",1)
            ch_y "Если ты хочешь, чтобы я снова тебе подрочила, только попроси. . ."

    elif Options[0] == "blow":
            if "blow" not in YanaX.Chat:
                    #Yana's response after giving the Player a blowjob.
                    $ YanaX.FaceChange("sly",2)
                    ch_y "Я хорошо делаю минет, да?"
                    menu:
                        extend ""
                        "Очень. Очень хорошо.":
                                    $ YanaX.Statup("Love", 90, 5)
                                    $ YanaX.Statup("Inbt", 60, 10)
                                    $ YanaX.FaceChange("sly",1,Eyes="side")
                                    ch_y "Я ожидала такой ответ."
                                    $ YanaX.FaceChange("sexy",1)
                                    ch_y "Дай мне знать, если захочешь повторить. . ."
                        "Честно? Все было хорошо. . . но, думаю, тебе нужно больше практики.":
                                if ApprovalCheck(YanaX, 300, "I") or not ApprovalCheck(YanaX, 800):
                                    $ YanaX.Statup("Love", 90, -5)
                                    $ YanaX.Statup("Obed", 60, 10)
                                    $ YanaX.Statup("Inbt", 50, 10)
                                    $ YanaX.FaceChange("perplexed",1)
                                    ch_y "Ах. Мне нравятся вызовы. . ."
                                else:
                                    $ YanaX.Statup("Obed", 70, 15)
                                    $ YanaX.Statup("Inbt", 50, 5)
                                    $ YanaX.FaceChange("sexy",1)
                                    ch_y "Хммм. . . -я- думала, что у меня это очень хорошо получается. . ."
                        "Угу, если бы мне нравились стремные звуки и шкрябанье зубов по члену, но это далеко не так.":
                                    $ YanaX.Statup("Love", 70, -5)
                                    $ YanaX.Statup("Love", 90, -10)
                                    $ YanaX.Statup("Obed", 60, 10)
                                    $ YanaX.FaceChange("angry",2)
                                    ch_y ". . ."
                                    ch_y "Я не издаю \"стремные звуки.\""
                                    $ YanaX.FaceChange("sly",1)
                                    $ YanaX.Statup("Inbt", 50, 5)
                                    ch_y "И тебе -понравилось- \"шкрябанье зубов.\""
                    $ YanaX.Blush = 1
                    $ YanaX.Chat.append("blow")
            else:
                    $ Line = renpy.random.choice(["Мне нужно снова отсосать у тебя.",
                            "Меня все еще беспокоит боль в челюсти.",
                            "Хочешь, чтобы тебе как-нибудь снова отсосали?",
                            "Хммм. . . [Стучит языком по внутренней стороне щеки.]"])
                    ch_y "[Line]"

    elif Options[0] == "swallowed":
            #Yana's response after swallowing the Player's cum.
            if "swallow" in YanaX.Chat:
                $ YanaX.FaceChange("sly",1)
                if not Player.Male:
                    ch_y "Я бы не отказалась как-нибудь снова проглотить твои соки."
                else:
                    ch_y "Я бы не отказалась как-нибудь снова проглотить твою сперму."
            else:
                $ YanaX.FaceChange("confused",1,Mouth="normal")
                if not Player.Male:
                    ch_y "Ты знала, что. . . у твоих соков неповторимый вкус?"
                else:
                    ch_y "Ты знал, что. . . у твоей спермы неповторимый вкус?"
                $ YanaX.FaceChange("normal",1)
                ch_y "Должно быть, здесь не обошлось без какой-то магии. . ."
                $ YanaX.FaceChange("sly",1)
                ch_y ". . ."
                $ YanaX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Yana's response after taking a facial from the Player.
            ch_y "Я знаю, что это необычная просьба. . ."
            $ YanaX.FaceChange("sexy",2)
            if not Player.Male:
                ch_y "-но мне бы хотелось, чтобы ты снова покрыла мое лицо своими соками."
            else:
                ch_y "-но мне бы хотелось, чтобы ты снова покрыл мое лицо своей спермой."
            ch_y ". . ."
            $ YanaX.Blush = 1

    elif Options[0] == "sleepover":
            #Yana's response after sleeping with the Player.
            ch_y "Мне -очень- понравилась та ночь."
            ch_y "Приятно, что порой можно не спать в одиночестве. . ."

    elif Options[0] == "creampie":
            #Another of Yana's responses after having sex with the Player.
            "[YanaX.Name] сближается с вами, чтобы прошептать вам на ухо."
            ch_y "Мне нравится, как твое семя стекает по моим бедрам."

    elif Options[0] == "sexed":
            #A final response from Yana after having sex with the Player.
            $ YanaX.FaceChange("sly",2,Eyes="side")
            ch_y ". . . знаешь, когда я остаюсь наедине со своими мыслями. . ."
            ch_y ". . . наедине со своим телом. . ."
            $ YanaX.FaceChange("sexy",2)
            ch_y "-я думаю о тебе. . ."
            $ YanaX.Blush = 1

    elif Options[0] == "anal":
            #Yana's response after getting anal from the Player.
            $ YanaX.FaceChange("sly")
            ch_y "Я раньше не занималась анальным сексом. . ."
            $ YanaX.FaceChange("sexy",1)
            ch_y ". . . я нахожу его -очень- приятным."

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ YanaX.FaceChange("sly",1, Eyes="down")
            ch_y "[YanaX.Petname]. . ."
            if not Player.Male:
                ch_y "Я весь день не могу выбросить твою киску из головы. . ."
                ch_y "Нам нужно как-то это исправить. . ."
            else:
                ch_y "Я весь день не могу выбросить твой член из головы. . ."
                ch_y "Нам нужно как-то это исправить. . ."
            $ YanaX.FaceChange("bemused",1)
            $ YanaX.Statup("Love", 50, 5)
            $ YanaX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            if not Player.Male:
                ch_y "Интересно, когда ты увидела мою грудь впервые. . ."
                ch_y "Что ты о них подумала?"
            else:
                ch_y "Интересно, когда ты увидел мою грудь впервые. . ."
                ch_y "Что ты о них подумал?"
            call Girl_First_TMenu
            $ YanaX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            if not Player.Male:
                ch_y "Интересно, когда ты увидела мою киску впервые. . ."
                ch_y "Что ты о ней подумала?"
            else:
                ch_y "Интересно, когда ты увидел мою киску впервые. . ."
                ch_y "Что ты о ней подумал?"
            call Girl_First_BMenu
            $ YanaX.History.remove("bottomless")

#    elif Options[0] == "boyfriend?":
#        call Yana_BF
#    elif Options[0] == "lover?":
#        call Yana_Love
#    elif Options[0] == "sir?":
#        call Yana_Sub
#    elif Options[0] == "master?":
#        call Yana_Master
#    elif Options[0] == "sexfriend?":
#        call Yana_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Yana_Fuckbuddy
#    elif Options[0] == "daddy?":
#        call Yana_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Отойди от меня.",
                "Я не желаю тебя видеть.",
                "Просто уйди.",
                "Уйди.",
                "Прочь!"])
        ch_y "[Line]"

    else: #all else fell through. . .
            if YanaX not in ActiveGirls:
                    $ D20 = 21
            else:
                    $ D20 = renpy.random.randint(1, 21)
            if D20 == 1:
                    $ YanaX.FaceChange("smile")
                    ch_y "Я тихонько втягиваюсь в учебный процесс."
            elif D20 == 2:
                    $ YanaX.FaceChange("sly")
                    ch_y "Преподаватели помогают мне адаптироваться."
            elif D20 == 3:
                    $ YanaX.FaceChange("surprised")
                    ch_y "Ах, извини, я задумалась."
            elif D20 == 4:
                    $ YanaX.FaceChange("normal")
                    ch_y "[YanaX.Petname], ты часто сталкиваешься с волшебными существами?"
            elif D20 == 5:
                    $ YanaX.FaceChange("smile")
                    ch_y "Мне очень нравится здешняя еда, жаль только, что здесь не подают торты."
            elif D20 == 6:
                    $ YanaX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_y "[YanaX.Petname], ты не видела [JubesX.Name_vin]? Мы собирались по магазинам."
                    else:
                        ch_y "[YanaX.Petname], ты не видел [JubesX.Name_vin]? Мы собирались по магазинам."
            elif D20 == 7:
                    $ YanaX.FaceChange("normal")
                    ch_y "Недавно в Комнате Опасности я отрабатывала техники избегания атак противника с помощью порталов."
            elif D20 == 8:
                    $ YanaX.FaceChange("sad")
                    ch_y "Я начинаю снова привыкать к жизни на Земле. . ."
            elif D20 == 9:
                    $ YanaX.FaceChange("smile",2)
                    ch_y "Знаешь, мне кажется, что на днях Курт пристально смотрел на меня."
                    $ YanaX.FaceChange("smile",1)
            elif D20 == 10:
                    $ YanaX.FaceChange("smile")
                    ch_y "Знаешь, очень удобно иметь возможность в мгновение ока попасть туда, куда мне заблагорассудится."
                    ch_y "Я могу лично забирать заказанную еду из любого города мира."
            elif D20 == 11:
                    $ YanaX.FaceChange("smile")
                    ch_y "[JeanX.Name] недавно пыталась доказать свое превосходство."
                    ch_y "-она не понимает, что нужно для того, чтобы пред ней пресмыкались."
            elif D20 == 12:
                    $ YanaX.FaceChange("sad")
                    ch_y "Мне тяжело даются тесты. Мне еще многое нужно наверстать. . ."
            elif D20 == 13:
                    $ YanaX.FaceChange("smile")
                    ch_y "Не так давно мы с [GwenX.Name_tvo] играли в бильярд, она рассказывает. . . интересные истории."
            elif D20 == 14:
                    $ YanaX.FaceChange("sad")
                    ch_y "Мне нравятся учиться, но расслабляться тоже важно."
            elif D20 == 15:
                    $ YanaX.FaceChange("perplexed")
                    if not Player.Male:
                        ch_y "Ты видела тот фильм об охотниках на демонов?"
                    else:
                        ch_y "Ты видел тот фильм об охотниках на демонов?"
                    ch_y "Он очень нереалистичный!"
                    ch_y "Демонов так просто не найти."
            elif D20 == 16:
                    $ YanaX.FaceChange("sly")
                    ch_y "Ты не поверишь, какое выражение было на лице [JeanX.Name_rod], когда я проткнула ее своим мечом."
                    $ YanaX.FaceChange("perplexed",1)
                    ch_y "О, не волнуйся, людям от этого не больно."
                    $ YanaX.FaceChange("sly",0)
                    ch_y "Он просто прошел прямо сквозь нее, не причинив вреда."
            elif D20 == 17:
                    $ YanaX.FaceChange("sly",Eyes="side")
                    ch_y "На днях я случайно забросила Меган в Лимбо."
                    $ YanaX.FaceChange("perplexed",2)
                    ch_y "О, не волнуйся, с ней все в порядке."
                    $ YanaX.FaceChange("sly",1,Eyes="side")
                    ch_y "-в итоге."
                    $ YanaX.FaceChange("normal")
            elif D20 == 18:
                    $ YanaX.FaceChange("smile")
                    if not Player.Male:
                        ch_y "Ты заметила, что даже преподаватели пристально смотрят на тебя?"
                    else:
                        ch_y "Ты заметил, что даже преподаватели пристально смотрят на тебя?"
            elif D20 == 19:
                    $ YanaX.FaceChange("smile")
                    ch_y "Не волнуйся, рога только для виду."
                    $ YanaX.FaceChange("bemused",1)
                    ch_y "-в основном."
                    $ YanaX.FaceChange("sly,1")
            elif D20 == 20:
                    $ YanaX.FaceChange("smile")
                    ch_y "Так приятно иметь возможность снова. . . снова поговорить с людьми, понимаешь?"
            else:
                    $ YanaX.FaceChange("smile")
                    ch_y "Ох, мне нравится разговаривать с тобой. . ."

    $ Line = 0
    return

# start Yana_Names//////////////////////////////////////////////////////////
label Yana_Names:    #rkeljsvgbdw
    menu:
        ch_y "Как ты хочешь, чтобы я звала тебя?"
        "Зови меня по инициалу." if Player.Name in YanaX.Petnames:
            $ YanaX.Petname = Player.Name[:1]  #fix test this
            $ YanaX.Petname_rod = Player.Name[:1]
            $ YanaX.Petname_dat = Player.Name[:1]
            $ YanaX.Petname_vin = Player.Name[:1]
            $ YanaX.Petname_tvo = Player.Name[:1]
            $ YanaX.Petname_pre = Player.Name[:1]
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня по имени.":
            $ YanaX.Petname = Player.Name
            $ YanaX.Petname_rod = Player.Name_rod
            $ YanaX.Petname_dat = Player.Name_dat
            $ YanaX.Petname_vin = Player.Name_vin
            $ YanaX.Petname_tvo = Player.Name_tvo
            $ YanaX.Petname_pre = Player.Name_pre
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня своей \"девушкой\"." if "boyfriend" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "моя девушка"
            $ YanaX.Petname_rod = "моей девушки"
            $ YanaX.Petname_dat = "моей девушке"
            $ YanaX.Petname_vin = "мою девушку"
            $ YanaX.Petname_tvo = "моей девушкой"
            $ YanaX.Petname_pre = "моей девушке"
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня своим \"парнем\"." if "boyfriend" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "мой парень"
            $ YanaX.Petname_rod = "моего парня"
            $ YanaX.Petname_dat = "моему парню"
            $ YanaX.Petname_vin = "моего парня"
            $ YanaX.Petname_tvo = "моим парнем"
            $ YanaX.Petname_pre = "моем парне"
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня \"любимая\"." if "lover" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "любимая"
            $ YanaX.Petname_rod = "любимой"
            $ YanaX.Petname_dat = "любимой"
            $ YanaX.Petname_vin = "любимую"
            $ YanaX.Petname_tvo = "любимой"
            $ YanaX.Petname_pre = "любимой"
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня \"любимый\"." if "lover" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "любимый"
            $ YanaX.Petname_rod = "любимого"
            $ YanaX.Petname_dat = "любимому"
            $ YanaX.Petname_vin = "любимого"
            $ YanaX.Petname_tvo = "любимым"
            $ YanaX.Petname_pre = "любимом"
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня \"госпожа\"." if "sir" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "госпожа"
            $ YanaX.Petname_rod = "госпожи"
            $ YanaX.Petname_dat = "госпоже"
            $ YanaX.Petname_vin = "госпожу"
            $ YanaX.Petname_tvo = "госпожой"
            $ YanaX.Petname_pre = "госпоже"
            ch_y "Конечно, [YanaX.Petname]."
        "Зови меня \"господин\"." if "sir" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "господин"
            $ YanaX.Petname_rod = "господина"
            $ YanaX.Petname_dat = "господину"
            $ YanaX.Petname_vin = "господина"
            $ YanaX.Petname_tvo = "господином"
            $ YanaX.Petname_pre = "господине"
            ch_y "Конечно, [YanaX.Petname]."
        "Зови меня \"хозяйка\"." if "master" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "хозяйка"
            $ YanaX.Petname_rod = "хозяйки"
            $ YanaX.Petname_dat = "хозяйке"
            $ YanaX.Petname_vin = "хозяйку"
            $ YanaX.Petname_tvo = "хозяйкой"
            $ YanaX.Petname_pre = "хозяйке"
            ch_y "Да, [YanaX.Petname]."
        "Зови меня \"хозяин\"." if "master" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "хозяин"
            $ YanaX.Petname = "хозяин"
            $ YanaX.Petname_rod = "хозяина"
            $ YanaX.Petname_dat = "хозяину"
            $ YanaX.Petname_vin = "хозяина"
            $ YanaX.Petname_tvo = "хозяином"
            $ YanaX.Petname_pre = "хозяине"
            ch_y "Да, [YanaX.Petname]."
        "Зови меня \"любовница\"." if "sex friend" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "любовница"
            $ YanaX.Petname_rod = "любовницы"
            $ YanaX.Petname_dat = "любовнице"
            $ YanaX.Petname_vin = "любовницу"
            $ YanaX.Petname_tvo = "любовницей"
            $ YanaX.Petname_pre = "любовнице"
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня \"любовник\"." if "sex friend" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "любовник"
            $ YanaX.Petname_rod = "любовника"
            $ YanaX.Petname_dat = "любовнику"
            $ YanaX.Petname_vin = "любовника"
            $ YanaX.Petname_tvo = "любовником"
            $ YanaX.Petname_pre = "любовнике"
            ch_y "Хорошо, [YanaX.Petname]."
        "Зови меня \"секс-партнерша\"." if "fuck buddy" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "секс-партнерша"
            $ YanaX.Petname_rod = "секс-партнерши"
            $ YanaX.Petname_dat = "секс-партнерше"
            $ YanaX.Petname_vin = "секс-партнершу"
            $ YanaX.Petname_tvo = "секс-партнершей"
            $ YanaX.Petname_pre = "секс-партнерше"
            ch_y "[YanaX.Petname]. . . хех, впечатляет. . . "
        "Зови меня \"секс-партнер\"." if "fuck buddy" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "секс-партнер"
            $ YanaX.Petname_rod = "секс-партнера"
            $ YanaX.Petname_dat = "секс-партнеру"
            $ YanaX.Petname_vin = "секс-партнера"
            $ YanaX.Petname_tvo = "секс-партнером"
            $ YanaX.Petname_pre = "секс-партнере"
            ch_y "[YanaX.Petname]. . . хех, впечатляет. . . "
        "Зови меня \"мамочка\"." if "daddy" in YanaX.Petnames and not Player.Male:
            $ YanaX.Petname = "мамочка"
            $ YanaX.Petname_rod = "мамочки"
            $ YanaX.Petname_dat = "мамочке"
            $ YanaX.Petname_vin = "мамочку"
            $ YanaX.Petname_tvo = "мамочкой"
            $ YanaX.Petname_pre = "мамочке"
            ch_y "Конечно, [YanaX.Petname]."
        "Зови меня \"папочка\"." if "daddy" in YanaX.Petnames and Player.Male:
            $ YanaX.Petname = "папочка"
            $ YanaX.Petname_rod = "папочки"
            $ YanaX.Petname_dat = "папочке"
            $ YanaX.Petname_vin = "папочку"
            $ YanaX.Petname_tvo = "папочкой"
            $ YanaX.Petname_pre = "папочке"
            ch_y "Конечно, [YanaX.Petname]."
        "Зови меня \"сис\"." if not Player.Male:
            $ YanaX.Petname = "сис"
            $ YanaX.Petname_rod = "сис"
            $ YanaX.Petname_dat = "сис"
            $ YanaX.Petname_vin = "сис"
            $ YanaX.Petname_tvo = "сис"
            $ YanaX.Petname_pre = "сис"
            ch_y "Не бро? Как скажешь, сис."
        "Зови меня \"бро\"." if Player.Male:
            $ YanaX.Petname = "бро"
            $ YanaX.Petname_rod = "бро"
            $ YanaX.Petname_dat = "бро"
            $ YanaX.Petname_vin = "бро"
            $ YanaX.Petname_tvo = "бро"
            $ YanaX.Petname_pre = "бро"
            ch_y "Ладно, бро."
        "Неважно.":
            return
    return
# end Yana_Names//////////////////////////////////////////////////////////

label Yana_Pet: #rkeljsvgbdw
    while 1:
        menu:
            extend ""
            "Обходительно":
                menu:
                    "Думаю, буду просто звать тебя. . ."
                    "Ульяна.":
                        $ YanaX.Pet = "Ульяна"
                        $ YanaX.Pet_rod = "Ульяны"
                        $ YanaX.Pet_dat = "Ульяне"
                        $ YanaX.Pet_vin = "Ульяну"
                        $ YanaX.Pet_tvo = "Ульяной"
                        $ YanaX.Pet_pre = "Ульяне"
                        ch_y "Ладно."

                    "Яна.":
                        $ YanaX.Pet = "Яна"
                        $ YanaX.Pet_rod = "Яны"
                        $ YanaX.Pet_dat = "Яне"
                        $ YanaX.Pet_vin = "Яну"
                        $ YanaX.Pet_tvo = "Яной"
                        $ YanaX.Pet_pre = "Яне"
                        ch_y "Ладно."

                    "Снежинка." if "Snowflake" in YanaX.Pets:
                        $ YanaX.Pet = "Снежинка"
                        $ YanaX.Pet_rod = "Снежинки"
                        $ YanaX.Pet_dat = "Снежинке"
                        $ YanaX.Pet_vin = "Снежинку"
                        $ YanaX.Pet_tvo = "Снежинкой"
                        $ YanaX.Pet_pre = "Снежинке"
                        if ApprovalCheck(YanaX, 700, "L") and not ApprovalCheck(YanaX, 500, "O"):
                                ch_y "Эх, ностальгия, [YanaX.Petname]."
                        else:
                                ch_y "Ладно, я не возражаю."

                    "\"моя девушка\".":
                        if "boyfriend" in YanaX.Petnames or ApprovalCheck(YanaX, 600, "L"):
                            $ YanaX.FaceChange("sexy", 1)
                            ch_y "Да, я же твоя девушка, [YanaX.Petname]."
                            $ YanaX.Pet = "моя девушка"
                            $ YanaX.Pet_rod = "моей девушки"
                            $ YanaX.Pet_dat = "моей девушке"
                            $ YanaX.Pet_vin = "мою девушку"
                            $ YanaX.Pet_tvo = "моей девушкой"
                            $ YanaX.Pet_pre = "моей девушке"
                        else:
                            $ YanaX.FaceChange("angry")
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"детка\".":
                        if "boyfriend" in YanaX.Petnames or ApprovalCheck(YanaX, 700, "L"):
                            $ YanaX.Pet = "детка"
                            $ YanaX.Pet_rod = "детки"
                            $ YanaX.Pet_dat = "детке"
                            $ YanaX.Pet_vin = "детку"
                            $ YanaX.Pet_tvo = "деткой"
                            $ YanaX.Pet_pre = "детке"
                            $ YanaX.FaceChange("sexy", 1)
                            ch_y "Твоя \"детка,\" забавно!"
                        else:
                            $ YanaX.FaceChange("angry")
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"крошка\".":
                        if "boyfriend" in YanaX.Petnames or ApprovalCheck(YanaX, 600, "L"):
                            $ YanaX.Pet = "крошка"
                            $ YanaX.Pet_rod = "крошки"
                            $ YanaX.Pet_dat = "крошке"
                            $ YanaX.Pet_vin = "крошку"
                            $ YanaX.Pet_tvo = "крошкой"
                            $ YanaX.Pet_pre = "крошке"
                            $ YanaX.FaceChange("sexy", 1)
                            ch_y "Твоя \"крошка,\" хех!"
                        else:
                            $ YanaX.FaceChange("angry")
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"малышка\".":
                        if "boyfriend" in YanaX.Petnames or ApprovalCheck(YanaX, 500, "L"):
                            $ YanaX.Pet = "малышка"
                            $ YanaX.Pet_rod = "малышки"
                            $ YanaX.Pet_dat = "малышке"
                            $ YanaX.Pet_vin = "малышку"
                            $ YanaX.Pet_tvo = "малышкой"
                            $ YanaX.Pet_pre = "малышке"
                            $ YanaX.FaceChange("sexy", 1)
                            ch_y "Восхитительно, [YanaX.Petname]."
                        else:
                            $ YanaX.FaceChange("angry")
                            ch_y "Это будет странно, [YanaX.Petname]."


                    "\"милая\".":
                        if "boyfriend" in YanaX.Petnames or ApprovalCheck(YanaX, 600, "L"):
                            $ YanaX.Pet = "милая"
                            $ YanaX.Pet_rod = "милой"
                            $ YanaX.Pet_dat = "милой"
                            $ YanaX.Pet_vin = "милую"
                            $ YanaX.Pet_tvo = "милой"
                            $ YanaX.Pet_pre = "милой"
                            ch_y "Звучит \"мило\", [YanaX.Petname]."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"секси\".":
                        if "lover" in YanaX.Petnames or ApprovalCheck(YanaX, 800):
                            $ YanaX.Pet = "секси"
                            $ YanaX.Pet_rod = "секси"
                            $ YanaX.Pet_dat = "секси"
                            $ YanaX.Pet_vin = "секси"
                            $ YanaX.Pet_tvo = "секси"
                            $ YanaX.Pet_pre = "секси"
                            $ YanaX.FaceChange("sexy", 1)
                            ch_y "Хех. . ."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"любимая\".":
                        if "lover" in YanaX.Petnames or ApprovalCheck(YanaX, 1200):
                            $ YanaX.Pet = "любимая"
                            $ YanaX.Pet_rod = "любимой"
                            $ YanaX.Pet_dat = "любимой"
                            $ YanaX.Pet_vin = "любимую"
                            $ YanaX.Pet_tvo = "любимой"
                            $ YanaX.Pet_pre = "любимой"
                            $ YanaX.FaceChange("sexy", 1)
                            ch_y "Конечно."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Я так не думаю, [YanaX.Petname]."

                    "Назад":
                        pass

            "Рискованно":
                menu:
                    "Думаю, буду звать тебя. . ."
                    "\"рабыня\".":
                        if "master" in YanaX.Petnames or ApprovalCheck(YanaX, 800, "O"):
                            $ YanaX.Pet = "рабыня"
                            $ YanaX.Pet_rod = "рабыни"
                            $ YanaX.Pet_dat = "рабыне"
                            $ YanaX.Pet_vin = "рабыню"
                            $ YanaX.Pet_tvo = "рабыней"
                            $ YanaX.Pet_pre = "рабыне"
                            $ YanaX.FaceChange("bemused", 1)
                            ch_y "Да, [YanaX.Petname]."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Я не твоя рабыня, [YanaX.Petname]."

                    "\"питомец\".":
                        if "master" in YanaX.Petnames or ApprovalCheck(YanaX, 650, "O"):
                            $ YanaX.Pet = "питомец"
                            $ YanaX.Pet_rod = "питомце"
                            $ YanaX.Pet_dat = "питомцу"
                            $ YanaX.Pet_vin = "питомца"
                            $ YanaX.Pet_tvo = "питомцем"
                            $ YanaX.Pet_pre = "питомце"
                            $ YanaX.FaceChange("bemused", 1)
                            ch_y "Я не возражаю, [YanaX.Petname]."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Я не твой питомец, [YanaX.Petname]."

                    "\"шлюха\".":
                        if "sex friend" in YanaX.Petnames or ApprovalCheck(YanaX, 900, "OI"):
                            $ YanaX.Pet = "шлюха"
                            $ YanaX.Pet_rod = "шлюхи"
                            $ YanaX.Pet_dat = "шлюхе"
                            $ YanaX.Pet_vin = "шлюху"
                            $ YanaX.Pet_tvo = "шлюхой"
                            $ YanaX.Pet_pre = "шлюхе"
                            $ YanaX.FaceChange("sexy")
                            ch_y "Это. . . не так далеко от правды. . ."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            $ YanaX.Mouth = "surprised"
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"блядь\".":
                        if "fuckbuddy" in YanaX.Petnames or ApprovalCheck(YanaX, 1000, "OI"):
                            $ YanaX.Pet = "блядь"
                            $ YanaX.Pet_rod = "бляди"
                            $ YanaX.Pet_dat = "бляде"
                            $ YanaX.Pet_vin = "блядь"
                            $ YanaX.Pet_tvo = "блядью"
                            $ YanaX.Pet_pre = "бляде"
                            $ YanaX.FaceChange("sly")
                            ch_y ". . . это довольно грубо, но ладно. . ."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Это будет -очень- странно, [YanaX.Petname]."

                    "\"сладкогрудая\".":
                        if "sex friend" in YanaX.Petnames or ApprovalCheck(YanaX, 1400):
                            $ YanaX.Pet = "сладкогрудая"
                            $ YanaX.Pet_rod = "сладкогрудой"
                            $ YanaX.Pet_dat = "сладкогрудой"
                            $ YanaX.Pet_vin = "сладкогрудую"
                            $ YanaX.Pet_tvo = "сладкогрудой"
                            $ YanaX.Pet_pre = "сладкогрудой"
                            $ YanaX.FaceChange("sly", 1)
                            ch_y "Хм? Ладно. . ."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"любовница\".":
                        if "sex friend" in YanaX.Petnames or ApprovalCheck(YanaX, 600, "I"):
                            $ YanaX.Pet = "любовница"
                            $ YanaX.Pet_rod = "любовницы"
                            $ YanaX.Pet_dat = "любовнице"
                            $ YanaX.Pet_vin = "любовницу"
                            $ YanaX.Pet_tvo = "любовницей"
                            $ YanaX.Pet_pre = "любовнице"
                            $ YanaX.FaceChange("sly")
                            ch_y "Хорошо."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"секс-партнерша\".":
                        if "fuckbuddy" in YanaX.Petnames or ApprovalCheck(YanaX, 700, "I"):
                            $ YanaX.Pet = "секс-партнерша"
                            $ YanaX.Pet_rod = "секс-партнерши"
                            $ YanaX.Pet_dat = "секс-партнерше"
                            $ YanaX.Pet_vin = "секс-партнершу"
                            $ YanaX.Pet_tvo = "секс-партнершей"
                            $ YanaX.Pet_pre = "секс-партнерше"
                            $ YanaX.FaceChange("sly")
                            ch_y "Хорошо."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            $ YanaX.Mouth = "surprised"
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "\"доченька\".":
                        if "daddy" in YanaX.Petnames or ApprovalCheck(YanaX, 1200):
                            $ YanaX.Pet = "доченька"
                            $ YanaX.Pet_rod = "доченьки"
                            $ YanaX.Pet_dat = "доченьке"
                            $ YanaX.Pet_vin = "доченьку"
                            $ YanaX.Pet_tvo = "доченькой"
                            $ YanaX.Pet_pre = "доченьке"
                            $ YanaX.FaceChange("smile", 1)
                            ch_y "Звучит восхитительно."
                        else:
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Это будет странно, [YanaX.Petname]."

                    "Назад":
                        pass

            "Неважно.":
                return
    return

#label Yana_Namecheck(YanaX.Pet = YanaX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname


# start Yana_Rename//////////////////////////////////////////////////////////
label Yana_Rename:  #rkeljsvgbdw
        #Sets alternate names from Yana
        $ YanaX.Mouth = "smile"
        ch_y "Да?"
        menu:
            extend ""
            "Думаю, \"Ульяна\" красивое имя." if YanaX.Name != "Ульяна":
                            $ YanaX.Name = "Ульяна"
                            $ YanaX.Name_rod = "Ульяны"
                            $ YanaX.Name_dat = "Ульяне"
                            $ YanaX.Name_vin = "Ульяну"
                            $ YanaX.Name_tvo = "Ульяной"
                            $ YanaX.Name_pre = "Ульяне"
                            ch_y "Спасибо."
            "Думаю, \"Яна\" красивое имя." if YanaX.Name != "Яна":
                            $ YanaX.Name = "Яна"
                            $ YanaX.Name_rod = "Яны"
                            $ YanaX.Name_dat = "Яне"
                            $ YanaX.Name_vin = "Яну"
                            $ YanaX.Name_tvo = "Яной"
                            $ YanaX.Name_pre = "Яне"
                            ch_y "Конечно."
            "Думаю, \"Мэджик\" красивое имя." if YanaX.Name != "Мэджик":# and "Magik" in YanaX.Names:
                    if not ApprovalCheck(YanaX, 500):
                            $ YanaX.FaceChange("confused", 1)
                            ch_y "Мне больше нравится, когда меня зовут \"[YanaX.Name_tvo]\"."
                    else:
                            if "namechange" not in YanaX.DailyActions:
                                    $ YanaX.Statup("Love", 70, 2)
                                    $ YanaX.Statup("Obed", 70, 5)
                            $ YanaX.Name = "Мэджик"
                            $ YanaX.Name_rod = "Мэджик"
                            $ YanaX.Name_dat = "Мэджик"
                            $ YanaX.Name_vin = "Мэджик"
                            $ YanaX.Name_tvo = "Мэджик"
                            $ YanaX.Name_pre = "Мэджик"
                            $ YanaX.FaceChange("sly", 1)
                            ch_y "Раз ты этого хочешь. . ."
            "Неважно.":
                    pass
        $ YanaX.AddWord(1,0,"namechange")
        return
# end Yana_Rename//////////////////////////////////////////////////////////


# start Yana_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Yana_Personality(Cnt = 0):   #rkeljsvgbdw
    if not YanaX.Chat[4] or Cnt:
        "Поскольку у вас все хорошо получается в одной области, вы можете убедить [YanaX.Name_vin] сосредоточиться на любой другой."
        "Каждый раз, когда вы превышаете лимит одной характеристики, избыток будет перетекать в выбранную характеристику."
        "Это также повлияет на то, какие черты личности будут преобладать в диалоге."
    menu:
        ch_y "Да?"
        "Больше Послушания. [[Любовь в Послушание]" if YanaX.Love > 900:
            ch_p "Если ты действительно любишь меня, пожалуйста, можешь просто делать то, что я говорю?"
            ch_y "Желаешь, чтобы я стала более покорной? Я попробую."
            $ YanaX.Chat[4] = 1
        "Больше Раскрепощенность. [[Любовь в Раскрепощенность]" if YanaX.Love > 900:
            ch_p "Если ты действительно любишь меня, можешь быть немного более расслабленной, просто веселиться?"
            ch_y "Желаешь, чтобы я стала более раскрепощенной? Я попробую."
            $ YanaX.Chat[4] = 2

        "Больше Раскрепощенность. [[Повиновение в Раскрепощенность]" if YanaX.Obed > 900:
            ch_p "Я хочу, чтобы ты была более раскрепощенной."
            ch_y "Желаешь, чтобы я стала более раскрепощенной? Я попробую."
            $ YanaX.Chat[4] = 3
        "Больше Любви. [[Повиновение в Любовь]" if YanaX.Obed > 900:
            ch_p "Я хочу, чтобы ты училась любить меня."
            ch_y "Я недостаточно тебя люблю? Попробую это исправить."
            $ YanaX.Chat[4] = 4

        "Больше Послушания. [[Раскрепощенность в Повиновение]" if YanaX.Inbt > 900:
            ch_p "Я знаю, что нам и так весело, но разве ты не можешь иногда слушаться меня?"
            ch_y "Желаешь, чтобы я стала более покорной? Я попробую."
            $ YanaX.Chat[4] = 5

        "Больше Любви. [[Раскрепощенность в Любовь]" if YanaX.Inbt > 900:
            ch_p "Я знаю, что мы веселимся, но ты можешь хоть иногда заботиться обо мне?"
            ch_y "Я недостаточно тебя люблю? Попробую это исправить."
            $ YanaX.Chat[4] = 6

        "Просто делай то, что тебе нравится. . .[[Сбросить]" if YanaX.Chat[4]:
            ch_p "Помнишь, что мы обсуждали? Забудь."
            ch_y "Хм. . . ладно?"
            $ YanaX.Chat[4] = 0
        "Повторить правила":
            call Yana_Personality(1)
            return
        "Неважно.":
            return
    return
# end Yana_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Yana_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Yana_Summon(Tempmod=Tempmod): #rkeljsvgbdw
    $ YanaX.OutfitChange()
    if "no summon" in YanaX.RecentActions:
                if "no summon" in YanaX.RecentActions:
                    ch_y "Перестань спрашивать!"
                    $ YanaX.AddWord(1,"angry",0,0,0)
                elif Current_Time == "Night":
                    ch_y "Я же сказала тебе, что уже слишком поздно."
                else:
                    ch_y "Я же сказала тебе, что я занята."
                $ YanaX.RecentActions.append("no summon")
                return

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    if YanaX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif YanaX.Loc == "bg dangerroom":
        $ Tempmod = -10
    elif YanaX.Loc == "bg showerroom":
        $ Tempmod = -30

    if D20 <= 3:
        #unlucky refusal
        $ Line = "no"
    if Time_Count >= 3: #night time
                if ApprovalCheck(YanaX, 500, "L") or ApprovalCheck(YanaX, 400, "O"):
                        #It's night time but she likes you.
                        ch_y "Конечно, я могу заглянуть."
                        $ YanaX.Loc = bg_current
                        call Taboo_Level
                        call Set_The_Scene
                else:
                        #It's night time and she isn't into you
                        ch_y "Уже слишком поздно, извини."
                        $ YanaX.RecentActions.append("no summon")
                return
    elif "les" in YanaX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(YanaX, 2000):
                    ch_y "У меня уже есть компания, но ты можешь присоединиться к нам. . ."
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "go to"
                        "Нет, спасибо.":
                            ch_y "Теперь наших насмешек тебе не избежать. . ."
                            return
            else:
                    ch_y "Давай позже."
                    ch_y "Я. . . не одна. . ."
                    $ YanaX.RecentActions.append("no summon")
                    return
    elif not ApprovalCheck(YanaX, 700, "L") or not ApprovalCheck(YanaX, 600, "O"):
        #It's not night time, but she's busy
        if not ApprovalCheck(YanaX, 300):
                ch_y "Я занята, [YanaX.Petname], извини."
                $ YanaX.RecentActions.append("no summon")
                return


        if "summoned" in YanaX.RecentActions:
                pass
        elif "goto" in YanaX.RecentActions:
                if not Player.Male:
                    ch_y "Ты только что ушла. . ."
                else:
                    ch_y "Ты только что ушел. . ."
        elif YanaX.Loc == "bg classroom":
                ch_y "Я в аудитории, желаешь тоже прийти?"
        elif YanaX.Loc == "bg dangerroom":
                ch_y "Я в Комнате Опасности, [YanaX.Petname], желаешь присоединиться ко мне?"
        elif YanaX.Loc == "bg campus":
                ch_y "Я отдыхаю во дворе, желаешь присоединиться ко мне?"
        elif YanaX.Loc == "bg yana":
                ch_y "Я в своей комнате, [YanaX.Petname], желаешь присоединиться ко мне?"
        elif YanaX.Loc == "bg player":
                ch_y "Я в твоей комнате, [YanaX.Petname], желаешь присоединиться ко мне?"
        elif YanaX.Loc == "bg showerroom":
            if ApprovalCheck(YanaX, 1600):
                ch_y "Я сейчас в душе. Желаешь присоединиться ко мне?"
            else:
                ch_y "Я сейчас в душе, [YanaX.Petname], увидимся позже."
                $ YanaX.RecentActions.append("no summon")
                return
        elif YanaX.Loc == "hold":
                ch_y "Я сейчас занята, извини."
                $ YanaX.RecentActions.append("no summon")
                return
        else:
                if not Player.Male:
                    ch_y "Ты могла бы подойти сюда. . ."
                else:
                    ch_y "Ты мог бы подойти сюда. . ."


        if "summoned" in YanaX.RecentActions:
            ch_y "Снова? Что ж, хорошо. . ."
            $ Line = "yes"
        elif "goto" in YanaX.RecentActions:
            menu:
                extend ""
                "Ты права, сейчас вернусь.":
#                                ch_y "See you then."
                                $ Line = "go to"
                "Нет.":
                                ch_y "Как пожелаешь."
                "Мне бы -очень- хотелось, чтобы ты пришла ко мне.":
                        if ApprovalCheck(YanaX, 600, "L") or ApprovalCheck(YanaX, 1400):
                                $ Line = "lonely"
                        else:
                                $ Line = "no"
                "Я сказала, давай ко мне." if not Player.Male:
                        if ApprovalCheck(YanaX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(YanaX, 1400):
                                #she is generally favorable
                                ch_y "Ладно."
                                $ Line = "yes"
                        elif ApprovalCheck(YanaX, 200, "O"):
                                #she is not obedient
                                ch_y "Ах."
                                ch_y "Если что, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
                "Я сказал, давай ко мне." if Player.Male:
                        if ApprovalCheck(YanaX, 600, "O"):
                                #she is obedient
                                $ Line = "command"
                        elif D20 >= 7 and ApprovalCheck(YanaX, 1400):
                                #she is generally favorable
                                ch_y "Ладно."
                                $ Line = "yes"
                        elif ApprovalCheck(YanaX, 200, "O"):
                                #she is not obedient
                                ch_y "Ах."
                                ch_y "Если что, ты знаешь, где меня найти."
                        else:
                                #she is obedient, but you failed to meet the checks
                                $ Line = "no"
        else:
            menu:
                extend ""
                "Конечно, сейчас приду.":
                    $ YanaX.Statup("Love", 55, 1)
                    $ YanaX.Statup("Inbt", 30, 1)
#                    ch_y "See you then."
                    $ Line = "go to"

                "Нет, поговорим позже.":
                    $ YanaX.Statup("Obed", 50, 1)
                    $ YanaX.Statup("Obed", 30, 2)
                    ch_y "Ах, что ж, хорошо."

                "Не могла бы ты навестить меня? Мне так одиноко.":
                    if ApprovalCheck(YanaX, 650, "L") or ApprovalCheck(YanaX, 1500):
                        $ YanaX.Statup("Love", 70, 1)
                        $ YanaX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else:
                        $ YanaX.Statup("Inbt", 30, 1)
                        $ Line = "no"
#                        ch_y "Wow, ok."

                "Приходи ко мне, будет весело.":
                    if ApprovalCheck(YanaX, 400, "L") and ApprovalCheck(YanaX, 800):
                        $ YanaX.Statup("Love", 70, 1)
                        $ YanaX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else:
                        $ YanaX.Statup("Inbt", 30, 1)
                        $ Line = "no"

                "Я сказала, давай ко мне." if not Player.Male:
                    if ApprovalCheck(YanaX, 600, "O"):
                        #she is obedient
                        $ YanaX.Statup("Love", 50, 1, 1)
                        $ YanaX.Statup("Love", 40, -1)
                        $ YanaX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(YanaX, 1500):
                        #she is generally favorable
                        $ YanaX.Statup("Love", 70, -2)
                        $ YanaX.Statup("Love", 90, -1)
                        $ YanaX.Statup("Obed", 50, 2)
                        $ YanaX.Statup("Obed", 90, 1)
                        ch_y "Ах, что ж, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(YanaX, 200, "O"):
                        #she is not obedient
                        $ YanaX.Statup("Love", 60, -4)
                        $ YanaX.Statup("Love", 90, -3)
                        ch_y ". . ."
                        $ YanaX.Statup("Inbt", 40, 2)
                        $ YanaX.Statup("Inbt", 60, 1)
                        $ YanaX.Statup("Obed", 70, -3)
                        ch_y "Не стоит ждать, что это сработает."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ YanaX.Statup("Inbt", 30, 1)
                        $ YanaX.Statup("Inbt", 50, 1)
                        $ YanaX.Statup("Love", 50, -1, 1)
                        $ YanaX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
                "Я сказал, давай ко мне." if Player.Male:
                    if ApprovalCheck(YanaX, 600, "O"):
                        #she is obedient
                        $ YanaX.Statup("Love", 50, 1, 1)
                        $ YanaX.Statup("Love", 40, -1)
                        $ YanaX.Statup("Obed", 90, 1)
                        $ Line = "command"

                    elif D20 >= 7 and ApprovalCheck(YanaX, 1500):
                        #she is generally favorable
                        $ YanaX.Statup("Love", 70, -2)
                        $ YanaX.Statup("Love", 90, -1)
                        $ YanaX.Statup("Obed", 50, 2)
                        $ YanaX.Statup("Obed", 90, 1)
                        ch_y "Ах, что ж, хорошо."
                        $ Line = "yes"

                    elif ApprovalCheck(YanaX, 200, "O"):
                        #she is not obedient
                        $ YanaX.Statup("Love", 60, -4)
                        $ YanaX.Statup("Love", 90, -3)
                        ch_y ". . ."
                        $ YanaX.Statup("Inbt", 40, 2)
                        $ YanaX.Statup("Inbt", 60, 1)
                        $ YanaX.Statup("Obed", 70, -3)
                        ch_y "Не стоит ждать, что это сработает."
                    else:
                        #she is obedient, but you failed to meet the checks
                        $ YanaX.Statup("Inbt", 30, 1)
                        $ YanaX.Statup("Inbt", 50, 1)
                        $ YanaX.Statup("Love", 50, -1, 1)
                        $ YanaX.Statup("Obed", 70, -1)
                        $ Line = "no"
                    #end "ordered"
    else:
        #automatic acceptance
        if YanaX.Love > YanaX.Obed:
            ch_y "Конечно."
        else:
            ch_y "Конечно. . ."
        $ Line = "yes"

    $ Tempmod = 0

    if not Line:
            #You end the dialog neutrally
            $ YanaX.RecentActions.append("no summon")
            return

    if Line == "no":
            # She's refused, context based dialog
            if YanaX.Loc == "bg classroom":
                ch_y "Мне нужно учиться."
            elif YanaX.Loc == "bg dangerroom":
                ch_y "Я только разогрелась!"
            else:
                ch_y "[YanaX.Petname], я очень занята, извини."
            $ YanaX.RecentActions.append("no summon")
            return

    elif Line == "go to":
            #You agreed to go to her instead
            $ renpy.pop_call()
            $ YanaX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            $ Nearby = []
            $ Line = 0
            $ Party = [YanaX]

            if YanaX.Loc == "bg classroom":
                    ch_y "Ты знаешь, где меня искать."
                    jump Class_Room
            elif YanaX.Loc == "bg dangerroom":
                    ch_y "Я пока немного разогреюсь."
                    jump Danger_Room
            elif YanaX.Loc == "bg yana":
                    ch_y "Я пока подготовлюсь к гостям."
                    jump Yana_Room
            elif YanaX.Loc == "bg player":
                    ch_y "Увидимся, когда придешь."
                    jump Player_Room
            elif YanaX.Loc == "bg showerroom":
                    ch_y "Я пока начну."
                    jump Shower_Room
            elif YanaX.Loc == "bg campus":
                    ch_y "Тогда до встречи."
                    jump Campus
            elif YanaX.Loc != "hold":
                    ch_y "Конечно."
                    $ bg_current = YanaX.Loc
                    jump Misplaced
            else:
                    ch_y "Я просто встречу тебя в своей комнате."
                    $ YanaX.Loc = "bg yana"
                    jump Yana_Room

    #She's agreed to come over
    elif Line == "lonely":
            ch_y "Я бы этого не хотела. . ."
    elif Line == "command":
            ch_y "Что ж, хорошо, [YanaX.Petname]."
    elif Line == "fun":
            ch_y "Конечно."

    $ YanaX.RecentActions.append("summoned")
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(YanaX)
            return
    $ YanaX.Loc = bg_current
    call Taboo_Level(0)
    $ YanaX.OutfitChange()
    call Set_The_Scene
    return

# End Yana Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Yana_Leave(Tempmod=Tempmod, GirlsNum = 0):    #rkeljsvgbdw
    if "leaving" in YanaX.RecentActions:
        $ YanaX.DrainWord("leaving")
    else:
        return

    if YanaX.Loc == "hold":
            # Activates if she's being moved out of play
            ch_y "Увидимся позже."
            return

    if YanaX in Party or "lockedtravels" in YanaX.Traits:
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ YanaX.Loc = bg_current
            return

    elif "freetravels" in YanaX.Traits or not ApprovalCheck(YanaX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.
            $ YanaX.OutfitChange()
            if GirlsNum: #if someone left before her
                        ch_y "Да, я тоже пошла."

            if YanaX.Loc == "bg classroom":
                        ch_y "У меня занятия."
            elif YanaX.Loc == "bg dangerroom":
                        ch_y "У меня тренировка в Комнате Опасности."
            elif YanaX.Loc == "bg campus":
                        ch_y "Я собираюсь отдохнуть во дворе."
            elif YanaX.Loc == "bg yana":
                        ch_y "Я возвращаюсь в свою комнату."
            elif YanaX.Loc == "bg player":
                        ch_y "Я ненадолго заскочу в твою комнату."
            elif YanaX.Loc == "bg pool":
                        ch_y "Я собираюсь поплавать."
            elif YanaX.Loc == "bg showerroom":
                if ApprovalCheck(YanaX, 1400):
                        ch_y "Я собираюсь принять душ."
                else:
                        ch_y "Да, пока."
            else:
                        ch_y "Да, пока."
            hide Yana_Sprite
            hide Yana_Seated
            return
            #End Free Travels

    if bg_current == "bg dangerroom":
            call Gym_Exit([YanaX])

    $ YanaX.OutfitChange()

    if "follow" not in YanaX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ YanaX.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ Line = 0
    # Sets her preferences
    if YanaX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif YanaX.Loc == "bg dangerroom":
        $ Tempmod = 20
    elif YanaX.Loc == "bg showerroom":
        $ Tempmod = 40


    if GirlsNum: #if someone left before her
            ch_y "Да, я тоже пойду."

    if YanaX.Loc == "bg classroom":
            ch_y "Я иду на занятия, хочешь со мной?"
    elif YanaX.Loc == "bg dangerroom":
            ch_y "Я иду в Комнату Опасности, [YanaX.Petname], желаешь присоединиться ко мне?"
    elif YanaX.Loc == "bg campus":
            ch_y "Я собираюсь погулять во дворе. Желаешь присоединиться ко мне?"
    elif YanaX.Loc == "bg yana":
            ch_y "Я направляюсь в свою комнату, [YanaX.Petname], желаешь присоединиться ко мне?"
    elif YanaX.Loc == "bg player":
            ch_y "Я направляюсь в твою комнату, [YanaX.Petname], желаешь присоединиться ко мне?"
    elif YanaX.Loc == "bg showerroom":
        if ApprovalCheck(YanaX, 1600):
            ch_y "Я собираюсь принять душ. Желаешь присоединиться ко мне?"
        else:
            ch_y "Я собираюсь принять душ, [YanaX.Petname], до встречи."
            return
    elif YanaX.Loc == "bg pool":
            ch_y "Я направляюсь к бассейну. Желаешь присоединиться ко мне?"
    elif YanaX.Loc == "bg mall":
            ch_y "Я направляюсь в торговый центр. Желаешь присоединиться ко мне?"
    else:
            ch_y "Желаешь присоединиться ко мне?"


    menu:
        extend ""
        "Конечно, я сразу за тобой.":
                if "followed" not in YanaX.RecentActions:
                    $ YanaX.Statup("Love", 55, 1)
                    $ YanaX.Statup("Inbt", 30, 1)
                $ Line = "go to"

        "Нет, поговорим позже.":
                if "followed" not in YanaX.RecentActions:
                    $ YanaX.Statup("Obed", 50, 1)
                    $ YanaX.Statup("Obed", 30, 2)
                ch_y "Ах, что ж, хорошо."

        "Ты можешь остаться со мной? Мне будет так одиноко без тебя.":
                if ApprovalCheck(YanaX, 650, "L") or ApprovalCheck(YanaX, 1500):
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Love", 70, 1)
                        $ YanaX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else:
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Inbt", 30, 1)
                    $ Line = "no"
#                    ch_y "Wow."

        "Останься, будет весело.":
                if ApprovalCheck(YanaX, 400, "L") and ApprovalCheck(YanaX, 800):
                    $ YanaX.Statup("Love", 70, 1)
                    $ YanaX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else:
                    $ YanaX.Statup("Inbt", 30, 1)
                    $ Line = "no"

        "Нет, останься здесь.":
                if ApprovalCheck(YanaX, 600, "O"):
                    #she is obedient
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Love", 40, -2)
                        $ YanaX.Statup("Obed", 90, 1)
                    $ Line = "command"

                elif D20 >= 7 and ApprovalCheck(YanaX, 1400):
                    #she is generally favorable
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Love", 70, -2)
                        $ YanaX.Statup("Love", 90, -1)
                        $ YanaX.Statup("Obed", 50, 2)
                        $ YanaX.Statup("Obed", 90, 1)
                    ch_y "Что ж, хорошо, я останусь."
                    $ Line = "yes"

                elif ApprovalCheck(YanaX, 200, "O"):
                    #she is not obedient
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Love", 70, -4)
                        $ YanaX.Statup("Love", 90, -2)
                    ch_y ". . ."
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Inbt", 40, 2)
                        $ YanaX.Statup("Inbt", 60, 1)
                        $ YanaX.Statup("Obed", 70, -2)
                    ch_y "Не с таким отношением ко мне."
                else:
                    #she is obedient, but you failed to meet the checks
                    if "followed" not in YanaX.RecentActions:
                        $ YanaX.Statup("Inbt", 30, 1)
                        $ YanaX.Statup("Inbt", 50, 1)
                        $ YanaX.Statup("Love", 50, -1, 1)
                        $ YanaX.Statup("Love", 90, -2)
                        $ YanaX.Statup("Obed", 70, -1)
                    $ Line = "no"
                #End ordered to stay

    call Taboo_Level(0)
    $ YanaX.RecentActions.append("followed")
    if not Line:
            #You end the dialog neutrally
            hide Yana_Sprite
            hide Yana_Seated
            call Gym_Clothes_Off([YanaX])
            return

    if Line == "no":
            # She's refused, context based dialog
            if YanaX.Loc == "bg classroom":
                ch_y "Мне нужно учиться."
            elif YanaX.Loc == "bg dangerroom":
                ch_y "Я только разогрелась!"
            else:
                ch_y "У меня много дел."
            hide Yana_Sprite
            hide Yana_Seated
            call Gym_Clothes_Off([YanaX])
            return

    elif Line == "go to":
            #You agreed to go to her instead
            #$ Party.append(YanaX)
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")
            $ YanaX.RecentActions.append("goto")
            $ Player.RecentActions.append("goto")
            $ Player.DrainWord("locked",0,0,1)
            hide Yana_Sprite
            hide Yana_Seated
            $ Nearby = []
            $ Party = [YanaX]
            call Gym_Clothes_Off([YanaX])
            if YanaX.Loc == "bg classroom":
                ch_y "Я займу тебе место."
                jump Class_Room_Entry
            elif YanaX.Loc == "bg dangerroom":
                ch_y "Тогда я пока разогреюсь."
                jump Danger_Room_Entry
            elif YanaX.Loc == "bg yana":
                ch_y "Буду ждать."
                jump Yana_Room
            elif YanaX.Loc == "bg player":
                ch_y "Буду ждать."
                jump Player_Room
            elif YanaX.Loc == "bg showerroom":
                ch_y "Буду ждать."
                jump Shower_Room_Entry
            elif YanaX.Loc == "bg campus":
                ch_y "Буду ждать."
                jump Campus_Entry
            elif YanaX.Loc == "bg pool":
                ch_y "Буду ждать."
                jump Pool_Entry
            elif YanaX.Loc == "bg mall":
                ch_y "Буду ждать."
                jump Mall_Entry
            else:
                ch_y "Тогда я просто встречусь с тобой в твоей комнате."
                $ YanaX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at

    #She's agreed to come over
    elif Line == "lonely":
            ch_y "Я бы этого не хотела. . ."
    elif Line == "command":
            ch_y "Что ж, хорошо, [YanaX.Petname]."
    elif Line == "fun":
            ch_y "Конечно."

    $ Line = 0
    ch_y "Я останусь здесь."
    $ YanaX.Loc = bg_current
    return

# End Yana Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

### Yana's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Yana_Clothes:   #rkeljsvgbdw
    if YanaX.Taboo:
            if "exhibitionist" in YanaX.Traits:
                ch_y "Хммммм . ."
            elif ApprovalCheck(YanaX, 900, TabM=4) or ApprovalCheck(YanaX, 400, "I", TabM=3):
                ch_y "Я бы предпочла не переодеваться здесь. . ."
            else:
                ch_y "Я бы предпочла не переодеваться здесь. . ."
                ch_y "Почему бы нам не поговорить об этом в одной из наших комнат?"
                return
    elif ApprovalCheck(YanaX, 900, TabM=4) or ApprovalCheck(YanaX, 600, "L") or ApprovalCheck(YanaX, 300, "O"):
                ch_y "Что ты желаешь обсудить?"
    else:
                ch_y "Почему тебя волнует моя одежда?"
                return

    if Girl != YanaX or Line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ Line = 0
    $ Girl = YanaX
    call Shift_Focus(Girl)

label Yana_Wardrobe_Menu:
    $ YanaX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .
    while True:
        menu:
            ch_y "Что ты желаешь обсудить?"
            "Верх":
                        call Yana_Clothes_Over
            "Низ":
                        call Yana_Clothes_Legs
            "Нижнее белье":
                        call Yana_Clothes_Under
            "Аксессуары":
                        call Yana_Clothes_Misc
            "Управление нарядами":
                        call Yana_Clothes_Outfits
            "Давай поговорим о том, что ты носишь.":
                        call Clothes_Schedule(YanaX)

            "Могу я посмотреть?" if YanaX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(YanaX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_y "Что думаешь?"
                    hide PhoneSex
            "Могу я посмотреть?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(YanaX,0,2)
                    if _return:
                        hide DressScreen
            "Может, тебе будет комфортнее за ширмой? (locked)" if YanaX.Taboo:
                    pass
            "Может, тебе будет комфортнее за ширмой?" if YanaX.Loc == bg_current and not YanaX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if not Player.Male and "girltalk" not in YanaX.History and "nogirls" not in YanaX.History:
                            ch_y "Ох, она ни к чему."
                    elif ApprovalCheck(YanaX, 1500) or (YanaX.SeenChest and YanaX.SeenPussy):
                            if not Player.Male:
                                ch_y "Что ты там еще не видела?"
                            else:
                                ch_y "Что ты там еще не видел?"
                    else:
                            show DressScreen zorder 150
                            ch_y "Пожалуй."

            "У меня есть подарок для тебя (locked)" if YanaX.Loc != bg_current:
                            pass
            "У меня есть подарок для тебя" if YanaX.Loc == bg_current:
                            ch_p "Мне бы хотелось тебе кое-что подарить."
                            call Gifts #(Girl)

            "Переключиться на. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(YanaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ YanaX.OutfitChange()
                    $ YanaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != YanaX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = YanaX
                    call Shift_Focus(Girl)

            "Сменить вид [[заблокировано] (locked)" if Girl.Loc != bg_current or renpy.showing('DressScreen'):
                    pass
            "Сменить вид" if Girl.Loc == bg_current and not renpy.showing('DressScreen'):
                    call WardrobeView(YanaX)

            "Неважно, ты и так хорошо выглядишь.":
                    call Girl_Pos_Reset(YanaX)
                    if "wardrobe" not in YanaX.RecentActions:
                            #Apply stat boosts only if it's the first time this turn
                            if YanaX.Chat[1] <= 1:
                                    $ YanaX.Statup("Love", 70, 15)
                                    $ YanaX.Statup("Obed", 40, 20)
                                    ch_y "Спасибо."
                            elif YanaX.Chat[1] <= 10:
                                    $ YanaX.Statup("Love", 70, 5)
                                    $ YanaX.Statup("Obed", 40, 7)
                                    ch_y "Да?"
                            elif YanaX.Chat[1] <= 50:
                                    $ YanaX.Statup("Love", 70, 1)
                                    $ YanaX.Statup("Obed", 40, 1)
                                    ch_y "Да? Ладно."
                            else:
                                    ch_y "Конечно."
                            $ YanaX.RecentActions.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(YanaX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ YanaX.OutfitChange()
                    $ YanaX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ YanaX.Chat[1] += 1
                    $ Trigger = 0
                    if YanaX.Panties and "pantyless" in YanaX.DailyActions:  #resets pantyless state if you had her put a pair on
                            $ YanaX.DailyActions.remove("pantyless")
                    return

        #Loops back up
        #return #jump Yana_Clothes
        #End of Yana Wardrobe Main Menu

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Yana_Clothes_Outfits:
        # Outfits
        "Ты должна запомнить этот наряд. [[Сохранить наряд]":
                menu:
                    "В какой слот вы желаете сохранить его?"
                    "Пользовательский 1":
                                call OutfitShame(YanaX,3,1)
                    "Пользовательский 2":
                                call OutfitShame(YanaX,5,1)
                    "Пользовательский 3":
                                call OutfitShame(YanaX,6,1)
                    "Спортивная одежда":
                                call OutfitShame(YanaX,4,1)
                    "Одежда для сна":
                                call OutfitShame(YanaX,7,1)
                    "Купальник":
                                call OutfitShame(YanaX,10,1)

                    "Повседневка 1" if ApprovalCheck(YanaX, 2500):
                                call OutfitShame(YanaX,11,1)
                    "Повседневка 2" if ApprovalCheck(YanaX, 2500):
                                call OutfitShame(YanaX,12,1)
                    #8 is Emma's teaching clothes,
                    "Неважно":
                                pass

        "Надень футболку и шорты.":
                $ YanaX.OutfitChange("casual1")
                menu:
                    "Ходи теперь в этом. [[Выбрать текущий наряд]":
                            $ YanaX.Outfit = "casual1"
                            $ YanaX.Shame = 0
                            ch_y "Да, мне они идут."
                    "Давай попробуем что-нибудь другое.":
                            ch_y "Ах."

        "Надень блузку и юбку.":
                $ YanaX.OutfitChange("casual2")
                menu:
                    "Ходи теперь в этом. [[Выбрать текущий наряд]":
                            $ YanaX.Outfit = "casual2"
                            $ YanaX.Shame = 0
                            ch_y "Мне они нравятся."
                    "Давай попробуем что-нибудь другое.":
                            ch_y "Ах."

        "Помнишь тот наряд, который мы подобрали вместе? [[сперва соберите и сохраните наряд] (locked)" if not YanaX.Custom1[0] and not YanaX.Custom2[0] and not YanaX.Custom3[0]:
                        pass

        "Помнишь тот наряд, который мы подобрали вместе?" if YanaX.Custom1[0] or YanaX.Custom2[0] or YanaX.Custom3[0]:
                $ Cnt = 0
                while 1:
                    menu:
                        "Надень Пользовательский 1 (locked)" if not YanaX.Custom1[0]:
                                pass
                        "Надень Пользовательский 1" if YanaX.Custom1[0]:
                                $ YanaX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Надень Пользовательский 2 (locked)" if not YanaX.Custom2[0]:
                                pass
                        "Надень Пользовательский 2" if YanaX.Custom2[0]:
                                $ YanaX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Надень Пользовательский 3 (locked)" if not YanaX.Custom3[0]:
                                pass
                        "Надень Пользовательский 3" if YanaX.Custom3[0]:
                                $ YanaX.OutfitChange("custom3")
                                $ Cnt = 6

                        "Ты должна одеваться так, когда мы наедине (locked)" if not Cnt:
                                pass
                        "Ты должна одеваться так, когда мы наедине" if Cnt:
                                if Cnt == 5:
                                    $ YanaX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ YanaX.Clothing[9] = "custom3"
                                else:
                                    $ YanaX.Clothing[9] = "custom1"
                                ch_y "Oh, sure."

                        "Если подумать, то лучше забудь один из нарядов, которые мы подобрали вместе. . .":
                                menu:
                                    "Пользовательский 1 [[очистить слот 1]" if YanaX.Custom1[0]:
                                        ch_y "Ах."
                                        $ YanaX.Custom1[0] = 0
                                    "Пользовательский 1 [[очистить слот 1] (locked)" if not YanaX.Custom1[0]:
                                        pass
                                    "Пользовательский 2 [[очистить слот 2]" if YanaX.Custom2[0]:
                                        ch_y "Ах."
                                        $ YanaX.Custom2[0] = 0
                                    "Пользовательский 2 [[очистить слот 2] (locked)" if not YanaX.Custom2[0]:
                                        pass
                                    "Пользовательский 3 [[очистить слот 3]" if YanaX.Custom3[0]:
                                        ch_y "Ах."
                                        $ YanaX.Custom3[0] = 0
                                    "Пользовательский 3 [[очистить слот 3] (locked)" if not YanaX.Custom3[0]:
                                        pass
                                    "Неважно [[назад]":
                                        pass

                        "Тебе следует надеть его [[сначала нужно выбрать наряд] (locked)" if not Cnt:
                                pass
                        "Тебе следует надеть его" if Cnt:
                                call Custom_Out(YanaX,Cnt)
                        "Ладно, вернемся к началу нашего разговора. . .":
                                $ Cnt = 0
                                return #jump Yana_Clothes

        "Наденешь спортивную одежду?" if not YanaX.Taboo or bg_current == "bg dangerroom":
                $ YanaX.OutfitChange("gym")

        "Наденешь одежду для сна?" if not YanaX.Taboo:
                if ApprovalCheck(YanaX, 1200):
                        $ YanaX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(YanaX)
                        if _return:
                            $ YanaX.OutfitChange("sleep")

        "Наденешь купальник? (locked)" if (YanaX.Taboo and bg_current != "bg pool" and not ApprovalCheck(YanaX, 800, TabM=2)) or not YanaX.Swim[0]:
                $ YanaX.OutfitChange("swimwear")
        "Наденешь купальник?" if (not YanaX.Taboo or bg_current == "bg pool" or ApprovalCheck(YanaX, 800, TabM=2)) and YanaX.Swim[0]:
                $ YanaX.OutfitChange("swimwear")

        "Наденешь хэллоуинский костюм?" if "halloween" in YanaX.History:
                ch_y "Ладно."
                $ YanaX.OutfitChange("costume")

        "Ты выглядишь прекрасно без одежды. . .":
                #Nude
                $ YanaX.FaceChange("sexy", 1)
                $ Line = 0
                if not YanaX.Chest and not YanaX.Panties and not YanaX.Over and not YanaX.Legs and not YanaX.Hose:
                    if not Player.Male:
                        ch_y "Ты подглядывала за мной?"
                    else:
                        ch_y "Ты подглядывал за мной?"
                elif YanaX.SeenChest and YanaX.SeenPussy and ApprovalCheck(YanaX, 1200, TabM=4):
                    ch_y "Спасибо. . ."
                    $ Line = 1
                elif ApprovalCheck(YanaX, 2000, TabM=4):
                    ch_y ". . ."
                    $ Line = 1
                elif YanaX.SeenChest and YanaX.SeenPussy and ApprovalCheck(YanaX, 1200, TabM=0):
                    ch_y "Да, но не в сложившихся обстоятельствах. . ."
                elif ApprovalCheck(YanaX, 2000, TabM=0):
                    ch_y "Да, но не в сложившихся обстоятельствах. . ."
                elif ApprovalCheck(YanaX, 1000, TabM=0):
                    $ YanaX.FaceChange("confused", 1,Mouth="smirk")
                    ch_y "Да, но не в сложившихся обстоятельствах. . ."
                    $ YanaX.FaceChange("bemused", 0)
                else:
                    $ YanaX.FaceChange("angry", 1)
                    ch_y "Да?"

                call expression YanaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "nogirls" in YanaX.History:
                        $ Line = 0
                if Line:
                    #If she got nude. . .
                    $ YanaX.OutfitChange("nude")
                    "Она сбрасывает одежду к своим ногам."
                    call Girl_First_Topless(YanaX)
                    call Girl_First_Bottomless(YanaX,1)
                    $ YanaX.FaceChange("sexy")
                    menu:
                        "Знаешь, мне кажется. что ты должна ходить в таком виде. [[установить текущий наряд]":
                            if "exhibitionist" in YanaX.Traits:
                                ch_y "Хммм. . ."
                                $ YanaX.Outfit = "nude"
                                $ YanaX.Statup("Lust", 50, 10)
                                $ YanaX.Statup("Lust", 70, 5)
                                $ YanaX.Shame = 50
                            elif ApprovalCheck(YanaX, 800, "I") or ApprovalCheck(YanaX, 2800, TabM=0):
                                ch_y "Я не уверена. . ."
                                $ YanaX.Outfit = "nude"
                                $ YanaX.Shame = 50
                            else:
                                $ YanaX.FaceChange("sexy", 1)
                                $ YanaX.Eyes = "surprised"
                                ch_y "Ты шутишь!"

                        "Давай попробуем что-нибудь другое.":
                            if "exhibitionist" in YanaX.Traits:
                                ch_y "Ах."
                            elif ApprovalCheck(YanaX, 800, "I") or ApprovalCheck(YanaX, 2800, TabM=0):
                                $ YanaX.FaceChange("bemused", 1)
                                ch_y "Значит, ты -не- хочешь, чтобы я ходила в таком виде? . ."
                                ch_y ". . ."
                            else:
                                $ YanaX.FaceChange("confused", 1)
                                ch_y "Я бы не стала выходить на улицу в таком виде. . ."
                $ Line = 0

        "Неважно":
            return #jump Yana_Clothes

    return #jump Yana_Clothes
    #End of Yana Outfits

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Yana_Clothes_Over:
        # Overshirts
        "Почему бы тебе не снять [get_clothing_name(YanaX.Over_key, vin)]?" if YanaX.Over:
                call Wardrobe_Remove(YanaX)

        "Примерь белую блузу" if YanaX.Over != "shirt":
                $ YanaX.FaceChange("bemused")
                if not YanaX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_y "Конечно."
                elif ApprovalCheck(YanaX, 800, TabM=0):
                    ch_y "Конечно."
                else:
                    call Display_DressScreen(YanaX)
                    if not _return:
                            $ YanaX.FaceChange("bemused", 1)
                            ch_y "Я бы не хотела сейчас переодевать [get_clothing_name(YanaX.Over_key, vin)]."
                            return #jump Yana_Clothes
                $ YanaX.Over = "shirt"

        "Примерь футболку" if YanaX.Over != "tshirt":
                $ YanaX.FaceChange("bemused")
                if not YanaX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_y "Конечно."
                elif ApprovalCheck(YanaX, 800, TabM=0):
                    ch_y "Конечно."
                else:
                    call Display_DressScreen(YanaX)
                    if not _return:
                            $ YanaX.FaceChange("bemused", 1)
                            ch_y "Я не собираюсь сейчас переодевать [get_clothing_name(YanaX.Over_key, vin)]."
                            return #jump Yana_Clothes
                $ YanaX.Over = "tshirt"

        "Примерь спортивную куртку" if YanaX.Over != "tracksuit":
                $ YanaX.FaceChange("bemused")
                if not YanaX.Over:
                    #if she's not already wearing a top, or has the leather bra on
                    ch_y "Конечно."
                elif ApprovalCheck(YanaX, 800, TabM=0):
                    ch_y "Конечно."
                else:
                    call Display_DressScreen(YanaX)
                    if not _return:
                            $ YanaX.FaceChange("bemused", 1)
                            ch_y "Я не собираюсь сейчас переодевать [get_clothing_name(YanaX.Over_key, vin)]."
                            return #jump Yana_Clothes
                $ YanaX.Over = "tracksuit"

#        "Purple top" if YanaX.Over != "purple top" and "halloween" in YanaX.History:
#                $ YanaX.FaceChange("bemused")
#                if not YanaX.Over:
#                    #if she's not already wearing a top, or has the leather bra on
#                    ch_y "Конечно."
#                elif ApprovalCheck(YanaX, 800, TabM=0):
#                    ch_y "Конечно."
#                else:
#                    call Display_DressScreen(YanaX)
#                    if not _return:
#                            $ YanaX.FaceChange("bemused", 1)
#                            ch_y "I don't want to take this [YanaX.Over] off right now."
#                            return #jump Yana_Clothes
#                $ YanaX.Over = "purple top"

        "Может, просто накинешь полотенце?" if YanaX.Over != "towel":
                $ YanaX.FaceChange("bemused", 1)
                if YanaX.Chest or YanaX.SeenChest:
                    ch_y ". . ."
                elif ApprovalCheck(YanaX, 1000, TabM=0):
                    $ YanaX.FaceChange("perplexed", 1)
                    ch_y "Ладно. . ."
                else:
                    call Display_DressScreen(YanaX)
                    if not _return:
                            ch_y "Я не хочу сейчас укутываться в полотенце."
                            return #jump Yana_Clothes
                $ YanaX.Over = "towel"

        "Сними [get_clothing_name(YanaX.Acc_key, vin)]" if YanaX.Acc:
                $ YanaX.FaceChange("bemused")
                ch_y "Конечно."
                $ YanaX.Acc = 0

        "Неважно":
            pass
    return #jump Yana_Clothes
    #End of Yana Top

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Yana_NoBra:
        menu:
            ch_y "У меня под [get_clothing_name(YanaX.Over_key, tvo)] ничего нет. . ."
            "Тогда надень что-нибудь. . .":
                        if YanaX.SeenChest and ApprovalCheck(YanaX, 1000, TabM=3):
                                $ YanaX.Blush = 1
                                ch_y "Меня это не особо беспокоит. . ."
                                $ YanaX.Blush = 0
                        elif ApprovalCheck(YanaX, 1200, TabM=4):
                                $ YanaX.Blush = 1
                                ch_y "Если честно, меня это не беспокоит. . ."
                                $ YanaX.Blush = 0
                        elif ApprovalCheck(YanaX, 900, TabM=2) and "lace bra" in YanaX.Inventory:
                                ch_y "Я могу что-нибудь подобрать."
                                $ YanaX.Chest  = "lace bra"
                                "Она достает свой кружевной лифчик и надевает его под [get_clothing_name(YanaX.Over_key, vin)]."
                        elif ApprovalCheck(YanaX, 700, TabM=2):
                                ch_y "Я могу что-нибудь подобрать."
                                $ YanaX.Chest = "white bra"
                                "Она достает свой белый лифчик и надевает его под [get_clothing_name(YanaX.Over_key, vin)]."
                        else:
                                ch_y "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(YanaX, 1100, "LI", TabM=2) and YanaX.Love > YanaX.Inbt:
                                ch_y "Конечно. . ."
                        elif ApprovalCheck(YanaX, 700, "OI", TabM=2) and YanaX.Obed > YanaX.Inbt:
                                ch_y "Конечно. . ."
                        elif ApprovalCheck(YanaX, 600, "I", TabM=2):
                                ch_y "Ах. . ."
                        elif ApprovalCheck(YanaX, 1300, TabM=2):
                                ch_y "Что ж, пожалуй."
                        else:
                                $ YanaX.FaceChange("surprised")
                                $ YanaX.Brows = "angry"
                                if YanaX.Taboo > 20:
                                    ch_y "Не на людях. Извини."
                                else:
                                    ch_y "Нет, конечно, [YanaX.Petname]!"
                                call expression YanaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                        ch_y "Ах. . ."
                        return 0
        return 1
        #End of Yana bra check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Yana_Clothes_Legs:
        # Leggings
        "Может, снимешь [get_clothing_name(YanaX.Legs_key, vin)]?" if YanaX.Legs:
                call Wardrobe_Remove(YanaX,1)


        "Примерь черные шорты" if YanaX.Legs != "shorts":
                ch_p "Ты великолепно выглядишь в черных шортах."
                ch_y "Да?"
                $ YanaX.Legs = "shorts"

        "Примерь желтую юбку" if YanaX.Legs != "skirt":
                ch_p "Почему бы тебе не примерить желтую юбку?"
                ch_y "Пожалуй, можно?"
                $ YanaX.Legs = "skirt"

        "Примерь спортивные штаны" if YanaX.Legs != "pants":
                ch_p "Как насчет спортивных штанов?"
                ch_y "Пожалуй, можно?"
                $ YanaX.Legs = "pants"

#        "Purple skirt" if YanaX.Legs != "skirt" and "halloween" in YanaX.History:
#                ch_p "What about wearing your purple skirt?"
#                ch_y "Yes?"
#                $ YanaX.Legs = "skirt"

        "Сними обувь (locked)" if not YanaX.Boots:
                pass
        "Сними [get_clothing_name(YanaX.Boots_key, vin)]" if YanaX.Boots:
                ch_p "Может, снимешь [get_clothing_name(YanaX.Boots_key, vin)]?"
                ch_y "Ладно."
                $ YanaX.Boots = 0
#        "Add Sneakers" if YanaX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_y "Ok."
#                $ YanaX.Boots = "sneaks"
        "Надень ботинки" if YanaX.Boots != "boots":
                ch_p "Может, наденешь ботинки?"
                ch_y "Ладно."
                $ YanaX.Boots = "boots"
#        "Add Sneakers" if YanaX.Boots != "sneaks":
#                ch_p "Maybe put your sneakers on."
#                ch_y "'K."
#                $ YanaX.Boots = "sneaks"

        "Неважно":
                pass
    return #jump Yana_Clothes
    #End of Yana Pants

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    label Yana_NoPantiesOn:
        menu:
            ch_y "На мне сейчас нет трусиков. . ."
            "Тогда тебе стоит надеть какие-нибудь. . .":
                        if YanaX.SeenPussy and ApprovalCheck(YanaX, 1100, TabM=4):
#                                $ YanaX.Blush = 2
                                ch_y "Мне и без них неплохо. . ."
#                                $ YanaX.Blush = 1
                        elif ApprovalCheck(YanaX, 1500, TabM=4):
                                $ YanaX.Blush = 2
                                ch_y "Мне и без них неплохо. . ."
                                $ YanaX.Blush = 1
                        elif ApprovalCheck(YanaX, 700, TabM=4):
                                ch_y "Ах, да."
                                if "lace panties" in YanaX.Inventory:
                                        ch_y "Мне нравится ход твоих мыслей."
                                        $ YanaX.Panties  = "lace panties"
                                else:
                                        $ YanaX.Panties = "white panties"
                                if ApprovalCheck(YanaX, 1200, TabM=4):
                                    $ Line = get_clothing_name(YanaX.Legs_key, vin)
                                    $ YanaX.Legs = 0
                                    "Она снимает [Line] и натягивает [get_clothing_name(YanaX.Panties_key, vin)]."
                                elif YanaX.Legs == "skirt":
                                    "Она достает [get_clothing_name(YanaX.Panties_key, vin)] и натягивает их под юбку."
                                    $ YanaX.Legs = 0
                                    "Затем она сбрасывает юбку на пол."
                                else:
                                    $ Line = get_clothing_name(YanaX.Legs_key, vin)
                                    $ YanaX.Legs = 0
                                    "Она на мгновение исчезает, а затем возвращается только в [get_clothing_name(YanaX.Panties_key, dat)]."
                                return #jump Yana_Clothes
                        else:
                                ch_y "Я так не думаю."
                                return 0

            "Так даже лучше. . .":
                        if ApprovalCheck(YanaX, 1100, "LI", TabM=3) and YanaX.Love > YanaX.Inbt:
                                ch_y "Естественно. . ."
                        elif ApprovalCheck(YanaX, 700, "OI", TabM=3) and YanaX.Obed > YanaX.Inbt:
                                ch_y "Конечно. . ."
                        elif ApprovalCheck(YanaX, 600, "I", TabM=3):
                                ch_y "Что ж, пожалуй. . ."
                        elif ApprovalCheck(YanaX, 1300, TabM=2):
                                ch_y "Что ж, пожалуй. . ."
                        else:
                                $ YanaX.FaceChange("surprised")
                                $ YanaX.Brows = "angry"
                                if YanaX.Taboo > 20:
                                    ch_y "Но не в общественном месте."
                                else:
                                    ch_y "Нет, конечно, [YanaX.Petname]."
                                call expression YanaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                                return 0
            "Неважно.":
                ch_y "Ах. . ."
                return 0
        return 1
        #End of Yana Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Yana_Clothes_Under:
        "Верх":
            menu:
                "Может, снимешь [get_clothing_name(YanaX.Chest_key, vin)]?" if YanaX.Chest:
                        $ YanaX.FaceChange("bemused", 1)
                        if YanaX.SeenChest and ApprovalCheck(YanaX, 900, TabM=2.7):
                                ch_y "Без проблем."
                        elif ApprovalCheck(YanaX, 1100, TabM=2):
                            if YanaX.Taboo:
                                ch_y "Я не хочу делать этого здесь. . ."
                            else:
                                ch_y "Пожалуй, можно. . ."
#                        elif YanaX.Over == "jacket" and ApprovalCheck(YanaX, 600, TabM=2):
#                            ch_y "This jacket is a bit revealing. . ."
                        elif YanaX.Over and ApprovalCheck(YanaX, 500, TabM=2):
                            ch_y "Пожалуй, можно. . ."
                        elif not YanaX.Over:
                            call Display_DressScreen(YanaX)
                            if not _return:
                                ch_y "Сперва мне нужно что-нибудь надеть сверху."
                                return #jump Yana_Clothes
                        else:
                            call Display_DressScreen(YanaX)
                            if not _return:
                                ch_y "Я так не думаю."
                                return #jump Yana_Clothes
                        $ Line = get_clothing_name(YanaX.Chest_key, vin)
                        $ YanaX.Chest = 0
                        if YanaX.Over:
                            "Она залезает под [get_clothing_name(YanaX.Over_key, vin)], хватает и снимает [Line], а затем бросает на пол."
                        else:
                            "Она скидывает [Line] на пол."
                            if not renpy.showing('DressScreen'):
                                call Girl_First_Topless(YanaX)

                "Примерь белый лифчик" if YanaX.Chest != "white bra":
                        ch_p "Мне нравится твой белый лифчик."
                        if YanaX.SeenChest or ApprovalCheck(YanaX, 1100, TabM=2):
                            ch_y "Да?"
                            $ YanaX.Chest = "white bra"
                        else:
                            call Display_DressScreen(YanaX)
                            if not _return:
                                ch_y "Он почти ничего не прикрывает. . ."
                            else:
                                $ YanaX.Chest = "white bra"


                "Примерь кружевной лифчик" if YanaX.Chest != "lace bra" and "lace bra" in YanaX.Inventory:
                        ch_p "Мне нравится твой кружевной лифчик."
                        if YanaX.SeenChest or ApprovalCheck(YanaX, 1300, TabM=2):
                            ch_y "Конечно."
                            $ YanaX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(YanaX)
                            if not _return:
                                ch_y "Я не уверена на его счет. . ."
                            else:
                                $ YanaX.Chest = "lace bra"

                "Примерь спортивный лифчик" if YanaX.Chest != "sports bra":
                        ch_p "Мне нравится твой спортивный лифчик."
                        if YanaX.SeenChest or ApprovalCheck(YanaX, 1100, TabM=2):
                            ch_y "Да?"
                            $ YanaX.Chest = "sports bra"
                        else:
                            call Display_DressScreen(YanaX)
                            if not _return:
                                ch_y "Я не уверена на его счет. . ."
                            else:
                                $ YanaX.Chest = "sports bra"

                "Примерь лифчик бикини" if YanaX.Chest != "bikini top" and "bikini top" in YanaX.Inventory:
                        ch_p "Мне нравится твой лифчик бикини."
                        if bg_current == "bg pool":
                                ch_y "Конечно."
                                $ YanaX.Chest = "bikini top"
                        else:
                                if YanaX.SeenChest or ApprovalCheck(YanaX, 1000, TabM=2):
                                    ch_y "Конечно?"
                                    $ YanaX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(YanaX)
                                    if not _return:
                                            ch_y "Я не уверена, мы сейчас не на пляже. . ."
                                    else:
                                            $ YanaX.Chest = "bikini top"
                "Неважно":
                        pass
            return #jump Yana_Clothes_Under

        "Варианты колготок и чулок":
            menu:
                "Сними [get_clothing_name(YanaX.Hose_key, vin)]." if YanaX.Hose:
                                $ YanaX.FaceChange("sexy", 1)
                                if YanaX.SeenPanties and YanaX.Panties and ApprovalCheck(YanaX, 500, TabM=5):
                                    ch_y "Конечно."
                                elif YanaX.SeenPussy and ApprovalCheck(YanaX, 900, TabM=4):
                                    ch_y "Конечно."
                                elif ApprovalCheck(YanaX, 1300, TabM=2) and YanaX.Panties:
                                    ch_y "Ладно, раз просишь ты. . ."
                                elif ApprovalCheck(YanaX, 700) and not YanaX.Panties:
                                    call Yana_NoPantiesOn
                                    if not _return and not YanaX.Panties:
                                        if not ApprovalCheck(YanaX, 1500):
                                            call Display_DressScreen(YanaX)
                                            if not _return:
                                                return #jump Yana_Clothes
                                        else:
                                                return #jump Yana_Clothes
                                else:
                                    call Display_DressScreen(YanaX)
                                    if not _return:
                                        ch_y "Я так не думаю."
                                        if not YanaX.Panties:
                                                ch_y "На мне сейчас нет трусиков. . ."
                                        return #jump Yana_Clothes
                                $ YanaX.Hose = 0

                "Чулки дополнили бы твой образ." if YanaX.Hose != "stockings" and Girl.Tag + " stockings and garterbelt" in YanaX.Inventory:
                                $ YanaX.Hose = "stockings"
                "Колготки дополнили бы твой образ." if YanaX.Hose != "pantyhose" and Girl.Tag + " pantyhose" in YanaX.Inventory:
                                $ YanaX.Hose = "pantyhose"
                "Рваные колготки дополнили бы твой образ." if YanaX.Hose != "ripped pantyhose" and "ripped pantyhose" in YanaX.Inventory:
                                $ YanaX.Hose = "ripped pantyhose"
                "Черные леггинсы дополнили бы твой образ." if YanaX.Hose != "tights":
                                $ YanaX.Hose = "tights"
                "Рваные леггинсы дополнили бы твой образ." if YanaX.Hose != "ripped tights" and "ripped tights" in YanaX.Inventory:
                                $ YanaX.Hose = "ripped tights"
                "Чулки и пояс с подвязками дополнили бы твой образ." if YanaX.Hose != "stockings and garterbelt" and Girl.Tag + " stockings and garterbelt" in YanaX.Inventory:
                                $ YanaX.Hose = "stockings and garterbelt"
                "Может, наденешь только пояс с подвязками?" if YanaX.Hose != "garterbelt" and Girl.Tag + " stockings and garterbelt" in YanaX.Inventory:
                                $ YanaX.Hose = "garterbelt"
                "Черные носки дополнили бы твой образ." if YanaX.Hose != "socks":
                                $ YanaX.Hose = "socks"
                "Неважно":
                        pass
            return #jump Yana_Clothes_Under

        #Panties
        "Низ":
            menu:
                "Ты должна снять [get_clothing_name(YanaX.Panties_key, vin)]. . ." if YanaX.Panties:
                        $ YanaX.FaceChange("bemused", 1)
                        if ApprovalCheck(YanaX, 900) and (YanaX.Legs or (YanaX.SeenPussy and not YanaX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                                if ApprovalCheck(YanaX, 850, "L"):
                                        ch_y "Без проблем. . ."
                                elif ApprovalCheck(YanaX, 500, "O"):
                                        ch_y "Конечно."
                                elif ApprovalCheck(YanaX, 350, "I"):
                                        ch_y "Ах."
                                else:
                                        ch_y "Это можно. . ."
                        else:                       #low approval or not wearing pants or in public
                                if ApprovalCheck(YanaX, 1100, "LI", TabM=3) and YanaX.Love > YanaX.Inbt:
                                        ch_y "Не на людях. . ."
                                elif ApprovalCheck(YanaX, 700, "OI", TabM=3) and YanaX.Obed > YanaX.Inbt:
                                        ch_y "Что ж. . ."
                                elif ApprovalCheck(YanaX, 600, "I", TabM=3):
                                        ch_y "Хммм. . ."
                                elif ApprovalCheck(YanaX, 1300, TabM=3):
                                        ch_y "Хм. . ."
                                else:
                                        call Display_DressScreen(YanaX)
                                        if not _return:
                                            $ YanaX.FaceChange("surprised")
                                            $ YanaX.Brows = "angry"
                                            if YanaX.Taboo > 20:
                                                ch_y "Не на людях. Извини."
                                            else:
                                                ch_y "Нет, конечно, [YanaX.Petname]!"
                                            return #jump Yana_Clothes
                        $ Line = get_clothing_name(YanaX.Panties_key, vin)
                        $ YanaX.Panties = 0
                        if not YanaX.Legs:
                            "Она снимает [Line] и бросает их на пол."
                            if not renpy.showing('DressScreen'):
                                    call Girl_First_Bottomless(YanaX)
                        elif ApprovalCheck(YanaX, 1200, TabM=4):
                            $ Trigger = YanaX.Legs
                            $ YanaX.Legs = 0
                            pause 0.5
                            $ YanaX.Legs = Trigger
                            "Она снимает [get_clothing_name(YanaX.Legs_key, vin)] и [Line], затем снова надевает [get_clothing_name(YanaX.Legs_key, vin)]."
                            $ Trigger = 1
                            call Girl_First_Bottomless(YanaX,1)
                        elif YanaX.Legs == "skirt":
                            "Она залезает под юбку и стягивает [Line]."
                        else:
                            $ YanaX.Blush = 1
                            "Она на мгновение отходит, а затем возвращается."
                            $ YanaX.Blush = 0
                        $ Line = 0

                "Почему бы тебе вместо этих не надеть белые трусики?" if YanaX.Panties and YanaX.Panties != "white panties":
                        if ApprovalCheck(YanaX, 1100, TabM=3):
                                ch_y "Без проблем."
                                $ YanaX.Panties = "white panties"
                        else:
                                call Display_DressScreen(YanaX)
                                if not _return:
                                        ch_y "Мое нижнее белье тебя не касается."
                                else:
                                        $ YanaX.Panties = "white panties"

                "Почему бы тебе вместо этих не надеть кружевные трусики?" if "lace panties" in YanaX.Inventory and YanaX.Panties and YanaX.Panties != "lace panties":
                        if ApprovalCheck(YanaX, 1300, TabM=3):
                                ch_y "Без проблем."
                                $ YanaX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(YanaX)
                                if not _return:
                                        ch_y "Мое нижнее белье тебя не касается."
                                else:
                                        $ YanaX.Panties = "lace panties"

                "Примерь трусики бикини" if YanaX.Panties != "bikini bottoms" and "bikini bottoms" in YanaX.Inventory:
                        ch_p "Мне нравятся твои трусики бикини."
                        if bg_current == "bg pool":
                                ch_y "Без проблем."
                                $ YanaX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(YanaX, 800, TabM=2):
                                    ch_y "Без проблем."
                                    $ YanaX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(YanaX)
                                    if not _return:
                                            ch_y "Мы сейчас не на пляже. . ."
                                    else:
                                            $ YanaX.Panties = "bikini bottoms"

                "Знаешь, ты могла надеть какие-нибудь трусики. . ." if not YanaX.Panties:
                        $ YanaX.FaceChange("bemused", 1)
                        if YanaX.Legs and (YanaX.Love+YanaX.Obed) <= (2 * YanaX.Inbt):
                            $ YanaX.Mouth = "smile"
                            ch_y "Я бы предпочла этого не делать. . ."
                            menu:
                                "Твое право":
                                    return #jump Yana_Clothes
                                "Я настаиваю, надевай.":
                                    if (YanaX.Love+YanaX.Obed) <= (1.5 * YanaX.Inbt):
                                        $ YanaX.FaceChange("angry", Eyes="side")
                                        ch_y "Жаль."
                                        return #jump Yana_Clothes
                                    else:
                                        $ YanaX.FaceChange("sadside")
                                        ch_y "Ах, ладно. . ."
                        else:
                            ch_y "Пожалуй. . ."
                        menu:
                            extend ""
                            "Как насчет белых?":
                                    ch_y "Без проблем."
                                    $ YanaX.Panties = "white panties"
                            "Как насчет кружевных?" if "lace panties" in YanaX.Inventory:
                                    ch_y "Без проблем."
                                    $ YanaX.Panties  = "lace panties"
                            "Как насчет трусиков бикини?" if "bikini bottoms" in YanaX.Inventory:
                                    ch_y "Без проблем."
                                    $ YanaX.Panties = "bikini bottoms"
                "Неважно":
                    pass
            return #jump Yana_Clothes_Under
        "Неважно":
            pass
    return #jump Yana_Clothes
    #End of Yana Underwear

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    menu Yana_Clothes_Misc:
        #Misc
        "Сухие волосы" if YanaX.Hair == "wet" or YanaX.Hair == "wetlong":
                ch_p "Тебе идут сухие волосы."
                if ApprovalCheck(YanaX, 600):
                    ch_y "Ах, ладно."
                    show blackscreen onlayer black
                    "Она исчезает в портале, а через минуту появляется снова перед вами."
#                    if YanaX.Hair == "wet":
#                        $ YanaX.Hair = "short"
#                    else:
                    $ YanaX.Hair = "long"
                    hide blackscreen onlayer black
                else:
                    ch_y "Мне нравится моя нынешняя прическа."

        "Волосы в пучке" if YanaX.Hair != "bun":
                ch_p "Мне кажется, тебе идет, когда ты собираешь волосы в пучок."
                if ApprovalCheck(YanaX, 600):
                    ch_y "Ах, ладно."
                    show blackscreen onlayer black
                    "Она исчезает в портале, а через мгновение появляется снова перед вами."
                    $ YanaX.Hair = "bun"
                    hide blackscreen onlayer black
                else:
                    ch_y "Мне нравится моя нынешняя прическа."
        "Распущенные волосы" if YanaX.Hair == "bun":
                ch_p "Тебе идут распущенные волосы."
                if ApprovalCheck(YanaX, 600):
                    ch_y "Ах, ладно."
                    show blackscreen onlayer black
                    "Она исчезает в портале, а через мгновение появляется снова перед вами."
                    $ YanaX.Hair = "long"
                    hide blackscreen onlayer black
                else:
                    ch_y "Мне нравится моя нынешняя прическа."

        "Влажные волосы" if YanaX.Hair != "wet" and YanaX.Hair != "wetlong":
                ch_p "Тебе стоит увлажнить волосы."
                if ApprovalCheck(YanaX, 800):
                    ch_y "Ах, ладно."
                    $ YanaX.Hair = "wet"
                    show blackscreen onlayer black
                    "Она исчезает в портале, а через минуту появляется снова перед вами."
                    hide blackscreen onlayer black
                    ch_y "Так?"
                else:
                    ch_y "Это слишком хлопотно."

        "Отрасти волосы на лобке" if not YanaX.Pubes:
                ch_p "Слушай, мне нравятся волосы на лобке. Может, отрастишь?"
                call expression YanaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                if "pubes" in YanaX.Todo:
                        $ YanaX.FaceChange("bemused", 1)
                        ch_y "В процессе."
                else:
                    $ YanaX.FaceChange("bemused", 1)
                    if ApprovalCheck(YanaX, 1000, TabM=0):
                            ch_y "Без проблем. . ."
                            show blackscreen onlayer black
                            "Она ненадолго исчезает в портале."
                            $ YanaX.Pubes = 1
                            hide blackscreen onlayer black
                    else:
                            $ YanaX.FaceChange("surprised")
                            $ YanaX.Brows = "angry"
                            ch_y ". . . это тебя не касается."
                            return #jump Yana_Clothes
#                    $ YanaX.Todo.append("pubes")
#                    $ YanaX.PubeC = 6
        "Побрей лобок" if YanaX.Pubes:
                ch_p "Мне нравится гладкий лобок."
                call expression YanaX.Tag + "_Girltalk" pass (1) #call Rogue_Girltalk
                $ YanaX.FaceChange("bemused", 1)
                if "shave" in YanaX.Todo:
                        ch_y "Скоро я все сделаю."
                else:
                    if ApprovalCheck(YanaX, 1100, TabM=0):
                        ch_y "Ах, серьезно?"
                        show blackscreen onlayer black
                        "Она ненадолго исчезает в портале."
                        $ YanaX.Pubes = 0
                        hide blackscreen onlayer black
                    else:
                        $ YanaX.FaceChange("surprised")
                        $ YanaX.Brows = "angry"
                        ch_y ". . . это тебя не касается."
                        return #jump Yana_Clothes
#                    $ YanaX.Todo.append("shave")

        "Пирсинг [[Сначала посмотрите, как она выглядит без него] (locked)" if not YanaX.SeenPussy and not YanaX.SeenChest:
            pass

        "Надень пирсинг-кольца" if YanaX.Pierce != "ring" and (YanaX.SeenPussy or YanaX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсингом-кольцами."
                if "ring" in YanaX.Todo:
                    ch_y "Я работаю над этим."
                else:
                    $ YanaX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(YanaX, 1150, TabM=0)
                    if ApprovalCheck(YanaX, 900, "L", TabM=0) or (Approval and YanaX.Love > 2* YanaX.Obed):
                        ch_y "Думаешь, он меня украсит?"
                    elif ApprovalCheck(YanaX, 600, "I", TabM=0) or (Approval and YanaX.Inbt > YanaX.Obed):
                        ch_y "Я уже думала об этом. . ."
                    elif ApprovalCheck(YanaX, 500, "O", TabM=0) or Approval:
                        ch_y "Что ж, раз тебе такое нравится, [YanaX.Petname]. . ."
                    else:
                        $ YanaX.FaceChange("surprised")
                        $ YanaX.Brows = "angry"
                        ch_y "Мне это неинтересно, [YanaX.Petname]."
                        return #jump Yana_Clothes
                    show blackscreen onlayer black
                    "Она ненадолго исчезает в портале."
                    $ YanaX.Pierce = "ring"
                    hide blackscreen onlayer black
#                    $ YanaX.Todo.append("ring")

        "Надень пирсинг-штанги" if YanaX.Pierce != "barbell" and (YanaX.SeenPussy or YanaX.SeenChest):
                ch_p "Слушай, ты бы очень хорошо выглядела с пирсинг-штангами."
                if "barbell" in YanaX.Todo:
                    ch_y "Я работаю над этим."
                else:
                    $ YanaX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(YanaX, 1150, TabM=0)
                    if ApprovalCheck(YanaX, 900, "L", TabM=0) or (Approval and YanaX.Love > 2 * YanaX.Obed):
                        ch_y "Думаешь, он меня украсит?"
                    elif ApprovalCheck(YanaX, 600, "I", TabM=0) or (Approval and YanaX.Inbt > YanaX.Obed):
                        ch_y "Я уже думала об этом. . ."
                    elif ApprovalCheck(YanaX, 500, "O", TabM=0) or Approval:
                        ch_y "Что ж, раз тебе такое нравится, [YanaX.Petname]. . ."
                    else:
                        $ YanaX.FaceChange("surprised")
                        $ YanaX.Brows = "angry"
                        ch_y "Мне это неинтересно, [YanaX.Petname]."
                        return #jump Yana_Clothes
                    show blackscreen onlayer black
                    "Она ненадолго исчезает в портале."
                    $ YanaX.Pierce = "barbell"
                    hide blackscreen onlayer black

#                    $ YanaX.Todo.append("barbell")

        "Сними пирсинг" if YanaX.Pierce:
                ch_p "Слушай, без пирсинга ты выглядишь лучше."
                $ YanaX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(YanaX, 1350, TabM=0)
                if ApprovalCheck(YanaX, 950, "L", TabM=0) or (Approval and YanaX.Love > YanaX.Obed):
                    ch_y "Ах, его было так сложно сделать. . ."
                elif ApprovalCheck(YanaX, 700, "I", TabM=0) or (Approval and YanaX.Inbt > YanaX.Obed):
                    ch_y "Что ж, а мне он нравится."
                    return
                elif ApprovalCheck(YanaX, 600, "O", TabM=0) or Approval:
                    ch_y "Ах. . ."
                else:
                    $ YanaX.FaceChange("surprised")
                    $ YanaX.Brows = "angry"
                    ch_y "Что ж, а мне он нравится."
                    return #jump Yana_Clothes
                show blackscreen onlayer black
                "Она ненадолго исчезает в портале."
                $ YanaX.Pierce = 0
                hide blackscreen onlayer black

#        "Headband" if YanaX.Hat != "headband" and "halloween" in YanaX.History:
#                ch_p "Why don't you wear that headband?"
#                ch_y "Oh, ok. . ."
#                $ YanaX.Hat = "headband"
#        "Glasses" if YanaX.Hat != "glasses" and "halloween" in YanaX.History:
#                ch_p "Why don't you wear those glasses?"
#                ch_y "Oh, ok. . ."
#                $ YanaX.Hat = "glasses"
        "Сними [get_clothing_name(YanaX.Hat_key, vin)]" if YanaX.Hat:
                ch_p "Думаю, тебе лучше [get_clothing_name(YanaX.Hat_key, vin)]."
                ch_y "Что ж, хорошо. . ."
                $ YanaX.Hat = 0

        "Надень черный чокер" if YanaX.Neck != "choker":
                ch_p "Почему бы тебе не надеть чокер?"
                ch_y "Что ж, хорошо. . ."
                $ YanaX.Neck = "choker"
#        "Green scarf" if YanaX.Neck != "scarf" and "halloween" in YanaX.History:
#                ch_p "Why don't you try on that green scarf?"
#                ch_y "Ладно. . ."
#                $ YanaX.Neck = "scarf"
        "Сними украшения с шеи" if YanaX.Neck:
                ch_p "Думаю, тебе стоит снять [get_clothing_name(YanaX.Neck_key, vin)]."
                ch_y "Что ж, хорошо. . ."
                $ YanaX.Neck = 0

        "О демонической форме. . ." if "master" in YanaX.Petnames:
                call Yana_Demon

        "Неважно":
            pass
    return #jump Yana_Clothes
    #End of Yana Misc Wardrobe

return
#End Yana Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
