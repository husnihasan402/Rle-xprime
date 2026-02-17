
# start YanaMeet//////////////////////////////////////////////////////////

#        if YanaX in ActiveGirls:
#                    if "switchcheck" in YanaX.Traits:
#                            pass
#                    elif "witch" not in YanaX.History and ApprovalCheck(YanaX, 1200) and YanaX.Loc == bg_current:
#                            #Shows off MCU costume
#                            call Yana_Witch
#                            return

#        elif "met" not in YanaX.History and "met" in BetsyX.History:
#                    elif bg_current != "bg classroom" and Time_Count == 1 and "Intro" not in Player.DailyActions:
#                            #You hadn't asked Yana yet
#                            call YanaMeet
#                            jump Misplaced

label YanaMeet:
        #set-up
        $ Situation = bg_current
        $ bg_current = "bg campus"
        $ YanaX.OutfitDay = "casual1"
        $ YanaX.Outfit = "casual1"
        $ YanaX.OutfitChange("casual1")
        call CleartheRoom("All",0,1)
        $ YanaX.Love = 300
        $ YanaX.Obed = 100
        $ YanaX.Inbt = 200
        $ YanaX.Petname = "бро"
        $ YanaX.Names = ["Illyana","Yana"]
        $ YanaX.Name = "? ? ?"
        call Shift_Focus(YanaX)
        $ YanaX.Loc = "hold"
        $ YanaX.SpriteLoc = StageCenter
        call Set_The_Scene
        if "Yana" not in GwenX.History:
                $ GwenX.History.append("Yana")

        #start
        $ HP = 25
        $ ImpHP = 25
        call Punch
        "Вы идете по своим делам, когда что-то небольшого размера бьет вас сзади."
        $ Line = 0
        while HP > 5 and ImpHP > 15: #breaks after hit 5 times or attack imp twice
            menu:
                "Ваши действия?"
                "Атаковать":
                        #attack twice to end the encounter
                        if ImpHP == 25:
                                $ YanaX.RecentActions.append("attack")
                        if ImpHP < 25:
                                "Вы снова бьете в ответ, ожидая на этот раз лучших результатов."
                        elif "arcana" in YanaX.RecentActions:
                                "Вы замахиваетесь на беса."
                        elif "look" in YanaX.RecentActions:
                                "Вы замахиваетесь на это существо."
                        else:
                                "Вы оборачиваетесь и видите какое-то маленькое существо, долго не думая, вы замахиваетесь на него."
                        $ ImpHP -= 5
                        "Похоже, тварь получила какой-то урон, но это ее не остановило."
                        if ImpHP < 20:
                                "Результаты примерно те же."
                "Бежать в укрытие":
                        if "hide" in YanaX.RecentActions:
                                "Прошлое укрытие вам никак не помогло! Вы пробуете укрыться за другим деревом."
                        else:
                                $ YanaX.RecentActions.append("hide")
                                "Вы бежите к ближайшему дереву и прячетесь за ним."
                        if "arcana" in YanaX.RecentActions:
                                "Бес следует за вами и продолжает наносить вам удары."
                        elif "look" in YanaX.RecentActions or ImpHP < 25:
                                "Это странного вида существо следует за вами и продолжает наносить вам удары."
                        else:
                                "Что-то продолжает цепляться за вашу спину, нанося вам удары."
                        "Укрытие вам не помогло."

                "Кинуть проверку на \"Восприятие\"":
                        $ D20 = renpy.random.randint(11, 19)
                        if "look" in YanaX.RecentActions:
                                "Выпадает [D20]: вы понимаете, что оно все еще здесь и все еще кромсает вас."
                        else:
                                $ YanaX.RecentActions.append("look")
                                "Вы оглядываетесь."
                                "Выпадает [D20]: вы замечаете маленькое красное существо с рогами, хвостом и крыльями, как у летучей мыши."
                                "Что важнее - у него маленькие когтистые лапы, и они сейчас царапают вам лицо."

                "Кинуть проверку на \"Мудрость\"" if "look" in YanaX.RecentActions or ImpHP < 25:
                        $ D20 = renpy.random.randint(11, 19)
                        if "arcana" in YanaX.RecentActions:
                                "Вы всматриваетесь пристальнее, в самую его суть."
                                "Выпадает [D20]: эта тварь все еще очень похожа на беса."
                                "И у вас нет никаких сомнений, что она все еще хочет вас исполосовать."
                        else:
                                $ YanaX.RecentActions.append("arcana")
                                "Вы изучаете существо."
                                "Выпадает [D20]: оно точно похоже на какого-то беса."
                                "Вы понимаете это в основном по острым когтям, которые летят вам в лицо."

                "Кинуть проверку на \"Живучесть\"" if "look" in YanaX.RecentActions or ImpHP < 25:
                        $ D20 = renpy.random.randint(11, 19)
                        if "survival" in YanaX.RecentActions:
                                "Вы пытаетесь устоять на ногах снова."
                                "На этот раз это сложнее."
                                "Выпадает [D20]: у вас снова получается."
                                "Рано или поздно этот метод перестанет быть эффективным."
                        else:
                                $ YanaX.RecentActions.append("survival")
                                "Вы пытаетесь устоять на ногах."
                                "Выпадает [D20]: у вас получается."
                        "Но по вам все равно прилетает удар."

                "Пропустить ход":
                        $ D20 = renpy.random.randint(11, 19)
                        if "wait" in YanaX.RecentActions:
                                "Вы уверены, что рано или поздно это прекратится."
                                "Выпадает [D20]: время идет."
                        else:
                                $ YanaX.RecentActions.append("wait")
                                "Вы решаете, что ваши страдания рано или поздно закончатся."
                                "Выпадает [D20]: проходит какое-то время."

                        if "arcana" in YanaX.RecentActions:
                                "Бес тем временем снова полосует вас когтями."
                        elif "look" in YanaX.RecentActions or ImpHP < 25:
                                "Странное создание тем временем снова полосует вас когтями."
                        elif HP < 25:
                                "Что-то определенно продолжает бить вас по спине."
                        else:
                                "И что-то снова бьет вас по спине."

            #outside menu
            $ HP -= 5
            call Punch
            "Вы получаете 5 единиц урона."
            if HP < 10:
                    "Наверное, вам стоит перестать получать урон."
                    "На улице темнеет, или вам только кажется?"

        #end while not Line:
        if HP <= 10:
                #if you took a lot of damage
                "Как раз когда вы задаетесь вопросом, верные ли сегодня вы приняли решения, сзади раздается треск."

        if "arcana" in YanaX.RecentActions:
                "Резкий взмах рассекает беса надвое - чисто и аккуратно."
        elif "look" in YanaX.RecentActions or ImpHP < 25:
                "Резкий взмах рассекает странное существо надвое - чисто и аккуратно."
        else:
                "Вы чувствуете резкий порыв ветра за спиной и слышите тошнотворный хруст."
                "Обернувшись, вы видите двух странных красных существ, у одного отсутствует верхняя часть туловища, у другого нет нижней части."
        "Из обеих частей хлещет кровь, они падают на землю, и вся эта мешанина втягивается в светящийся желтый диск."

        #Show Yana here
        "Как только вы перестаете пялиться на. . . \"это\", в поле зрения появляется юная девушка."
        $ YanaX.Loc = "bg campus"
        call Shift_Focus(YanaX)
        $ YanaX.FaceChange("angry",0,Eyes="side")
        $ YanaX.SpriteLoc = StageCenter

        $ YanaX.Sword = 1
        call Show_Yana

        if not Player.Male:
                "У нее в руках очень большой меч."
                "Вам хочется подумать, что вы видели и побольше, но, наверное, нет, не видели."
        else:
                "У нее в руках очень большой меч."
                "Вы пытаетесь не завидовать."
                "Ваш тоже вполне ничего."
        $ YanaX.FaceChange("confused",0)
        if not Player.Male:
            ch_y "Ты цела?"
        else:
            ch_y "Ты цел?"
        $ Count = 2
        while Count > 0:
            #loops once, unless you advance it
            menu:
                "Ваши действия?"
                "Ага, но спасибо!":
                        if HP <= 10:
                                #if you took a lot of damage
                                $ YanaX.Statup("Love", 90, 1)
                                $ YanaX.Statup("Obed", 200, 1)
                        $ YanaX.FaceChange("sly",1,Eyes="side")
                        $ YanaX.Statup("Love", 90, 2)
                        ch_y "О, эм. . . не за что."
                        $ YanaX.FaceChange("sly",1)
                        $ Count = 1

                "Да я бы и сама справилась." if not Player.Male:
                        if HP <= 10:
                                #if you took a lot of damage
                                $ YanaX.Statup("Love", 90, 1)
                                $ YanaX.Statup("Obed", 200, 1)
                        $ YanaX.FaceChange("sly",1)
                        $ YanaX.Statup("Love", 90, 1)
                        $ YanaX.Statup("Obed", 200, 1)
                        ch_y "Конечно справилась бы, но я рада помочь."
                        $ Count = 1

                "Да я бы и сам справился." if Player.Male:
                        if HP <= 10:
                                #if you took a lot of damage
                                $ YanaX.Statup("Love", 90, 1)
                                $ YanaX.Statup("Obed", 200, 1)
                        $ YanaX.FaceChange("sly",1)
                        $ YanaX.Statup("Love", 90, 1)
                        $ YanaX.Statup("Obed", 200, 1)
                        ch_y "Конечно справился бы, но я рада помочь."
                        $ Count = 1

                "Было близко.":
                        if HP <= 10:
                                #if you took a lot of damage
                                $ YanaX.Statup("Love", 90, 1)
                                $ YanaX.Statup("Obed", 200, 2)
                        $ YanaX.FaceChange("sly",1,Eyes="side")
                        $ YanaX.Statup("Love", 90, 1)
                        if not Player.Male:
                            ch_y "Уверена, ты бы и сама справилась, но я рада помочь."
                        else:
                            ch_y "Уверена, ты бы и сам справился, но я рада помочь."
                        $ Count = 1

                "Напасть" if Count == 2:
                        $ D20 = renpy.random.randint(3, 15)
                        "В ужасе вы бросаетесь на нее."
                        $ YanaX.Statup("Love", 90, -2)
                        $ YanaX.Statup("Inbt", 200, 2)
                        $ YanaX.FaceChange("surprised",2,Mouth="normal")
                        "Выпадает [D20]: она уклоняется от вашего выпада."
                        $ YanaX.FaceChange("confused",1,Mouth="normal")
                        ch_y "Воу, [YanaX.Petname], вдохни поглубже. Я тебя не трону."
                        ch_y "Я просто хотела узнать, в порядке ли ты."
                        $ YanaX.FaceChange("sly",0)

                "Бежать в укрытие" if Count == 2:
                        $ YanaX.Statup("Obed", 200, -2)
                        $ YanaX.Statup("Inbt", 200, 2)
                        $ YanaX.FaceChange("surprised",2)
                        if "hide" in YanaX.RecentActions:
                                "Вы продолжаете прятаться за деревом."
                        else:
                                $ YanaX.RecentActions.append("hide")
                                "Вы прячетесь за деревом."
                        $ YanaX.Statup("Love", 90, 1)
                        $ YanaX.FaceChange("confused",1)
                        ch_y "Воу, [YanaX.Petname], вдохни поглубже. Я тебя не трону."
                        $ YanaX.FaceChange("sly",0)
                        ch_y "Я просто хотела узнать, в порядке ли ты."

                "Кинуть проверку на \"Восприятие\"" if Count == 2:
                        $ D20 = renpy.random.randint(11, 19)
                        "Вы шесть секунд сверлите ее взглядом."
                        "Выпадает [D20]: вы отмечаете, что она довольно сексуальная, на вид ей лет семнадцать-девятнадцать."
                        $ YanaX.Statup("Inbt", 200, 1)
                        $ YanaX.FaceChange("confused",1)
                        ch_y "Эм, ты в порядке, [YanaX.Petname]?"

                "Кинуть проверку на \"Мудрость\"" if Count == 2:
                        $ D20 = renpy.random.randint(11, 19)
                        "Вы шесть секунд сверлите ее взглядом."
                        if "arcana" in YanaX.RecentActions:
                                "Выпадает [D20]: до вас доходит, что ее мечом, скорее всего, и прикончили беса."
                        elif "look" in YanaX.RecentActions:
                                "Выпадает [D20]: до вас доходит, что ее мечом, скорее всего, и прикончили то существо."
                        else:
                                "Выпадает [D20]: до вас доходит, что ее мечом, скорее всего, и прикончили тех непонятных существ."
                                "Хотя нет, вы вдруг понимаете, что существо-то было одно - просто разрубленное надвое."
                        $ YanaX.Statup("Inbt", 200, 1)
                        $ YanaX.FaceChange("confused",1)
                        ch_y "Эм, ты в порядке, [YanaX.Petname]?"

                "Кинуть проверку на \"Живучесть\"" if Count == 2:
                        $ D20 = renpy.random.randint(11, 19)
                        "Вы пытаетесь удержаться на ногах."
                        if "survival" in YanaX.RecentActions:
                                "Выпадает [D20]: выходит куда лучше, чем в прошлый раз - вы почти не тратите на это силы."
                        else:
                                "Выпадает [D20]: вроде бы работает - вы все еще на ногах."
                        $ YanaX.Statup("Inbt", 200, 1)
                        $ YanaX.FaceChange("confused",1)
                        ch_y "Эм, ты в порядке, [YanaX.Petname]?"

                ". . . [[пропустить ход]" if Count == 2:
                        $ D20 = renpy.random.randint(11, 19)
                        "Выпадает [D20]: проходит какое-то время."
                        $ YanaX.Statup("Inbt", 200, 1)
                        $ YanaX.FaceChange("confused",1)
                        ch_y "Эм, ты в порядке, [YanaX.Petname]?"

                ". . . [[пропустить ход]" if Count != 2:
                        $ D20 = renpy.random.randint(11, 19)
                        "Выпадает [D20]: время идет."
                        $ YanaX.Statup("Love", 90, 2)
                        $ YanaX.Statup("Obed", 200, 1)
                        $ YanaX.Statup("Inbt", 200, 1)
                        $ YanaX.FaceChange("confused",2)
                        ch_y "Пожалуй, ты немного в шоке. . ."
            #end menu:
            $ Count -= 1
        #end while Count > 0:
        $ YanaX.Statup("Obed", 200, 1)
        $ YanaX.Statup("Inbt", 200, 1)
        $ YanaX.FaceChange("sadside",2,Eyes="leftside")
        ch_y "Я должна извиниться за произошедшее."
        $ YanaX.FaceChange("sly",1)
        ch_y "Этот мелкий бес из Лимба один из моих."
        ch_y "Он ускользнул от меня, а я поздно спохватилась."
        if HP <= 5:
                #if you took a lot of damage
                $ YanaX.Statup("Love", 90, 2)
                $ YanaX.Statup("Obed", 200, 1)
                $ YanaX.FaceChange("sly",1,Brows="surprised")
                if not Player.Male:
                    ch_y "-Поразительно-, что ты вообще жива. . ."
                else:
                    ch_y "-Поразительно-, что ты вообще жив. . ."
        elif HP <= 10:
                #if you took a lot of damage
                $ YanaX.Statup("Love", 90, 1)
                $ YanaX.Statup("Obed", 200, 1)
                $ YanaX.FaceChange("sly",1)
                ch_y "Он тебя знатно потрепал. . ."
        else:
                $ YanaX.Statup("Obed", 200, 5)
                $ YanaX.FaceChange("sly",1)
                if not Player.Male:
                    ch_y "Ты отлично держалась!"
                else:
                    ch_y "Ты отлично держался!"
                ch_y "Но все-таки он тебя задел. . ."
        ch_y "-за это я прошу прощения."
        menu:
            extend ""
            "Да ничего страшного.":
                    $ YanaX.Statup("Love", 90, 3)
                    $ YanaX.FaceChange("smile",1)
                    ch_y "Мило, что ты так считаешь."
            "Ты вообще кто?":
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 1)
            "Бывает.":
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Inbt", 200, 2)
                    $ YanaX.FaceChange("smile",1)
                    ch_y "Наверное, в этих \"краях твари из бездны\" - не такая уж редкость."
            "Будешь должна.":
                    $ YanaX.Statup("Obed", 200, 4)
                    $ YanaX.FaceChange("surprised",2,Brows="sad",Mouth="smile")
                    ch_y "Конечно. Как я уже сказала, мне очень жаль, я все исправлю."
            "Точно, это все твоя вина!":
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 200, 3)
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("surprised",2,Brows="angry")
                    ch_y "Конечно! Я так и сказала!"
                    $ YanaX.FaceChange("sadside",1)
                    ch_y "Мне очень жаль, я все исправлю."
            "Почему ты зовешь меня \"бро?\"" if not Player.Male:
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 200, 3)
                    $ YanaX.Statup("Inbt", 200, -1)
                    $ YanaX.FaceChange("surprised",2)
                    ch_y "Что?"
                    ch_y "Ты \"бро\"."
                    $ YanaX.FaceChange("confused",1,Eyes="side")
                    ch_y "Он \"бро,\""
                    $ YanaX.FaceChange("confused",1,Eyes="leftside")
                    ch_y "-она \"бро,\""
                    $ YanaX.FaceChange("confused",1)
                    ch_y "-мы все \"бро,\" бро."
            ". . .":
                    $ YanaX.FaceChange("sadside",1)
                    ch_y "Еще раз, мне очень жаль."
                    $ YanaX.FaceChange("sly",0)

        $ YanaX.FaceChange("sly",0,Mouth="open")
        ch_y "Ах! Я, наверное, должна представиться!"
        ch_y "Меня зовут Ульяна Распутина."
        $ YanaX.Name = "Ульяна"
        $ YanaX.Name_rod = "Ульяны"
        $ YanaX.Name_dat = "Ульяне"
        $ YanaX.Name_vin = "Ульяну"
        $ YanaX.Name_tvo = "Ульяной"
        $ YanaX.Name_pre = "Ульяне"
        $ YanaX.Pet = "Ульяна"
        $ YanaX.Pet_rod = "Ульяны"
        $ YanaX.Pet_dat = "Ульяне"
        $ YanaX.Pet_vin = "Ульяну"
        $ YanaX.Pet_tvo = "Ульяной"
        $ YanaX.Pet_pre = "Ульяне"
        menu:
            extend ""
            "Приятно познакомиться, меня зовут [Player.Name].":
                    $ YanaX.Petname = Player.Name
                    $ YanaX.Petname_rod = Player.Name_rod
                    $ YanaX.Petname_dat = Player.Name_dat
                    $ YanaX.Petname_vin = Player.Name_vin
                    $ YanaX.Petname_tvo = Player.Name_tvo
                    $ YanaX.Petname_pre = Player.Name_pre
                    $ YanaX.Statup("Love", 90, 3)
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("smile",1)
            "Приятно познакомиться.":
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("smile",1)
            "Понятно.":
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("smile",1)
            ". . .":
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("confused",1)

        if YanaX.Petname != Player.Name:
                #if she doesn't know your name yet. . .
                ch_y "А тебя как звать? . ."
                menu:
                    extend ""
                    "[Player.Name], извини, надо было сразу представиться.":
                            $ YanaX.Petname = Player.Name
                            $ YanaX.Petname_rod = Player.Name_rod
                            $ YanaX.Petname_dat = Player.Name_dat
                            $ YanaX.Petname_vin = Player.Name_vin
                            $ YanaX.Petname_tvo = Player.Name_tvo
                            $ YanaX.Petname_pre = Player.Name_pre
                            $ YanaX.Statup("Love", 90, 3)
                            $ YanaX.FaceChange("smile",1)
                            ch_y "Все нормально."
                    "[Player.Name].":
                            $ YanaX.Petname = Player.Name
                            $ YanaX.Petname_rod = Player.Name_rod
                            $ YanaX.Petname_dat = Player.Name_dat
                            $ YanaX.Petname_vin = Player.Name_vin
                            $ YanaX.Petname_tvo = Player.Name_tvo
                            $ YanaX.Petname_pre = Player.Name_pre
                            $ YanaX.Statup("Love", 90, 2)
                            $ YanaX.Statup("Obed", 200, 1)
                            $ YanaX.FaceChange("smile",1)

                    "Я пока не готова раскрывать эту информацию." if not Player.Male:
                            $ YanaX.Statup("Obed", 200, 2)
                            $ YanaX.Statup("Inbt", 200, 1)
                            $ YanaX.FaceChange("sly",1,Brows="angry")

                    "Я пока не готов раскрывать эту информацию." if Player.Male:
                            $ YanaX.Statup("Obed", 200, 2)
                            $ YanaX.Statup("Inbt", 200, 1)
                            $ YanaX.FaceChange("sly",1,Brows="angry")

                    ". . .":
                            $ YanaX.Statup("Obed", 200, 2)
                            $ YanaX.Statup("Inbt", 200, 1)
                            $ YanaX.FaceChange("confused",1)

        if YanaX.Petname == Player.Name:
                ch_y "Что ж, приятно познакомиться, [Player.Name]."

        "Слышен топот - кто-то быстро приближается к вам."

        $ KittyX.Loc = "bg campus"
        $ KittyX.SpriteLoc = StageRight

        show Kitty_Sprite at Sprite_Set(1200)
        show Kitty_Sprite at SpriteLoc(StageRight) with easeinright

        $ KittyX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_k "Ульяна! Ты нашла бе-"
        $ KittyX.FaceChange("perplexed",2)
        $ YanaX.FaceChange("smile",1,Eyes="leftside")
        ch_k "-зобразное существо, которое мы вроде как искали в той мобильной игре?"
        $ KittyX.FaceChange("smile",2)
        $ YanaX.FaceChange("smile",1)
        if not Player.Male:
            ch_k "О, привет, [Player.Name]. Ты, как я вижу, уже столкнулась с Ульяной."
        else:
            ch_k "О, привет, [Player.Name]. Ты, как я вижу, уже столкнулся с Ульяной."
        $ KittyX.FaceChange("smile",1)

        if YanaX.Petname != Player.Name:
                $ YanaX.Petname = Player.Name
                $ YanaX.Petname_rod = Player.Name_rod
                $ YanaX.Petname_dat = Player.Name_dat
                $ YanaX.Petname_vin = Player.Name_vin
                $ YanaX.Petname_tvo = Player.Name_tvo
                $ YanaX.Petname_pre = Player.Name_pre
                $ YanaX.FaceChange("sly",1)
                if not Player.Male:
                    ch_y "Да, она как раз собиралась представиться."
                else:
                    ch_y "Да, он как раз собирался представиться."
                ch_y "Значит, тебя зовут \"[Player.Name]\", да?"
        else:
                $ YanaX.FaceChange("smile",1)
                ch_y "Да, мы уже познакомились."
        $ YanaX.Petname = "бро"
        $ YanaX.Petname_rod = "бро"
        $ YanaX.Petname_dat = "бро"
        $ YanaX.Petname_vin = "бро"
        $ YanaX.Petname_tvo = "бро"
        $ YanaX.Petname_pre = "бро"
        if not Player.Male:
            ch_y "В общем, она знает про беса."
        else:
            ch_y "В общем, он знает про беса."
        if ImpHP <= 15:
                $ YanaX.Statup("Love", 90, 1)
                $ YanaX.Statup("Obed", 200, 2)
                $ YanaX.FaceChange("sly",1)
                if not Player.Male:
                    ch_y "У нее получилось даже неплохо держаться против него."
                else:
                    ch_y "У него получилось даже неплохо держаться против него."
        menu:
            extend ""
            "Она как раз собиралась рассказать мне о том, что произошло.":
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 3)
                    $ YanaX.FaceChange("sly",1)
                    ch_y "Справедливо."
            "Ага.":
                    $ YanaX.Statup("Love", 50, 1)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 2)
                    $ YanaX.FaceChange("smile",1)
                    ch_y "Да, что ж. . ."
                    ch_y "Позволь мне объясниться."
            "Это было ужасно!":
                if HP > 10:
                    #if you weren't that hurt
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 200, -2)
                    $ YanaX.Statup("Inbt", 200, 3)
                    $ YanaX.FaceChange("angry",2)
                    ch_y "Ох, ну не плачь."
                else:
                    #if you were very hurt
                    $ KittyX.Statup("Love", 90, 3)
                    $ KittyX.FaceChange("surprised",1,Brows="sad")
                    ch_k "Ни фига себе, ты выглядишь очень плохо."
                    $ KittyX.FaceChange("normal",1)
                    $ YanaX.Statup("Love", 90, 4)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, -1)
                    $ YanaX.FaceChange("confused",2)
                    ch_y "Я же извинилась, нет?"
                $ YanaX.FaceChange("angry",1,Eyes="side")
                ch_y "Надо бы объяснить, что произошло."
                $ YanaX.FaceChange("normal",0)
            ". . .":
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("confused",1)
                    ch_y "Да, что ж. . ."
                    $ YanaX.FaceChange("normal",0)
                    ch_y "Позволь мне объясниться."

        ch_y "Желаешь узнать что-то конкретное?"
        $ Count = 3
        while Count > 0:
            #loops once, unless you advance it
            menu:
                extend ""
                "Ты мутант?" if "powers" not in YanaX.RecentActions:
                        ch_y "Да, но все не так просто. . ."
                        call Yana_Scene_Powers

                "Что это был за бес?" if "limbo" not in YanaX.RecentActions:
                        call Yana_Scene_Limbo

                "Что у тебя за меч?" if "sword" not in YanaX.RecentActions:
                        $ YanaX.RecentActions.append("sword")
                        $ YanaX.Sword = 0
                        $ YanaX.FaceChange("sly",1)
                        "Меч исчезает во вспышке света."
                        ch_y "Мне -очень- сложно о нем рассказывать."
                        menu:
                            extend ""
                            "Ладно.":
                                    $ YanaX.Statup("Love", 90, 2)
                                    $ YanaX.Statup("Obed", 200, -1)
                                    $ YanaX.Statup("Inbt", 200, 1)
                                    $ YanaX.FaceChange("smile",1)

                            "Теперь мне еще интересней о нем узнать!":
                                    $ YanaX.Statup("Love", 90, 1)
                                    $ YanaX.Statup("Obed", 200, 2)
                                    $ YanaX.FaceChange("sly",1)

                            ". . .":
                                    $ YanaX.Statup("Obed", 200, 1)
                                    $ YanaX.Statup("Inbt", 200, 1)
                                    $ YanaX.FaceChange("smile",1)

                "Хорошо, вот теперь точно \"приятно познакомиться\"." if "limbo" in YanaX.RecentActions or "powers" in YanaX.RecentActions:
                        #if you asked at least one question.
                        $ YanaX.Statup("Love", 90, 3)
                        $ YanaX.Statup("Obed", 200, 1)
                        $ YanaX.FaceChange("smile",1)
                        ch_y "Да, согласна."
                        $ Count = 1

                ". . .":
                        $ YanaX.Statup("Love", 90, -2)
                        $ YanaX.Statup("Obed", 200, 1)
                        $ YanaX.FaceChange("confused",2)
                        if "limbo" not in YanaX.RecentActions and "powers" not in YanaX.RecentActions and "sword" not in YanaX.RecentActions:
                            ch_y "Тебе совсем ничего неинтересно?"
                        else:
                            ch_y "Тебе больше ничего неинтересно?"
                        $ YanaX.FaceChange("sly",1)
                        $ Count = 1
            #end menu:
            $ Count -= 1

        if "limbo" not in YanaX.RecentActions:
                $ KittyX.FaceChange("smile",1,Eyes="side")
                $ YanaX.FaceChange("sly",1,Eyes="leftside")
                if not Player.Male:
                    ch_k "Ты должна хотя бы рассказать ей о том, как этот бес сюда попал."
                else:
                    ch_k "Ты должна хотя бы рассказать ему о том, как этот бес сюда попал."
                $ KittyX.FaceChange("smile",1)
                $ YanaX.FaceChange("sly",1)
                ch_y "Да."
                call Yana_Scene_Limbo
        elif "powers" not in YanaX.RecentActions:
                $ KittyX.FaceChange("smile",1,Eyes="side")
                $ YanaX.FaceChange("sly",1,Eyes="leftside")
                if not Player.Male:
                    ch_k "Расскажи ей о том, как работают твои силы."
                else:
                    ch_k "Расскажи ему о том, как работают твои силы."
                $ KittyX.FaceChange("smile",1)
                $ YanaX.FaceChange("sly",1)
                call Yana_Scene_Powers
        if "zero" not in YanaX.RecentActions:
                ch_y "А -ты- почему здесь, бро?"
                menu:
                    extend ""
                    "Я могу отключать способности мутантов.":
                            $ YanaX.Statup("Love", 200, 1)
                            $ YanaX.Statup("Obed", 200, 1)
                    "У меня ловкий язычок.":
                            $ YanaX.Statup("Obed", 200, 1)
                            $ YanaX.Statup("Inbt", 200, 2)
                            if KittyX.LickP:
                                    $ KittyX.FaceChange("surprised",2)
                                    $ KittyX.Statup("Love", 90, 1)
                                    $ KittyX.Statup("Obed", 90, 2)
                                    ch_k "[KittyX.Petname]!!!"
                                    $ KittyX.FaceChange("sexy",1)
                                    $ YanaX.Statup("Inbt", 200, 1)
                                    ch_k "Потише!"
                            else:
                                    $ KittyX.FaceChange("surprised",1)
                                    ch_k "[KittyX.Petname]!!!"
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            $ YanaX.FaceChange("confused",1,Eyes="leftside")
                            ch_k "Да ну тебя, [KittyX.Petname] умеет отключать способности мутантов!"
                    ". . .":
                            $ KittyX.FaceChange("sly",1,Eyes="side")
                            $ YanaX.FaceChange("confused",1,Eyes="leftside")
                            ch_k "Да ну тебя, [KittyX.Petname] умеет отключать способности мутантов!"
                call Yana_Scene_Zero_Powers
        #end while Count > 0:

        ch_y "В общем, рада, что смогла исправить положение. . ."
        $ KittyX.FaceChange("smile",1,Eyes="side")
        $ YanaX.FaceChange("smile",1,Eyes="leftside")
        ch_k "Как же круто, что ты снова здесь, Ульяна!"
        ch_k "Кажется, что я не видела тебя здесь уже целую вечность."
        $ YanaX.FaceChange("sly",1,Eyes="side")
        ch_y "Да, в последнее время я была немного. . . занята."
        $ YanaX.FaceChange("smile",1,Eyes="leftside")
        ch_y "Но я тоже рада тебя видеть."
        $ YanaX.FaceChange("smile",2,Eyes="leftside")
        ch_y "Очень рада."
        $ YanaX.FaceChange("smile",1,Eyes="leftside")
        ch_k "О, мне не терпится рассказать тебе о том, что здесь происходило!"
        if KittyX.SEXP >= 15:
                $ KittyX.Statup("Love", 90, 3)
                $ KittyX.Statup("Obed", 90, 2)
                $ KittyX.Statup("Lust", 60, 2)
                $ KittyX.FaceChange("smile",2,Eyes="side")
                $ YanaX.FaceChange("surprised",2,Eyes="leftside")
                ch_k "Мы с [KittyX.Petname_tvo] очень. . . сблизились."
                $ YanaX.Statup("Love", 90, -1)
                $ YanaX.Statup("Obed", 200, 3)
                $ YanaX.Statup("Lust", 60, 5)
        else:
                $ KittyX.Statup("Obed", 70, 1)
                $ KittyX.Statup("Inbt", 70, 5)
                $ KittyX.Statup("Lust", 60, 2)
                $ KittyX.FaceChange("smile",2)
                $ YanaX.FaceChange("surprised",2,Eyes="leftside")
                if not Player.Male:
                    ch_k "Эм, [KittyX.Petname] хорошо зарекомендовала себя в институте. . ."
                else:
                    ch_k "Эм, [KittyX.Petname] хорошо зарекомендовал себя в институте. . ."
                $ YanaX.Statup("Obed", 200, 3)
                $ YanaX.Statup("Inbt", 200, 2)
                $ YanaX.Statup("Lust", 60, 3)
        $ KittyX.FaceChange("smile",2)
        $ YanaX.FaceChange("sly",1)
        ch_y "Ох, вот как. . ."
        ch_y "Хммм. . ."
        $ KittyX.FaceChange("smile",1,Eyes="side")
        $ YanaX.FaceChange("smile",1,Eyes="leftside")
        ch_y "Хорошо, мне нужно кое-что уладить, увидимся на занятиях."
        ch_y "До встречи."
        call Hide_Yana
        "Ильяна исчезает в появившемся портале."
        hide Kitty_Sprite with easeoutright
        "А [KittyX.Name] уходит по своим делам."
        $ KittyX.FaceChange("smile",1)
        $ YanaX.FaceChange("smile",1)
        "Вы остаетесь один, вам остается лишь продолжить свой путь."
        $ YanaX.AddWord(1,0,0,0,"met") #adds "word" tag to History
        $ ActiveGirls.append(YanaX) if YanaX not in ActiveGirls else ActiveGirls
        $ bg_current = Situation
        $ YanaX.Sword = 0
        jump Misplaced
