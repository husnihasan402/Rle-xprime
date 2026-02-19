# Basic character Sprites

image Yana_Sprite:
    LiveComposite(
        (600,1250),       #550,950
        (0,0), "images/YanaSprite/Yana_Sprite_Shadow.png",

#        (0,0), "images/YanaSprite/Yana_Sprite_Arm.png",
#            #back arm

#        (0,0), ConditionSwitch(
#            #Back Arm layer
#            "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Over_Purple_Back.png",
#            "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Chest_Mesh_Arm.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
                #Tail
                "YanaX.Demon","images/YanaSprite/Yana_Sprite_Tail.png",
                "True", Null(),
                ),
        (100,72), "Yana_Sprite_HairBack", #(15,-80)
        (0,0), ConditionSwitch(
            #body
#            "YanaX.ArmPose != 1", "images/YanaSprite/Yana_Sprite_Body2.png",
            "renpy.showing('Yana_HJ_Animation') or renpy.showing('Yana_Finger_Animation')", "images/YanaSprite/Yana_Sprite_Body_Hand.png",
            "YanaX.Pubes", "images/YanaSprite/Yana_Sprite_Body_Pubes.png",
            "True", "images/YanaSprite/Yana_Sprite_Body.png",
            ),

        (0,0), ConditionSwitch(
            #Over arm
            "YanaX.Uptop and YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Over_Shirt_Back.png",
            "YanaX.Uptop and YanaX.Over == 'tracksuit'", "images/YanaSprite/Yana_Sprite_Over_Track_Back.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #stockings
            "YanaX.Hose == 'socks'", "images/YanaSprite/Yana_Sprite_Hose_Socks.png",
            "YanaX.Hose == 'stockings'", "images/YanaSprite/Yana_Sprite_Hose_Stockings.png",
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSprite/Yana_Sprite_Hose_StockingsGarter.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaSprite/Yana_Sprite_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
#            "not YanaX.Panties", Null(),
            "YanaX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not YanaX.Legs or YanaX.Upskirt or YanaX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "YanaX.Panties == 'bikini bottoms'", "images/YanaSprite/Yana_Sprite_Panties_Bikini_Down.png",
                            "YanaX.Panties == 'lace panties'", "images/YanaSprite/Yana_Sprite_Panties_Lace_Down.png",
                            "YanaX.Panties and YanaX.Wet", "images/YanaSprite/Yana_Sprite_Panties_White_DownW.png",
                            "YanaX.Panties", "images/YanaSprite/Yana_Sprite_Panties_White_Down.png",
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                #if she's not wet
                "YanaX.Panties == 'bikini bottoms'", "images/YanaSprite/Yana_Sprite_Panties_Bikini.png",
                "YanaX.Panties == 'lace panties'", "images/YanaSprite/Yana_Sprite_Panties_Lace.png",
                "YanaX.Panties and YanaX.Wet", "images/YanaSprite/Yana_Sprite_Panties_WhiteW.png",
                "YanaX.Panties", "images/YanaSprite/Yana_Sprite_Panties_White.png",
                "True", Null(),
                ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "YanaX.Hose == 'pantyhose' and (not YanaX.PantiesDown or not YanaX.Panties)", "images/YanaSprite/Yana_Sprite_Hose_Pantyhose.png",
            "YanaX.Hose == 'tights' and YanaX.Wet and (not YanaX.PantiesDown or not YanaX.Panties)", "images/YanaSprite/Yana_Sprite_Hose_TightsW.png",
            "YanaX.Hose == 'tights' and (not YanaX.PantiesDown or not YanaX.Panties)", "images/YanaSprite/Yana_Sprite_Hose_Tights.png",
            "YanaX.Hose == 'ripped pantyhose' and (not YanaX.PantiesDown or not YanaX.Panties)", "images/YanaSprite/Yana_Sprite_Hose_Pantyhose_Holed.png",
            "YanaX.Hose == 'ripped tights' and (not YanaX.PantiesDown or not YanaX.Panties)", "images/YanaSprite/Yana_Sprite_Hose_Tights_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Chest layer
            "YanaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Chest_Bikini_Up.png",
                    "YanaX.Chest == 'sports bra'", "images/YanaSprite/Yana_Sprite_Chest_Sports_Up.png",
#                    "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Chest_Lace_Up.png",
                    "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Chest_Bikini.png",
            "YanaX.Chest == 'sports bra'", "images/YanaSprite/Yana_Sprite_Chest_Sports.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Chest_Lace.png",
            "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Chest_Bra.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Boots/Shoes
            "YanaX.Boots == 'boots'", "images/YanaSprite/Yana_Sprite_Boots.png",
#            "YanaX.Boots == 'sneaks'", "images/YanaSprite/Yana_Sprite_Boots_Sneaks.png",
            "True", Null(),
            ),

        (215,560), ConditionSwitch(    #275,560
            #Personal Wetness
            "not YanaX.Wet", Null(),
            "YanaX.Wet == 1 or (YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt' and not YanaX.Upskirt)", ConditionSwitch( #Wet = 1 "Wet_Drip", #
                    "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
                    "YanaX.Panties and not YanaX.PantiesDown", Null(),
#                    "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts')", AlphaMask("Wet_Drip","Yana_Drip_MaskP"),
#                    "YanaX.Panties and YanaX.PantiesDown", AlphaMask("Wet_Drip","Yana_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Yana_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+  "Wet_Drip2", #
#                    "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and YanaX.Upskirt", AlphaMask("Wet_Drip2","Yana_Drip_MaskP"),
#                    "YanaX.Panties and YanaX.PantiesDown", AlphaMask("Wet_Drip2","Yana_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip2","Yana_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (215,560), ConditionSwitch(    #275,560
            #Spunk
            "('in' not in YanaX.Spunk and 'anal' not in YanaX.Spunk) or not Player.Male", Null(),
            "YanaX.Panties and not YanaX.PantiesDown", "Spunk_Drip", #ConditionSwitch( #Wet = 1
            "YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt' and not YanaX.Upskirt", ConditionSwitch( #Wet = 1 "Spunk_Drip", #
#                    "YanaX.Panties and YanaX.PantiesDown", AlphaMask("Spunk_Drip","Yana_Drip_MaskP"),
#                    "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and YanaX.Upskirt", AlphaMask("Spunk_Drip","Yana_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Yana_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+  "Spunk_Drip2", #
#                    "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and YanaX.Upskirt", AlphaMask("Spunk_Drip2","Yana_Drip_MaskP"),
#                    "YanaX.Panties and YanaX.PantiesDown", AlphaMask("Spunk_Drip2","Yana_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Yana_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),

        (0,0), ConditionSwitch(
            #Water effect
##            "YanaX.Water and YanaX.ArmPose == 1", "images/YanaSprite/Yana_Sprite_Water1.png",
            "YanaX.Water", "images/YanaSprite/Yana_Sprite_Water.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness  over
            "not YanaX.Wet", Null(),
            "YanaX.Panties and not YanaX.PantiesDown", Null(),
            "YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt' and not YanaX.Upskirt", Null(),
            "True", "images/YanaSprite/Yana_Sprite_Wet.png", #ConditionSwitch( #Wet = 2+
            ),
        (0,0), ConditionSwitch(
            #Spunk over
            "('in' not in YanaX.Spunk and 'anal' not in YanaX.Spunk) or not Player.Male", Null(),
            "YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt' and not YanaX.Upskirt", Null(),
            "YanaX.Panties and not YanaX.PantiesDown", Null(),
            "True", "images/YanaSprite/Yana_Sprite_Spunk_Pussy.png",
            ),

        (0,0), ConditionSwitch(
            #pants
#            "not YanaX.Legs", Null(),
            "YanaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
#                        "YanaX.Legs == 'shorts' and YanaX.Wet > 1", "images/YanaSprite/Yana_Sprite_Legs_Shorts_Down_Wet.png",
                        "YanaX.Legs == 'skirt'", "images/YanaSprite/Yana_Sprite_Legs_Skirt_Up.png",
                        "YanaX.Legs == 'shorts'", "images/YanaSprite/Yana_Sprite_Legs_Shorts_Down.png",
#                        "YanaX.Legs == 'pants' and YanaX.Wet > 1", "images/YanaSprite/Yana_Sprite_Legs_Pants_Down_Wet.png",
                        "YanaX.Legs == 'pants'", "images/YanaSprite/Yana_Sprite_Legs_Pants_Down.png",
                        "True", Null(),
                        ),
            "YanaX.Legs == 'skirt'", "images/YanaSprite/Yana_Sprite_Legs_Skirt.png",
#            "YanaX.Legs == 'shorts' and YanaX.Wet > 1", "images/YanaSprite/Yana_Sprite_Legs_Shorts_Wet.png",
            "YanaX.Legs == 'shorts'", "images/YanaSprite/Yana_Sprite_Legs_Shorts.png",
            "YanaX.Legs == 'pants' and YanaX.Wet > 1", "images/YanaSprite/Yana_Sprite_Legs_Pants_Wet.png",
            "YanaX.Legs == 'pants'", "images/YanaSprite/Yana_Sprite_Legs_Pants.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nude lower piercings
            "not YanaX.Pierce", Null(),
            "YanaX.Legs == 'skirt' and not YanaX.Upskirt", Null(),
            "YanaX.Over == 'towel' and not YanaX.Upskirt", Null(),
            "YanaX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Legs == 'shorts' and not YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_Black.png",
                    "YanaX.Legs == 'pants' and YanaX.Wet > 1 and not YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_YellowB.png",
                    "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_Yellow.png",

                    "YanaX.Panties and YanaX.PantiesDown", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R.png",
                    "YanaX.Hose == 'pantyhose'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_Lace.png",
                    "YanaX.Hose == 'tights'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_Black.png",

#                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_White.png",
                    "YanaX.Panties == 'lace panties'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_Lace.png",
                    "YanaX.Panties", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R_White.png",

                    "True", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_R.png",
                    ),

            "YanaX.Legs == 'shorts' and not YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_Black.png",
            "YanaX.Legs == 'pants' and YanaX.Wet > 1 and not YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_YellowB.png",
            "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_Yellow.png",

            "YanaX.Panties and YanaX.PantiesDown", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B.png",
            "YanaX.Hose == 'pantyhose'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_Lace.png",
            "YanaX.Hose == 'tights'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_Black.png",

#            "YanaX.Panties == 'bikini bottoms'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_White.png",
            "YanaX.Panties == 'lace panties'", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_Lace.png",
            "YanaX.Panties", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B_White.png",

            "True", "images/YanaSprite/Yana_Sprite_Pierce_Pussy_B.png",
            ),

        (0,0), ConditionSwitch(
            #Necklaces
#            "YanaX.Neck == 'scarf'", "images/YanaSprite/Yana_Sprite_Neck_Scarf.png",
            "YanaX.Neck", "images/YanaSprite/Yana_Sprite_Neck_Choker.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "YanaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Over == 'tshirt'", "images/YanaSprite/Yana_Sprite_Over_Tshirt_Up.png",
                    "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Over_Shirt_Up.png",
                    "YanaX.Over == 'tracksuit'", "images/YanaSprite/Yana_Sprite_Over_Track_Up.png",
                    "YanaX.Over == 'towel' and YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Over_Towel_Up.png",
                    "YanaX.Over == 'towel'", "images/YanaSprite/Yana_Sprite_Over_Towel_Uptop.png",
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "YanaX.Over == 'tshirt'", "images/YanaSprite/Yana_Sprite_Over_Tshirt.png",
            "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Over_Shirt.png",
            "YanaX.Over == 'tracksuit'", "images/YanaSprite/Yana_Sprite_Over_Track.png",
            "YanaX.Over == 'towel' and YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Over_Towel_Upskirt.png",
            "YanaX.Over == 'towel'", "images/YanaSprite/Yana_Sprite_Over_Towel.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra over
            "YanaX.Uptop and YanaX.Chest == 'sports bra'", "images/YanaSprite/Yana_Sprite_Chest_Sports_Over.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Nipples
            #Only does this if she has piercings, has no tops, or has her top up
            "not YanaX.Pierce", Null(),
            "YanaX.Pierce == 'ring'", ConditionSwitch(
                    "YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R.png",

                    "YanaX.Over == 'towel'", Null(),
                    "YanaX.Over == 'tshirt'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_Black.png",
                    "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_White.png",
                    "YanaX.Over == 'tracksuit'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_Sport.png",

                    "YanaX.Chest == 'sports bra'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_Sport.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_Lace.png",
#                    "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_WhiteB.png",
#                    "YanaX.Chest == 'bra'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_WhiteB.png",
                    "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R_WhiteB.png",

                    "True", "images/YanaSprite/Yana_Sprite_Pierce_Tits_R.png",
                    ),
#            "YanaX.Pierce == 'barbell'", ConditionSwitch(
            "YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B.png",

            "YanaX.Over == 'towel'", Null(),
            "YanaX.Over == 'tshirt'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_Black.png",
            "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_White.png",
            "YanaX.Over == 'tracksuit'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_Sport.png",

            "YanaX.Chest == 'sports bra'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_Sport.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_Lace.png",
#            "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_WhiteB.png",
#            "YanaX.Chest == 'bra'", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_WhiteB.png",
            "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B_WhiteB.png",

            "True", "images/YanaSprite/Yana_Sprite_Pierce_Tits_B.png",
            ),

        (0,0), ConditionSwitch(
            #Sword
            "YanaX.Sword > 1", "Yana_Sprite_Sword",
            "YanaX.Sword", "images/YanaSprite/Yana_Sprite_Sword.png",
            "True", Null(),
            ),

#        (0,0), "images/YanaSprite/Yana_Sprite_Arm_Over.png", #53,-45

        (0,0), ConditionSwitch(
            #Hand over
            "renpy.showing('Yana_HJ_Animation') or renpy.showing('Yana_Finger_Animation')", Null(),
            "True", "images/YanaSprite/Yana_Sprite_Arm_Over.png",
            ),
        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

#        (0,0), "images/YanaSprite/Yana_Sprite_Headref.png", #53,-45
        (100,35), "Yana_Sprite_Head", #(95,25)




#        (0,0), ConditionSwitch(
#            #hand spunk
#            "YanaX.ArmPose == 2 or 'hand' not in YanaX.Spunk", Null(),
#            "True", "images/YanaSprite/Yana_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not YanaX.Held or YanaX.ArmPose != 2", Null(),
#            "YanaX.ArmPose == 2 and YanaX.Held == 'phone'", "images/YanaSprite/Yana_held_phone.png",
#            "YanaX.ArmPose == 2 and YanaX.Held == 'dildo'", "images/YanaSprite/Yana_held_dildo.png",
#            "YanaX.ArmPose == 2 and YanaX.Held == 'vibrator'", "images/YanaSprite/Yana_held_vibrator.png",
#            "YanaX.ArmPose == 2 and YanaX.Held == 'panties'", "images/YanaSprite/Yana_held_panties.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using RogueX.Offhand actions while lead
            "Trigger == 'lesbian' or not YanaX.Offhand",Null(),# or Ch_Focus is not YanaX", Null(),
            "YanaX.Offhand == 'fondle pussy' and Trigger != 'sex' and YanaX.Lust >= 70", "GirlFingerPussy_Yana",
            "YanaX.Offhand == 'fondle pussy'", "GirlGropePussy_Yana",
            "YanaX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_Yana",    #When zero is working the right breast, fondle left
            "YanaX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_Yana", #When zero is working the left breast, fondle right
            "YanaX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Yana",
            "YanaX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Yana",
            "YanaX.Offhand == 'vibrator pussy'", "VibratorPussy_Yana",
            "YanaX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Yana",
            "YanaX.Offhand == 'vibrator anal'", "VibratorAnal_Yana",
            "YanaX.Offhand == 'vibrator anal insert'", "VibratorPussy_Yana",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for RogueX.Offhand(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Partner or Partner is YanaX or YanaX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and YanaX.Lust >= 70", "GirlFingerPussy_Yana",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Yana",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Yana",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Yana",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Yana",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Yana", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Yana",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Yana",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Yana",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Yana",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Yana",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Yana",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not YanaX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and YanaX.Lust >= 70", "GirlFingerPussy_Yana",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Yana",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Yana",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Yana",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Yana",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Yana", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Yana",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Yana",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Yana",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Yana",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Yana",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Yana",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus is not YanaX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Yana",
            "Trigger == 'fondle thighs'", "GropeThigh_Yana",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Yana",
            "Trigger == 'suck breasts'", "LickRightBreast_Yana",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Yana",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Yana",
            "Trigger == 'vibrator anal'", "VibratorAnal_Yana",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Yana",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Yana",
            "Trigger == 'fondle pussy'", "GropePussy_Yana",
            "Trigger == 'lick pussy'", "Lickpussy_Yana",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not YanaX", Null(),
#            "Trigger == 'fondle breasts' and not YanaX.Offhand", "GropeRightBreast_Yana",  #"Trigger == 'fondle breasts' and not RogueX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Yana",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Yana",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Yana",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Yana",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Yana",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Yana",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Yana",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Yana",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Yana",
            "Trigger2 == 'fondle pussy'", "GropePussy_Yana",
            "Trigger2 == 'lick pussy'", "Lickpussy_Yana",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Yana",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #UI tool for When Yana is masturbating using Trigger3 actions
#            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != YanaX", Null(),

#            #this is not a lesbian thing, and a trigger is set, and Yana is the primary. . .
#            "Trigger3 == 'fondle pussy'", "GirlGropePussy_YanaSelf",
#            "Trigger3 == 'fondle breasts'", ConditionSwitch(
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_Yana",
#                        #When zero is working the right breast, fondle left
#                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_Yana",
#                        #When zero is working the left breast, fondle right
#                    "True", "GirlGropeBothBreast_Yana",
#                        #else, fondle both
#                    ),
#            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Yana",
#            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Yana",
#            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Yana",
#            "Trigger3 == 'vibrator anal'", "VibratorAnal_Yana",
#            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Yana",
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Yana is secondary)
#            "Trigger != 'lesbian' or Ch_Focus == YanaX or not Trigger3", Null(),

#            # If there is a Trigger3 and Yana is not the focus
#            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and YanaX.Lust >= 70", "GirlFingerPussy_Yana",
#            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Yana",
#            "Trigger3 == 'lick pussy'", "Lickpussy_Yana",
#            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Yana",
#            "Trigger3 == 'suck breasts'", "LickRightBreast_Yana",
#            "Trigger3 == 'fondle breasts'", ConditionSwitch(
#                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Yana",
#                        #When zero is working the right breast, fondle left
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Yana",
#                        #When zero is working the left breast, fondle right
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_Yana",
#                        #When zero is working the right breast, fondle left
#                    "True", "GirlGropeRightBreast_Yana",
#                        #else, fondle right
#                    ),
#            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",
#            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
#            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
#            "Trigger3 == 'vibrator anal'", "VibratorAnal",
#            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
#            "True", Null(),
#            ),
        )
    anchor (0.5, 0.0)
    offset (60,0)
    zoom .80  #.75


image Yana_Sprite_HairBack:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                #hair back
    #            "renpy.showing('Yana_BJ_Animation')", Null(),
    #            "renpy.showing('Yana_SexSprite')", "images/YanaSex/Yana_Sprite_Hair_Long_UnderSex.png",
                "YanaX.Hair == 'wet' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaSprite/Yana_Sprite_Hair_Wet_Back.png",
                "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaSprite/Yana_Sprite_Long_Wet_Back.png",
#                "YanaX.Hair == 'wet' or YanaX.Water", "images/YanaSprite/Yana_Sprite_Hair_Short_Wet_Back.png",
#                "not Player.Male and 'facial' in YanaX.Spunk","images/YanaSprite/Yana_Sprite_Hair_Short_Wet_Back.png",
                "YanaX.Hair == 'long'", "images/YanaSprite/Yana_Sprite_Hair_Long_Back.png",
                "True", Null(), #"images/YanaSprite/Yana_Sprite_Hair_Short_Back.png",
                ),
        )
    anchor (0.5, 0.5)
    zoom .42#.47
    transform_anchor True
#    rotate -10


image Yana_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                #hair Under
                "YanaX.Hair == 'bun'", Null(),
#                "YanaX.Hair == 'wet' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaSprite/Yana_Sprite_Hair_Wet_Over.png",
                "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaSprite/Yana_Sprite_Hair_Wet_Under.png",
                "YanaX.Hair == 'wet' or YanaX.Water", "images/YanaSprite/Yana_Sprite_Hair_Wet_Under.png",
#                "YanaX.Hair == 'long'", "images/YanaSprite/Yana_Sprite_Hair_Long_Over.png",
                "True", "images/YanaSprite/Yana_Sprite_Hair_Long_Under.png",
                ),
        (0,0), ConditionSwitch(
                # Face background plate
#                "renpy.showing('Yana_SexSprite') and YanaX.Blush >= 2", "images/YanaSprite/Yana_Sprite_Head_Sex_Blush2.png",
#                "renpy.showing('Yana_SexSprite') and YanaX.Blush", "images/YanaSprite/Yana_Sprite_Head_Sex_Blush1.png",
#                "renpy.showing('Yana_SexSprite')", "images/YanaSprite/Yana_Sprite_Head_Sex.png",

                "YanaX.Hair != 'bun' and (YanaX.Hair == 'wet' or YanaX.Water)", ConditionSwitch(
                        #
                        "YanaX.Blush >= 2", "images/YanaSprite/Yana_Sprite_Head2_B2.png",
                        "YanaX.Blush", "images/YanaSprite/Yana_Sprite_Head2_B1.png",
                        "True", "images/YanaSprite/Yana_Sprite_Head2.png",
                        ),
                "YanaX.Blush >= 2", "images/YanaSprite/Yana_Sprite_Head_B2.png",
                "YanaX.Blush", "images/YanaSprite/Yana_Sprite_Head_B1.png",
                "True", "images/YanaSprite/Yana_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "YanaX.Mouth == 'lipbite'", "images/YanaSprite/Yana_Sprite_Mouth_Lipbite.png",
            "YanaX.Mouth == 'sucking'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
            "YanaX.Mouth == 'kiss'", "images/YanaSprite/Yana_Sprite_Mouth_Kiss.png",
            "YanaX.Mouth == 'sad'", "images/YanaSprite/Yana_Sprite_Mouth_Sad.png",
            "YanaX.Mouth == 'smile'", "images/YanaSprite/Yana_Sprite_Mouth_Smile.png",
            "YanaX.Mouth == 'surprised'", "images/YanaSprite/Yana_Sprite_Mouth_Kiss.png",
#            "not Player.Male and 'mouth' in YanaX.Spunk and YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Mouth_Tongue_Wet.png",
            "YanaX.Mouth == 'tongue' and YanaX.Demon", "images/YanaSprite/Yana_Sprite_Mouth_Tongue2.png",
            "YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Mouth_Tongue.png",
            "YanaX.Mouth == 'grimace'", "images/YanaSprite/Yana_Sprite_Mouth_Smile.png",
            "YanaX.Mouth == 'smirk'", "images/YanaSprite/Yana_Sprite_Mouth_Smirk.png",
            "YanaX.Mouth == 'open'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
            "True", "images/YanaSprite/Yana_Sprite_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in YanaX.Spunk or not Player.Male", Null(),
            "YanaX.Mouth == 'lipbite'", "images/YanaSprite/Yana_Sprite_Spunk_Smile.png",
            "YanaX.Mouth == 'sucking'", "images/YanaSprite/Yana_Sprite_Spunk_Open.png",
            "YanaX.Mouth == 'kiss'", "images/YanaSprite/Yana_Sprite_Spunk_Kiss.png",
            "YanaX.Mouth == 'sad'", "images/YanaSprite/Yana_Sprite_Spunk_Kiss.png",
            "YanaX.Mouth == 'smile'", "images/YanaSprite/Yana_Sprite_Spunk_Smile.png",
            "YanaX.Mouth == 'surprised'", "images/YanaSprite/Yana_Sprite_Spunk_Kiss.png",
#            "not Player.Male and 'mouth' in YanaX.Spunk and YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Mouth_Tongue_Wet.png",
            "YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Spunk_Open.png",
            "YanaX.Mouth == 'grimace'", "images/YanaSprite/Yana_Sprite_Spunk_Smile.png",
            "YanaX.Mouth == 'smirk'", "images/YanaSprite/Yana_Sprite_Spunk_Smirk.png",
            "YanaX.Mouth == 'open'", "images/YanaSprite/Yana_Sprite_Spunk_Open.png",
            "True", "images/YanaSprite/Yana_Sprite_Spunk_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in YanaX.Spunk and 'chin' not in YanaX.Spunk", Null(),
            "YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Head_Wet_Tongue.png",
            "'chin' in YanaX.Spunk", "images/YanaSprite/Yana_Sprite_Head_Wet_Face.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "YanaX.Brows == 'angry'", "images/YanaSprite/Yana_Sprite_Brows_Angry.png",
            "YanaX.Brows == 'sad'", "images/YanaSprite/Yana_Sprite_Brows_Sad.png",
            "YanaX.Brows == 'surprised'", "images/YanaSprite/Yana_Sprite_Brows_Surprised.png",
            "YanaX.Brows == 'confused'", "images/YanaSprite/Yana_Sprite_Brows_Confused.png",
            "True", "images/YanaSprite/Yana_Sprite_Brows_Normal.png",
            ),
#        (0,0), ConditionSwitch(
#                #Eyes
#                "YanaX.Demon","Yana BlinkD",
#                "True", "Yana Blink",
#                ),
        (0,0), "Yana Blink",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
                #hair over
    #            "renpy.showing('Yana_BJ_Animation')", Null(),
    #            "renpy.showing('Yana_SexSprite')", "images/YanaSex/Yana_Sprite_Hair_Long_UnderSex.png",

                "YanaX.Hair == 'bun' and YanaX.Demon", "images/YanaSprite/Yana_Sprite_Hair_Bun_OverHorn.png",
                "YanaX.Hair == 'bun'", "images/YanaSprite/Yana_Sprite_Hair_Bun_Over.png",
#                "YanaX.Hair == 'wet' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaSprite/Yana_Sprite_Hair_Wet_Over.png",
                "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaSprite/Yana_Sprite_Hair_Wet_Over.png",
                "YanaX.Hair == 'wet' or YanaX.Water", "images/YanaSprite/Yana_Sprite_Hair_Wet_Over.png",
#                "YanaX.Hair == 'long'", "images/YanaSprite/Yana_Sprite_Hair_Long_Over.png",
                "YanaX.Demon", "images/YanaSprite/Yana_Sprite_Hair_Long_OverHorn.png",
                "True", "images/YanaSprite/Yana_Sprite_Hair_Long_Over.png",
                ),
        (0,-276), ConditionSwitch(
                #horns
                "not YanaX.Demon",Null(),
                "YanaX.Hair == 'bun'", "images/YanaSprite/Yana_Sprite_HornsBangs.png",
                "YanaX.Hair == 'wet' or YanaX.Water or (not Player.Male and 'facial' in YanaX.Spunk)", "images/YanaSprite/Yana_Sprite_Horns.png",
                "True", "images/YanaSprite/Yana_Sprite_HornsBangs.png",
                ),
#        (0,-276), "images/YanaSprite/Yana_Sprite_HornRef.png",     #Eyes  (0,5)
#        (0,0), "images/YanaSprite/Yana_Sprite_WetRef.png",     #Eyes  (0,5)

#        (0,0), "images/YanaSprite/Yana_Sprite_Earring.png",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #Hair Water
            "YanaX.Water", "images/YanaSprite/Yana_Sprite_Head_Wet.png",
            "not Player.Male and 'facial' in YanaX.Spunk", "images/YanaSprite/Yana_Sprite_Head_Wet.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Hair.png",
            "'facial' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .42#.5
    transform_anchor True
#    rotate -10
#    alpha 0.9