# end Yana intro main sequence, returns to original location


label Yana_Scene_Powers:
        #called when you ask about her powers
        $ YanaX.RecentActions.append("powers")
        $ YanaX.FaceChange("smile",1)
        # "Are you a mutant?"
        #ch_y "I am, but it is complicated. . ."
        $ YanaX.FaceChange("sly",1)
        ch_y "У меня есть способности мутанта, но не только они."
        ch_y "Я могу создавать ступенчатые диски, которые позволяют мне телепортировать себя и других через время и пространство."
        if "limbo" in YanaX.RecentActions:
                    ch_y "Каждый раз, когда я открываю портал, я прохожу через Лимбо - так я туда впервые и попала."
        menu:
            extend ""
            "А я могу отключать способности.":
                    $ YanaX.Statup("Love", 200, 1)
                    $ YanaX.Statup("Obed", 200, 1)
                    call Yana_Scene_Zero_Powers
            "Это не объясняет появление беса." if "limbo" not in YanaX.RecentActions:
                    $ YanaX.Statup("Love", 200, 1)
                    $ YanaX.FaceChange("sly",1,Eyes="side")
                    ch_y "Объясняет. . . в некотором смысле. . ."
                    call Yana_Scene_Limbo
                    $ Count -= 1 if Count else 0
                    ch_y "Каждый раз, когда я открываю портал, я прохожу через Лимбо."
            "Хм.":
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.FaceChange("normal")
            ". . .":
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("confused")
        return

label Yana_Scene_Limbo:
        #called when you ask about limbo
        $ YanaX.RecentActions.append("limbo")
        $ YanaX.FaceChange("sadside",1)
        # "What about that imp?"
        ch_y "Бес пришел из Лимбо. Это часть Преисподней."
        $ YanaX.FaceChange("angry",1,Eyes="side")
        ch_y "Из-за кое-каких. . . обстоятельств, в которые я сейчас вдаваться не буду. . ."
        $ YanaX.FaceChange("sly",1)
        ch_y "Сейчас я - правительница Лимбо, и все его приспешники подчиняются мне."
        $ YanaX.FaceChange("angry",1,Eyes="side")
        ch_y "Или должны, по крайней мере."
        ch_y "Боюсь, иногда кто-то из них \"срывается с цепи.\""
        $ YanaX.FaceChange("sly",1)
        menu:
            extend ""
            "Ничего себе!":
                    $ YanaX.FaceChange("sly")
                    ch_y "Не скажу, что это был -приятный- опыт, но у него есть свои плюсы."
            "Так ты не мутант?" if "powers" not in YanaX.RecentActions:
                    $ YanaX.Statup("Love", 200, 1)
                    ch_y "Мутант, но все довольно сложно. . ."
                    call Yana_Scene_Powers
                    $ Count -= 1 if Count else 0
            "Хм.":
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.FaceChange("normal")
            ". . .":
                    $ YanaX.Statup("Inbt", 200, 1)
                    $ YanaX.FaceChange("confused")
        if Count < 1 and "powers" not in YanaX.RecentActions:
                    #if this is outside of the questions loop
                    $ KittyX.FaceChange("smile",1,Eyes="side")
                    ch_k "-Иииии- она тоже мутант!"
                    $ KittyX.FaceChange("smile",1)
                    call Yana_Scene_Powers
        return

label Yana_Scene_Zero_Powers:
        #called when you tell her about your powers or Rogue does
        $ YanaX.RecentActions.append("zero")
        $ YanaX.FaceChange("surprised",1)
        ch_y "О? Правда?"
        $ YanaX.FaceChange("smile",1)
        ch_y "Очень полезная способность. . ."
        ch_y "Можешь попробовать на мне?"
        menu:
            extend ""
            "Конечно.":
                    $ YanaX.Statup("Love", 200, 3)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.FaceChange("smile",1)
                    "Вы протягиваете руку и берете ее за ладонь."
                    $ YanaX.Addictionrate += 2
                    $ YanaX.Statup("Lust", 90, 5)
                    ch_y "Оох, -интересные- ощущения. . ."
                    ch_y "А теперь я попробую вернуться в свою комнату. . ."
                    $ YanaX.FaceChange("surprised",2)
                    ch_y ". . ."
                    $ YanaX.FaceChange("normal",1)
                    ch_y "Хм, ничего."
            "Нет, спасибо.":
                    $ YanaX.Statup("Love", 200, -3)
                    $ YanaX.Statup("Inbt", 200, 2)
                    $ YanaX.FaceChange("sly",1)
                    ch_y "Хммм. . ."
                    "Над вашей головой возникает светящийся портал и опускается вниз, как лезвие гильотины."
                    call Punch
                    "Но ваши способности активны: портал гаснет в момент касания."
                    $ YanaX.FaceChange("surprised",2)
#                    $ YanaX.Addictionrate += 2
#                    $ YanaX.Statup("Lust", 90, 5)
                    $ YanaX.Statup("Obed", 200, 4)
                    "И в итоге портал окончательно исчезает."
                    $ YanaX.FaceChange("sly",1)
                    ch_y "Ооох, как -интересно-. . ."
        $ YanaX.FaceChange("smile",1)
        ch_y "Какая оригинальная сила."
        return

#end Yana Meet content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Yana_Key:
        call Shift_Focus(YanaX)
        $ YanaX.Loc = bg_current
        call Set_The_Scene
        $ YanaX.FaceChange("bemused")
        $ Event_Queue = [0,0]
        ch_y "Эй, я обычно не пользуюсь дверью, поэтому она почти всегда заперта. . ."
        ch_y "-вот. . ."
        "Она вручает вам ключ с маленьким брелоком в виде меча."
        $ Keys.append(YanaX) if YanaX not in Keys else Keys
        $ YanaX.Event[0] = 1
        ch_p "Спасибо."
        return

#Start Yana demon horns content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Yana_Horny:
        #scene for when Yana looks like a demon, discusses demonic look
#        if "horny" not in YanaX.History:
#                call Yana_Horny
        #called from Addiction first fix

        $ YanaX.AddWord(1,0,0,0,"horny") #history
        $ YanaX.Demon = 1
        call Shift_Focus(YanaX)

        ch_y "Сегодня я чувствую себя немного необычно."
        menu:
            extend ""
            "У тебя тут рожки выросли.":
                    $ YanaX.FaceChange("confused",1,Eyes="stunned")
                    $ YanaX.Statup("Love", 70, 1)
            "У тебя. . . [[показать на ее рога]":
                    $ YanaX.FaceChange("confused",1,Eyes="stunned")
                    $ YanaX.Statup("Love", 80, 1)
            "Да ты вся на рогах.":
                    $ YanaX.AddWord(1,"horny") #recent
                    $ YanaX.Statup("Obed", 70, 2)
                    if ApprovalCheck(YanaX, 30, "I") and YanaX.Lust > 40:
                            $ YanaX.FaceChange("sly",2)
                            $ YanaX.Statup("Inbt", 50, 2)
                            ch_y "Да, немного, но я не думаю, что дело в этом."
                    else:
                            $ YanaX.FaceChange("surprised",2)
                            $ YanaX.Statup("Love", 60, -1)
                            $ YanaX.Statup("Inbt", 50, 1)
                            ch_y "Я не-"
                    "Вы невольно смотрите чуть выше ее линии глаз."
                    $ YanaX.FaceChange("confused",1,Eyes="stunned")
            "Да?":
                    $ YanaX.FaceChange("perplexed",1)
                    "Вы невольно смотрите чуть выше ее линии глаз."
                    $ YanaX.FaceChange("confused",1,Eyes="stunned")
            ". . .":
                    "Вы невольно смотрите чуть выше ее линии глаз."
                    $ YanaX.FaceChange("confused",1,Eyes="stunned")
        ch_y "Что?"
        $ YanaX.FaceChange("angry",2,Eyes="stunned")
        ch_y "Ох, они снова вылезли."
        $ YanaX.FaceChange("sly",1,Brows="angry")
        menu:
            extend ""
            "А что с ними?":
                    pass
            "У тебя уже такое бывало?":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 80, 1)
                    $ YanaX.Statup("Inbt", 80, 1)
                    ch_y "К сожалению, да. . ."
            "А они сексуальные.":
                    $ YanaX.AddWord(1,"hot") #recent
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Statup("Love", 80, 1)
                    $ YanaX.Statup("Obed", 80, 1)
                    $ YanaX.Statup("Inbt", 50, 1)
                    ch_y "Спасибо?"
            ". . .":
                    pass
        ch_y "У меня. . . это бывает время от времени."
        menu:
            extend ""
            "Почему?":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 70, 1)
            "Это потому что ты на рогах?":
                    if ApprovalCheck(YanaX, 30, "I") and YanaX.Lust > 40:
                            $ YanaX.FaceChange("sly",1)
                            $ YanaX.Statup("Love", 90, 1)
                            $ YanaX.Statup("Inbt", 70, 2)
                            ch_y "Вернемся к этому позже!"
                    elif "horny" not in YanaX.RecentActions:
                            $ YanaX.Statup("Obed", 60, 1)
                            $ YanaX.Statup("Inbt", 80, 2)
                            ch_y "Да-да, хорошая шутка."
                            ch_y "А теперь заткнись."
                    else:
                            $ YanaX.FaceChange("angry",2)
                            $ YanaX.Statup("Love", 70, -2)
                            $ YanaX.Statup("Obed", 80, 2)
                            ch_y "Не поэтому!"
                    $ YanaX.AddWord(1,"horny") #recent
            "А они сексуальные." if "hot" not in YanaX.RecentActions:
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Statup("Love", 70, 1)
                    $ YanaX.Statup("Obed", 50, 2)
                    $ YanaX.Statup("Inbt", 40, 1)
                    $ YanaX.Statup("Inbt", 60, 2)
                    ch_y "Спасибо?"
            ". . .":
                    pass
        $ YanaX.FaceChange("sly",1,Eyes="side",Brows="angry")
        ch_y "Это. . . нечто демоническое."
        ch_y "Связано с моих пребыванием в Лимбо."
        $ YanaX.FaceChange("sly",1,Eyes="stunned")
        ch_y "По. . . разным причинам я могу принимать демонический облик. . ."
        $ YanaX.FaceChange("sly",1)
        ch_y "-и демонический образ мышления тоже. . ."
        menu:
            extend ""
            "И как тебе это?":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 70, 1)
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Inbt", 60, 2)
            "Ничего себе!":
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 60, 1)
                    $ YanaX.Statup("Inbt", 80, 2)
                    ch_y "Я рада, что -ты- так думаешь. . ."
            "Хм.":
                    $ YanaX.FaceChange("confused",1)
                    $ YanaX.Statup("Love", 60, -1)
                    $ YanaX.Statup("Obed", 60, 1)
                    ch_y "Да. . ."
            ". . .":
                    $ YanaX.FaceChange("confused",1)
                    $ YanaX.Statup("Love", 60, -1)
                    $ YanaX.Statup("Obed", 60, 1)
        ch_y "Меня это не -сильно- напрягает. . ."
        ch_y "Но я стараюсь держать это состояние под контролем."
        return

#end Yana demon horns content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Yana limbo2 content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Yana_Limbo2:
        # How did Illyana end up in Limbo?
        # if "limbo2" not in YanaX.History: call Yana_Limbo2
        $ YanaX.AddWord(1,0,0,0,"limbo2") #recent and history
        $ YanaX.FaceChange("sadside",1)
        ch_y "Когда мои силы только пробудились, я даже это не поняла."
        ch_y "Я просто проснулась в аду."
        ch_y "Тогда я была ребенком. Я понятия не имела, где я и как сюда попала."
        ch_y "Это был край огня и вулканических скал, освещенный лишь магмой и магической энергией."
        ch_y "Время там течет иначе - для меня могли пройти годы, а здесь - лишь мгновения."
        $ YanaX.FaceChange("sadside",1,Mouth="smirk")
        ch_y "Там были души друзей моего брата, некоторые помогали мне, растили и заботились обо мне. . ."
        $ YanaX.FaceChange("sadside",1,Brows="angry")
        ch_y "-но другие меня мучили."
        ch_y "И меня постоянно окружали бесы и демоны - они улюлюкали, угрожали, но редко причиняли вред."
        $ YanaX.FaceChange("sadside",1)
        ch_y "Я прожила там много лет. . . долгих лет. . ."
        ch_y "Из ребенка превратилась в девушку."
        ch_y "Только когда я полностью овладела своими силами, я смогла обуздать их настолько, чтобы вернуться домой."
        return

label Yana_Belasco:
        #on Belasco
        # if "belasco" not in YanaX.History: call Yana_Belasco
        $ YanaX.AddWord(1,0,0,0,"belasco") #recent and history
        $ YanaX.FaceChange("sly",1,Brows="angry")
        ch_y "Пока я была заперта в Лимбо, меня часто навещал демон по имени \"Беласко.\""
        ch_y "Он хотел использовать мою невинность для создания камней душ."
        ch_y "С их помощью он мог творить могущественную магию."
        $ YanaX.FaceChange("sadside",2,Brows="angry")
        ch_y "Когда я подросла, он попытался склонить меня на темную сторону."
        $ YanaX.FaceChange("sadside",1)
        ch_y "Он поведал мне трагедию Гарта Пламбуса Мудрого. . . и не только."
        ch_y "Со временем я стала еще сильнее и смогла перековать те камни душ."
        $ YanaX.FaceChange("sly",1,Eyes="leftside")
        $ YanaX.Sword = 1
        ch_y "Я выковала из них этот меч."
        $ YanaX.FaceChange("sly",1)
        ch_y "С ним я смогла вырвать свою свободу из лап Беласко."
        $ YanaX.Sword = 0
        return

label Yana_Sword:
        #on the sword
        # if "sword" not in YanaX.History: call Yana_Sword
        $ YanaX.AddWord(1,0,0,0,"sword") #recent and history
        $ YanaX.FaceChange("sly",1,Eyes="leftside")
        $ YanaX.Sword = 1
        ch_y "Этот меч - часть меня, выкованный из моей души."
        ch_y "Он обладает огромной магической силой, способен рассекать колдовство и демонических созданий."
        ch_y "Но им нельзя ранить живых."
        $ YanaX.FaceChange("sly",1)
        ch_y "По крайней мере, не слишком сильно."
        return

label Yana_Snowflake:
        # if "Snowflake" not in YanaX.Pets: call Yana_Snowflake
#        $ YanaX.AddWord(1,0,0,0,"snowflake") #recent and history
        $ YanaX.FaceChange("sadside",2,Mouth="smirk")
        ch_y "Когда я была маленькой, брат звал меня \"Снежинкой.\""
        if not Player.Male:
            ch_y "Я была бы не против, если бы и ты тоже так меня звала. . ."
        else:
            ch_y "Я была бы не против, если бы и ты тоже так меня звал. . ."
        menu:
            "Начать звать ее так?"
            "Ладно, Снежинка. [[да]":
                    $ YanaX.Statup("Love", 200, 6)
                    $ YanaX.Pet = "Снежинка"
                    $ YanaX.Pet_rod = "Снежинки"
                    $ YanaX.Pet_dat = "Снежинке"
                    $ YanaX.Pet_vin = "Снежинку"
                    $ YanaX.Pet_tvo = "Снежинкой"
                    $ YanaX.Pet_pre = "Снежинке"
            ". . . [[Нет]":
                    pass
        $ YanaX.FaceChange("sly",1)
        $ YanaX.Pets.append("Snowflake")
        return

#end Yana limbo2 content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Yana_BF(BO=[]):
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(YanaX,"bemused","краснеет. . .")
                return
        call Set_The_Scene
        if YanaX.Loc != bg_current:
            if YanaX not in Party:
                "[YanaX.Name] подходит к вам и показывает жестом, что хочет поговорить с вами наедине."
            else:
                "[YanaX.Name] поворачивается к вам и показывает жестом, что хочет поговорить с вами наедине."
        $ Event_Queue = [0,0]
        $ YanaX.Loc = bg_current
        call Display_Girl(YanaX,DLoc=900)
        call Shift_Focus(YanaX)
        call CleartheRoom(YanaX)
        call Taboo_Level
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ YanaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in YanaX.History:
                call expression YanaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                if "girltalk" not in YanaX.History:
                        return
        $ YanaX.Event[5] += 1
        $ YanaX.FaceChange("normal",1)
        if "asked boyfriend" not in YanaX.DailyActions:
                ch_y "[YanaX.Petname]. Мы можем поговорить?"
        else:
                ch_y ". . ."

        if "limbo2" not in YanaX.History:
                call Yana_Limbo2
                #ch_y "It was only after I fully matured into my powers that I was able to control them enough to return home."
        elif "belasco" not in YanaX.History:
                call Yana_Belasco
                #ch_y "With it, I tore my freedom from Belasco's hide."
                $ YanaX.FaceChange("smile",1)
                ch_y "И именно благодаря нему я чувствую себя свободной и могу наслаждаться своей жизнью. . ."
        elif "Snowflake" not in YanaX.Pets:
                call Yana_Snowflake
        elif "sword" not in YanaX.History:
                call Yana_Sword
                #ch_y "At least, not too badly."
                ch_y "Но поскольку я нахожусь в постоянном контакте со своей душой, я знаю, чего хочу."

        if YanaX in Player.Harem:
                #if she somehow already ended up in the harem
                if "YanaYes" in Player.Traits:
                        $ Player.Traits.remove("YanaYes")
                if "boyfriend" not in YanaX.Petnames:
                        $ YanaX.Petnames.append("boyfriend")
                ch_y "Я рада, что мы нашли друг друга."
                return

        $ YanaX.FaceChange("sly",1,Brows="sad")
        ch_y "И теперь я здесь, с тобой."
        $ YanaX.FaceChange("sly",2,Brows="sad")
        ch_y "Я наслаждаюсь временем, которое мы проводим вместе."
        $ YanaX.FaceChange("sly",2,Eyes="side")
        ch_y ". . . и поэтому я хочу спросить. . ."
        $ YanaX.FaceChange("sly",2,Brows="sad")
        if not Player.Male:
            ch_y "Ты хочешь. . . стать моей. . . девушкой?"
        else:
            ch_y "Ты хочешь. . . стать моим. . . парнем?"