image Yana Blink:
    ConditionSwitch(
    "YanaX.Eyes == 'closed'", "images/YanaSprite/Yana_Sprite_Eyes_Closed.png",
    "YanaX.Eyes == 'sexy'", "images/YanaSprite/Yana_Sprite_Eyes_Sexy.png",
    "YanaX.Eyes == 'side'", "images/YanaSprite/Yana_Sprite_Eyes_Side.png",
    "YanaX.Eyes == 'surprised'", "images/YanaSprite/Yana_Sprite_Eyes_Surprised.png",
    "YanaX.Eyes == 'normal'", "images/YanaSprite/Yana_Sprite_Eyes_Normal.png",
    "YanaX.Eyes == 'stunned'", "images/YanaSprite/Yana_Sprite_Eyes_Stunned.png",
    "YanaX.Eyes == 'down'", "images/YanaSprite/Yana_Sprite_Eyes_Down.png",
    "YanaX.Eyes == 'leftside'", "images/YanaSprite/Yana_Sprite_Eyes_Leftside.png",
    "YanaX.Eyes == 'manic'", "images/YanaSprite/Yana_Sprite_Eyes_Sexy.png",#"images/YanaSprite/Yana_Sprite_Eyes_Squint.png",
    "YanaX.Eyes == 'squint'", "Yana_Squint",#"Yana_Squint",
#    "YanaX.Eyes == 'psychic'", "images/YanaSprite/Yana_Sprite_Eyes_Psychic.png",
    "True", "images/YanaSprite/Yana_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/YanaSprite/Yana_Sprite_Eyes_Closed.png"
    .25
    repeat

image Yana_Squint:
    "images/YanaSprite/Yana_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/YanaSprite/Yana_Sprite_Eyes_Sexy.png"
    .25
    repeat

image Yana BlinkD:
    ConditionSwitch(
    "YanaX.Eyes == 'closed'", "images/YanaSprite/Yana_Sprite_Eyes_Closed.png",
    "YanaX.Eyes == 'sexy'", "images/YanaSprite/Yana_Sprite_Eyes_DSexy.png",
    "YanaX.Eyes == 'side'", "images/YanaSprite/Yana_Sprite_Eyes_DSide.png",
    "YanaX.Eyes == 'surprised'", "images/YanaSprite/Yana_Sprite_Eyes_DSurprised.png",
    "YanaX.Eyes == 'normal'", "images/YanaSprite/Yana_Sprite_Eyes_DNormal.png",
    "YanaX.Eyes == 'stunned'", "images/YanaSprite/Yana_Sprite_Eyes_DStunned.png",
    "YanaX.Eyes == 'down'", "images/YanaSprite/Yana_Sprite_Eyes_DDown.png",
    "YanaX.Eyes == 'leftside'", "images/YanaSprite/Yana_Sprite_Eyes_DLeftside.png",
    "YanaX.Eyes == 'manic'", "images/YanaSprite/Yana_Sprite_Eyes_DSexy.png",#"images/YanaSprite/Yana_Sprite_Eyes_Squint.png",
    "YanaX.Eyes == 'squint'", "Yana_SquintD",#"Yana_Squint",
#    "YanaX.Eyes == 'psychic'", "images/YanaSprite/Yana_Sprite_Eyes_Psychic.png",
    "True", "images/YanaSprite/Yana_Sprite_Eyes_DNormal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/YanaSprite/Yana_Sprite_Eyes_Closed.png"
    .25
    repeat

image Yana_SquintD:
    "images/YanaSprite/Yana_Sprite_Eyes_DNormal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/YanaSprite/Yana_Sprite_Eyes_DSexy.png"
    .25
    repeat

image Yana_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/YanaSprite/Yana_Sprite_WetMask.png"
        offset (-215,-560)#(-145,-15)#(-212,-4834)

image Yana_Sprite_Sword:
    "images/YanaSprite/Yana_Sprite_Sword.png"
    yzoom -1
    yoffset -525
##image Yana_Drip_MaskPanties:
##    #This is the mask for her drip pattern in panties down mode
##    contains:
##        "images/YanaSprite/Yana_Sprite_DripMaskPanties.png"
##        offset (-145,-560)#(-225,-560)

##image Yana_Drip_MaskP:
##    #This is the mask for her drip pattern in panties down mode
##    contains:
##        "images/YanaSprite/Yana_Sprite_WetMask_Pants.png"
##        offset (-275,-560)#(-145,-560)

## End Yana Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Yana Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Yana_Doggy_Base = LiveComposite(
image Yana_Doggy_Animation: #nee Yana_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite or Ch_Focus is not YanaX", "Yana_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Yana_Doggy_Fuck2_Top",
                    "Speed > 1", "Yana_Doggy_Fuck_Top",
                    "Speed", "Yana_Doggy_Anal_Head_Top",
                    "True", "Yana_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Yana_Doggy_Fuck2_Top",
                    "Speed > 1", "Yana_Doggy_Fuck_Top",
                    "True", "Yana_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Yana_Doggy_Foot2_Top",
                    "Speed", "Yana_Doggy_Foot1_Top",
                    "True", "Yana_Doggy_Foot0_Top",
                    ),
            "True", "Yana_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite or Ch_Focus is not YanaX", "Yana_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Yana_Doggy_Fuck2_Ass",
                    "Speed > 1", "Yana_Doggy_Fuck_Ass",
                    "Speed", "Yana_Doggy_Anal_Head_Ass",
                    "True", "Yana_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Yana_Doggy_Fuck2_Ass",
                    "Speed > 1", "Yana_Doggy_Fuck_Ass",
                    "True", "Yana_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Yana_Doggy_Foot2_Ass",
                    "Speed", "Yana_Doggy_Foot1_Ass",
                    "True", "Yana_Doggy_Foot0_Ass",
                    ),
            "True", "Yana_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            "not Player.Sprite", "Yana_Doggy_Shins0",
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Yana_Doggy_Feet2",
                    "Speed", "Yana_Doggy_Feet1",
                    "True", "Yana_Doggy_Feet0",
                    ),
            "ShowFeet", "Yana_Doggy_Shins0",# "not Player.Sprite and ShowFeet", "Yana_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Yana_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Yana_Doggy_Hair_Under", #back of the hair
#        (0,60), "Yana_Doggy_Head",               #Head

#        (0,0), "images/YanaDoggy/Yana_Doggy_HeadRef.png",               #Head
        (0,0), ConditionSwitch(
            #head
            "YanaX.Facing", "Yana_Doggy_Head_Fore",
            "True", "Yana_Doggy_Head",
            ),

        (0,0), "images/YanaDoggy/Yana_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #bra
#            "YanaX.Uptop", ConditionSwitch(
#                    "YanaX.Chest == 'lace bra'", "images/YanaDoggy/Yana_Doggy_Chest_Lace_Up.png",
#                    "YanaX.Chest == 'sports bra'", "images/YanaDoggy/Yana_Doggy_Chest_Sport_Up.png",
#                    "YanaX.Chest == 'bikini top'", "images/YanaDoggy/Yana_Doggy_Chest_Bikini_Up.png",
#                    "True", "images/YanaDoggy/Yana_Doggy_Chest_Bra_Up.png",
#                    ),
            "YanaX.Chest == 'lace bra'", "images/YanaDoggy/Yana_Doggy_Chest_Lace.png",
            "YanaX.Chest == 'mesh top'", "images/YanaDoggy/Yana_Doggy_Chest_Mesh.png",
            "YanaX.Chest == 'bikini top'", "images/YanaDoggy/Yana_Doggy_Chest_Bikini.png",
            "YanaX.Chest", "images/YanaDoggy/Yana_Doggy_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "YanaX.Water", "images/YanaDoggy/Yana_Doggy_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Dress
            "YanaX.Legs == 'dress' and YanaX.Uptop", "images/YanaDoggy/Yana_Doggy_Over_Towel.png",
            "YanaX.Legs == 'dress'", "images/YanaDoggy/Yana_Doggy_Over_Dress.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "YanaX.Over == 'purple top'", "images/YanaDoggy/Yana_Doggy_Over_Purple.png",
            "YanaX.Over == 'corset'", "images/YanaDoggy/Yana_Doggy_Over_Corset.png",
            "YanaX.Over == 'shirt'", "images/YanaDoggy/Yana_Doggy_Over_Shirt.png",
            "YanaX.Over == 'towel'", "images/YanaDoggy/Yana_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #armlets
            "YanaX.Arms", "images/YanaDoggy/Yana_Doggy_Armlets.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket
            "YanaX.Acc == 'jacket'", "images/YanaDoggy/Yana_Doggy_Over_Jacket.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #long Hair
            "YanaX.Hair != 'long' and YanaX.Hair != 'wetlong'", Null(),
#            "YanaX.Facing", ConditionSwitch(
#                    "YanaX.Water or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hair_Long_Wet_Fore.png",
#                    "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Long_Wet_Fore.png",
#                    "True", "images/YanaDoggy/Yana_Doggy_Hair_Long_Fore.png",
#                    ),
            "YanaX.Water or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hair_Long_Wet_Over.png",
            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Long_Wet_Over.png",
            "True", "images/YanaDoggy/Yana_Doggy_Hair_Long_Over.png",
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Ch_Focus is YanaX and (Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts')", "Yana_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Yana_Doggy_Head",               #Head
        #(165,0),"Yana_Doggy_Hair_Over", #front of the hair
        )
#    zoom 2
#    transform_anchor True
#    anchor (225,1400)
#    offset (-175,25)#(-200,0)
#    offset (0,25)#(-200,0)
#    zoom .95
#    offset (-350,-180)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Yana_Doggy_Head:
    LiveComposite(
        #Head
        (420,420),
        #(0,0), "images/YanaDoggy/Yana_Doggy_Head.png", #Body base
        #(0,0), "images/YanaDoggy/Yana_Doggy_TestArm.png",#Eyes
#        (0,0), ConditionSwitch(
#            #Hair back
#            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaDoggy/Yana_Doggy_Hair_Wet_Back.png",
#            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Wet_Back.png",
#            "YanaX.Hair == 'pony'", Null(),
#            "True", "images/YanaDoggy/Yana_Doggy_Hair_Short_Back.png",
#            ),
        (0,0), ConditionSwitch(
            #Hair
            "YanaX.Water or YanaX.Hair == 'long' or YanaX.Hair == 'wetlong'", Null(),
            "not Player.Male and 'facial' in YanaX.Spunk",Null(),
            "True", "images/YanaDoggy/Yana_Doggy_Hair_Short_Back.png",
            ),
        (0,0), ConditionSwitch(
            #Head
            #"YanaX.Blush > 1", "images/YanaDoggy/Yana_Doggy_Head_Blush2.png",
            "YanaX.Blush", "images/YanaDoggy/Yana_Doggy_Head_Blush.png",
            "True", "images/YanaDoggy/Yana_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "YanaX.Mouth == 'normal'", "images/YanaDoggy/Yana_Doggy_Mouth_Normal.png",
            "YanaX.Mouth == 'lipbite'", "images/YanaDoggy/Yana_Doggy_Mouth_Normal.png",
            "YanaX.Mouth == 'sucking'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
            "YanaX.Mouth == 'kiss'", "images/YanaDoggy/Yana_Doggy_Mouth_Kiss.png",
            "YanaX.Mouth == 'sad'", "images/YanaDoggy/Yana_Doggy_Mouth_Sad.png",
            "YanaX.Mouth == 'smile'", "images/YanaDoggy/Yana_Doggy_Mouth_Smirk.png",
            "YanaX.Mouth == 'grimace'", "images/YanaDoggy/Yana_Doggy_Mouth_Normal.png",
            "YanaX.Mouth == 'surprised'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
            "YanaX.Mouth == 'tongue'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
            "YanaX.Mouth == 'smirk'", "images/YanaDoggy/Yana_Doggy_Mouth_Smirk.png",
            "True", "images/YanaDoggy/Yana_Doggy_Mouth_Normal.png",
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in YanaX.Spunk", "images/YanaDoggy/Yana_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in YanaX.Spunk", Null(),
#            #"YanaX.Mouth == 'normal'", "images/YanaDoggy/Yana_Doggy_Spunk_Normal.png",
#            #"YanaX.Mouth == 'sad'", "images/YanaDoggy/Yana_Doggy_Spunk_Normal.png",
#            "YanaX.Mouth == 'lipbite'", "images/YanaDoggy/Yana_Doggy_Spunk_Sad.png",
#            "YanaX.Mouth == 'smile'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
#            "YanaX.Mouth == 'grimace'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
#            "YanaX.Mouth == 'sucking'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
#            #"YanaX.Mouth == 'kiss'", "images/YanaDoggy/Yana_Doggy_Spunk_Open.png",
#            "YanaX.Mouth == 'surprised'", "images/YanaDoggy/Yana_Doggy_Mouth_Open.png",
#            "YanaX.Mouth == 'tongue'", "images/YanaDoggy/Yana_Doggy_Spunk_Smile.png",
            "True", "images/YanaDoggy/Yana_Doggy_Spunk_Mouth.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"YanaX.Brows == 'normal'", "images/YanaDoggy/Yana_Doggy_Brows_Normal.png",
            "YanaX.Brows == 'angry'", "images/YanaDoggy/Yana_Doggy_Brows_Angry.png",
            "YanaX.Brows == 'sad'", "images/YanaDoggy/Yana_Doggy_Brows_Sad.png",
            "YanaX.Brows == 'surprised'", "images/YanaDoggy/Yana_Doggy_Brows_Surprised.png",
            #"YanaX.Brows == 'confused'", "images/YanaDoggy/Yana_Doggy_Brows_Normal.png",
            "True", "images/YanaDoggy/Yana_Doggy_Brows_Normal.png",
            ),
        (0,0), "Yana Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "YanaX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suit collar
            "YanaX.Chest == 'mesh top'", "images/YanaDoggy/Yana_Doggy_Collar_Red.png",
            "YanaX.Neck == 'scarf'", "images/YanaDoggy/Yana_Doggy_Scarf.png",
            "YanaX.Neck", "images/YanaDoggy/Yana_Doggy_Collar_Black.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #face spunk
#            "'facial' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Facial.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Hair
            "(YanaX.Water and YanaX.Hair == 'long') or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hair_Long_Wet.png",
            "(YanaX.Water and YanaX.Hair == 'long') and not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Long_Wet.png",
            "YanaX.Hair == 'long'", "images/YanaDoggy/Yana_Doggy_Hair_Long.png",
            "YanaX.Water or YanaX.Hair == 'wet' or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hair_Short_Wet.png",
            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Short_Wet.png",
            "True", "images/YanaDoggy/Yana_Doggy_Hair_Short.png",
            ),
        (0,0), ConditionSwitch(
                #hairband
                "not YanaX.Hat",Null(),
                "YanaX.Water or YanaX.Hair == 'wet' or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hairband_Wet.png",
                "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hairband_Wet.png",
                "True", "images/YanaDoggy/Yana_Doggy_Hairband_Short.png",
                ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Hair.png",
            "'facial' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Facial.png",
#            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaDoggy/Yana_Doggy_Head_Wet.png",
#            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana Doggy Blink:
        #Eyes
        ConditionSwitch(
        "YanaX.Eyes == 'sexy'", "images/YanaDoggy/Yana_Doggy_Eyes_Sexy.png",
        "YanaX.Eyes == 'side'", "images/YanaDoggy/Yana_Doggy_Eyes_Side.png",
#        "YanaX.Eyes == 'normal'", "images/YanaDoggy/Yana_Doggy_Eyes_Normal.png",
        "YanaX.Eyes == 'closed'", "images/YanaDoggy/Yana_Doggy_Eyes_Closed.png",
        "YanaX.Eyes == 'manic'", "images/YanaDoggy/Yana_Doggy_Eyes_Stunned.png",
        "YanaX.Eyes == 'down'", "images/YanaDoggy/Yana_Doggy_Eyes_Down.png",
        "YanaX.Eyes == 'stunned'", "images/YanaDoggy/Yana_Doggy_Eyes_Stunned.png",
        "YanaX.Eyes == 'surprised'", "images/YanaDoggy/Yana_Doggy_Eyes_Surprised.png",
        "YanaX.Eyes == 'squint'", "images/YanaDoggy/Yana_Doggy_Eyes_Sexy.png",
        "True", "images/YanaDoggy/Yana_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/YanaDoggy/Yana_Doggy_Eyes_Closed.png"
        .25
        repeat

# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,420),
        (0,0), ConditionSwitch(
            #Hair
            "(YanaX.Water and YanaX.Hair == 'long') or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hair_Long_Wet_Fore.png",
            "(YanaX.Water and YanaX.Hair == 'long') and not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Long_Wet_Fore.png",
            "YanaX.Hair == 'long'", "images/YanaDoggy/Yana_Doggy_Hair_Long_Fore.png",
            "YanaX.Water or YanaX.Hair == 'wet' or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hair_Short_Wet_Fore.png",
            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hair_Short_Wet_Fore.png",
            "True", "images/YanaDoggy/Yana_Doggy_Hair_Short_Fore.png",
            ),
        (0,0), ConditionSwitch(
                #hairband
                "not YanaX.Hat",Null(),
                "YanaX.Water or YanaX.Hair == 'wet' or YanaX.Hair == 'wetlong'", "images/YanaDoggy/Yana_Doggy_Hairband_Fore_Wet.png",
                "not Player.Male and 'facial' in YanaX.Spunk","images/YanaDoggy/Yana_Doggy_Hairband_Fore_Wet.png",
                "True", "images/YanaDoggy/Yana_Doggy_Hairband_Fore_Short.png",
                ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
        (0,0), ConditionSwitch(
            #Legs backside
#            "YanaX.Legs == 'dress'","images/YanaDoggy/Yana_Doggy_Legs_Dress_Under.png",
            "YanaX.Upskirt", Null(),
            "YanaX.Legs == 'skirt'","images/YanaDoggy/Yana_Doggy_Legs_Skirt_Under.png",
            "YanaX.Legs == 'dress'","images/YanaDoggy/Yana_Doggy_Legs_Dress_Under.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pussy base
            "YanaX.Legs and not YanaX.Upskirt", "images/YanaDoggy/Yana_Doggy_Ass_Closed.png",
            "YanaX.Panties and not YanaX.PantiesDown", "images/YanaDoggy/Yana_Doggy_Ass_Closed.png",
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'in'", "images/YanaDoggy/Yana_Doggy_Ass_Base.png",
            "YanaX.Offhand == 'dildo pussy'", "images/YanaDoggy/Yana_Doggy_Ass_Base.png",
            "YanaX.Offhand == 'fondle pussy'", "images/YanaDoggy/Yana_Doggy_Ass_Base.png",
            #only applies if she is the lead
            "Ch_Focus is YanaX", ConditionSwitch(
                    "Trigger == 'lick pussy'", "images/YanaDoggy/Yana_Doggy_Ass_Open.png",
                    "'dildo pussy' in (Trigger,Trigger2)", "images/YanaDoggy/Yana_Doggy_Ass_Base.png",
                    "'fondle pussy' in (Trigger,Trigger2) or (Partner and Partner.Offhand == 'girl fondle pussy')", "images/YanaDoggy/Yana_Doggy_Ass_Base.png",
                    "Trigger == 'insert pussy'", "images/YanaDoggy/Yana_Doggy_Ass_Base.png",
                    "True", "images/YanaDoggy/Yana_Doggy_Ass_Closed.png",
                    ),
            "True", "images/YanaDoggy/Yana_Doggy_Ass_Closed.png",
            ),
#        (0,0), ConditionSwitch(
#            #Hotdogging plate
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "True", "images/RogueDoggy/Rogue_Doggy_Hotdog.png",
#            ),
        (0,0), ConditionSwitch(
            #ass red
            "YanaX.Red", "images/YanaDoggy/Yana_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus base
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed", "images/YanaDoggy/Yana_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),

            "YanaX.Offhand == 'insert ass'", "images/YanaDoggy/Yana_Doggy_Anal_FullBase.png",
            "YanaX.Offhand == 'dildo anal'", "images/YanaDoggy/Yana_Doggy_Anal_FullBase.png",
            "Ch_Focus is YanaX and 'dildo anal' in (Trigger,Trigger2)", "images/YanaDoggy/Yana_Doggy_Anal_FullBase.png",
            "Ch_Focus is YanaX and 'insert ass' in (Trigger,Trigger2) or (Partner and Partner.Offhand == 'girl insert ass')", "images/YanaDoggy/Yana_Doggy_Anal_FullBase.png",

            "YanaX.Plug", "images/PlugIn.png",
            "YanaX.Loose > 2", "Yana_Gape_Anal",    #intentional
            "YanaX.Loose", "images/YanaDoggy/Yana_Doggy_Asshole_Loose.png",
            "True", "images/YanaDoggy/Yana_Doggy_Asshole_Tight.png",
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "YanaX.Water", "images/YanaDoggy/Yana_Doggy_Water_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "YanaX.Hose == 'stockings'", "images/YanaDoggy/Yana_Doggy_Hose_Stockings.png",
#            "YanaX.Hose == 'socks'", "images/YanaDoggy/Yana_Doggy_Hose_Socks.png",
#            "Player.Sprite and Player.Cock == 'in'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaDoggy/Yana_Doggy_Hose_StockingsGarter.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaDoggy/Yana_Doggy_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not YanaX.PantiesDown or (YanaX.Legs == 'pants' and not YanaX.Upskirt)", Null(),
            "YanaX.Panties == 'lace panties'", "images/YanaDoggy/Yana_Doggy_Panties_Bikini_Down.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaDoggy/Yana_Doggy_Panties_Bikini_Down.png",
            "YanaX.Panties", "images/YanaDoggy/Yana_Doggy_Panties_Gray_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "Ch_Focus is YanaX and 'in' in YanaX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/YanaDoggy/Yana_Doggy_SpunkPussyOpen.png",  #fix for YanaX.Spunk is used later
            "Ch_Focus is YanaX and 'in' in YanaX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "Ch_Focus is YanaX and YanaX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "YanaX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not YanaX.Pubes", Null(),
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'in'", Null(), # "images/YanaDoggy/Yana_Doggy_Pubes_Fuckingucked.png",
            "YanaX.Offhand == 'dildo pussy'", "Yana_Pussy_Fucking2",
            "YanaX.Offhand == 'fondle pussy'", "Yana_Pussy_Fingering",
            "Ch_Focus is YanaX and 'dildo pussy' in (Trigger,Trigger2)", "Yana_Pussy_Fucking2",
            "Ch_Focus is YanaX and ('fondle pussy' in (Trigger,Trigger2) or (Partner and Partner.Offhand == 'fondle girl pussy'))", "Yana_Pussy_Fingering",
            "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaDoggy/Yana_Doggy_Pubes_Clothed.png",
            "YanaX.PantiesDown and Ch_Focus is YanaX and Trigger == 'lick pussy'", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
            "YanaX.PantiesDown", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
            "YanaX.Panties", "images/YanaDoggy/Yana_Doggy_Pubes_Clothed.png",
            "YanaX.Hose and YanaX.Hose == 'pantyhose'", "images/YanaDoggy/Yana_Doggy_Pubes_Clothed.png",
            "Ch_Focus is YanaX and Trigger == 'lick pussy'", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
            "True", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Ch_Focus is YanaX and Player.Sprite", Null(),
            "YanaX.Panties and not YanaX.PantiesDown", Null(),
            "YanaX.Pierce == 'barbell'", "images/YanaDoggy/Yana_Doggy_Pierce_B.png",
            "(YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt') and not YanaX.Upskirt", Null(),
            "YanaX.Pierce == 'ring'", "images/YanaDoggy/Yana_Doggy_Pierce_R.png",
            "True", Null(),
            ),

        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in YanaX.Spunk or (Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/YanaDoggy/Yana_Doggy_SpunkAnalOpen.png",
            "YanaX.Loose", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "YanaX.PantiesDown or not YanaX.Panties", Null(),
            "Ch_Focus is YanaX and Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "YanaX.Panties == 'lace panties'", "images/YanaDoggy/Yana_Doggy_Panties_Lace.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaDoggy/Yana_Doggy_Panties_Bikini.png",
            "YanaX.Wet", "images/YanaDoggy/Yana_Doggy_Panties_Gray_Wet.png",
            "True", "images/YanaDoggy/Yana_Doggy_Panties_Gray.png",
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "YanaX.Panties and YanaX.PantiesDown", Null(),
            "YanaX.Hose == 'ripped pantyhose'", "images/YanaDoggy/Yana_Doggy_Hose_Pantyhose_Holed.png",
#            "YanaX.Hose == 'ripped tights'", "images/YanaDoggy/Yana_Doggy_Hose_Tights_Holed.png",
            "Ch_Focus is YanaX and Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "YanaX.Hose == 'pantyhose'", "images/YanaDoggy/Yana_Doggy_Hose_Pantyhose.png",
#            "YanaX.Hose == 'tights' and YanaX.Wet", "images/YanaDoggy/Yana_Doggy_Hose_Tights_Wet.png",
#            "YanaX.Hose == 'tights'", "images/YanaDoggy/Yana_Doggy_Hose_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "YanaX.Legs == 'dress'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , "images/YanaDoggy/Yana_Doggy_Legs_Dress_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "YanaX.Upskirt", "images/YanaDoggy/Yana_Doggy_Legs_Dress_Up.png",
                    "True", "images/YanaDoggy/Yana_Doggy_Legs_Dress.png",
                    ),
            "YanaX.Legs == 'skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , "images/YanaDoggy/Yana_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "YanaX.Upskirt", "images/YanaDoggy/Yana_Doggy_Legs_Skirt_Up.png",
                    "True", "images/YanaDoggy/Yana_Doggy_Legs_Skirt.png",
                    ),
            "YanaX.Legs == 'pants'", ConditionSwitch(
                    "YanaX.Upskirt or YanaX.PantiesDown", "images/YanaDoggy/Yana_Doggy_Legs_Shorts_Down.png",
                    "YanaX.Wet > 1", "images/YanaDoggy/Yana_Doggy_Legs_Pants_Wet.png",
                    "True", "images/YanaDoggy/Yana_Doggy_Legs_Pants.png",
                    ),
            "YanaX.Legs == 'shorts'", ConditionSwitch(
                    "YanaX.Upskirt or YanaX.PantiesDown", "images/YanaDoggy/Yana_Doggy_Legs_Shorts_Down.png",
                    "YanaX.Wet > 1", "images/YanaDoggy/Yana_Doggy_Legs_Shorts_Wet.png",
                    "True", "images/YanaDoggy/Yana_Doggy_Legs_Shorts.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            #only applies if she is the lead
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Yana_Pussy_Fucking3",        #Speed 3
                    "Speed > 1", "Yana_Pussy_Fucking2",        #Speed 2
                    "Speed", "Yana_Pussy_Heading",             #Speed 1
                    "True", "Yana_Pussy_Static",               #Speed 0
                    ),
            "YanaX.Offhand == 'dildo pussy'", "Yana_Pussy_Fucking2",
            "YanaX.Offhand == 'fondle pussy'", "Yana_Pussy_Fingering",
            "Ch_Focus is YanaX and 'dildo pussy' in (Trigger,Trigger2)", "Yana_Pussy_Fucking2",
            "Ch_Focus is YanaX and ('fondle pussy' in (Trigger,Trigger2) or (Partner and Partner.Offhand == 'fondle girl pussy'))", "Yana_Pussy_Fingering",
            "Partner is YanaX and Ch_Focus.Offhand == 'fondle girl pussy'", "Yana_Pussy_Fingering",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Pussy Composite
##            "YanaX.Legs and not YanaX.Upskirt",Null(),
##            "YanaX.Panties and not YanaX.PantiesDown", Null(),
#            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
#                    "Speed > 2", "Yana_Pussy_Fucking3",#Speed 3
#                    "Speed > 1", "Yana_Pussy_Fucking2",#Speed 2
#                    "Speed", "Yana_Pussy_Heading",      #Speed 1
#                    "True", "Yana_Pussy_Static",              #Speed 0
#                    ),
#            "'dildo pussy' in (Trigger,Trigger2,YanaX.Offhand)", "Yana_Pussy_Fucking2",
#            "'fondle pussy' in (Trigger,Trigger2,YanaX.Offhand)", "Yana_Pussy_Fingering",
#            "Partner is YanaX and Ch_Focus.Offhand == 'lick girl pussy'", "Yana_Pussy_Fingering",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            #only applies if she is the lead
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Yana_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Yana_Anal_Fucking",  #Speed 2
                    "Speed", "Yana_Anal_Heading",      #Speed 1
                    "True", "Yana_Anal",               #Speed 0
                    ),
            "YanaX.Legs and not YanaX.Upskirt",Null(),
            "YanaX.Panties and not YanaX.PantiesDown", Null(),
            "YanaX.Offhand == 'dildo anal'", "Yana_Anal_Fucking",
            "YanaX.Offhand == 'insert ass'", "Yana_Anal_Fingering",
            "Ch_Focus is YanaX and 'dildo anal' in (Trigger,Trigger2)", "Yana_Anal_Fucking",
            "Ch_Focus is YanaX and ('insert ass' in (Trigger,Trigger2) or (Partner and Partner.Offhand == 'insert girl ass'))", "Yana_Anal_Fingering",
            "Partner is YanaX and Ch_Focus.Offhand == 'insert girl ass'", "Yana_Anal_Fingering",
#            "YanaX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Over Layer
            "YanaX.Acc == 'jacket' and (YanaX.Upskirt or YanaX.Legs == 'dress' or YanaX.Legs == 'skirt')", "images/YanaDoggy/Yana_Doggy_Legs_Jacket_Up.png",
            "YanaX.Acc == 'jacket'", "images/YanaDoggy/Yana_Doggy_Legs_Jacket.png",
            "YanaX.Over == 'towel' and (YanaX.Upskirt or YanaX.Legs == 'dress' or YanaX.Legs == 'skirt')", "images/YanaDoggy/Yana_Doggy_Legs_Dress_Up.png",
            "YanaX.Over == 'towel'", "images/YanaDoggy/Yana_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Ch_Focus is YanaX and Player.Sprite and Player.Cock", Null(),
            "Ch_Focus is YanaX and Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",                                 #Rogue is lead, you're licking
            "Ch_Focus is YanaX and Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",                                     #Rogue is lead, you're licking
            "Ch_Focus is YanaX and Partner and Partner.Offhand == 'lick girl pussy'", "Rogue_Doggy_Lick_Pussy",        #Rogue is lead, partner's licking
            "Ch_Focus is YanaX and Partner and Partner.Offhand == 'lick girl ass'", "Rogue_Doggy_Lick_Ass",            #Rogue is lead, partner's licking
            "Partner is YanaX and Ch_Focus.Offhand == 'lick girl pussy'", "Rogue_Doggy_Lick_Pussy",                    #Rogue is partner, lead's licking
            "Partner is YanaX and Ch_Focus.Offhand == 'lick girl ass'", "Rogue_Doggy_Lick_Ass",                        #Rogue is partner, lead's licking
            "True", Null()
            ),
#        (0,0), ConditionSwitch(
#            #Hotdogging underlayer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "YanaX.Over == 'towel'", Null(),
#            "(YanaX.Legs == 'dress' or YanaX.Legs == 'other skirt') and YanaX.Upskirt", "images/YanaDoggy/Yana_Doggy_Hotdog_Upskirt.png",
#            "True", "images/YanaDoggy/Yana_Doggy_HotdogBack.png",
#            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "Ch_Focus is not YanaX or not Player.Sprite or Player.Cock != 'out'", Null(),
            "(YanaX.Legs == 'dress' or YanaX.Legs == 'skirt') and YanaX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "(YanaX.Legs == 'dress' or YanaX.Legs == 'skirt') and YanaX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
#        (0,0), ConditionSwitch(
#            #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        )
# End Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Yana_Doggy_Shins", "images/YanaDoggy/Yana_Doggy_Feet_Mask.png")

image Yana_Doggy_Feet_Under:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Yana's footjob shins
#    contains:
#        "images/YanaDoggy/Yana_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "YanaX.Hose == 'garterbelt'", "images/YanaDoggy/Yana_Doggy_Feet.png",
#            "YanaX.Hose == 'ripped pantyhose'", "images/YanaDoggy/Yana_Doggy_Feet_Holed.png",
            "YanaX.Hose == 'socks'", "images/YanaDoggy/Yana_Doggy_Feet_Socks.png",
            "YanaX.Hose", "images/YanaDoggy/Yana_Doggy_Feet_Hose.png",
            "True", "images/YanaDoggy/Yana_Doggy_Feet.png",
            )
    contains:
        #pants
        ConditionSwitch(
            "YanaX.Legs == 'pants'", "images/YanaDoggy/Yana_Doggy_Feet_Pants.png",
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Feet_Under.png",
            "True", Null(),
            )
#    pos (0,0)