label Yana_BF_Redux:
        $ Line = "start"
        call Shift_Focus(YanaX)
        while Line != "yes":
            menu:
                extend ""
                "Конечно." if Line != "maybe":
                        $ YanaX.FaceChange("smile",1)
                        $ YanaX.Statup("Love", 200, 6)
                        $ YanaX.Statup("Obed", 80, 2)
                        ch_y "Замечательно!"
                        $ Line = "yes"
                "Ладно." if Line == "maybe":
                        $ YanaX.FaceChange("normal",1)
                        $ YanaX.Statup("Love", 200, 4)
                        $ YanaX.Statup("Obed", 80, 2)
                        $ YanaX.Statup("Inbt", 60, 1)
                        $ YanaX.Statup("Inbt", 80, 2)
                        ch_y "Это значит \"да\"?"
                        $ Line = "yes"

                "Мне это не особо интересно." if Line != "maybe":
                        $ YanaX.FaceChange("sad",1)
                        $ YanaX.Statup("Love", 200, -3)
                        $ YanaX.Statup("Obed", 80, 3)
                        ch_y "Ах. . . я понимаю."
                        $ Line = "maybe"
                "не это -совсем- не интересно." if Line == "maybe":
                        $ YanaX.FaceChange("sad",1)
                        $ YanaX.Statup("Love", 200, -5)
                        $ YanaX.Statup("Obed", 60, 1)
                        $ YanaX.Statup("Obed", 80, 3)
                        ch_y "Тц."
                        $ Line = "no"

                "Нет, не думаю, что [Player.Harem[0].Name] меня поймет." if len(Player.Harem) == 1:
                        $ YanaX.Statup("Love", 200, -15)
                        $ YanaX.Statup("Obed", 80, 7)
                        $ YanaX.FaceChange("sadside",1)
                        $ YanaX.GLG(Player.Harem[0],800,-10,1)
                        ch_y "Ах. . . я понимаю."
                        $ Line = "no"
                "Другим девушкам это не понравится." if len(Player.Harem) > 1:
                        $ YanaX.Statup("Love", 200, -15)
                        $ YanaX.Statup("Obed", 80, 7)
                        $ YanaX.FaceChange("sad",1)
                        call HaremStatup(YanaX,700,-10) #lowers like of all Harem girls by 10
                        ch_y "Ах, да. . . у тебя же много -других- девушек. . ."
                        $ Line = "no"

            if Player.Harem and Line == "yes":
                #if you agreed, but have other girls. . .
                if not ApprovalCheck(YanaX, 1400):
                    $ YanaX.FaceChange("sadside",1)
                    ch_y "Однако ты уже с кем-то встречаешься . ."
                    $ Line = "no"
                else:
                    if len(Player.Harem) >= 2:
                        ch_y "Другие девушки будут не против?"
                    else:
                        ch_y "[Player.Harem[0].Name] будет не против?"
                    menu:
                        extend ""
                        "Нет, все будет нормально." if "YanaYes" in Player.Traits:
                                $ YanaX.Statup("Love", 200, 5)
                                $ YanaX.Statup("Obed", 80, 10)
                                $ YanaX.Statup("Inbt", 80, 5)
                                $ YanaX.FaceChange("surprised",1)
                                ch_y "Ах! Превосходно!"
                        "Честно говоря. . . Сперва нужно это узнать." if "YanaYes" not in Player.Traits:
                                $ YanaX.Statup("Love", 200, 3)
                                $ YanaX.Statup("Obed", 80, 3)
                                $ YanaX.Statup("Inbt", 80, 1)
                                $ YanaX.Statup("Lust", 80, 1)
                                $ YanaX.FaceChange("confused",1)
                                ch_y "Ах."
                                ch_y "Тогда. . . дашь мне знать, если что-то изменится?"
                                $ YanaX.Event[5] = 20
                                call Remove_Girl(YanaX)
                                $ Line = 0
                                return
                    call HaremStatup(YanaX,900,20) #raises like of all Harem girls by 20

            if Line == "no":
                    $ YanaX.FaceChange("sadside",1)
                    ch_y "Пожалуй, я слишком \"дикая\" для тебя. . ."
                    call Hide_Yana
                    "[YanaX.Name] исчезает в портале."
                    $ YanaX.Event[5] = 20
                    call Remove_Girl(YanaX)
                    $ Line = 0
                    return
            # end menu

        if "Historia" not in Player.Traits:
            $ Player.Harem.append(YanaX)
            if "YanaYes" in Player.Traits:
                    $ Player.Traits.remove("YanaYes")
            $ YanaX.Petnames.append("boyfriend")
            call Harem_Initiation
        $ YanaX.Statup("Love", 200, 3)
        $ YanaX.Statup("Obed", 80, 3)
        $ YanaX.Statup("Inbt", 80, 1)
        $ YanaX.Statup("Lust", 80, 1)
        $ YanaX.FaceChange("sly",1)
        ch_y "Что ж, а теперь. . ."
        ch_y "Когда мы уладили все \серьезные дела. . .\""
        ch_y "Чем бы нам заняться?"
        if "Historia" in Player.Traits:
                return 1
        $ Tempmod = 10
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        $ Tempmod = 0
        return




## start Yana_Love//////////////////////////////////////////////////////////


label Yana_Love(BO=[]):
        if bg_current != "bg yana":
            if YanaX.Loc == bg_current or YanaX in Party:
                "Внезапно [YanaX.Name] изъявляет желание поговорить с вами в своей комнате, после чего телепортирует вас туда."
            else:
                "[YanaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить с вами в своей комнате, после чего телепортирует вас туда."
        else:
                "[YanaX.Name] внезапно начинает очень пристально смотреть на вас."
        $ bg_current = "bg yana"
        $ Event_Queue = [0,0]
        call Set_The_Scene
        $ YanaX.Loc = bg_current
        call Display_Girl(YanaX,DLoc=900)
        call Shift_Focus(YanaX)
        call CleartheRoom(YanaX)
        call Taboo_Level
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ YanaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in YanaX.History:
                call expression YanaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                if "girltalk" not in YanaX.History:
                        return
        $ YanaX.FaceChange("normal",1)
        ch_y "[YanaX.Petname]. Мы можем поговорить?"

        if "Snowflake" not in YanaX.Pets:
                call Yana_Snowflake
                ch_y "А еще. . ."
        elif "belasco" not in YanaX.History:
                call Yana_Belasco
                #ch_y "With it, I tore my freedom from Belasco's hide."
                $ YanaX.FaceChange("smile",1)
                ch_y "И именно благодаря нему я чувствую себя свободной и могу наслаждаться своей жизнью. . ."
                ch_y "С тобой. . ."
        elif "sword" not in YanaX.History:
                call Yana_Sword
                #ch_y "At least, not too badly."
                ch_y "Но поскольку я нахожусь в постоянном контакте со своей душой, я знаю, чего хочу."

        $ YanaX.FaceChange("smile",1)
        ch_y "Я хочу сказать, что. . . я люблю тебя."

        menu:
            extend ""
            "Я тоже тебя люблю!":
                $ YanaX.FaceChange("smile",2,Eyes="surprised")
                $ YanaX.Statup("Love", 200, 20)
                $ YanaX.Statup("Inbt", 90, 5)
                ch_y "!!!"
                $ YanaX.FaceChange("smile",1)
                $ YanaX.Petnames.append("lover")
                jump Yana_Love_End
            "Я знаю.":
                $ YanaX.FaceChange("confused",1)
                $ YanaX.Statup("Love", 200, -5)
                $ YanaX.Statup("Obed", 90, 5)
                $ YanaX.Statup("Inbt", 90, 5)
                ch_y "Хм?"
                ch_y "Я не понимаю. . ."
                $ YanaX.FaceChange("normal",1,Mouth="smirk")
                ch_y "Это положительный ответ?"
            "Круто?":
                $ YanaX.FaceChange("confused",1,Mouth="smile")
                $ YanaX.Statup("Obed", 90, 5)
                if not Player.Male:
                    ch_y "Я. . . не думаю, что ты меня поняла. . ."
                else:
                    ch_y "Я. . . не думаю, что ты меня понял. . ."
            "Хм.":
                $ YanaX.FaceChange("sadside",1)
                $ YanaX.Statup("Love", 200, -5)
                $ YanaX.Statup("Obed", 90, 10)
                ch_y "Значит, ты не можешь ответить мне взаимностью. . ."
        menu:
            extend ""
            "Ох, я тоже тебя люблю!":
                $ YanaX.FaceChange("smile",1)
                $ YanaX.Statup("Love", 200, 15)
                $ YanaX.Statup("Obed", 90, 5)
                ch_y "Ах. . . "
                $ YanaX.FaceChange("sly",1)
                $ YanaX.Statup("Inbt", 90, 5)
                ch_y "!!!"
                $ YanaX.Petnames.append("lover")
                jump Yana_Love_End
            "Я. . . тоже тебя люблю?":
                $ YanaX.FaceChange("confused",1)
                $ YanaX.Statup("Love", 200, 5)
                $ YanaX.Statup("Obed", 90, 5)
                ch_y "[YanaX.Petname], не относись к таким вещам так легкомысленно."
                $ YanaX.FaceChange("bemused",1)
                $ YanaX.Petnames.append("lover")
                jump Yana_Love_End
            "Это, конечно, круто и все такое. . .":
                $ YanaX.FaceChange("sad",1)
                $ YanaX.Statup("Love", 200, -5)
                $ YanaX.Statup("Obed", 90, 10)
                $ YanaX.Statup("Inbt", 90, -5)
                ch_y ". . . я понимаю. . ."
                ch_y "Со мной бывает трудно."
            "Мне. . . некомфортно от этого.":
                $ YanaX.FaceChange("sadside",1)
                $ YanaX.Statup("Love", 200, -10)
                $ YanaX.Statup("Obed", 90, 15)
                $ YanaX.Statup("Inbt", 90, -5)
                ch_y "Ах. . ."
                $ YanaX.FaceChange("sad",1)
                ch_y "Я понимаю."

        if "sexfriend" in YanaX.Petnames:
                $ YanaX.FaceChange("sly",1)
                ch_y "Не волнуйся, мы все еще можем заниматься сексом. . ."
        elif "sir" in YanaX.Petnames:
                $ YanaX.FaceChange("sad",1,Mouth="normal")
                ch_y "Я все еще рассчитываю на твою помощь в удержании моей темной стороны под контролем. . ."
        else:
                $ YanaX.FaceChange("sad",1)
                ch_y "Мы все равно можем остаться друзьями. . ."
                $ YanaX.FaceChange("sadside",1,Mouth="smirk")
        menu:
            extend ""
            "Ага. . .":
                    $ YanaX.FaceChange("sad",1)
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Inbt", 80, 1)
                    ch_y "Хорошо. . ."
            ". . .":
                    $ YanaX.FaceChange("sad",1)
                    $ YanaX.Statup("Obed", 90, 1)
            "Поговорим в другой раз":
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 80, 2)
                    ch_y "Что ж, хорошо. . ."
                    $ YanaX.FaceChange("sad",1)
        call Hide_Yana
        "[YanaX.Name] исчезает в портале."
        call Remove_Girl(YanaX)
        $ YanaX.Loc = "hold" #puts her off the board for the day
        $ YanaX.Event[6] = 20
        $ Line = 0
        jump Misplaced
        return

label Yana_Love_End:
        $ YanaX.Event[6] = 5
        "[YanaX.Name] бросается к вам и целует."
        $ YanaX.Statup("Love", 200, 25)
        $ YanaX.Statup("Lust", 90, 5)
        $ YanaX.FaceChange("sly",1)
        ch_y "Я так заволновалась."
        ch_y "-на мгновение, конечно."
        $ YanaX.Statup("Lust", 90, 10)

        if not YanaX.Sex:
                $ YanaX.FaceChange("bemused",2)
                ch_y "Возможно, теперь я готова. . ."
        ch_y "Ты желаешь сейчас заняться со мной сексом?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Ага, давай. . . [[заняться сексом] (locked)":   #fix, unlock once sex becomes an option
                    $ YanaX.Statup("Inbt", 30, 20)
                    $ YanaX.Statup("Obed", 70, 10)
                    ch_y "Замечательно. . ."
                    if Player.Male:
                            call SexAct("sex") # call Yana_SexAct("sex")
                    else:
                            call SexAct("blow") # call Yana_SexAct("blow")
                "У меня есть пара идей. . . [[выбрать другое занятие]":
                    $ YanaX.Brows = "confused"
                    $ YanaX.Statup("Obed", 70, 25)
                    ch_y "Каких? . ."
                    $ Tempmod = 20
                    call SexMenu
        jump Misplaced

label Yana_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ YanaX.DailyActions.append("relationship")

        if YanaX.Event[6] >= 25:
                #if this is the second time through
                ch_p "Надеюсь, ты простила меня, я все еще люблю тебя."
                $ YanaX.Statup("Love", 95, 10)
                if "syke" in YanaX.History:
                    $ YanaX.Statup("Love", 200, -5)
                if ApprovalCheck(YanaX, 950, "L"):
                    $ Line = "love"
                else:
                    $ YanaX.FaceChange("sad",1)
                    ch_y "Я. . . я не могу. . . пока."
                    $ YanaX.FaceChange("sadside",Mouth="lipbite")
                    ch_y ". . ."
        else:
                    if not Player.Male:
                        ch_p "Помнишь, я сказала тебе, что не люблю тебя?"
                    else:
                        ch_p "Помнишь, я сказал тебе, что не люблю тебя?"
                    $ YanaX.FaceChange("perplexed",1)
                    ch_y "Да?"

        if Line != "love":
                menu:
                    extend ""
                    "Прости, я не хотела так говорить." if not Player.Male:
                        $ YanaX.FaceChange("confused",1)
                        ch_y ". . ."
                        ch_y "Ах. . ."
                        ch_p "Что ж. . . я люблю тебя, [YanaX.Name]."
                        $ YanaX.Statup("Love", 200, 10)
                        if ApprovalCheck(YanaX, 950, "L"):
                            $ Line = "love"
                            $ YanaX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ YanaX.FaceChange("sadside")
                            ch_y ". . .  наверное, я не могу ответить тебе взаимностью. . ."
                    "Прости, я не хотел так говорить." if Player.Male:
                        $ YanaX.FaceChange("confused",1)
                        ch_y ". . ."
                        ch_y "Ах. . ."
                        ch_p "Что ж. . . я люблю тебя, [YanaX.Name]."
                        $ YanaX.Statup("Love", 200, 10)
                        if ApprovalCheck(YanaX, 950, "L"):
                            $ Line = "love"
                            $ YanaX.FaceChange("surprised",1,Mouth="normal")
                        else:
                            $ YanaX.FaceChange("sadside")
                            ch_y ". . .  наверное, я не могу ответить тебе взаимностью. . ."
                    "Я передумала, я люблю тебя, так что. . ." if not Player.Male:
                        if ApprovalCheck(YanaX, 950, "L"):
                            $ Line = "love"
                            $ YanaX.FaceChange("surprised",1,Mouth="normal")
                            ch_y "Да?"
                        else:
                            $ YanaX.Mouth = "sad"
                            ch_y "Ах. . ."
                            $ YanaX.Statup("Inbt", 90, 10)
                            $ YanaX.FaceChange("sadside")
                            ch_y ". . . наверное, я уже оставило это в прошлом. . ."
                    "Я передумал, я люблю тебя, так что. . ." if Player.Male:
                        if ApprovalCheck(YanaX, 950, "L"):
                            $ Line = "love"
                            $ YanaX.FaceChange("surprised",1,Mouth="normal")
                            ch_y "Да?"
                        else:
                            $ YanaX.Mouth = "sad"
                            ch_y "Ах. . ."
                            $ YanaX.Statup("Inbt", 90, 10)
                            $ YanaX.FaceChange("sadside")
                            ch_y ". . . наверное, я уже оставило это в прошлом. . ."
                    "Эм, неважно.":
                            $ YanaX.Statup("Love", 200, -30)
                            $ YanaX.Statup("Obed", 50, 10)
                            $ YanaX.FaceChange("angry")
                            ch_y "Ты подвергаешь себя опасности. . ."
                            $ YanaX.RecentActions.append("angry")
                            $ YanaX.DailyActions.append("angry")
        if Line == "love":
                $ YanaX.Statup("Love", 200, 40)
                $ YanaX.Statup("Obed", 90, 10)
                $ YanaX.Statup("Inbt", 90, 10)
                $ YanaX.FaceChange("normal")
                if not Player.Male:
                    ch_y "Хорошо, что ты все обдумала. . ."
                else:
                    ch_y "Хорошо, что ты все обдумал. . ."
                ch_y ". . . я тоже тебя люблю, [YanaX.Petname]!"
                $ YanaX.Petnames.append("lover")
        $ YanaX.Event[6] = 25
        return

# end Yana_Love//////////////////////////////////////////////////////////


# start Yana_Sub//////////////////////////////////////////////////////////

label Yana_Sub:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(YanaX,"bemused","выглядит тихой. . .")
                return
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ YanaX.Demon = 1
        call Set_The_Scene
        if YanaX.Loc != bg_current and YanaX not in Party:
            "Внезапно [YanaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."

        $ Event_Queue = [0,0]
        $ YanaX.Loc = bg_current
        call Display_Girl(YanaX,DLoc=900)
        call Shift_Focus(YanaX)
        call CleartheRoom(YanaX)
        call Taboo_Level
        $ YanaX.DailyActions.append("relationship")
        $ YanaX.FaceChange("bemused", 1)
        if not Player.Male and "girltalk" not in YanaX.History:
                call expression YanaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                if "girltalk" not in YanaX.History:
                        return

        if "horny" not in YanaX.History:
                call Yana_Horny
        $ YanaX.FaceChange("bemused",1)
        if "limbo2" not in YanaX.History:
                call Yana_Limbo2
        elif "sword" not in YanaX.History:
                call Yana_Sword
                $ YanaX.Sword = 0
                ch_y "-но не беспокойся об этом."

        ch_y "Мое прошлое в Лимбо. . . оставило на мне свой отпечаток."
        ch_y "Мне нужна помощь, чтобы справиться с этим."
        $ YanaX.FaceChange("confused",2)
        ch_y "Ты понимаешь, о чем я прошу тебя?"
        $ YanaX.FaceChange("bemused",1)
        $ YanaX.History.append("sir")
        menu:
            extend ""
            "Ага, пожалуй.":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 80, 1)
                    $ YanaX.Statup("Obed", 90, 5)
            "Конечно.":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 80, 1)
                    $ YanaX.Statup("Obed", 90, 8)
            "Наверное.":
                    $ YanaX.Statup("Obed", 90, 2)
                    $ YanaX.FaceChange("confused",1)
                    ch_y "Я не думаю, что ты принимаешь этот разговор всерьез. . ."
            ". . .":
                    $ YanaX.Statup("Obed", 90, 1)
            "Что?":
                    $ YanaX.Statup("Love", 80, -1)
                    $ YanaX.Statup("Obed", 90, -1)
                    $ YanaX.Statup("Inbt", 80, 1)
                    ch_y "Мне кажется, ты понимаешь меня."
        ch_y "Моя демоническая половина постоянно борется за контроль над моим телом."
        if not Player.Male:
            ch_y "Я хотела бы, чтобы ты помогла мне в этой борьбе."
            ch_y "Мне нужно, чтобы ты направляла меня, говорила, что я должна делать."
        else:
            ch_y "Я хотела бы, чтобы ты помог мне в этой борьбе."
            ch_y "Мне нужно, чтобы ты направлял меня, говорил, что я должна делать."
        $ YanaX.FaceChange("sly",1)
        menu:
            extend ""
            "Это я могу.":
                    $ YanaX.Statup("Obed", 200, 10)
                    $ YanaX.Statup("Inbt", 70, 2)
                    $ YanaX.FaceChange("smile",1)
                    ch_y "Хорошо. . ."
                    $ YanaX.FaceChange("sly",1)
                    if not Player.Male:
                        ch_y ". . . госпожа."
                    else:
                        ch_y ". . . господин."
            "О, ладно.":
                    $ YanaX.Statup("Inbt", 70, 3)
                    if not Player.Male:
                        ch_y "Приму это за \"да,\" . . госпожа."
                    else:
                        ch_y "Приму это за \"да,\" . . господин."
            "Это слишком хлопотно.":
                    $ YanaX.Statup("Love", 80, -5)
                    $ YanaX.Statup("Obed", 200, -10)
                    $ YanaX.Statup("Inbt", 70, -2)
                    $ YanaX.FaceChange("sadside",2)
                    ch_y "Ах. . . я понимаю. . ."
                    return  #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            "Мне это неинтересно.":
                    $ YanaX.Statup("Obed", 200, -5)
                    $ YanaX.Statup("Inbt", 70, -2)
                    $ YanaX.FaceChange("sadside",2)
                    ch_y "Ах. . . я понимаю. . ."
                    return  #endpoint       endpoint       endpoint       endpoint       endpoint       endpoint
            ". . .":
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 70, 3)
                    if not Player.Male:
                        ch_y "Это. . . \"да,\" госпожа?"
                    else:
                        ch_y "Это. . . \"да,\" господин?"
        $ YanaX.Petnames.append("sir")
        menu:
            extend ""
            "Ага, [YanaX.Pet].":
                    $ YanaX.Statup("Love", 80, 2)
                    $ YanaX.Statup("Obed", 200, 10)
                    $ YanaX.Statup("Inbt", 70, 2)
                    $ YanaX.NameCheck() #checks reaction to petname
                    if not Player.Male:
                        $ YanaX.Petname = "госпожа"
                        $ YanaX.Petname_rod = "госпожи"
                        $ YanaX.Petname_dat = "госпоже"
                        $ YanaX.Petname_vin = "госпожу"
                        $ YanaX.Petname_tvo = "госпожой"
                        $ YanaX.Petname_pre = "госпоже"
                    else:
                        $ YanaX.Petname = "господин"
                        $ YanaX.Petname_rod = "господина"
                        $ YanaX.Petname_dat = "господину"
                        $ YanaX.Petname_vin = "господина"
                        $ YanaX.Petname_tvo = "господином"
                        $ YanaX.Petname_pre = "господине"
            ". . .":
                    $ YanaX.Statup("Obed", 200, 7)
                    if not Player.Male:
                        $ YanaX.Petname = "госпожа"
                        $ YanaX.Petname_rod = "госпожи"
                        $ YanaX.Petname_dat = "госпоже"
                        $ YanaX.Petname_vin = "госпожу"
                        $ YanaX.Petname_tvo = "госпожой"
                        $ YanaX.Petname_pre = "госпоже"
                    else:
                        $ YanaX.Petname = "господин"
                        $ YanaX.Petname_rod = "господина"
                        $ YanaX.Petname_dat = "господину"
                        $ YanaX.Petname_vin = "господина"
                        $ YanaX.Petname_tvo = "господином"
                        $ YanaX.Petname_pre = "господине"
            "Только не зови меня \"госпожой\"." if not Player.Male:
                    $ YanaX.Statup("Obed", 200, 10)
                    $ YanaX.Statup("Inbt", 70, -1)
                    $ YanaX.FaceChange("sadside",2)
                    ch_y "Поняла, [YanaX.Petname]."
                    $ YanaX.FaceChange("sly",1)
            "Только не зови меня \"господином\"." if Player.Male:
                    $ YanaX.Statup("Obed", 200, 10)
                    $ YanaX.Statup("Inbt", 70, -1)
                    $ YanaX.FaceChange("sadside",2)
                    ch_y "Поняла, [YanaX.Petname]."
                    $ YanaX.FaceChange("sly",1)
        if YanaX.Addict <= 50:
                $ YanaX.Demon = 0
                ch_y "Ах, так-то лучше. . ."
        ch_y "Если тебе что-нибудь понадобится, тебе нужно только попросить. . ."
        $ YanaX.FaceChange("sly",1)
        ch_y "Я не такая и \"хрупкая\". . ."
        return

label Yana_Sub_Asked:
        $ Line = 0
        $ YanaX.FaceChange("sadside", 1)
        if not Player.Male:
            ch_y "Ты. . . казалось, в этом не заинтересована."
        else:
            ch_y "Ты. . . казалось, в этом не заинтересован."
        menu:
            extend ""
            "Ну, я хочу извиниться. Надеюсь, ты дашь мне второй шанс.":
                    if "sir" in YanaX.Petnames and ApprovalCheck(YanaX, 850, "O"):
                            #if this is asking about the "master" name, and her Obedience is higher than 700
                            pass
                    elif ApprovalCheck(YanaX, 550, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            pass
                    else: #if it failed both those things,
                            $ YanaX.FaceChange("angry", 1)
                            ch_y "Я не думаю, что в этом есть необходимость." #Failed again. :(
                            $ Line = "rude"

                    if Line != "rude":
                            $ YanaX.Statup("Love", 90, 10)
                            $ YanaX.FaceChange("sly", 1)
                            ch_y "Ах. . . тогда мы можем попробовать. . ."

            "Послушай. . . я знаю, что ты этого хочешь. Ты согласна попробовать еще раз, или нет?":
                    $ YanaX.FaceChange("bemused", 1)
                    if "sir" in YanaX.Petnames:
                        if ApprovalCheck(YanaX, 850, "O"):
                            if not Player.Male:
                                ch_y "Да, госпожа. . ."
                            else:
                                ch_y "Да, господин. . ."
                        else:
                            ch_y ". . . Я не думаю, что теперь я этого хочу. . ."
                            $ Line = "rude"
                    elif ApprovalCheck(YanaX, 600, "O"):
                            #if it's instead about earning the "sir" title, and her approval is over 500
                            $ YanaX.FaceChange("confused", 1)
                            ch_y "Ах. . ."
                            $ YanaX.FaceChange("sly", 1)
                            ch_y ". . . возможно."
                            ch_y "На этот раз ты говоришь серьезно?"
                            menu:
                                extend ""
                                "Да, извини, что я была довольно груба." if not Player.Male:
                                                $ YanaX.Statup("Love", 90, 15)
                                                $ YanaX.Statup("Inbt", 50, 10)
                                                $ YanaX.FaceChange("bemused", 1)
                                                $ YanaX.Eyes = "side"
                                                ch_y "Что ж, хорошо."
                                "Да, извини, что я был довольно груб." if Player.Male:
                                                $ YanaX.Statup("Love", 90, 15)
                                                $ YanaX.Statup("Inbt", 50, 10)
                                                $ YanaX.FaceChange("bemused", 1)
                                                $ YanaX.Eyes = "side"
                                                ch_y "Что ж, хорошо."
                                "Ты пиздец как права, сучка.":
                                        if "sir" in YanaX.Petnames and ApprovalCheck(YanaX, 900, "O"):
                                                $ YanaX.Statup("Love", 200, -5)
                                                $ YanaX.Statup("Obed", 200, 10)
                                                ch_y ". . ."
                                        elif ApprovalCheck(YanaX,500, "O"):
                                                $ YanaX.Statup("Love", 200, -5)
                                                $ YanaX.Statup("Obed", 200, 10)
                                                ch_y ". . . что?"
                                                ch_y "Не такого поведения я ожидала. . ."
                                        else: #if it failed both those things,
                                                $ YanaX.Statup("Love", 200, -10)
                                                $ YanaX.Statup("Obed", 90, -10)
                                                $ YanaX.Statup("Obed", 200, -10)
                                                $ YanaX.Statup("Inbt", 50, -15)
                                                $ YanaX.FaceChange("angry", 1)
                                                ch_y "Это слишком."
                                                $ Line = "rude"
                                "Ладно, тогда не бери в голову.":
                                                $ YanaX.FaceChange("angry", 1)
                                                $ YanaX.Statup("Love", 200, -10)
                                                $ YanaX.Statup("Obed", 90, -10)
                                                $ YanaX.Statup("Obed", 200, -10)
                                                $ YanaX.Statup("Inbt", 50, -15)
                                                ch_y ". . ."
                                                ch_y "Мне это неинтересно, если ты не воспринимаешь мою просьбу всерьез."
                                                $ Line = "rude"

        $ YanaX.RecentActions.append("asked sub")
        $ YanaX.DailyActions.append("asked sub")
        if Line == "rude":
                #If line hasn't been set to "rude" by something above, then it skips right past this
                call Hide_Yana
                "[YanaX.Name] исчезает в портале."
                call Remove_Girl(YanaX)
                $ YanaX.RecentActions.append("angry")
                if "Historia" not in Player.Traits:
                        $ renpy.pop_call()
        elif "sir" in YanaX.Petnames:
                #it didn't fail and "sir" was covered
                $ YanaX.Statup("Obed", 200, 50)
                $ YanaX.Petnames.append("master")
                if not Player.Male:
                    $ YanaX.Petname = "хозяйка"
                    $ YanaX.Petname_rod = "хозяйки"
                    $ YanaX.Petname_dat = "хозяйке"
                    $ YanaX.Petname_vin = "хозяйку"
                    $ YanaX.Petname_tvo = "хозяйкой"
                    $ YanaX.Petname_pre = "хозяйке"
                else:
                    $ YanaX.Petname = "хозяин"
                    $ YanaX.Petname_rod = "хозяина"
                    $ YanaX.Petname_dat = "хозяину"
                    $ YanaX.Petname_vin = "хозяина"
                    $ YanaX.Petname_tvo = "хозяином"
                    $ YanaX.Petname_pre = "хозяине"
                $ YanaX.Eyes = "sly"
                if not Player.Male:
                    ch_y ". . . хозяйка. . ."
                else:
                    ch_y ". . . хозяин. . ."
                call Yana_Demon(1) #no intro
        else:
                #it didn't fail
                $ YanaX.Statup("Obed", 200, 30)
                $ YanaX.Petnames.append("sir")
                if not Player.Male:
                    $ YanaX.Petname = "госпожа"
                    $ YanaX.Petname_rod = "госпожи"
                    $ YanaX.Petname_dat = "госпоже"
                    $ YanaX.Petname_vin = "госпожу"
                    $ YanaX.Petname_tvo = "госпожой"
                    $ YanaX.Petname_pre = "госпоже"
                else:
                    $ YanaX.Petname = "господин"
                    $ YanaX.Petname_rod = "господина"
                    $ YanaX.Petname_dat = "господину"
                    $ YanaX.Petname_vin = "господина"
                    $ YanaX.Petname_tvo = "господином"
                    $ YanaX.Petname_pre = "господине"
                $ YanaX.FaceChange("sly", 1)
                if not Player.Male:
                    ch_y ". . . госпожа."
                else:
                    ch_y ". . . господин."
        return

# end Yana_Sub//////////////////////////////////////////////////////////


# start Yana_Master//////////////////////////////////////////////////////////

label Yana_Master:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(YanaX,"bemused","выглядит необычайно покорной. . .")
                return
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene
        $ YanaX.Demon = 1
        if YanaX.Loc != bg_current and YanaX not in Party:
            "Внезапно [YanaX.Name] появляется, словно из ниоткуда, и изъявляет желание поговорить."

        $ Event_Queue = [0,0]
        $ YanaX.Loc = bg_current
        call Display_Girl(YanaX,DLoc=900)
        call Shift_Focus(YanaX)
        call CleartheRoom(YanaX)
        call Taboo_Level
        $ YanaX.DailyActions.append("relationship")
        $ Line = 0
        $ YanaX.FaceChange("sly", 1)
        if "belasco" not in YanaX.History:
                call Yana_Belasco
        if "sword" not in YanaX.History:
                call Yana_Sword
        ch_y ". . . [YanaX.Petname]. . ."
        ch_y "Как ты оцениваешь мои успехи на данный момент?"
        ch_y "Считаешь ли ты, что я уступаю соблазнам?"
        menu:
            "Да?":
                    $ YanaX.Statup("Love", 90, 1)
                    if YanaX.SEXP >= 40 or "exhibitionist" in YanaX.Traits:
                            $ YanaX.Statup("Inbt", 90, 2)
                            ch_y "Справедливое замечание."
                    else:
                            $ YanaX.FaceChange("sad",1)
                            $ YanaX.Statup("Obed", 200, 2)
                            $ YanaX.Statup("Inbt", 80, 2)
                            ch_y "Не думаю, что я была настолько плоха."
                            $ YanaX.FaceChange("smile",1)
            "Только в хорошем плане.":
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Inbt", 80, 2)
                    if YanaX.SEXP >= 40 or "exhibitionist" in YanaX.Traits:
                            ch_y "Справедливое замечание."
                    else:
                            $ YanaX.FaceChange("smile",1)
                            ch_y "Я немного не это имела в виду."
            "Вижу, ты на рогах. . .":
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Inbt", 70, 2)
                    if YanaX.SEXP >= 40 or "exhibitionist" in YanaX.Traits:
                            $ YanaX.FaceChange("smile",1)
                            $ YanaX.Statup("Inbt", 80, 2)
                            ch_y "Конечно, в хорошем смысле."
                    else:
                            $ YanaX.FaceChange("smile",1)
                            $ YanaX.Statup("Love", 90, 1)
                            ch_y "Справедливое замечание."
            "Да не особо.":
                    if YanaX.SEXP >= 40 or "exhibitionist" in YanaX.Traits:
                            $ YanaX.FaceChange("smile",1)
                            $ YanaX.Statup("Inbt", 80, 2)
                            ch_y "Думаешь, я не заходила слишком далеко?"
                    else:
                            $ YanaX.FaceChange("smile",1)
                            $ YanaX.Statup("Love", 90, 1)
                            ch_y "Это хорошо. . ."
            ". . .":
                            $ YanaX.FaceChange("smile",1)
                            $ YanaX.Statup("Obed", 200, 2)
                            ch_y "Нет? . ."
                            ch_y "Это хорошо."
        ch_y "Мне все труднее сохранять контроль."
        $ YanaX.FaceChange("angry",1,Eyes="side")
        ch_y "Когда я была маленькой, Беласко пытался подчинить меня - и у него ничего не вышло."
        $ YanaX.FaceChange("sad",2,Eyes="side")
        ch_y "Когда он пытался мной управлять, это было. . .\"грязно.\" . ."
        ch_y "Порочно. . ."
        $ YanaX.FaceChange("sly",1,Eyes="side")
        ch_y "Но когда я с тобой, мне не -хочется- сопротивляться."
        $ YanaX.FaceChange("smile",1)
        ch_y "Наоборот, я чувствую поддержку, утешение."
        $ YanaX.FaceChange("sly",1)
        ch_y "Я верю, что ты способен обуздать мою темную сторону."
        ch_y "С твоей помощью я не -страшусь- этой части себя. . ."
        if not Player.Male:
            ch_y ". . . хозяйка. . ."
        else:
            ch_y ". . . хозяин. . ."

        $ Line = 0

        $ YanaX.History.append("master")
        menu:
            extend ""
            "Да, продолжай звать меня \"хозяйкой\"" if not Player.Male:
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 15)
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Petnames.append("master")
                    ch_y "Спасибо. . ."
            "Да, продолжай звать меня \"хозяином\"" if Player.Male:
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 15)
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Petnames.append("master")
                    ch_y "Спасибо. . ."
            "Прекращай.":
                    $ YanaX.Statup("Love", 90, -3)
                    $ YanaX.Statup("Obed", 200, -3)
                    $ YanaX.FaceChange("confused",1)
            "Че?":
                    $ YanaX.Statup("Obed", 200, -3)
                    $ YanaX.FaceChange("confused",1)
            ". . .":
                    $ YanaX.Statup("Obed", 200, 5)
                    $ YanaX.Statup("Inbt", 80, 3)
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Petnames.append("master")
                    ch_y ". . ."

        while "master" not in YanaX.Petnames:
            if not Player.Male:
                ch_y "Я не могу звать тебя хозяйкой?"
            else:
                ch_y "Я не могу звать тебя хозяином?"
            menu:
                extend ""
                "Можешь, конечно.":
                        $ YanaX.Petnames.append("master")
                        $ YanaX.Statup("Love", 200, 1)
                        $ YanaX.Statup("Obed", 200, 2)
                        ch_y "Замечательно."
                "Можешь.":
                        $ YanaX.Petnames.append("master")
                        $ YanaX.FaceChange("confused",1,Eyes="side")
                        $ YanaX.Statup("Obed", 200, -1)
                        ch_y "Что ж. . . хорошо. . ."
                        $ YanaX.FaceChange("normal",1)
                "Мне не хочется ничего менять.":
                        $ YanaX.FaceChange("sadside",2)
                        $ YanaX.Statup("Love", 80, -1)
                        $ YanaX.Statup("Obed", 200, -2)
                        $ YanaX.Statup("Inbt", 70, -2)
                        ch_y "Ах. . . что ж, хорошо. . ."
                        $ YanaX.FaceChange("normal",1)
                        ch_y "Я понимаю. . ."
                        return
                "Нет.":
                        $ YanaX.FaceChange("sad",2,Eyes="surprised")
                        $ YanaX.Statup("Love", 80, -1)
                        $ YanaX.Statup("Obed", 200, -4)
                        $ YanaX.Statup("Inbt", 70, -2)
                        ch_y "Ах. . ."
                        $ YanaX.FaceChange("sad",2)
                        ch_y "Мне не стоило оказывать на тебя такое давление. . ."
                        ch_y "Пожалуй. . . я лучше уйду."
                        call Hide_Yana
                        "[YanaX.Name] исчезает в портале."
                        call Remove_Girl(YanaX)
                        $ YanaX.FaceChange("normal",1)
                        $ YanaX.Loc = "hold" #puts her off the board for the day
                        return
                "Что ты имеешь в виду?" if "what" not in YanaX.RecentActions:
                        $ YanaX.RecentActions.append("what")
                        $ YanaX.Statup("Obed", 200, -1)
                        ch_y "Я бы хотела звать тебя. . ."
        if not Player.Male:
            ch_y ". . . \"хозяйка\"."
        else:
            ch_y ". . . \"хозяин\"."
        menu:
            extend ""
            ". . .":
                    if not Player.Male:
                        $ YanaX.Petname = "хозяйка"
                        $ YanaX.Petname_rod = "хозяйки"
                        $ YanaX.Petname_dat = "хозяйке"
                        $ YanaX.Petname_vin = "хозяйку"
                        $ YanaX.Petname_tvo = "хозяйкой"
                        $ YanaX.Petname_pre = "хозяйке"
                    else:
                        $ YanaX.Petname = "хозяин"
                        $ YanaX.Petname_rod = "хозяина"
                        $ YanaX.Petname_dat = "хозяину"
                        $ YanaX.Petname_vin = "хозяина"
                        $ YanaX.Petname_tvo = "хозяином"
                        $ YanaX.Petname_pre = "хозяине"
                    $ YanaX.FaceChange("smile", 2, Eyes="side")
                    $ YanaX.Statup("Obed", 200, 2)
            "А хорошо звучит.":
                    if not Player.Male:
                        $ YanaX.Petname = "хозяйка"
                        $ YanaX.Petname_rod = "хозяйки"
                        $ YanaX.Petname_dat = "хозяйке"
                        $ YanaX.Petname_vin = "хозяйку"
                        $ YanaX.Petname_tvo = "хозяйкой"
                        $ YanaX.Petname_pre = "хозяйке"
                    else:
                        $ YanaX.Petname = "хозяин"
                        $ YanaX.Petname_rod = "хозяина"
                        $ YanaX.Petname_dat = "хозяину"
                        $ YanaX.Petname_vin = "хозяина"
                        $ YanaX.Petname_tvo = "хозяином"
                        $ YanaX.Petname_pre = "хозяине"
                    $ YanaX.FaceChange("normal", 1)
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 80, 2)
            "Мне не нравится термин \"хозяйка\"." if not Player.Male:
                    $ YanaX.FaceChange("sad", 1,Mouth="smile")
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Obed", 200, 3)
                    ch_y "Я понимаю, я могу звать тебя как угодно."
            "Мне не нравится термин \"хозяин\"." if Player.Male:
                    $ YanaX.FaceChange("sad", 1,Mouth="smile")
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Obed", 200, 3)
                    ch_y "Я понимаю, я могу звать тебя как угодно."
        $ YanaX.FaceChange("sly",1)
        ch_y "Теперь я чувствую, что могу принимать облик демона или человека, когда захочу."
        ch_y "Обязательно скажи мне, какой из них тебе нравится больше. . ."
        call Yana_Demon(0) #no intro
        return