image Yana_Doggy_Feet_Over:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Yana's footjob shins
#    contains:
#        "images/YanaDoggy/Yana_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "YanaX.Hose == 'garterbelt'", "images/YanaDoggy/Yana_Doggy_Feet_Over.png",
#            "YanaX.Hose == 'ripped pantyhose'", "images/YanaDoggy/Yana_Doggy_Feet_Holed.png",
            "YanaX.Hose == 'socks'", "images/YanaDoggy/Yana_Doggy_Feet_Socks_Over.png",
            "YanaX.Hose", "images/YanaDoggy/Yana_Doggy_Feet_Hose_Over.png",
            "True", "images/YanaDoggy/Yana_Doggy_Feet_Over.png",
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in YanaX.Spunk and Player.Male", "images/YanaDoggy/Yana_Doggy_Spunk_Feet_Over.png",
            "True", Null(),
            )
#    pos (0,0)

image Yana_Doggy_Shins0:
        #static animation
        "Yana_Doggy_Feet_Under"
        offset (0, 100) #(0,150) top


image Yana_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (190,350)#(270,410)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Yana_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/EmmaDoggy/Emma_Doggy_Anal_GapeBase.png"
            anchor (0.52,0.69)
            offset (218,513)#(218,513)
            zoom .35 # loose
            block:
                ease 3 zoom .20 #in
                ease 3.2 zoom .30 #out
                repeat
        contains:
            subpixel True
            "images/JubesDoggy/Jubes_Doggy_Anal_GapeHole.png"
            anchor (0.52,0.69)
            offset (218,513)#(218,513)
            zoom .35 # loose
            block:
                ease 3 zoom .15 #in
                ease 3.2 zoom .30 #out
                repeat

#Hotdogging animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Zero_Yana_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Yana_Hotdog_Moving:
    # The moving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


image Yana_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Yana_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Yana_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Yana_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Pussy fucking animations


image Yana_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/YanaDoggy/Yana_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
#    contains:
#        #pubes
#        ConditionSwitch(
#            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
#            "True", Null(),
#            )
#        subpixel True
#        transform_anchor True
#        anchor (0.515,0.69)#(0.52,0.69)
#        pos (217,518) #(219,518)
#        xzoom 1.1
    contains:
        #pubes
        ConditionSwitch(
            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (213,518) #(217,518)
        xzoom .9
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .9
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "YanaX.Pierce == 'barbell'", "images/YanaDoggy/Yana_Doggy_Pierce_B.png",
            "YanaX.Pierce == 'ring'", "images/YanaDoggy/Yana_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (218,516) #(221,516)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Yana_Doggy_Static", "Yana_Pussy_Mask_Static")
    xoffset 2

image Yana_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Yana_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/YanaDoggy/Yana_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#image Yana_PussyHole_Static:
#    #This is the image impacted by the mask for the pussy flap in "Yana_Pussy_Moving"
#    contains:
#        #Mask
#        "images/YanaDoggy/Yana_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 512
#            pause 1
#            ease 3 ypos 515
#            repeat


image Zero_Yana_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 545 #out stroke
            repeat

image Yana_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/YanaDoggy/Yana_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.51,0.69)#(0.52,0.69)
#        anchor (0.52,0.69)
        pos (213,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
#    contains:
#        #pubes
#        ConditionSwitch(
#            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Fucking.png",
#            "True", Null(),
#            )
#        subpixel True
#        anchor (0.51,0.69)
#        pos (213,518) #(213,518)
#        xzoom .75
#        block:
#            ease 1 xzoom 1
#            pause 1
#            ease 3 xzoom .77
#            repeat
    contains:
        #pubes
        ConditionSwitch(
            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,522) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .65
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,518) #(213,518)
        xzoom .77
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "YanaX.Pierce == 'barbell'", "images/YanaDoggy/Yana_Doggy_Pierce_B.png",
            "YanaX.Pierce == 'ring'", "images/YanaDoggy/Yana_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.75) #(0.52,0.69)
        pos (215,560) #(221,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Yana_Doggy_Heading", "Yana_Pussy_Mask")


#    contains:
#        # expanding pussy flap
#        AlphaMask("Yana_Pussy_Heading_Flap", "Yana_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.515,0.75)#(0.52,0.69)
        pos (215,560) #(221,518)
        xzoom .8
        yzoom .6
        parallel:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .7#.6
            repeat
        parallel:
            ease .9 yzoom 1
            pause 1.6
            ease 2.5 yzoom .5#.4
            repeat
    xoffset 2


image Yana_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Yana_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/YanaDoggy/Yana_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

#image Yana_Pussy_Heading_Flap:
#    #This is the image impacted by the mask for the pussy flap in "Yana_Pussy_Heading"
#    contains:
#        #Mask
#        "images/YanaDoggy/Yana_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 505
#            pause 1
#            ease 3 ypos 515
#            repeat

image Yana_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/YanaDoggy/Yana_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9#1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,518) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "YanaX.Pierce == 'barbell'", "images/YanaDoggy/Yana_Doggy_Pierce_B.png",
            "YanaX.Pierce == 'ring'", "images/YanaDoggy/Yana_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (215,516)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
#    contains:
#        # expanding pussy flap
#        AlphaMask("Yana_Pussy_Heading_Flap", "Yana_Pussy_Hole_Mask")

    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.515,0.75)#(0.52,0.69)
        pos (215,560) #(221,518)
        xzoom .8
        yzoom .6
        parallel:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .7#.6
            repeat
        parallel:
            ease .9 yzoom 1
            pause 1.6
            ease 2.5 yzoom .5#.4
            repeat


image Zero_Yana_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat


# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Yana_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/YanaDoggy/Yana_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "YanaX.Pierce == 'barbell'", "images/YanaDoggy/Yana_Doggy_Pierce_B.png",
            "YanaX.Pierce == 'ring'", "images/YanaDoggy/Yana_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "YanaX.Offhand == 'dildo pussy'", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "Ch_Focus is YanaX and 'dildo pussy' in (Trigger,Trigger2)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "Ch_Focus is YanaX",AlphaMask("Zero_Yana_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",Null(),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
    xoffset 1


image Zero_Yana_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Yana_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/YanaDoggy/Yana_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "YanaX.Pubes", "images/YanaDoggy/Yana_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "YanaX.Pierce == 'barbell'", "images/YanaDoggy/Yana_Doggy_Pierce_B.png",
            "YanaX.Pierce == 'ring'", "images/YanaDoggy/Yana_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Yana_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
    xoffset 1


image Zero_Yana_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Yana_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/YanaDoggy/Yana_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,515)#(208,500)
        zoom 1.25
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Yana_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75#1
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #Cock with mask
        AlphaMask("Zero_Yana_Doggy_Anal_Finger", "Yana_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .7
        block:
            ease .5 zoom .8
            pause .5
            ease 1.5 zoom .7 #.5
            repeat

image Zero_Yana_Doggy_Anal_Finger:
        #the cock anal heading animation
    contains:
        "images/UI_Fingering.png"
        pos (172,480)#500
        alpha 0.8
        block:
            ease .5 ypos 460#450
            pause .25
            ease 1.75 ypos 480#500
            repeat
image Yana_Doggy_Anal_Fingering_Mask:
    #the masking animation for the anal heading
    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
#        yoffset 10
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Yana_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #Cock with mask
        AlphaMask("Zero_Yana_Doggy_Anal_Heading", "Yana_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .6
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .6 #.5
            repeat

image Zero_Yana_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Yana_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Yana_Doggy_Anal_Heading_Mask:
    #the masking animation for the anal heading
    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,534)
        block:
            ease .5 ypos 518
            pause .25
            ease 1.75 ypos 534#518
            repeat

image Yana_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Yana_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Yana_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Yana_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Yana_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Yana_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "YanaX.Offhand == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "Ch_Focus is YanaX and 'dildo anal' in (Trigger,Trigger2)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "Ch_Focus is YanaX", AlphaMask("Zero_Yana_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", Null(),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Yana_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Yana_Doggy_Body"
        ypos 10#28
        pause .4
        block:
            ease .2 ypos 0#10
            pause .3
            ease 2 ypos 10#28
            repeat

image Yana_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Yana_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Yana_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Yana_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Yana_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in YanaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Yana_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Yana_Doggy_Body"
        ypos 5
        block:
            pause .15
            ease .1 ypos -10#0
            pause .1
            easein .5 ypos 5#20
            pause .05
            repeat

image Yana_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Yana_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat


# Footjob animations > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Yana_Doggy_Feet0:
    #static animation
    contains:
        "Yana_Doggy_Feet_Under"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (160,480)  #(145,480)
    contains:
        "Yana_Doggy_Feet_Over"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Yana_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Yana_Doggy_Body"
        ypos 10#28
        #pause .4
        block:
            pause .5
            ease 2 ypos 14
            pause .5
            ease 2 ypos 10
            repeat

image Yana_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Yana_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause .1 #.5
            ease 2 ypos 10
            pause .5
            ease 2.4 ypos 0
            repeat


image Yana_Doggy_Feet1:
    #slow animation
    contains:
        "Yana_Doggy_Feet_Under"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Yana_Doggy_Feet_Over"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Yana_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Yana_Doggy_Body"
        ypos 0#28
        block:
            pause .3
            ease 1.9 ypos 80
            ease .8 ypos 0#70
            repeat

image Yana_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Yana_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat


image Yana_Doggy_Feet2:
    #fast animation
    contains:
        "Yana_Doggy_Feet_Under"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Yana_Doggy_Feet_Over"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat

image Yana_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Yana_Doggy_Body"
        ypos 70#28
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Yana_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Yana_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Yana_Doggy_Launch(Line = Trigger):
    $ renpy.start_predict("images/YanaDoggy/*.*")
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Yana_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(YanaX,1) #call Rogue_Hide
    show Yana_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150
    with dissolve
    return

label Yana_Doggy_Reset:
    if not renpy.showing("Yana_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ YanaX.ArmPose = 2
    $ YanaX.SpriteVer = 0
    hide Yana_Doggy_Animation
    call Girl_Hide(YanaX) #call Rogue_Hide
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
                    alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Yana Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start Yana Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_SexSprite:
    LiveComposite(
        (1120,840),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Yana_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Yana_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Yana_Sex_Fucking_Speed3",
                        "Speed >= 2", "Yana_Sex_Fucking_Speed2",
                        "Speed", "Yana_Sex_Fucking_Speed1",
                        "True", "Yana_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Yana_Sex_Anal_Speed3",
                        "Speed >= 2", "Yana_Sex_Anal_Speed2",
                        "Speed", "Yana_Sex_Anal_Speed1",
                        "True", "Yana_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Yana_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Yana_Sex_Hotdog_Speed1",
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Yana_Sex_FJ_Speed2",
                        "Speed", "Yana_Sex_FJ_Speed1",
                        "True", "Yana_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Yana_Hotdog_Body_Anim2",
                "True", "Yana_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (700,200)#(650,303)
    zoom 1#0.85

# End Yana Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Yana_SexSprite
        (1120,840),
#        (0,-100), "images/YanaSex/Yana_Sex_Headref.png",
        (460,120), "Yana_HairBack_Sex",
        (0,0), "images/YanaSex/Yana_Sex_Body.png",

        (0,0), ConditionSwitch(
            #mesh arm layer
            "YanaX.Over == 'purple top'", "images/YanaSex/Yana_Sex_Over_Purple_Arm.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_Sex_Chest_Mesh_Arm.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket arm layer
            "YanaX.Acc == 'jacket'", "images/YanaSex/Yana_Sex_Jacket_Arm.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "YanaX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_Sex_Chest_Mesh_Up.png",
                    "YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_Sex_Chest_Bikini_Up.png",
#                    "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_Sex_Chest_Lace_Up.png",
                    "YanaX.Chest", "images/YanaSex/Yana_Sex_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_Sex_Chest_Mesh.png",
            "YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_Sex_Chest_Bikini.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_Sex_Chest_Lace.png",
            "YanaX.Chest", "images/YanaSex/Yana_Sex_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "YanaX.Water", "images/YanaSex/Yana_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress layer
            "YanaX.Uptop and YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Over_Dress_Up.png",
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Over_Dress.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "YanaX.Uptop", ConditionSwitch(
                    #if the top's down. . .
#                    "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Over_Towel.png",
                    "YanaX.Over == 'purple top'", "images/YanaSex/Yana_Sex_Over_Purple_Up.png",
                    "YanaX.Over == 'shirt'", "images/YanaSex/Yana_Sex_Over_Shirt_Up.png",
                    "YanaX.Over == 'corset'", "images/YanaSex/Yana_Sex_Over_Corset_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Over_Towel.png",
            "YanaX.Over == 'purple top'", "images/YanaSex/Yana_Sex_Over_Purple.png",
            "YanaX.Over == 'shirt'", "images/YanaSex/Yana_Sex_Over_Shirt.png",
            "YanaX.Over == 'corset'", "images/YanaSex/Yana_Sex_Over_Corset.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #necklace layer
            "YanaX.Neck == 'scarf'", "images/YanaSex/Yana_Sex_Scarf.png",
            "YanaX.Neck", "images/YanaSex/Yana_Sex_Neck.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket layer
            "YanaX.Acc == 'jacket'", "images/YanaSex/Yana_Sex_Jacket.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #over jacket layer layer
            "not YanaX.Uptop", Null(),
            "YanaX.Over == 'shirt' or YanaX.Chest", "images/YanaSex/Yana_Sex_Chest_Red_Over.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nipples layer
            "YanaX.Pierce == 'ring'", ConditionSwitch(
                    "YanaX.Uptop", "images/YanaSex/Yana_Sex_Nips_R.png",

                    "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Nips_R_Black.png",
                    "YanaX.Over == 'purple top'", "images/YanaSex/Yana_Sex_Nips_R_Purp.png",
                    "YanaX.Over", "images/YanaSex/Yana_Sex_Nips_R_Red.png",
                    "YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Nips_R_Black.png",
                    #"YanaX.Over == 'corset'", "images/YanaSex/Yana_Sex_Nips_R_Red.png",

                    "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_Sex_Nips_R_Mesh.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_Sex_Nips_R_Lace.png",
                    #"YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_Sex_Nips_R_Red.png",
                    "YanaX.Chest", "images/YanaSex/Yana_Sex_Nips_R_Red.png",
                    "True", "images/YanaSex/Yana_Sex_Nips_R.png",
                    ),
            "YanaX.Pierce", ConditionSwitch( #barbells
                    "YanaX.Uptop", "images/YanaSex/Yana_Sex_Nips_B.png",

                    "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Nips_B_Black.png",
                    "YanaX.Over == 'purple top'", "images/YanaSex/Yana_Sex_Nips_B_Purp.png",
                    "YanaX.Over", "images/YanaSex/Yana_Sex_Nips_B_Red.png",
                    "YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Nips_B_Black.png",
                    #"YanaX.Over == 'corset'", "images/YanaSex/Yana_Sex_Nips_B_Red.png",

                    "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_Sex_Nips_B_Mesh.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_Sex_Nips_B_Lace.png",
                    #"YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_Sex_Nips_B_Red.png",
                    "YanaX.Chest", "images/YanaSex/Yana_Sex_Nips_B_Red.png",
                    "True", "images/YanaSex/Yana_Sex_Nips_B.png",
                    ),
            "YanaX.Lust < 50 and not YanaX.OCount", Null(),                                                 #nips only poke at high lust
            "YanaX.Uptop", "images/YanaSex/Yana_Sex_Nips.png",

            "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Nips_Black.png",
            "YanaX.Over == 'purple top'", "images/YanaSex/Yana_Sex_Nips_Purp.png",
            "YanaX.Over", "images/YanaSex/Yana_Sex_Nips_Red.png",
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Nips_Black.png",
            #"YanaX.Over == 'corset'", "images/YanaSex/Yana_Sex_Nips_Red.png",

            "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_Sex_Nips_Mesh.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_Sex_Nips_Lace.png",
            #"YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_Sex_Nips_Red.png",
            "YanaX.Chest", "images/YanaSex/Yana_Sex_Nips_Red.png",
            "True", "images/YanaSex/Yana_Sex_Nips.png",
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Yana_Sex_Fondle_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #breast licking animation
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Yana_Sex_Lick_Breasts",
            "True", Null()
            ),
        (455,120), "Yana_Head_Sex",  #(50,-325)(335,-40)
#        (0,0), "images/YanaSex/Yana_Sex_HeadRef.png",
        )
#    yoffset -163
# End Yana Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Yana_Head_Sex:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
            # Face background plate
            "YanaX.Blush >= 2", "images/YanaSprite/Yana_Sprite_Head_Blush2.png",
            "YanaX.Blush", "images/YanaSprite/Yana_Sprite_Head_Blush1.png",
            "True", "images/YanaSprite/Yana_Sprite_Head.png",
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "YanaX.Mouth == 'lipbite'", "images/YanaSprite/Yana_Sprite_Mouth_Lipbite.png",
            "YanaX.Mouth == 'sucking'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
            "YanaX.Mouth == 'kiss'", "images/YanaSprite/Yana_Sprite_Mouth_Kiss.png",
            "YanaX.Mouth == 'sad'", "images/YanaSprite/Yana_Sprite_Mouth_Sad.png",
            "YanaX.Mouth == 'smile'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
            "YanaX.Mouth == 'surprised'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
#            "not Player.Male and 'mouth' in YanaX.Spunk and YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Mouth_Tongue_Wet.png",
            "YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Mouth_Tongue.png",
            "YanaX.Mouth == 'grimace'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
            "YanaX.Mouth == 'smirk'", "images/YanaSprite/Yana_Sprite_Mouth_Smirk.png",
            "YanaX.Mouth == 'open'", "images/YanaSprite/Yana_Sprite_Mouth_Open.png",
            "True", "images/YanaSprite/Yana_Sprite_Mouth_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in YanaX.Spunk or not Player.Male", Null(),
            "YanaX.Mouth == 'sucking'", "images/YanaSprite/Yana_Sprite_Spunk_Tongue.png",
#            "YanaX.Mouth == 'kiss'", "images/YanaSprite/Yana_Sprite_Spunk_Kiss.png",
#            "YanaX.Mouth == 'sad'", "images/YanaSprite/Yana_Sprite_Spunk_Sad.png",
#            "YanaX.Mouth == 'smirk'", "images/YanaSprite/Yana_Sprite_Spunk_Sad.png",
#            "YanaX.Mouth == 'lipbite'", "images/YanaSprite/Yana_Sprite_Spunk_Sad.png",
            "YanaX.Mouth == 'surprised'", "images/YanaSprite/Yana_Sprite_Spunk_Tongue.png",
#            "YanaX.Mouth == 'open'", "images/YanaSprite/Yana_Sprite_Spunk_Open.png",
            "YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Spunk_Tongue.png",
            "True", "images/YanaSprite/Yana_Sprite_Spunk_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in YanaX.Spunk and 'chin' not in YanaX.Spunk", Null(),
            "YanaX.Mouth == 'tongue'", "images/YanaSprite/Yana_Sprite_Wet_MouthTongue.png",
            "'chin' in YanaX.Spunk", "images/YanaSprite/Yana_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "YanaX.Brows == 'angry'", "images/YanaSprite/Yana_Sprite_Brows_Angry.png",
            "YanaX.Brows == 'sad'", "images/YanaSprite/Yana_Sprite_Brows_Sad.png",
            "YanaX.Brows == 'surprised'", "images/YanaSprite/Yana_Sprite_Brows_Surprised.png",
            "YanaX.Brows == 'confused'", "images/YanaSprite/Yana_Sprite_Brows_Confused.png",
            "True", "images/YanaSprite/Yana_Sprite_Brows_Normal.png",
            ),
        (0,0), "Yana Blink",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #hair over
#            "renpy.showing('Yana_BJ_Animation')", Null(),
#            "renpy.showing('Yana_SexSprite')", "images/YanaSex/Yana_Sprite_Hair_Long_UnderSex.png",

            "YanaX.Hair == 'wetlong' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaSprite/Yana_Sprite_Hair_Long_Wet_Sex.png",
            "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaSprite/Yana_Sprite_Hair_Long_Wet_Sex.png",
            "YanaX.Hair == 'wet' or YanaX.Water", "images/YanaSprite/Yana_Sprite_Hair_Short_Wet.png",
            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaSprite/Yana_Sprite_Hair_Short_Wet.png",
            "YanaX.Hair == 'long'", "images/YanaSprite/Yana_Sprite_Hair_Long_Sex.png",
            "True", "images/YanaSprite/Yana_Sprite_Hair_Short.png",
            ),
        (0,0), ConditionSwitch(
                #hairband
                "not YanaX.Hat",Null(),
                "True", "images/YanaSprite/Yana_Sprite_Headband.png",
                ),
        (0,0), ConditionSwitch(
            #Hair Water
            "YanaX.Water", "images/YanaSprite/Yana_Sprite_Water_Face.png",
            "not Player.Male and 'facial' in YanaX.Spunk", "images/YanaSprite/Yana_Sprite_Water_Face.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Hair.png",
            "'facial' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .37#.5
    transform_anchor True
#    rotate -10
#    alpha 0.7

image Yana_Head_Sexb:
    # The head used for the sex pose, referenced by Yana_Sex_Body
    "Yana_Sprite_Head"
    zoom 1.0#1.24
    anchor (0.5,0.5)
    rotate 20#17
#    alpha 0.5

image Yana_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Yana_Sex_Body
    "Yana_Sprite_HairBack"
    zoom .9#1.36
    anchor (0.5,0.5)
#    rotate 20#15


image Yana_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.5
        offset (490,340)#(390,620)

image Yana_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom .93#1.5
        offset (360,0)#(190,-200)

# Start Yana Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Yana_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not YanaX.Wet", Null(),
            "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
            "YanaX.Panties and not YanaX.PantiesDown", Null(),
            "Player.Cock == 'foot'", Null(),
            "YanaX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in YanaX.Spunk or not Player.Male", Null(),
            "Player.Cock == 'foot'", Null(),
            "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
            "YanaX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #skin behind hose layer
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "YanaX.Panties and YanaX.PantiesDown", Null(),
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/YanaSex/Yana_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Yana_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/YanaSex/Yana_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/YanaSex/Yana_Sex_Ass.png",
            "True", "images/YanaSex/Yana_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "YanaX.Red", "images/YanaSex/Yana_Sex_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/YanaSex/Yana_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not YanaX.Water", Null(),
            "True", "images/YanaSex/Yana_Sex_Water_Legs.png",
            ),

        (0,0), "Yana_Sex_Anus",
            #Anus Composite

        (0,0), "Yana_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_Sex_Hose_StockingsGarter.png",
            "YanaX.Hose == 'socks'", "images/YanaSex/Yana_Sex_Hose_Socks.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaSex/Yana_Sex_Hose_Garter.png",
            "YanaX.Hose == 'stockings'", "images/YanaSex/Yana_Sex_Hose_Stockings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "YanaX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
                    "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Panties_Lace_Down.png",
                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Panties_Bikini_Down.png",
                    "YanaX.Panties", "images/YanaSex/Yana_Sex_Panties_Gray_Down.png",
                    "True", Null(),
                    ),
            "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Panties_Lace.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Panties_Bikini.png",
            "YanaX.Panties and YanaX.Wet", "images/YanaSex/Yana_Sex_Panties_Gray_Wet.png",
            "YanaX.Panties", "images/YanaSex/Yana_Sex_Panties_Gray.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "YanaX.Panties and YanaX.PantiesDown", Null(),
#            "YanaX.Hose == 'tights'", "images/YanaSex/Yana_Sex_Hose_Tights.png",
#            "YanaX.Hose == 'ripped tights'", "images/YanaSex/Yana_Sex_Hose_Tights_Holed.png",
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_Hose_Pantyhose.png",
            "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "YanaX.Legs == 'skirt'", "images/YanaSex/Yana_Sex_Legs_Skirt.png",
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Legs_Dress.png",
            "YanaX.Legs == 'pants' and YanaX.Upskirt", "images/YanaSex/Yana_Sex_Legs_Pants_Down.png",
            "YanaX.Legs == 'pants' and YanaX.Wet > 1", "images/YanaSex/Yana_Sex_Legs_Pants_Wet.png",
            "YanaX.Legs == 'pants'", "images/YanaSex/Yana_Sex_Legs_Pants.png",
            "YanaX.Legs == 'shorts' and YanaX.Upskirt", "images/YanaSex/Yana_Sex_Legs_Shorts_Down.png",
            "YanaX.Legs == 'shorts' and YanaX.Wet > 1", "images/YanaSex/Yana_Sex_Legs_Shorts_Wet.png",
            "YanaX.Legs == 'shorts'", "images/YanaSex/Yana_Sex_Legs_Shorts.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
            "not YanaX.Pierce", Null(),
            "YanaX.Legs == 'dress' or YanaX.Legs == 'skirt'", Null(),
            "Player.Sprite and Player.Cock == 'in' and Speed", Null(),
            "YanaX.Pierce == 'ring'",ConditionSwitch(
                    "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_R_Black.png",
                    "YanaX.Legs == 'shorts' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_R_Black.png",

                    "YanaX.PantiesDown", Null(), #"images/YanaSex/Yana_Sex_Pierce_Pussy_R.png",
                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Pierce_R_Red.png",
                    "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_Pierce_R_Lace.png",
                    "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Pierce_R_Lace.png",
                    "YanaX.Panties", "images/YanaSex/Yana_Sex_Pierce_R_Gray.png",
                    "True", Null(), #"images/YanaSex/Yana_Sex_Pierce_R.png",
                    ),
            #else, it's barbell
            "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_B_Black.png",
            "YanaX.Legs == 'shorts' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_B_Black.png",

            "YanaX.PantiesDown", Null(), #"images/YanaSex/Yana_Sex_Pierce_B.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Pierce_B_Red.png",
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_Pierce_B_Lace.png",
            "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Pierce_B_Lace.png",
            "YanaX.Panties", "images/YanaSex/Yana_Sex_Pierce_B_Gray.png",
            "True", Null(), #"images/YanaSex/Yana_Sex_Pierce_B.png",
            ),
        (0,0), ConditionSwitch(
            #towel Layer
            "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Foot2.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Yana_Hotdog_Zero_Anim2",
#            "Speed", "Yana_Hotdog_Zero_Anim1",
#            "True", "Yana_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Yana_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Yana_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Trigger3 == 'fondle pussy' and YanaX.Lust > 60 and not (Player.Sprite)",  At("YanaFingerHand", GirlFingerPussyX()), #"Yana_Sex_Mast2",
            "Trigger3 == 'fondle pussy'", At("YanaMastHand", GirlGropePussyX()), #"Yana_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Yana_Sex_Fondle_Pussy",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png"),
#            "ShowFeet", "Yana_Sex_Feet",
#            "Player.Sprite", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png"),
            "True", "Yana_Sex_Foot",
#            "True", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png"),
            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Yana_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_FeetMask.png"),
#            "True", "Yana_Sex_Feet",
#            ),
        )
# End Yana Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Yana_Sex_Foot:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Yana_Sex_Legs
        (1120,840),
#        (0,0), "images/YanaSex/Yana_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(YanaX.Hose == 'pantyhose' or YanaX.Hose == 'ripped pantyhose') and YanaX.Panties and YanaX.PantiesDown", "images/YanaSex/Yana_Sex_Foot.png",
            "YanaX.Hose == 'socks'", "images/YanaSex/Yana_Sex_Foot_Socks.png",
            "YanaX.Hose == 'pantyhose' or YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_Foot_Pantyhose.png",
            "YanaX.Hose and YanaX.Hose != 'garterbelt'", "images/YanaSex/Yana_Sex_Foot_Stockings.png",
            "True", "images/YanaSex/Yana_Sex_Foot.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not YanaX.Water", Null(),
            "True", "images/YanaSex/Yana_Sex_Water_Foot.png",
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Foot.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants layer
            "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Foot_Pants.png",
            "True", Null(),   #Null(),
            ),
        )

image Yana_Sex_Foot_Over:
        #this is the foot part that goes over the cock in the fj pose
        contains:
            AlphaMask("Yana_Sex_Foot", "images/YanaSex/Yana_Sex_Foot_Mask.png")
#        contains:
#            ConditionSwitch(
#                "'feet' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Foot.png",
#                "True", Null(),
#                )

# Start Yana Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Yana_Sex_Heading_Pussy",
                "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'out')", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "Trigger3 == 'fondle pussy' and YanaX.Lust > 60", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "True", "images/YanaSex/Yana_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not YanaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/DoreenSex/Doreen_Sex_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not YanaX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/YanaSex/Yana_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Trigger == 'lick pussy'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Trigger3 == 'fondle pussy' and YanaX.Lust > 60", "images/YanaSex/Yana_Sex_Pubes_Open.png",
                "True", "images/YanaSex/Yana_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in YanaX.Spunk or not Player.Male", Null(),
                "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
                "YanaX.Panties and not YanaX.PantiesDown", Null(),
                "True", AlphaMask("Spunk_Drip2","Yana_Sex_Drip_Mask"),
                )
            offset (545,540)

    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in YanaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in YanaX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in YanaX.Spunk", "images/YanaSex/Yana_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "YanaX.Panties and YanaX.PantiesDown", Null(),
#                "YanaX.Hose == 'ripped pantyhose' and ShowFeet", "images/YanaSex/Yana_Sex_Hose_Pantyhose_Holed.png",
#                "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Yana_Sex_Fucking_Zero_Anim3", "Yana_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Yana_Sex_Fucking_Zero_Anim2", "Yana_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Yana_Sex_Fucking_Zero_Anim1", "Yana_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Yana_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
    contains:
            #Piercings
            ConditionSwitch(
#                "YanaX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/YanaSex/Yana_Sex_Pierce_Pussy_BarbellF.png",
                "YanaX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/YanaSex/Yana_Sex_Pierce_R_Fucking.png",
                "YanaX.Pierce == 'barbell'", "images/YanaSex/Yana_Sex_Pierce_B.png",
                "YanaX.Pierce == 'ring'", "images/YanaSex/Yana_Sex_Pierce_R.png",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Yana_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Speed == 1", Null(),
                "'in' not in YanaX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
#                "Speed <= 1", Null(), #"Yana_Pussy_Spunk_Heading",
                "True", "Yana_Sex_Spunk",
                )

    #End Yana Pussy composite


image Yana_Sex_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Mask_Anal.png"
        offset (-545,-450)#(-275,-560)#(-145,-560)#(-225,-560)

image Yana_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Yana_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,580)#(535,550)

image Yana_Sex_Fondle_Pussy:
        "GropePussy_Yana"
        xzoom -1.2
        yzoom 1.2
        offset(-530,-150) #(-710,-450)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Yana_Sex_Spunk:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
        anchor (0.5,0)
        transform_anchor True
        xoffset 560
        yoffset 3
        xzoom .9