# end Yana_Master//////////////////////////////////////////////////////////

label Yana_Demon(Intro=1):
        #if "demon" in traits, she stays in demon form
        #if "resist" in traits, she avoids demon form as best she can
        # if neither, she has horns over 50 addiction
        $ YanaX.DrainWord(1,0,0,1) #traits
        if Intro:
            ch_y "Какой облик мне следует принимать?"
        menu:
            extend ""
            "Оставайся все время в облике Демона.":
                        $ YanaX.DrainWord("resist",0,0,1) #traits
                        $ YanaX.AddWord(1,0,0,0,"demon") #traits $ YanaX.AddWord("demon",0,0,1)
                        if not YanaX.Demon:
                                $ YanaX.FaceChange("sad",2,Eyes="closed",Mouth="open")
                                $ YanaX.Demon = 1
                                if "demonchange" not in YanaX.RecentActions:
                                        $ YanaX.Statup("Lust", 70, 5)
                                "[YanaX.Name] закрывает глаза и, кажется, немного расслабляется, затем у нее на голове вырастают рога."
            "Пусть твое тело само решает.":
                        #removes both traits, reseting the balance
                        $ YanaX.DrainWord("resist",0,0,1) #traits
                        $ YanaX.DrainWord("demon",0,0,1) #traits
            "Сопротивляйся Демону внутри.":
                        $ YanaX.DrainWord("demon",0,0,1) #traits
                        $ YanaX.AddWord(1,0,0,"resist") #traits
                        if YanaX.Demon:
                                $ YanaX.FaceChange("angry",2,Eyes="closed")
                                $ YanaX.Demon = 0
                                "[YanaX.Name] закрывает глаза и, кажется, сосредотачивается, затем ее рога и хвост втягиваются."
        $ YanaX.FaceChange("sly",1)
        if "demonchange" in YanaX.RecentActions:
                ch_y "Поняла, но мне не нравятся постоянные \"изменения.\""
        else:
                $ YanaX.AddWord(1,"demonchange")
                ch_y "Конечно, [YanaX.Petname]."
        return

# start Yana_Sexfriend//////////////////////////////////////////////////////////

label Yana_Sexfriend:   #Yana_Update
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        $ Event_Queue = [0,0]
        call CleartheRoom(Ch_Focus,1,1) #removes all but the focus girl, so she stays when the other goes
        $ YanaX.Loc = bg_current
        call Shift_Focus(YanaX)
        $ YanaX.FaceChange("smile",2)
        "[YanaX.Name] подходит к вам и отводит в сторону."
        call Set_The_Scene
        call Taboo_Level
        $ YanaX.DailyActions.append("relationship")
        if not Player.Male and "girltalk" not in YanaX.History:
                call expression YanaX.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"
                if "girltalk" not in YanaX.History:
                        return
        $ Line = 0
        $ YanaX.Petnames.append("sex friend")
        if "limbo2" not in YanaX.History:
                call Yana_Limbo2
        else:
                ch_y "Помнишь, я рассказывала тебе о своем пребывании в Лимбе?"
                menu:
                    extend ""
                    "Да?":
                            $ YanaX.FaceChange("smile",1)
                            $ YanaX.Statup("Love", 80, 1)
                            $ YanaX.Statup("Love", 90, 1)
                    "Напомнишь?":
                            $ YanaX.FaceChange("angry",1)
                            $ YanaX.Statup("Love", 80, -1)
                            $ YanaX.Statup("Obed", 200, 2)
                            if not Player.Male:
                                ch_y "Будь внимательна, и ты узнаешь много нового."
                            else:
                                ch_y "Будь внимателен, и ты узнаешь много нового."
                    "Да не особо.":
                            $ YanaX.FaceChange("angry",1)
                            $ YanaX.Statup("Love", 90, -2)
                            $ YanaX.Statup("Obed", 200, 2)
                            if not Player.Male:
                                ch_y "Будь внимательна, и ты узнаешь много нового."
                            else:
                                ch_y "Будь внимателен, и ты узнаешь много нового."
                    ". . .":
                            $ YanaX.Statup("Inbt", 200, 2)
        ch_y "Как я уже говорила, за время пребывания там я превратилась в девушку."
        $ YanaX.FaceChange("sadside",1)
        ch_y "За мной всегда следили бесы, куда бы я ни пошла."
        $ YanaX.FaceChange("sadside",2)
        ch_y "Каждый день, когда я ела, когда спала, когда. . ."
        ch_y "Изучала свое растущее тело. . ."
        menu:
            extend ""
            "Значит, ты. . .":
                    $ YanaX.Statup("Obed", 90, 2)
                    $ YanaX.Statup("Inbt",200, 2)
            "Ты -теребила фасолинку-?":
                    $ YanaX.Statup("Obed", 90, 1)
                    $ YanaX.Statup("Inbt", 200, 3)
            ". . .":
                    $ YanaX.Statup("Obed", 90, 2)
                    $ YanaX.Statup("Inbt", 200, 1)
        $ YanaX.FaceChange("sadside",1,Mouth="smirk")
        ch_y "Да, я. . . начала -мастурбировать-, пока еще была в Лимбо."
        ch_y "Там было не так уж много дел."
        $ YanaX.FaceChange("sly",1,Eyes="side")
        ch_y "-так что бесы, -конечно-, наблюдали и за этим."
        ch_y "Это казалось им -очень- забавным, хотя они не более, чем животные."
        menu:
            extend ""
            "Должно быть, тебе было нелегко.":
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Love", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "Все было не так уж и плохо. . ."
            "Тебе это нравилось.":
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Statup("Obed", 80, 1)
                    $ YanaX.Statup("Obed", 90, 2)
                    $ YanaX.Statup("Inbt", 2000, 2)
                    ch_y "Да."
            "Звучит эротично.":
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "Да."
            ". . .":
                    $ YanaX.Statup("Obed", 90, 1)
                    $ YanaX.Statup("Inbt", 200, 1)
        $ YanaX.FaceChange("sly",1)
        ch_y "Сначала, конечно, я не понимала, что делаю."
        $ YanaX.FaceChange("sly",1,Eyes="side")
        ch_y "Как и не понимала, что они делали. . ."
        $ YanaX.FaceChange("sly",2,Eyes="side")
        ch_y "Я прикасалась только к тем местам, которые. . . вызвали приятные ощущения."
        ch_y "Как только я все поняла. . ."
        $ YanaX.FaceChange("sly",1)
        ch_y "Я научилась. . . получать -удовольствие- от зрителей. . ."
        menu:
            extend ""
            "Еще бы.":
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 2)
            "Ага, тебе это по душе.":
                    $ YanaX.Statup("Obed", 90, 2)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "Теперь - да. . ."
            "Здорово.":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Inbt", 200, 1)
            ". . .":
                    $ YanaX.Statup("Obed", 90, 1)
                    $ YanaX.Statup("Inbt", 200, 1)
        $ YanaX.FaceChange("sly",1,Eyes="side")
        ch_y "В конце концов, меня перестало волновать мнение других."
        $ YanaX.FaceChange("sly",1)
        ch_y "-если, конечно им это не -нравится-."

        $ Situation = YanaX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call SexMenu
        #end "if no relationship"
        return

# end Yana_Sexfriend//////////////////////////////////////////////////////////


# start Yana_Fuckbuddy//////////////////////////////////////////////////////////

label Yana_Fuckbuddy:
        if bg_current not in PersonalRooms:
                #if you aren't in someone's rooms, it tries again later
                call AskedMeet(YanaX,"sly","выглядит взволнованной. . .")
                return
        $ YanaX.DailyActions.append("relationship")
        $ YanaX.Lust = 60
        $ YanaX.Wet = 2
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        #change Yana's outfit to default
        $ Event_Queue = [0,0]
        if YanaX.Loc != bg_current:
                "[YanaX.Name] появляется перед вами."
        else:
                "[YanaX.Name] поворачивается к вам."
        call CleartheRoom(Ch_Focus,1,1) #removes all but the focus girl, so she stays when the other goes
        $ YanaX.Loc = bg_current
        call Shift_Focus(YanaX)
        call Set_The_Scene#(0)
#        call Display_Girl(YanaX)
        call Taboo_Level
        #$ YanaX.Event[10] += 1
        $ YanaX.Petnames.append("fuck buddy")
        $ YanaX.FaceChange("sly",1)
        ch_y "Помнишь, я рассказывала тебе историю о своем пребывании в Лимбо?"
        ch_y "О том, что случилось, когда я. . . выросла там?"
        menu:
            extend ""
            "Да?":
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "И когда я мастурбировала. . ."
            "Как ты все время мастурбировала?":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "Да."
            "Как ты любила дразнить бесов?":
                    $ YanaX.FaceChange("sly",2)
                    $ YanaX.Statup("Obed", 200, 4)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y ". . .да."
                    $ YanaX.FaceChange("sly",1)
            "Нет, а что случилось?":
                    $ YanaX.FaceChange("sly",1,Brows="angry")
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 1)
                    ch_y "Я мастурбировала."
                    ch_y "-и когда я это делала. . ."
            ". . .":
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "И когда я мастурбировала. . ."
        ch_y ". . . я использовала не -только- пальцы."
        menu:
            extend ""
            "А что еще?":
                    $ YanaX.Statup("Love", 80, 1)
                    $ YanaX.Statup("Inbt", 80, 2)
            "Ты позволила бесам трахнуть себя?":
                    $ YanaX.FaceChange("suprised",2,Brows="angry",Mouth="open")
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, -2)
                    ch_y "Что? Нет!"
                    $ YanaX.FaceChange("angry",1)
                    $ YanaX.Statup("Love", 70, -1)
                    $ YanaX.Statup("Love", 90, -2)
                    ch_y "Фу."
                    $ YanaX.FaceChange("sadside",2,Mouth="smirk")
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 4)
                    ch_y "Я позволяла им -только- смотреть."
                    $ YanaX.FaceChange("sly",1)
            ". . .":
                    $ YanaX.Statup("Inbt", 80, 2)
        ch_y "Я использовала. . ."
        $ YanaX.FaceChange("sadside",2,Mouth="smirk")
        ch_y "Рукоять моего меча."
        $ YanaX.FaceChange("sadside",1,Mouth="smirk")
        menu:
            extend ""
            "Духовного меча?":
                    $ YanaX.FaceChange("sadside",2,Mouth="smirk")
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y ". . . да."
            "Она же огромная!":
                    $ YanaX.FaceChange("smile",2,Brows="side")
                    $ YanaX.Statup("Obed", 200, 3)
                    ch_y "Ну-"
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y "-тогда она была не такой уж и большой. . ."
            "Так вот почему он имеет форму-":
                    $ YanaX.FaceChange("sadside",2,Mouth="smirk")
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 2)
                    $ YanaX.Statup("Inbt", 80, 2)

                    ch_y "-члена? . . да. . ."
                    $ YanaX.FaceChange("sadside",1)
                    ch_y "Мне кажется, это было сделано ненамеренно. . ."
                    $ YanaX.FaceChange("sly",1)
                    ch_y "-но и другого я исключать не могу. . ."
            "Как эротично.":
                    $ YanaX.FaceChange("sadside",2,Mouth="smirk")
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 70, 1)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 2)
                    ch_y ". . . да."
            ". . .":
                    $ YanaX.Statup("Inbt", 200, 2)
        $ YanaX.Sword = 1
        $ YanaX.FaceChange("sly",1)
        if "sword" not in YanaX.History:
                call Yana_Sword
        ch_y "После этого мы с ним. . . стали по-настоящему одним целым."
        $ YanaX.FaceChange("sadside",2,Mouth="smirk")
        if not Player.Male:
            ch_y "Ты бы хотела. . ."
        else:
            ch_y "Ты бы хотел. . ."
        $ YanaX.Statup("Inbt", 200, 3)
        $ YanaX.FaceChange("sly",2)
        ch_y "На это посмотреть?"

        #fix, remove when sex scenes are in
        "Сцены пока нет в игре."
        "Возможно, появится в версии 1.72 или выше? Но можете не переживать, она будет (что-то такое здесь было от Oni)."
        $ YanaX.FaceChange("sad",2)
        $ YanaX.AddWord(1,0,0,0,"swordredux") #history
        "А здесь Oni за это извиняется."
        $ YanaX.FaceChange("normal",1)
        $ YanaX.Sword = 0
        return
        #fix, remove when sex scenes are in

label Yana_Fuckbuddy_Redux:
        menu:
            extend ""
            "Конечно!":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 90, 1)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 5)
            "О, да!":
                    $ YanaX.FaceChange("smile",1)
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Obed", 200, 1)
                    $ YanaX.Statup("Inbt", 200, 4)
            "Ты можешь воспользоваться моим \"мечом\".":
                    $ YanaX.FaceChange("sly",1)
                    $ YanaX.Statup("Love", 90, 3)
                    $ YanaX.Statup("Obed", 80, 2)
                    $ YanaX.Statup("Obed", 200, 2)
                    ch_y "Это меня тоже устроит. . ."
            "Нет, спасибо.":
                    $ YanaX.FaceChange("sad",2)
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 80, 2)
                    $ YanaX.Statup("Obed", 200, 3)
                    $ YanaX.Statup("Inbt", 200, -2)
                    ch_y "Что ж, хорошо."
            ". . .":
                    $ YanaX.FaceChange("confused",1)
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 200, 1)
                    ch_y "Тогда в другой раз."
        $ YanaX.Sword = 1
        $ Situation = YanaX
        $ Player.AddWord(1,"interruption") #adds to Recent
#        call Yana_SexPrep              #she offers sex
        call SexMenu
        $ YanaX.FaceChange("sly",1)
        return


        return
# end Yana_Fuckbuddy//////////////////////////////////////////////////////////

# start Yana_Daddy//////////////////////////////////////////////////////////

#Not updated

label Yana_Daddy:       #Yana_Update
        $ YanaX.DailyActions.append("relationship")
        $ YanaX.DrainWord("asked meet")
        $ Player.DrainWord("meet girl")
        call Set_The_Scene
        $ Event_Queue = [0,0]
        if YanaX.Loc != bg_current:
                "[YanaX.Name] подходит к вам."
        $ YanaX.Loc = bg_current
        call Display_Girl(YanaX,DLoc=900)
        call Shift_Focus(YanaX)
        call CleartheRoom(YanaX)
        call Taboo_Level
        $ YanaX.FaceChange("sadside",1,Mouth="normal")
        ch_y "Я уже рассказывала о своем. . . необычном детстве. . ."
        if "belasco" not in YanaX.History:
                call Yana_Belasco
                #ch_y "With it, I tore my freedom from Belasco's hide."
        else:
                ch_y "Что много лет \"Беласко\" заменял мне отца."
                menu:
                    extend ""
                    "Я помню.":
                            $ YanaX.Statup("Love", 80, 2)
                            $ YanaX.FaceChange("smile",1)
                    "Да?":
                            pass
                    "Че?":
                            $ YanaX.Statup("Love", 80, -1)
                            $ YanaX.Statup("Obed", 80, 1)
                            $ YanaX.FaceChange("confused",1)
                            ch_y "Тебе нужно быть внимательней."
                    ". . .":
                            $ YanaX.Statup("Obed", 60, 1)
                            $ YanaX.FaceChange("sly",1)
                            ch_y "Что ж. . ."
        $ YanaX.FaceChange("sadside",1,Mouth="smirk")
        ch_y "Я просто хотела, чтобы ты знал. . ."
        ch_y "-с тобой мне гораздо комфортнее, чем с ним."
        menu:
            extend ""
            "Я рада." if not Player.Male:
                    $ YanaX.Statup("Love", 80, 2)
                    $ YanaX.FaceChange("smile",1)
            "Я рад." if Player.Male:
                    $ YanaX.Statup("Love", 80, 2)
                    $ YanaX.FaceChange("smile",1)
            "Это, наверное, здорово?":
                    $ YanaX.Statup("Love", 80, -1)
                    $ YanaX.Statup("Obed", 80, 1)
                    $ YanaX.FaceChange("confused",1)
            "Что?":
                    $ YanaX.Statup("Love", 80, -1)
                    $ YanaX.Statup("Obed", 80, 1)
                    $ YanaX.FaceChange("confused",1)
            ". . .":
                    $ YanaX.Statup("Obed", 60, 1)
                    $ YanaX.FaceChange("sly",1)
                    ch_y "Так вот. . ."
        if "Snowflake" not in YanaX.Pets:
                call Yana_Snowflake
                ch_y "А еще. . ."
        ch_y "-я подумала, что, возможно, я могла бы. . ."
        $ YanaX.FaceChange("sadside",2,Mouth="smirk")
        ch_y ". . . звать тебя. . ."
        $ YanaX.FaceChange("sad",2,Mouth="normal")
        if not Player.Male:
            ch_y "\"мамочкой?\""
        else:
            ch_y "\"папочкой?\""
        menu:
            extend ""
            "Хорошо.":
                $ YanaX.FaceChange("smile")
                $ YanaX.Statup("Love", 90, 20)
                $ YanaX.Statup("Obed", 60, 10)
                $ YanaX.Statup("Inbt", 80, 30)
                ch_y "Ох. . . я рада."
            "Зачем все это?":
                $ YanaX.FaceChange("bemused")
                ch_y "Мне просто хочется. . ."
                if YanaX.Love > YanaX.Obed and YanaX.Love > YanaX.Inbt:
                        if not Player.Male:
                            ch_y "Ведь ты очень добра ко мне. . ."
                        else:
                            ch_y "Ведь ты очень добр ко мне. . ."
                elif YanaX.Obed > YanaX.Inbt:
                        if not Player.Male:
                            ch_y "Ведь ты очень сильная. . ."
                        else:
                            ch_y "Ведь ты очень сильный. . ."
                else:
                        ch_y "Ведь мне весело с тобой. . ."

                menu:
                    extend ""
                    "Ладно, можешь звать меня так.":
                            $ YanaX.FaceChange("smile")
                            $ YanaX.Statup("Love", 90, 15)
                            $ YanaX.Statup("Obed", 60, 20)
                            $ YanaX.Statup("Inbt", 80, 25)
                            ch_y "Замечательно!"
                            $ YanaX.FaceChange("sly",2)
                            if not Player.Male:
                                ch_y " . . . мамочка."
                            else:
                                ch_y " . . . папочка."
                            $ YanaX.FaceChange("sly",1)
                            if not Player.Male:
                                $ YanaX.Petname = "мамочка"
                                $ YanaX.Petname_rod = "мамочки"
                                $ YanaX.Petname_dat = "мамочке"
                                $ YanaX.Petname_vin = "мамочку"
                                $ YanaX.Petname_tvo = "мамочкой"
                                $ YanaX.Petname_pre = "мамочке"
                            else:
                                $ YanaX.Petname = "папочка"
                                $ YanaX.Petname_rod = "папочки"
                                $ YanaX.Petname_dat = "папочке"
                                $ YanaX.Petname_vin = "папочку"
                                $ YanaX.Petname_tvo = "папочкой"
                                $ YanaX.Petname_pre = "папочке"
                    "Не могла бы ты не звать меня так, пожалуйста?":
                            $ YanaX.Statup("Love", 90, 5)
                            $ YanaX.Statup("Obed", 80, 40)
                            $ YanaX.Statup("Inbt", 80, 20)
                            $ YanaX.FaceChange("sad")
                            ch_y ". . ."
                            ch_y "Ah. . ."
                    "Тебе так не хватает отца, да?" if Player.Male:
                            $ YanaX.Statup("Love", 90, -15)
                            $ YanaX.Statup("Obed", 80, 45)
                            $ YanaX.Statup("Inbt", 70, 5)
                            $ YanaX.FaceChange("sly",2)
                            ch_y "\"Настоящий ад\" способен и не на такое. . ."
                            $ YanaX.FaceChange("sadside",1)
                    "Тебе так не хватает матери, да?" if not Player.Male:
                            $ YanaX.Statup("Love", 90, -15)
                            $ YanaX.Statup("Obed", 80, 45)
                            $ YanaX.Statup("Inbt", 70, 5)
                            $ YanaX.FaceChange("sly",2)
                            ch_y "\"Настоящий ад\" способен и не на такое. . ."
                            $ YanaX.FaceChange("sadside",1)

            "Тебе так не хватает отца, да?" if Player.Male:
                    $ YanaX.Statup("Love", 90, -15)
                    $ YanaX.Statup("Obed", 80, 45)
                    $ YanaX.Statup("Inbt", 70, 5)
                    $ YanaX.FaceChange("sly",2)
                    ch_y "\"Настоящий ад\" способен и не на такое. . ."
                    $ YanaX.FaceChange("sadside",1,Mouth="normal")
            "Тебе так не хватает матери, да?" if not Player.Male:
                    $ YanaX.Statup("Love", 90, -15)
                    $ YanaX.Statup("Obed", 80, 45)
                    $ YanaX.Statup("Inbt", 70, 5)
                    $ YanaX.FaceChange("sly",2)
                    ch_y "\"Настоящий ад\" способен и не на такое. . ."
                    $ YanaX.FaceChange("sadside",1,Mouth="normal")
        $ YanaX.Petnames.append("daddy")
        return

# end Yana_Daddy//////////////////////////////////////////////////////////



# Start Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Meet Yana / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gwen_Yana_Meet:
        # GwenX.Event[2] tracks number of girls she knows you're dating
        call CleartheRoom("All",0,1)
        $ GwenX.Loc = bg_current
        $ YanaX.Loc = bg_current
        call Shift_Focus(GwenX)
        $ GwenX.ArmPose = 2
        call Set_The_Scene
        $ GwenX.FaceChange("normal",1)
        $ YanaX.FaceChange("smile",1)
        ch_y "Привет, [YanaX.Petname]. . ."
        if YanaX.Petname in (Terms["master"], Terms["sir"]):
                $ GwenX.Statup("Obed", 60, 2)
                $ GwenX.Statup("Obed", 80, 5)
        $ GwenX.ArmPose = 1
        $ YanaX.ArmPose = 2
        hide Yana_Seated
        show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc)
        hide Gwen_Seated
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom -1
        $ GwenX.Hat = 0
        $ GwenX.FaceChange("confused",1,Eyes="side")
        ch_g "Итак, а кто это у нас тут такая. . ."
        $ GwenX.FaceChange("sly",1,Eyes="side")
        if YanaX.Demon:
                ch_g "-рогатая."
        else:
                ch_g "-холодная."
        $ YanaX.FaceChange("confused",1,Eyes="side")
        ch_y "Я - Ульяна Распутина."
        if YanaX.Name != "Ульяна":
                ch_y "Однако я предпочитаю, чтобы меня звали [YanaX.Name_tvo]."
        $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
        ch_g "А, да!"
        ch_y "А тебя я не узнаю."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "О. . . Я Гвен. Гвен Пул."
        ch_g "У тебя такой дикий акцент, ты говоришь как Флоренс Пью или типа того."
        ch_y "Я не знаю, кто это."
        ch_g "Ну, я думаю, она, наверное, нечасто бывала. . ."
        ch_g "В Лимбо, да?"
        ch_y "Ты знаешь о Лимбо?"
        ch_y "Ты бывала там?"
        ch_g "А, нет, но. . . мне и самой довелось немного попутешествовать по измерениям, [YanaX.Name]."
        ch_y "Ах, пожалуй, тогда это все объясняет."
        $ YanaX.FaceChange("sly",1,Eyes="side")
        ch_y "Так, а какие у тебя способности?"
        ch_g "Да так, всякие \"мета\" штучки. Я понимаю, что я в игре и здешние правила можно нарушать."
        ch_y "Да-да, вся жизнь - игра."
        $ GwenX.FaceChange("surprised",1,Eyes="side")
        ch_g "Правда? Ты знаешь, что мы в -эро игре-?"
        $ YanaX.FaceChange("perplexed",1,Eyes="side")
        ch_y "Что?"
        $ YanaX.FaceChange("perplexed",1)
        ch_y "Что ты подразумеваешь под \"эро игрой?\""
        menu:
            extend ""
            "[GwenX.Name] думает, что мы в видеоигре.":
                    $ GwenX.FaceChange("sly",1)
                    $ GwenX.Statup("Love", 70, 2)
                    $ GwenX.Statup("Love", 90, 2)
                    $ GwenX.Statup("Obed", 80, 2)
                    ch_y "Ах, какая ненормальная девушка. . ."
            "Не обращай на нее внимания.":
                    $ GwenX.FaceChange("angry",1)
                    $ GwenX.Statup("Love", 90, -2)
                    $ GwenX.Statup("Obed", 70, 2)
                    ch_y "Ах, что ж, ладно, какая ненормальная девушка. . ."
            "Она ненормальная.":
                    $ GwenX.FaceChange("angry",2,Mouth="open")
                    $ GwenX.Statup("Love", 70, -2)
                    $ GwenX.Statup("Love", 90, -2)
            ". . .":
                    ch_g ". . ."
        ch_g "Эй!"
        $ GwenX.FaceChange("angry",1,Eyes="side")
        $ GwenX.Statup("Obed", 80, 3)
        $ GwenX.Statup("Inbt", 70, 3)
        ch_g "Я не ненормальная, я просто лучше информирована. . ."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_g "Там, откуда я родом, ваш мир - выдумка."
        $ YanaX.FaceChange("bemused",1,Eyes="side")
        ch_y "Я тоже видела, как искривляются время и пространство."
        ch_y "Я тоже оказывалась в плену там, где не хотела быть."
        ch_g "Ага."
        ch_y "Хочешь, чтобы я отправила тебя домой?"
        $ GwenX.FaceChange("surprised",1,Eyes="side")
        ch_g "А ты можешь?"
        if ApprovalCheck(GwenX, 1500):
                ch_g ". . ."
                ch_g "Неее, думаю, пока мне и здесь хорошо."
                ch_y "Ладно, это здорово."
        else:
                $ GwenX.FaceChange("surprised",1,Eyes="side",Mouth="open")
                ch_g "Правда-правда? Да, я хочу домой!"
                ch_y "Я могу попробовать. . ."
                $ YanaX.FaceChange("angry",1)
                $ GwenX.FaceChange("smile",1,Eyes="closed")
                "Под [GwenX.XName_tvo] появляется ступенчатый диск, но быстро гаснет."
                "Похоже, ничего не произошло."
                $ YanaX.FaceChange("sadside",1)
                ch_y "Это очень странно. Тебя словно здесь на самом деле нет."
                $ GwenX.FaceChange("smile",1)
                ch_g "Я часто это слышу."
                $ YanaX.FaceChange("perplexed",1,Eyes="side")
                ch_y "Ах. . ."
        $ YanaX.FaceChange("bemused",1,Eyes="side")
        $ GwenX.FaceChange("smile",1,Eyes="side")
        ch_y "Тем не менее, мне приятно познакомиться с тобой."
        ch_g "Ага, надеюсь, мы сможем поладить."
        $ GwenX.FaceChange("smile",1,Eyes="side")
        if not Player.Male:
            ch_g "Я полагаю, вы уже с ней знакомы? . ."
        else:
            ch_g "Я полагаю, вы уже с ним знакомы? . ."
        if YanaX in Player.Harem:
                $ YanaX.FaceChange("sly",1)
                $ GwenX.FaceChange("surprised",2,Eyes="side",Mouth="open")
                $ YanaX.Statup("Obed", 80, 1)
                $ YanaX.Statup("Inbt", 80, 2)
                ch_y "Да, знакомы, и -очень- хорошо. . ."
                $ GwenX.FaceChange("surprised",1,Eyes ="side")
                if GwenX.Event[2] > 1:
                        #if yana heard you were dating two+ girls
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 1)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "И ты тоже? . ."
                        $ GwenX.Statup("Obed", 50, 2)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_y "О. . . Да."
                elif GwenX.Event[2]:
                        #if yana heard you were dating someone else
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Inbt", 50, 3)
                        $ GwenX.Statup("Inbt", 80, 3)
                        ch_g "И ты тоже? . ."
                        $ GwenX.Statup("Obed", 50, 4)
                        $ GwenX.Statup("Obed", 80, 3)
                        ch_y "Хех. . . Да."
                else:
                        $ GwenX.Statup("Love", 90, -2)
                        $ GwenX.Statup("Obed", 60, 2)
                        $ GwenX.Statup("Obed", 80, 2)
                        $ GwenX.FaceChange("sly",1)
                        ch_g "О. . . круто, круто. . ."
                $ GwenX.Event[2] += 1
        elif YanaX.Petname in ("хозяин", "господин", "хозяйка", "госпожа"):
                $ YanaX.FaceChange("sad",1,Eyes="leftside",Mouth="smirk")
                if not Player.Male:
                    ch_y "Да, она моя. . . [YanaX.Petname]. . ."
                else:
                    ch_y "Да, он мой. . . [YanaX.Petname]. . ."
        elif not ApprovalCheck(YanaX, 500, "L"):
                $ YanaX.FaceChange("normal",0)
                if not Player.Male:
                    ch_y "Да, она. . . помогает мне держаться. . ."
                else:
                    ch_y "Да, он. . . помогает мне держаться. . ."
        else:
                $ YanaX.FaceChange("sad",1,Eyes="leftside")
                if not Player.Male:
                    ch_y "Да, она. . . очень веселая. . ."
                else:
                    ch_y "Да, он. . . очень веселый. . ."
        $ GwenX.FaceChange("normal",1,Eyes="side")
        $ YanaX.FaceChange("smile",1,Eyes="side",Mouth="open")
        ch_g "Ладно, как-нибудь еще увидимся."
        ch_y "Да, в этом я уверена."
        $ GwenX.FaceChange("normal",1)
        $ YanaX.FaceChange("smile",1)
        $ YanaX.GirlLikeUp(GwenX,100)
        $ GwenX.GirlLikeUp(YanaX,100)
        $ GwenX.DrainWord("Yana",0,0,0,1)
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc):
                xzoom 1
        return