#End Animations for Yana's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Zero_Cock:
        #this is the cock generally used by Yana's sex pose
        contains:
            subpixel True
            ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
            subpixel True
            anchor (0.5,1.0)
            transform_anchor True
            offset (1230,1620) #(546,1170)
            zoom 1.3

image Yana_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Yana_Sex_Speed2" and "Yana_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 3

# Start Yana Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Static:
    # Pose for Yana's Sex Pose in which she is static
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.3
#                ease 1.4 ypos -185 #-120
#                pause .3
#                ease 1.25 ypos -180 #-130
#                ease 0.15 ypos -177 #-130
#                ease 0.1 ypos -180 #-130
#                repeat
    contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            transform_anchor True
            anchor (0.5,0.9)
            pos (530,540)#(-800,-800)   #(0,-180)
            rotate 0
            block: #3.5 total
#                pause 0.3
                easein 1.5 rotate 0 #-120
                pause .3
                ease 1.4 rotate -5 #-130
                ease 0.2 rotate 15 #-130
                easeout 0.1 rotate 10 #-130
#                pause 0.3
                repeat

#    contains:
#            Yana's Feet
#            subpixel True
#            "Yana_Sex_Feet"
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png"),
#                "True", Null(),
#                )
#            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.3
#                ease 1.4 ypos -185 #-120
#                pause .3
#                ease 1.25 ypos -180 #-130
#                ease 0.15 ypos -177 #-130
#                ease 0.1 ypos -180 #-130
#                repeat

# End Yana Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Yana Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Fucking_Speed0:
    # Pose for Yana's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Yana_Sex_Fucking_Zero_Anim0:
        #this is Yana's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (0,60)#(498,530)
            block:
                pause 0.2
                easeout 1 ypos 50 #-140
                easein .8 ypos 45 #-140
                pause 1.4
                easeout 0.6 ypos 60 #-140
                easein 1 ypos 60 #-10
                repeat


#            pos (0,40)#(498,530)
#            block:
#                pause 0.2
#                easeout 1 ypos 20 #-140
#                easein .8 ypos 10 #-140
#                pause 1.4
#                easeout 0.6 ypos 10 #-140
#                easein 1 ypos 40 #-10
#                repeat

# End Yana Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Fucking_Speed1:
    # Pose for Yana's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 1
                ease 1.5 ypos -190 #0
                pause 1.6
                ease 0.9 ypos -180 #-130
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Yana_Sex_Fucking_Zero_Anim1:
        #this is Yana's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
#                ease 0.95 ypos -145
                ease 2 ypos -10#-10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Yana_Sex_Heading_Mask:
        #This is the mask image for Yana's heading pussy
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 1.8 yoffset 0#3
                pause 1#0.8
                ease 2 yoffset 10
                repeat


image Yana_Sex_Heading_Pussy:
        #This is the image for Yana's heading pussy growing
#        contains:
#            "images/YanaSex/Yana_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/YanaSex/Yana_Sex_Pussy_Fucking.png"
            anchor (0.5,0)
            transform_anchor True
            subpixel True
            xoffset 560
            xzoom .7
            block:
                pause 0.2
                ease 1.2 xzoom 1
                ease .4 xzoom 1#.9
                pause 1.2
                ease .2 xzoom 1
                ease 1.8 xzoom .7
                repeat
        contains:
            "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
            anchor (0.5,0.75)
            transform_anchor True
            subpixel True
            xoffset 560
            yoffset 560
            xzoom .7
            alpha 0.3
            parallel:
                pause 0.2
                ease 1.2 xzoom 1
                ease .4 xzoom .9
                pause 1.2
                ease .2 xzoom 1
                ease 1.8 xzoom .7
                repeat
            parallel:
                pause 0.2
                ease 1.2 yzoom 1
                ease .4 yzoom .9
                pause 1.2
                ease .2 yzoom 1
                ease 1.8 yzoom .7
                repeat

#image Kitty_Sex_Pussy_Hole:
#    "images/YanaDoggy/Yana_Doggy_Pussy_HHole.png"
#    transform_anchor True
#    anchor (212,580)#(210,600)
#    pos (558,580)#(400,-10)
#    xzoom 0.8
#    parallel:
#        ease 1 yzoom 1.2
#        pause 1
#        ease 3 yzoom 1
#        repeat
#    parallel:
#        ease 1 xzoom 1.2
#        pause 2
#        ease 2  xzoom 0.8
#        repeat

image Yana_Pussy_Spunk_Heading:
        #This is the image for Yana's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in YanaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
            anchor (0.5,0)
            transform_anchor True
            xoffset 560
            yoffset 5
            xzoom .7
            block:
                pause 0.7
                ease 0.7 xzoom .9
#                ease .4 xzoom .9#.9
                pause 1.8
#                ease .2 xzoom .9
                ease 1.8 xzoom .7
                repeat

# End Yana Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Fucking_Speed2:
    # Pose for Yana's Sex Pose in which she is fucking at speed 2
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-170) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.5
                ease .9 ypos -190 # 0
                pause 0.8
                ease 2.0 ypos -170 # -130
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
# End main animation for Sex Pose Fucking Speed 2


image Yana_Sex_Fucking_Zero_Anim2:
        #this is Yana's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            pos (0,20)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -100 # -145
                ease 0.25 ypos -90 # -140
                pause .8
                ease 2 ypos 20 #-10
                repeat

# End Yana Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Fucking_Speed3:
    # Pose for Yana's Sex Pose in which she is fucking at speed 3
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.5
                ease 0.4 ypos -200
                pause 0.1
#                pause 0.35
                ease 0.8 ypos -170
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat

# End main animation for Sex Pose Fucking Speed 3


image Yana_Sex_Fucking_Zero_Anim3:
        #this is Yana's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            pos (0,10)
            block:
                pause 0.1
                ease 0.55 ypos -100
                ease 0.15 ypos -90
                pause 0.25
                ease 0.75 ypos 10
                repeat

# End Yana Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Yana's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Yana's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/BetsySex/Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/BetsySex/Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Yana_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Yana_Sex_Anal_Tip",
            "YanaX.Plug", "images/PlugBase_Sex.png",
            "YanaX.Loose > 2", "Yana_Gape_Anal_Sex",
#            "YanaX.Loose", "images/YanaSex/Yana_Sex_Anus_Loose.png",
            "True", "images/YanaSex/Yana_Sex_Anus.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in YanaX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/YanaSex/Yana_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Yana_Sex_Anal_Spunk_Heading_Under",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
                )
            yoffset 5
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Yana_Sex_Anal_Zero_Anim3", "Yana_Sex_Anal_MaskF"),
                "Speed >= 2", AlphaMask("Yana_Sex_Anal_Zero_Anim2", "Yana_Sex_Anal_MaskF"),
                "Speed", AlphaMask("Yana_Sex_Anal_Zero_Anim1", "Yana_Sex_Anal_Mask"),
                "True", AlphaMask("Yana_Sex_Anal_Zero_Anim0", "Yana_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in YanaX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Yana_Sex_Anal_Spunk_Heading_Over",
                "True", "Yana_Sex_Anal_Spunk",
                )

image Yana_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/JubesSex/Jubes_Sex_Anal.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,625)#(218,518)
            zoom .4 # tight
            block:
                ease 3 zoom .50 #in.87
                ease 3 zoom .40 #out
                repeat

image Yana_Sex_Anal_Spunk:
    ConditionSwitch(
                "'anal' in YanaX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23#68
    xzoom .9#1.2

image Yana_Sex_Anal_Mask:
        #This is the mask image for small stuff
        # Used in "Yana_Sex_Speed2" and "Yana_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Anal.png"
            yoffset 98 #-9
            xoffset 3 #3
#            xoffset -5

image Yana_Sex_Anal_MaskF:
        #This is the mask image for deep stuff
        # Used in "Yana_Sex_Speed2" and "Yana_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_AnalB.png"
            yoffset 98 #-9
            xoffset 3



# Start Yana Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Anal_Speed0:
    # Pose for Yana's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Yana_Sex_Anal_Zero_Anim0:
        #this is Yana's sex animation, Speed 0 Anal
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,135)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 130 #90
                pause .8
                ease 2 ypos  135 #130
                repeat

image Yana_Sex_Anal_Tip:
    "images/BetsySex/Betsy_Sex_Anus.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    yoffset -20
    xzoom 0.4
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 xzoom 0.55   #.75 (1.0)
        pause 0.5   #
        ease .25 xzoom 0.55  #(1.0)
        ease 2.25 xzoom 0.4   #(0.6)
        repeat

# End Yana Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Anal_Heading:
    "images/BetsySex/Betsy_Sex_Anus.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    yoffset -20
    xzoom 0.6
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 xzoom 1.0   #.75 (1.0)
        pause 0.5   #
        ease .25 xzoom 1.0  #(1.0)
        ease 2.25 xzoom 0.6   #(0.6)
        repeat

image Yana_Sex_Anal_Spunk_Heading_Over:
    ConditionSwitch(
                "'anal' in YanaX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23
    xzoom 0.6
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 xzoom 0.9   #.75 (1.0)
        pause 0.5   #
        ease .25 xzoom 0.9 #(1.0)
        ease 2.25 xzoom 0.6   #(0.6)
        repeat


#    yoffset -23#68
#    xzoom .9#1.2

image Yana_Sex_Anal_Spunk_Heading_Under:
    "images/JubesSex/Jubes_Sex_Spunk_Anal.png"
    anchor (0.5,0.5)
    pos (560,420)#(0.5,0.5)
#    xzoom 0.6
#    block:
#        #total 5 second
#        ease .75 xzoom 1.0
#        ease .25 xzoom 0.95
#        pause 1.50
#        ease .25 xzoom 1.0
#        ease 2.25 xzoom 0.6
#        repeat

image Yana_Sex_Anal_Speed1:
    # Pose for Yana's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Yana_Sex_Anal_Zero_Anim1:
        #this is Yana's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,130)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 90 #40
                pause .8
                ease 2 ypos  130 #90
                repeat

# End Yana Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Anal_Speed2:
    # Pose for Yana's Sex Pose in which she is doing anal at speed 2
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 1.0 ypos -200
                pause .9
                ease 1.7 ypos -180
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.95 ypos -215
                ease 0.25 ypos -210
                pause .8
                ease 1.8 ypos -180
                repeat
#    contains:
#            #Zero's cock in the sex pose
#            AlphaMask("Yana_Sex_Fucking_Zero_Anim2", "Yana_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Yana_Sex_Anal_Zero_Anim2:
        #this is Yana's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,-10)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -25
                ease 0.25 ypos -20
                pause .8
                ease 2 ypos 90
                repeat

# End Yana Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Anal_Speed3:
    # Pose for Yana's Sex Pose in which she is Anal at speed 3
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .5 ypos -180
                ease .4 ypos -200
                pause .4
                ease .5 ypos -185
                repeat

    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.4
                easein 0.4 ypos -180
                ease 0.3 ypos -215
                ease 0.1 ypos -210
                pause 0.4
                easeout 0.6 ypos -185
                repeat
# End main animation for Sex Pose Fucking Speed 3


image Yana_Sex_Anal_Zero_Anim3:
        #this is Yana's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            pos (3,-40)
            block:
                pause 0.1
                ease 0.55 ypos -25
                ease 0.15 ypos -20
                pause 0.25
                ease 0.75 ypos 90
                repeat

# End Yana Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Yana Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Hotdog_Speed1:
    # Pose for Yana's Sex Pose in which she is hotdogging at speed 1 (slow)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.8
                ease 0.8 ypos -190 #-120
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.4
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 0.7 ypos -200 #-120
                ease 0.2 ypos -195 #-130
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.5
                repeat
    contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            pos (0,-180)
            block:
                pause 0.3
                ease 1.0 ypos -330 #-120
                pause .5
                ease 1.5 ypos -175 #-130
                ease 0.2 ypos -180 #-130
#                pause 0.3
                repeat
#    contains:
#            #Yana's Feet
#            subpixel True
#            "Yana_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_FeetMask.png"),
##                "True", Null(),
##                )
#            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.6
#                ease 0.7 ypos -200 #-120
#                ease 0.2 ypos -195 #-130
#                pause .5
#                ease 1.0 ypos -180 #-130
#                pause 0.5
#                repeat

# End main animation for Sex Pose Hotdog Speed 1

# End Yana Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_Hotdog_Speed2:
    # Pose for Yana's Sex Pose in which she is hotdogging at speed 2 (fast)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.25
                ease 0.45 ypos -195 #-120
                pause .1
                ease 0.8 ypos -180 #-130
#                pause 0.2
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.1
                ease 0.4 ypos -215 #-120
                ease 0.1 ypos -205 #-130
                pause 0.25
                ease 0.75 ypos -180 #-130
#                pause 0.25
                repeat
    contains:
            subpixel True
            "Yana_Sex_Zero_Cock"
            subpixel True
            pos (0,-180)
            block:
#                pause 1.2
                ease 0.5 ypos -330 #-120
                pause 0.25
                ease 0.75 ypos -205 #-130
                ease 0.1 ypos -210 #-130
#                pause 0.3
                repeat
#    contains:
#            #Yana's Feet
#            subpixel True
#            "Yana_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_FeetMask.png"),
##                "True", Null(),
##                )
#            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.1
#                ease 0.4 ypos -215 #-120
#                ease 0.1 ypos -205 #-130
#                pause 0.25
#                ease 0.75 ypos -180 #-130
##                pause 0.25
#                repeat

# End main animation for Sex Pose Hotdog Speed 2

# End Yana Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Yana Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_FJ_Speed0:
    # Pose for Yana's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            anchor (800,325)#(410,470)
            offset (1025,440)    #(840,390)
            transform_anchor True
            rotate 25
            pos (50,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos 0#-40 #-140
                pause 0.8
                ease 2 ypos 5#-60 #-180
                pause 0.2
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            anchor (800,325)#(410,470)
            offset (1020,490)    #(560,390)
            transform_anchor True
            rotate 40
            pos (70,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 2 ypos 0 #10
                pause 0.8
                ease 2 ypos 10 #0
                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot"
            anchor (800,325)#(410,470)
            offset (1020,490)    #(560,390)
            transform_anchor True
            rotate 40
            pos (70,10) #X less is left, Y less is up (200,-180)
            parallel:
                pause 0.2
                ease 2 ypos 0 #10
                pause 0.8
                ease 2 ypos 10 #0
                repeat
#            parallel:
#                pause 0.2
#                ease 2 rotate 40 #10
#                pause 0.8
#                ease 2 rotate 35 #0
#                repeat
    contains:
            subpixel True
#            "Yana_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .4#.5
            subpixel True
            pos (550,550) #(630,520)
            rotate -5 #0
            parallel:
                pause 0.2
                ease 2 rotate 0 #10
                pause 0.8
                ease 2 rotate -5 #0
                repeat
#    contains:
#            #Yana's Legs
#            subpixel True
#            "Yana_Sex_Foot_Over"
##            alpha 0.5
##            AlphaMask("Yana_Sex_Feet", "images/YanaSex/Yana_Sex_Feet_Mask.png")
#            pos (50,-270) #X less is left, Y less is up (80,0)
#            block: #adds to 5
##                pause 0.2
#                ease 2 ypos -290 #10
#                pause 0.8
#                ease 2 ypos -270 #0
#                pause 0.2
#                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Yana Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_FJ_Speed1:
    # Pose for Yana's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            anchor (800,325)#(410,470)
            offset (845,340)    #(840,390)
            transform_anchor True
            rotate 25
            pos (50,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 1 ypos 0#-40 #-140
                pause 0.8
                ease 1 ypos 5#-60 #-180
                pause 0.2
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            anchor (800,325)#(410,470)
            offset (840,390)    #(560,330)
            transform_anchor True
            rotate 40
            pos (70,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 1 ypos 0 #10
                pause 0.8
                ease 1 ypos 10 #0
                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot"
            anchor (800,325)#(410,470)
            offset (840,395)    #(560,330)
            transform_anchor True
            rotate 35
            pos (70,0) #X less is left, Y less is up (200,-180)
            parallel:
#                pause 0.2
                ease 1.2 rotate 50 #10
                pause 0.8
                ease 1 rotate 35 #0
                repeat
    contains:
            subpixel True
#            "Yana_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .4#.5
            subpixel True
            pos (550,550) #(630,520)
            rotate -5 #0
            parallel:
                pause 0.2
                ease 1 rotate -10 #10
                pause 0.8
                ease 1 rotate -5 #0
                repeat
#    contains:
#            #Yana's Feet
#            subpixel True
#            "Yana_Sex_Foot_Over"
#            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
#            transform_anchor True
#            rotate 35
#            pos (70,0) #X less is left, Y less is up (200,-180)
#            parallel:
#                pause 0.2
#                ease 1 rotate 50 #10
#                pause 0.8
#                ease 1 rotate 35 #0
#                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Yana Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_Sex_FJ_Speed2:
    # Pose for Yana's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            anchor (800,325)#(410,470)
            offset (845,280)    #(840,390)
            transform_anchor True
            rotate 25
            pos (50,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 0.5 ypos 0#-40 #-140
#                pause 0.8
                ease 0.5 ypos 5#-60 #-180
                pause 0.1
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_Sex_Legs"
            anchor (800,325)#(410,470)
            offset (840,330)    #(560,330)
            transform_anchor True
            rotate 40
            pos (70,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.1
                ease 0.5 ypos 0 #10
#                pause 0.8
                ease 0.5 ypos 10 #0
                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot"
            anchor (800,325)#(410,470)
            offset (840,345)    #(560,330)
            transform_anchor True
            rotate 35
            pos (70,0) #X less is left, Y less is up (200,-180)
            parallel:
                pause 0.1
                ease 0.5 rotate 55 #10
#                pause 0.2
                ease 0.5 rotate 45 #0
                repeat
    contains:
            subpixel True
#            "Yana_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .4#.5
            subpixel True
            pos (550,550) #(630,520)
            rotate -5 #0
            parallel:
                pause 0.1
                ease 0.5 rotate -10 #10
#                pause 0.2
                ease 0.5 rotate -5 #0
                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot_Over"
            anchor (800,325)#(410,470)
            offset (840,345)    #(560,330)
            transform_anchor True
            rotate 35
            pos (70,0) #X less is left, Y less is up (200,-180)
            parallel:
                pause 0.1
                ease 0.5 rotate 55 #10
#                pause 0.2
                ease 0.5 rotate 45 #0
                repeat

# End main animation for Sex Pose Footjob Speed 2

# End Yana Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Yana_Sex_Launch(Line = Trigger):
    $ renpy.start_predict("images/YanaSex/*.*")
    $ YanaX.Offhand = 0 if YanaX.Offhand == "hand" else YanaX.Offhand

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ YanaX.Pose = "doggy"
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(YanaX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(YanaX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if YanaX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ YanaX.Upskirt = 1
        $ Player.Cock = "out"
    elif Line == "foot":
        $ Player.Sprite = 1
        $ ShowFeet = 1
        $ Player.Cock = "foot"
    elif Line == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    elif Line == "dildo pussy":
        $ Player.Cock = 0 if Player.Cock == "in" else Player.Cock
    elif Line == "dildo anal":
        $ Player.Cock = 0 if Player.Cock == "anal" else Player.Cock
    else: #elif Line == "solo":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        if Trigger != "fondle pussy":
                $ Speed = 0

    if Player.Sprite:
        call Zero_Strapped(YanaX) #puts strap-on on.
    $ Trigger = Line

    if YanaX.Pose == "doggy":
            call Yana_Doggy_Launch(Line)
            return
    if renpy.showing("Yana_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(YanaX,1) #call Rogue_Hide
    show Yana_SexSprite zorder 150
    with dissolve
    return

label Yana_Sex_Reset:
    if renpy.showing("Yana_Doggy_Animation"):
        call Yana_Doggy_Reset
        return
    if not renpy.showing("Yana_SexSprite"):
        return
    $ YanaX.ArmPose = 2
    hide Yana_SexSprite
    call Girl_Hide(YanaX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5,0.0)
    with dissolve
    $ Speed = 0
    return


## End Yana Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


### End Yana Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Yana Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Yana BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Yana BJ element
#Yana BJ Over Sprite Compositing


image Yana_BJ_Animation:#                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            "Speed == 1", "Yana_BJ_Anim1",               #Licking
            "Speed == 2", "Yana_BJ_Anim2",               #Heading
            "Speed == 3", "Yana_BJ_Anim3",               #Sucking
            "Speed == 4", "Yana_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Yana_BJ_Anim5",               #Cumming High
            "Speed == 6", "Yana_BJ_Anim6",               #Cumming Deep
            "Speed == 0", "Yana_BJ_Anim0",               #Static
            ),
        )
    zoom .55
    transform_anchor True
    anchor (.5,.5)
    offset (300,0)

image Yana_BJ_Backdrop:
    #Her Body under the head
    LiveComposite(
        (600,1250),       #550,950
        (-500,120), ConditionSwitch(      #-375,250
            #blanket
            "'blanket' in YanaX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (130,100), "Yana_BJ_HairBack2", #(50,25)
        (0,0), "images/YanaSprite/Yana_Sprite_Arm.png",
            #back arm

        (0,0), ConditionSwitch(
            #Chest layer
            "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Over_Purple_Back.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Chest_Mesh_Arm.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #armlets
            "YanaX.Arms", "images/YanaSprite/Yana_Sprite_Armlets1.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket under
            "YanaX.Acc == 'jacket'", "images/YanaSprite/Yana_Sprite_Jacket_Back.png",         # right hand up/left down
            "True", Null(),
            ),
        (0,0), "images/YanaSprite/Yana_Sprite_Body.png",


        (0,0), ConditionSwitch(
            #Chest layer
            "YanaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Chest == 'bikini top' and (YanaX.Acc == 'jacket' or YanaX.Over == 'purple top')", "images/YanaSprite/Yana_Sprite_Chest_Bikini_Up_Jacket.png",
                    "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Chest_Bikini_Up.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Chest_Mesh_Up.png",
#                    "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Chest_Lace_Up.png",
                    "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Chest == 'bikini top' and YanaX.Acc == 'jacket'", "images/YanaSprite/Yana_Sprite_Chest_Bikini_Jacket.png",
            "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Chest_Bikini.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Chest_Mesh.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Chest_Lace.png",
            "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
##            "YanaX.Water and YanaX.ArmPose == 1", "images/YanaSprite/Yana_Sprite_Water1.png",
            "YanaX.Water", "images/YanaSprite/Yana_Sprite_Water.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress
            "not YanaX.Legs", Null(),
            "YanaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "YanaX.Legs == 'dress' and YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Legs_Dress_Up.png",
                        "YanaX.Legs == 'dress'", "images/YanaSprite/Yana_Sprite_Legs_Dress_Upskirt.png",
                        "True", Null(),
                        ),
            "YanaX.Legs == 'dress' and YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Legs_Dress_Uptop.png",
            "YanaX.Legs == 'dress'", "images/YanaSprite/Yana_Sprite_Legs_Dress.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "YanaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Over_Purple_Up.png",
                    "YanaX.Over == 'corset'", "images/YanaSprite/Yana_Sprite_Over_Corset_Up.png",
                    "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Over_Shirt_Up.png",
                    "YanaX.Over == 'towel' and YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Over_Towel_Up.png",
                    "YanaX.Over == 'towel'", "images/YanaSprite/Yana_Sprite_Over_Towel_Uptop.png",
                    "True", Null(),
                    ),
            "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Over_Purple.png",
            "YanaX.Over == 'corset'", "images/YanaSprite/Yana_Sprite_Over_Corset.png",
            "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Over_Shirt.png",
            "YanaX.Over == 'towel' and YanaX.Upskirt", "images/YanaSprite/Yana_Sprite_Over_Towel_Upskirt.png",
            "YanaX.Over == 'towel'", "images/YanaSprite/Yana_Sprite_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #armlets
            "YanaX.Arms", "images/YanaSprite/Yana_Sprite_Armlets2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket over
            "YanaX.Acc == 'jacket'", "images/YanaSprite/Yana_Sprite_Jacket.png",         # right hand up/left down
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Chest layer over jacket
            "not YanaX.Uptop", Null(),
            "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Over_Shirt_Over.png",
            "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Chest_Bikini_Over.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Chest_Mesh_Over.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Chest_Lace_Over.png",
            "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Chest_Bra_Over.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Nipples
            #Only does this if she has piercings, has no tops, or has her top up
            "YanaX.Pierce == 'ring'", ConditionSwitch(
                    "YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Nips_Ring.png",

                    "YanaX.Over == 'towel'", Null(),
                    "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Nips_Ring_Purp.png",
                    "YanaX.Over", "images/YanaSprite/Yana_Sprite_Nips_Ring_Red.png", #== 'shirt' or 'corset'
                    "YanaX.Legs == 'dress'", "images/YanaSprite/Yana_Sprite_Nips_Ring_Black.png",
#                    "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Nips_Ring_Red.png",

                    "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Nips_Ring_Red.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Nips_Ring_Mesh.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Nips_Ring_Lace.png",
                    "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Nips_Ring_Red.png",

                    "True", "images/YanaSprite/Yana_Sprite_Nips_Ring.png",
                    ),
            "YanaX.Pierce == 'barbell'", ConditionSwitch(
                    "YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Nips_Barbell.png",

                    "YanaX.Over == 'towel'", Null(),
                    "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Purp.png",
                    "YanaX.Over", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Red.png", #== 'shirt' or 'corset'
                    "YanaX.Legs == 'dress'", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Black.png",
#                    "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Red.png",

                    "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Red.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Mesh.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Lace.png",
                    "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Nips_Barbell_Red.png",

                    "True", "images/YanaSprite/Yana_Sprite_Nips_Barbell.png",
                    ),
            # if no piercings. . .

            "YanaX.Lust < 50 and not YanaX.OCount", Null(),                                                 #nips only poke at high lust
            "YanaX.Uptop", "images/YanaSprite/Yana_Sprite_Nips.png",

            "YanaX.Over == 'towel'", Null(),
            "YanaX.Over == 'purple top'", "images/YanaSprite/Yana_Sprite_Nips_Purp.png",               #== 'shirt' or 'corset'
            "YanaX.Over", "images/YanaSprite/Yana_Sprite_Nips_Red.png",               #== 'shirt' or 'corset'
            "YanaX.Legs == 'dress'", "images/YanaSprite/Yana_Sprite_Nips_Black.png",
#                    "YanaX.Over == 'shirt'", "images/YanaSprite/Yana_Sprite_Nips_Red.png",

            "YanaX.Chest == 'bikini top'", "images/YanaSprite/Yana_Sprite_Nips_Red.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSprite/Yana_Sprite_Nips_Mesh.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSprite/Yana_Sprite_Nips_Lace.png",
            "YanaX.Chest", "images/YanaSprite/Yana_Sprite_Nips_Red.png",

            "True", "images/YanaSprite/Yana_Sprite_Nips.png",

            ),

        (0,0), ConditionSwitch(
            #Necklaces
            "YanaX.Neck == 'scarf'", "images/YanaSprite/Yana_Sprite_Neck_Scarf.png",
            "YanaX.Neck", "images/YanaSprite/Yana_Sprite_Neck.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in YanaX.Spunk and Player.Male", "images/YanaSprite/Yana_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        (75,50), "Yana_BJ_HairBack", #(50,25)
#        (30,-300), ConditionSwitch(    #(30,-300)
#            #Hair overlay
#            "YanaX.Hair == 'wetlong' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",
#            "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",

#            "YanaX.Hair == 'long'","images/YanaBJFace/Yana_BJ_Hair_Long_Under.png",
#            "True", Null(),
#            ),
        )
#    anchor (0.5, 0.0)
    zoom 3.2#.80
    anchor (300,525)#(300,625)
    offset (-410,-100)#(-400,0)
#    offset (230,-650)#(60,0)

image Yana_BJ_HairBack:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(
            #Hair overlay
            "YanaX.Hair == 'wetlong' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",
            "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",

            "YanaX.Hair == 'long'","images/YanaBJFace/Yana_BJ_Hair_Long_Under.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .35#.40
    transform_anchor True
#    rotate -10

image Yana_BJ_HairBack2:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(
            #Hair overlay
            "YanaX.Hair == 'wetlong' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",
            "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",

            "YanaX.Hair == 'long'","images/YanaBJFace/Yana_BJ_Hair_Long_Under.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .25#.40
    transform_anchor True
#    rotate -10

image Yana_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
#        (0,0), ConditionSwitch(
#            #Hair back
#            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaBJFace/Yana_BJ_HairBackWet.png", #AlphaMask("images/YanaBJFace/Yana_BJ_HairBackWet.png", "Yana_BJ_Backdrop"),
#            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaBJFace/Yana_BJ_HairBackWet.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #scarf
            "YanaX.Neck == 'scarf' and renpy.showing('Yana_TJ_Animation')", "images/YanaBJFace/Yana_BJ_Scarf.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "YanaX.Blush > 1", "images/YanaBJFace/Yana_BJ_Head_Blush2.png",
            "YanaX.Blush", "images/YanaBJFace/Yana_BJ_Head_Blush1.png",
            "True",  "images/YanaBJFace/Yana_BJ_Head.png"
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "Player.Male and 'chin'  in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "Speed and renpy.showing('Yana_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/YanaBJFace/Yana_BJ_Mouth_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),#"Yana_BJ_MouthHeadingB",#Null(),                          #heading
                    "Speed == 3", "images/YanaBJFace/Yana_BJ_Mouth_Sucking.png", #sucking
                    "Speed == 4", "images/YanaBJFace/Yana_BJ_Mouth_Sucking.png", #deepthroat
                    "Speed == 6", "images/YanaBJFace/Yana_BJ_Mouth_Sucking.png", #cumming
                    "True", "images/YanaBJFace/Yana_BJ_Mouth_Sucking.png", #cumming
                    ),
            "renpy.showing('Yana_CUN_Animation') and Speed", "images/YanaBJFace/Yana_BJ_Mouth_Tongue.png",
            "Speed == 3 and renpy.showing('Yana_TJ_Animation')", "images/YanaBJFace/Yana_BJ_Mouth_Tongue.png",
            "Speed >= 5 and renpy.showing('Yana_TJ_Animation')", "images/YanaBJFace/Yana_BJ_Mouth_Tongue.png",
#            "YanaX.Mouth == 'normal'", "images/YanaBJFace/Yana_BJ_Mouth_Smile.png",
            "YanaX.Mouth == 'lipbite'", "images/YanaBJFace/Yana_BJ_Mouth_Lipbite.png",
            "YanaX.Mouth == 'sucking'", "images/YanaBJFace/Yana_BJ_Mouth_Heading.png",
            "YanaX.Mouth == 'kiss'", "images/YanaBJFace/Yana_BJ_Mouth_Kiss.png",
            "YanaX.Mouth == 'sad'", "images/YanaBJFace/Yana_BJ_Mouth_Sad.png",
#            "YanaX.Mouth == 'smile'", "images/YanaBJFace/Yana_BJ_Mouth_Smile.png",
#            "YanaX.Mouth == 'grimace'", "images/YanaBJFace/Yana_BJ_Mouth_Smile.png",
            "YanaX.Mouth == 'surprised'", "images/YanaBJFace/Yana_BJ_Mouth_Heading.png",
            "YanaX.Mouth == 'tongue'", "images/YanaBJFace/Yana_BJ_Mouth_Tongue.png",
            "True", "images/YanaBJFace/Yana_BJ_Mouth_Normal.png",
            ),
        (425,530), ConditionSwitch(  #(428,555)
            # Heading Mouth
            "not renpy.showing('Yana_BJ_Animation')", Null(),
            "Speed == 2", "Yana_BJ_MouthHeading",  #heading
            "Speed == 5", "Yana_BJ_MouthHigh", #cumming high
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in YanaX.Spunk and 'chin' not in YanaX.Spunk", Null(),
            "'chin' not in YanaX.Spunk and (YanaX.Mouth == 'tongue' or Speed)", "images/YanaBJFace/Yana_BJ_Wet_Tongue.png",
            "YanaX.Mouth == 'tongue' or Speed", "images/YanaBJFace/Yana_BJ_Wet_Tongue2.png",
            "'mouth' in YanaX.Spunk or 'chin' in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in YanaX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Yana_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/YanaBJFace/Yana_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/YanaBJFace/Yana_BJ_Spunk_Sucking_O.png", #sucking
                    "Speed == 4", "images/YanaBJFace/Yana_BJ_Spunk_Sucking_O.png", #deepthroat
                    "Speed == 6", "images/YanaBJFace/Yana_BJ_Spunk_Sucking_O.png", #cumming
                    "True", "images/YanaBJFace/Yana_BJ_Spunk_Tongue.png", #cumming
                    ),
            "(Speed == 3 or Speed >= 5) and renpy.showing('Yana_TJ_Animation')", "images/YanaBJFace/Yana_BJ_Spunk_Tongue.png",
#            "YanaX.Mouth == 'normal'", "images/YanaBJFace/Yana_BJ_Spunk_Smile.png",
#            "YanaX.Mouth == 'lipbite'", "images/YanaBJFace/Yana_BJ_Spunk_Lipbite.png",
#            "YanaX.Mouth == 'kiss'", "images/YanaBJFace/Yana_BJ_Spunk_Kiss.png",
#            "YanaX.Mouth == 'sad'", "images/YanaBJFace/Yana_BJ_Spunk_Kiss.png",
#            "YanaX.Mouth == 'smile'", "images/YanaBJFace/Yana_BJ_Spunk_Smile.png",
            "YanaX.Mouth == 'surprised'", "images/YanaBJFace/Yana_BJ_Spunk_Tongue.png",
            "YanaX.Mouth == 'tongue'", "images/YanaBJFace/Yana_BJ_Spunk_Tongue.png",
            "YanaX.Mouth == 'sucking'", "images/YanaBJFace/Yana_BJ_Spunk_Tongue.png", #fix add
            "True", "images/YanaBJFace/Yana_BJ_Spunk_Mouth.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            "YanaX.Brows == 'normal'", "images/YanaBJFace/Yana_BJ_Brows_Normal.png",
            "YanaX.Brows == 'angry'", "images/YanaBJFace/Yana_BJ_Brows_Angry.png",
            "YanaX.Brows == 'sad'", "images/YanaBJFace/Yana_BJ_Brows_Sad.png",
            "YanaX.Brows == 'surprised'", "images/YanaBJFace/Yana_BJ_Brows_Surprised.png",
            "YanaX.Brows == 'confused'", "images/YanaBJFace/Yana_BJ_Brows_Confused.png",
            "True", "images/YanaBJFace/Yana_BJ_Brows_Normal.png",
            ),
        (0,0), "Yana BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #cum on the face
            "'facial' in YanaX.Spunk and Player.Male", "images/YanaBJFace/Yana_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair overlay
            "YanaX.Hair == 'wetlong' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Over.png",
            "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Over.png",

            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaBJFace/Yana_BJ_Hair_Wet.png",
            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaBJFace/Yana_BJ_Hair_Wet.png",

            "YanaX.Hair == 'long'", "images/YanaBJFace/Yana_BJ_Hair_Long_Over.png",
            "True", "images/YanaBJFace/Yana_BJ_Hair_Short.png",
            ),
        (0,0), ConditionSwitch(
            #hairband
            "not YanaX.Hat",Null(),
            "True", "images/YanaBJFace/Yana_BJ_Headband.png",
            ),
        (0,0), ConditionSwitch(
            #Hair water overlay
            "not YanaX.Water and not (not Player.Male and 'facial' in YanaX.Spunk)", Null(),
            "True", "images/YanaBJFace/Yana_BJ_Water.png",
            ),
        (0,0), ConditionSwitch(
            #cum on the hair
            "'hair' in YanaX.Spunk and Player.Male", "images/YanaBJFace/Yana_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.1
    anchor (0.5, 0.5)
#end image Yana_BJ_Head:

image Yana BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "YanaX.Eyes == 'normal'", "images/YanaBJFace/Yana_BJ_Eyes_Normal.png",
            "YanaX.Eyes == 'sexy'", "images/YanaBJFace/Yana_BJ_Eyes_Sexy.png",
            "YanaX.Eyes == 'closed'", "images/YanaBJFace/Yana_BJ_Eyes_Closed.png",
            "YanaX.Eyes == 'surprised'", "images/YanaBJFace/Yana_BJ_Eyes_Surprised.png",
            "YanaX.Eyes == 'side'", "images/YanaBJFace/Yana_BJ_Eyes_Side.png",
            "YanaX.Eyes == 'leftside'", "images/YanaBJFace/Yana_BJ_Eyes_Leftside.png",
            "YanaX.Eyes == 'stunned'", "images/YanaBJFace/Yana_BJ_Eyes_Stunned.png",
            "YanaX.Eyes == 'down'", "images/YanaBJFace/Yana_BJ_Eyes_Down.png",
            "YanaX.Eyes == 'manic'", "images/YanaBJFace/Yana_BJ_Eyes_Surprised.png",
            "YanaX.Eyes == 'squint'", "images/YanaBJFace/Yana_BJ_Eyes_Sexy.png",
            "True", "images/YanaBJFace/Yana_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/YanaBJFace/Yana_BJ_Eyes_Closed.png"
        .25
        repeat
#end image Yana BJ Blink:

image Yana_BJ_MouthHeadingB:
    #the mouth used for the heading animations
    contains:
        "images/YanaBJFace/Yana_BJ_Mouth_Heading.png"
        alpha .5
# end image Yana_BJ_MouthHeading:

image Yana_BJ_MouthSuckingMask:
    #the mask used for sucking animations, Yana_BJ_Anim3, Yana_BJ_Anim4, Yana_BJ_Anim6
    contains:
        "images/YanaBJFace/Yana_BJ_Mask_Sucking.png"
#    contains:
#        ConditionSwitch(
#            "'mouth' not in YanaX.Spunk or not Player.Male", Null(),
#            "Speed != 2 and Speed != 5", Null(),
#            "True", "images/YanaBJFace/Yana_BJ_Spunk_SuckingU.png",
#            )
    zoom 1.1
    anchor (0.5, 0.5)

image Yana_BJ_SpunkSucking:
    #the mouth used for the sucking animations
    contains:
        ConditionSwitch(
            "'mouth' in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Spunk_Sucking_O.png",
            "True", Null(),
            )
        zoom 1.1
        anchor (0.5, 0.5)
        offset (75,40)


#Head and Body Animations for Yana's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#Head and Body Animations for Yana's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_BJ_Anim0:
    #Animation for Yana BJ static (Speed 0)
    contains:
            # Yana's body, everything below the chin (Speed 0)
            "Yana_BJ_Backdrop"
            subpixel True
            offset (0,0)
    contains:
            # Yana's head Underlay (Speed 0)
            "Yana_BJ_Head"
            subpixel True
            offset (0,0)
    contains:
            # Cock (Speed 0)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate -10
#end Yana_BJ_Anim0 Static (Speed 0)


image Yana_BJ_Anim1:
    #Animation for Yana BJ Licking (Speed 1)
    contains:
            # Yana's body, everything below the chin (Speed 1)
            "Yana_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,-50)  #top
            rotate 0  #top
            parallel:
                ease 2.5 pos (0,140) #bottom (30,90)
                ease 2 pos (0,-50)  #top
                pause .5
                repeat
            parallel:
                ease 2.5 rotate -10 #bottom 25,50
                ease 2 rotate 0  #top
                pause .5
                repeat

    contains:
            # Yana's head Underlay (Speed 1)
            "Yana_BJ_Head"
            subpixel True
            offset (0,-35)  #top
            block:
                ease 2.5 offset (25,100) #bottom
                ease 2 offset (0,-35)  #top
                pause .5
                repeat
    contains:
            # Cock (Speed 1)
            "Blowcock"
            subpixel True
            anchor (.5,.5)
            offset (305,170)
            rotate 0
            block:
                ease 2 rotate -5 #410
                pause .5
                ease 2.5 rotate 0
                repeat
#end Yana_BJ_Anim1 Licking (Speed 1)


image Yana_BJ_Anim2:
    #Animation for Yana BJ Heading (Speed 2)
    contains:
            # Yana's body, everything below the chin (Speed 2)
            "Yana_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,0)  #top
            rotate -5  #top
            parallel:
                ease 1 pos (0,100) #bottom (30,90)
                ease 1.5 pos (0,0)  #top
                repeat
            parallel:
                ease 1 rotate -10 #bottom 25,50
                ease 1.5 rotate -5  #top
                repeat
    contains:
            # Yana's head Underlay (Speed 2)
            "Yana_BJ_Head"
            subpixel True
            offset (0,35)     #top
            block:
                ease 1 yoffset 90#35           #bottom
                ease 1.5 offset (0,35)     #top
                repeat
    contains:
            # Cock (Speed 2)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # Her face overlay for the heading animation  (Speed 2)
            contains:
                AlphaMask("Yana_BJ_HeadingHead", "Yana_BJ_MaskHeadingMask")
                anchor (0.5, 0.5)
            subpixel True
            offset (0,35)     #top
            block:
                ease 1 yoffset 90#35           #bottom
                ease 1.5 offset (0,35)     #top
                repeat
    contains:
            # Her spunk for the heading animation (Speed 2)
            "Yana_BJ_SpunkHeading"
            subpixel True
#            offset (0,-40)     #top
#            anchor (0.5, 0.5)
#            block:
#                ease 1 yoffset 35           #bottom
#                ease 1.5 offset (0,-40)     #top
#                repeat
            pos (0,77)
            offset (0,35)     #top
            block:
                ease 1 yoffset 90#35           #bottom
                ease 1.5 offset (0,35)     #top
                repeat
#end Yana_BJ_Anim2 Heading (Speed 2)


image Yana_BJ_MouthHeading:
    #the mouth used for the heading animations
    contains:
        "images/YanaBJFace/Yana_BJ_Mouth_Heading.png"
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .8 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
    contains:
        ConditionSwitch(
            "'mouth' in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Spunk_Heading_U.png",
            "True", Null(),
            )
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .8 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
# end image Yana_BJ_MouthHeading:

image Yana_BJ_MaskHeadingMask:
    #the mask used for the heading image
    contains:
        "images/YanaBJFace/Yana_BJ_Mask_Heading.png"
        subpixel True
        transform_anchor True
        anchor (430,530)#429,464)
        offset (430,540)#(415,490)
        zoom .8 #0.70
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
#end image Yana_BJ_MaskHeadingMask:

image Yana_BJ_HeadingHead:
    #An alt copy of her head that is alphaed by Yana_BJ_MaskHeadingMask
    #used in Yana_BJ_Anim2
    contains:
        "Yana_BJ_Head"
        anchor (460,530)#429,464)
        offset (417,484)#(460,530)#(257,279)

image Yana_BJ_SpunkHeading:
    #the mouth used for the heading animations
    contains:
        contains:
            ConditionSwitch(
                "'mouth' in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Spunk_Heading_O.png",
                "True", Null(),
                )
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .8 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
#end image Yana_BJ_SpunkHeading:
#end Yana_BJ_Anim2 Heading (Speed 2) Elements / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Yana_BJ_Anim3:
    #Animation for Yana BJ Sucking (Speed 3)
    contains:
            # Yana's body, everything below the chin (Speed 3)
            "Yana_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,200)  #top
            rotate -20  #top
            parallel:
                ease 1 pos (0,350) #bottom (30,90)
                ease 1.5 pos (0,200)  #top
                repeat
            parallel:
                ease 1 rotate -25 #bottom 25,50
                ease 1.5 rotate -20  #top
                repeat
    contains:
            # Yana's head Underlay (Speed 3)
            "Yana_BJ_Head"
            subpixel True
            offset (0,50)
            parallel:
                ease 1   yoffset 250 #100
                ease 1.5 yoffset 120
                repeat
            parallel:
                easeout .5  xoffset -2 #100
                easein .5  xoffset 0 #100
                easeout .5  xoffset -2 #100
                easein 1   xoffset -10
                repeat
    contains:
            # Cock (Speed 3)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 3)
            AlphaMask("Yana_BJ_Head", "Yana_BJ_MouthSuckingMask")
            subpixel True
            anchor (0.5, 0.5)
            offset (0,50)
            parallel:
                ease 1   yoffset 250 #100
                ease 1.5 yoffset 120
                repeat
            parallel:
                easeout .5  xoffset -2 #100
                easein .5  xoffset 0 #100
                easeout .5  xoffset -2 #100
                easein 1   xoffset -10
                repeat
    contains:
            # Her spunk for the heading animation (Speed 3)
            "Yana_BJ_SpunkSucking"
            subpixel True
            offset (0,50)
            parallel:
                ease 1   yoffset 250 #100
                ease 1.5 yoffset 120
                repeat
            parallel:
                easeout .5  xoffset -2 #100
                easein .5  xoffset 0 #100
                easeout .5  xoffset -2 #100
                easein 1   xoffset -10
                repeat
#end Yana_BJ_Anim3 Sucking (Speed 3)


image Yana_BJ_Anim4:
    #Animation for Yana BJ Deep (Speed 4)
    contains:
            # Yana's body, everything below the chin (Speed 4)
            "Yana_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,350)  #top
            rotate -25  #top
            parallel:
                ease 1 pos (0,500) #bottom (30,90)
                pause .5
                ease 2 pos (0,350)  #top
                repeat
            parallel:
                ease 1 rotate -30 #bottom 25,50
                pause .5
                ease 2 rotate -25  #top
                repeat
    contains:
            # Yana's head Underlay (Speed 4)
            "Yana_BJ_Head"
            offset (0,175)
            block:
                subpixel True
                ease 1 yoffset 375
                pause .5
                ease 2 yoffset 175
                repeat
    contains:
            # Cock (Speed 4)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)#(300,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 4)
            AlphaMask("Yana_BJ_Head", "Yana_BJ_MouthSuckingMask")
            anchor (0.5, 0.5)
            offset (0,175)
            block:
                subpixel True
                ease 1 yoffset 375
                pause .5
                ease 2 yoffset 175
                repeat
    contains:
            # Her spunk for the heading animation (Speed 4)
            "Yana_BJ_SpunkSucking"
            subpixel True
            offset (0,175)
            block:
                subpixel True
                ease 1 yoffset 375
                pause .5
                ease 2 yoffset 175
                repeat
#end Yana_BJ_Anim4 Deep (Speed 4)


image Yana_BJ_Anim5:
    #Animation for Yana BJ cum high (Speed 5)
    contains:
            # Yana's body, everything below the chin (Speed 5)
            "Yana_BJ_Backdrop"
            subpixel True
            offset (0,-30)     #top
            block:
                ease 1 yoffset -20           #bottom
                ease 1.5 offset (0,-30)     #top
                repeat
    contains:
            # Yana's head Underlay (Speed 5)
            "Yana_BJ_Head"
            subpixel True
            offset (0,50)     #top
            block:
                ease 1 yoffset 60           #bottom
                ease 1.5 offset (0,50)     #top
                repeat
    contains:
            # Cock (Speed 5)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # Her face overlay for the heading animation  (Speed 5)
            contains:
                AlphaMask("Yana_BJ_CumHighHead", "Yana_BJ_MaskCumHighMask")
                anchor (0.5, 0.5)
            subpixel True
            offset (0,50)     #top
            block:
                ease 1 yoffset 60           #bottom
                ease 1.5 offset (0,50)     #top
                repeat
    contains:
            # Her spunk for the heading animation (Speed 5)
            "Yana_BJ_SpunkCumHigh"
            subpixel True
            pos (0,77)
            offset (0,50)     #top
            block:
                ease 1 yoffset 60           #bottom
                ease 1.5 offset (0,50)     #top
                repeat
            #redo animation process for this one.
#end Yana_BJ_Anim5 Cum High (Speed 5)

image Yana_BJ_MouthHigh:
    #the mouth used for the cumming high animations
    contains:
        "images/YanaBJFace/Yana_BJ_Mouth_Heading.png"
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .9 #0.45
        block:
            ease 1      zoom 1          #bottom
            ease 1.5    zoom .9     #top
            repeat
#    contains:
#        ConditionSwitch(
#            "'mouth' in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Spunk_SuckingU.png",
#            "True", Null(),
#            )
#        zoom 1.1
#        anchor (0.50,0.6)#(0.50,0.65)  #(0.40,0.65)
# end image Yana_BJ_MouthHigh:

image Yana_BJ_MaskCumHighMask:
    #the mask used for the cumming high image
    contains:
        "images/YanaBJFace/Yana_BJ_Mask_Heading.png"
        subpixel True
        transform_anchor True
        anchor (430,530)#429,464)
        offset (430,540)#(415,490)
        zoom .9 #0.70
        block:
            ease 1      zoom 1          #bottom
            ease 1.5    zoom .9     #top
            repeat
#end image Yana_BJ_MaskCumHighMask:

image Yana_BJ_CumHighHead:
    #An alt copy of her head that is alphaed by Yana_BJ_MaskCumHighMask
    #used in Yana_BJ_Anim5
    contains:
        "Yana_BJ_Head"
        anchor (460,530)#429,464)
        offset (417,484)#(460,530)#(257,279)

image Yana_BJ_SpunkCumHigh:
    #the spunk used for the cumming high animations
    contains:
        contains:
            ConditionSwitch(
                "'mouth' in YanaX.Spunk", "images/YanaBJFace/Yana_BJ_Spunk_Heading_O.png",
                "True", Null(),
                )
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom 1 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1.05          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom 1     #top
            repeat
#end image Yana_BJ_SpunkCumHigh:
#end Yana_BJ_Anim5 Cum High (Speed 5) Elements / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_BJ_Anim6:
    #Animation for Yana BJ cum deep (Speed 6)
    contains:
            # Yana's body, everything below the chin (Speed 6)
            "Yana_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,450)  #top
            rotate -28  #top
            parallel:
                ease 1 pos (0,500) #bottom (30,90)
                pause .5
                ease 2 pos (0,450)  #top
                repeat
            parallel:
                ease 1 rotate -30 #bottom 25,50
                pause .5
                ease 2 rotate -28  #top
                repeat
    contains:
            # Yana's head Underlay (Speed 6)
            "Yana_BJ_Head"
            offset (0,330)
            block:
                subpixel True
                ease 1 yoffset 375#250
                pause .5
                ease 2 yoffset 330#230
                repeat
    contains:
            # Cock (Speed 6)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 6)
            AlphaMask("Yana_BJ_Head", "Yana_BJ_MouthSuckingMask")
            anchor (0.5, 0.5)
            offset (0,330)
            block:
                subpixel True
                ease 1 yoffset 375#250
                pause .5
                ease 2 yoffset 330#230
                repeat
    contains:
            # Her spunk for the heading animation (Speed 6)
            "Yana_BJ_SpunkSucking"
            subpixel True
            offset (0,330)
            block:
                subpixel True
                ease 1 yoffset 375#250
                pause .5
                ease 2 yoffset 330#230
                repeat
#end Yana_BJ_Anim6 cum deep (Speed 6)

#end Yana_BJ_Anims / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Yana_BJ_Launch(Line = Trigger):    # The sequence to launch the Yana BJ animations
    $ renpy.start_predict("images/YanaBJFace/*.*")
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Yana_BJ_Animation") and YanaX.Pose != "69":
        return
    elif renpy.showing("Yana_69_Animation") and YanaX.Pose == "69":
        return

    if not Player.Male:
        call Yana_CUN_Launch
        return

    call Girl_Hide(YanaX) #call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Yana_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Yana_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (150,80)
        with dissolve

    if Line == "L":
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != YanaX:
                            "[YanaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != YanaX:
                            "[YanaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[YanaX.Name] небрежно оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            if not YanaX.Blow:
                "[YanaX.Name] нерешительно опускается на колени и прикасается ртом к вашему члену."
            else:
                "[YanaX.Name] опускается на колени и берет ваш член в свой рот."

    $ Speed = 0

    if Line == "none":
        $ Player.Sprite = 0
    elif Line != "cum":
        $ Trigger = "blow"

    show Yana_Sprite:
        alpha 0
    if YanaX.Pose == "69":
            show Yana_69_Animation zorder 150
    else:
            show Yana_BJ_Animation zorder 150

    return

label Yana_BJ_Reset: # The sequence to the Yana animations from BJ to default
    if not renpy.showing("Yana_BJ_Animation") and not renpy.showing("Yana_69_Animation"):
        return
    call Girl_Hide(YanaX) #call Rogue_Hide
    $ Speed = 0

    show Yana_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Yana_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Yana Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Yana's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Yana's upper body
                    "not Player.Sprite","Yana_TJ_0",#Static
                    "Speed == 1", "Yana_TJ_1",#slow
                    "Speed == 3", "Yana_TJ_3",#licking
                    "Speed == 4", "Yana_TJ_4",#cumming high
                    "Speed == 5", "Yana_TJ_5",#cumming low
                    "Speed >= 2", "Yana_TJ_2",#fast
                    "True",       "Yana_TJ_0",#Static
                    )
            zoom .6 #.7
            transform_anchor True
            anchor (.5,.5)
            offset (400,250)#(950,1050)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Yana_TJ_Head:
#            #Hair underlay
#            "Yana_BJ_Head"
#            transform_anchor True
#            zoom .7
#            anchor (0.5, 0.5)
#            offset (30,-450)
#            rotate 0


image Yana_TJ_ZeroCock:
            #cock used in Yana's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .8#.6
            anchor (0.5, 0.6)
            offset (-5,50)#(45,50)
            rotate 0


image Yana_TJ_Body:
    LiveComposite(
        (1000,1000),       #550,950
#        (-10,-90), "Yana_BJ_HairBack", #(75,-10)

#        (0,0), "images/YanaBJFace/Yana_TJ_Body.png",

        (0,0), "images/YanaBJFace/Yana_TJ_Body.png",
        (0,0), ConditionSwitch(
            # water drops
            "YanaX.Water", "images/YanaBJFace/Yana_TJ_Wet_Body.png",
            "True", Null(),
            ),
#        (0,0), "images/YanaBJFace/Yana_TJ_RefCock.png",

#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "not Player.Sprite", Null(),
#            "True", "images/YanaBJFace/Yana_TJ_Tits_Under.png",
#            ),
        (0,0), ConditionSwitch(
            #Chest layer under tits
#            "YanaX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Chest_Lace_Body_Up.png",
#                    "YanaX.Chest == 'bra'", "images/YanaBJFace/Yana_TJ_Chest_Lace_Body_Up.png",
#                    "YanaX.Chest == 'tank'", "images/YanaBJFace/Yana_TJ_Chest_Tank_Body_Up.png",
#                    "YanaX.Chest == 'swimsuit'", "images/YanaBJFace/Yana_TJ_Chest_Bikini_Body_Up.png",
#                    "True", Null(),
#                    ),
#            "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Chest_Bra.png",
            "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Chest_Mesh.png",
            "YanaX.Chest == 'bikini top'", "images/YanaBJFace/Yana_TJ_Chest_Bikini.png",
            "YanaX.Chest", "images/YanaBJFace/Yana_TJ_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
#            "YanaX.Over == 'corset'", "images/YanaBJFace/Yana_TJ_Over_Corset.png",
            "YanaX.Over == 'shirt'", "images/YanaBJFace/Yana_TJ_Over_Shirt.png",
            "YanaX.Over == 'purple top'", "images/YanaBJFace/Yana_TJ_Over_Purple.png",
            "YanaX.Legs == 'dress'", "images/YanaBJFace/Yana_TJ_Tits_Dress_Under.png",
#            "YanaX.Over == 'towel'", "images/YanaBJFace/Yana_TJ_Over_Towel_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket body layer
            "YanaX.Acc == 'jacket'", "images/YanaBJFace/Yana_TJ_Jacket.png",
            "True", Null(),
            ),
#        (0,0), "images/YanaBJFace/Yana_TJ_RefLine.png",

#        (0,0), ConditionSwitch(
#            #Hair overlay
#            "YanaX.Hair != 'long' and YanaX.Hair != 'wetlong'", Null(),
#            "YanaX.Water or YanaX.Hair == 'wetlong'", "images/YanaBJFace/Yana_TJ_Hair_Wet.png",
#            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaBJFace/Yana_TJ_Hair_Wet.png",
#            "True", "images/YanaBJFace/Yana_TJ_Hair_Long.png",
#            ),

        (30,-300), ConditionSwitch(
            #Hair overlay
            "YanaX.Hair == 'wetlong' or (YanaX.Hair == 'long' and YanaX.Water)", "images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",
            "YanaX.Hair == 'long' and (not Player.Male and 'facial' in YanaX.Spunk)","images/YanaBJFace/Yana_BJ_Hair_Long_Wet_Under.png",

            "YanaX.Hair == 'long'","images/YanaBJFace/Yana_BJ_Hair_Long_Under.png",
            "True", Null(),
            ),
#        (-10,-90), "Yana_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.6, 1.0)#(0.6, 0.0)
    xoffset 118#150
    yoffset 240#271#125
#    zoom .75  #.76
    rotate 0

#    transform_anchor True
#    zoom 1
#    anchor (0.4, 1.0)
#    #offset (410,770) # (300,275)
#    rotate 0


image Yana_TJ_Tits_Under:
    LiveComposite(
        (1000,1000),       #550,950
        (0,0), ConditionSwitch(
            # under tit
#            "Player.Sprite and renpy.showing('Yana_TJ_Animation')", "images/YanaBJFace/Yana_TJ_Tits_Under.png",
            "True", "images/YanaBJFace/Yana_TJ_Tits_Under.png",
            ),
#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "not YanaX.Uptop", Null(),
#            "YanaX.Over == 'tshirt'", "images/YanaBJFace/Yana_TJ_Over_Tshirt_Mask.png",
#            "YanaX.Chest == 'sports bra'", "images/YanaBJFace/Yana_TJ_Chest_Sports_Mask.png",
##            "YanaX.Chest == 'swimsuit'", "images/YanaBJFace/Yana_TJ_Chest_Bikini_Tits.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in YanaX.Spunk", Null(),
            "True", "images/YanaBJFace/Yana_TJ_Spunk_Tits_Under.png",
            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


image Yana_TJ_Tits_Over:
    LiveComposite(
        (1000,1000),    #800,950
        (0,0), ConditionSwitch(
            # over tit
            "Player.Sprite and renpy.showing('Yana_TJ_Animation')", "images/YanaBJFace/Yana_TJ_Tits_Over.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            # water drops
            "YanaX.Water", "images/YanaBJFace/Yana_TJ_Wet_Tits.png",
            "True", Null(),
            ),
#        (0,0),  "images/YanaBJFace/Yana_TJ_TitsRef.png",
        (0,0), ConditionSwitch(
            #Chest tits layer
            "YanaX.Over == 'tshirt'", Null(),
            "YanaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Tits_Chest_Bra_Up.png",
                    "YanaX.Chest == 'bikini top'", "images/YanaBJFace/Yana_TJ_Tits_Chest_Bikini_Up.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Tits_Chest_Mesh_Up.png",
                    "YanaX.Chest", "images/YanaBJFace/Yana_TJ_Tits_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Tits_Chest_Lace.png",
            "YanaX.Chest == 'bikini top'", "images/YanaBJFace/Yana_TJ_Tits_Chest_Bikini.png",
            "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Tits_Chest_Mesh.png",
            "YanaX.Chest", "images/YanaBJFace/Yana_TJ_Tits_Chest_Bra.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress layer
            "YanaX.Uptop or YanaX.Over == 'shirt'", Null(),
            "YanaX.Legs == 'dress'", "images/YanaBJFace/Yana_TJ_Tits_Dress.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over tits layer
            "YanaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "YanaX.Over == 'shirt'", "images/YanaBJFace/Yana_TJ_Tits_Over_Shirt_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Over == 'purple top'", "images/YanaBJFace/Yana_TJ_Tits_Over_Purple.png",
            "YanaX.Over == 'shirt'", "images/YanaBJFace/Yana_TJ_Tits_Over_Shirt.png",
            "YanaX.Over == 'corset'", "images/YanaBJFace/Yana_TJ_Tits_Over_Corset.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # spunk over tits
            "'tits' not in YanaX.Spunk", Null(),
#            "YanaX.Over == 'tshirt'", "images/YanaBJFace/Yana_TJ_Spunk_Clothed.png",
#            "not YanaX.Uptop and YanaX.Over", "images/YanaBJFace/Yana_TJ_Spunk_Clothed.png",
            "YanaX.Chest == 'mesh top'", Null(),
            "True", "images/YanaBJFace/Yana_TJ_Spunk_Tits_Over.png",
            ),
#        (0,0), "images/YanaBJFace/Yana_TJ_RefLine.png",
#        (0,0), "images/YanaBJFace/Yana_TJ_RefLine2.png",
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 562)
#    xoffset 155#300
#    yoffset 325#125
#    yoffset -925#-625#-325
#    zoom .75  #.76
    rotate 0


image Yana_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                    #Over tits layer
#                    "YanaX.Over == 'tshirt'", "images/YanaBJFace/Yana_TJ_Stretch_Tshirt.png",
#                    "YanaX.Over == 'sweater'", "images/YanaBJFace/Yana_TJ_Stretch_Sweater.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Brastretch_Mesh.png",
                    "True", Null(),
                    )
#            contains:
#                    "images/YanaBJFace/Yana_TJ_RefLine2.png"
            transform_anchor True
#            zoom 1
#            offset (50,0) # (300,275)
#            anchor (.1,.1)#(0.1, .2)
            rotate 0

image Yana_TJ_Hands:
    LiveComposite(
        (1000,1000),       #550,950
        (0,0), ConditionSwitch(
            # hands
            "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Hands_Mesh.png",
            "True", "images/YanaBJFace/Yana_TJ_Hands.png",
            ),
        (0,0), ConditionSwitch(
            # sleeves
            "YanaX.Over == 'purple top'", "images/YanaBJFace/Yana_TJ_Sleeves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # wrists
            "YanaX.Arms", "images/YanaBJFace/Yana_TJ_Hands_Armlet.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            # nips
#            "True", "images/YanaBJFace/Yana_TJ_Nips.png",
#            ),
#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "not YanaX.Uptop", Null(),
#            "YanaX.Over == 'tshirt'", "images/YanaBJFace/Yana_TJ_Over_Tshirt_Mask.png",
#            "YanaX.Chest == 'sports bra'", "images/YanaBJFace/Yana_TJ_Chest_Sports_Mask.png",
##            "YanaX.Chest == 'swimsuit'", "images/YanaBJFace/Yana_TJ_Chest_Bikini_Tits.png",
#            "True", Null(),
#            ),


        (0,0), ConditionSwitch(
            #Piercings layer
#            "not YanaX.Pierce", Null(),
            "YanaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "YanaX.Uptop", "images/YanaBJFace/Yana_TJ_Pierce_R.png",

                    "YanaX.Over == 'purple top'", "images/YanaBJFace/Yana_TJ_Pierce_R_Purp.png",
                    "YanaX.Over == 'shirt' or YanaX.Over == 'corset'", "images/YanaBJFace/Yana_TJ_Pierce_R_Red.png",
                    "YanaX.Legs == 'dress'", "images/YanaBJFace/Yana_TJ_Pierce_R_Black.png",

                    "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Pierce_R_Lace.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Pierce_R_Mesh.png",
                    "YanaX.Chest", "images/YanaBJFace/Yana_TJ_Pierce_R_Red.png",
                    "True", "images/YanaBJFace/Yana_TJ_Pierce_R.png",
                    ),

            "YanaX.Pierce", ConditionSwitch(
                    #if it's the ring pericings
                    "YanaX.Uptop", "images/YanaBJFace/Yana_TJ_Pierce_B.png",

                    "YanaX.Over == 'purple top'", "images/YanaBJFace/Yana_TJ_Pierce_B_Purp.png",
                    "YanaX.Over == 'shirt' or YanaX.Over == 'corset'", "images/YanaBJFace/Yana_TJ_Pierce_B_Red.png",
                    "YanaX.Legs == 'dress'", "images/YanaBJFace/Yana_TJ_Pierce_B_Black.png",

                    "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Pierce_B_Lace.png",
                    "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Pierce_B_Mesh.png",
                    "YanaX.Chest", "images/YanaBJFace/Yana_TJ_Pierce_B_Red.png",
                    "True", "images/YanaBJFace/Yana_TJ_Pierce_B.png",
                    ),

            "YanaX.Lust < 50", Null(),
            "YanaX.Uptop", "images/YanaBJFace/Yana_TJ_Nips.png",
            "YanaX.Over == 'purple top'", "images/YanaBJFace/Yana_TJ_Nips_Purp.png",
            "YanaX.Over == 'shirt' or YanaX.Over == 'corset'", "images/YanaBJFace/Yana_TJ_Nips_Red.png",
            "YanaX.Legs == 'dress'", "images/YanaBJFace/Yana_TJ_Nips_Black.png",

            "YanaX.Chest == 'lace bra'", "images/YanaBJFace/Yana_TJ_Nips_Lace.png",
            "YanaX.Chest == 'mesh top'", "images/YanaBJFace/Yana_TJ_Nips_Mesh.png",
            "YanaX.Chest", "images/YanaBJFace/Yana_TJ_Nips_Red.png",
            "True", "images/YanaBJFace/Yana_TJ_Nips.png",
            ),

#        (0,0), ConditionSwitch(
#            # spunk under tits
#            "'tits' not in YanaX.Spunk", Null(),
#            "True", "images/YanaBJFace/Yana_TJ_Spunk_Tits.png",
#            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


## Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Yana_TJ_0:
        #Her Body in the TJ pose, static
#        contains:
#                #hair back
#                "Yana_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-70,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 30
#                    pause .3
#                    ease 2 ypos 0
#                    pause .4
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 10
#                    pause .3
#                    ease 2 rotate 0
#                    pause .3
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Yana_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
        contains:
                #underside tit
                "Yana_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#150
                yoffset -271#125
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #head
                "Yana_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-90,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease 2 rotate 0
                    pause .3
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Yana_TJ_ZeroCock"
#                ConditionSwitch(
#                            "Player.Sprite","Yana_TJ_ZeroCock",
#                            "True",  Null(),
#                            )
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Yana_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .3
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
#                    pause .2
                    ease 2 yzoom .53
                    pause .3
                    ease 2 yzoom .3
                    pause .4
                    repeat
        contains:
                #overside tit
                "Yana_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#160
                yoffset -271#271
                yzoom 1
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #hands over everything
                "Yana_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat


# End Yana TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Yana_TJ_1:
        #Her Body in the TJ pose, slow
#        contains:
#                #hair back
#                "Yana_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-70,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 120
#                    pause .3
#                    ease 2 ypos 0
#                    pause .4
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 10
#                    pause .3
#                    ease 2 rotate 0
#                    pause .3
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Yana_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
        contains:
                #underside tit
                "Yana_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .90
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #head
                "Yana_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(50,-600)
                pos (-90,0) #top (0,-10)
                transform_anchor True
                rotate 10
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate -5#0
                    pause .3
                    ease .5 rotate 20#14
                    ease 1.8 rotate 10
#                    pause 1.3
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Yana_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Yana_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .3
#                alpha 0.7
                parallel:
                    ease 2 ypos 150
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
#                    pause .2
                    ease 2 yzoom 1.36#1.2
                    pause .3
                    ease 2 yzoom .3
                    pause .4
                    repeat
        contains:
                #overside tit
                "Yana_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#-271
                yzoom 1
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .90
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #hands over everything
                "Yana_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    pause .1
                    ease 1.9 ypos 110
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
## End Yana TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Yana_TJ_2:
        #Her Body in the TJ pose, fast
#        contains:
#                #hair back
#                "Yana_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-70,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel: #4.7s total -> 1.7
#                    ease .6 ypos 60 #120
#                    pause .1
#                    ease .8 ypos 0
#                    pause .2
#                    repeat
#                parallel:
#                    ease .5 rotate -5
#                    pause .2
#                    ease .8 rotate 0
#                    pause .2
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Yana_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
        contains:
                #underside tit
                "Yana_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                yzoom 1
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .4 yzoom .90
                    pause .3
                    ease .3 yzoom 1.05
                    ease .2 yzoom .98
                    ease .2 yzoom 1
                    pause .3
                    repeat
        contains:
                #head
                "Yana_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-90,0) #top (0,0)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .5 rotate -5
                    pause .2
                    ease .8 rotate 0
                    pause .2
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Yana_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Yana_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .3
                parallel: #4.7s total -> 1.9
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel: #4.7s total -> 1.9
                    ease .6 yzoom .72 #.35
                    pause .1
                    ease .8 yzoom .3
                    pause .2
                    repeat
        contains:
                #overside tit
                "Yana_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                yzoom 1
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .4 yzoom .90
                    pause .3
                    ease .3 yzoom 1.05
                    ease .2 yzoom .98
                    ease .2 yzoom 1
                    pause .3
                    repeat
        contains:
                #hands over everything
                "Yana_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel: #4.7s total -> 1.9
#                    ease .75 ypos 60 #60
##                    pause .05
#                    ease .75 ypos 0
#                    pause .2
#                    repeat

                    ease .5 ypos 45
#                    ease .2 ypos 45
                    pause .4
#                    ease .2 ypos 40
                    ease .5 ypos 0
                    pause .3
                    repeat

## End Yana TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Yana_TJ_3:
        #Her Body in the TJ pose, licking
#        contains:
#                #hair back
#                "Yana_BJ_HairBack"
#                subpixel True
#                pos (-70,110) #top (0,0)
#                transform_anchor True
#                rotate 0
#                parallel: #4.7s total -> 3.8
#                    ease 1.9 ypos 130
#                    pause .3
#                    ease .6 ypos 100
#                    pause 1
#                    repeat
#                parallel:
#                    ease 1.9 rotate -15
#                    pause .3
#                    ease .6 rotate 0
#                    pause 1
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Yana_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,100) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat
        contains:
                #underside tit
                "Yana_TJ_Tits_Under"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #head
                "Yana_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-90,110) #top (0,0)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 3.8
                    ease 1.9 ypos 130
                    pause .3
                    ease .6 ypos 100
                    pause 1
                    repeat
                parallel:
                    ease 1.9 xpos -90
                    pause .3
                    ease .6 xpos -120
                    pause 1
                    repeat
                parallel:
                    ease 1.9 rotate -15
                    pause .3
                    ease .6 rotate 0
                    pause 1
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Yana_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
                parallel:
                    pause .1
                    ease 2 rotate -3
                    pause .3
                    ease .5 rotate 0
                    pause .9
                    repeat
        contains:
                #bra stretch
                "Yana_TJ_BraStretch"
                subpixel True
                pos (0,120) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom 1.15
#                alpha 0.7
                parallel:
                    ease 2 pos (-25,150)#(-25,120)
                    pause .3
                    ease .5 pos (0,120)#(0,90)
                    pause 1
                    repeat
                parallel:
                    ease 2 yzoom 1.38#1.25
                    pause .3
                    ease .5 yzoom 1.15#1.05
                    pause 1
                    repeat
        contains:
                #overside tit
                "Yana_TJ_Tits_Over"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #hands over everything
                "Yana_TJ_Hands"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat


## End Yana TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
#image Yana_TJ_4:
#        #Her Body in the TJ pose, cummming high
#        contains:
#                #jacket
#                "Yana_TJ_Jacketback"
#                subpixel True
#                pos (0,0) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#        contains:
#                #bra strap backing
#                "Yana_TJ_Braback"
#                subpixel True
#                pos (0,5) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    pause .2
#                    ease 1.9 ypos -30
#                    pause .2
#                    ease 1.9 ypos 5
#                    repeat
#        contains:
#                #base body test / / / / / / / / / / / / / / / / / / / /
#                "Yana_TJ_Body"
#                subpixel True
#                pos (0,0) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#        contains:
#                #head
#                "Yana_TJ_Head"
#                subpixel True
#                pos (20,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 20#-5
#                    pause .1
#                    ease 2 rotate 15#0
#                    repeat
#        contains:
#                #zero cock / / / / / / / / / / / / / / / / / / / /
#                subpixel True
#                "Yana_TJ_ZeroCock"
#                pos (0,20) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 0
#                    pause .1
#                    ease 2 ypos 20
#                    pause .1
#                    repeat
#        contains:
#                contains:
#                    "Yana_TJ_Tits"
#                subpixel True
#                pos (0,5) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    pause .2
#                    ease 1.9 ypos -30
#                    pause .2
#                    ease 1.9 ypos 5
#                    repeat

## End Yana TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Yana_TJ_5:
        #Her Body in the TJ pose, cumming low
#        contains:
#                #hair back
#                "Yana_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-60,115) #top (0,-10)
#                transform_anchor True
#                rotate 5
#                parallel:
#                    ease 2 ypos 120
#                    pause .3
#                    ease 1.5 ypos 115
#                    pause .5
#                    repeat
#                parallel:
#                    pause .1
#                    ease 1 rotate -5
#                    pause .3
#                    ease .5 rotate 5
#                    pause .9
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Yana_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,100) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat
        contains:
                #underside tit
                "Yana_TJ_Tits_Under"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat
        contains:
                #head
                "Yana_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-95,115) #top (0,-10)
                transform_anchor True
                rotate 5
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 1.5 ypos 115
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos -40
                    pause .3
                    ease .5 xpos -95
                    pause .9
                    repeat
                parallel:
                    pause .1
                    ease 1 rotate -5
                    pause .3
                    ease .5 rotate 5
                    pause .9
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Yana_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
                parallel:
                    pause .1
                    ease 1.1 rotate 3
                    pause .3#1.5
                    ease .5 rotate -5
                    ease .8 rotate 0
                    repeat
        contains:
                #bra stretch
                "Yana_TJ_BraStretch"
                subpixel True
                pos (-5,120) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .8
#                alpha 0.7
                parallel:
                    pause 1.5
                    ease .5 xpos -45
                    ease .8 xpos -5
                    repeat
                parallel:
                    ease 2 yzoom 1.30#1.21
                    pause .3
                    ease 1.5 yzoom 1.25#1.18
                    pause .5
                    repeat
                parallel:
                    ease 2 ypos 140
                    pause .3
                    ease 1.5 ypos 130
                    pause .5
                    repeat
        contains:
                #overside tit
                "Yana_TJ_Tits_Over"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat
        contains:
                #hands over everything
                "Yana_TJ_Hands"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat

# End Yana TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Yana's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Yana_TJ_Launch(Line = Trigger):    # The sequence to launch the Yana Titfuck animations
    $ renpy.start_predict("images/YanaBJFace/*.*")
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    return
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Yana_TJ_Animation"):
        return

    if Line == "L": # Yana gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != YanaX:
                            "[YanaX.Name]  оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != YanaX:
                            "[YanaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[YanaX.Name] небрежно оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
#            "[YanaX.Name] bends over and places your cock between her breasts."
    if YanaX.Chest == "suit" and not YanaX.Uptop:
        $ YanaX.Uptop = 1
        "Она слегка расстегивает свой костюм."
#    if YanaX.Chest and YanaX.Over:
#        "She throws off her [YanaX.Over] and her [YanaX.Chest]."
#    elif YanaX.Over:
#        "She throws off her [YanaX.Over], baring her breasts underneath."
#    elif YanaX.Chest:
#        "She tugs off her [YanaX.Chest] and throws it aside."
#    $ YanaX.Over = 0
#    $ YanaX.Chest = 0
#    $ YanaX.ArmPose = 0
    call Girl_First_Topless(YanaX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Yana_BJ_Animation"):
            hide Yana_BJ_Animation
    else:
            call Girl_Hide(YanaX) #call Rogue_Hide
            show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Yana_Sprite:
                alpha 0

#    if YanaX.Over == "towel" or YanaX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ YanaX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Yana_TJ_Animation zorder 150#:
        #pos (950,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Yana_TJ_Reset:
    # The sequence to the Yana animations from Titfuck to default
    if not renpy.showing("Yana_TJ_Animation"):
        return
#    hide Yana_TJ_Animation
    call Girl_Hide(YanaX) #call Rogue_Hide
    $ Player.Sprite = 0

    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Yana_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos YanaX.SpriteLoc yoffset 50
    "[YanaX.Name] отстраняется"
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 offset (0,50) xpos YanaX.SpriteLoc
    return

## End Yana TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Yana Handjob element //////////////////////////////////////////////////////////////////////

image Yana_HJ_Body:
    "Yana_Sprite"
    pos (-30,-1250)#(0,-1250)
    zoom 4.8#2.15


transform Yana_HJ_Body_1():
    subpixel True
    pos (-30,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Yana_HJ_Body_2():
    subpixel True
    pos (-30,-1250)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Yana_Hand_Arm:
    contains:
        "images/YanaBJFace/handyana3.png"
    anchor (0.5,0.5)
    pos (200,0) #(170,0)
#    xzoom -1

image Yana_Hand_Under:
    contains:
        "images/YanaBJFace/handyana2.png"
    anchor (0.5,0.5)
    pos (200,0) #(170,0)
#    xzoom -1


image Yana_Hand_Over:
    contains:
        "images/YanaBJFace/handyana1.png"
    anchor (0.5,0.5)
    pos (200,0) #(100,0)
#    xzoom -1

transform Yana_Hand_1():
    subpixel True
    pos (200,-100)
    rotate 5
    block:
        ease .5 pos (200,150) rotate -5 #ypos 150 rotate 5 Bottom 90
        pause 0.25
        ease 1.0 pos (200,-100) rotate 5 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Yana_Hand_2():
    subpixel True
    pos (200,-120)
    rotate 10
    block:
        ease 0.2 pos (200,0) rotate 0   #(-15,0) 85
        pause 0.1
        ease 0.4 pos (200,-120) rotate 5 #-15,-120)
        pause 0.1
        repeat

transform Yana_Arm_1():
    subpixel True
    pos (200,-100)
    rotate 5
    block:
        ease .5 pos (200,150) rotate -5 #ypos 150 rotate 5 Bottom 90
        pause 0.25
        ease 1.0 pos (200,-100) rotate 5 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Yana_Arm_2():
    subpixel True
    pos (200,-120)
    rotate 10
    block:
        ease 0.2 pos (200,0) rotate 0   #(-15,0) 85
        pause 0.1
        ease 0.4 pos (200,-120) rotate 5 #-15,-120)
        pause 0.1
        repeat

image Yana_HJ_Animation:
    contains:
        ConditionSwitch(
            # body
            "not Speed", Transform("Yana_HJ_Body"),
            "Speed == 1", At("Yana_HJ_Body", Yana_HJ_Body_1()),
            "Speed >= 2", At("Yana_HJ_Body", Yana_HJ_Body_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # arm
            "not Speed", Transform("Yana_Hand_Arm"),
            "Speed == 1", At("Yana_Hand_Arm", Yana_Hand_1()),
            "Speed >= 2", At("Yana_Hand_Arm", Yana_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Yana_Hand_Under"),
            "Speed == 1", At("Yana_Hand_Under", Yana_Hand_1()),
            "Speed >= 2", At("Yana_Hand_Under", Yana_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # cock
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1L()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2L()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            # fingers of the hand
            "not Speed", Transform("Yana_Hand_Over"),
            "Speed == 1", At("Yana_Hand_Over", Yana_Hand_1()),
            "Speed >= 2", At("Yana_Hand_Over", Yana_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
#    xzoom -0.4#0.6
    zoom 0.4#0.6


label Yana_HJ_Launch(Line = Trigger):
    $ renpy.start_predict("images/YanaBJFace/*.*")
    if renpy.showing("Yana_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Yana_Finger_Launch
        return
    call Girl_Hide(YanaX) #call Rogue_Hide
    $ YanaX.ArmPose = 1
    if Line == "L":
        show Yana_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-230,200)#(0,200)
    else:
        show Yana_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (-230,150)#(-150,150)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Yana_Sprite:
        alpha 0
    show Yana_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (200,250)#(150,250)
    $ YanaX.ArmPose = 2
    return

label Yana_HJ_Reset: # The sequence to the Yana animations from handjob to default
    if not renpy.showing("Yana_HJ_Animation"):
        return
    $ Speed = 0
    $ YanaX.ArmPose = 1
    hide Yana_HJ_Animation with dissolve
    call Girl_Hide(YanaX) #call Rogue_Hide
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-250,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 offset (0,0)
#    $ YanaX.ArmPose = 1
    return

## End Yana Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Yana CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Yana CUN element
#Yana CUN Over Sprite Compositing

image Yana_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Yana_CUN_Anim_Static",
            "Speed == 1",  "Yana_CUN_Anim_Licking1",
            "Speed == 2",  "Yana_CUN_Anim_Licking2",
            "Speed >= 3",  "Yana_CUN_Anim_Licking3",
            "Speed == 4",  "Yana_CUN_Anim_Licking1",
            "True", "Yana_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Yana_CUN_Anim_Static:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Yana_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (70,0)#(-10,0)
#        rotate 20
#        block:
#            ease 2 yoffset 10
#            ease 2 yoffset 0
#            repeat
    contains:
        #body 2
        "Yana_BJ_Backdrop"
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (0,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Yana_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-100,0)#(-150,220)
        offset (70,0)#(-10,0)
        rotate 0
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,0)
        pause 0.1
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat


image Yana_CUN_Anim_Licking1:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Yana_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (40,40)#490)
#        rotate 10
#        block: #5s total
#            ease 2.5 offset (45,100) #bottom (0,75)
#            easeout 1.5 offset (45,60)  #top (0,60)
#            ease .5 offset (40,20)  #top
#            ease .5 offset (42,30)  #top
#            repeat
    contains:
        #body 2
        "Yana_BJ_Backdrop"#"Yana_Sprite"
#        zoom 1 #4.5
#        pos (-350,-290)#(-440,-290)
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Yana_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-70,0)#(-150,220)
        offset (40,40)#490)
        rotate 0
        block: #5s total
            ease 2.5 offset (45,100) #bottom (0,75)
            easeout 1.5 offset (45,60)  #top (0,60)
            ease .5 offset (40,20)  #top
            ease .5 offset (42,30)  #top
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,5)#490)
        block:
            easein 1 yoffset 10 #510 bottom
            pause 1.5
            easeout 1 yoffset 0#490
            linear .3 yoffset -5#490
            easein .2 yoffset -3#490
            easeout 1 yoffset 5 #510 bottom
            repeat
#End Yana Licking 1

image Yana_CUN_Anim_Licking2:
    #Animation for licking speed 2
#    contains:
#        #hair
#        "Yana_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (40,30)#490)
#        rotate 10
#        parallel: #2s total
#            ease 1 offset (30,100) #bottom
#            easeout .65 offset (40,70)  #top -35)
#            linear .35 offset (40,30)  #top -35)
#            pause .10
#            repeat
#        parallel: #2s total
#            ease 1 rotate 4 #bottom
#            easeout .65 rotate 7  #top -35)
#            linear .35 rotate 10  #top -35)
#            pause .10
#            repeat
    contains:
        #body 2
        "Yana_BJ_Backdrop"
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (10,50)#490)
        block:
            ease .75 offset (10,70) #bottom (30,90)
            ease .95 offset (10,50)  #top
            pause .40
            repeat
    contains:
        #head
        "Yana_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-40,0)#(-150,220)
        offset (40,30)#490)
        rotate 10
        parallel: #2s total
            ease 1 offset (30,100) #bottom
            easeout .65 offset (40,70)  #top -35)
            linear .35 offset (40,30)  #top -35)
            pause .10
            repeat
        parallel: #2s total
            ease 1 rotate 4 #bottom
            easeout .65 rotate 7  #top -35)
            linear .35 rotate 10  #top -35)
            pause .10
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,-3)#490)
        block:
            ease .5 yoffset 10 #510 bottom
            pause .5
            easeout .6 yoffset 0#490
            linear .1 yoffset -5#490
            easein .1 yoffset -3#490
            pause .3
            repeat
#End Yana Licking 2

image Yana_CUN_Anim_Licking3:
    #Animation for licking speed 3
#    contains:
#        #hair
#        "Yana_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (20,110)#490)
#        block: #2s total
#            ease .5 offset (20,130) #bottom
#            ease .5 offset (20,110)  #top -35)
#            repeat
    contains:
        #body 2
        "Yana_BJ_Backdrop"
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (0,110)#490)
        block:
            ease .4 offset (0,100) #bottom (30,90)
            ease .4 offset (0,110)  #top
            pause .2
            repeat
    contains:
        #head
        "Yana_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-40,0)#(-70,0)
        offset (20,110)#490)
        block: #2s total
            ease .5 offset (20,130) #bottom
            ease .5 offset (20,110)  #top -35)
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,5)#490)
        block:
            ease .25 yoffset 10 #510 bottom
            pause .25
            ease .25 yoffset 5#490
            ease .25 yoffset 6#490
            repeat
#End Yana Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Yana_CUN_Launch(Line = Trigger):
    $ renpy.start_predict("images/YanaBJFace/*.*")
    # The sequence to launch the Yana CUN animations
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Yana_CUN_Animation") and YanaX.Pose != "69":
        return
    elif renpy.showing("Yana_69_Animation") and YanaX.Pose == "69":
        return

    if Player.Male == 1:
        call Yana_BJ_Launch
        return


    call Girl_Hide(YanaX) #call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Yana_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Yana_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo > 20 and Line == "L":
            # Yana gets started. . .
            if len(Present) >= 2:
                if Present[0] != YanaX:
                        "[YanaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != YanaX:
                        "[YanaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[YanaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not YanaX.Blow:
                "[YanaX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[YanaX.Name] наклоняется и начинает лизать вашу киску."

    if Line == "none":
        $ Player.Sprite = 0
    elif Line != "cum":
        $ Trigger = "cun"

    $ Player.Cock = 0
    show Yana_Sprite:
        alpha 0
    if YanaX.Pose == "69":
            show Yana_69_CUN zorder 150
    else:
            show Yana_CUN_Animation zorder 150:
                pos (800,830)#(645,610)
    return

label Yana_CUN_Reset: # The sequence to the Yana animations from CUN to default
    if not renpy.showing("Yana_CUN_Animation") and not renpy.showing("Yana_69_CUN"):
        return
    call Girl_Hide(YanaX) #call Rogue_Hide
    $ Speed = 0

    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ YanaX.FaceChange("sexy")
    return

##End Yana Cunnilingus Animations
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////


## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////

image Yana_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Yana_Finger_1",
            "Speed >= 2", "Yana_Finger_2",
            "True", "Yana_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Yana_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Yana_Sprite"
            pos (50,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "YanaBJFace/Yana_Fingering_wet.png",
                "True", "YanaBJFace/Yana_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-5,50)#(20,50)
#            xzoom -1

#            "Yana_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "YanaBJFace/Yana_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (-5,50)#(20,50)
#            xzoom -1
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Yana_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Yana_Sprite"
            pos (50,-550)
            zoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "YanaBJFace/Yana_Fingering_wet.png",
                "True", "YanaBJFace/Yana_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
#            xzoom -1
            transform_anchor True
            pos (-5,50)#(15,50)
            rotate -5
            block:
                ease .5 pos (-10,115) rotate 0 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (-5,40) rotate -5 #(40,0) Top                 pause 0.1
                repeat
    contains:
            "Zero_Pussy"
            subpixel True
            rotate_pad False
            block:
                pause 0.1
                ease .5 yoffset 10 #rotate -2 #30
                pause 0.15
                ease 1.0 yoffset 0 #rotate 0 #20
                repeat
    contains:
            "YanaBJFace/Yana_Fingering_Over.png"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
#            xzoom -1
            transform_anchor True
            pos (-5,50)#(15,50)
            rotate -5
            block:
                ease .5 pos (-10,115) rotate 0 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (-5,40) rotate -5 #(40,0) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Yana_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Yana_Sprite"
            pos (50,-550)
            zoom 2.15
            block:
                ease 0.15 ypos -540 #rotate 3   100
                pause 0.1
                ease 0.45 ypos -550 #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "YanaBJFace/Yana_Fingering_wet.png",
                "True", "YanaBJFace/Yana_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
#            xzoom -1
            transform_anchor True
#            rotate -15
            pos (-10,30)#(10,30)
            block:
                ease 0.15 ypos 125 #rotate 3   65
                pause 0.1
                ease 0.45 ypos 60 #rotate -3  30
                pause 0.1
                repeat
    contains:
            "Zero_Pussy"
            subpixel True
            rotate_pad False
            block:
                pause 0.05
                ease 0.15 yoffset 15 #rotate 35
                pause 0.15
                ease 0.45 yoffset 0 #rotate 20
                repeat
    contains:
            "YanaBJFace/Yana_Fingering_Over.png"
            subpixel True
            anchor (0.5,0.6)
#            xzoom -1
            transform_anchor True
#            rotate -15
            pos (-10,30)#(10,30)
            block:
                ease 0.15 ypos 125 #rotate 3   65
                pause 0.1
                ease 0.45 ypos 60 #rotate -3  30
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Yana_Finger_Launch(Line = Trigger):
    $ renpy.start_predict("images/YanaBJFace/*.*")
    if renpy.showing("Yana_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Yana_HJ_Launch
        return

    call Girl_Hide(YanaX) #call Rogue_Hide
    $ YanaX.Arms = 0
    $ YanaX.ArmPose = 2
    if not renpy.showing("Yana_Sprite"):
        show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 560 yoffset 200 #offset (-50,200)
        with dissolve
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 560 yoffset 200 #offset (-50,200)  850
#   (400,945)
    if Taboo > 20 and Line == "L":
        # Yana gets started. . .
        if len(Present) >= 2:
            if Present[0] != YanaX:
                    "[YanaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != YanaX:
                    "[YanaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[YanaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not YanaX.Hand and YanaX.Arms:
            "Когда вы стягиваете свои штаны, [YanaX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not YanaX.Hand and YanaX.Arms:
            "Когда вы стягиваете свои штаны, [YanaX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[YanaX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[YanaX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Yana_Sprite zorder YanaX.Layer:
        alpha 0
    show Yana_Finger_Animation at SpriteLoc(YanaX.SpriteLoc) zorder 150 with fade
    return

label Yana_Finger_Reset: # The sequence to the Yana animations from handjob to default
    if not renpy.showing("Yana_Finger_Animation"):
        return
    $ Speed = 0
    hide Yana_Finger_Animation
    with dissolve
    call Girl_Hide(YanaX) #call Rogue_Hide
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
#        alpha 1
#        zoom 1.7  xpos 850 yoffset 200
    show Yana_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos YanaX.SpriteLoc yoffset 0
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 xpos YanaX.SpriteLoc yoffset 0
    return

## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////


# Start Yana 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Yana_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Yana_69_Anim1",
                "Speed == 2", "Yana_69_Anim2",
                "Speed == 3", "Yana_69_Anim3",
                "Speed == 4", "Yana_69_Anim4",
                "Speed == 5", "Yana_69_Anim5",
                "Speed == 6", "Yana_69_Anim6",
                "Speed", "Yana_69_Anim1",
                "True", "Yana_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-800)#(475,-700)
    zoom 1.8#1/3

#Start Animations for Yana's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Yana_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #shirt layer
            "YanaX.Over == 'shirt' and YanaX.Uptop", "images/YanaSex/Yana_69_Over_Shirt_Up.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not YanaX.Uptop", Null(),
            #if top's up
            "YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_69_Chest_Bikini.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_69_Chest_Mesh.png",
#            "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_69_Chest_Lace.png",
            "YanaX.Chest", "images/YanaSex/Yana_69_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
#            "YanaX.Arms", "images/YanaSex/Yana_69_BodyG.png",
            "True", "images/YanaSex/Yana_69_Body.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "YanaX.Water", "images/YanaSex/Yana_69_Water_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra layer
            "YanaX.Uptop", Null(),
            #if top's up
            "YanaX.Chest == 'bikini top'", "images/YanaSex/Yana_69_Chest_Bikini.png",
            "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_69_Chest_Mesh.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_69_Chest_Lace.png",
            "YanaX.Chest", "images/YanaSex/Yana_69_Chest_Bra.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress layer
            "YanaX.Uptop", ConditionSwitch(
                    # ring pierce
                    "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Over_Dress_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Over_Dress.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "YanaX.Uptop", ConditionSwitch(
                    # ring pierce
#                    "YanaX.Over == 'towel'", Null(),
#                    "YanaX.Over == 'shirt'", Null(),
                    "YanaX.Over == 'purple top'", "images/YanaSex/Yana_69_Over_Purple_Up.png",
                    "YanaX.Over == 'corset'", "images/YanaSex/Yana_69_Over_Corset_Up.png",
                    "True", Null(),
                    ),
            "YanaX.Over == 'towel'", "images/YanaSex/Yana_69_Over_Towel.png",
            "YanaX.Over == 'purple top'", "images/YanaSex/Yana_69_Over_Purple.png",
            "YanaX.Over == 'shirt'", "images/YanaSex/Yana_69_Over_Shirt.png",
            "YanaX.Over == 'corset'", "images/YanaSex/Yana_69_Over_Corset.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #piercings
#            "not YanaX.Pierce", Null(),
            "YanaX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "YanaX.Uptop", "images/YanaSex/Yana_69_Pierce_Tits_R.png",

                    "YanaX.Over == 'towel'", "images/YanaSex/Yana_69_Pierce_Tits_R_Black.png",
                    "YanaX.Over == 'purple top'", "images/YanaSex/Yana_69_Pierce_Tits_R_Purp.png",
                    "YanaX.Over", "images/YanaSex/Yana_69_Pierce_Tits_R_Red.png", #Shirt or Corset
                    "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Pierce_Tits_R_Black.png",

                    "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_69_Pierce_Tits_R_Mesh.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_69_Pierce_Tits_R_Lace.png",
                    "YanaX.Chest", "images/YanaSex/Yana_69_Pierce_Tits_R_Red.png",

                    "True", "images/YanaSex/Yana_69_Pierce_Tits_R.png",
                    ),

            "YanaX.Pierce", ConditionSwitch( #barbells
                    "YanaX.Uptop", "images/YanaSex/Yana_69_Pierce_Tits_B.png",

                    "YanaX.Over == 'towel'", "images/YanaSex/Yana_69_Pierce_Tits_B_Black.png",
                    "YanaX.Over == 'purple top'", "images/YanaSex/Yana_69_Pierce_Tits_B_Purp.png",
                    "YanaX.Over", "images/YanaSex/Yana_69_Pierce_Tits_B_Red.png", #Shirt or Corset
                    "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Pierce_Tits_B_Black.png",

                    "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_69_Pierce_Tits_B_Mesh.png",
                    "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_69_Pierce_Tits_B_Lace.png",
                    "YanaX.Chest", "images/YanaSex/Yana_69_Pierce_Tits_B_Red.png",

                    "True", "images/YanaSex/Yana_69_Pierce_Tits_B.png",
                    ),
            "YanaX.Lust < 50 and not YanaX.OCount", Null(),                           #nips only poke at high lust
            "YanaX.Uptop", "images/YanaSex/Yana_69_Nips.png",

            "YanaX.Over == 'towel'", "images/YanaSex/Yana_69_Nips_Black.png",
            "YanaX.Over == 'purple top'", "images/YanaSex/Yana_69_Nips_Purp.png",
            "YanaX.Over", "images/YanaSex/Yana_69_Nips_Red.png", #Shirt or Corset
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Nips_Black.png",

            "YanaX.Chest == 'mesh top'", "images/YanaSex/Yana_69_Nips_Mesh.png",
            "YanaX.Chest == 'lace bra'", "images/YanaSex/Yana_69_Nips_Lace.png",
            "YanaX.Chest", "images/YanaSex/Yana_69_Nips_Red.png",

            "True", "images/YanaSex/Yana_69_Nips.png",
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_69_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/YanaSex/Yana_Sex_HeadRef.png",
        )
    zoom 1.0#.9#.8
    offset (15,80)#(85,150)#(75,30)#(145,150)#(250,210)#(175,175)
#    yoffset -163
# End Yana 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Yana_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Yana_69_CUN') and Speed != 3", "images/YanaSex/Yana_69_Tongue.png",
            "Speed == 1", "images/YanaSex/Yana_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/YanaSex/Yana_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_69_Spunk_Mouth.png",
            "('mouth' in YanaX.Spunk or 'chin' in YanaX.Spunk) and not Player.Male", "images/YanaSex/Yana_69_WetFace.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'chin' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_69_Spunk_Chin.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair over
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
#            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaSex/Yana_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in YanaX.Spunk or 'facial' in YanaX.Spunk)","images/YanaSex/Yana_69_Hair_Pony.png",

##            "YanaX.Hair == 'long'", "images/YanaSex/Yana_69_Hair_Long_Over.png",
#            "True", Null(),
#            ),

#        (0,0), "images/YanaSex/Yana_69_Hair_Short.png",
        (0,0), ConditionSwitch(
            #Hair over
            "Speed == 1", Null(), # and Player.Male", Null(),
            "Speed == 4", Null(), # and Player.Male", Null(),
            "Speed == 6", Null(), # and Player.Male", Null(),
            "(YanaX.Hair == 'long' and YanaX.Water) or YanaX.Hair == 'wetlong'", "images/YanaSex/Yana_69_Hair_Wet.png",
            "YanaX.Hair == 'long' and not Player.Male and ('hair' in YanaX.Spunk or 'facial' in YanaX.Spunk)","images/YanaSex/Yana_69_Hair_Wet.png",
            "YanaX.Hair == 'long'", "images/YanaSex/Yana_69_Hair_Long.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck over
            "(Speed == 0 or Speed == 2 or Speed == 3 or Speed == 5) and Player.Male", "images/YanaSex/Yana_69_Neck.png",
            "not Player.Male", "images/YanaSex/Yana_69_Neck.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #collar
            "not YanaX.Neck", Null(),
            "(Speed == 0 or Speed == 2 or Speed == 3 or Speed == 5) and Player.Male", "images/YanaSex/Yana_69_Collar.png",
            "not Player.Male", "images/YanaSex/Yana_69_Collar.png",
            "True", Null(),
            ),
        )
    zoom .8
    offset (153,260)#(0,0)#(145,150)
#    offset (0,0)#(175,135)#(175,175)
#    yoffset -163
# End Yana 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Yana_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair over
            "(YanaX.Hair == 'long' and YanaX.Water) or YanaX.Hair == 'wetlong'", "images/YanaSex/Yana_69_Hair_Wet.png",
            "YanaX.Hair == 'long' and not Player.Male and ('hair' in YanaX.Spunk or 'facial' in YanaX.Spunk)","images/YanaSex/Yana_69_Hair_Wet.png",
            "YanaX.Hair == 'long'", "images/YanaSex/Yana_69_Hair_Long.png",

#            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaSex/Yana_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in YanaX.Spunk or 'facial' in YanaX.Spunk)","images/YanaSex/Yana_69_Hair_Wet.png",
#            "True", "images/YanaSex/Yana_69_Hair_Short.png",
            "True", Null(),
            ),

        (0,0), "images/YanaSex/Yana_69_Neck.png",
        (0,0), ConditionSwitch(
            #collar
            "YanaX.Neck", "images/YanaSex/Yana_69_Collar.png",     # == 'spiked collar'
            "True", Null(),
            ),
        )
    zoom .8
    offset (153,260)#(0,0)#(145,150)
#    offset (0,0)#(175,135)#(180,100)
#    yoffset -163
# End Yana 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Yana_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair under
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
            "(YanaX.Hair == 'long' and YanaX.Water) or YanaX.Hair == 'wetlong'", "images/YanaSex/Yana_69_Hair_Wet_Under.png",
            "YanaX.Hair == 'long' and not Player.Male and ('hair' in YanaX.Spunk or 'facial' in YanaX.Spunk)","images/YanaSex/Yana_69_Hair_Wet_Under.png",
            "YanaX.Hair == 'long'", "images/YanaSex/Yana_69_Hair_Long_Under.png",

            "YanaX.Water or YanaX.Hair == 'wet'", "images/YanaSex/Yana_69_Hair_Short_Wet_Under.png",
            "not Player.Male and ('hair' in YanaX.Spunk or 'facial' in YanaX.Spunk)","images/YanaSex/Yana_69_Hair_Short_Wet_Under.png",
            "True", "images/YanaSex/Yana_69_Hair_Short_Under.png",
            ),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Yana_TJ_Animation')", Null(),
#            "YanaX.Hair == 'blonde'", "images/YanaSex/Yana_69_Hair_Blonde_Under.png",
#            "YanaX.Hair == 'long' or YanaX.Hair == 'wetlong'", "images/YanaSex/Yana_69_Hair_Long_Under.png",
#            "YanaX.Hair == 'wet' or YanaX.Hair == 'wetlong' or YanaX.Water", "images/YanaSex/Yana_69_Hair_Long.png",
#            "not Player.Male and 'facial' in YanaX.Spunk","images/YanaSex/Yana_Sprite_Hair_Wet.png",
            "True", Null(),#"images/YanaSex/Yana_69_Hair_Under.png",
            ),
        )
    zoom .8
    offset (153,260)#(145,150)#(175,135)#(175,175)
#    yoffset -163
# End Yana 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#image Yana_Sex_Legs = LiveComposite(
image Yana_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Yana_SexSprite
        (1120,840),
#        (0,0), "images/YanaSex/Yana_69_Hips.png",
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Legs_Dress_Under.png",
            "YanaX.Legs == 'skirt'", "images/YanaSex/Yana_69_Legs_Skirt_Under.png",
            "YanaX.Over == 'towel' and not YanaX.Uptop", "images/YanaSex/Yana_69_Legs_Towel_Under.png",
            "YanaX.Hose == 'stockings and garterbelt' or YanaX.Hose == 'garterbelt'", "images/YanaSex/Yana_69_Hose_Garter_Under.png",
            "YanaX.Hose == 'pantyhose' or YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_69_Under.png",
            "True", Null(),
            ),
        (0,0), "images/YanaSex/Yana_69_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "YanaX.Water", "images/YanaSex/Yana_Sex_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Yana_69_Anus",                                                                          #Anus Composite

        (0,0), "Yana_69_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(
            #hose layer
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_69_Hose_StockingsGarter.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaSex/Yana_69_Hose_Garter.png",
            "YanaX.Hose == 'stockings'", "images/YanaSex/Yana_69_Hose_Stockings.png",
            "YanaX.Hose == 'socks'", "images/YanaSex/Yana_69_Hose_Socks.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "YanaX.PantiesDown", ConditionSwitch(
                    "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_69_Panties_Bikini_Down.png",
                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_69_Panties_Bikini_Down.png",
        #            "YanaX.Panties and YanaX.Wet", "images/YanaSex/Yana_69_Panties_Gray_Up_Wet.png",
                    "YanaX.Panties", "images/YanaSex/Yana_69_Panties_Gray_Down.png",
                    "True", Null(),
                    ),
            "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_69_Panties_Lace.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_69_Panties_Bikini.png",
#            "YanaX.Panties and YanaX.Wet", "images/YanaSex/Yana_69_Panties_Gray_Wet.png",
            "YanaX.Panties", "images/YanaSex/Yana_69_Panties_Gray.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "YanaX.Panties and YanaX.PantiesDown", Null(),
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_69_Hose_Pantyhose.png",
            "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_69_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "YanaX.Upskirt", ConditionSwitch(
#                    "YanaX.Legs == 'shorts' and YanaX.Wet > 1", "images/YanaSex/Yana_69_Legs_Shorts_Wet.png",
                    "YanaX.Legs == 'shorts'", "images/YanaSex/Yana_69_Legs_Shorts_Down.png",
#                    "YanaX.Legs == 'pants' and YanaX.Wet > 1", "images/YanaSex/Yana_69_Legs_Yoga_Wet.png",
                    "YanaX.Legs == 'pants'", "images/YanaSex/Yana_69_Legs_Pants_Down.png",
                    "True", Null(),
                    ),