# End Gwen Meet Yana / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Character Meet Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Yana_Switch:
        #scene for after a shift in gender.
        call Set_The_Scene
        if "switched" in YanaX.History:
                jump Yana_Switch2
        $ YanaX.FaceChange("confused", 1)
        ch_y "Хмммм. . ."
        ch_y ". . ."
        $ YanaX.FaceChange("sly", 1)
        if not Player.Male:
            ch_y "Знаешь, ты так похожа на [Player.XName_vin]. . ."
        else:
            ch_y "Знаешь, ты так похож на [Player.XName_vin]. . ."
        ch_y "У меня тоже есть брат-близнец, хотя мы не очень похожи."
        if not Player.Male:
            ch_y "[Player.XName] же твой брат?"
        else:
            ch_y "[Player.XName] же твоя сестра?"
        menu:
            extend ""
            "Это я, [Player.XName].":
                    $ YanaX.FaceChange("smile", 1)
                    ch_y "Ох!"
                    $ YanaX.AddWord(1,"switch") #recent

            "Нет.":
                if Player.Male:
                    ch_y "Хм. Вы очень похожи."
                else:
                    ch_y "Хм. Вы очень похожи, но ты, пожалуй, сексуальнее."
            "Возможно?":
                    ch_y "\"Возможно?\" . ."
                    ch_y "Понимаю. У меня тоже \"возможно\" есть сестра."

        if "switch" not in YanaX.RecentActions:
                    $ YanaX.FaceChange("confused", 1)
                    ch_y ". . . секунду!"
                    $ YanaX.FaceChange("surprised", 1,Mouth= "open")
                    ch_y "Ты и -есть- [Player.XName]!"
                    $ YanaX.AddWord(1,"switch") #recent
                    menu:
                        extend ""
                        "Ага, это я, [Player.XName].":
                                $ YanaX.FaceChange("smile", 1)
                                $ YanaX.Statup("Love", 90, 1)
                                $ YanaX.Statup("Obed", 70, 1)
                                ch_y "Тебе удалось меня ненадолго обмануть!"
                                $ YanaX.FaceChange("sly", 1)
                        "Нет.":
                                $ YanaX.FaceChange("bemused", 1)
                                $ YanaX.Statup("Obed", 60, 1)
                                $ YanaX.Statup("Obed", 70, 1)
                                ch_y "Да-да."
                        "Возможно?":
                                $ YanaX.FaceChange("sly", 1)
                                $ YanaX.Statup("Love", 80, 1)
                                $ YanaX.Statup("Obed", 70, 1)
                                $ YanaX.Statup("Inbt", 60, 1)
                                ch_y "Я тебя раскусила."
                    ch_y "К чему это все?"
                    menu:
                        extend ""
                        "Извини, хотелось пошутить.":
                                $ YanaX.FaceChange("sly", 1)
                                $ YanaX.Statup("Love", 70, 1)
                        "Молодец, тебя не обманешь.":
                                $ YanaX.FaceChange("sly", 1)
                                $ YanaX.Statup("Obed", 70, 1)
                                $ YanaX.Statup("Inbt", 80, 1)
                                ch_y "Конечно."
                        "Хех.":
                                $ YanaX.FaceChange("sly", 1,Eyes="side")
                                $ YanaX.Statup("Love", 70, 1)
                                $ YanaX.Statup("Love", 90, 1)
                                $ YanaX.Statup("Inbt", 70, 1)
                                ch_y "Как мило. . ."
#                    ch_y "Anyway, I get it. . ."
        #end "tried to lie"
        $ YanaX.FaceChange("smile", 1)
        ch_y "Это какое-то колдовство или что-то похожее?"
        menu:
            extend ""
            "Просто по приколу захотелось сменить облик.":
                    $ YanaX.Statup("Inbt", 70, 1)
                    $ YanaX.FaceChange("sly", 1)
                    ch_y "Понимаю, у всех такое бывает."
            "Я так себя сейчас ощущаю.":
                    ch_y "Ладно, у меня с этим никаких проблем."
            "Колдовство не виновато, я даже не знаю, почему мне захотелось сменить облик.":
                    ch_y "Колдовство лучше всего все объясняет!"

        if [Player.Name] != [Player.XName]:
                ch_p "А еще меня теперь зовут [Player.Name]."
                ch_y "[Player.Name], что ж, хорошо."

        if YanaX.SEXP >= 15:
                $ YanaX.FaceChange("sly", 1)
                ch_y "Я тебе все еще нравлюсь?"
                menu:
                    extend ""
                    "Конечно!":
#                            $ YanaX.FaceChange("normal", 1)
                            $ YanaX.Statup("Love", 70, 2)
                            $ YanaX.Statup("Love", 90, 1)
                            ch_y "Замечательно."
                    "Не особо.":
                            $ YanaX.FaceChange("sad", 1)
                            $ YanaX.Statup("Love", 80, -2)
                            $ YanaX.Statup("Obed", 60, 2)
                            $ YanaX.Statup("Obed", 80, 2)
                            ch_y ". . . жаль. . ."
                    "А ты как думаешь?":
                            $ YanaX.FaceChange("sly", 1)
                            $ YanaX.Statup("Obed", 70, 1)
                            $ YanaX.Statup("Inbt", 70, 1)
                            ch_y "Рада слышать."

        if not Player.Male and YanaX.Les > 5:
                $ YanaX.FaceChange("sly", 1)
                ch_y "Это может быть интересно. . ."
#        if ApprovalCheck(YanaX, 1200):
#                ch_y "I guess we could give this a try. . ."
#                $ YanaX.AddWord(1,0,0,0,"girltalk") #history
#        else:
#                $ YanaX.FaceChange("normal", 1,Eyes="side")
        ch_y "В общем, еще увидимся. . ."
        $ YanaX.AddWord(1,0,0,0,"girltalk") #history
        $ YanaX.Traits.remove("switchcheck")
        $ YanaX.AddWord(1,0,0,0,"switched") #history
        return

label Yana_Switch2:
        #when you switch for a 2+ time
        $ YanaX.FaceChange("smile", 1)
        if not Player.Male:
            ch_w "Ах, [Player.Name], ты вернула свой прежний облик."
        else:
            ch_w "Ах, [Player.Name], ты вернул свой прежний облик."
        $ YanaX.Traits.remove("switchcheck")
        $ YanaX.History.remove("switched")
        $ YanaX.AddWord(1,0,0,0,"switched2") #history
        return

# End Sex Change Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Yana_Girltalk(Auto=0,Other=0):
        # if Auto Yana starts the conversation, otherwise it assumes that you asked about it. . .
        if Player.Male or "girltalk" in YanaX.History:
                return
        if "nogirls" in YanaX.History:
                jump Yana_Girltalk_Redux
        $ YanaX.FaceChange("sly", 1)
        if Auto:
                ch_y "[Player.Name]. . ."
#                ch_y "I am curious, are you attracted to me?"
#                ch_y "Sexually, I mean."
#        else:
#                ch_y "Hey, I just gotta ask, are you into me?"
        ch_y "Мне любопытно, я тебе нравлюсь?"
        ch_y "В сексуальном плане."
        menu:
            extend ""
            "Да?":
                    $ YanaX.FaceChange("sly", 1)
                    $ YanaX.Statup("Love", 70, 2)
                    $ YanaX.Statup("Love", 90, 2)
                    $ YanaX.Statup("Obed", 70, 1)
                    ch_y "Это. . . хорошо. . ."
            "Возможно?":
                    $ YanaX.FaceChange("confused", 1)
                    $ YanaX.Statup("Love", 70, 1)
                    $ YanaX.Statup("Obed", 80, 2)
                    $ YanaX.Statup("Inbt", 80, 2)
                    ch_y "Я понимаю. . ."
                    ch_y "Если определишься, дай мне знать."
            "Не особо.":
                    $ YanaX.Statup("Love", 90, -1)
                    $ YanaX.Statup("Obed", 60, 2)
                    $ YanaX.Statup("Obed", 80, 2)
                    if ApprovalCheck(YanaX, 1200):
                            $ YanaX.FaceChange("sad", 1)
                            ch_y "Жаль."
                            $ YanaX.FaceChange("sly", 1)
                    else:
                            $ YanaX.FaceChange("sly", 1)
                            ch_y "Что ж, жаль."
#                    ch_y "I get it though. . ."
        $ YanaX.FaceChange("sly", 1)
        if not YanaX.Les:
                ch_y "У меня нет большого опыта в этом деле. . ."
#                $ YanaX.FaceChange("sly", 2,Eyes="side")
#                ch_y "-I haven't been with many people. . ."
        if not ApprovalCheck(YanaX, 900) and not ApprovalCheck(YanaX, 600, "L") and not YanaX.Les:
                ch_y "Я. . . не уверена, хочу ли я подобного. . ."
                $ YanaX.AddWord(1,0,0,0,"nogirls") #history
                call Girltalk_Check(YanaX)
                return

        ch_y "Возможно, мне даже понравится. . ."
        $ YanaX.AddWord(1,0,0,0,"girltalk") #history
        call Girltalk_Check(YanaX)
        return

label Yana_Girltalk_Redux(Other=0):
        #gets called if she refused the first time, until she stops refusing
        if ApprovalCheck(YanaX, 1000) or ApprovalCheck(YanaX, 600, "L"):
                $ YanaX.FaceChange("sly", 1)
                if Other in TotalGirls and "nogirls" in Other.History:
                        ch_y "Хммм. . ."
                ch_y "Пожалуй, мне это не повредит?"
                $ YanaX.DrainWord("nogirls",0,0,0,1) #history
                $ YanaX.AddWord(1,0,0,0,"girltalk") #history
        elif "nogirls" not in YanaX.History:
                $ YanaX.AddWord(1,0,0,0,"nogirls") #history
                ch_y "Хмм. . . я не уверена. . ."
        elif "nogirls" in YanaX.DailyActions:
                $ YanaX.FaceChange("angry", 1)
                if YanaX.Forced:
                        #if Forced, she will just go with it anyway
                        if "nogirls" not in YanaX.RecentActions:
                                $ YanaX.Statup("Love", 80, -2)
                                $ YanaX.Statup("Obed", 80, 2)
                                $ YanaX.AddWord(1,"nogirls",0,0,0) #recent
                        return
                ch_y "Не спрашивай меня об этом больше."
        else:
                $ YanaX.Statup("Inbt", 50, 2)
                ch_y "Я не думаю, что из этого что-то выйдет. . ."
                $ YanaX.AddWord(1,0,"nogirls",0,0) #daily
        return

# End Are you into me Dialogues / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Yana_69_Intro:
        return #fix, remove when she has a 69 pose.
        if "69" in YanaX.History:
                return
        if Trigger == "lick pussy" and YanaX.LickP >= 3:
                if YanaX.Blow or (ApprovalCheck(YanaX, 1300) and YanaX.SeenPeen):
                        #if licking pussy but have gotten blowjob
                        $ YanaX.AddWord(1,0,0,0,"69") #history
                        ch_y "Итак. . . раз уж ты мне помогаешь. . ."
                        "Она прижимает вас к земле и забирается на вас сверху."
                        if "cockout" not in Player.RecentActions:
                                $ Player.RecentActions.append("cockout")
                                "Она вытаскивает ваш член и начинает его сосать."
                        else:
                                "Она обнажает вашу киску и начинает ее лизать."
                        $ YanaX.Pose = "69"
                        call Yana_BJ_Launch
                        if not Player.Male:
                            ch_y "Не могла бы ты, эм. . ."
                        else:
                            ch_y "Не мог бы ты, эм. . ."
                        menu:
                            extend ""
                            "Приступить к работе.":
                                    $ Trigger2 = "lick pussy"
                                    $ YanaX.Statup("Love", 95, 3)
                                    $ YanaX.Statup("Inbt", 70, 2)
                                    $ YanaX.Statup("Inbt", 90, 1)
                                    ch_y "Хех, спасибо."
                            "Расслабиться, оставив ее киску без внимания.":
                                    $ YanaX.Statup("Love", 80, -8)
                                    $ YanaX.Statup("Obed", 80, 3)
                                    $ YanaX.Statup("Obed", 90, 1)
                                    $ YanaX.Statup("Inbt", 70, -1)
                                    ch_y "Ах, жаль."
                        $ Situation = "69"
                        call SexAct("blow") # call Yana_SexAct("blow")
                        $ renpy.pop_call() #causes it to skip past the Escalation
                        $ renpy.pop_call() #causes it to skip past the last activity
                return
        elif Trigger == "blow" and YanaX.Blow >= 3:
                #if licked pussy
                $ YanaX.AddWord(1,0,0,0,"69") #history
                ch_y "Слушай, эм. . . раз я уже здесь. . ."
                "Она прижимает вас к земле и забирается на вас сверху."
                $ YanaX.Pose = "69"
                call Yana_BJ_Launch
                if not Player.Male:
                    ch_y "Не могла бы ты, эм. . ."
                else:
                    ch_y "Не мог бы ты, эм. . ."
                ch_y "-отплатить мне?"
                menu:
                    extend ""
                    "Приступить к работе.":
                            $ Trigger2 = "lick pussy"
                            $ YanaX.Statup("Love", 95, 3)
                            $ YanaX.Statup("Inbt", 70, 2)
                            $ YanaX.Statup("Inbt", 90, 1)
                            ch_y "Хех, спасибо."
                            if not YanaX.LickP:
                                $ YanaX.LickP += 1
                    "Расслабиться, оставив ее киску без внимания.":
                            $ YanaX.Statup("Love", 80, -5)
                            $ YanaX.Statup("Obed", 80, 3)
                            $ YanaX.Statup("Obed", 90, 1)
                            $ YanaX.Statup("Inbt", 70, -1)
                            ch_y "Ах, жаль."
                #returns to BJ already in progress
                return
        else:
                return
        return