#            "YanaX.Legs == 'shorts' and YanaX.Wet > 1", "images/YanaSex/Yana_69_Legs_Shorts_Wet.png",
            "YanaX.Legs == 'shorts'", "images/YanaSex/Yana_69_Legs_Shorts.png",
#            "YanaX.Legs == 'pants' and YanaX.Wet > 1", "images/YanaSex/Yana_69_Legs_Yoga_Wet.png",
            "YanaX.Legs == 'pants'", "images/YanaSex/Yana_69_Legs_Pants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Dress Layer
            "YanaX.Legs == 'skirt'", "images/YanaSex/Yana_69_Legs_Skirt.png",
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Legs_Dress.png",
            "YanaX.Over == 'towel' and not YanaX.Uptop", "images/YanaSex/Yana_69_Legs_Dress.png",
#            "YanaX.Upskirt", Null(),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not YanaX.Pierce", Null(),
            "YanaX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
#                    "Player.Sprite and Player.Cock == 'in'", "images/YanaSex/Yana_Sex_Pussy_RingF.png",

                    "YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt' and not YanaX.Upskirt", "images/YanaSex/Yana_69_Pierce_Pussy_R_Black.png",

                    "YanaX.PantiesDown", "images/YanaSex/Yana_69_Pierce_Pussy_R.png",
                    "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_69_Pierce_Pussy_R_Lace.png",
                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_69_Pierce_Pussy_R_Red.png",
                    "YanaX.Hose == 'pantyhose' and not (YanaX.Panties and YanaX.PantiesDown)", "images/YanaSex/Yana_69_Pierce_Pussy_R_Red.png",
                    "YanaX.Panties", "images/YanaSex/Yana_69_Pierce_Pussy_R_Gray.png",

                    "True", "images/YanaSex/Yana_69_Pierce_Pussy_R.png",
                    ),
            #else, it's barbell
#            "Player.Sprite and Player.Cock == 'in'", "images/YanaSex/Yana_Sex_Pussy_BarbellF.png",

            "YanaX.Legs and YanaX.Legs != 'dress' and YanaX.Legs != 'skirt' and not YanaX.Upskirt", "images/YanaSex/Yana_69_Pierce_Pussy_B_Black.png",

            "YanaX.PantiesDown", "images/YanaSex/Yana_69_Pierce_Pussy_B.png",
            "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_69_Pierce_Pussy_B_Lace.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_69_Pierce_Pussy_B_Red.png",
            "YanaX.Hose == 'pantyhose' and not (YanaX.Panties and YanaX.PantiesDown)", "images/YanaSex/Yana_69_Pierce_Pussy_B_Red.png",
            "YanaX.Panties", "images/YanaSex/Yana_69_Pierce_Pussy_B_Gray.png",

            "True", "images/YanaSex/Yana_69_Pierce_Pussy_B.png",
            ),

#        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
#            "'belly' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Pelvis.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Yana_Hotdog_Zero_Anim2",
#            "Speed", "Yana_Hotdog_Zero_Anim1",
#            "True", "Yana_Hotdog_Zero_Anim0",
#            ),

        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Yana_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Yana_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "YanaX.Offhand == 'fondle pussy' and YanaX.Lust > 60 and not (Player.Sprite)",  At("YanaFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "YanaX.Offhand == 'fondle pussy'", At("YanaMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Yana_69_Fondle_Pussy",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", "Yana_Footcock_Zero_Anim2",
#            "Speed", "Yana_Footcock_Zero_Anim1",
#            "True", "Yana_Footcock_Static",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Yana_Footcock", Yana_Footcock_Zero_Anim2A()),
#            "Speed", At("Yana_Footcock", Yana_Footcock_Zero_Anim1A()),
#            "True", At("Yana_Footcock", Yana_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')", AlphaMask("Yana_69_Feet", "images/YanaSex/Yana_69_FeetMask.png"),
#            "not Speed", "Yana_69_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Yana_69_Feet", "images/YanaSex/Yana_69_FeetMask.png"),
#            "True", "Yana_69_Feet",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "YanaX.Upskirt", Null(),
#            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Feet_Dress.png",
#            "True", Null(),
#            ),
        )
    offset (10,25)#(15,80)

#image Yana_69_Feet = LiveComposite(
#        #the lower legs used in the sex pose, referenced by Yana_Sex_Legs
#        (1120,840),
##        (0,0), "images/YanaSex/Yana_Sex_Feet.png",                                                         #Legs Base
##        (0,0), ConditionSwitch(                                                                                 #Wet look
##            "YanaX.Water", "images/YanaSex/Yana_Sex_Water_Feet.png",
##            "True", Null(),
##            ),

#        (0,0), ConditionSwitch(
#            #hose layer
#            "YanaX.Legs and not YanaX.Upskirt and YanaX.Legs != 'blue skirt' and YanaX.Legs != 'shorts'",ConditionSwitch(
#                    #If she has pants on, I need alternate kneesocks to not clip through knees
#                    "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_69_Feet_Stockings.png",
#                    "YanaX.Hose == 'stockings'", "images/YanaSex/Yana_69_Feet_Stockings.png",
#                    "YanaX.Hose == 'knee stockings'", "images/YanaSex/Yana_69_Feet_Kneesocks.png",
#                    "YanaX.Panties and YanaX.PantiesDown", "images/YanaSex/Yana_69_Feet.png",
#                    "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_69_Feet_Stockings.png",
#                    "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_69_Feet_Stockings_Holed.png",
#                    "True", "images/YanaSex/Yana_69_Feet.png",
#                    ),
##            "YanaX.Legs and (not YanaX.Upskirt and YanaX.Legs != 'blue skirt' and YanaX.Legs != 'shorts') and YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_Sex_Hose_Stockings_FeetP.png",
##            "YanaX.Legs and (not YanaX.Upskirt and YanaX.Legs != 'blue skirt' and YanaX.Legs != 'blue skirt') and YanaX.Hose == 'stockings'", "images/YanaSex/Yana_Sex_Hose_Stockings_FeetP.png",
##            "YanaX.Legs and (not YanaX.Upskirt and YanaX.Legs != 'blue skirt' and YanaX.Legs != 'blue skirt') and YanaX.Hose == 'knee stockings'", "images/YanaSex/Yana_Sex_Hose_Stockings_FeetP.png",
#            "YanaX.Hose == 'stockings' or YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_69_Feet_Stockings.png",
#            "YanaX.Hose == 'knee stockings'", "images/YanaSex/Yana_69_Feet_Kneesocks.png",
#            "YanaX.Panties and YanaX.PantiesDown", Null(),
#            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_69_Feet_Stockings.png",
##            "YanaX.Legs and (not YanaX.Upskirt and YanaX.Legs != 'blue skirt' and YanaX.Legs != 'blue skirt') and YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_Hose_RippedPantyhose_FeetP.png",
#            "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_69_Feet_Stockings_Holed.png",
#            "True", "images/YanaSex/Yana_69_Feet.png",
#            ),

#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "YanaX.Upskirt", Null(),
#            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_69_Feet_Dress.png",
#            "YanaX.Legs == 'capris'", "images/YanaSex/Yana_69_Feet_Blue.png",
#            "YanaX.Legs == 'black jeans'", "images/YanaSex/Yana_69_Feet_Black.png",
#            "YanaX.Legs == 'yoga pants'", "images/YanaSex/Yana_69_Feet_Yoga.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #spunk
#            "'feet' in YanaX.Spunk", "images/YanaSex/Yana_Sex_Spunk_Feet.png",
#            "True", Null(),
#            ),
#        )


# Start Yana 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Yana_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/YanaSex/Yana_69_Pussy_Open.png",
                "YanaX.Offhand == 'fondle pussy' and YanaX.Lust > 60", "images/YanaSex/Yana_69_Pussy_Open.png",
                "True", "images/YanaSex/Yana_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not YanaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
            xzoom -1
#            offset (5,0)
    contains:
            # pubes
            ConditionSwitch(
                "not YanaX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/YanaSex/Yana_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Trigger == 'lick pussy'", "images/YanaSex/Yana_69_Pubes_Open.png",
#                "YanaX.Offhand == 'fondle pussy' and YanaX.Lust > 60", "images/YanaSex/Yana_69_Pubes_Open.png",
                "True", "images/YanaSex/Yana_69_Pubes.png",
                )
    contains:
            #Wet
            ConditionSwitch(
                "not YanaX.Wet", Null(),
                "(YanaX.Legs == 'yoga pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
                "YanaX.Panties and not YanaX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (15,0)
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in YanaX.Spunk or not Player.Male", Null(),
                "(YanaX.Legs == 'yoga pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
                "YanaX.Panties and not YanaX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (15,0)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in YanaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in YanaX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in YanaX.Spunk", "images/YanaSex/Yana_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "YanaX.Panties and YanaX.PantiesDown", Null(),
#                "YanaX.Hose == 'ripped pantyhose' and ShowFeet", "images/YanaSex/Yana_Sex_Hose_Pantyhose_Holed.png",
#                "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Yana_Sex_Fucking_Zero_Anim3", "Yana_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Yana_Sex_Fucking_Zero_Anim2", "Yana_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Yana_Sex_Fucking_Zero_Anim1", "Yana_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Yana_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "YanaX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/YanaSex/Yana_Sex_Pierce_Pussy_BarbellF.png",
#                "YanaX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/YanaSex/Yana_Sex_Pierce_Pussy_RingF.png",
#                "YanaX.Pierce == 'barbell'", "images/YanaSex/Yana_Sex_Pierce_Pussy_Barbell.png",
#                "YanaX.Pierce == 'ring'", "images/YanaSex/Yana_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Yana_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in YanaX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Yana_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Yana Pussy composite


image Yana_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,520)#(535,500
image Yana_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,580)#(535,580)

image Yana_69_Fondle_Pussy:
        "GropePussy_Yana"
        xzoom -1.3
        yzoom 1.3
#        rotate 180
        offset(-610,-300) #(-710,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Yana_69_Fondle_Pussy:
        "GropePussy_Yana"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Yana_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/YanaSex/Yana_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/YanaSex/Yana_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Yana_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Yana_Sex_Anal_Tip",
            "YanaX.Plug", "images/PlugBase_Sex.png",
            "YanaX.Loose > 2", "Yana_Gape_Anal_69",
#            "YanaX.Loose", "images/YanaSex/Yana_Sex_Hole_Loose.png",
            "True", "images/YanaSex/Yana_69_Anus.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in YanaX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/YanaSex/Yana_Sex_Spunk_Anal_Under.png",
#                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Yana_Sex_Anal_Spunk_Heading_Under",
                "True", "images/BetsySex/Betsy_69_Spunk_Ass.png",
                )
            offset (-8,10)#(-8,-5)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Yana_Sex_Anal_Zero_Anim3", "Yana_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Yana_Sex_Anal_Zero_Anim2", "Yana_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Yana_Sex_Anal_Zero_Anim1", "Yana_Sex_Anal_Mask"),
#                "True", AlphaMask("Yana_Sex_Anal_Zero_Anim0", "Yana_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in YanaX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Yana_Sex_Anal_Spunk_Heading_Over",
#                "True", "Yana_Sex_Anal_Spunk",
#                )

image Yana_Gape_Anal_Sex2:
        #removing an anal plug
        contains:
            #Hole
            "images/YanaSex/Yana_69_Anus_Gape.png"
            transform_anchor True
            subpixel True
            anchor (730,700)#(560,620)
            offset (730,700)#(560,617)
            zoom .30 # tight
            block:
                ease 3 zoom .40 #in.87
                ease 3 zoom .30 #out
                repeat

image Yana_Gape_Anal_69:
        "Yana_Gape_Anal_Sex2"
#        xzoom -1.5
#        yzoom 1.5
        offset(-175,-200) #(-890,-300)

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Static:
        #this is the animation for Yana's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-125) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-130) #top -130
#                pause .5
                ease 1.25 pos (0,-125) #bottom -125
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#(675,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Yana's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-125) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-130) #top -130
#                pause .5
                ease 1.25 pos (0,-125) #bottom -125
                repeat
        #this is the animation for Yana's upper body during 69, Speed 0 (static)
#        contains:
#            "Yana_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,-35) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (0,-40) #top
#                pause .25
#                ease 1 pos (0,-35) #bottom
#                repeat
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-80) #top -80
                pause .25
                ease 1 pos (0,-60) #bottom -70
                repeat
        #this is the animation for Yana's lower body during 69, Speed 0 (static)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (0,25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,20) #top
                pause .25
                ease 1 pos (0,25) #bottom
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Anim1:
        #this is the animation for Yana's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Yana_69_HairBack"
            transform_anchor True
            anchor (450,320)#(450,180)# (610,420)
            offset (605,620)#(620,720)#
            rotate 190
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,-10) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -160 #top -10(35,-65)
                pause .75#1.25
                ease 2.5 ypos -10 #bottom 150(85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 180#210
                pause 1.5
                ease 1.25 rotate 190#240
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos -30 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos 5 #bottom 175(85,50)
                pause 1 #1.25
                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (licking)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#(#(675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 0
                pause 1.75
                ease 1.5 rotate -5
                pause .75
                repeat
        #this is the animation for Yana's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Yana_69_Head"
            transform_anchor True
            anchor (450,320)#(450,180)# (610,420)
            offset (615,620)#(760,880)#(620,720)#
            rotate 240
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .50 rotate 90#210
#                pause 1.5
#                ease 1.25 rotate 180#240
#                pause 1.25
#                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -160 #top -10(35,-65)
                pause .75#1.25
                ease 2.5 ypos 0 #bottom 150(85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 210#210
                pause 1.5
                ease 1.25 rotate 240#240
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos -30 #top -50
                pause .75#1.25
                ease 2.0 xpos 0 #bottom 175(85,50)
                pause 1 #1.25
                repeat
        contains:
            subpixel True
            "Yana_69_HairOver"
            transform_anchor True
            anchor (450,320)#(450,180)# (610,420)
            offset (615,620)#(620,720)#
            rotate 210
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,-10) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -160 #top -10(35,-65)
                pause .75#1.25
                ease 2.5 ypos -10 #bottom 150(85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 200#210
                pause 1.5
                ease 1.25 rotate 210#190
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos -30 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos 5 #bottom 175(85,50)
                pause 1 #1.25
                repeat
##        contains:
##            subpixel True
##            "Yana_69_Tits"
##            rotate 180
###            zoom .65
##            pos (30,40) #X less is left, Y less is up
##            block:
##                #Total time, 5 seconds
##                pause .5
##                easein .75 pos (10,-10) #top
##                pause 1.25
##                ease 2.5 pos (30,40) #bottom
##                repeat
        #this is the animation for Yana's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Yana_69_Body"
            rotate 180
            pos (85,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos 30 #top (10,-70)
                pause .8
                ease 1.4 xpos 70 #bottom(30,-10)
                ease 1.3 xpos 85 #bottom(30,-10)
#                pause 1.3
                pause .25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -90 #top (10,-70)
                pause .8
                ease 2.7 ypos 60 #bottom(30,-10)
                pause .25
                repeat
#        #this is the animation for Yana's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Yana_69_Legs"
            rotate 185
            pos (80,105) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 pos (30,-15)#(0,-5)
                pause .5
                ease 2.5 pos (80,105)#(30,25)
                pause .5
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 rotate 180
                pause .5
                ease 2.5 rotate 185
                pause .5
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Anim2:
        #this is the animation for Yana's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-120) #top -160
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Yana's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-120) #top -160
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Yana's upper body during 69, Speed 2 (heading)
#        contains:
#            "Yana_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (0,-20) #top
#                pause .25
#                ease 1 pos (0,0) #bottom
#                repeat
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-70) #top -10
                pause .25
                ease 1 pos (0,-50) #bottom 0
                repeat
        #this is the animation for Yana's lower body during 69, Speed 2 (heading)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,25) #top
                pause .25
                ease 1 pos (0,40) #bottom
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Anim3:
        #this is the animation for Yana's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-80) #top -20
#                pause .5
                ease 1.25 pos (0,-30) #bottom 30
                repeat
#        #this is the animation for Zero's cock during 69, Speed 3 (sucking)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Yana's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-80) #top -20
#                pause .5
                ease 1.25 pos (0,-30) #bottom 30
                repeat
        #this is the animation for Yana's upper body during 69, Speed 3 (sucking)
#        contains:
#            subpixel True
#            "Yana_69_Tits"
#            rotate 180
#            anchor (560,400)#(560,330) + is right and down
#            offset (700,715)#(-560,-330) + is right and down
#            transform_anchor True
##            zoom .65
#            pos (0,30) #X less is left, Y less is up
##            alpha .9
#            parallel:
#                #Total time, 3 seconds
#                easein .75 pos (0,-5) #top
#                ease 1.25 pos (0,30) #bottom
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                ease .15 yzoom 1.2
#                ease .25 yzoom 1
#                ease .35 yzoom 1.1

#                ease .5 yzoom .8
#                ease .75 yzoom 1         #bottom
#                repeat
        #this is the animation for Yana's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Yana_69_Body"
            rotate 180
#            zoom .65
            pos (0,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-60) #top 0
#                pause .5
                ease 1.25 pos (0,-20) #bottom 40
                repeat
        #this is the animation for Yana's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Yana_69_Legs"
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25) #-5
#                pause .5
                ease 1.25 pos (0,40) #10
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Anim4:
        #this is the animation for Yana's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-30) #top 30
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Zero's cock during 69, Speed 4 (deep)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Yana's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-30) #top 30
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        contains:
            subpixel True
            "Yana_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-35) #top 25
                pause .5
                ease 1.75 pos (0,0) #bottom 60
                repeat
        #this is the animation for Yana's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Yana_69_Tits"
#            rotate 180
##            zoom .65
#            pos (0,40) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,5) #top
#                pause .5
#                ease 1.75 pos (0,40) #bottom
#                repeat
#        contains:
#            subpixel True
#            "Yana_69_Tits"
#            rotate 180
#            anchor (560,400)#(560,330) + is right and down
#            offset (700,715)#(-560,-330) + is right and down
#            transform_anchor True
##            zoom .65
#            pos (0,40) #X less is left, Y less is up
##            alpha .9
#            parallel:
#                #Total time, 3 seconds
#                easein .75 pos (0,5) #top
#                pause .5
#                ease 1.75 pos (0,40) #bottom
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                ease .15 yzoom 1.2
#                ease .25 yzoom 1
#                ease .35 yzoom 1.1
#                pause .5
#                ease .5 yzoom .9
#                ease 1.25 yzoom 1         #bottom
#                repeat
        contains:
            subpixel True
            "Yana_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-25) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Yana's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Yana_69_Legs"
            rotate 180
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,55)
#                pause .5
                ease 2.25 pos (0,60)
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Anim5:
        #this is the animation for Yana's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 0.5 pos (0,-110) #top -160
                pause 1.25
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Yana's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 0.5 pos (0,-110) #top -160
                pause 1.25
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Yana's upper body during 69, Speed 2 (heading)
#        contains:
#            "Yana_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (0,-20) #top
#                pause .25
#                ease 1 pos (0,0) #bottom
#                repeat
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-90) #top -10
                pause .25
                ease 1 pos (0,-70) #bottom 0
                repeat
        #this is the animation for Yana's lower body during 69, Speed 2 (heading)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,25) #top
                pause .25
                ease 1 pos (0,40) #bottom
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Anim6:
        #this is the animation for Yana's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein .75 pos (0,-10) #top 30
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Zero's cock during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Yana's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein .75 pos (0,-10) #top 30
                ease 1.75 pos (0,10) #bottom 70
                repeat
        contains:
            subpixel True
            "Yana_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein .75 pos (0,-15) #top 25
                ease 1.75 pos (0,0) #bottom 60
                repeat
        #this is the animation for Yana's upper body during 69, Speed 6 (cum deep)
#        contains:
#            subpixel True
#            "Yana_69_Tits"
#            rotate 180
##            zoom .65
#            pos (0,30) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,35) #top
#                pause .5
#                ease 1.75 pos (0,30) #bottom
#                repeat
        contains:
            subpixel True
            "Yana_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Yana's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Yana_69_Legs"
            rotate 180
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,55)
#                pause .5
                ease 2.25 pos (0,60)
                repeat

#End Animations for Yana's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Yana 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Yana's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Yana_69_Anim1",
                "Speed == 2",   "Yana_69_Cun2",
                "Speed == 3",   "Yana_69_Cun3",
                "Speed",        "Yana_69_Cun1",
                "True",         "Yana_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Yana's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Cun0:
        #this is the animation for Yana's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-120) #(10,-120) X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-115) #top
#                pause .5
                ease 1.25 pos (10,-120) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Pussy",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Legs",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Yana's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-120) #(10,-120) X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-115) #top
#                pause .5
                ease 1.25 pos (10,-120) #bottom
                repeat
        #this is the animation for Yana's upper body during 69, Speed 0 (static)
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (5,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (5,-75) #top 35
                pause .5
                ease 1.75 pos (5,-70) #bottom 70
                repeat
        #this is the animation for Yana's lower body during 69, Speed 0 (static)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (15,25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (15,25) #top
                pause .25
                ease 1 pos (15,25) #bottom
                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Cun1:
        #this is the animation for Yana's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -115 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause .5
#                ease .5 xpos 32 #top
#                pause .25
#                easein 1.25 xpos 0 #bottom
#                pause .5
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause .5
#                easein .5 rotate 180 #top
#                pause .25
#                easein 1.25 rotate 185 #bottom
#                pause .5
#                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (lick)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Pussy",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Legs",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        #this is the animation for Yana's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 185
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -115 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                easein .5 rotate 175 #top
                pause .25
                easein 1.25 rotate 185 #bottom
                pause .5
                repeat
        contains:
            subpixel True
            "Yana_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -115 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause .5
#                ease .5 xpos 32 #top
#                pause .25
#                easein 1.25 xpos 12 #bottom
#                pause .5
#                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                easein .5 rotate 180 #top
                pause .25
                easein 1.25 rotate 185 #bottom
                pause .5
                repeat
        #this is the animation for Yana's upper body during 69, Speed 1 (lick)
#        contains:
#            "Yana_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (15,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.25 pos (15,-5) #top
#                pause .25
#                ease 1.25 pos (15,0) #bottom
#                repeat
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (10,-75) #top
                pause .25
                ease 1.25 pos (10,-70) #bottom
                repeat
        #this is the animation for Yana's lower body during 69, Speed 1 (lick)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (15,20) #X less is left, Y less is up
#            block:
#                pause .25
#                easein 1.5 pos (15,25) #top
#                pause .25
#                ease 1 pos (15,20) #bottom
#                repeat


#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Cun2:
        #this is the animation for Yana's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-105) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -100 #top
                easein 1.1 ypos -105 #bottom
                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause 0.2
#                easein .8 xpos 0 #top
#                easein 1.0 xpos 32 #bottom
#                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (clit)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Pussy",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Legs",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Yana's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 178
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-105) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -100 #top
                easein 1.1 ypos -105 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.2
                easein .8 rotate 183 #top
                easein 1.0 rotate 178 #bottom
                repeat
        #this is the animation for Yana's upper body during 69, Speed 2 (clit)
#        contains:
#            "Yana_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (10,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1 pos (10,-5) #top
#                ease 1 pos (10,0) #bottom
#                repeat
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-75) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-80) #top
                ease 1 pos (10,-75) #bottom
                repeat
        #this is the animation for Yana's lower body during 69, Speed 2 (clit)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (15,25) #X less is left, Y less is up
#            block:
#                pause .25
#                easein 1.5 pos (15,-30) #top
#                pause .25
#                ease 1 pos (15,-25) #bottom
#                repeat

#Start Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_69_Cun3:
        #this is the animation for Yana's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Yana_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .5 ypos -95 #top -150
                pause 1.25
                ease 1.25 ypos -90 #bottom -145
                repeat
        #this is the animation for Zero's cock during 69, Speed 3 (suck)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Pussy",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        contains:
            #pussy
            ConditionSwitch(
                "Ch_Focus is YanaX and Player.Sprite", "Zero_Legs",
                "True",Null(),
                )
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(745,921)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        #this is the animation for Yana's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Yana_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .5 ypos -95 #top -150
                pause 1.25
                ease 1.25 ypos -90 #bottom -145
                repeat
        #this is the animation for Yana's upper body during 69, Speed 3 (suck)
#        contains:
#            "Yana_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (10,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .3
#                easein 1.5 pos (10,-5) #top
#                pause .3
#                ease .9 pos (10,0) #bottom
#                repeat
        contains:
            "Yana_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-65) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-70) #top
                pause .25
                ease 1 pos (10,-65) #bottom
                repeat
        #this is the animation for Yana's lower body during 69, Speed 3 (suck)
        contains:
            "Yana_69_Legs"
            subpixel True
            rotate 180
            pos (15,35) #X less is left, Y less is up
#            block:
#                pause .25
#                easein 1.5 pos (15,25) #top
#                pause .25
#                ease 1 pos (15,35) #bottom
#                repeat
#End Animations for Yana's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Yana 69 Animations

# Start Yana Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Yana_SC_Anim_2",
                "Speed", "Yana_SC_Anim_1",
                "True", "Yana_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (700,200)#(650,303)
    zoom 1#0.85

image Yana_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Yana_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not YanaX.Wet", Null(),
            "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
            "YanaX.Panties and not YanaX.PantiesDown", Null(),
            "Player.Cock == 'foot'", Null(),
            "YanaX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in YanaX.Spunk or not Player.Male", Null(),
            "Player.Cock == 'foot'", Null(),
            "(YanaX.Legs == 'pants' or YanaX.Legs == 'shorts') and not YanaX.Upskirt", Null(),
            "YanaX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #skin behind hose layer
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "YanaX.Panties and YanaX.PantiesDown", Null(),
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_UnderLegs.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/YanaSex/Yana_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Yana_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/YanaSex/Yana_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/YanaSex/Yana_Sex_Ass.png",
            "True", "images/YanaSex/Yana_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "YanaX.Red", "images/YanaSex/Yana_Sex_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/YanaSex/Yana_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not YanaX.Water", Null(),
            "True", "images/YanaSex/Yana_Sex_Water_Legs.png",
            ),

#        (0,0), "Yana_Sex_Anus",
            #Anus Composite

        (0,0), "Yana_SC_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "YanaX.Hose == 'stockings and garterbelt'", "images/YanaSex/Yana_Sex_Hose_StockingsGarter.png",
            "YanaX.Hose == 'socks'", "images/YanaSex/Yana_Sex_Hose_Socks.png",
            "YanaX.Hose == 'garterbelt'", "images/YanaSex/Yana_Sex_Hose_Garter.png",
            "YanaX.Hose == 'stockings'", "images/YanaSex/Yana_Sex_Hose_Stockings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "YanaX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
                    "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Panties_Lace_Down.png",
                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Panties_Bikini_Down.png",
                    "YanaX.Panties", "images/YanaSex/Yana_Sex_Panties_Gray_Down.png",
                    "True", Null(),
                    ),
            "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Panties_Lace.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Panties_Bikini.png",
            "YanaX.Panties and YanaX.Wet", "images/YanaSex/Yana_Sex_Panties_Gray_Wet.png",
            "YanaX.Panties", "images/YanaSex/Yana_Sex_Panties_Gray.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "YanaX.Panties and YanaX.PantiesDown", Null(),
#            "YanaX.Hose == 'tights'", "images/YanaSex/Yana_Sex_Hose_Tights.png",
#            "YanaX.Hose == 'ripped tights'", "images/YanaSex/Yana_Sex_Hose_Tights_Holed.png",
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_Hose_Pantyhose.png",
            "YanaX.Hose == 'ripped pantyhose'", "images/YanaSex/Yana_Sex_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "YanaX.Legs == 'skirt'", "images/YanaSex/Yana_Sex_Legs_Skirt.png",
            "YanaX.Legs == 'dress'", "images/YanaSex/Yana_Sex_Legs_Dress.png",
            "YanaX.Legs == 'pants' and YanaX.Upskirt", "images/YanaSex/Yana_Sex_Legs_Pants_Down.png",
            "YanaX.Legs == 'pants' and YanaX.Wet > 1", "images/YanaSex/Yana_Sex_Legs_Pants_Wet.png",
            "YanaX.Legs == 'pants'", "images/YanaSex/Yana_Sex_Legs_Pants.png",
            "YanaX.Legs == 'shorts' and YanaX.Upskirt", "images/YanaSex/Yana_Sex_Legs_Shorts_Down.png",
            "YanaX.Legs == 'shorts' and YanaX.Wet > 1", "images/YanaSex/Yana_Sex_Legs_Shorts_Wet.png",
            "YanaX.Legs == 'shorts'", "images/YanaSex/Yana_Sex_Legs_Shorts.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
            "not YanaX.Pierce", Null(),
            "YanaX.Legs == 'dress' or YanaX.Legs == 'skirt'", Null(),
            "Player.Sprite and Player.Cock == 'in' and Speed", Null(),
            "YanaX.Pierce == 'ring'",ConditionSwitch(
                    "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_R_Black.png",
                    "YanaX.Legs == 'shorts' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_R_Black.png",

                    "YanaX.PantiesDown", Null(), #"images/YanaSex/Yana_Sex_Pierce_Pussy_R.png",
                    "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Pierce_R_Red.png",
                    "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_Pierce_R_Lace.png",
                    "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Pierce_R_Lace.png",
                    "YanaX.Panties", "images/YanaSex/Yana_Sex_Pierce_R_Gray.png",
                    "True", Null(), #"images/YanaSex/Yana_Sex_Pierce_R.png",
                    ),
            #else, it's barbell
            "YanaX.Legs == 'pants' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_B_Black.png",
            "YanaX.Legs == 'shorts' and not YanaX.Upskirt", "images/YanaSex/Yana_Sex_Pierce_B_Black.png",

            "YanaX.PantiesDown", Null(), #"images/YanaSex/Yana_Sex_Pierce_B.png",
            "YanaX.Panties == 'bikini bottoms'", "images/YanaSex/Yana_Sex_Pierce_B_Red.png",
            "YanaX.Hose == 'pantyhose'", "images/YanaSex/Yana_Sex_Pierce_B_Lace.png",
            "YanaX.Panties == 'lace panties'", "images/YanaSex/Yana_Sex_Pierce_B_Lace.png",
            "YanaX.Panties", "images/YanaSex/Yana_Sex_Pierce_B_Gray.png",
            "True", Null(), #"images/YanaSex/Yana_Sex_Pierce_B.png",
            ),
        (0,0), ConditionSwitch(
            #towel Layer
            "YanaX.Over == 'towel'", "images/YanaSex/Yana_Sex_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in YanaX.Spunk and Player.Male", "images/YanaSex/Yana_Sex_Spunk_Foot2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Yana_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Yana_Sex_Lick_Ass",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #pussy fondling animation
#            "Trigger3 == 'fondle pussy' and YanaX.Lust > 60 and not (Player.Sprite)",  At("YanaFingerHand", GirlFingerPussyX()), #"Yana_Sex_Mast2",
#            "Trigger3 == 'fondle pussy'", At("YanaMastHand", GirlGropePussyX()), #"Yana_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Yana_Sex_Fondle_Pussy",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Footjob overlay
#            "Player.Cock == 'foot'", Null(),
#            "True", "Yana_Sex_Foot",
#            ),
        )
# End Yana SC Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Yana Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Yana_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Yana_Sex_Heading_Pussy",
#                "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'out')", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "Trigger3 == 'fondle pussy' and YanaX.Lust > 60", "images/YanaSex/Yana_Sex_Pussy_Open.png",
                "True", "images/YanaSex/Yana_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not YanaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/DoreenSex/Doreen_Sex_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not YanaX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/YanaSex/Yana_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/YanaSex/Yana_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Trigger == 'lick pussy'", "images/YanaSex/Yana_Sex_Pubes_Open.png",
#                "Trigger3 == 'fondle pussy' and YanaX.Lust > 60", "images/YanaSex/Yana_Sex_Pubes_Open.png",
                "True", "images/YanaSex/Yana_Sex_Pubes_Closed.png",
                )

    #End Yana Pussy composite

# Start Yana Sex Pose Speed 0 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_SC_Anim_0:
    # Pose for Yana's Sex Pose in which she is scissoring at speed 0 (static)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            anchor (800,325)#(410,470)
            offset (910,410) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (20,2) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 1 ypos 0#-40 #-140
                pause 0.8
                ease 1 ypos 2#-60 #-180
                pause 0.2
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_SC_Legs"
            anchor (800,325)#(410,470)
            offset (925,470)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (20,-23) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 1 ypos -20 #10
                pause 0.8
                ease 1 ypos -23 #0
                repeat
#    contains:
#            subpixel True
##            "Yana_Sex_Zero_Cock"
#            "Zero_Blowcock"
#            zoom .4#.5
#            subpixel True
#            pos (550,550) #(630,520)
#            rotate -5 #0
#            alpha 0.5
#            parallel:
#                pause 0.2
#                ease 1 rotate -10 #10
#                pause 0.8
#                ease 1 rotate -5 #0
#                repeat
    contains:
            #pussy
            "Zero_Pussy_Full"
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            offset (791,785)#(750,770)
#            block: #adds to 5
#                ease 1 offset (0,0)
#                ease 1 offset (0,500)
#                ease 1 offset (750,700)
#                ease 1 offset (500,0)
#                ease 1 offset (0,0)
#                ease 1 offset (0,0)
#                ease 1 offset (0,-500)
#                ease 1 offset (-500,-500)
#                ease 1 offset (-500,0)
#                ease 1 offset (0,0)
#                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot"
            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
            offset (925,465)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (20,-20) #X less is left, Y less is up (200,-180)
            parallel:
#                pause 0.2
                ease 1.2 rotate 32#50 #10
                pause 0.8
                ease 1 rotate 30 #0
                repeat

# End main animation for Sex Pose scissoring Speed 0

# End Yana Sex Pose Speed 0 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 1 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_SC_Anim_1:
    # Pose for Yana's Sex Pose in which she is scissoring at speed 1 (slow)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            anchor (800,325)#(410,470)
            offset (910,410) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (0,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 1 ypos 0#-40 #-140
                pause 0.8
                ease 1 ypos 5#-60 #-180
                pause 0.2
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_SC_Legs"
            anchor (800,325)#(410,470)
            offset (925,470)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (0,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 1 ypos 0 #10
                pause 0.8
                ease 1 ypos 10 #0
                repeat
#    contains:
#            subpixel True
##            "Yana_Sex_Zero_Cock"
#            "Zero_Blowcock"
#            zoom .4#.5
#            subpixel True
#            pos (550,550) #(630,520)
#            rotate -5 #0
#            alpha 0.5
#            parallel:
#                pause 0.2
#                ease 1 rotate -10 #10
#                pause 0.8
#                ease 1 rotate -5 #0
#                repeat
    contains:
            #pussy
            "Zero_Pussy_Full"
            anchor (.5,.5)
            zoom .7#.45
            pos (0,-10)#(410,790)
            offset (791,785)#(750,770)
            parallel: #adds to 5
#                pause 0.2
                ease 1 ypos 0 #10
                pause 1#0.8
                ease 1 ypos -10 #0
                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot"
            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
            offset (925,465)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,0) #X less is left, Y less is up (200,-180)
            parallel:
#                pause 0.2
                ease 1.2 rotate 30#50 #10
                pause 0.8
                ease 1 rotate 35 #0
                repeat

# End main animation for Sex Pose scissoring Speed 1

# End Yana Sex Pose Speed 1 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Yana Sex Pose Speed 2 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Yana_SC_Anim_2:
    # Pose for Yana's Sex Pose in which she is scissoring at speed 2 (fast)
    contains:
            #Yana's underlying body
            subpixel True
            "Yana_Sex_Body"
            anchor (800,325)#(410,470)
            offset (910,410) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (0,20) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                pause .1#0.8
                ease .3 ypos 25#-40 #-140
#                pause 0.8
                ease .5 ypos 30#-60 #-180
                repeat
    contains:
            #Yana's Legs
            subpixel True
            "Yana_SC_Legs"
            anchor (800,325)#(410,470)
            offset (925,470)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (0,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.1
                easeout .3 ypos 0 #10
                ease .5 ypos 10 #0
                repeat
#    contains:
#            subpixel True
##            "Yana_Sex_Zero_Cock"
#            "Zero_Blowcock"
#            zoom .4#.5
#            subpixel True
#            pos (550,550) #(630,520)
#            rotate -5 #0
#            alpha 0.5
#            parallel:
#                pause 0.2
#                ease 1 rotate -10 #10
#                pause 0.8
#                ease 1 rotate -5 #0
#                repeat
    contains:
            #pussy
            "Zero_Pussy_Full"
            anchor (.5,.5)
            zoom .7#.45
            pos (0,-10)#(410,790)
            offset (791,785)#(750,770)
            parallel: #adds to 5
                easeout .3 ypos -10 #10
                pause .1#0.8
                ease .5 ypos 5 #0
                repeat
    contains:
            #Yana's Feet
            subpixel True
            "Yana_Sex_Foot"
            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
            offset (925,465)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (0,5) #X less is left, Y less is up (200,-180)
            parallel:
                ease .3 rotate 40#50 #10
                ease .5 rotate 38 #0
                pause .1#0.8
                repeat

# End main animation for Sex Pose Scissor Speed 2

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Yana_SC_Launch(Line = Trigger):
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Yana_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(YanaX,1) #call Rogue_Hide
    show Yana_SC_Sprite zorder 150
    with dissolve
    return

label Yana_SC_Reset:
    if not renpy.showing("Yana_SC_Sprite"):
        return
    $ YanaX.ArmPose = 2
    hide Yana_SC_Sprite
    call Girl_Hide(YanaX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


## End Yana Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# End Yana Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


## Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Yana Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Yana_Kissing_Launch(T = Trigger,Set=1):
#    call Girl_Hide(YanaX) #call Rogue_Hide
#    $ Trigger = T
#    $ YanaX.Pose = "kiss" if Set else YanaX.Pose
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 110
#    show Yana_Sprite at SpriteLoc(StageCenter) zorder 110:
#        ease 0.5 offset (100,0) zoom 2 alpha 1
#    return

#label Yana_Kissing_Smooch:
#    $ YanaX.FaceChange("kiss")
#    show Yana_Sprite at SpriteLoc(StageCenter) zorder 110:
#        ease 0.5 xpos StageCenter offset (100,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos YanaX.SpriteLoc zoom 1
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 110:
#        zoom 1
#    $ YanaX.FaceChange("sexy")
#    return

#label Yana_Breasts_Launch(T = Trigger,Set=1):
#    call Girl_Hide(YanaX) #call Rogue_Hide
#    $ Trigger = T
#    $ YanaX.Pose = "breasts" if Set else YanaX.Pose
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 110:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Yana_Middle_Launch(T = Trigger,Set=1):
#    call Girl_Hide(YanaX) #call Rogue_Hide
#    $ Trigger = T
#    $ YanaX.Pose = "mid" if Set else YanaX.Pose
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 110:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Yana_Pussy_Launch(T = Trigger,Set=1):
#    call Girl_Hide(YanaX) #call Rogue_Hide
#    $ Trigger = T
#    $ YanaX.Pose = "pussy" if Set else YanaX.Pose
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder 110:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Yana_Pos_Reset(T = 0,Set=0):
#    if YanaX.Loc != bg_current:
#            return
#    call Girl_Hide(YanaX) #call Rogue_Hide
#    show Yana_Sprite at SpriteLoc(YanaX.SpriteLoc) zorder YanaX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Yana_Sprite zorder YanaX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (YanaX.SpriteLoc,50)
#    $ YanaX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Yana_Hide(Sprite=0):
##        call Yana_Sex_Reset
#        hide Yana_SexSprite
#        hide Yana_Doggy_Animation
#        hide Yana_HJ_Animation
#        hide Yana_BJ_Animation
#        hide Yana_TJ_Animation
#        hide Yana_Finger_Animation
#        hide Yana_CUN_Animation
#        hide Yana_69_Animation
#        hide Yana_69_CUN
#        hide Yana_Seated
#        if Sprite:
#                hide Yana_Sprite
#        return



## Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Yana:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (255,370)#(275,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Yana:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (160,350)#(190,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image LickRightBreast_Yana:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (240,350)#(270,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (220,330)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (240,350)#(105,375) bottom
            repeat

image LickLeftBreast_Yana:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (145,335) #(195,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (130,305)#(135,335)
            pause .5
            ease 1.5 rotate 30 pos (145,335)#(200,410)
            repeat

image GropeThigh_Yana:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (215,650)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (205,740) #(205,740) bottom
            ease 1 rotate 100 pos (215,650)   #245,640
            repeat

image GropePussy_Yana:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (205,580)#(240,580)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 ypos 565 #(190)
                ease .75 rotate 170 ypos 580
            choice:
                ease .5 rotate 190 ypos 565
                pause .25
                ease 1 rotate 170 ypos 580
            repeat

image FingerPussy_Yana:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (210,660)#(275,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (220,635)#(150,665)
                pause .5
                ease 1 rotate 50 pos (210,660)  #(140,700)
            choice:
                ease .5 rotate 40 pos (220,635)
                pause .5
                ease 1.75 rotate 50 pos (210,660)
            choice:
                ease 2 rotate 40 pos (220,635)
                pause .5
                ease 1 rotate 50 pos (210,660)
            choice:
                ease .25 rotate 40 pos (220,635)
                ease .25 rotate 50 pos (210,660)
                ease .25 rotate 40 pos (220,635)
                ease .25 rotate 50 pos (210,660)
            repeat

image Lickpussy_Yana:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (230,610)#(155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (220,590) #(210,605)
            linear .5 rotate -60 pos (210,600) #(200,615)
            easein 1 rotate 10 pos (230,610) #(230,625)
            repeat

image VibratorRightBreast_Yana:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (135,330)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            pause .25
            ease 1 rotate 35 ypos 320
            pause .25
            ease 1 rotate 55 ypos 330
            repeat

image VibratorLeftBreast_Yana:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (230,340) #(270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 330
            pause .25
            ease 1 rotate 55 ypos 340
            pause .25
            repeat

image VibratorPussy_Yana:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (220,605) #(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 pos (210,595)
            pause .25
            ease 1 rotate 70 pos (220,605)
            pause .25
            repeat

image VibratorAnal_Yana:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (265,590)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 pos (245,580)
            pause .25
            ease 1 rotate 10 pos (255,590)
            pause .25
            repeat

image VibratorPussyInsert_Yana:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (220,580)#(240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Yana:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,570)#(250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Yana:
    contains:
        "GirlGropeLeftBreast_Yana"
    contains:
        "GirlGropeRightBreast_Yana"

image GirlGropeLeftBreast_Yana:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (260,350) #(220,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 350#(280,390)
            ease 1 rotate -10 ypos 340
            repeat

image GirlGropeRightBreast_Yana:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (140,350) #(90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 ypos 360#(90,410)
            ease 1 rotate -10 ypos 350
            repeat

image GirlGropeThigh_Yana:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (250,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 740
            ease 1 ypos 650
            repeat
        parallel:
            pause .5
            ease .5 xpos 223
            ease .5 xpos 220
            ease .5 xpos 223
            ease .5 xpos 225
            repeat

image GirlGropePussy_YanaSelf:
    contains:
        "GirlGropePussy_Yana"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (305,565)#(265,615)

image GirlGropePussy_Yana:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,580)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 570
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 570#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 580 #(205,590)
                ease .75 rotate 200 ypos 585 #(205,595)
                ease .5 rotate 205 ypos 580
                ease .75 rotate 200 ypos 585
            choice: #Fast stroke
                ease .3 rotate 205 ypos 580
                ease .3 rotate 200 ypos 590
                ease .3 rotate 205 ypos 580
                ease .3 rotate 200 ypos 590
            repeat

image GirlFingerPussy_Yana:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (215,590)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 585
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 585
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 585
                ease .75 rotate 200 ypos 590
                ease .5 rotate 205 ypos 585
                ease .75 rotate 200 ypos 590
            choice: #Fast stroke
                ease .3 rotate 205 ypos 585
                ease .3 rotate 200 ypos 595
                ease .3 rotate 205 ypos 585
                ease .3 rotate 200 ypos 595
            repeat



image YanaMastHand:
        "images/UI_GirlHand_Jean.png"
        zoom 0.8
        rotate 240
        offset (385,270)

image YanaFingerHand:
        "images/UI_GirlFinger_Jean.png"
        zoom 0.8
        rotate 220
        offset (360,330)

# Start of Illyana disc appearance stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Magik_Solid_Appear:
        #this is a blank solid I use to test things.
        contains:
            #the contains portion is necessary for the motion to translate to her Alpha
            Solid("#75d7ec", xysize=(1024,768))
#            alpha 0.2
            ypos -800
            pause .5
            linear 1 ypos 20

image Magik_Appear:
        #Shows when Illyana appears
#        contains:
#            "Magik_Solid_Exit"
##            ypos 0
##            ease 2 ypos -1000
        contains:
            "images/YanaSprite/Yana_Sprite_Disc_Back.png"
            alpha 0
            anchor (0.5, 0.0)
            offset (572,0)#(60,0)
            zoom .80  #.75
            yoffset 620
            parallel:
                ypos -750#-800
                pause .5
                linear 1 ypos 70#20
            parallel:
                pause .5
                ease .1 alpha 1
                pause .9

#        contains:
#            "Yana_Sprite"
#            xoffset 512

        contains:
            AlphaMask("Yana_Sprite", "Magik_Solid_Appear")
            xoffset 332#332

        contains:
            "images/YanaSprite/Yana_Sprite_Disc_Over.png"
            alpha 0
            anchor (0.5, 0.0)
            offset (572,0)#(60,0)
            zoom .80  #.75
            yoffset 620
            parallel:
                pause .5
                ypos -750#-800
                linear 1 ypos 70#20
            parallel:
                pause .5
                ease .1 alpha 1
                pause .9

#end image Magik_Appear:

image Magik_Solid_Exit:
        #this is a blank solid I use to test things.
        contains:
            #the contains portion is necessary for the motion to translate to her Alpha
            Solid("#75d7ec", xysize=(1024,768))
#            alpha 0.2
            ypos 20
            pause .5
            linear 1 ypos -800

image Magik_Exit:
        #Shows when Illyana appears
#        contains:
#            "Magik_Solid_Exit"
##            ypos 0
##            ease 2 ypos -1000
        contains:
            "images/YanaSprite/Yana_Sprite_Disc_Back.png"
            alpha 1
            anchor (0.5, 0.0)
            offset (572,0)#(60,0)
            zoom .80  #.75
            yoffset 620
            parallel:
                ypos 70
                pause .5
                linear 1 ypos -750
            parallel:
                pause .5
                pause .9
                ease .1 alpha 0

#        contains:
#            "Yana_Sprite"
#            xoffset 512

        contains:
            AlphaMask("Yana_Sprite", "Magik_Solid_Exit")
            xoffset 332#512

        contains:
            "images/YanaSprite/Yana_Sprite_Disc_Over.png"
            alpha 1
            anchor (0.5, 0.0)
            offset (572,0)#(60,0)
            zoom .80  #.75
            yoffset 620
            parallel:
                ypos 70
                pause .5
                linear 1 ypos -750
            parallel:
                pause .5
                pause .9
                ease .1 alpha 0

#end image Magik_Exit:


label Show_Yana:
        # launcher for showing Magik entering
        if renpy.showing("Yana_Sprite"):
                return
        show Magik_Appear at Sprite_Set(YanaX.SpriteLoc,50) zorder YanaX.Layer
        pause 1.5
        show Yana_Sprite at Sprite_Set(YanaX.SpriteLoc,50) zorder YanaX.Layer
        hide Magik_Appear
        return

label Hide_Yana:
        # launcher for showing Magik leaving
        if not renpy.showing("Yana_Sprite"):
                return
        show Magik_Exit at Sprite_Set(YanaX.SpriteLoc,50) zorder YanaX.Layer
        hide Yana_Sprite at Sprite_Set(YanaX.SpriteLoc,50) zorder YanaX.Layer
        pause 1.5
        hide Magik_Exit
        return
# End of Illyana disc appearance stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End of Illyana disc appearance stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
