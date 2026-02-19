# Basic character Sprites
layeredimage Rogue_Sprite:
    always:
        "images/RogueSprite/Rogue_Sprite_Shadow.png"
    if renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation') or renpy.showing('Rogue_CUN_Animation'):
        Null()
    else:
        "Rogue_HairBack" offset (185, 38)
    if not RogueX.Over:
        Null()
    elif RogueX.Over == 'cape':
        "images/RogueSprite/modification/Rogue_over_cape_back.png"
    elif RogueX.Over == 'hoodie':
        Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_hoodieB.png")
    elif RogueX.Uptop:
        if RogueX.ArmPose == 1:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh1_Up.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty_Up.png")
        else:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh2_Up.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty_Up.png")
    else:
        if RogueX.ArmPose == 1:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh1.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty1.png")
        else:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh2.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty2.png")
    if RogueX.Legs == 'pants' and RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSprite/Rogue_pantsback.png")
    if RogueX.ArmPose == 1:
        if RogueX.Pubes and RogueX.Pierce == 'ring':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_1_haired_ring.png"
        elif RogueX.Pubes and RogueX.Pierce == 'barbell':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_1_haired_barbell.png"
        elif RogueX.Pierce == 'ring':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_1_ring.png"
        elif RogueX.Pierce == 'barbell':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_1_barbell.png"
        elif RogueX.Pubes:
            Recolor("Rogue", "Pubes", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_1_haired.png")
        else:
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_1_bare.png"
    elif RogueX.Pubes and RogueX.Pierce == 'ring':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_2_haired_ring.png"
    elif RogueX.Pubes and RogueX.Pierce == 'barbell':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_2_haired_barbell.png"
    elif RogueX.Pierce == 'ring':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_2_ring.png"
    elif RogueX.Pierce == 'barbell':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_2_barbell.png"
    elif RogueX.Pubes:
        Recolor("Rogue", "Pubes", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_2_haired.png")
    else:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_body_2_bare.png"
    if not RogueX.Panties:
        Null()
    elif RogueX.Legs == 'pants' and not RogueX.Upskirt:
        Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties.png")
    elif RogueX.PantiesDown:
        if RogueX.Wet > 1:
            if RogueX.Panties == 'shorts':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_shorts_down_wet.png")
            elif RogueX.Panties == 'green panties':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_undies_down_wet.png")
            elif RogueX.Panties == 'bikini bottoms':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties_bikini_down.png")
            elif RogueX.Panties == 'harness panties':
                "images/RogueSprite/modification/Rogue_sprite_underwear_panties_harness_down_wet.png"
            elif RogueX.Panties == 'raven leotard':
                "images/RogueSprite/modification/Rogue_panties_Raven_Down.png"
            else:
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties_down.png")
        else:
            if RogueX.Panties == 'shorts':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_shorts_down.png")
            elif RogueX.Panties == 'green panties':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_undies_down.png")
            elif RogueX.Panties == 'bikini bottoms':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties_bikini_down.png")
            elif RogueX.Panties == 'harness panties':
                "images/RogueSprite/modification/Rogue_sprite_underwear_panties_harness_down.png"
            elif RogueX.Panties == 'raven leotard':
                "images/RogueSprite/modification/Rogue_panties_Raven_Down.png"
            else:
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties_down.png")
    else:
        if RogueX.Wet > 1:
            if RogueX.Panties == 'shorts' and RogueX.Wet > 1:
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_shorts_wet.png")
            elif RogueX.Panties == 'green panties' and RogueX.Wet > 1:
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_undies_wet.png")
            elif RogueX.Panties == 'lace panties':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_lacepanties.png")
            elif RogueX.Panties == 'bikini bottoms':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties_bikini.png")
            elif RogueX.Panties == 'harness panties':
                "images/RogueSprite/modification/Rogue_sprite_underwear_panties_harness_wet.png"
            elif RogueX.Panties == 'raven leotard':
                "images/RogueSprite/modification/Rogue_panties_Raven.png"
            else:
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties.png")
        else:
            if RogueX.Panties == 'shorts':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_shorts.png")
            elif RogueX.Panties == 'green panties':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_undies.png")
            elif RogueX.Panties == 'lace panties':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_lacepanties.png")
            elif RogueX.Panties == 'bikini bottoms':
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties_bikini.png")
            elif RogueX.Panties == 'harness panties':
                "images/RogueSprite/modification/Rogue_sprite_underwear_panties_harness.png"
            elif RogueX.Panties == 'raven leotard':
                "images/RogueSprite/modification/Rogue_panties_Raven.png"
            else:
                Recolor("Rogue", "Panties", "images/RogueSprite/Rogue_panties.png")
    if RogueX.Hose == 'stockings':
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_Stockings.png")
    elif RogueX.Hose == 'stockings and garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_StockingsandGarter.png")
    elif RogueX.Hose == 'garterbelt':
        "images/RogueSprite/Rogue_Hose_Garter.png"
    if RogueX.Panties and RogueX.PantiesDown:
        Null()
    elif RogueX.Hose == 'pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_Pantyhose.png")
    elif RogueX.Hose == 'tights' and RogueX.Wet:
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_Tights_Wet.png")
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_Tights.png")
    elif RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_Pantyhose_Holed.png")
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueSprite/Rogue_Hose_Tights_Holed.png")
    if not RogueX.Wet and Player.Male:
        Null()
    elif RogueX.Legs == 'pants' and not RogueX.Upskirt:
        Null()
    elif RogueX.Panties and not RogueX.PantiesDown and RogueX.Wet <= 1:
        Null()
    elif RogueX.Wet == 1:
        if RogueX.Panties and RogueX.PantiesDown:
            AlphaMask("Wet_Drip","Rogue_Drip_MaskP") offset (240, 560)
        elif RogueX.Legs == 'pants':
            AlphaMask("Wet_Drip","Rogue_Drip_MaskPn") offset (240, 560)
        else:
            AlphaMask("Wet_Drip","Rogue_Drip_Mask") offset (240, 560)
    else:
        if RogueX.Panties and RogueX.PantiesDown:
            AlphaMask("Wet_Drip2","Rogue_Drip_MaskP") offset (240, 560)
        elif RogueX.Panties and RogueX.Legs == 'pants':
            AlphaMask("Wet_Drip","Rogue_Drip_MaskPn") offset (240, 560)
        elif RogueX.Legs == 'pants':
            AlphaMask("Wet_Drip2","Rogue_Drip_MaskPn") offset (240, 560)
        elif RogueX.Panties:
            AlphaMask("Wet_Drip","Rogue_Drip_Mask") offset (240, 560)
        else:
            AlphaMask("Wet_Drip2","Rogue_Drip_Mask") offset (240, 560)
    if not RogueX.Wet:
        Null()
    elif RogueX.Legs and RogueX.Wet <= 1:
        Null()
    elif RogueX.Legs:
        "images/RogueSprite/Rogue_wet.png"
    elif RogueX.Wet == 1:
        "images/RogueSprite/Rogue_wet.png"
    else:
        "images/RogueSprite/Rogue_wet2.png"
    if ('in' not in RogueX.Spunk and 'anal' not in RogueX.Spunk) or not Player.Male:
        Null()
    elif RogueX.Legs == 'pants' and not RogueX.Upskirt:
        Null()
    else:
        if RogueX.Panties and RogueX.PantiesDown:
            AlphaMask("Spunk_Drip2","Rogue_Drip_MaskP") offset (240, 560)
        elif RogueX.Panties and RogueX.Legs == 'pants':
            AlphaMask("Spunk_Drip","Rogue_Drip_MaskPn") offset (240, 560)
        elif RogueX.Legs == 'pants':
            AlphaMask("Spunk_Drip2","Rogue_Drip_MaskPn") offset (240, 560)
        else:
            AlphaMask("Spunk_Drip2","Rogue_Drip_Mask") offset (240, 560)
    if RogueX.Boots == 'sneaks':
        "images/RogueSprite/Rogue_boots_sneaks.png"
    elif RogueX.Boots == 'boots high shoes':
        "images/RogueSprite/modification/Rogue_sprite_boots_high_shoes.png"
    elif RogueX.Boots:
        "images/RogueSprite/Rogue_boots.png"
    if RogueX.Legs == 'pants' and RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSprite/Rogue_legs_pants_down.png")
    elif RogueX.Legs == 'pants' and RogueX.Wet > 1:
        Recolor("Rogue", "Legs", "images/RogueSprite/Rogue_legs_pants_wet.png")
    elif RogueX.Legs == 'pants':
        Recolor("Rogue", "Legs", "images/RogueSprite/Rogue_legs_pants.png")
    elif RogueX.Legs == 'skirt' and RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSprite/Rogue_legs_skirt_up.png")
    elif RogueX.Legs == 'skirt':
        Recolor("Rogue", "Legs", "images/RogueSprite/Rogue_legs_skirt.png")
    elif RogueX.Legs == 'short skirt' and RogueX.Upskirt:
        "images/RogueSprite/modification/Rogue_Sprite_legs_short_skirt_up.png"
    elif RogueX.Legs == 'short skirt':
        "images/RogueSprite/modification/Rogue_Sprite_legs_short_skirt.png"
    elif RogueX.Legs == 'SR7 skirt' and RogueX.Upskirt:
        "images/RogueSprite/modification/Rogue_Sprite_legs_SR7_skirt_up.png"
    elif RogueX.Legs == 'SR7 skirt':
        "images/RogueSprite/modification/Rogue_Sprite_legs_SR7_skirt.png"
    elif RogueX.Legs == 'bottom harem' and RogueX.Upskirt:
        "images/RogueSprite/modification/Rogue_sprite_skirt_harem_bottom_up.png"
    elif RogueX.Legs == 'bottom harem' and RogueX.Wet > 1:
        "images/RogueSprite/modification/Rogue_sprite_skirt_harem_bottom_wet.png"
    elif RogueX.Legs == 'bottom harem':
        "images/RogueSprite/modification/Rogue_sprite_skirt_harem_bottom.png"
    if RogueX.ArmPose == 1 and RogueX.Arms == 'gloves' and RogueX.Neck == 'spiked collar':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms1a_gloved.png"
    elif RogueX.ArmPose == 1 and RogueX.Arms == 'gloves':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms1b_gloved.png"
    elif RogueX.ArmPose == 1 and RogueX.Neck == 'spiked collar':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms1a_bare.png"
    elif RogueX.ArmPose == 1:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms1b_bare.png"
    elif RogueX.Arms == 'gloves' and RogueX.Neck == 'spiked collar':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms2_gloved.png"
    elif RogueX.Arms == 'gloves':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms2b_gloved.png"
    elif RogueX.Neck == 'spiked collar':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms2_bare.png"
    else:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_arms2b_bare.png"
    if not RogueX.Chest:
        Null()
    elif RogueX.Uptop:
        if RogueX.Chest == 'tank':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_tank_Up.png")
        elif RogueX.Chest == 'tube top':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_tube_Up.png")
        elif RogueX.Chest == 'buttoned tank':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_tank2_Up.png")
        elif RogueX.Chest == 'bra':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_bra_Up.png")
        elif RogueX.Chest == 'sports bra':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_sportsbra_Up.png")
        elif RogueX.Chest == 'lace bra':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_lacebra_Up.png")
        elif RogueX.Chest == 'bikini top':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_bikini_Up.png")
        elif RogueX.Chest == 'SR7 tank top':
            "images/RogueSprite/modification/Rogue_Sprite_chest_SR7_tank_top_Up.png"
        elif RogueX.Chest == 'raven leotard':
            "images/RogueSprite/modification/Rogue_chest_Raven_Up.png"
        elif RogueX.Chest == 'harness bra':
            "images/RogueSprite/modification/Rogue_sprite_underwear_bra_harness_up.png"
    else:
        if RogueX.Chest == 'tank':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_tank.png")
        elif RogueX.Chest == 'tube top':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_tube.png")
        elif RogueX.Chest == 'buttoned tank':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_tank2.png")
        elif RogueX.Chest == 'bra':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_bra.png")
        elif RogueX.Chest == 'sports bra':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_sportsbra.png")
        elif RogueX.Chest == 'lace bra':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_lacebra.png")
        elif RogueX.Chest == 'bikini top':
            Recolor("Rogue", "Chest", "images/RogueSprite/Rogue_chest_bikini.png")
        elif RogueX.Chest == 'SR7 tank top':
            "images/RogueSprite/modification/Rogue_Sprite_Chest_SR7_tank_top.png"
        elif RogueX.Chest == 'harness bra':
            "images/RogueSprite/modification/Rogue_sprite_underwear_bra_harness.png"
        elif RogueX.Chest == 'raven leotard' and RogueX.ArmPose == 1:
            "images/RogueSprite/modification/Rogue_chest_Raven1.png"
        elif RogueX.Chest == 'raven leotard' and RogueX.ArmPose == 2:
            "images/RogueSprite/modification/Rogue_chest_Raven2.png"
    if RogueX.Water and RogueX.ArmPose == 1:
        "images/RogueSprite/Rogue_body_wet1.png"
    elif RogueX.Water:
        "images/RogueSprite/Rogue_body_wet2.png"
    if RogueX.Water == 3:
        "images/RogueSprite/Rogue_body_wet3.png"
    if not RogueX.Over:
        Null()
    elif RogueX.Uptop:
        if RogueX.ArmPose == 1:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh1_Up.png")
            elif RogueX.Over == 'pink top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_pink1_Up.png")
            elif RogueX.Over == 'hoodie':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_hoodie1_Up.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty_Up.png")
            elif RogueX.Over == 'cape':
                "images/RogueSprite/modification/Rogue_over_cape_front1.png"
            elif RogueX.Over == 'top harem':
                "images/RogueSprite/modification/Rogue_sprite_over_harem_arms1_top_up.png"
        else:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh2_Up.png")
            elif RogueX.Over == 'pink top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_pink2_Up.png")
            elif RogueX.Over == 'hoodie':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_hoodie2_Up.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty_Up.png")
            elif RogueX.Over == 'cape':
                "images/RogueSprite/modification/Rogue_over_cape_front2.png"
            elif RogueX.Over == 'top harem':
                "images/RogueSprite/modification/Rogue_sprite_over_harem_arms2_top_up.png"
    else:
        if RogueX.ArmPose == 1:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh1.png")
            elif RogueX.Over == 'pink top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_pink1.png")
            elif RogueX.Over == 'towel':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_towel1.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty1.png")
            elif RogueX.Over == 'hoodie':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_hoodie1.png")
            elif RogueX.Over == 'cape':
                "images/RogueSprite/modification/Rogue_over_cape_front1.png"
            elif RogueX.Over == 'dress blue' and RogueX.Upskirt:
                "images/RogueSprite/modification/Rogue_sprite_over_dress_blue_arms1_bottom_up.png"
            elif RogueX.Over == 'dress blue':
                "images/RogueSprite/modification/Rogue_sprite_over_dress_blue_arms1.png"
            elif RogueX.Over == 'dress red' and RogueX.Upskirt:
                "images/RogueSprite/modification/Rogue_sprite_over_dress_red_arms1_bottom_up.png"
            elif RogueX.Over == 'dress red':
                "images/RogueSprite/modification/Rogue_sprite_over_dress_red_arms1.png"
            elif RogueX.Over == 'top harem':
                "images/RogueSprite/modification/Rogue_sprite_over_harem_arms1_top.png"
        else:
            if RogueX.Over == 'mesh top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_mesh2.png")
            elif RogueX.Over == 'pink top':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_pink2.png")
            elif RogueX.Over == 'hoodie':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_hoodie2.png")
            elif RogueX.Over == 'nighty':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_nighty2.png")
            elif RogueX.Over == 'towel':
                Recolor("Rogue", "Over", "images/RogueSprite/Rogue_over_towel2.png")
            elif RogueX.Over == 'cape':
                "images/RogueSprite/modification/Rogue_over_cape_front2.png"
            elif RogueX.Over == 'dress blue' and RogueX.Upskirt:
                "images/RogueSprite/modification/Rogue_sprite_over_dress_blue_arms2_bottom_up.png"
            elif RogueX.Over == 'dress blue':
                "images/RogueSprite/modification/Rogue_sprite_over_dress_blue_arms2.png"
            elif RogueX.Over == 'dress red' and RogueX.Upskirt:
                "images/RogueSprite/modification/Rogue_sprite_over_dress_red_arms2_bottom_up.png"
            elif RogueX.Over == 'dress red':
                "images/RogueSprite/modification/Rogue_sprite_over_dress_red_arms2.png"
            elif RogueX.Over == 'top harem':
                "images/RogueSprite/modification/Rogue_sprite_over_harem_arms2_top.png"
    if RogueX.Acc == 'belt':
        "images/RogueSprite/modification/Rogue_acc_belt.png"
    elif RogueX.Acc == 'sweater' and RogueX.ArmPose != 1:
        "images/RogueSprite/Rogue_acc_sweater2.png"
    elif RogueX.Acc == 'sweater':
        "images/RogueSprite/Rogue_acc_sweater.png"
    if renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation') or renpy.showing('Rogue_CUN_Animation'):
        Null()
    else:
        "Rogue_Head" offset (185, 38)
    if 'hand' in RogueX.Spunk and RogueX.ArmPose != 1 and Player.Male:
        "images/RogueSprite/Rogue_spunkhand.png"
    if 'belly' in RogueX.Spunk and Player.Male:
        "images/RogueSprite/Rogue_spunkbelly.png"
    if 'tits' in RogueX.Spunk and Player.Male:
        "images/RogueSprite/Rogue_spunktits.png"
    if RogueX.Lust > 70:
        "Steam" offset (230, 600)
    if not RogueX.Held or RogueX.ArmPose == 1:
        Null()
    elif RogueX.ArmPose != 1 and RogueX.Held == 'phone':
        "images/RogueSprite/Rogue_held_phone.png"
    elif RogueX.ArmPose != 1 and RogueX.Held == 'dildo':
        "images/RogueSprite/Rogue_held_dildo.png"
    elif RogueX.ArmPose != 1 and RogueX.Held == 'vibrator':
        "images/RogueSprite/Rogue_held_vibrator.png"
    elif RogueX.ArmPose != 1 and RogueX.Held == 'panties':
        "images/RogueSprite/Rogue_held_panties.png"
    if Trigger == 'lesbian' or not RogueX.Offhand:
        Null()
    elif RogueX.Offhand == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70:
        "GirlFingerPussy"
    elif RogueX.Offhand == 'fondle pussy':
        "GirlGropePussy"
    elif RogueX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'):
        "GirlGropeRightBreast"
    elif RogueX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts'):
        "GirlGropeLeftBreast"
    elif RogueX.Offhand == 'fondle breasts':
        "GirlGropeRightBreast"
    elif RogueX.Offhand == 'vibrator breasts':
        "VibratorRightBreast"
    elif RogueX.Offhand == 'vibrator pussy':
        "VibratorPussy"
    elif RogueX.Offhand == 'vibrator pussy insert':
        "VibratorPussy"
    elif RogueX.Offhand == 'vibrator anal':
        "VibratorAnal"
    elif RogueX.Offhand == 'vibrator anal insert':
        "VibratorPussy"
    if not Partner or Partner is RogueX or RogueX in Nearby:
        Null()
    elif Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and RogueX.Lust >= 70:
        "GirlFingerPussy"
    elif Partner.Offhand == 'fondle girl pussy':
        "GirlGropePussy"
    elif Partner.Offhand == 'lick girl pussy':
        "Lickpussy"
    elif Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts'):
        "LickLeftBreast"
    elif Partner.Offhand == 'suck girl breasts':
        "LickRightBreast"
    elif Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts'):
        "GirlGropeLeftBreast"
    elif Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'):
        "GirlGropeRightBreast"
    elif Partner.Offhand == 'fondle girl breasts':
        "GirlGropeRightBreast"
    elif Partner.Offhand == 'vibrator girl breasts':
        "VibratorRightBreast"
    elif Partner.Offhand == 'vibrator girl pussy':
        "VibratorPussy"
    elif Partner.Offhand == 'vibrator girl pussy insert':
        "VibratorPussy"
    elif Partner.Offhand == 'vibrator girl anal':
        "VibratorAnal"
    elif Partner.Offhand == 'vibrator girl anal insert':
        "VibratorPussy"
    if not Partner or Partner is not RogueX:
        Null()
    elif Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and RogueX.Lust >= 70:
        "GirlFingerPussy"
    elif Ch_Focus.Offhand == 'fondle girl pussy':
        "GirlGropePussy"
    elif Ch_Focus.Offhand == 'lick girl pussy':
        "Lickpussy"
    elif Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts'):
        "LickLeftBreast"
    elif Ch_Focus.Offhand == 'suck girl breasts':
        "LickRightBreast"
    elif Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts'):
        "GirlGropeLeftBreast"
    elif Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'):
        "GirlGropeRightBreast"
    elif Ch_Focus.Offhand == 'fondle girl breasts':
        "GirlGropeRightBreast"
    elif Ch_Focus.Offhand == 'vibrator girl breasts':
        "VibratorRightBreast"
    elif Ch_Focus.Offhand == 'vibrator girl pussy':
        "VibratorPussy"
    elif Ch_Focus.Offhand == 'vibrator girl pussy insert':
        "VibratorPussy"
    elif Ch_Focus.Offhand == 'vibrator girl anal':
        "VibratorAnal"
    elif Ch_Focus.Offhand == 'vibrator girl anal insert':
        "VibratorPussy"
    if not Trigger or Ch_Focus is not RogueX:
        Null()
    elif Trigger == 'vibrator breasts':
        "VibratorLeftBreast"
    elif Trigger == 'fondle thighs':
        "GropeThigh"
    elif Trigger == 'fondle breasts':
        "GropeRightBreast"
    elif Trigger == 'suck breasts':
        "LickRightBreast"
    elif Trigger == 'vibrator pussy':
        "VibratorPussy"
    elif Trigger == 'vibrator pussy insert':
        "VibratorPussy"
    elif Trigger == 'vibrator anal':
        "VibratorAnal"
    elif Trigger == 'vibrator anal insert':
        "VibratorPussy"
    elif Trigger == 'fondle pussy' and Speed == 2:
        "FingerPussy"
    elif Trigger == 'fondle pussy':
        "GropePussy"
    elif Trigger == 'lick pussy':
        "Lickpussy"
    if not Trigger2 or Ch_Focus is not RogueX:
        Null()
    elif Trigger2 == 'fondle breasts' and Trigger == 'suck breasts':
        "GropeLeftBreast"
    elif Trigger2 == 'fondle breasts':
        "GropeLeftBreast"
    elif Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts':
        "VibratorLeftBreast"
    elif Trigger2 == Trigger:
        Null()
    elif Trigger2 == 'vibrator breasts':
        "VibratorRightBreast"
    elif Trigger2 == 'suck breasts':
        "LickLeftBreast"
    elif Trigger2 == 'vibrator pussy':
        "VibratorPussy"
    elif Trigger2 == 'vibrator pussy insert':
        "VibratorPussy"
    elif Trigger2 == 'vibrator anal':
        "VibratorAnal"
    elif Trigger2 == 'vibrator anal insert':
        "VibratorPussy"
    elif Trigger2 == 'fondle pussy':
        "GropePussy"
    elif Trigger2 == 'lick pussy':
        "Lickpussy"
    elif Trigger2 == 'fondle thighs':
        "GropeThigh"
    anchor (0.5, 0.0)
    zoom .75
layeredimage Rogue_Head:
    if RogueX.Blush > 1:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_base_blush2.png"
    elif RogueX.Blush:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_base_blush.png"
    else:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_base.png"
    if RogueX.HeadAcc == 'jewel':
        "images/RogueSprite/modification/Rogue_sprite_face_jewel.png"
    if RogueX.Mouth == 'normal':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_normal.png")
    elif RogueX.Mouth == 'lipbite':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_lipbite.png")
    elif RogueX.Mouth == 'sucking' or RogueX.Mouth == 'open':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_surprised.png")
    elif RogueX.Mouth == 'kiss':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_kiss.png")
    elif RogueX.Mouth == 'sad':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_sad.png")
    elif RogueX.Mouth == 'smile':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_smile.png")
    elif RogueX.Mouth == 'grimace':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_smile.png")
    elif RogueX.Mouth == 'surprised':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_surprised.png")
    elif RogueX.Mouth == 'tongue':
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_licking.png")
    else:
        Recolor("Rogue", "Lips", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_mouth_normal.png")
    if 'chin' in RogueX.Spunk and Player.Male:
        "images/RogueSprite/Rogue_Sprite_spunk_chin.png"
    if 'mouth' not in RogueX.Spunk or not Player.Male:
        Null()
    elif RogueX.Mouth == 'normal':
        "images/RogueSprite/Rogue_Sprite_spunk_normal.png"
    elif RogueX.Mouth == 'lipbite':
        "images/RogueSprite/Rogue_Sprite_spunk_lipbite.png"
    elif RogueX.Mouth == 'sucking':
        "images/RogueSprite/Rogue_Sprite_spunk_licking.png"
    elif RogueX.Mouth == 'kiss':
        "images/RogueSprite/Rogue_Sprite_spunk_kiss.png"
    elif RogueX.Mouth == 'sad':
        "images/RogueSprite/Rogue_Sprite_spunk_sad.png"
    elif RogueX.Mouth == 'smile':
        "images/RogueSprite/Rogue_Sprite_spunk_smile.png"
    elif RogueX.Mouth == 'grimace':
        "images/RogueSprite/Rogue_Sprite_spunk_smile.png"
    elif RogueX.Mouth == 'surprised' or RogueX.Mouth == 'open':
        "images/RogueSprite/Rogue_Sprite_spunk_licking.png"
    elif RogueX.Mouth == 'tongue':
        "images/RogueSprite/Rogue_Sprite_spunk_licking.png"
    else:
        "images/RogueSprite/Rogue_Sprite_spunk_normal.png"
    if RogueX.Blush > 1:
        if RogueX.Brows == 'angry':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_angry_b.png"
        elif RogueX.Brows == 'sad':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_sad_b.png"
        elif RogueX.Brows == 'surprised':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_surprised_b.png"
        elif RogueX.Brows == 'confused':
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_confused_b.png"
        else:
            "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_normal_b.png"
    elif RogueX.Brows == 'angry':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_angry.png"
    elif RogueX.Brows == 'sad':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_sad.png"
    elif RogueX.Brows == 'surprised':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_surprised.png"
    elif RogueX.Brows == 'confused':
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_confused.png"
    else:
        "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_brows_normal.png"
    always:
        "Rogue Blink"
    if 'chin' in RogueX.Spunk and not Player.Male:
        "images/RogueSprite/Rogue_Sprite_face_wet.png"
    elif Trigger != 'blow' or 'mouth' not in RogueX.Spunk or not Player.Male:
        Null()
    elif Speed == 3:
        "images/RogueSprite/Rogue_Sprite_face_over_sucking_cum.png"
    elif Speed == 4:
        "images/RogueSprite/Rogue_Sprite_face_over_sucking_cum.png"
    if RogueX.Water:
        Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_wet.png")
    elif RogueX.Hair == 'cosplay':
        Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_cos.png")
    elif RogueX.Hair == 'wet':
        Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_wet.png")
    elif not Player.Male and ('hair' in RogueX.Spunk or 'facial' in RogueX.Spunk):
        Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_wet.png")
    else:
        Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_evo.png")
    if RogueX.Water:
        "images/RogueSprite/Rogue_Sprite_wet.png"
    elif not Player.Male and ('hair' in RogueX.Spunk or 'facial' in RogueX.Spunk):
        "images/RogueSprite/Rogue_Sprite_wet.png"
    if 'hair' in RogueX.Spunk and Player.Male:
        "images/RogueSprite/Rogue_Sprite_spunk_hair.png"
    elif 'facial' in RogueX.Spunk and Player.Male:
        "images/RogueSprite/Rogue_Sprite_spunk_facial.png"
    if RogueX.Mask == 'mask harem':
        "images/RogueSprite/modification/Rogue_sprite_mask_harem.png"
    zoom .29
image Rogue_HairBack:
    ConditionSwitch(
        #Hair underlay
            "RogueX.Water or RogueX.Hair == 'wet'", Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_wet_back.png"),
            "not Player.Male and ('hair' in RogueX.Spunk or 'facial' in RogueX.Spunk)", Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_wet_back.png"),
            "RogueX.Hair == 'cosplay'", Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_cos_back.png"),
            "True", Recolor("Rogue", "Hair", "images/RogueSprite/Rogue_Sprite_hair_evo_back.png"),
            ),
    zoom .29
image Rogue Blink:
    #eyeblinks
    ConditionSwitch(
        "RogueX.Eyes == 'normal'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_normal.png",
        "RogueX.Eyes == 'sexy'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_sexy.png",
        "RogueX.Eyes == 'closed'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_closed.png",
        "RogueX.Eyes == 'surprised'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_surprised.png",
        "RogueX.Eyes == 'leftside'", "images/RogueSprite/Rogue_Sprite_face_eyes_leftside.png",
        "RogueX.Eyes == 'side'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_side.png",
        "RogueX.Eyes == 'stunned'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_stunned.png",
        "RogueX.Eyes == 'down'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_down.png",
        "RogueX.Eyes == 'manic'", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_manic.png",
        "RogueX.Eyes == 'squint'", "Rogue_Squint",
        "True", "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_normal.png",
        )
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_closed.png"
    .25
    repeat
image Rogue_Squint:
    "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_sexy.png",
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/RogueSprite/[RogueX.skin_image.skin_path]Rogue_Sprite_face_eyes_squint.png",
    .25
    repeat
image Rogue_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/RogueSprite/Rogue_WetMask.png"
        offset (-240,-560)
image Rogue_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/RogueSprite/Rogue_WetMaskP.png"
        offset (-240,-560)
image Rogue_Drip_MaskPn:
    #This is the mask for her drip pattern in pants down mode
    contains:
        "images/RogueSprite/Rogue_WetMaskPn.png"
        offset (-240,-560)



# Rogue Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Rogue_Doggy_Base = LiveComposite(
layeredimage Rogue_Doggy_Animation:
    if not Player.Sprite:
        "Rogue_Doggy_Body"
    elif Player.Cock == 'anal':
        if Speed > 2:
            "Rogue_Doggy_Fuck2_Top"
        elif Speed > 1:
            "Rogue_Doggy_Fuck_Top"
        elif Speed:
            "Rogue_Doggy_Anal_Head_Top"
        else:
            "Rogue_Doggy_Body"
    elif Player.Cock == 'in':
        if Speed > 2:
            "Rogue_Doggy_Fuck2_Top"
        elif Speed > 1:
            "Rogue_Doggy_Fuck_Top"
        else:
            "Rogue_Doggy_Body"
    else:
        "Rogue_Doggy_Body"
    if not Player.Sprite:
        "Rogue_Doggy_Ass"
    elif Player.Cock == 'anal':
        if Speed > 2:
            "Rogue_Doggy_Fuck2_Ass"
        elif Speed > 1:
            "Rogue_Doggy_Fuck_Ass"
        elif Speed:
            "Rogue_Doggy_Anal_Head_Ass"
        else:
            "Rogue_Doggy_Ass"
    elif Player.Cock == 'in':
        if Speed > 2:
            "Rogue_Doggy_Fuck2_Ass"
        elif Speed > 1:
            "Rogue_Doggy_Fuck_Ass"
        else:
            "Rogue_Doggy_Ass"
    else:
        "Rogue_Doggy_Ass"
    if Player.Sprite and Player.Cock == 'foot':
        if Speed > 1:
            "Rogue_Doggy_Feet2"
        elif Speed:
            "Rogue_Doggy_Feet1"
        else:
            "Rogue_Doggy_Feet0"
    elif ShowFeet:
        "Rogue_Doggy_Shins0"
    align (0.6,0.0)
layeredimage Rogue_Doggy_Body:
    always:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Body.png"
    if not RogueX.Chest:
        Null()
    elif RogueX.Chest == 'tube top':
        Recolor("Rogue", "Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Tube.png")
    elif RogueX.Chest == 'tank':
        Recolor("Rogue", "Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png")
    elif RogueX.Chest == 'buttoned tank':
        Recolor("Rogue", "Chest", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png")
    elif RogueX.Chest == 'sports bra':
        Recolor("Rogue", "Chest", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png")
    elif RogueX.Chest == 'bikini top':
        Recolor("Rogue", "Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Bikini.png")
    elif RogueX.Chest == 'raven leotard':
        "images/RogueDoggy/modification/Rogue_Doggy_Chest_Raven.png"
    elif RogueX.Chest == 'SR7 tank top':
        "images/RogueDoggy/modification/Rogue_Doggy_Chest_SR7_tank_top.png"
    elif RogueX.Chest:
        Recolor("Rogue", "Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png")
    if not RogueX.Over:
        Null()
    elif RogueX.Over == 'mesh top':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png")
    elif RogueX.Over == 'pink top':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png")
    elif RogueX.Over == 'hoodie':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png")
    elif RogueX.Over == 'nighty':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png")
    elif RogueX.Over == 'towel':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_TowelTop.png")
    elif RogueX.Over == 'dress blue':
        "images/RogueDoggy/modification/Rogue_doggy_over_dress_blue_top.png"
    elif RogueX.Over == 'dress red':
        "images/RogueDoggy/modification/Rogue_doggy_over_dress_red_top.png"
    elif RogueX.Over == 'top harem':
        "images/RogueDoggy/modification/Rogue_doggy_over_harem_top.png"
    if RogueX.Neck == 'spiked collar':
        "images/RogueDoggy/Rogue_Doggy_Collar.png"
    if RogueX.Facing:
        "Rogue_Doggy_Head_Fore"
    else:
        "Rogue_Doggy_Head"
    if RogueX.Over == 'hoodie':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png")
    if not RogueX.Spunk or not Player.Male:
        Null()
    elif 'hair' in RogueX.Spunk:
        "images/RogueDoggy/Rogue_Doggy_Spunk_Hair.png"
    elif 'facial' in RogueX.Spunk:
        "images/RogueDoggy/Rogue_Doggy_Spunk_Facial.png"
    if Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts':
        "Rogue_Doggy_GropeBreast"
layeredimage Rogue_Doggy_Head:
    if RogueX.Water:
        Null()
    elif not Player.Male and ('hair' in RogueX.Spunk or 'facial' in RogueX.Spunk):
        Null()
    elif RogueX.Hair == 'evo':
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_HairB.png")
    always:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Head.png"
    if 'mouth' in RogueX.Spunk and Player.Male:
        if RogueX.Mouth == 'lipbite':
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_LipbiteW.png")
        elif RogueX.Mouth == 'surprised' or RogueX.Mouth == 'open':
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_SurprisedW.png")
        elif RogueX.Mouth == 'sucking':
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_BlowW.png")
        elif RogueX.Mouth == 'sad':
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_SadW.png")
        elif RogueX.Mouth == 'smile':
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_SmileW.png")
        elif RogueX.Mouth == 'tongue':
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_TongueW.png")
        else:
            Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_NormalW.png")
    elif RogueX.Mouth == 'normal':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Normal.png")
    elif RogueX.Mouth == 'lipbite':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Lipbite.png")
    elif RogueX.Mouth == 'sucking' or RogueX.Mouth == 'open':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Blow.png")
    elif RogueX.Mouth == 'kiss':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Surprised.png")
    elif RogueX.Mouth == 'sad':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Sad.png")
    elif RogueX.Mouth == 'smile':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Smile.png")
    elif RogueX.Mouth == 'grimace':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Smile.png")
    elif RogueX.Mouth == 'surprised':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Surprised.png")
    elif RogueX.Mouth == 'tongue':
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Tongue.png")
    else:
        Recolor("Rogue", "Lips", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Mouth_Smile.png")
    if RogueX.Blush:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Blush.png"
    if RogueX.Brows == 'normal':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Brows_Normal.png"
    elif RogueX.Brows == 'angry':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Brows_Angry.png"
    elif RogueX.Brows == 'sad':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Brows_Sad.png"
    elif RogueX.Brows == 'surprised':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Brows_Surprised.png"
    elif RogueX.Brows == 'confused':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Brows_Normal.png"
    else:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Brows_Normal.png"
    always:
        "Rogue Doggy Blink"
    if RogueX.Water:
        "images/RogueDoggy/Rogue_Doggy_WetTop.png"
    if RogueX.Hair == 'evo' and RogueX.HeadAcc == 'jewel':
        "images/RogueDoggy/modification/Rogue_Doggy_Face_Jewel.png"
    if RogueX.Water or RogueX.Hair == 'wet':
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_HairWet.png")
    elif not Player.Male and ('hair' in RogueX.Spunk or 'facial' in RogueX.Spunk):
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_HairWet.png")
    elif RogueX.Hair == 'cosplay':
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_Hair_Cos.png")
    else:
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_HairF.png")
    if RogueX.Hair != 'evo' and RogueX.HeadAcc == 'jewel':
        "images/RogueDoggy/modification/Rogue_Doggy_Face_Jewel.png"
    if RogueX.Over == 'hoodie':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png")
    if not RogueX.Spunk or not Player.Male:
        Null()
    elif 'hair' in RogueX.Spunk:
        "images/RogueDoggy/Rogue_Doggy_Spunk_Hair.png"
    elif 'facial' in RogueX.Spunk:
        "images/RogueDoggy/Rogue_Doggy_Spunk_Facial.png"
    if RogueX.Mask == 'mask harem':
        "images/RogueDoggy/modification/Rogue_doggy_mask_harem.png"
layeredimage Rogue_Doggy_Head_Fore:
    if RogueX.Water or RogueX.Hair == 'wet':
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_Hair_Wet_Fore.png")
    elif not Player.Male and ('hair' in RogueX.Spunk or 'facial' in RogueX.Spunk):
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_Hair_Wet_Fore.png")
    elif RogueX.Hair == 'cosplay':
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_Hair_Cos_Fore.png")
    else:
        Recolor("Rogue", "Hair", "images/RogueDoggy/Rogue_Doggy_Hair_Evo_Fore.png")
    if RogueX.Over == 'hoodie':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png")
layeredimage Rogue_Doggy_Ass:
    if not RogueX.PantiesDown or (RogueX.Legs == 'pants' and not RogueX.Upskirt):
        Null()
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png")
    elif RogueX.Panties == 'green panties':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Undies_Back.png")
    elif RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Back.png")
    elif RogueX.Panties == 'harness panties':
        "images/RogueDoggy/modification/Rogue_doggy_panties_harness_back.png"
    elif RogueX.Panties == 'raven leotard':
        Null()
    elif RogueX.Panties:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png")
    if Trigger == 'lick pussy':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Open.png"
    elif RogueX.Legs and not RogueX.Upskirt:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Closed.png"
    elif RogueX.Panties and not RogueX.PantiesDown:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Closed.png"
    elif Player.Sprite and Player.Cock == 'in':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Fucking.png"
    elif 'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand):
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Fucking.png"
    elif 'fondle pussy' in (Trigger,Trigger2,RogueX.Offhand) or (Partner and Partner.Offhand == 'girl fondle pussy'):
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Fucking.png"
    elif Trigger == 'insert pussy':
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Fucking.png"
    else:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Ass_Closed.png"
    if Player.Sprite and Player.Cock == 'anal':
        if Speed:
            "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullBase.png"
    elif 'insert ass' in (Trigger,Trigger2,RogueX.Offhand) or (Partner and Partner.Offhand == 'girl insert ass'):
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullBase.png"
    elif 'dildo anal' in (Trigger,Trigger2,RogueX.Offhand):
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullBase.png"
    elif RogueX.Loose > 2:
        "Rogue_Gape_Anal"
    elif RogueX.Loose:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Asshole_Loose.png"
    else:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Asshole_Tight.png"
    if RogueX.Red:
        "images/RogueDoggy/Rogue_Doggy_Red.png"
    if RogueX.Water:
        "images/RogueDoggy/Rogue_Doggy_WetAss.png"
    if RogueX.Hose == 'stockings':
        "images/RogueDoggy/Rogue_Doggy_Hose.png"
    if not RogueX.PantiesDown or (RogueX.Legs == 'pants' and not RogueX.Upskirt):
        Null()
    elif RogueX.Panties == 'shorts' and RogueX.Wet > 1:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png")
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png")
    elif RogueX.Panties == 'green panties' and RogueX.Wet > 1:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png")
    elif RogueX.Panties == 'green panties':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Undies_Down.png")
    elif RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Down.png")
    elif RogueX.Panties == 'harness panties' and RogueX.Wet > 1:
        "images/RogueDoggy/modification/Rogue_doggy_panties_harness_down_wet.png"
    elif RogueX.Panties == 'harness panties':
        "images/RogueDoggy/modification/Rogue_doggy_panties_harness_down.png"
    elif RogueX.Panties == 'raven leotard':
        Null()
    elif RogueX.Panties:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png")
    if not RogueX.Pubes:
        Null()
    elif Player.Sprite and Player.Cock == 'in':
        Null()
    elif 'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand):
        Null()
    elif 'fondle pussy' in (Trigger,Trigger2,RogueX.Offhand) or (Partner and Partner.Offhand == 'girl fondle pussy'):
        Null()
    elif Trigger == 'insert pussy':
        Null()
    elif RogueX.Legs == 'pants' and not RogueX.Upskirt:
        Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Panties.png")
    elif RogueX.PantiesDown:
        Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes.png")
    elif RogueX.Panties:
        Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Panties.png")
    elif RogueX.Hose and (RogueX.Hose == 'pantyhose' or RogueX.Hose == 'tights'):
        Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Panties.png")
    elif Trigger == 'lick pussy':
        Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Open.png")
    else:
        Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes.png")
    if Player.Sprite:
        Null()
    elif 'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand):
        Null()
    elif 'fondle pussy' in (Trigger,Trigger2,RogueX.Offhand) or (Partner and Partner.Offhand == 'girl fondle pussy'):
        Null()
    elif Trigger == 'insert pussy':
        Null()
    elif RogueX.Pierce == 'ring':
        "images/RogueDoggy/Rogue_Doggy_PussyRing.png"
    elif RogueX.Pierce == 'barbell':
        "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png"
    if RogueX.Plug:
        "images/PlugIn.png"
    if 'anal' not in RogueX.Spunk or Player.Sprite or not Player.Male:
        Null()
    elif RogueX.Loose:
        "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png" offset (2, -8)
    else:
        "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png" offset (2, -8)
    if RogueX.PantiesDown or not RogueX.Panties:
        Null()
    elif Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal'):
        Null()
    elif RogueX.Panties == 'shorts' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png")
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Shorts.png")
    elif RogueX.Panties == 'green panties' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png")
    elif RogueX.Panties == 'green panties':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Undies.png")
    elif RogueX.Panties == 'lace panties':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png")
    elif RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini.png")
    elif RogueX.Panties == 'harness panties' and RogueX.Wet:
        "images/RogueDoggy/modification/Rogue_doggy_panties_harness_wet.png"
    elif RogueX.Panties == 'harness panties':
        "images/RogueDoggy/modification/Rogue_doggy_panties_harness.png"
    elif RogueX.Panties == 'raven leotard':
        "images/RogueDoggy/modification/Rogue_Doggy_Panties_Raven.png"
    else:
        Recolor("Rogue", "Panties", "images/RogueDoggy/Rogue_Doggy_Panties.png")
    if RogueX.Hose == 'garterbelt':
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png")
    elif RogueX.Hose == 'stockings and garterbelt':
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Stockings.png")
    elif RogueX.Panties and RogueX.PantiesDown:
        Null()
    elif RogueX.Hose == 'tights' and RogueX.Wet:
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png")
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Tights.png")
    elif RogueX.Hose == 'pantyhose':
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_FullHose.png")
    elif RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png")
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png")
    if RogueX.Legs == 'pants':
        if RogueX.Upskirt:
            Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png")
        elif RogueX.Wet > 1:
            Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png")
        else:
            Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png")
    elif RogueX.Legs == 'skirt':
        if RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed:
            Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png")
        elif RogueX.Upskirt:
            Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png")
        else:
            Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png")
    elif RogueX.Legs == 'SR7 skirt':
        if RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed:
            "images/RogueDoggy/modification/Rogue_Doggy_Legs_SR7_Skirt_UpAnal.png"
        elif RogueX.Upskirt:
            "images/RogueDoggy/modification/Rogue_Doggy_Legs_SR7_Skirt_Up.png"
        else:
            "images/RogueDoggy/modification/Rogue_Doggy_Legs_SR7_Skirt.png"
    elif RogueX.Legs == 'short skirt':
        if RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed:
            "images/RogueDoggy/modification/Rogue_Doggy_Legs_Short_Skirt_UpAnal.png"
        elif RogueX.Upskirt:
            "images/RogueDoggy/modification/Rogue_Doggy_Legs_Short_Skirt_Up.png"
        else:
            "images/RogueDoggy/modification/Rogue_Doggy_Legs_Short_Skirt.png"
    elif RogueX.Legs == 'bottom harem':
        if RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed:
            "images/RogueDoggy/modification/Rogue_doggy_skirt_harem_bottom_ass_anal_up.png"
        elif RogueX.Upskirt:
            "images/RogueDoggy/modification/Rogue_doggy_skirt_harem_bottom_ass_up.png"
        else:
            "images/RogueDoggy/modification/Rogue_doggy_skirt_harem_bottom_ass.png"
    if RogueX.Over == 'nighty' and RogueX.Upskirt:
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png")
    elif RogueX.Over == 'nighty' and (Player.Cock == 'in' or Player.Cock == 'out'):
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png")
    elif RogueX.Over == 'nighty':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png")
    elif RogueX.Over == 'towel' and RogueX.Upskirt:
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png")
    elif RogueX.Over == 'towel' and (Player.Cock == 'in' or Player.Cock == 'out'):
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png")
    elif RogueX.Over == 'towel':
        Recolor("Rogue", "Over", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss.png")
    elif RogueX.Over == 'dress blue':
        if RogueX.Upskirt and Player.Cock == 'anal':
            "images/RogueDoggy/modification/Rogue_doggy_over_dress_blue_ass_anal_up.png"
        elif Player.Cock == 'in' or Player.Cock == 'out':
            "images/RogueDoggy/modification/Rogue_doggy_over_dress_blue_ass_up.png"
        else:
            "images/RogueDoggy/modification/Rogue_doggy_over_dress_blue_ass.png"
    elif RogueX.Over == 'dress red':
        if RogueX.Upskirt and Player.Cock == 'anal' and Speed:
            "images/RogueDoggy/modification/Rogue_doggy_over_dress_red_ass_anal_up.png"
        elif Player.Cock == 'in' or Player.Cock == 'out':
            "images/RogueDoggy/modification/Rogue_doggy_over_dress_red_ass_up.png"
        else:
            "images/RogueDoggy/modification/Rogue_doggy_over_dress_red_ass.png"
    if RogueX.Acc == 'sweater' and (RogueX.Upskirt or (Player.Sprite and Player.Cock == 'out')):
        "images/RogueDoggy/Rogue_Doggy_Acc_Sweater_Up.png"
    elif RogueX.Acc == 'sweater':
        "images/RogueDoggy/Rogue_Doggy_Acc_Sweater.png"
    if 'back' in RogueX.Spunk and Player.Male:
        "images/RogueDoggy/Rogue_Doggy_SpunkAss.png"
    if RogueX.Legs and not RogueX.Upskirt:
        Null()
    elif RogueX.Panties and not RogueX.PantiesDown:
        Null()
    elif Player.Sprite and Player.Cock == 'in':
        if Speed > 2:
            "Rogue_Pussy_Fucking3"
        elif Speed > 1:
            "Rogue_Pussy_Fucking2"
        elif Speed:
            "Rogue_Pussy_Heading"
        else:
            "Rogue_Pussy_Static"
    elif 'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand):
        "Rogue_Pussy_Fucking2"
    elif 'fondle pussy' in (Trigger,Trigger2,RogueX.Offhand) or (Partner and Partner.Offhand == 'girl fondle pussy'):
        "Rogue_Pussy_Fingering"
    elif Trigger == 'insert pussy':
        "Rogue_Pussy_Fingering"
    if RogueX.Legs and not RogueX.Upskirt:
        Null()
    elif RogueX.Panties and not RogueX.PantiesDown:
        Null()
    elif Player.Sprite and Player.Cock == 'anal':
        if Speed > 2:
            "Rogue_Anal_Fucking2"
        elif Speed > 1:
            "Rogue_Anal_Fucking"
        elif Speed:
            "Rogue_Anal_Heading"
        else:
            "Rogue_Anal"
    elif 'dildo anal' in (Trigger,Trigger2,RogueX.Offhand):
        "Rogue_Anal_Fucking"
    elif 'insert ass' in (Trigger,Trigger2,RogueX.Offhand) or (Partner and Partner.Offhand == 'girl insert ass'):
        "Rogue_Anal_Fingering"
    elif RogueX.Plug:
        "images/PlugIn.png"
    if Player.Sprite and Player.Cock:
        Null()
    elif Trigger == 'lick pussy':
        "Rogue_Doggy_Lick_Pussy"
    elif Trigger == 'lick ass':
        "Rogue_Doggy_Lick_Ass"
    if not Player.Sprite or Player.Cock != 'out':
        Null()
    elif RogueX.Legs == 'skirt' and RogueX.Upskirt:
        "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png"
    else:
        "images/RogueDoggy/Rogue_Doggy_HotdogBack.png"
    if not Player.Sprite or Player.Cock != 'out':
        Null()
    elif RogueX.Legs == 'skirt' and RogueX.Upskirt and Speed:
        AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png")
    elif RogueX.Legs == 'skirt' and RogueX.Upskirt:
        AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png")
    elif Speed:
        AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png")
    else:
        AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png")
image Rogue Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(
    "RogueX.Eyes == 'sexy'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Sexy.png",
    "RogueX.Eyes == 'side'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Side.png",
    "RogueX.Eyes == 'normal'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Normal.png",
    "RogueX.Eyes == 'closed'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Closed.png",
    "RogueX.Eyes == 'manic'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Surprised.png",
    "RogueX.Eyes == 'down'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Sexy.png",
    "RogueX.Eyes == 'stunned'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Stunned.png",
    "RogueX.Eyes == 'surprised'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Surprised.png",
    "RogueX.Eyes == 'squint'", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Sexy.png",
    "True", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Normal.png",
    ),
#    choice:
#        3.5
#    choice:
#        3.25
#    choice:
#        3
    3
    # This randomizes the time between blinking.
    "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Eyes_Closed.png"
    .25
    repeat
image Rogue_Doggy_Feet:
    contains:
            AlphaMask("Rogue_Doggy_Shins", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Toes.png")
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
image Rogue_Doggy_Shins:
    #Rogue's footjob shins
    contains:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Shins.png"
    contains:
        #pants
        ConditionSwitch(
            "RogueX.Legs == 'pants'", Recolor("Rogue", "Legs", "images/RogueDoggy/Rogue_Doggy_Feet_Pants.png"),
            "True", Null(),
            )
    contains:
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Feet.png"
    contains:
            #hose
        ConditionSwitch(
            "not RogueX.Hose", Null(),
            "RogueX.Hose == 'stockings'", Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png"),
            "RogueX.Hose == 'stockings and garterbelt'", Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png"),
            "RogueX.Hose == 'tights'", Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Feet_Tights.png"),
            "RogueX.Hose == 'pantyhose'", Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png"),
            "RogueX.Hose == 'ripped pantyhose'", Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Feet_Hose_Holed.png"),
            "RogueX.Hose == 'ripped tights'", Recolor("Rogue", "Hose", "images/RogueDoggy/Rogue_Doggy_Feet_Tights_Holed.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
#    pos (0,0)
image Rogue_Doggy_Shins0:
        #static animation
        "Rogue_Doggy_Shins"
        offset (0, 50) #(0,0) top
image Rogue_Doggy_Lick_Pussy:
        "Lick_Anim"
        zoom 0.5
        offset (195,540)
image Rogue_Doggy_Lick_Ass:
        "Lick_Anim"
        zoom 0.5
        offset (195,500)
image Rogue_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (150,340)#(100,200)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat
image Rogue_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_GapeBase.png"
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
image Zero_Doggy_Up:
    #Cock when out (hotdog)
    contains:
        ConditionSwitch(
            "not Player.Male", "images/RogueDoggy/Rogue_Doggy_Cock_U_D.png",
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png",
            )
    contains:
        ConditionSwitch(
            "Player.Spunk and Player.Male", "images/RogueDoggy/Rogue_Doggy_Cock_U_Spunk.png",
            "Player.Wet or Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null(),
            )
image Zero_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        alpha 0.8
        pos (175, 370)
image Zero_Hotdog_Moving:
    # The moving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        alpha 0.8
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Insert cock animations
image Zero_Doggy_Insert:
    #Insert cock
    contains:
        ConditionSwitch(
            "not Player.Male", "images/RogueDoggy/Rogue_Doggy_Cock_In_D.png",
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png",
            )
        alpha 0.5
    contains:
        ConditionSwitch(
            "Player.Spunk and Player.Male", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",
            "Player.Wet or Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",
            "True", Null(),
            )
        alpha 0.5
    contains:
        ConditionSwitch(
            "not AlphaCock", Null(),
            "not Player.Male", "images/RogueDoggy/Rogue_Doggy_Cock_In_D.png",
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png",
            )
    contains:
        ConditionSwitch(
            "not AlphaCock", Null(),
            "Player.Spunk and Player.Male", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",
            "Player.Wet or Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",
            "True", Null(),
            )
image Zero_Doggy_Static:
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
image Zero_Doggy_Heading:
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
image Zero_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat
image Zero_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat
image Rogue_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Rogue_Pussy_Moving"
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
image Rogue_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Rogue_Pussy_Moving"
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
image Rogue_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "RogueX.Pubes", Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (215,518) #(213,518)
        xzoom .8
        block:
            ease 1 xzoom .85
            pause 1
            ease 3 xzoom .8
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (218,516) #(221,516)
        xzoom .7
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .7
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Static", "Rogue_Pussy_Mask_Static")
    contains:
        # expanding pussy flap
        AlphaMask("Rogue_PussyHole_Static", "Rogue_Pussy_Hole_Mask_Static")
image Rogue_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
image Rogue_PussyHole_Static:
    #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Moving"
    contains:
        #Mask
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat
image Rogue_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "RogueX.Pubes", Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (215,518) #(213,518)
        xzoom .75#.75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .75
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Doggy_Heading", "Rogue_Pussy_Mask")
    contains:
        # expanding pussy flap
        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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
image Rogue_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
image Rogue_Pussy_Heading_Flap:
    #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Heading"
    contains:
        #Mask
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat
image Rogue_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png"
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
            "RogueX.Pubes", Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (215,518) #(213,518)
        xzoom .75#.75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .75
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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
image Zero_Pussy_Finger:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (171,545)
        alpha 0.8
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >
image Rogue_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "RogueX.Pubes", Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
image Rogue_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "RogueX.Pubes", Recolor("Rogue", "Pubes", "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Pussy_Wet.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in RogueX.Spunk and not Player.Male", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "'in' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
image Doggy_Fucking_Dildo:
    #Animation for speed 2 Cock
    contains:
        "images/DildoIn.png"
        pos (169,500)
        alpha 0.8
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal_Fingering:
    #Animation for speed 1
#    contains:
#        #Base
#        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75#1
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Rogue_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .6 #.5
            repeat
image Zero_Rogue_Doggy_Anal_Finger:
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
image Rogue_Doggy_Anal_Fingering_Mask:
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,515)
        zoom 1.25
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            "True", Null(),
            )
        yoffset -15
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Heading", "Rogue_Doggy_Anal_Heading_Mask")

    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Doggy_Anal_Heading", "Rogue_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .6 #.5
            repeat
image Zero_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat
image Zero_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat
image Rogue_Doggy_Anal_Heading_Mask:
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
image Rogue_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat
image Rogue_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat
image Rogue_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullHole.png"
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,RogueX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
image Rogue_Doggy_Anal_Dildo:
    #Animation for speed 2 Cock
    contains:
        "images/DildoIn.png"
        pos (172,460)
        alpha 0.8
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat
image Rogue_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat
image Rogue_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat
image Rogue_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/RogueDoggy/[RogueX.skin_image.skin_path]Rogue_Doggy_Anal_FullHole.png"
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in RogueX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
image Rogue_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat
image Rogue_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
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
image Rogue_Doggy_Feet0:
    #static animation
    contains:
        "Rogue_Doggy_Shins"
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
        pos (145,480)
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat
image Rogue_Doggy_Feet1:
    #slow animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
image Rogue_Doggy_Feet2:
    #fast animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             UI Tool animations
label Slap_Anim(Girl=ch_focus,Plug_Mod=[0,0]):
        if Girl is LauraX:
            $ Plug_Mod[0] = 100
        show Slap_Ass zorder 151
        pause 0.2
        call Punch
        pause .7
        hide Slap_Ass
        return

image Slap_Ass:
    contains:
        "UI_Hand"
        subpixel True
        zoom 1
        alpha 0.5
        anchor (0.5,0.5)
        transform_anchor True
        rotate 40
        offset (200,-100)
        parallel:
            ease .2 xoffset 0 rotate 80
            ease .1 xoffset 40
            ease .5 alpha 0
        parallel:
            ease .2 yoffset 0
    pos (1150+Plug_Mod[0],1350+Plug_Mod[1])


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Rogue_Doggy_Launch(Line = Trigger):
    if renpy.showing("Rogue_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(RogueX,1) #call Rogue_Hide(1)
    show Rogue_Doggy_Animation at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return

label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ RogueX.ArmPose = 2
    $ RogueX.SpriteVer = 0
    hide Rogue_Doggy_Animation
    call Girl_Hide(RogueX) #call Rogue_Hide
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return





# Rogue Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


layeredimage Rogue_SexSprite:
    if not Player.Sprite:
        "Rogue_Sex_Body_Static"
    elif Player.Cock == 'anal':
        if Speed >= 3:
            "Rogue_Sex_Body_Anim3"
        elif Speed >= 2:
            "Rogue_Sex_Body_Anim2"
        elif Speed:
            "Rogue_Sex_Body_Anim1"
        else:
            "Rogue_Sex_Body_Static"
    elif Player.Cock == 'in':
        if Speed >= 3:
            "Rogue_Sex_Body_Anim3"
        elif Speed >= 2:
            "Rogue_Sex_Body_Anim2"
        elif Speed:
            "Rogue_Sex_Body_Anim1"
        else:
            "Rogue_Sex_Body_Static"
    elif Player.Cock == 'foot':
        if Speed >= 2:
            "Rogue_Sex_Body_FootAnim2"
        elif Speed:
            "Rogue_Sex_Body_FootAnim1"
        else:
            "Rogue_Sex_Body_FootAnimStatic"
    elif Player.Cock == 'out' and Speed >= 2:
        "Rogue_Hotdog_Body_Anim2"
    else:
        "Rogue_Sex_Body_Static"
    if not Player.Sprite:
        "Rogue_Sex_Legs_Static"
    elif Player.Cock == 'anal':
        if Speed >= 3:
            "Rogue_Sex_Legs_Anim3"
        elif Speed >= 2:
            "Rogue_Sex_Legs_Anim2"
        elif Speed:
            "Rogue_Sex_Legs_Anim1"
        else:
            "Rogue_Sex_Legs_Static"
    elif Player.Cock == 'in':
        if Speed >= 3:
            "Rogue_Sex_Legs_Anim3"
        elif Speed >= 2:
            "Rogue_Sex_Legs_Anim2"
        elif Speed:
            "Rogue_Sex_Legs_Anim1"
        else:
            "Rogue_Sex_Legs_Static"
    elif Player.Cock == 'foot':
        if Speed >= 2:
            "Rogue_Sex_Legs_FootAnim2"
        elif Speed:
            "Rogue_Sex_Legs_FootAnim1"
        else:
            "Rogue_Sex_Legs_FootAnimStatic"
    elif Player.Cock == 'out' and Speed >= 2:
        "Rogue_Hotdog_Legs_Anim2"
    else:
        "Rogue_Sex_Legs_Static"
    align (0.6,0.0)
    pos (650,200)#(650,230)
    zoom 0.85#0.8
image Rogue_Sex_Body_Static:
    contains:
            "Rogue_Sex_Body"
    pos (650,230)
image Rogue_Sex_Legs_Static:
    contains:
            "Rogue_Sex_Legs"
    pos (650,230)

#image Rogue_Sex_Body = LiveComposite(
layeredimage Rogue_Sex_Body:
    if RogueX.Over == 'cape':
        "images/RogueSex/modification/Rogue_sex_over_cape_under.png"
    always:
        "Rogue_HairBack_Sex" offset (320, -135)
    if RogueX.Pierce == 'barbell':
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Body_Barbell.png"
    elif RogueX.Pierce == 'ring':
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Body_Ring.png"
    else:
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Body.png"
    if not RogueX.Chest:
        Null()
    elif RogueX.Uptop:
        if RogueX.Chest == 'tank':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Tank_Up.png")
        elif RogueX.Chest == 'tube top':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Tube_Up.png")
        elif RogueX.Chest == 'buttoned tank':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_ButtonTank_Up.png")
        elif RogueX.Chest == 'sports bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_SportsBra_Up.png")
        elif RogueX.Chest == 'bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Bra_Up.png")
        elif RogueX.Chest == 'bikini top':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Bikini_Up.png")
        elif RogueX.Chest == 'lace bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Bra_Up.png")
        elif RogueX.Chest == 'SR7 tank top':
            "images/RogueSex/modification/Rogue_Sex_Chest_SR7_tank_top_Up.png"
        elif RogueX.Chest == 'harness bra':
            "images/RogueSex/modification/Rogue_sex_chest_harness_bra_up.png"
    else:
        if RogueX.Chest == 'tank':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Tank.png")
        elif RogueX.Chest == 'tube top':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Tube.png")
        elif RogueX.Chest == 'buttoned tank':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_ButtonTank.png")
        elif RogueX.Chest == 'sports bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_SportsBra.png")
        elif RogueX.Chest == 'bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Bra.png")
        elif RogueX.Chest == 'bikini top':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_Bikini.png")
        elif RogueX.Chest == 'lace bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_Sex_Chest_LaceBra.png")
        elif RogueX.Chest == 'SR7 tank top':
            "images/RogueSex/modification/Rogue_Sex_Chest_SR7_tank_top.png"
        elif RogueX.Chest == 'raven leotard':
            "images/RogueSex/modification/Rogue_sex_chest_raven.png"
        elif RogueX.Chest == 'harness bra':
            "images/RogueSex/modification/Rogue_sex_chest_harness_bra.png"
    if RogueX.Water:
        "images/RogueSex/Rogue_Sex_Wet_Body.png"
    if not RogueX.Over:
        Null()
    elif RogueX.Uptop:
        if RogueX.Over == 'pink top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Pink_Up.png")
        elif RogueX.Over == 'mesh top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Mesh_Up.png")
        elif RogueX.Over == 'hoodie':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Hoodie_Up.png")
        elif RogueX.Over == 'nighty':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Nighty_Up.png")
        elif RogueX.Over == 'towel':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Towel_Up.png")
        elif RogueX.Over == 'cape':
            "images/RogueSex/modification/Rogue_sex_over_cape.png"
        elif RogueX.Over == 'top harem':
            "images/RogueSex/modification/Rogue_sex_over_harem_top_up.png"
    else:
        if RogueX.Over == 'pink top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Pink.png")
        elif RogueX.Over == 'mesh top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Mesh.png")
        elif RogueX.Over == 'hoodie':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Hoodie.png")
        elif RogueX.Over == 'nighty':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Nighty.png")
        elif RogueX.Over == 'towel':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_Sex_Over_Towel.png")
        elif RogueX.Over == 'cape':
            "images/RogueSex/modification/Rogue_sex_over_cape.png"
        elif RogueX.Over == 'dress blue':
            "images/RogueSex/modification/Rogue_sex_over_dress_blue.png"
        elif RogueX.Over == 'dress red':
            "images/RogueSex/modification/Rogue_sex_over_dress_red.png"
        elif RogueX.Over == 'top harem':
            "images/RogueSex/modification/Rogue_sex_over_harem_top.png"
    if RogueX.Uptop or (not RogueX.Over and not RogueX.Chest):
        Null()
    elif RogueX.Pierce == 'barbell':
        "images/RogueSex/Rogue_Sex_Pierce_BarbellC.png"
    elif RogueX.Pierce == 'ring':
        "images/RogueSex/Rogue_Sex_Pierce_RingC.png"
    if RogueX.Neck == 'spiked collar':
        "images/RogueSex/Rogue_Sex_Neck_Stud.png"
    if 'belly' in RogueX.Spunk and Player.Male:
        "images/KittySex/Kitty_Sex_Spunk_Body.png"
    if 'tits' in RogueX.Spunk and Player.Male:
        "images/KittySex/Kitty_Sex_Spunk_Tits.png" offset (0, 80)
    if Trigger == 'suck breasts' or Trigger2 == 'suck breasts':
        "Rogue_Sex_Lick_Breasts"
    if Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts':
        "Rogue_Sex_Fondle_Breasts"
    always:
        "Rogue_Head_Sex" offset (320, -135)
    zoom 0.9
    offset (50,50)
image Rogue_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.6
        offset (450,270)
image Rogue_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.1
        offset (320,-130)
image Rogue_Head_Sex:
    # The head used for the sex pose, referenced by Rogue_Sex_Body
    "Rogue_Head"#"Rogue_Head"
    zoom 1.28 #0.37
    anchor (0.5,0.5)
    rotate -10
image Rogue_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Rogue_Sex_Body
    "Rogue_HairBack"
    zoom 1.28 # 0.37
    anchor (0.5,0.5)
    rotate -10


#image Rogue_Sex_Legs = LiveComposite(
layeredimage Rogue_Sex_Legs:
    always:
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Legs.png"
    if RogueX.Water:
        "images/RogueSex/Rogue_Sex_Wet_Legs.png"
    always:
        "Rogue_Sex_Anus"
    always:
        "Rogue_Sex_Pussy"
    if not RogueX.Panties or RogueX.PantiesDown:
        Null()
    elif Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal'):
        Null()
    elif RogueX.Panties == 'lace panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Lace.png")
    elif RogueX.Panties == 'green panties' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Green_Wet.png")
    elif RogueX.Panties == 'green panties' or RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Green.png")
    elif RogueX.Panties == 'shorts' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Shorts_Wet.png")
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Shorts.png")
    elif RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Black_Wet.png")
    elif RogueX.Panties == 'harness panties' and RogueX.Wet:
        "images/RogueSex/modification/Rogue_sex_panties_harness_wet.png"
    elif RogueX.Panties == 'harness panties':
        "images/RogueSex/modification/Rogue_sex_panties_harness.png"
    elif RogueX.Panties == 'raven leotard' and RogueX.Wet:
        "images/RogueSex/modification/Rogue_sex_panties_raven_wet.png"
    elif RogueX.Panties == 'raven leotard':
        "images/RogueSex/modification/Rogue_sex_panties_raven.png"
    else:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Black.png")
    if RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Full_Hole.png")
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Hole.png")
    elif RogueX.Hose == 'stockings':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Stockings.png")
    elif RogueX.Hose == 'stockings and garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_StockingGarter.png")
    elif RogueX.Hose == 'garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Garter.png")
    elif RogueX.PantiesDown:
        Null()
    elif Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal'):
        Null()
    elif RogueX.Hose == 'pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Full.png")
    elif RogueX.Hose == 'tights' and RogueX.Wet:
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Wet.png")
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights.png")
    if RogueX.Legs == 'skirt':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Skirt.png")
    elif RogueX.Upskirt:
        Null()
    elif RogueX.Legs == 'pants' and RogueX.Wet > 1:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Pants_Wet.png")
    elif RogueX.Legs == 'pants':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Pants.png")
    elif RogueX.Legs == 'SR7 skirt':
        "images/RogueSex/modification/Rogue_Sex_Legs_SR7_Skirt.png"
    elif RogueX.Legs == 'short skirt':
        "images/RogueSex/modification/Rogue_Sex_Legs_Short_Skirt.png"
    elif RogueX.Legs == 'bottom harem' and RogueX.Wet > 1:
        "images/RogueSex/modification/Rogue_sex_skirt_harem_bottom_wet.png"
    elif RogueX.Legs == 'bottom harem':
        "images/RogueSex/modification/Rogue_sex_skirt_harem_bottom.png"
    if RogueX.Acc == 'sweater':
        "images/RogueSex/Rogue_Sex_Sweater.png"
    if 'belly' in RogueX.Spunk and Player.Male:
        "images/KittySex/Kitty_Sex_Spunk_Pelvis.png"
    if not Player.Sprite or Player.Cock != 'out':
        Null()
    elif Speed >= 2:
        "Rogue_Hotdog_Zero_Anim2"
    elif Speed:
        "Rogue_Hotdog_Zero_Anim1"
    else:
        "Rogue_Hotdog_Zero_Anim0"
    if Player.Sprite:
        Null()
    elif Trigger == 'lick pussy':
        "Rogue_Sex_Lick_Pussy"
    elif Trigger == 'lick ass':
        "Rogue_Sex_Lick_Ass"
    elif RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60:
        At("RogueFingerHand", GirlFingerPussyX())
    elif RogueX.Offhand == 'fondle pussy':
        At("RogueMastHand", GirlGropePussyX())
    if not Player.Sprite or Player.Cock != 'foot':
        Null()
    elif Speed >= 2:
        "Rogue_Footcock_Zero_Anim2"
    elif Speed:
        "Rogue_Footcock_Zero_Anim1"
    else:
        "Rogue_Footcock_Static"
    if not Speed or Player.Cock == 'foot' or ShowFeet:
        "Rogue_Sex_Feet"
    else:
        AlphaMask("Rogue_Sex_Feet","images/RogueSex/Rogue_Sex_FeetMask2.png")
layeredimage Rogue_Sex_Feet:
    always:
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Feet.png"
    if RogueX.Water:
        "images/RogueSex/Rogue_Sex_Wet_Feet.png"
    if not RogueX.Panties or not RogueX.PantiesDown:
        Null()
    elif RogueX.Legs == 'pants':
        Null()
    elif RogueX.Panties == 'lace panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Lace_Down.png")
    elif RogueX.Panties == 'green panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Green_Down.png")
    elif RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Bikini_Down.png")
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Shorts_Down.png")
    elif RogueX.Panties == 'harness panties':
        "images/RogueSex/modification/Rogue_sex_panties_harness_down.png"
    elif RogueX.Panties == 'raven leotard':
        Null()
    else:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Black_Down.png")
    if not RogueX.Hose:
        Null()
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Feet_Tights_Hole.png")
    elif RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking_Hole.png")
    elif RogueX.Hose == 'stockings and garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png")
    elif RogueX.Hose == 'stockings':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png")
    elif RogueX.PantiesDown:
        Null()
    elif Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal'):
        Null()
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Feet_Tights.png")
    elif RogueX.Hose == 'garterbelt':
        Null()
    else:
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png")
    if RogueX.Legs == 'pants' and RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Pants_Down.png")
    elif RogueX.Legs == 'pants':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Pants_Feet.png")
    elif RogueX.Legs == 'bottom harem' and RogueX.Upskirt:
        "images/RogueSex/modification/Rogue_sex_skirt_harem_bottom_down.png"
    elif RogueX.Legs == 'bottom harem':
        "images/RogueSex/modification/Rogue_sex_skirt_harem_bottom_feet.png"
    if 'feet' in RogueX.Spunk:
        "images/RogueSex/Rogue_Sex_Spunk_Feet.png"
image Rogue_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (530,510)
image Rogue_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,590)
image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat
image Rogue_Sex_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask")
image Rogue_Sex_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask")
image Rogue_Sex_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask")
image Rogue_Sex_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask")
image Rogue_Pussy_Fucking_Mask:
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Pussy_Mask.png"
image Rogue_Pussy_Open_Mask:
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Pussy_Mask.png"
            yoffset 3
image Rogue_Sex_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
image Rogue_Sex_Pussy_Hole:
    "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
    transform_anchor True
    anchor (212,580)#(210,600)
    pos (558,580)#(400,-10)
    xzoom 0.8
    parallel:
        ease 1 yzoom 1.2
        pause 1
        ease 3 yzoom 1
        repeat
    parallel:
        ease 1 xzoom 1.2
        pause 2
        ease 2  xzoom 0.8
        repeat
image Rogue_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Closed.png",
                "'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand)", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
#                "Trigger == 'dildo pussy'", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "True", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Closed.png",
                )
    contains:
            # growing pussy hole
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Rogue_Sex_Pussy_Hole",#"images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "True", Null(),
                )
    contains:
            # wet pussy
            ConditionSwitch(
                "not RogueX.Wet", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "RogueX.Pierce != 'ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                )
    contains:
            #barbell piercing
            ConditionSwitch(
                "RogueX.Pierce != 'barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
                "Player.Sprite and Player.Cock == 'in'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Closed.png"),
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
                "'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand)", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                "RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
#                "Trigger == 'dildo pussy'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Closed.png"),
                )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'in' in RogueX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed", AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask"),
                "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", AlphaMask("Rogue_Sex_FingerP_Anim1", "Rogue_Pussy_Open_Mask"),
                "'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand)", AlphaMask("Rogue_Sex_Dildo_Anim2", "Rogue_Pussy_Fucking_Mask"),
#                "Trigger == 'dildo pussy'", AlphaMask("Rogue_Sex_Dildo_Anim2", "Rogue_Pussy_Fucking_Mask"),
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'in' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
                "Speed <= 1", "Rogue_Sex_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )

    #End Rogue Pussy composite

#End Animations for Rogue's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_FingerP_Anim1:
        #this is Rogue's fingering animation
        contains:
            subpixel True
            "images/UI_Fingering.png"
            pos (507,520) #X less is left, Y less is up(498,525)
            zoom 1.2#1.3
            block:
                ease .2 ypos 480 #(498,500)
                pause .2
                ease .6 ypos 520
                repeat
image Rogue_Sex_Dildo_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "images/DildoIn.png"
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease 1 ypos 380 #(500,470)
                pause 1
                ease 3 ypos 490
                repeat

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,530) #X less is left, Y less is up (498,530)
            zoom 1.3#1.4
image Rogue_Sex_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,525) #X less is left, Y less is up(498,525)
            zoom 1.3#1.4
            block:
                ease 1 ypos 510 #(498,500)
                pause 1
                ease 3 ypos 525
                repeat
image Rogue_Sex_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease 1 ypos 380 #(500,470)
                pause 1
                ease 3 ypos 490
                repeat
image Rogue_Sex_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease .25 ypos 380 #(500,470)
                pause .25
                ease 1.5 ypos 490
                repeat
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Legs_Anim1:
        #this is the animation for Rogue's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat
image Rogue_Sex_Legs_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat
image Rogue_Sex_Legs_Anim3:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,0)
                repeat
#End Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Body_Anim1:
        #this is the animation for Rogue's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat
image Rogue_Sex_Body_Anim2:
        #this is the animation for Rogue's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat
image Rogue_Sex_Body_Anim3:
        #this is the animation for Rogue's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,10)
                repeat
#End Animations for Rogue's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





#Start Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Rogue_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Rogue_Sex_Anal_Tip",
            "Trigger == 'insert ass' or Trigger2 == 'insert ass'", "Rogue_Sex_Anal_Tip",
            "Trigger == 'dildo anal'", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "RogueX.Plug", "images/PlugBase_Sex.png",
            "RogueX.Loose > 2", "Rogue_Gape_Anal_Sex",
            "RogueX.Loose", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Hole_Loose.png",
            "True", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Hole_Tight.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in RogueX.Spunk or not Player.Male", Null(),
                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Rogue_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
            "Trigger == 'insert ass' or Trigger2 == 'insert ass'", AlphaMask("Rogue_Sex_FingerA_Anim1", "Rogue_Anal_Fucking_Mask"),
            "Trigger == 'dildo anal'", AlphaMask("Rogue_Anal_Dildo_Anim2", "Rogue_Anal_Fucking_Mask"),
            "not Player.Sprite or Player.Cock != 'anal'", Null(),
            "Speed >= 3",  AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Anal_Fucking_Mask"),
            "Speed >= 2", AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask"),
            "True", AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask"),
            )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Rogue_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )
image Rogue_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/KittySex/Kitty_Sex_Hole_Open.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,615)#(218,518)
            zoom .40 # tight
            block:
                ease 3 zoom .50 #in.87
                ease 3 zoom .40 #out
                repeat
image Rogue_Sex_FingerA_Anim1:
        #this is Rogue's fingering animation
        contains:
            subpixel True
            "images/UI_Fingering.png"
            pos (507,600) #X less is left, Y less is up(498,525)
            zoom 1.2#1.3
            block:
                ease .4 ypos 550 #480
                pause .4
                ease 1.2 ypos 600#520
                repeat
image Rogue_Anal_Dildo_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "images/DildoIn.png"
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 450 #(500,470)
                pause 1
                ease 3 ypos 570
                repeat
image Rogue_Sex_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask")
image Rogue_Sex_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Heading"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask")
image Rogue_Sex_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask")
image Rogue_Sex_Anal_Fucking3:
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask")
image Rogue_Anal_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 1#0
image Rogue_Anal_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 3#3
image Rogue_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.9
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat
image Rogue_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:
        #total 5 second
        ease .75 xzoom 1.0   #(1.0)
        pause 1.75
        ease .25 xzoom 1.0  #(1.0)
        ease 2.25 xzoom 0.8   #(0.6)
        repeat
image Rogue_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat
image Rogue_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6

#End Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Anal_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,600) #X less is left, Y less is up (498,520)
            zoom 1.3
image Rogue_Anal_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,600) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 570 #(500,470)
                pause 1
                ease 3 ypos 600
                repeat
image Rogue_Anal_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 450 #(500,470)
                pause 1
                ease 3 ypos 570
                repeat
image Rogue_Anal_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease .25 ypos 450 #(500,470)
                pause .25
                ease 1.5 ypos 570
                repeat
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Hotdog_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,570) #X less is left, Y less is up
            zoom 1.3
image Rogue_Hotdog_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,500) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 560 #(500,500)
                pause .5
                ease 1.5 ypos 500
                repeat
image Rogue_Hotdog_Zero_Anim2:
        #this is Rogue's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,510) #X less is left, Y less is up
            zoom 1.3
            block:
                ease .5 ypos 400 #(500,470)
                pause .5
                ease 1 ypos 510
                repeat
image Rogue_Hotdog_Body_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat
image Rogue_Hotdog_Legs_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat

#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Footcock:
    contains:
            subpixel True
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
#            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)
image Rogue_Footcock_Static:
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
    #pos (750,230)
    offset (0,-100)
image Rogue_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 ypos 360#65
                ease .25 ypos 355#60
                pause 1
                ease 2.50 ypos 270#285
                repeat
    offset (0,-100)
image Rogue_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 ypos 360
                ease .2 ypos 355
                pause .2
                ease 1.00 ypos 270
                repeat
    offset (0,-100)

#transform Rogue_Footcock_Zero_Anim1A():
#            subpixel True
#            offset (0,0)
#            block:
#                #Total time, 4 seconds
#                pause .5
#                easein .75 yoffset 60#65
#                ease .25 yoffset 55#60
#                pause 1
#                ease 1.50 yoffset -30#285
#                repeat

#transform Rogue_Footcock_Zero_Anim2A():
#            subpixel True
#            offset (0,0)
#            block:
#                #Total time, 2 seconds
#                pause .2
#                easein .4 yoffset 60
#                ease .2 yoffset 55
#                pause .2
#                ease 1.00 yoffset -30
#                pause .2
#                easein .4 yoffset 60
#                ease .2 yoffset 55
#                pause .2
#                ease 1.00 yoffset -30
#                repeat

#transform Rogue_Footcock_StaticA():
#            subpixel True
#            offset (0,-5)
#            block:
#                #Total time, 4 seconds
#                pause .5
#                ease 1 yoffset 0
#                pause 1
#                ease 1.50 yoffset -5
#                repeat
image Rogue_Sex_Legs_FootAnimStatic:
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        offset (0,100)
image Rogue_Sex_Legs_FootAnim1:
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-65)
                ease .25 pos (0,-60)
                pause 1
                ease 2.50 pos (0,25)#(0,10)
                repeat
        #pos (750,230)
        offset (0,100)
image Rogue_Sex_Legs_FootAnim2:
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 pos (0,-65)
                ease .2 pos (0,-60)
                pause .2
                ease 1.0 pos (0,25)#(0,10)
                repeat
        offset (0,100)

#transform Rogue_Sex_Legs_FootAnim1A():
#        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
#            subpixel True
#            offset (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 4 seconds
#                pause .5
#                easein .75 yoffset -65
#                ease .25 yoffset -60
#                pause 1
#                ease 1.50 yoffset 25
#                repeat

#transform Rogue_Sex_Legs_FootAnim2A():
#        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
#            subpixel True
#            offset (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 4 seconds
#                pause .2
#                easein .4 yoffset -65
#                ease .2 yoffset -60
#                pause .2
#                ease 1.0 yoffset 25
#                pause .2
#                easein .4 yoffset -65
#                ease .2 yoffset -60
#                pause .2
#                ease 1.0 yoffset 25
#                repeat

#transform Rogue_Sex_Legs_FootAnimStaticA():
#        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
#            subpixel True
#            offset (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 4 seconds
#                pause .5
#                ease 1 yoffset -5
#                pause 1
#                ease 1.50 yoffset 0
#                repeat

#End Animations for Rogue's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Body_FootAnimStatic:
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        offset (0,100)
image Rogue_Sex_Body_FootAnim1:
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-25)#(0,-5)
                ease .25 pos (0,-15)#(0,0)
                pause 1
                ease 2.50 pos (0,15)#(0,5)
                repeat
        #pos (750,230)
        offset (0,100)
image Rogue_Sex_Body_FootAnim2:
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 pos (0,-25)#(0,-5)
                ease .2 pos (0,-15)#(0,0)
                pause .2
                ease 1.0 pos (0,15)#(0,5)
                repeat
        offset (0,100)

#transform Rogue_Sex_Body_FootAnim1A():
#        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
#            subpixel True
#            offset (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 4 seconds
#                pause .5
#                easein .75 yoffset -25
#                ease .25 yoffset -15
#                pause 1
#                ease 1.50 yoffset 15
#                repeat

#transform Rogue_Sex_Body_FootAnim2A():
#        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
#            subpixel True
#            offset (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 2 seconds
#                pause .2
#                easein .4 yoffset -25
#                ease .2 yoffset -15
#                pause .2
#                ease 1.0 yoffset 15
#                pause .2
#                easein .4 yoffset -25
#                ease .2 yoffset -15
#                pause .2
#                ease 1.0 yoffset 15
#                repeat

#transform Rogue_Sex_Body_FootAnimStaticA():
#        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
#            subpixel True
#            offset (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 4 seconds
#                pause .5
#                ease 1 yoffset -5
#                pause 1
#                ease 1.50 yoffset 0
#                repeat
#End Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Rogue_Sex_Launch(Line = Trigger):
    $ RogueX.Offhand = 0 if RogueX.Offhand == "hand" else RogueX.Offhand

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(RogueX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(RogueX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
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
        call Zero_Strapped(RogueX) #puts strap-on on.
    $ Trigger = Line

    if RogueX.Pose == "doggy":
            call Rogue_Doggy_Launch(Line)
            return
    if renpy.showing("Rogue_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(RogueX,1) #call Rogue_Hide(1)
    show Rogue_SexSprite zorder 150
#    show Rogue_SexSprite zorder 150:
#        pos (750,230)
    return

label Rogue_Sex_Reset:
    if renpy.showing("Rogue_Doggy_Animation"):
        call Rogue_Doggy_Reset
        return
    if not renpy.showing("Rogue_SexSprite"):
        return
    $ RogueX.ArmPose = 2
    hide Rogue_SexSprite
    call Girl_Hide(RogueX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    $ Speed = 0
    return


# End Rogue Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue BJ element
#Rogue BJ Over Sprite Compositing

## Rogue's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


layeredimage Rogue_BJ_Animation:
    if Speed == 0:
        "Rogue_BJ_Anim0"
    elif Speed == 1:
        "Rogue_BJ_Anim1"
    elif Speed == 2:
        "Rogue_BJ_Anim2"
    elif Speed == 3:
        "Rogue_BJ_Anim3"
    elif Speed == 4:
        "Rogue_BJ_Anim4"
    elif Speed == 5:
        "Rogue_BJ_Anim5"
    elif Speed == 6:
        "Rogue_BJ_Anim6"
    zoom .8 #.7
    transform_anchor True
    anchor (.5,.5)
    offset (-95,85) #(-90,100)
image Rogue_BJ_Backdrop:                                                                        #Her Body under the head
    "Rogue_Sprite"
    zoom 3
    pos (50,-850)#(175,-110)
#    offset #(-615, -125)

# image Rogue_BJ_Backdrop # image Rogue_BJ_Backdrop # image Rogue_BJ_Backdrop End # image Rogue_BJ_Backdrop # image Rogue_BJ_Backdrop End
layeredimage Rogue_BJ_Head:
    if renpy.showing('Rogue_BJ_Animation') and Speed > 1:
        Null()
    else:
        "Rogue_BJ_Head_Under" offset (-105, 300)
    if RogueX.Blush and renpy.showing('Rogue_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6):
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Head_Over_Blush.png"
    elif renpy.showing('Rogue_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6):
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Head_Over.png"
    elif RogueX.Blush:
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Head_Over_Blush.png"
    else:
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Head_Over.png"
    if Speed and renpy.showing('Rogue_BJ_Animation'):
        if Speed == 1:
            "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
        else:
            "images/RogueBJFace/Rogue_BJ_Mouth_Over.png"
    elif renpy.showing('Rogue_CUN_Animation') and Speed:
        "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
    elif Speed >= 3 and renpy.showing('Rogue_TJ_Animation'):
        "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
    elif RogueX.Mouth == 'lipbite':
        "images/RogueBJFace/Rogue_BJ_Mouth_Lipbite.png"
    elif RogueX.Mouth == 'sucking':
        "images/RogueBJFace/Rogue_BJ_Mouth_Open.png"
    elif RogueX.Mouth == 'kiss':
        "images/RogueBJFace/Rogue_BJ_Mouth_Kiss.png"
    elif RogueX.Mouth == 'sad':
        "images/RogueBJFace/Rogue_BJ_Mouth_Sad.png"
    elif RogueX.Mouth == 'smile':
        "images/RogueBJFace/Rogue_BJ_Mouth_Smile.png"
    elif RogueX.Mouth == 'smirk':
        "images/RogueBJFace/Rogue_BJ_Mouth_Normal.png"
    elif RogueX.Mouth == 'grimace':
        "images/RogueBJFace/Rogue_BJ_Mouth_Smile.png"
    elif RogueX.Mouth == 'surprised':
        "images/RogueBJFace/Rogue_BJ_Mouth_Sucking.png"
    elif RogueX.Mouth == 'tongue':
        "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
    else:
        "images/RogueBJFace/Rogue_BJ_Mouth_Normal.png"
    if 'mouth' not in RogueX.Spunk or not Player.Male:
        Null()
    elif Speed and renpy.showing('Rogue_BJ_Animation'):
        if Speed == 1:
            "images/RogueBJFace/Rogue_BJ_Spunk_Tongue.png"
        elif (Speed == 2 or Speed == 5):
            "images/RogueBJFace/Rogue_BJ_Spunk_Heading.png"
        elif Speed == 3:
            "images/RogueBJFace/Rogue_BJ_Spunk_Sucking.png"
        elif Speed == 4:
            "images/RogueBJFace/Rogue_BJ_Spunk_Sucking.png"
        elif Speed == 6:
            "images/RogueBJFace/Rogue_BJ_Spunk_Sucking.png"
    elif RogueX.Mouth == 'sucking':
        "images/RogueBJFace/Rogue_BJ_Spunk_Open.png"
    elif RogueX.Mouth == 'kiss':
        "images/RogueBJFace/Rogue_BJ_Spunk_Sad.png"
    elif RogueX.Mouth == 'sad':
        "images/RogueBJFace/Rogue_BJ_Spunk_Sad.png"
    elif RogueX.Mouth == 'surprised':
        "images/RogueBJFace/Rogue_BJ_Spunk_Open.png"
    elif RogueX.Mouth == 'tongue':
        "images/RogueBJFace/Rogue_BJ_Spunk_Tongue.png"
    else:
        "images/RogueBJFace/Rogue_BJ_Spunk_Smile.png"
    if Player.Male:
        Null()
    elif 'mouth' not in RogueX.Spunk and 'chin' not in RogueX.Spunk:
        Null()
    elif RogueX.Mouth == 'tongue' or Speed:
        "images/RogueBJFace/Rogue_BJ_Wet_Tongue.png"
    elif 'mouth' in RogueX.Spunk or 'chin' in RogueX.Spunk:
        "images/RogueBJFace/Rogue_BJ_Wet_Mouth.png"
    if RogueX.Brows == 'angry':
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Brows_Angry.png"
    elif RogueX.Brows == 'sad':
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Brows_Sad.png"
    elif RogueX.Brows == 'surprised':
        "images/RogueBJFace/Rogue_BJ_Brows_Surprised.png"
    elif RogueX.Brows == 'confused':
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Brows_Confused.png"
    else:
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Brows_Normal.png"
    always:
        "Rogue BJ Blink"
    if RogueX.Water or RogueX.Hair == 'wet':
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Wet.png")
    elif not Player.Male and 'facial' in RogueX.Spunk:
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Wet.png")
    elif RogueX.Hair == 'cosplay':
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Cos.png")
    else:
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Evo.png")
    if RogueX.Water:
        "images/RogueBJFace/Rogue_BJ_Water_Head.png"
    elif not Player.Male and 'facial' in RogueX.Spunk:
        "images/RogueBJFace/Rogue_BJ_Water_Head.png"
    if 'hair' in RogueX.Spunk and Player.Male:
        "images/RogueBJFace/Rogue_BJ_Spunk_Hair.png"
    elif 'facial' in RogueX.Spunk and Player.Male:
        "images/RogueBJFace/Rogue_BJ_Spunk_Facial.png"
    else:
        "Big_Steam" offset (250, 400)
    if RogueX.Lust > 70:
        "Big_Steam" offset (250, 400)
    zoom 1
    anchor (0.5, 0.5)
    offset (105,-300)#(90,-480)
image Rogue BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "RogueX.Eyes == 'normal'", "images/RogueBJFace/Rogue_BJ_Eyes_Normal.png",
            "RogueX.Eyes == 'sexy'", "images/RogueBJFace/Rogue_BJ_Eyes_Sexy.png",
            "RogueX.Eyes == 'closed'", "images/RogueBJFace/Rogue_BJ_Eyes_Closed.png",
            "RogueX.Eyes == 'surprised'", "images/RogueBJFace/Rogue_BJ_Eyes_Surprised.png",
            "RogueX.Eyes == 'side'", "images/RogueBJFace/Rogue_BJ_Eyes_Side.png",
            "RogueX.Eyes == 'leftside'", "images/RogueBJFace/Rogue_BJ_Eyes_Side.png",
            "RogueX.Eyes == 'stunned'", "images/RogueBJFace/Rogue_BJ_Eyes_Stunned.png",
            "RogueX.Eyes == 'down'", "images/RogueBJFace/Rogue_BJ_Eyes_Down.png",
            "RogueX.Eyes == 'manic'", "images/RogueBJFace/Rogue_BJ_Eyes_Surprised.png",
            "RogueX.Eyes == 'squint'", "images/RogueBJFace/Rogue_BJ_Eyes_Sexy.png",
            "True", "images/RogueBJFace/Rogue_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/RogueBJFace/Rogue_BJ_Eyes_Closed.png"
        .25
        repeat
layeredimage Rogue_BJ_HairBack:
    if RogueX.Water or RogueX.Hair == 'wet':
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Wet_Back.png")
    elif not Player.Male and 'facial' in RogueX.Spunk:
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Wet_Back.png")
    elif RogueX.Hair == 'cosplay':
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Cos_Back.png")
    else:
        Recolor("Rogue", "Hair", "images/RogueBJFace/Rogue_BJ_Hair_Evo_Back.png")
    zoom 1
    anchor (0.5, 0.5)
    offset (105,-300)#(90,-480)
layeredimage Rogue_BJ_Head_Under:
    always:
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_BJ_Head.png"
    if Speed and renpy.showing('Rogue_BJ_Animation'):
        if Speed == 1:
            "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
        elif Speed == 2 or Speed == 5:
            Null()
        else:
            "images/RogueBJFace/Rogue_BJ_Mouth_Heading.png"
    elif renpy.showing('Rogue_CUN_Animation') and Speed:
        "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
    elif Speed >= 3 and renpy.showing('Rogue_TJ_Animation'):
        "images/RogueBJFace/Rogue_BJ_Mouth_Tongue.png"
    else:
        "images/RogueBJFace/Rogue_BJ_Mouth_Normal.png"
    if 'chin' not in RogueX.Spunk or not Player.Male:
        Null()
    else:
        "images/RogueBJFace/Rogue_BJ_Spunk_Chin.png"
    zoom 1
    anchor (0.5, 0.5)
    offset (105,-300)#(90,-480)
layeredimage Rogue_BJ_Heading_Mouth:
    always:
        "images/RogueBJFace/Rogue_BJ_Mouth_Heading.png"
    if 'mouth' in RogueX.Spunk and Player.Male:
        "images/RogueBJFace/Rogue_BJ_Spunk_Sucking.png"
    zoom 1
    anchor (0.5, 0.5)
    offset (105,-300)#(90,-480)
image Rogue_TJ_ZeroCock:
            #cock used in Rogue's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.6)
            offset (-5,50)#(45,50)
            rotate 0
## End Rogue BJ Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_BJ_Anim0:
        #Static animation
        contains:
                # Rogue's hair back
                "Rogue_BJ_HairBack"
                subpixel True
                offset (-50,-105)     #top (350,190), - is up
                rotate 5
                parallel:
                    ease 1 yoffset -90           #bottom
                    pause .2
                    ease 1.5 yoffset -105     #top
                    repeat
                parallel:
                    ease 1 rotate -2          #bottom
                    pause .2
                    ease 1.5 rotate 2    #top
                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                offset (-300,0)     #top
                alpha 1
                transform_anchor True
                rotate -20
                parallel:
                    ease 1 yoffset 20          #bottom
                    pause .2
                    ease 1.5 yoffset 0    #top
                    repeat
#                parallel:
#                    ease 1 rotate -10
#                    pause .2
#                    ease 1.5 rotate -5#-20
#                    repeat
        contains:
                # head overlay
                "Rogue_BJ_Head"
                subpixel True
#                alpha .9
                offset (-50,-105)     #top (350,190), - is up
                rotate 5
                parallel:
                    ease 1 yoffset -90           #bottom
                    pause .2
                    ease 1.5 yoffset -105     #top
                    repeat
                parallel:
                    ease 1 rotate -2          #bottom
                    pause .2
                    ease 1.5 rotate 2    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
                    pause 1
                    ease .2 rotate .5
#                    pause .2
                    ease .3 rotate -0.2
                    ease .3 rotate 0
                    pause .9
                    repeat
#end Rogue_BJ_Anim0 Static
image Rogue_BJ_Anim1:
        #Licking animation
        contains:
                # Rogue's hair back
                "Rogue_BJ_HairBack"
                subpixel True
#                alpha .5
                offset (-110,-105)     #top (350,190), - is up
                rotate -16
                parallel:
                    ease 1.3 xoffset -130#-20           #bottom
                    ease .8 xoffset -90#-30           #bottom
                    ease .5 xoffset -95#-55     #top
                    ease 1.6 xoffset -110#-20     #top
                    repeat
                parallel: #4.2
                    pause .2
                    ease 1 yoffset 50#-5           #bottom
                    pause .2
                    ease 1.5 yoffset -125     #top
                    ease 1.3 yoffset -105     #top
                    repeat
                parallel:
                    easein 1.3 rotate -33          #bottom
                    ease 1.0 rotate -10    #top
                    ease .5 rotate 6#28          #bottom
                    ease .3 rotate 3#26          #bottom
#                    pause .1
                    easeout 1.1 rotate -16    #top  -16
                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                anchor (670,450)#(340,450)
                offset (-40,360)     #top
                alpha 1
                transform_anchor True
                rotate -20
#                parallel: #2.4 down, 1.8 up
#                    ease 1 xoffset -40           #top  40
#                    pause .6
#                    ease 1.2 xoffset -40     #bottom    -40
#                    ease 1 xoffset -40     #top  -30
#                    pause .4
#                    repeat
                parallel:
                    pause .3
                    ease 0.9 offset (-40,500)#-5           #bottom
                    pause .2
                    ease 1.5 yoffset 360     #top
                    ease 1.3 yoffset 360     #top
                    repeat
                parallel:
#                    ease .2 rotate -5          #
                    ease 1.0 rotate -25          #bottom
                    ease 1.0 rotate -23          #bottom
                    ease 1.2 rotate -20          #
                    pause 1#.5
                    repeat
        contains:
                # head overlay
                "Rogue_BJ_Head"
                subpixel True
#                alpha .5
                offset (-110,-105)     #top (350,190), - is up
                rotate -16
                parallel:
                    ease 1.3 xoffset -130#-20           #bottom
                    ease .8 xoffset -90#-30           #bottom
                    ease .5 xoffset -95#-55     #top
                    ease 1.6 xoffset -110#-20     #top
                    repeat
                parallel: #4.2
                    pause .2
                    ease 1 yoffset 50#-5           #bottom
                    pause .2
                    ease 1.5 yoffset -125     #top
                    ease 1.3 yoffset -105     #top
                    repeat
                parallel:
                    easein 1.3 rotate -33          #bottom
                    ease 1.0 rotate -10    #top
                    ease .5 rotate 6#28          #bottom
                    ease .3 rotate 3#26          #bottom
#                    pause .1
                    easeout 1.1 rotate -16    #top  -16
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
#                    pause 2.5
                    pause .3
                    ease .7 rotate -3
                    pause .5
                    ease .9 rotate -2           #bottom
                    pause .1
                    ease .1 rotate -2
                    ease .3 rotate 1
                    ease .2 rotate 0
                    pause 1.1
                    repeat
#end Rogue_BJ_Anim1 Licking
image Rogue_BJ_Anim2:
        #Heading animation
        contains:
                # Rogue's hairback
                "Rogue_BJ_HairBack"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                offset (-340,-20)     #top (-20,130), - is up
                alpha 1
                transform_anchor True
                rotate -20
#                parallel:
#                    ease .4 rotate -30
#                    pause .05
#                    ease .55 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset 0#-90   #bottom
                    pause .4
                    ease 1 yoffset -20#-130         #top
                    repeat
        contains:
                # Rogue's head Underlay
                "Rogue_BJ_Head_Under"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                # Rogue's open mouth
                "Rogue_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (340,450)#(350,640)
                pos (-10,100) #(0,293)
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                xzoom .8
                yzoom 1
                parallel:
                    ease 1 xzoom .9    #bottom
                    pause .4
                    ease 1 xzoom .5     #top
                    repeat
                parallel:
                    ease 1 yzoom 1.2    #bottom
                    pause .4
                    ease 1 yzoom 1      #top
                    repeat
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate -1
                alpha 1
                parallel:
                    easeout .4 rotate 0    #bottom
                    pause 1.6
                    easein .4 rotate -1      #top
                    repeat
#                parallel:
#                    pause .1
#                    ease .3 yoffset 20
#                    ease .5 yoffset 0
#                    pause .1
#                    repeat
        contains:
                # Rogue's head overlay
                "Rogue_BJ_Head"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
#end Rogue_BJ_Anim2 Heading
image Rogue_BJ_Anim3:
        #sucking fast animation
        contains:
                # Rogue's hairback
                "Rogue_BJ_HairBack"
                subpixel True
                offset (-90,-75)     #top (350,190), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-90,20)           #bottom
                    pause .05
                    ease .55 offset (-90,-75)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                offset (-420,100)     #top (-20,130), - is up
                alpha 1
                transform_anchor True
                rotate -30
#                parallel:
#                    ease .4 rotate -30
#                    pause .05
#                    ease .55 rotate -20#-20
#                    repeat
                parallel:
                    ease .35 yoffset 150#400           #bottom
                    pause .05
                    ease .6 yoffset 100     #top
                    repeat
        contains:
                # Rogue's head Underlay
                "Rogue_BJ_Head_Under"
                subpixel True
                offset (-90,-75)     #top (350,190), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-90,20)           #bottom
                    pause .05
                    ease .55 offset (-90,-75)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate 0
#                parallel:
#                    pause .1
#                    ease .3 rotate 2
#                    ease .4 rotate 0
#                    pause .2
#                    repeat
                parallel:
                    pause .1
                    ease .3 yoffset 20
                    ease .5 yoffset 0
                    pause .1
                    repeat
        contains:
                # head overlay
                "Rogue_BJ_Head"
                subpixel True
#                alpha .9
                offset (-90,-75)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-90,20)           #bottom
                    pause .05
                    ease .55 offset (-90,-75)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
##end Rogue_BJ_Anim3 Sucking
image Rogue_BJ_Anim4:
        #Deep animation
        contains:
                # Rogue's hairback
                "Rogue_BJ_HairBack"
                subpixel True
                offset (-90,80)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1 offset (-90,230)          #bottom
                    pause .2
                    ease 1.5 offset (-90,80)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                offset (-440, 200)     #top
                alpha 1
                transform_anchor True
                rotate -40
#                parallel:
#                    ease 1 rotate -45
#                    pause .2
#                    ease 1.5 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset 400#400           #bottom
                    pause .2
                    ease 1.5 yoffset 300     #top
                    repeat
        contains:
                # Rogue's head Underlay
                "Rogue_BJ_Head_Under"
                subpixel True
                offset (-90,80)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1 offset (-90,230)          #bottom
                    pause .2
                    ease 1.5 offset (-90,80)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
#                parallel:
#                    pause .2
#                    ease .8 rotate 15
#                    pause .2
#                    ease 1.2 rotate 0
#                    pause .3
#                    repeat
        contains:
                # head overlay
                "Rogue_BJ_Head"
                subpixel True
#                alpha .9
                offset (-90,80)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1 offset (-90,230)          #bottom
                    pause .2
                    ease 1.5 offset (-90,80)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
#end Rogue_BJ_Anim4 Deep
image Rogue_BJ_Anim5:
        #Cum high animation
        contains:
                # Rogue's hair back
                "Rogue_BJ_HairBack"
                subpixel True
                offset (-90,-110)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                offset (-340,-20)     #top (-20,130), - is up
                alpha 1
                transform_anchor True
                rotate -20
                parallel:
                    ease 1.5 offset (-340,0)#-90   #bottom
                    pause .2
                    ease 1.5 offset (-340,-20)#-130         #top
                    repeat
        contains:
                # Rogue's head Underlay
                "Rogue_BJ_Head_Under"
                subpixel True
                offset (-90,-110)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat
        contains:
                # Rogue's open mouth
                "Rogue_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (340,450)#(350,640)
                pos (-10,100) #(0,293)
                offset (-90,-110)     #top (-20,130), - is up
                rotate 0
                xzoom .8
                yzoom 1
                parallel:
                    ease 1.5 xzoom 1    #bottom
                    pause .2
                    ease 1.5 xzoom .8     #top
                    repeat
                parallel:
                    ease 1.5 yzoom 1.2    #bottom
                    pause .2
                    ease 1.5 yzoom 1      #top
                    repeat
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat

        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate 0
#                alpha .6
#                parallel:
#                    easeout .4 rotate 0    #bottom
#                    pause 1.6
#                    easein .4 rotate -1      #top
#                    repeat
#                parallel:
#                    pause .1
#                    ease .3 yoffset 20
#                    ease .5 yoffset 0
#                    pause .1
#                    repeat
        contains:
                # Rogue's head overlay
                "Rogue_BJ_Head"
                subpixel True
                offset (-90,-110)     #top (-20,130), - is up
                rotate 0
#                alpha .6
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat
#end Rogue_BJ_Anim5 Cum high
image Rogue_BJ_Anim6:
        #Cum Deep animation
        contains:
                # Rogue's hairback
                "Rogue_BJ_HairBack"
                subpixel True
                offset (-90,200)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1.1 offset (-90,230)          #bottom
                    pause .2
                    ease .7 offset (-90,200)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
        contains:
                #  Rogue's body, everything below the chin
                "Rogue_BJ_Backdrop"
                subpixel True
                offset (-440,380)     #top
                alpha 1
                transform_anchor True
                rotate -40
#                parallel:
#                    ease 1 rotate -45
#                    pause .2
#                    ease 1.5 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset 420#400           #bottom
                    pause .2
                    ease .8 yoffset 380     #top
                    repeat

        contains:
                # Rogue's head Underlay
                "Rogue_BJ_Head_Under"
                subpixel True
                offset (-90,200)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1.1 offset (-90,230)          #bottom
                    pause .2
                    ease .7 offset (-90,200)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Rogue_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
#                parallel:
#                    pause .2
#                    ease .8 rotate 15
#                    pause .2
#                    ease 1.2 rotate 0
#                    pause .3
#                    repeat
        contains:
                # head overlay
                "Rogue_BJ_Head"
                subpixel True
#                alpha .9
                offset (-90,200)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1.1 offset (-90,230)          #bottom
                    pause .2
                    ease .7 offset (-90,200)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
#end Rogue_BJ_Anim6 Cum Deep


# End Rogue Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


                                                            #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_BJ_Launch(Line = Trigger):
    # The sequence to launch the Rogue BJ animations
    if renpy.showing("Rogue_BJ_Animation") and RogueX.Pose != "69":
        return
    elif renpy.showing("Rogue_69_Animation") and RogueX.Pose == "69":
        return

    if not Player.Male:
        call Rogue_CUN_Launch
        return

    $ Speed = 0
    $ Player.Sprite = 1
    $ RogueX.ArmPose = 1

    if Line == "none":
        $ Player.Sprite = 0
    elif Line != "cum":
        $ Trigger = "blow"

    call Girl_Hide(RogueX) #call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Rogue_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Rogue_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,140) #(-90,140)
        with dissolve
    hide Rogue_Sprite

    if RogueX.Pose == "69":
            show Rogue_69_Animation zorder 150
    else:
            show Rogue_BJ_Animation zorder 150:
                pos (1000,1050)#(1000,1000)#(700,520)

    if Taboo and Line == "L":
            # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[RogueX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    if Line == "L":
                    if not RogueX.Blow:
                        "[RogueX.Name] нерешительно стягивает с вас штаны и прикасается своим ртом к вашему члену"
                    else:
                        "[RogueX.Name] наклоняется и начинает сосать ваш член."

    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

#    show Rogue_Sprite zorder RogueX.Layer:
#        alpha 0
#    show Rogue_BJ_Animation zorder 150:
#        pos (1000,1050)#pos (645,510)
    return

label Rogue_BJ_Reset: # The sequence to the Rogue animations from BJ to default
    if Player.Male != 1:
            call Rogue_CUN_Reset
    if not renpy.showing("Rogue_BJ_Animation") and not renpy.showing("Rogue_69_Animation"):
        return
#    hide Rogue_BJ_Animation
    call Girl_Hide(RogueX) #call Rogue_Hide
    $ Speed = 0

    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    $ RogueX.FaceChange("sexy")
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


image Blowcock:
    contains:
        ConditionSwitch(
            "not Player.Male", "images/RogueBJFace/Zero_Cock_D.png",
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk and Player.Male", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)#(-175,450)
image Ghostcock:
    "Blowcock"
    alpha 0.5
image Zero_Blowcock:
    LiveComposite(                            #The compositived BJ cock
        (175,946),
        (0,0), ConditionSwitch(
            "not Player.Male", "images/RogueBJFace/Zero_Cock_D.png",
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Spunk and Player.Male", "images/RogueBJFace/Zero_Cock_S.png",
            "Player.Wet or Player.Spunk", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
        )
    anchor (0.5,0.5)
    zoom 1.2
    xoffset 5
image Zero_Ghostcock:
    "Zero_Blowcock"
    alpha 0.5



# Core Rogue Titfucking element //////////////////////////////////////////////////////////////////////                                         Core Rogue TJ element
image Rogue_TJ_Under:
    contains:
        "Rogue_BJ_HairBack"
        pos (410, 300)#(150, -560)
        zoom 1.4
        rotate -5
    contains:
        "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_tj_base.png"
    contains:
        ConditionSwitch(
            "'tits' in RogueX.Spunk and Player.Male", "images/RogueBJFace/Rogue_tj_spunkU.png",
            "True", Null(),
            ),
    contains:
        "Rogue_BJ_Head"
        pos (410, 300)#(150, -560)
        zoom 1.4
        rotate -5
    pos (-60, 200)
image Rogue_TJ_Over:
    contains:
        ConditionSwitch(
            "RogueX.Pierce == 'barbell'", "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_tj_tits_b.png",
            "RogueX.Pierce == 'ring'", "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_tj_tits_r.png",
            "RogueX.Pierce != 'barbell'", "images/RogueBJFace/[RogueX.skin_image.skin_path]Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch(
            "'tits' in RogueX.Spunk and Player.Male", "images/RogueBJFace/Rogue_tj_spunk.png",
            "True", Null(),
            ),
    pos (-60, 200)
transform Rogue_TJ_Under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout .2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_TJ_Over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout .1 ypos 300
        easein 1.2 ypos 120
        repeat

transform Rogue_TJ_Under_2():
    ypos 200
    subpixel True
    block:
        ease .25 ypos 200
        ease .4 ypos 120
        ease .1 ypos 125
        repeat

transform Rogue_TJ_Over_2():
    ypos 200
    subpixel True
    block:
        ease .3 ypos 200
        ease .35 ypos 120
        ease .1 ypos 125          #high point
        repeat


transform Zero_TJ_Cock():
    #The sucking animation for the cock
    anchor (.5,.5)
    pos (440,1020) #220,1000 #(180,560)
    rotate 0

transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout .2 ypos 1060
        easein 1.3 ypos 1020
        repeat

transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease .35 ypos 1030
        ease .4 ypos 1020
#        pause .1
        repeat



image Rogue_TJ_Animation:
    #core TJ animation
    contains:
        ConditionSwitch(
            "not Speed", Transform("Rogue_TJ_Under"),
            "Speed == 1", At("Rogue_TJ_Under", Rogue_TJ_Under_1()),
            "Speed >= 2", At("Rogue_TJ_Under", Rogue_TJ_Under_2()),
            "Speed", Null(),
            ),

    contains:
        ConditionSwitch(
            "not Speed", At("Zero_Blowcock", Zero_TJ_Cock()),
            "Speed == 1", At("Zero_Blowcock", Zero_TJ_Cock_1()),
            "Speed >= 2", At("Zero_Blowcock", Zero_TJ_Cock_2()),
            "Speed", Null(),
            ),

    contains:
        ConditionSwitch(
            "not Speed", Transform("Rogue_TJ_Over"),
            "Speed == 1", At("Rogue_TJ_Over", Rogue_TJ_Over_1()),
            "Speed >= 2", At("Rogue_TJ_Over", Rogue_TJ_Over_2()),
            "Speed", Null(),
            ),
    anchor (0.6, 0.0)
    offset (-75, 250)
    zoom .55
label Rogue_TJ_Launch(Line = Trigger):
    # The sequence to launch the Rogue Titfuck animations
    if renpy.showing("Rogue_TJ_Animation"):
        return
    call Girl_Hide(RogueX) #call Rogue_Hide
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 2 xpos 550 offset (0,50)
    if Taboo: # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[RogueX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."

    if RogueX.Chest and RogueX.Over:
        "Она снимает [get_clothing_name(RogueX.Over_key, vin)] и [get_clothing_name(RogueX.Chest_key, vin)]."
    elif RogueX.Over:
        "Она снимает [get_clothing_name(RogueX.Over_key, vin)], обнажая грудь."
    elif RogueX.Chest:
        "Она стягивает [get_clothing_name(RogueX.Chest_key, vin)] и отбрасывает в сторону."
    $ RogueX.Over = 0
    $ RogueX.Chest = 0
    $ RogueX.Arms = 0

    call Girl_First_Topless(RogueX)

    if not RogueX.Tit and Line == "L": #first time
        if not RogueX.Chest and not RogueX.Over:
            "Когда вы вытаскиваете свой член, [RogueX.Name] нерешительно помещает его между грудей и начинает двигать ими вверх и вниз по всей длине члена."
        elif RogueX.Chest and not RogueX.Over:
            "Когда вы вытаскиваете свой член, [RogueX.Name] нерешительно помещает его под [get_clothing_name(RogueX.Chest_key, vin)], между грудей, и начинает двигать ими вверх и вниз по всей длине члена."
        elif RogueX.Chest and RogueX.Over:
            "Когда вы вытаскиваете свой член, [RogueX.Name] нерешительно помещает его под [get_clothing_name(RogueX.Over_key, vin)], между грудей, и начинает двигать ими вверх и вниз по всей длине члена."
        else:
            "Когда вы вытаскиваете свой член, [RogueX.Name] нерешительно помещает его себе под одежду, между грудей, и начинает двигать ими вверх и вниз по всей длине члена."
    elif Line == "L": #any other time
        if not RogueX.Chest and not RogueX.Over:
            "Когда вы вытаскиваете свой член, [RogueX.Name] помещает его между грудей и начинает двигать ими вверх и вниз по всей длине члена."
        elif RogueX.Chest and not RogueX.Over:
            "Когда вы вытаскиваете свой член, [RogueX.Name] помещает его под [get_clothing_name(RogueX.Chest_key, vin)], между грудей, и начинает двигать ими вверх и вниз по всей длине члена."
        elif RogueX.Chest and RogueX.Over:
            "Когда вы вытаскиваете свой член, [RogueX.Name] помещает его под [get_clothing_name(RogueX.Over_key, vin)], между грудей, и начинает двигать ими вверх и вниз по всей длине члена."
        else:
            "Когда вы вытаскиваете свой член, [RogueX.Name] помещает его себе под одежду, между грудей, и начинает двигать ими вверх и вниз по всей длине члена."
    else:
            "[RogueX.Name] обхватывает своими сиськами ваш член."
    show blackscreen onlayer black with dissolve
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Rogue_TJ_Animation at SpriteLoc(StageRight) zorder 150
    hide blackscreen onlayer black with dissolve
    return

label Rogue_TJ_Reset:
    # The sequence to the Rogue animations from Titfuck to default
    if not renpy.showing("Rogue_TJ_Animation"):
            return
    hide Rogue_TJ_Animation
    call Girl_Hide(RogueX) #call Rogue_Hide
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
            zoom 2 xpos 550 offset (0,50)
    show Rogue_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 500 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.SpriteLoc yoffset 0
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1 zoom 1 xpos RogueX.SpriteLoc yoffset 0

    "[RogueX.Name] отстраняется"
    return


# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element

image Zero_Handcock:
    contains:
        ConditionSwitch(    # Zero cock sucking
            "not Player.Male", "images/RogueBJFace/handcock_D.png",
            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png",
            "Player.Color != 'pink'", Null(),
            ),
    anchor (0.5,1.0)  #1.0
    pos (200,400)#(200,400)
image Rogue_HJ_Body:
    "Rogue_Sprite"
    pos (350,-650)#(450,-650)
    zoom 3#4.8
transform Rogue_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -620
        pause 0.25
        ease 1.0 ypos -650
        pause 0.1
        repeat

transform Rogue_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -640
        pause 0.1
        ease 0.4 ypos -650
        pause 0.1
        repeat

image Rogue_Hand_Under:
    "images/RogueBJFace/[RogueX.skin_image.skin_path]hand2.png"
    anchor (0.5,0.5)
    pos (0,0)
image Rogue_Hand_Over:
    "images/RogueBJFace/[RogueX.skin_image.skin_path]hand1.png"
    anchor (0.5,0.5)
    pos (0,0)
transform Handcock_1():
    subpixel True
    rotate_pad False
    ease .5 ypos 450 rotate -2 #450
    pause 0.25
    ease 1.0 ypos 400 rotate 0 #400
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease .2 ypos 430 rotate -3 #410
    ease .5 ypos 400 rotate 0
    pause 0.1
    repeat

transform Rogue_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

image Rogue_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Rogue_HJ_Body"),
            "Speed == 1", At("Rogue_HJ_Body", Rogue_HJ_Body_1()),
            "Speed >= 2", At("Rogue_HJ_Body", Rogue_HJ_Body_2()),
            "Speed", Null(),
            )
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", "Rogue_Hand_Under",
            "Speed == 1", At("Rogue_Hand_Under", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Under", Rogue_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", "Zero_Handcock",
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", "Rogue_Hand_Over",
            "Speed == 1", At("Rogue_Hand_Over", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Over", Rogue_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6
label Rogue_HJ_Launch(Line = Trigger):
    if renpy.showing("Rogue_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Rogue_Finger_Launch
        return
    call Girl_Hide(RogueX) #call Rogue_Hide
    $ RogueX.Arms = 0
    $ RogueX.ArmPose = 1
    if not renpy.showing("Rogue_Sprite"):
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 700 offset (0,200)
        with dissolve
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7  xpos 700 offset (0,200)

    if Line == "L": # Rogue gets started. . .
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != EmmaX:
                        "[RogueX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[RogueX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и хватает ваш член."
        else:
            "[RogueX.Name] наклоняется и хватает ваш член."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    show Rogue_HJ_Animation at SpriteLoc(RogueX.SpriteLoc) zorder 150 with fade
    return

label Rogue_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Rogue_HJ_Animation"):
        return
    $ Speed = 0
    hide Rogue_HJ_Animation
    with dissolve
    call Girl_Hide(RogueX) #call Rogue_Hide
#    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
#        alpha 1
#        zoom 1.7  xpos 700 offset (0,200)
    show Rogue_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.SpriteLoc yoffset 0
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1 zoom 1  xpos RogueX.SpriteLoc yoffset 0
    return
# End Rogue HJ stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue CUN element
#Rogue CUN Over Sprite Compositing


# Core Image for Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
image Zero_Pussy:
    contains:
        ConditionSwitch(    # Zero's pussy
            "(Player.Wet or Player.Spunk) and Player.Color == 'brown'",  "images/Zero_Puss_B_Wet.png",
            "(Player.Wet or Player.Spunk) and Player.Color == 'green'",  "images/Zero_Puss_G_Wet.png",
            "Player.Wet or Player.Spunk",                                "images/Zero_Puss_P_Wet.png",
            "Player.Color == 'brown'",  "images/Zero_Puss_B.png",
            "Player.Color == 'green'",  "images/Zero_Puss_G.png",
            "True",                     "images/Zero_Puss_P.png",
            ),
    anchor (0.5,0.5)  #1.0
    pos (250,300) #(350,300)
# end Core Image for Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

# Core Image for Zero's legs < < < < < < < < < < < < < < < < < < < < < < < <
image Zero_Legs:
    contains:
        ConditionSwitch(    # Zero's pussy
            "Player.Color == 'brown'",  "images/Zero_Legs_B.png",
            "Player.Color == 'green'",  "images/Zero_Legs_G.png",
            "True",                     "images/Zero_Legs_P.png",
            ),
    anchor (0.5,0.5)  #1.0
    pos (250,300) #(350,300)
image Zero_Pussy_Full:
    contains:
            #pussy
            "Zero_Pussy"
            offset (250,-3)
    contains:
            #pussy
            "Zero_Legs"
#    alpha 0.8
# end image Zero_Pussy_Full
# end Core Image for Zero's legs < < < < < < < < < < < < < < < < < < < < < < < <
layeredimage Rogue_CUN_Animation:
    if Speed == 0:
        "Rogue_CUN_Anim_Static"
    elif Speed == 1:
        "Rogue_CUN_Anim_Licking1"
    elif Speed == 2:
        "Rogue_CUN_Anim_Licking2"
    elif Speed >= 3:
        "Rogue_CUN_Anim_Licking3"
    else:
        "Rogue_CUN_Anim_Static"
    zoom .55
    anchor (.5,.5)
image Rogue_CUN_Anim_Static:
    #Animation for licking speed 1
    contains:
        #hair
        "Rogue_BJ_HairBack"#"BJ_HairBack"
        subpixel True
#        offset (-10,0)
        zoom 1.4
        pos (120,750)#(-50,570)
        offset (70,0)#(-10,0)
        rotate 0
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #body 2
        "Rogue_Sprite"
        zoom 4.5
        pos (135,-290)# (345,-110)
        subpixel True
        offset (0,0)  #top(0,-35)
    contains:
        #head
        "Rogue_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
#        offset (-10,0)
        pos (120,750)#(-50,570)
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
        pos (500,1260)#750)
        offset (0,0)
    #    block:
    #        ease 1 yoffset 490
    #        ease 1 yoffset 480
    #        repeat
image Rogue_CUN_Anim_Licking1:
    #Animation for licking speed 1
    contains:
        #hair
        "Rogue_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (120,750)#(-50,570)
        offset (40,40)#(40,40)
#        rotate 10
        block: #5s total
            ease 2.5 offset (45,100) #bottom (0,75)
            easeout 1.5 offset (45,60)  #top (0,60)
            ease .5 offset (40,20)  #top
            ease .5 offset (42,30)  #top
            repeat
    contains:
        #body 2
        "Rogue_Sprite"
        zoom 4.5
        pos (135,-290)#(345,-110)
#        offset (-615, -125)
        subpixel True
        offset (-70,0)#490)
        block:
            ease 2.5 offset (-55,90) #bottom (30,90)
            ease 2 offset (-70,0)  #top
            pause .5
            repeat
    contains:
        #head
        "Rogue_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (120,750)#(-50,570)
        offset (40,40)#(40,40)
#        rotate 10
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
        pos (500,1260)#750)
        offset (0,5)#490)
        block:
            easein 1 yoffset 10 #510 bottom
            pause 1.5
            easeout 1 yoffset 0#490
            linear .3 yoffset -5#490
            easein .2 yoffset -3#490
            easeout 1 yoffset 5 #510 bottom
            repeat
#End Rogue Licking 1
image Rogue_CUN_Anim_Licking2:
    #Animation for licking speed 2
    contains:
        #hair
        "Rogue_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (230,750)#(-50,570)
        offset (-80,30)#490)
        block: #2s total
            ease 1 offset (-60,100) #bottom
            easeout .65 offset (-70,70)  #top -35)
            linear .25 offset (-80,30)  #top -35)
            pause .1
            repeat
    contains:
        #body 2
        "Rogue_Sprite"
        zoom 4.5
        pos (135,-290)# (345,-110)#(175,-110)
        subpixel True
        offset (-70,0)#490)
        block:
            ease .75 offset (-55,50) #bottom (30,90)
            ease .95 offset (-70,0)  #top
            pause .30
            repeat
    contains:
        #head
        "Rogue_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (230,750)#(-50,570)
        offset (-80,30)#490)
        block: #2s total
            ease 1 offset (-60,100) #bottom
            easeout .65 offset (-70,70)  #top -35)
            linear .25 offset (-80,30)  #top -35)
            pause .10
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (500,1260)#750)
        offset (0,-3)#490)
        block:
            ease .5 yoffset 10 #510 bottom
            pause .5
            easeout .6 yoffset 0#490
            linear .1 yoffset -5#490
            easein .1 yoffset -3#490
            pause .2
            repeat
#End Rogue Licking 2
image Rogue_CUN_Anim_Licking3:
    #Animation for licking speed 3
    contains:
        #hair
        "Rogue_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (240,750)#(-50,570)
        offset (-80,90)#490)
        block: #2s total
            ease .5 offset (-80,110) #bottom
            ease .5 offset (-80,90)  #top -35)
            repeat
    contains:
        #body 2
        "Rogue_Sprite"
        zoom 4.5
        pos (135,-290)#(345,-110)
        subpixel True
        offset (-70,90)#490)
        block:
            ease .4 offset (-70,100) #bottom (30,90)
            ease .4 offset (-70,90)  #top
            pause .2
            repeat
    contains:
        #head
        "Rogue_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (240,750)#(-50,570)
        offset (-80,90)#490)
        block: #2s total
            ease .5 offset (-80,110) #bottom
            ease .5 offset (-80,90)  #top -35)
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (500,1260)#(670,1260)
        offset (0,5)#490)
        block:
            ease .25 yoffset 10 #510 bottom
            pause .25
            ease .25 yoffset 5#490
            ease .25 yoffset 6#490
            repeat
#End Rogue Licking 3

#BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Rogue_CUN_Launch(Line = Trigger):
    # The sequence to launch the Rogue CUN animations
    if renpy.showing("Rogue_CUN_Animation") and RogueX.Pose != "69":
        return
    elif renpy.showing("Rogue_69_CUN") and RogueX.Pose == "69":
        return

    if Player.Male == 1:
        call Rogue_BJ_Launch
        return

    call Girl_Hide(RogueX) #call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Rogue_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240)
        with dissolve
    else:
        show Rogue_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != RogueX:
                        "[RogueX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[RogueX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not RogueX.Blow:
                "[RogueX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[RogueX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Rogue_Sprite:
        alpha 0
    if RogueX.Pose == "69":
            show Rogue_69_CUN zorder 150
    else:
            show Rogue_CUN_Animation zorder 150:
                pos (645,570)#(645,610)

    return

label Rogue_CUN_Reset: # The sequence to the Rogue animations from CUN to default
    if not renpy.showing("Rogue_CUN_Animation") and not renpy.showing("Rogue_69_CUN"):
        return
#    hide Rogue_CUN_Animation
    call Girl_Hide(RogueX) #call Rogue_Hide
    $ Speed = 0

    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ RogueX.FaceChange("sexy")
    return

#End Rogue Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Rogue_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Rogue_Finger_1",
            "Speed >= 2", "Rogue_Finger_2",
            "True", "Rogue_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
image Rogue_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Rogue_Sprite"
            pos (280,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Wet.png",
                "True", "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (20,40)

#            "Rogue_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (20,40)
#            "Rogue_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
image Rogue_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Rogue_Sprite"
            pos (280,-550)
            zoom 2.15
            block:
                ease .5 ypos (-540) #(-30,50)   Bottom
                pause 0.25
                ease 1.0 ypos (-550)  #((20,-60) Top                 pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Wet.png",
                "True", "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (10,40)
            rotate -5
            block:
                ease .5 pos (10,85) rotate -15 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (10,40) rotate -5 #((20,-60) Top                 pause 0.1
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
            "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Over.png"
#            "Rogue_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (10,40)
            rotate -5
            block:
                ease .5 pos (10,85) rotate -15 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (10,40) rotate -5 #((20,-60) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
image Rogue_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Rogue_Sprite"
            pos (280,-550)
            zoom 2.15
            block:
                ease 0.15 ypos -540  #rotate 3   100
                pause 0.1
                ease 0.45 ypos -550  #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Wet.png",
                "True", "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
            rotate -15
            pos (10,40)
            block:
                ease 0.15 ypos 85 #rotate 3   100
                pause 0.1
                ease 0.45 ypos 40 #rotate -3  40
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
            "RogueBJFace/[RogueX.skin_image.skin_path]Rogue_Fingering_Over.png"
#            "Rogue_Finger_Over"
            anchor (0.5,0.6)
            subpixel True
            transform_anchor True
            rotate -15
            pos (10,40)
            block:
                ease 0.15 ypos 85 #rotate 3
                pause 0.1
                ease 0.45 ypos 40 #rotate -3 -50
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
label Rogue_Finger_Launch(Line = Trigger):
    if renpy.showing("Rogue_Finger_Animation"):
        $ Trigger = "finger"
        return
    if Player.Male == 1:
        call Rogue_HJ_Launch
        return

    call Girl_Hide(RogueX) #call Rogue_Hide
    $ RogueX.Arms = 0
    $ RogueX.ArmPose = 1
    if not renpy.showing("Rogue_Sprite"):
        show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 800 yoffset 200 #offset (-50,200)
        with dissolve
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 800 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Rogue gets started. . .
        if len(Present) >= 2:
            if Present[0] != RogueX:
                    "[RogueX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != RogueX:
                    "[RogueX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[RogueX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not RogueX.Hand and RogueX.Arms:
            "Когда вы стягиваете свои штаны, [RogueX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not RogueX.Hand and RogueX.Arms:
            "Когда вы стягиваете свои штаны, [RogueX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[RogueX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[RogueX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    show Rogue_Finger_Animation at SpriteLoc(RogueX.SpriteLoc) zorder 150 with fade
    return

label Rogue_Finger_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Rogue_Finger_Animation"):
        return
    $ Speed = 0
    hide Rogue_Finger_Animation
    with dissolve
    call Girl_Hide(RogueX) #call Rogue_Hide
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder 150:
        alpha 0 zoom 1.7  xpos 800 yoffset 200
    show Rogue_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos RogueX.SpriteLoc yoffset 0
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1 zoom 1  xpos RogueX.SpriteLoc yoffset 0
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Start Rogue 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

layeredimage Rogue_69_Animation:
    if Speed == 2:
        "Rogue_69_Anim2"
    elif Speed == 3:
        "Rogue_69_Anim3"
    elif Speed == 4:
        "Rogue_69_Anim4"
    elif Speed == 5:
        "Rogue_69_Anim5"
    elif Speed == 6:
        "Rogue_69_Anim6"
    elif Speed:
        "Rogue_69_Anim1"
    else:
        "Rogue_69_Static"
    align (0.6,0.0)
    pos (475,-800)#(475,-700)
    zoom 1.8#1/3
layeredimage Rogue_69_Body:
    if 'tits' in RogueX.Spunk and Player.Male:
        "images/RogueSex/Rogue_69_Spunk_Tits.png"
    if not RogueX.Uptop:
        Null()
    elif RogueX.Chest == 'bikini top':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Bikini.png")
    elif RogueX.Chest == 'sports bra':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Sports_Up.png")
    elif RogueX.Chest == 'lace bra':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Lace.png")
    elif RogueX.Chest == 'tube top':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Tube_Up.png")
    elif RogueX.Chest == 'tank':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Tank_Up.png")
    elif RogueX.Chest == 'buttoned tank':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Tank_Up.png")
    elif RogueX.Over == 'mesh top' and RogueX.Uptop:
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Mesh_Up.png")
    elif RogueX.Over == 'nighty' and RogueX.Uptop:
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Mesh_Up.png")
    "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Body.png"
    if RogueX.Uptop:
        Null()
    elif RogueX.Chest == 'bikini top':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Bikini.png")
    elif RogueX.Chest == 'sports bra':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Sports.png")
    elif RogueX.Chest == 'lace bra':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Lace.png")
    elif RogueX.Chest == 'tube top':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Tube.png")
    elif RogueX.Chest == 'tank':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Tank.png")
    elif RogueX.Chest == 'buttoned tank':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Chest_Tank2.png")
    if RogueX.Over == 'pink top' and RogueX.Uptop:
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Pink_Up.png")
    elif RogueX.Uptop:
        Null()
    elif RogueX.Over == 'towel':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Towel.png")
    elif RogueX.Over == 'pink top':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Pink.png")
    elif RogueX.Over == 'mesh top':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Mesh.png")
    elif RogueX.Over == 'nighty':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Over_Nighty.png")
    if not RogueX.Pierce:
        Null()
    elif RogueX.Pierce == 'ring':
        if RogueX.Uptop:
            "images/RogueSex/Rogue_69_Pierce_Tits_R.png"
        elif RogueX.Over == 'nighty':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_R_Nighty.png")
        elif RogueX.Over == 'pink top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_R_Pink.png")
        elif RogueX.Over == 'towel':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_R_Towel.png")
        elif RogueX.Over == 'mesh top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_R_Mesh.png")
        elif RogueX.Chest == 'sports bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_R_Sports.png")
        elif RogueX.Chest == 'tube top':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_R_Tube.png")
        elif RogueX.Chest == 'bikini top':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_R_Bikini.png")
        elif RogueX.Chest == 'lace bra':
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_R_Lace.png")
        elif RogueX.Chest:
            Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_R_Tank.png")
        else:
            "images/RogueSex/Rogue_69_Pierce_Tits_R.png"
    elif RogueX.Uptop:
        "images/RogueSex/Rogue_69_Pierce_Tits_B.png"
    elif RogueX.Over == 'nighty':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_B_Nighty.png")
    elif RogueX.Over == 'pink top':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_B_Pink.png")
    elif RogueX.Over == 'towel':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_B_Towel.png")
    elif RogueX.Over == 'mesh top':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_B_Mesh.png")
    elif RogueX.Chest == 'sports bra':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_B_Sports.png")
    elif RogueX.Chest == 'tube top':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_B_Tube.png")
    elif RogueX.Chest == 'bikini top':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_B_Bikini.png")
    elif RogueX.Chest == 'lace bra':
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_B_Lace.png")
    elif RogueX.Chest:
        Recolor("Rogue", "Chest", "images/RogueSex/Rogue_69_Pierce_Tits_B_Tank.png")
    else:
        "images/RogueSex/Rogue_69_Pierce_Tits_B.png"
    if not RogueX.Pierce:
        Null()
    elif RogueX.Uptop:
        Null()
    elif RogueX.Pierce == 'ring':
        if RogueX.Over == 'mesh top':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_R_Mesh.png")
        elif RogueX.Over == 'nighty':
            Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_R_Nighty.png")
    elif RogueX.Over == 'mesh top':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_B_Mesh.png")
    elif RogueX.Over == 'nighty':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Pierce_Tits_B_Nighty.png")
    if 'belly' in RogueX.Spunk and Player.Male:
        "images/RogueSex/Rogue_69_Spunk_Belly.png"
    zoom .8
    offset (145,150)#(250,210)#(175,175)
layeredimage Rogue_69_Head:
    if renpy.showing('Rogue_69_CUN') and Speed != 3:
        "images/RogueSex/Rogue_69_Tongue.png"
    elif Speed == 1:
        "images/RogueSex/Rogue_69_Tongue.png"
    always:
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Head.png"
    if 'mouth' in RogueX.Spunk and Player.Male:
        "images/RogueSex/Rogue_69_Spunk_Mouth.png"
    if Speed == 1 and Player.Male:
        Null()
    elif Speed == 4 and Player.Male:
        Null()
    elif Speed == 6 and Player.Male:
        Null()
    else:
        Recolor("Rogue", "Hair", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Hair_Over.png")
    if RogueX.Neck:
        "images/RogueSex/Rogue_69_Collar.png"
    zoom .8
    offset (145,150)
layeredimage Rogue_69_HairOver:
    Recolor("Rogue", "Hair", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Hair_Over.png")
    if RogueX.Neck:
        "images/RogueSex/Rogue_69_Collar.png"
    zoom .8
    offset (145,150)
layeredimage Rogue_69_HairBack:
    Recolor("Rogue", "Hair", "images/RogueSex/Rogue_69_Hair_Under.png")
    zoom .8
    offset (145,150)#(175,135)#(175,175)
layeredimage Rogue_69_Legs:
    if RogueX.Uptop:
        Null()
    elif RogueX.Over == 'nighty':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Legs_Nighty.png")
    elif RogueX.Over == 'towel':
        Recolor("Rogue", "Over", "images/RogueSex/Rogue_69_Legs_Towel.png")
    "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Legs.png"
    always:
        "Rogue_69_Anus"
    always:
        "Rogue_69_Pussy"
    if not RogueX.Wet:
        Null()
    elif (RogueX.Legs == 'yoga pants' or RogueX.Legs == 'shorts') and not RogueX.Upskirt:
        Null()
    elif RogueX.Panties and not RogueX.PantiesDown:
        Null()
    elif RogueX.Wet == 1:
        AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png")
    else:
        AlphaMask("Wet_Drip2_69","images/BetsySex/Betsy_69_Mask_Pussy.png")
    if 'anal' not in RogueX.Spunk or not Player.Male:
        Null()
    elif (RogueX.Legs == 'yoga pants' or RogueX.Legs == 'shorts') and not RogueX.Upskirt:
        Null()
    else:
        AlphaMask("Spunk_Drip_69_Anal","images/BetsySex/Betsy_69_Mask_Ass.png")
    if 'anal' in RogueX.Spunk:
        "images/BetsySex/Betsy_69_Spunk_Ass.png"
    if RogueX.PantiesDown:
        Null()
    elif RogueX.Panties == 'shorts' and RogueX.Wet > 1:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Legs_Shorts_Wet.png")
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Legs_Shorts.png")
    elif RogueX.Panties == 'lace panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Panties_Lace.png")
    elif RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Panties_Green.png")
    elif RogueX.Panties == 'green panties' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Panties_Green_Wet.png")
    elif RogueX.Panties == 'green panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Panties_Green.png")
    elif RogueX.Panties and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Panties_Black_Wet.png")
    elif RogueX.Panties:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Panties_Black.png")
    if RogueX.Hose == 'stockings and garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_StockingsGarter.png")
    elif RogueX.Hose == 'garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_Garter.png")
    elif RogueX.Hose == 'stockings':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_Stockings.png")
    if RogueX.Panties and RogueX.PantiesDown:
        Null()
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_Tights.png")
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_Tights_Holed.png")
    elif RogueX.Hose == 'pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_Pantyhose.png")
    elif RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Hose_Pantyhose_Holed.png")
    if RogueX.Acc == 'sweater':
        "images/RogueSex/Rogue_69_Sweater.png"
    if RogueX.Legs == 'skirt':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Skirt.png")
    elif RogueX.Upskirt:
        Null()
    elif RogueX.Legs == 'pants' and RogueX.Wet > 1:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Legs_Pants_Wet.png")
    elif RogueX.Legs == 'pants':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Legs_Pants.png")
    if not RogueX.Pierce:
        Null()
    elif RogueX.Pierce == 'ring':
        if Player.Sprite and Player.Cock == 'in':
            "images/RogueSex/Rogue_Sex_Pussy_RingF.png"
        elif (RogueX.Hose == 'pantyhose' or RogueX.Hose == 'tights') and not (RogueX.Panties and RogueX.PantiesDown):
            Null()
        elif RogueX.Legs == 'pants' and not RogueX.Upskirt:
            Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Pierce_Pussy_R_Black.png")
        elif RogueX.PantiesDown:
            "images/RogueSex/Rogue_Sex_Pussy_Ring.png"
        elif RogueX.Panties == 'bikini bottoms' or RogueX.Panties == 'green panties':
            Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Pierce_Pussy_R_Green.png")
        elif RogueX.Panties == 'shorts':
            Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Pierce_Pussy_R_Yellow.png")
        elif RogueX.Panties == 'lace panties':
            Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Pierce_Pussy_R_Lace.png")
        elif RogueX.Panties:
            Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Pierce_Pussy_R_Black.png")
        else:
            "images/RogueSex/Rogue_Sex_Pussy_Ring.png"
    elif Player.Sprite and Player.Cock == 'in':
        "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png"
    elif RogueX.Legs == 'shorts' and not RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Pierce_Pussy_B_Clothed.png")
    elif RogueX.Legs == 'pants' and not RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Pierce_Pussy_B_Clothed.png")
    elif (RogueX.Hose == 'pantyhose' or RogueX.Hose == 'tights') and not (RogueX.Panties and RogueX.PantiesDown):
        Null()
    elif RogueX.PantiesDown:
        "images/RogueSex/Rogue_Sex_Pussy_Barbell.png"
    elif RogueX.Panties == 'lace panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Pierce_Pussy_B_Lace.png")
    elif RogueX.Panties:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_69_Pierce_Pussy_B_Clothed.png")
    else:
        "images/RogueSex/Rogue_Sex_Pussy_Barbell.png"
    if Trigger == 'lick pussy' or Trigger2 == 'lick pussy':
        "Rogue_69_Lick_Pussy"
    elif Trigger == 'lick ass' or Trigger2 == 'lick ass':
        "Rogue_69_Lick_Ass"
    if RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60 and not (Player.Sprite):
        At("RogueFingerHand", GirlFingerPussyX())
    elif RogueX.Offhand == 'fondle pussy':
        At("RogueMastHand", GirlGropePussyX())
    elif Player.Sprite and Player.Cock:
        Null()
    elif Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy':
        "Rogue_Sex_Fondle_Pussy"
    if Player.Cock == 'foot':
        Null()
    elif Player.Sprite and Player.Cock == 'anal':
        AlphaMask("Rogue_69_Feet", "images/RogueSex/Rogue_69_Feet_Mask.png")
    elif renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex'):
        AlphaMask("Rogue_69_Feet", "images/RogueSex/Rogue_69_Feet_Mask.png")
    elif ShowFeet:
        "Rogue_69_Feet"
    else:
        AlphaMask("Rogue_69_Feet", "images/RogueSex/Rogue_69_Feet_Mask.png")
layeredimage Rogue_69_Feet:
    "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Feet.png"
    if (RogueX.Hose == 'pantyhose' or RogueX.Hose == 'ripped pantyhose') and RogueX.Panties and RogueX.PantiesDown:
        Recolor("Rogue", "Hose", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Feet.png")
    elif (RogueX.Hose == 'tights' or RogueX.Hose == 'ripped tights') and RogueX.Panties and RogueX.PantiesDown:
        Recolor("Rogue", "Hose", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Feet.png")
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Feet_Tights_Holed.png")
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Feet_Tights.png")
    elif RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_69_Feet_Hose_Holed.png")
    elif RogueX.Hose and RogueX.Hose != 'garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_69_Feet_Hose.png")
    else:
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Feet.png"
    if RogueX.Legs == 'pants' and RogueX.Upskirt:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Feet_Pants_Down.png")
    elif RogueX.Legs == 'pants':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_69_Feet_Pants.png")
image Rogue_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Rogue_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/RogueSex/Rogue_69_Pussy_Open.png",
                "RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60", "images/RogueSex/Rogue_69_Pussy_Open.png",
                "True", "images/RogueSex/Rogue_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not RogueX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Rogue", "Pubes", "images/RogueSex/Rogue_69_Pubes_Open.png"),
                "RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60", Recolor("Rogue", "Pubes", "images/RogueSex/Rogue_69_Pubes_Open.png"),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/Rogue_69_Pubes_Closed.png"),
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in RogueX.Spunk or not Player.Male", Null(),
                "(RogueX.Legs == 'yoga pants' or RogueX.Legs == 'shorts') and not RogueX.Upskirt", Null(),
                "RogueX.Panties and not RogueX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
#            offset (-700,-570)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in RogueX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in RogueX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in RogueX.Spunk", "images/RogueSex/Rogue_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "RogueX.Panties and RogueX.PantiesDown", Null(),
#                "RogueX.Hose == 'ripped pantyhose' and ShowFeet", "images/RogueSex/Rogue_Sex_Hose_Pantyhose_Holed.png",
#                "RogueX.Hose == 'ripped pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Rogue_Sex_Fucking_Zero_Anim3", "Rogue_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Rogue_Sex_Fucking_Zero_Anim2", "Rogue_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Rogue_Sex_Fucking_Zero_Anim1", "Rogue_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Rogue_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "RogueX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pierce_Pussy_BarbellF.png",
#                "RogueX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pierce_Pussy_RingF.png",
#                "RogueX.Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Pierce_Pussy_Barbell.png",
#                "RogueX.Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Rogue_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Rogue_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Rogue Pussy composite
image Spunk_Drip_69:
    contains:
        "Spunk_Drip2"
        rotate 180
        offset(-700,-500)
image Spunk_Drip_69_Anal:
    contains:
#        Solid("#159457", xysize=(1120,840))
        "Spunk_Drip2"
        rotate 180
        offset(-695,-450)
image Wet_Drip_69:
    contains:
        "Wet_Drip"
        rotate 180
        offset(-700,-500)
image Wet_Drip2_69:
    contains:
        "Wet_Drip2"
        rotate 180
        offset(-700,-500)
image Rogue_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (510,500)#(535,500
image Rogue_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (535,580)#(535,550)
image Rogue_69_Fondle_Pussy:
        "GropePussy_Rogue"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat
image Rogue_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/RogueSex/Rogue_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/RogueSex/Rogue_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Rogue_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Rogue_Sex_Anal_Tip",
            "RogueX.Plug", "images/PlugBase_Sex.png",
            "RogueX.Loose > 2", "Rogue_Gape_Anal_Sex",
            "RogueX.Loose", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Hole_Loose.png",
            "True", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Hole_Tight.png",
            "True", Null(),
            )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'anal' not in RogueX.Spunk or not Player.Male", Null(),
##                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/RogueSex/Rogue_Sex_Spunk_Anal_Under.png",
##                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Rogue_Sex_Anal_Spunk_Heading_Under",
#                "True", "images/RogueSex/Rogue_69_Spunk_Ass.png",
#                )
#            offset (5,0)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Rogue_Sex_Anal_Zero_Anim3", "Rogue_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Rogue_Sex_Anal_Zero_Anim2", "Rogue_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Rogue_Sex_Anal_Zero_Anim1", "Rogue_Sex_Anal_Mask"),
#                "True", AlphaMask("Rogue_Sex_Anal_Zero_Anim0", "Rogue_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Rogue_Sex_Anal_Spunk_Heading_Over",
#                "True", "Rogue_Sex_Anal_Spunk",
#                )


#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Static:
        #this is the animation for Rogue's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-65) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-70) #top
#                pause .5
                ease 1.25 pos (0,-65) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            subpixel True
            ConditionSwitch(
                "Player.Male and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#(675,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Rogue's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-65) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-70) #top
#                pause .5
                ease 1.25 pos (0,-65) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 0 (static)
#        contains:
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-20) #top
                pause .25
                ease 1 pos (0,-10) #bottom
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 0 (static)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Anim1:
        #this is the animation for Rogue's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (50,45) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (20,-60) #top(10,-30)
                pause .75#1.50
                ease 2.5 pos (50,45) #bottom(45,55)
                pause .5# 0
                repeat
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 rotate 180
#                pause 1.50
#                ease 2.25 rotate 210
#                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Zero_Blowcock"
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
        #this is the animation for Rogue's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 220
#            zoom .75
#            offset (180,50)#(180,100)
            pos (85,50) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (35,-65) #top (50,-65)
                pause .75#1.25
                ease 2.5 pos (85,50) #bottom (100,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 200
                pause 1.5
                ease 1.25 rotate 220
                pause 1.25
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Rogue_69_HairOver"
            rotate 190
#            zoom .75
#            offset (10,0)
#            offset (180,50)#(180,100)
            pos (50,45) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,-60) #top(10,-30)
                pause .7#.75
                ease 2.6 pos (50,40) #bottom(45,55)
                pause .45# 0
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause .5#1.50
                ease 2 rotate 190 #2.25
                pause 1.25#1.50
                repeat
#        contains:
#            subpixel True
#            "Rogue_69_Tits"
#            rotate 180
##            zoom .65
#            pos (30,40) #X less is left, Y less is up
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (10,-10) #top
#                pause 1.25
#                ease 2.5 pos (30,40) #bottom
#                repeat
        contains:
            subpixel True
            "Rogue_69_Body"
            rotate 180
#            zoom .65
#            alpha 0.5
            pos (30,50) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,-20) #top
                pause 1
                ease 2.5 pos (30,50) #bottom
                pause .25
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Rogue_69_Legs"
            rotate 185
            pos (0,25) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,25)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .25
                easein 1 rotate 180
                pause 1
                ease 2.75 rotate 185
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Anim2:
        #this is the animation for Rogue's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-60) #top
#                pause .5
                ease 1.25 pos (0,-30) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Rogue's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-60) #top
#                pause .5
                ease 1.25 pos (0,-30) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 2 (heading)
#        contains:
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-10) #top
                pause .25
                ease 1 pos (0,0) #bottom
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 2 (heading)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Anim3:
        #this is the animation for Rogue's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-20) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
#        #this is the animation for Zero's cock during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Rogue's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-20) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 3 (sucking)
#        contains:
#            subpixel True
#            "Rogue_69_Tits"
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
        #this is the animation for Rogue's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Rogue_69_Body"
            rotate 180
#            zoom .65
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,0) #top
#                pause .5
                ease 1.25 pos (0,40) #bottom
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Rogue_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 1.25 pos (0,10)
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Anim4:
        #this is the animation for Rogue's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,30) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Rogue's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,30) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        contains:
            subpixel True
            "Rogue_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,25) #top
                pause .5
                ease 1.75 pos (0,60) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Rogue_69_Tits"
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
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            rotate 180
#            zoom .65
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,35) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Rogue_69_Legs"
            rotate 180
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25)
#                pause .5
                ease 2.25 pos (0,30)
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Anim5:
        #this is the animation for Rogue's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-60) #top
#                pause .5
                ease 1.25 pos (0,-50) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Rogue's head during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-50) #top
#                pause .5
                ease 1.25 pos (0,-40) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 5 (cum high)
#        contains:
#            "Rogue_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,-10) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .5
#                easein 1.75 pos (0,-20) #top
##                pause .5
#                ease 1.25 pos (0,-10) #bottom
#                repeat
        contains:
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein 1.75 pos (0,-10) #top
#                pause .5
                ease 1.25 pos (0,0) #bottom
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 5 (cum high)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein 1.75 pos (0,-5)
                pause .5
                ease 1.25 pos (0,0)
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Anim6:
        #this is the animation for Rogue's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,50) #top
                pause .5
                ease 1.75 pos (0,60) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Rogue's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,50) #top
                pause .5
                ease 1.75 pos (0,60) #bottom
                repeat
        contains:
            subpixel True
            "Rogue_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,55) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,40) #top
                pause .5
                ease 1.75 pos (0,55) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 6 (cum deep)
#        contains:
#            subpixel True
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            rotate 180
#            zoom .65
            pos (0,65) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,55) #top
                pause .5
                ease 1.75 pos (0,65) #bottom
                repeat
        #this is the animation for Rogue's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Rogue_69_Legs"
            rotate 180
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25)
#                pause .5
                ease 2.25 pos (0,30)
                repeat

#End Animations for Rogue's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Rogue 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Rogue's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
layeredimage Rogue_69_CUN:
    if Speed == 2:
        "Rogue_69_Cun2"
    elif Speed == 3:
        "Rogue_69_Cun3"
    elif Speed:
        "Rogue_69_Cun1"
    else:
        "Rogue_69_Cun0"
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3
image Rogue_69_Cun0:
        #this is the animation for Rogue's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-50) #(15,-20)X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-45) #top
#                pause .5
                ease 1.25 pos (10,-50) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        #this is the animation for Rogue's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-50) #(15,-20)X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-45) #top
#                pause .5
                ease 1.25 pos (10,-50) #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 0 (static)
#        contains:
#            "Rogue_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (10,-20) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (10,-25) #top
#                pause .25
#                ease 1 pos (10,-20) #bottom
#                repeat
        contains:
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (5,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (5,-5) #top
                pause .25
                ease 1 pos (5,0) #bottom
                repeat

#            subpixel True
#            "Rogue_69_Body"
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
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Rogue's lower body during 69, Speed 0 (static)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Cun1:
        #this is the animation for Rogue's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                ease 1.0 ypos -35 #top
                easeout .5 ypos -45 #top
                easein 1.0 ypos -50 #bottom
                pause .5
                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (lick)
        contains:
            #pussy
            "Zero_Pussy"
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
        #this is the animation for Rogue's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-50) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -35 #top
                easeout .5 ypos -45 #top
                easein 1.0 ypos -50 #bottom
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
        #this is the animation for Rogue's upper body during 69, Speed 1 (lick)
#        contains:
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (10,-5) #top
                pause .25
                ease 1.25 pos (10,0) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Rogue's lower body during 69, Speed 1 (lick)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat


#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Cun2:
        #this is the animation for Rogue's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-40) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -35 #top
                easein 1.1 ypos -40 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.3
                easein .9 rotate 185 #top
                easein 0.8 rotate 175 #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (clit)
        contains:
            #pussy
            "Zero_Pussy"
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
        #this is the animation for Rogue's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-40) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -35 #top
                easein 1.1 ypos -40 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.2
                easein .8 rotate 185 #top
                easein 1.0 rotate 175 #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 2 (clit)
#        contains:
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-5) #top
                ease 1 pos (10,0) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Rogue's lower body during 69, Speed 2 (clit)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_69_Cun3:
        #this is the animation for Rogue's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Rogue_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-25) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 ypos -30 #top
#                pause .5
                ease 1.25 ypos -25 #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 3 (suck)
        contains:
            #pussy
            "Zero_Pussy"
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
        #this is the animation for Rogue's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Rogue_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-25) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 ypos -30 #top
#                pause .5
                ease 1.25 ypos -25 #bottom
                repeat
        #this is the animation for Rogue's upper body during 69, Speed 3 (suck)
#        contains:
#            "Rogue_69_Tits"
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
            "Rogue_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-5) #top
                pause .25
                ease 1 pos (10,0) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Rogue's lower body during 69, Speed 3 (suck)
        contains:
            "Rogue_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
#End Animations for Rogue's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Rogue 69 Animations

# Start Rogue Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
layeredimage Rogue_SC_Sprite:
    if Speed >= 2:
        "Rogue_SC_Anim_2"
    elif Speed:
        "Rogue_SC_Anim_1"
    else:
        "Rogue_SC_Anim_0"
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8
layeredimage Rogue_SC_Legs:
    always:
        "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Legs.png"
    if RogueX.Water:
        "images/RogueSex/Rogue_Sex_Wet_Legs.png"
    always:
        "Rogue_SC_Pussy"
    if not RogueX.Panties or RogueX.PantiesDown:
        Null()
    elif Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal'):
        Null()
    elif RogueX.Panties == 'lace panties':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Lace.png")
    elif RogueX.Panties == 'green panties' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Green_Wet.png")
    elif RogueX.Panties == 'green panties' or RogueX.Panties == 'bikini bottoms':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Green.png")
    elif RogueX.Panties == 'shorts' and RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Shorts_Wet.png")
    elif RogueX.Panties == 'shorts':
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Shorts.png")
    elif RogueX.Wet:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Black_Wet.png")
    else:
        Recolor("Rogue", "Panties", "images/RogueSex/Rogue_Sex_Panties_Black.png")
    if RogueX.Hose == 'ripped pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Full_Hole.png")
    elif RogueX.Hose == 'ripped tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Hole.png")
    elif RogueX.Hose == 'stockings':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Stockings.png")
    elif RogueX.Hose == 'stockings and garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_StockingGarter.png")
    elif RogueX.Hose == 'garterbelt':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Garter.png")
    elif RogueX.PantiesDown:
        Null()
    elif Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal'):
        Null()
    elif RogueX.Hose == 'pantyhose':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Full.png")
    elif RogueX.Hose == 'tights' and RogueX.Wet:
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Wet.png")
    elif RogueX.Hose == 'tights':
        Recolor("Rogue", "Hose", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights.png")
    if RogueX.Legs == 'skirt':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Skirt.png")
    elif RogueX.Upskirt:
        Null()
    elif RogueX.Legs == 'pants' and RogueX.Wet > 1:
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Pants_Wet.png")
    elif RogueX.Legs == 'pants':
        Recolor("Rogue", "Legs", "images/RogueSex/Rogue_Sex_Legs_Pants.png")
    if RogueX.Acc == 'sweater':
        "images/RogueSex/Rogue_Sex_Sweater.png"
    if 'belly' in RogueX.Spunk and Player.Male:
        "images/KittySex/Kitty_Sex_Spunk_Pelvis.png"
    if Player.Sprite:
        Null()
    elif Trigger == 'lick pussy':
        "Rogue_Sex_Lick_Pussy"
    elif Trigger == 'lick ass':
        "Rogue_Sex_Lick_Ass"
    elif RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60:
        At("RogueFingerHand", GirlFingerPussyX())
    elif RogueX.Offhand == 'fondle pussy':
        At("RogueMastHand", GirlGropePussyX())
image Rogue_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Closed.png",
                "'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand)", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
#                "Trigger == 'dildo pussy'", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Fucking.png",
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
                "True", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Closed.png",
                )
#    contains:
#            # growing pussy hole
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Rogue_Sex_Pussy_Hole",#"images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pussy_Open.png",
#                "True", Null(),
#                )
    contains:
            # wet pussy
            ConditionSwitch(
                "not RogueX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "RogueX.Pierce != 'ring'", Null(),
#                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                )
    contains:
            #barbell piercing
            ConditionSwitch(
                "RogueX.Pierce != 'barbell'", Null(),
#                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Closed.png"),
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
#                "'dildo pussy' in (Trigger,Trigger2,RogueX.Offhand)", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                "RogueX.Offhand == 'fondle pussy' and RogueX.Lust > 60", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Open.png"),
#                "Trigger == 'dildo pussy'", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Fucking.png"),
                "True", Recolor("Rogue", "Pubes", "images/RogueSex/[RogueX.skin_image.skin_path]Rogue_Sex_Pubes_Closed.png"),
                )

    #End Rogue Pussy composite

#End Animations for Rogue's Pussy during SC / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# End Rogue Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_SC_Anim_0:
        #this is the animation for Rogue's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (40,50) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (40,60)
                pause .5
                ease 2 pos (40,50)
                pause .5
                repeat
        contains:
            subpixel True
            "Rogue_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 30
                pause .5
                ease 2 rotate 35
                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate -15
            offset (925,740)#(910,850)
        contains:
            subpixel True
#            "Rogue_Sex_Feet"
            ConditionSwitch(
                #Shows different lower body motion depending on events
                "ShowFeet", "Rogue_Sex_Feet",
                "True", AlphaMask("Rogue_Sex_Feet","images/RogueSex/Rogue_Sex_FeetMask2.png")
                )
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 30
                pause .5
                ease 2 rotate 35
                repeat
        #end animation for Rogue's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_SC_Anim_1:
        #this is the animation for Rogue's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (40,60) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (40,70)
                pause .5
                ease 1 pos (40,60)
                pause .5
                repeat
        contains:
            subpixel True
            "Rogue_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
#                pause .5
                ease 1.5 rotate 30
#                pause .5
                ease 1.5 rotate 35
                repeat
            parallel:
                ease 1 pos (0,20)
                pause .5
                ease 1 pos (0,-10)
                pause .5
                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate -15
            offset (925,740)#(910,850)
            parallel:
                pause .5
                ease 1 pos (0,-5)
                pause .5
                ease 1 pos (0,0)
                repeat
        contains:
            subpixel True
#            "Rogue_Sex_Feet"
            ConditionSwitch(
                #Shows different lower body motion depending on events
                "ShowFeet", "Rogue_Sex_Feet",
                "True", AlphaMask("Rogue_Sex_Feet","images/RogueSex/Rogue_Sex_FeetMask2.png")
                )
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
#                pause .5
                ease 1.5 rotate 30
#                pause .5
                ease 1.5 rotate 35
                repeat
            parallel:
                ease 1 pos (0,20)
                pause .5
                ease 1 pos (0,-10)
                pause .5
                repeat
        #End animation for Rogue's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_SC_Anim_2:
        #this is the animation for Rogue's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (30,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (30,90)
                ease .5 pos (30,80)
                repeat
        contains:
            subpixel True
            "Rogue_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
                ease .5 rotate 30
                pause .1
                ease .5 rotate 35
                repeat
            parallel:
                ease .5 pos (0,20)
                ease .5 pos (0,-10)
                pause .1
                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate -15
            offset (925,740)#(910,850)
            parallel:
                ease .5 pos (0,-5)
                ease .5 pos (0,0)
                pause .1
                repeat
        contains:
            subpixel True
#            "Rogue_Sex_Feet"
            ConditionSwitch(
                #Shows different lower body motion depending on events
                "ShowFeet", "Rogue_Sex_Feet",
                "True", AlphaMask("Rogue_Sex_Feet","images/RogueSex/Rogue_Sex_FeetMask2.png")
                )
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
                ease .5 rotate 30
                pause .1
                ease .5 rotate 35
                repeat
            parallel:
                ease .5 pos (0,20)
                ease .5 pos (0,-10)
                pause .1
                repeat
        #End animation for Rogue's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Rogue_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Rogue_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(RogueX,1) #call Rogue_Hide
    show Rogue_SC_Sprite zorder 150
    with dissolve
    return

label Rogue_SC_Reset:
    if not renpy.showing("Rogue_SC_Sprite"):
        return
    $ RogueX.ArmPose = 2
    hide Rogue_SC_Sprite
    call Girl_Hide(RogueX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Rogue Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Start Rogue view-shifting  stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Kissing_Launch(T = Trigger,Set=1):
    call Rogue_Hide
    $ Trigger = T
    $ RogueX.Pose = "kiss" if Set else RogueX.Pose
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer
    show Rogue_Sprite at SpriteLoc(StageCenter) zorder 150:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Rogue_Kissing_Smooch:
    $ RogueX.FaceChange("kiss")
    show Rogue_Sprite at SpriteLoc(StageCenter) zorder 150:
            offset (0,0)
            alpha 1
            ease 0.5 xpos StageCenter zoom 2
            pause 1
            ease 0.5 xpos RogueX.SpriteLoc zoom 1
    pause 1
    $ RogueX.FaceChange("sexy")
    return

label Rogue_Breasts_Launch(T = Trigger,Set=1):
    call Rogue_Hide
    $ Trigger = T
    $ RogueX.Pose = "breasts" if Set else RogueX.Pose
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1
    return

label Rogue_Middle_Launch(T = Trigger,Set=1):
    call Rogue_Hide
    $ Trigger = T
    $ RogueX.Pose = "mid" if Set else RogueX.Pose
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Rogue_Pussy_Launch(T = Trigger,Set=1):
    call Rogue_Hide
    $ Trigger = T
    $ RogueX.Pose = "pussy" if Set else RogueX.Pose
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
        ease 0.5 pos (700,-400) zoom 2 offset (0,0) alpha 1
    return

#transform Feet(XPOS=700,YPOS=350,ZM=1):
#        #this positions girls in a small state
#        alpha 1
#        rotate 0
#        zoom ZM
#        pos (XPOS,YPOS)#(700,150)#(0,50)
##        offset (700,100)#(XPOS,YPOS)

label Girl_Feet_Launch(Girl=0,T = Trigger):
    $ Trigger = T
    call Girl_Hide(Girl,0)
    $ renpy.show(Girl.Tag+"_Sprite",at_list=[Feet_View()],zorder=Girl.Layer)
    return

transform Feet_View():
    ease 0.5 pos (500,-850) zoom 1.5 offset (0,0) alpha 1


label Rogue_Pos_Reset(T = 0,Set=0):
    if RogueX.Loc != bg_current:
            return
    call Rogue_Hide
    show Rogue_Sprite at SpriteLoc(RogueX.SpriteLoc) zorder RogueX.Layer:
            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Rogue_Sprite zorder RogueX.Layer:
            offset (0,0)
            anchor (0.5, 0.0)
            zoom 1
            xzoom 1
            yzoom 1
            alpha 1
            pos (RogueX.SpriteLoc,50)
    $ RogueX.Pose = "full" if Set else 0
    $ Trigger = T
    return

label Rogue_Hide(Sprite=0):
#    call Rogue_Sex_Reset
    hide Rogue_SexSprite
    hide Rogue_Doggy_Animation
    hide Rogue_HJ_Animation
    hide Rogue_BJ_Animation
    hide Rogue_TJ_Animation
    hide Rogue_Finger_Animation
    hide Rogue_CUN_Animation
    hide Rogue_69_Animation
    hide Rogue_69_CUN
    hide Rogue_Seated
    if Sprite:
            hide Rogue_Sprite
    return

label Girl_Smol_Launch(Girl=0,Set=1):
    call Girl_Hide(Girl)
    $ Girl.Pose = "smol" if Set else Girl.Pose
    $ renpy.show(Girl.Tag+"_Sprite",at_list=[Smol],zorder=Girl.Layer)
    return

# End Rogue view-shifting  stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Interface items  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Vibrate():
    subpixel True
    block:
        linear .5 xoffset 2
        linear .5 xoffset -2
        repeat


image UI_Vibrator:
    LiveComposite(
        (224,224),
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA",
            "Vibration", At("UI_VibB", Vibrate()),
            ),
        )
image GropeLeftBreast:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat
image GropeRightBreast:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.7
        xzoom -0.7
        pos (180,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat
image LickRightBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -45 pos (150,370)
            pause .5
            ease 1.5 rotate 30 pos (160,400)
            repeat
image LickLeftBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)#(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -45 pos (260,380)#(150,370)
            pause .5
            ease 1.5 rotate 30 pos (280,410)#(160,400)
            repeat
image GropeThigh:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat
image GropePussy:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (220,620)
                ease .75 rotate 170 pos (220,635)
            choice:
                ease .5 rotate 190 pos (220,620)
                pause .25
                ease 1 rotate 170 pos (220,635)
            repeat
image FingerPussy:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.7
        pos (230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease .5 rotate 40 pos (240,685)
                pause .5
                ease 1.75 rotate 50 pos (230,720)
            choice:
                ease 2 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
            repeat
image Lickpussy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (250,670)#(0.5,0.5)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (230,650)
            linear .5 rotate -60 pos (220,660)
            easein 1 rotate 10 pos (250,670)
            repeat
image VibratorRightBreast:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380
            pause .25
            repeat
image VibratorLeftBreast:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400
            pause .25
            repeat
image VibratorPussy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665
            pause .25
            repeat
image VibratorAnal:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat
image VibratorPussyInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0
image VibratorAnalInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
image TestUIAnimation:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat

#Lesbian action animations.
image GirlGropeLeftBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6#.7
        pos (300,400)#(300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (280,390)
            ease 1 rotate -20 pos (300,400)
            repeat
image GirlGropeRightBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (160,380) #(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat
image GirlGropeThigh:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat
image GirlGropePussy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (230,615)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (225,620)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
            choice: #Fast stroke
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
            repeat
image GirlFingerPussy:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (230,630)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (230,635)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
            choice: #Fast stroke
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
            repeat
transform GirlGropePussyX():
        #used in the sex poses for the girl masturbating
        subpixel True
        anchor (0.70,0.70)
        transform_anchor True
        block:
            choice: #fast rub
                ease .75 rotate 5 offset (0,0)
                ease .5 rotate 0
                ease .75 rotate 5
                ease .5 rotate 0
            choice: #slow rub
                ease .5 rotate 5 offset (0,0)
                ease 1 rotate 0
                pause .25
                ease .5 rotate 5
                ease 1 rotate 0
                pause .25
            choice: #slow stroke
                ease .5 rotate 5 offset (0,0)
                ease .75 rotate 0 offset (0,5)
                ease .5 rotate 5 offset (0,0)
                ease .75 rotate 0 offset (0,5)
            choice: #Fast stroke
                ease .3 rotate 5 offset (0,0)
                ease .3 rotate 0 offset (0,10)
                ease .3 rotate 5 offset (0,0)
                ease .3 rotate 0 offset (0,10)
            repeat


transform GirlFingerPussyX():
        #used in the sex poses for the girl masturbating at high Lust
        subpixel True
        anchor (0.70,0.70)
        transform_anchor True
        rotate 0
        block:
            choice: #fast rub
                ease .75 rotate 5 offset (0,0)
                ease .5 rotate 0
                ease .75 rotate 5
                ease .5 rotate 0
            choice: #slow rub
                ease .5 rotate 5 offset (0,0)
                ease 1 rotate 0
                pause .25
                ease .5 rotate 5
                ease 1 rotate 0
                pause .25
            choice: #slow stroke
                ease .5 offset (0,-15)
                ease .75 offset (0,0)
                ease .5 offset (0,-15)
                ease .75 offset (0,0)
                repeat 2
            choice: #Fast stroke
                ease .3 offset (0,-15)
                ease .3 offset (0,0)
                ease .3 offset (0,-15)
                ease .3 offset (0,0)
                repeat 2
            repeat

image RogueMastHand:
        "images/UI_GirlHand_Rogue.png"
        zoom 0.9
        rotate 240
        offset (365,220)
image RogueFingerHand:
        "images/UI_GirlFinger_Rogue.png"
        zoom 0.9
        rotate 220
        offset (333,300)
image Lick_Anim:
    anchor (0.5, 0.5)
    parallel: #total 2.6
        "images/Lick1.png"
        .8
        "images/Lick6.png"
        .2
        "images/Lick2.png"
        .2
        "images/Lick3.png"
        .2
        "images/Lick4.png"
        .8
        "images/Lick3.png"
        .1
        "images/Lick2.png"
        .1
        repeat
    parallel: #total 2.6
        pause .6
        easein .7 yoffset -15
        pause .3
        easein .8 yoffset 0
        repeat
image Lick_AnimF:
    anchor (0.5, 0.5)
    parallel: #total 2.6
        "images/Lick1.png"
        .8
        "images/Lick6.png"
        .2
        "images/Lick2.png"
        .2
        "images/Lick3.png"
        .2
        "images/Lick4.png"
        .8
        "images/Lick3.png"
        .1
        "images/Lick2.png"
        .1
        repeat
    parallel: #total 2.6
        pause .6
        easein .7 yoffset 0
        pause .3
        easein .8 yoffset -15
        repeat
label Close_Launch(GirlA=0,GirlB=0,XLoc=0,YLoc=0,XZoom=0,BO=[]):  #rkeljsvg
    # Launches the girls close to player
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if GirlB:
            $ BO = [GirlA,GirlB]
    elif GirlA:
            $ BO = [GirlA]
    while BO:
            if BO[0] is KittyX or BO[0] is LauraX:
                $ BO[0].ArmPose = 1
            else:
                $ BO[0].ArmPose = 2
            $ YLoc = 100
            if GirlA == BO[0]:
                    #If this girl is lead
                    if BO[0] is KittyX:
                        $ XLoc = 450
                    elif BO[0] is WandaX or BO[0] is BetsyX:
                        $ XLoc = 400
                    elif BO[0] is RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500
                    $ BO[0].Layer = 100
                    $ XZoom = -1.3
            elif GirlB == BO[0]:
                    #If the other girl is lead
                    if BO[0] is EmmaX or BO[0] is LauraX:
                        $ XLoc = 700
                    elif BO[0] is WandaX:
                        $ XLoc = 750
                    else:
                        $ XLoc = 715
                    $ BO[0].Layer = 75
                    $ XZoom = 1.3

            call Girl_Hide(BO[0],0)
            $ renpy.show(BO[0].Tag+"_Sprite",at_list=[CloseZoom(XLoc,YLoc,XZoom=XZoom)],zorder=BO[0].Layer)
            $ BO.remove(BO[0])
    return

transform CloseZoom(XLoc=715,YLoc=50,XZoom=.2):
        #The animation for the heading mouth
        pos (XLoc,YLoc) alpha 1 zoom 1 xzoom XZoom yzoom 1.3 offset (0,0) anchor (0.5, 0.0)

transform Smol(XPOS=700,YPOS=150,ZM=0.55):
        #this positions girls in a small state
        alpha 1 zoom ZM pos (XPOS,YPOS)#(700,150)#(0,50)
#        offset (700,100)#(XPOS,YPOS)

transform Feet(XPOS=700,YPOS=350,ZM=1):
        #this positions girls in a small state
        alpha 1 zoom ZM pos (XPOS,YPOS)#(700,150)#(0,50)
#        offset (700,100)#(XPOS,YPOS)

#label QuickReset(Girl=0): #rkeljsvgbdw
#    if RogueX == Girl:
#                call Girl_Pos_Reset(RogueX)
#    if KittyX == Girl:
#                call Girl_Pos_Reset(KittyX)
#    if EmmaX == Girl:
#                call Girl_Pos_Reset(EmmaX)
#    if LauraX == Girl:
#                call Girl_Pos_Reset(LauraX)
#    if JeanX == Girl:
#                call Girl_Pos_Reset(JeanX)
#    if StormX == Girl:
#                call Girl_Pos_Reset(StormX)
#    return

label Les_Launch(Girl=0,XLoc=0,YLoc=0,XZoom=0,BO=[]): #rkeljsvgbdw
    # Launches the lesbian sex positions
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if Partner not in TotalGirls:
            return
#    if Girl is BetsyX or Girl is DoreenX:
#            pass        #remove when they have doggy poses. . .
    if Trigger == "lesbian" and Girl.Offhand == "lick girl pussy":
            call Les_Launch_Doggy(Girl)
            return
    $ BO = [Girl,Partner]
    while BO:
            if "unseen" in BO[0].RecentActions:
                        $ BO[0].Eyes = "closed"
#            elif Girl == BO[0]:
#                if Girl is RogueX:
#                        $ BO[0].Eyes = "side"
#                elif Girl is EmmaX:
#                        $ BO[0].Eyes = "sly"
#                else:
#                        $ BO[0].Eyes = "leftside"
            else:
                        $ BO[0].Eyes = "side"

            if BO[0] is KittyX or BO[0] is LauraX:
                $ BO[0].ArmPose = 1
            else:
                $ BO[0].ArmPose = 2
            $ YLoc = 100
            if Girl == BO[0]:
                    #If this girl is lead
                    if BO[0] is KittyX:
                        $ XLoc = 550
                    elif BO[0] is RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500
                    $ BO[0].Layer = 100
                    $ XZoom = -1.3
            else: #Partner == BO[0]:
                    #If the other girl is lead
#                    if BO[0] is EmmaX or BO[0] is LauraX:
#                        $ XLoc = 700
#                    else:
                    $ XLoc = 715
                    if BO[0] is KittyX:
                            if RogueX in (Partner,Girl):
                                    $ KittyX.Layer = 100
                            else:
                                    $ KittyX.Layer = 25
                    else:
                                    $ BO[0].Layer = 75
                    $ XZoom = 1.3

            call Girl_Hide(BO[0],0)
            $ renpy.show(BO[0].Tag+"_Sprite",at_list=[Sprite_Set(XLoc,YLoc,XZM=XZoom,YZM=1.3)],zorder=BO[0].Layer)

#            if BO[0] is RogueX:
#                    call Rogue_Hide
#                    show Rogue_Sprite at SpriteLoc(XLoc,YLoc) zorder RogueX.Layer:
#                            alpha 1 zoom 1 xzoom XZoom yzoom 1.3 offset (0,0) anchor (0.5, 0.0)
            $ BO.remove(BO[0])
    return

transform Ease_Low():
        # Lowers girl during threesome actions, called from Threesome_Set
        ease 1 ypos 200

label Les_Launch_Doggy(Girl=0,XLoc=530,BO=[]): #rkeljs
    # Launches the lesbian sex doggy
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if Partner not in TotalGirls or Girl not in TotalGirls:
            return
    $ BO = [Partner,Girl]
#    if Girl == GwenX:
#            #fix, temporary until I have a doggy pose for her
#            return
#            $ BO[0].Upskirt = 1


    if BO[0] is RogueX:
            $ XLoc = 525
    elif BO[0] is KittyX:
            $ XLoc = 505
    elif BO[0] is EmmaX:
            $ XLoc = 540
    elif BO[0] is LauraX:
            $ XLoc = 490
    elif BO[0] is JeanX:
            $ XLoc = 530
    elif BO[0] is StormX:
            $ XLoc = 480
    elif BO[0] is JubesX:
            $ XLoc = 550
    elif BO[0] is GwenX:
            $ XLoc = 540
    elif BO[0] is BetsyX:
            $ XLoc = 430#460
    elif BO[0] is DoreenX:
            $ XLoc = 500
    elif BO[0] is WandaX:
            $ XLoc = 450


    call Girl_Hide(BO[0],1)
    $ renpy.show(BO[0].Tag+"_Sprite",at_list=[Sprite_Set(XLoc,0,ZM=1.1,XZM=-1)],zorder=BO[0].Layer)


#    if BO[0] is RogueX:
#            call Rogue_Hide(1)
#            show Rogue_Sprite at SpriteLoc(525,0) zorder RogueX.Layer:
#                    alpha 1 zoom 1.1 xzoom -1 offset (0,0) anchor (0.5, 0.0)
    #than show main girl in foreground
    $ Girl.Facing = 1
    $ Speed = 0


    call Girl_Hide(BO[1],1)


    if BO[1] is RogueX:
            show Rogue_Doggy_Animation at Sprite_Set(600,400,1,0.85) zorder 150
    elif BO[1] is KittyX:
            show Kitty_Doggy_Animation at Sprite_Set(700,280,1,0.9) zorder 150
    elif BO[1] is EmmaX:
            show Emma_Doggy_Animation at Sprite_Set(620,370,1,1) zorder 150
    elif BO[1] is LauraX:
            show Laura_Doggy_Animation at Sprite_Set(650,380,1,0.8) zorder 150
    elif BO[1] is JeanX:
            show Jean_Doggy_Animation at Sprite_Set(650,330,1,0.95) zorder 150
    elif BO[1] is StormX:
            show Storm_Doggy_Animation at Sprite_Set(740,360,1,0.95) zorder 150
    elif BO[1] is JubesX:
            show Jubes_Doggy_Animation at Sprite_Set(650,350,1,0.85) zorder 150
    elif BO[1] is GwenX:
            show Gwen_Doggy_Animation at Sprite_Set(600,330,1,0.9) zorder 150
    elif BO[1] is BetsyX:
            show Betsy_Doggy_Animation at Sprite_Set(600,350,1,0.95) zorder 150
    elif BO[1] is DoreenX:
            show Doreen_Doggy_Animation at Sprite_Set(600,240,1,0.95) zorder 150
    elif BO[1] is WandaX:
            show Wanda_Doggy_Animation at Sprite_Set(550,320,1,0.95) zorder 150
    return
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Start Anal Plug Doggy in/out < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Anal_Plug_In_Doggy:
        #inserting an anal plug
        contains:
            #Hole
            ConditionSwitch(
                "renpy.showing('Storm_Doggy_Animation') and Partner != StormX", "images/StormDoggy/Storm_Doggy_Anal_FullHole.png",
                "True", "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png",
                )
#            "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
            transform_anchor True
            anchor (0.52,0.69)
            offset (0,0)#(218,518)
            zoom .35 # tight
            block:
                ease 2.2 zoom .87 #in
                ease .3 zoom .6 #out
        contains:
            AlphaMask("Anal_Plug_Tip_Insert_Doggy", "Anal_Plug_Tip_Mask_Insert_Doggy")
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,0)
        contains:
            "images/RogueDoggy/Rogue_Doggy_Plug.png"
            anchor (0.5,0.5)
            transform_anchor True
            offset (-6,-120) #plug inserted
            alpha 1
            block:
                ease 2.5 yoffset -160 #in (-6,-145)
        pos (1076+Plug_Mod[0],1330+Plug_Mod[1]) #(1100,1300)
image Anal_Plug_Tip_Insert_Doggy:
            #the anal plug insert
#        contains:
#            Solid("#159457", xysize=(420,750))
#            alpha 0.1
#    #        offset (0,0)
#            offset (400,300)#(500,300) #pos (218,518)
        contains:
            "images/RogueDoggy/Rogue_Doggy_PlugTip.png"
            anchor (0.52,0.69)
            transform_anchor True
            offset (515,410) #out
            zoom 1 #in
            parallel:
                ease 2.5 yoffset 370 #in
            parallel:
                pause 2.2
                ease .3 zoom .5 #out
image Anal_Plug_Tip_Mask_Insert_Doggy:
        #the masking animation for the anal plug insert
        contains:
            "images/Anal_Plug_Mask.png"
            transform_anchor True
            anchor (0.52,0.69)
            offset (513,390) #(500,385) #pos (218,518)
            zoom .5 # in
            block:
                ease 2.2 zoom 1 #in
                ease .3 zoom .7 #out

#End Anal Plug Doggy insertion  animations < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

#Start Anal Plug Doggy removal animations
image Anal_Plug_Out_Doggy:
        #removing an anal plug
        contains:
            #Hole
            ConditionSwitch(
                "renpy.showing('Storm_Doggy_Animation') and Partner != StormX", "images/StormDoggy/Storm_Doggy_Anal_FullHole.png",
                "True", "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png" ,
                )
#            "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
            transform_anchor True
            anchor (0.52,0.69)
            offset (0,0)#(218,518)
            zoom .6 # loose
            block:
                ease .3 zoom .87 #in
                ease 2.2 zoom .35 #out
#                ease .5 alpha 0
        contains:
            AlphaMask("Anal_Plug_Tip_Out_Doggy", "Anal_Plug_Tip_Mask_Out_Doggy")
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,0)
        contains:
            "images/RogueDoggy/Rogue_Doggy_Plug.png"
            anchor (0.5,0.5)
            transform_anchor True
            offset (-6,-160) #plug inserted
            alpha 1
            block:
                ease 2.5 yoffset -120 #out (-6,-110)
                ease 1 yoffset -70 alpha 0
        pos (1076+Plug_Mod[0],1330+Plug_Mod[1]) #(1100,1300)
image Anal_Plug_Tip_Out_Doggy:
            #the anal plug being removed
        contains:
            "images/RogueDoggy/Rogue_Doggy_PlugTip.png"
#            anchor (0.5,0.5)
            anchor (0.52,0.69)
            transform_anchor True
            offset (515,370) #out
            zoom 0.5 #in
            parallel:
                ease 2.5 yoffset 410 #out
                ease 1 yoffset 460 alpha 0
            parallel:
                ease .3 zoom 1 #in
                pause 2.2
image Anal_Plug_Tip_Mask_Out_Doggy:
        #the masking animation for the anal plug removal
        contains:
            "images/Anal_Plug_Mask.png"
            transform_anchor True
            anchor (0.52,0.69)
            offset (513,390) #(500,385) #pos (218,518)
            zoom .7 # in
            block:
                ease .3 zoom 1 #in
                ease 2.2 zoom .5 #out
#End Anal Plug Doggy removal animations < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start Anal Plug in/out Sex (Rogue,Kitty,Laura,Jubes)< < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Anal_Plug_In_Sex:
        #inserting an anal plug
        contains:
            #Hole
            "images/JubesSex/Jubes_Sex_Anal.png"
            transform_anchor True
            anchor (560,620)#(0.52,0.69)
#            offset (0,33)#(218,518)
            offset (0,28)#(218,518)
            zoom .35 # tight
            block:
                ease 2.0 zoom 1.1 #in.87
                pause 0.2
                ease .3 zoom .6 #out
        contains:
            AlphaMask("Anal_Plug_Tip_Insert_Sex", "Anal_Plug_Tip_Mask_Insert_Sex")
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,0)
        contains:
            "images/PlugBase_Sex.png"
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,-90)#(-6,-120) #plug inserted
            alpha 1
            block:
                ease 2.5 yoffset -160 #in (-6,-145)
        pos (990+Plug_Mod[0],1347+Plug_Mod[1])        #(1076+Plug_Mod,1330)
        zoom 0.85
#        pos (500,500)
image Anal_Plug_Tip_Insert_Sex:
            #the anal plug insert
#        contains:
#            Solid("#159457", xysize=(420,750))
#            alpha 0.95
#    #        offset (0,0)
#            offset (400,300)#(500,300) #pos (218,518)
        contains:
            "images/PlugTip_SexF.png"
            anchor (560,620)#(0.52,0.69)
            transform_anchor True
            offset (513,485) #out(515,485)
            zoom .85 #in
#            alpha .5
            parallel:
                ease 2.5 yoffset 420 #in430
            parallel:
                pause 2.2
                ease .3 zoom .5 #out
image Anal_Plug_Tip_Mask_Insert_Sex:
        #the masking animation for the anal plug insert
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            anchor (560,620)#(0.52,0.69)
            transform_anchor True
            offset (515,419) #out(515,485)
            zoom .35 # tight
            block:
                ease 2.0 zoom 1.1 #in.87
                pause 0.2
                ease .3 zoom .6 #out

#End Anal Plug insertion  animations (Rogue,Kitty,Laura,Jubes)< < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


#Start Anal Plug Sex removal animations (Rogue,Kitty,Laura,Jubes)
image Anal_Plug_Out_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/JubesSex/Jubes_Sex_Anal.png"
            transform_anchor True
            anchor (560,620)#(0.52,0.69)
            offset (0,28)#(218,518)
            zoom .6 # tight
            block:
                ease .3 zoom 1.1 #in.87
                pause 0.2
                ease 2.0 zoom .35 #out
        contains:
            AlphaMask("Anal_Plug_Tip_Out_Sex", "Anal_Plug_Tip_Mask_Out_Sex")
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,0)
        contains:
            "images/PlugBase_Sex.png"
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,-160)#(-6,-120) #plug inserted
            alpha 1
            block:
                ease 2.5 yoffset -90 #in (-6,-145)
                ease 1 yoffset -70 alpha 0
        pos (990+Plug_Mod[0],1347+Plug_Mod[1])        #(1076+Plug_Mod,1330)
        zoom 0.85
image Anal_Plug_Tip_Out_Sex:
            #the anal plug being removed
#        contains:
#            Solid("#159457", xysize=(420,750))
#            alpha 0.5
#    #        offset (0,0)
#            offset (400,300)#(500,300) #pos (218,518)
        contains:
            "images/PlugTip_SexF.png"
            anchor (560,620)#(0.52,0.69)
            transform_anchor True
            offset (513,420) #out(515,485)
            zoom .5 #in
#            alpha .9
            parallel:
                ease 2.5 yoffset 485 #in430
                ease 1 yoffset 505 alpha 0
            parallel:
                ease .3 zoom .85 #out
                pause 2.2
image Anal_Plug_Tip_Mask_Out_Sex:
        #the masking animation for the anal plug removal
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            anchor (560,620)#(0.52,0.69)
            transform_anchor True
            offset (515,419) #out(515,418)
            zoom .6 # tight
            block:
                ease 0.3 zoom 1.1 #in.87
                pause 0.2
                ease 2.0 zoom .6 #out .35
#End Anal Plug Sex removal animations (Rogue,Kitty,Laura,Jubes) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start Anal Plug in/out Sex (Emma, Jean, Storm)< < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Anal_Plug_In_Sex_Back:
        #inserting an anal plug
        contains:
            "images/PlugBase_Sex.png"
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,-110)#(-6,-120) #plug inserted
            alpha 1
            block:
                ease 2.5 yoffset -180 #in (-6,-145)
        contains:
            "Anal_Plug_Tip_Insert_Sex_Back"
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,0)
        pos (990+Plug_Mod[0],1347+Plug_Mod[1])        #(1076+Plug_Mod,1330)
        zoom 0.85
#        pos (500,500)
image Anal_Plug_Tip_Insert_Sex_Back:
            #the anal plug insert
#        contains:
#            Solid("#159457", xysize=(420,750))
#            alpha 0.95
#    #        offset (0,0)
#            offset (400,300)#(500,300) #pos (218,518)
        contains:
            "images/PlugTip_SexB.png"
            anchor (560,620)#(0.52,0.69)
            transform_anchor True
            offset (515,480) #out(515,485)
            zoom .85 #in
#            alpha .5
            parallel:
                ease 2.5 yoffset 410 #in420
            parallel:
                pause 2.2
                ease .3 zoom .5 #out

#End Anal Plug Sex insertion  animations (Emma, Jean, Storm)< < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

#Start Anal Plug removal animations (Emma, Jean, Storm)
image Anal_Plug_Out_Sex_Back:
        #removing an anal plug
        contains:
            "images/PlugBase_Sex.png"
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,-180)#(-6,-120) #plug inserted
            alpha 1
            block:
                ease 2.5 yoffset -110 #out (-6,-145)
                ease 1 yoffset -70 alpha 0
        contains:
            "Anal_Plug_Tip_Out_Sex_Back"
            anchor (0.5,0.5)
            transform_anchor True
            offset (0,0)
        pos (990+Plug_Mod[0],1347+Plug_Mod[1])        #(1076+Plug_Mod,1330)
        zoom 0.85
image Anal_Plug_Tip_Out_Sex_Back:
            #the anal plug being removed
#        contains:
#            Solid("#159457", xysize=(420,750))
#            alpha 0.5
#    #        offset (0,0)
#            offset (400,300)#(500,300) #pos (218,518)
        contains:
            "images/PlugTip_SexB.png"
            anchor (560,620)#(0.52,0.69)
            transform_anchor True
            offset (515,410) #out(515,485)
            zoom .5 #in
#            alpha .9
            parallel:
                ease 2.5 yoffset 480 #in430
                ease 1 yoffset 525 alpha 0
            parallel:
                ease .3 zoom .85 #out
                pause 2.2

#End Anal Plug Sex removal animations (Emma, Jean, Storm)< < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <





#Start Anal Plug removal labels < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
label Insert_Anal_Plug(Girl=0): #rkeljsvgb
        #this is called to initiate the anal plug sequence.
        if "plug" not in Girl.Inventory:
                "У нее ее нет."
                return
        if Girl.Plug:
                "Похоже, у нее уже она есть."
                return
        if "asked plug" in Girl.DailyActions and "plug" not in Girl.DailyActions:
                #you've been refused already times today
                call AnyLine(Girl,"Хватит.")
                return

        if not Girl.Plugged:
                #first time. . .
                "Вы достаете ее анальную пробку."
                $ Girl.AddWord(1,0,"asked plug",0,0) #adds tag to daily
                $ Girl.FaceChange("sad",2)
                if Girl is RogueX:
                        ch_r "Я не знаю, готова ли я. . ."
                        $ Line = "Ты готова."
                elif Girl is KittyX:
                        ch_k "Мне кажется. . . будет неудобно. . ."
                        $ Line = "Посмотрим."
                elif Girl is EmmaX:
                        ch_e "Я как-то не горю желанием. . ."
                        $ Line = "Все будет хорошо."
                elif Girl is LauraX:
                        ch_l "Хм. . . Я не уверена. . ."
                        $ Line = "Все будет хорошо."
                elif Girl is JeanX:
                        ch_j "Куда ты собираешься вставить ее? . ."
                        $ Line = "В твою попку."
                elif Girl is StormX:
                        ch_s "Надеюсь, ты не хочешь. . ."
                        $ Line = "Да, я хочу вставить ее в твою попку."
                elif Girl is JubesX:
                        ch_v "Она, эм. . . большая. . ."
                        $ Line = "Ты справишься."
                elif Girl is GwenX:
                        ch_g "Ох, эм. . . она для. . ."
                        $ Line = "Да, она для твоей попки."
                elif Girl is BetsyX:
                        ch_b "Ох, дорогуша. . . Я так понимаю, она для. . ."
                        $ Line = "Для твоей попки, да."
                elif Girl is DoreenX:
                        ch_d "Что? Ты хочешь, чтобы я вставила ее в. . ."
                        $ Line = "В твою попку, да."
                elif Girl is WandaX:
                        ch_w "Воу, время для тяжелой артиллерии. . ?"
                        $ Line = "Ты справишься."
                menu:
                    extend ""
                    "Ладно, забудь.":
                                $ Line = 0
                                $ Girl.Statup("Love", 90, 2)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.FaceChange("smile",1)
                                if Girl is "Rogue":
                                        ch_r "Спасибо. . ."
                                elif Girl is KittyX:
                                        $ Girl.Statup("Love", 90, 1)
                                        ch_k "[Girl.Like]фух. . ."
                                elif Girl is EmmaX:
                                        ch_e "Ох, замечательно. . ."
                                elif Girl is LauraX:
                                        ch_l "Клево. . ."
                                elif Girl is JeanX:
                                        $ Girl.Statup("Love", 70, 2)
                                        ch_j "Так я и думала. . ."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v "Уфф. . ."
                                elif Girl is GwenX:
                                        ch_g "Фух. . . как гора с плеч. . ."
                                elif Girl is BetsyX:
                                        ch_b "Ох. . . благодарю. . ."
                                elif Girl is DoreenX:
                                        ch_d "Фух. . . спасибо. . ."
                                elif Girl is WandaX:
                                        ch_w "Ох, ладно. . ."
                                return

                    "Ты не плохо справлялась с другими игрушками. . ." if Girl.Anal + Girl.DildoA > 5:
                            $ Line = 0
                            if ApprovalCheck(Girl, 1600,TabM=3,Alt=[[LauraX],1300]) or ApprovalCheck(Girl, 1100, "OI",TabM=3,Alt=[[LauraX],900]):
                                $ Girl.Statup("Love", 70, 1)
                                $ Girl.Statup("Obed", 70, 5)
                                $ Girl.Statup("Obed", 80, 10)
                                $ Girl.Statup("Inbt", 90, 10)
                                $ Girl.FaceChange("sly",1)
                                if Girl is "Rogue":
                                        ch_r "Полагаю, я уже привыкла. . ."
                                elif Girl is KittyX:
                                        ch_k "Ага[Girl.like]наверное. . ."
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, мы можем попробовать и ее. . ."
                                elif Girl is LauraX:
                                        ch_l "Конечно."
                                elif Girl is JeanX:
                                        ch_j "Ну, мы можем -попробовать- и ее. . ."
                                elif Girl is StormX:
                                        ch_s "Мы можем попробовать и ее. . ."
                                elif Girl is JubesX:
                                        if not Player.Male:
                                            ch_v "Ага, пожалуй, ты права. . ."
                                        else:
                                            ch_v "Ага, пожалуй, ты прав. . ."
                                elif Girl is GwenX:
                                        ch_g "Ну, да, но. . ."
                                elif Girl is BetsyX:
                                        ch_b "Возможно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ну. . . может быть. . ."
                                elif Girl is WandaX:
                                        ch_w "Ага, конечно. . ."
                            else:
                                $ Girl.Statup("Love", 80, -3)
                                $ Girl.Statup("Obed", 80, 5)
                                $ Girl.Statup("Inbt", 70, 5)
                                $ Girl.FaceChange("smile",1)
                                if Girl is "Rogue":
                                        ch_r "Да, но она довольно большая. . ."
                                elif Girl is KittyX:
                                        ch_k "Но[Girl.like]это. . ."
                                elif Girl is EmmaX:
                                        ch_e "Это другое. . ."
                                elif Girl is LauraX:
                                        ch_l "Ага, но это другое. . ."
                                elif Girl is JeanX:
                                        ch_j "Не, я пас. . ."
                                elif Girl is StormX:
                                        ch_s "Я так не думаю. . ."
                                elif Girl is JubesX:
                                        ch_v "Ага, но я откажусь. . ."
                                elif Girl is GwenX:
                                        ch_g "Эм. . . наверное, но ее я не хочу. . ."
                                elif Girl is BetsyX:
                                        ch_b "Я так не думаю. . ."
                                elif Girl is DoreenX:
                                        ch_d "Но не с ней!"
                                elif Girl is WandaX:
                                        ch_w "Ага, но это, мне кажется, слишком. . ."
                                return
                    "Тебе очень понравится.":
                            $ Line = 0
                            if ApprovalCheck(Girl, 1600,TabM=3,Alt=[[LauraX],1300]) or ApprovalCheck(Girl, 1300, "OI",TabM=3,Alt=[[LauraX],900]):
                                $ Girl.Statup("Love", 70, 5)
                                $ Girl.Statup("Obed", 70, 3)
                                $ Girl.Statup("Obed", 80, 5)
                                $ Girl.Statup("Inbt", 90, 5)
                                $ Girl.FaceChange("sly",1)
                                if Girl is "Rogue":
                                        ch_r "Может и так. . ."
                                elif Girl is KittyX:
                                        ch_k "Ага[Girl.like]возможно. . ."
                                elif Girl is EmmaX:
                                        ch_e "Я полагаю, мы можем попробовать. . ."
                                elif Girl is LauraX:
                                        ch_l "Может быть."
                                elif Girl is JeanX:
                                        ch_j "Ну, мы может -попробовать-. . ."
                                elif Girl is StormX:
                                        ch_s "Мы может попробовать. . ."
                                elif Girl is JubesX:
                                        ch_v "Ага, наверное. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох. . . -возможно-. . ."
                                elif Girl is BetsyX:
                                        ch_b "Возможно. . ."
                                elif Girl is DoreenX:
                                        ch_d "Что?! Ну. . . может быть. . ."
                                elif Girl is WandaX:
                                        ch_w "Пожалуй. . ."
                            else:
                                $ Girl.Statup("Obed", 80, -2)
                                $ Girl.Statup("Inbt", 80, 2)
                                $ Girl.FaceChange("smile",1)
                                if Girl is "Rogue":
                                        ch_r "Сомневаюсь. . ."
                                elif Girl is KittyX:
                                        ch_k "Но[Girl.like]она такая. . ."
                                elif Girl is EmmaX:
                                        ch_e "Сомневаюсь. . ."
                                elif Girl is LauraX:
                                        ch_l "Мне кажется нет. . ."
                                elif Girl is JeanX:
                                        ch_j "Сомневаюсь. . ."
                                elif Girl is StormX:
                                        ch_s "Я так не думаю. . ."
                                elif Girl is JubesX:
                                        ch_v "Вряд ли. . ."
                                elif Girl is GwenX:
                                        ch_g "Я. . . эм, так не думаю. . ."
                                elif Girl is BetsyX:
                                        ch_b "Боюсь, что нет. . ."
                                elif Girl is DoreenX:
                                        ch_d "Что?! Я так не думаю!"
                                elif Girl is WandaX:
                                        ch_w "Хех, может, в другой раз. . ."
                                return
                    "Ты можешь заменить хвост на нее." if Girl == DoreenX:
                                $ Girl.Statup("Love", 90, -3)
                                $ Girl.Statup("Obed", 80, 5)
                                $ Girl.FaceChange("angry",2)
                                ch_d "Это настоящий хвост! А не. . ."
                                if not Player.Male:
                                    ch_d "Ну, ты поняла!"
                                else:
                                    ch_d "Ну, ты понял!"
                                if ApprovalCheck(Girl, 1300, "OI",TabM=3) or Girl.Forced:
                                    $ Girl.FaceChange("sly",1,Eyes="side")
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 80, 5)
                                    ch_d "Ох. . . ладно, я все сделаю. . ."
                                else:
                                    $ Girl.Statup("Love", 80, -10)
                                    ch_d "Мой ответ \"нет\"!"
                    "[Line] [[Вставляй]":
                            $ Line = 0
                            if ApprovalCheck(Girl, 1300, "OI",TabM=3,Alt=[[StormX],1400]) or Girl.Forced:
                                $ Girl.Statup("Love", 80, -2)
                                $ Girl.Statup("Obed", 80, 10)
                                $ Girl.Statup("Obed", 200, 5)
                                $ Girl.Statup("Inbt", 80, 5)
                                if Girl.Forced:
                                        $ Girl.Forced += 1
                                        $ Girl.Statup("Love", 80, -5)
                                        $ Girl.Statup("Obed", 80, 3)
                                $ Girl.FaceChange("sly",1,Eyes="side")
                                if Girl is "Rogue":
                                        ch_r "Ладно. . ."
                                elif Girl is KittyX:
                                        ch_k "Как скажешь. . ."
                                elif Girl is EmmaX:
                                        ch_e "Хорошо. . ."
                                elif Girl is LauraX:
                                        ch_l "Как скажешь. . ."
                                elif Girl is JeanX:
                                        ch_j ". . . ладно. . ."
                                elif Girl is StormX:
                                        ch_s "Хорошо. . ."
                                elif Girl is JubesX:
                                        ch_v ". . . ладно."
                                elif Girl is GwenX:
                                        ch_g "Агась. . ."
                                elif Girl is BetsyX:
                                        ch_b "Если это так необходимо. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ох. . . ладно. . ."
                                elif Girl is WandaX:
                                        ch_w "Конечно. . ."
                            else:
                                $ Girl.Statup("Love", 80, -10)
                                $ Girl.Statup("Love", 90, -3)
                                $ Girl.Statup("Obed", 80, 5)
                                $ Girl.FaceChange("smile",1)
                                if Girl is "Rogue":
                                        ch_r "Я так не думаю. . ."
                                elif Girl is KittyX:
                                        ch_k "Не-а. . ."
                                elif Girl is EmmaX:
                                        ch_e "Это вряд ли."
                                elif Girl is LauraX:
                                        ch_l "Не-а."
                                elif Girl is JeanX:
                                        ch_j "Мечтай."
                                elif Girl is StormX:
                                        ch_s "Я так не думаю. . ."
                                elif Girl is JubesX:
                                        ch_v "Неее. . ."
                                elif Girl is GwenX:
                                        ch_g "Нет!"
                                elif Girl is BetsyX:
                                        ch_b "Конечно я не буду этого делать!"
                                elif Girl is DoreenX:
                                        ch_d "Что?! Нет!"
                                elif Girl is WandaX:
                                        ch_w "Хех, может, в другой раз. . ."
                                return
        #conflict resolution
        if Trigger2 in ("dildo anal","insert ass"):
                $ Trigger2 = 0
        if Girl.Offhand in ("dildo anal","fondle ass","insert ass"):
                $ Girl.Offhand = 0
#        if Trigger4 in ("dildo anal","fondle ass","insert ass"):
#                $ Trigger4 = 0
#        if Trigger5 in ("dildo anal","fondle ass","insert ass"):
#                $ Trigger5 = 0

        call Insert_Anal_Plug_Action(Girl)
        if not Girl.Plugged:
                #first time
                $ Girl.Statup("Obed", 50, 3)
                $ Girl.Statup("Obed", 90, 2)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Inbt", 90, 2)
                if Girl is "Rogue":
                        ch_r "Воу. . ."
                        ch_r "Так. . . плотно. . ."
                elif Girl is KittyX:
                        ch_k "Ооох!"
                        ch_k "Так[Girl.like]непривычно. . ."
                elif Girl is EmmaX:
                        ch_e "Я не часто таким занимаюсь. . ."
                elif Girl is LauraX:
                        ch_l "Такая большая. . ."
                elif Girl is JeanX:
                        ch_j "Хм, так вот каково это. . ."
                elif Girl is StormX:
                        ch_s "Ооох, это довольно необычно. . ."
                elif Girl is JubesX:
                        ch_v "Оох. Ахх."
                elif Girl is GwenX:
                        ch_g "Уууух. . . ох."
                elif Girl is BetsyX:
                        ch_b "Ох. . . Боже. . ."
                elif Girl is DoreenX:
                        ch_d "Ох. . . ого, она прямо огромная."
                elif Girl is WandaX:
                        ch_w "Oooo. . ."
                        ch_w "Она, эм. . . большая."
        return


default Plug_Mod = [0,0]

label Insert_Anal_Plug_Action(Girl=0,Cock=0,Legs=0,Panties=0,Plug_Mod=[0,0],Feet=ShowFeet):  #rkeljsvg
        #shows insertting butt plug
        #hides cock if visible, then restores it after, same with upskirt/panties down states
        if Player.Sprite:
                $ Cock = 1
                $ Player.Sprite = 0
        if not Girl.Upskirt:
                $ Legs = 1
                $ Girl.Upskirt = 1
        if not Girl.PantiesDown:
                $ Panties = 1
                $ Girl.PantiesDown = 1
        $ ShowFeet = 0
        $ Speed = 0
        $ Girl.FaceChange("angry",2,Eyes="closed")
        if renpy.showing(Girl.Tag+"_Doggy_Animation"):
                if Girl is LauraX:
                        $ Plug_Mod = [100,0]
                elif Girl is JeanX:
                        $ Plug_Mod = [4,52]
                show Anal_Plug_In_Doggy zorder 151
                pause 2.5
        if renpy.showing(Girl.Tag+"_SexSprite"):
                if Girl is RogueX:
                        $ Plug_Mod = [0,0]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is KittyX:
                        $ Plug_Mod = [17,-62]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is LauraX:
                        $ Plug_Mod = [26,-27]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is JubesX:
                        $ Plug_Mod = [0,-45]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is GwenX:
                        $ Plug_Mod = [0,-52]#[0,-45]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is BetsyX:
                        $ Plug_Mod = [0,-43]#[0,-45]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is DoreenX:
                        $ Plug_Mod = [-15,-75]#[0,-43]
                        show Anal_Plug_In_Sex zorder 151
                elif Girl is WandaX:
                        $ Plug_Mod = [30,-85]#[0,-43]
                        show Anal_Plug_In_Sex zorder 151

                elif Girl is EmmaX:
                        $ Plug_Mod = [10,0]
                        show Anal_Plug_In_Sex_Back zorder 120
                        pause 1
                elif Girl is JeanX:
                        $ Plug_Mod = [115,-45]
                        show Anal_Plug_In_Sex_Back zorder 120
                        pause 1
                elif Girl is StormX:
                        $ Plug_Mod = [15,-10]
                        show Anal_Plug_In_Sex_Back zorder 120
                pause 2.5
        $ Girl.Plug = 1
        hide Anal_Plug_In_Doggy
        hide Anal_Plug_In_Sex
        hide Anal_Plug_In_Sex_Back
        $ ShowFeet = Feet
        $ Girl.FaceChange("sucking",1,Eyes="closed")
        if "plug" not in Girl.RecentActions:
                if Girl.Plugged <= 5:
                        $ Girl.Statup("Obed", 50, 2)
                if Girl.Plugged <= 10:
                        $ Girl.Statup("Obed", 80, 1)
        if Girl.Loose:
                $ Girl.Statup("Lust", 200, 2)
        else:
                $ Girl.Statup("Obed", 80, 1)
                $ Girl.Statup("Lust", 200, -5)
        call AnyLine(Girl,"Нннннг.")
        $ Girl.FaceChange("sly",1)
        $ Girl.AddWord(1,"plug","plug",0,0) #adds tag to daily
        $ Player.Sprite = 1 if Cock else Player.Sprite
        $ Girl.Upskirt = 0 if Legs else 1
        $ Girl.PantiesDown = 0 if Panties else 1
        return

label Remove_Anal_Plug(Girl=0,Cock=0,Legs=0,Panties=0,Plug_Mod=[0,0],Feet=ShowFeet): #rkeljsvg
        #shows removing butt plug
        #hides cock if visible, then restores it after, same with upskirt/panties down states
        if Player.Sprite:
                $ Cock = 1
                $ Player.Sprite = 0
        if not Girl.Upskirt:
                $ Legs = 1
                $ Girl.Upskirt = 1
        if not Girl.PantiesDown:
                $ Panties = 1
                $ Girl.PantiesDown = 1
        $ Speed = 0
        $ Girl.Plug = 0
        $ Girl.Loose = 3
        $ Girl.FaceChange("angry",2,Eyes="closed")
        $ ShowFeet = 0
        if renpy.showing(Girl.Tag+"_Doggy_Animation"):
                if Girl is LauraX:
                        $ Plug_Mod = [100,0]
                elif Girl is JeanX:
                        $ Plug_Mod = [4,50]
                show Anal_Plug_Out_Doggy zorder 151
                pause 3
        if renpy.showing(Girl.Tag+"_SexSprite"):
                if Girl is RogueX:
                        $ Plug_Mod = [0,0]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is KittyX:
                        $ Plug_Mod = [17,-62]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is LauraX:
                        $ Plug_Mod = [26,-27]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is JubesX:
                        $ Plug_Mod = [0,-45]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is GwenX:
                        $ Plug_Mod = [0,-52]#[0,-45]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is BetsyX:
                        $ Plug_Mod = [0,-43]#[0,-45]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is DoreenX:
                        $ Plug_Mod = [-15,-70]#[0,-45]
                        show Anal_Plug_Out_Sex zorder 151
                elif Girl is WandaX:
                        $ Plug_Mod = [35,-73]#[0,-43]
                        show Anal_Plug_Out_Sex zorder 151

                elif Girl is EmmaX:
                        $ Plug_Mod = [10,0]
                        show Anal_Plug_Out_Sex_Back zorder 120
                        pause 1
                elif Girl is JeanX:
                        $ Plug_Mod = [115,-45]
                        show Anal_Plug_Out_Sex_Back zorder 120
                        pause 1
                elif Girl is StormX:
                        $ Plug_Mod = [15,-10]
                        show Anal_Plug_Out_Sex_Back zorder 120
                        pause 1
                pause 3
        hide Anal_Plug_Out_Doggy
        hide Anal_Plug_Out_Sex
        hide Anal_Plug_Out_Sex_Back
        $ Girl.FaceChange("sucking",1,Eyes="closed")
        $ Girl.Statup("Lust", 200, 2)
        call AnyLine(Girl,"Нннннг.")
        $ ShowFeet = Feet
        if not Girl.Plugged or "plug" not in Girl.RecentActions:
                $ Girl.Plugged += 1
        if Girl.Plugged == 1:
                #first time out.
                $ Girl.Statup("Obed", 80, 2)
                $ Girl.FaceChange("smile",1)
                if Girl is "Rogue":
                        ch_r "Воу. . ."
                        ch_r "Какое. . . облегчение. . ."
                elif Girl is KittyX:
                        ch_k "Ооох!"
                        ch_k "Странный. . . опыт."
                elif Girl is EmmaX:
                        ch_e "Что ж, как гора с плеч. . ."
                elif Girl is LauraX:
                        ch_l "Фух. . ."
                elif Girl is JeanX:
                        ch_j "Без нее гораздо лучше. . ."
                elif Girl is StormX:
                        ch_s "Это было очень интересно. . ."
                elif Girl is JubesX:
                        ch_v "Ооохххх."
                        ch_v "Безумие."
                elif Girl is GwenX:
                        ch_g "Фух. . . ох."
                        ch_g "Какое расслабление. . ."
                elif Girl is BetsyX:
                        ch_b "Ох. . . какое облегчение."
                elif Girl is DoreenX:
                        ch_d "Ох. . . как же теперь хорошо."
                elif Girl is WandaX:
                        ch_w "Ох. . . как приятно. . ."
        $ Girl.FaceChange("sly",1)
        $ Player.Sprite = 1 if Cock else Player.Sprite
        $ Girl.Upskirt = 0 if Legs else 1
        $ Girl.PantiesDown = 0 if Panties else 1
        return

#End Anal Plug removal labels < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# End Anal Plug in/out
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# ////   Etc.  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Drip animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Spunk_Drip:
        #the minor dripping animation
        contains:
            "images/SpermdropB.png"
            zoom 0.3
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (0,0)
                    alpha 1
                    easeout 2.5 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha 1
                    easeout 2.5 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha 1
                    easeout 2.5 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha 1
                    easeout 2.5 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat
image Spunk_Drip2:
        #Dripping spunk
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1
                repeat
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (9,0)
                pause .2
                alpha 1
                easeout 2.5 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .4
                repeat
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (6,0)
                pause .4
                alpha 1
                easeout 2.5 ypos 65
                easeout .9 ypos 350
                alpha 0
                repeat
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (12,0)
                pause .8
                alpha 1
                easeout 2.5 ypos 60
                easeout .9 ypos 350
                alpha 0
                repeat
image Wet_Drip:
        #the minor dripping animation
        contains:
            "images/Wetdrop.png"
            zoom 0.2
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (14,0)
                    alpha .8
                    easeout .9 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha .8
                    easeout .9 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha .8
                    easeout .9 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha .8
                    easeout .9 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat
image Wet_Drip2:
        #The dripping wetness animation at 2x speed
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (14,0)
                alpha .8
                easeout .9 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1.5
                repeat
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (9,0)
                pause .3
                alpha .8
                easeout .9 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .6
                repeat
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (6,0)
                pause .6
                alpha .8
                easeout .9 ypos 65
                easeout .9 ypos 350
                alpha 0
                repeat
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (12,0)
                pause .8
                alpha .8
                easeout .9 ypos 60
                easeout .9 ypos 350
                alpha 0
                pause .2
                repeat
# End Drip animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Chibicock stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Zero_Chibicock:
    LiveComposite(                            #The compositived Chibi UI cock
        (225,350),
        (0,0), ConditionSwitch(
            "Player.Color == 'pink'", "images/Chibi_Cock_P.png",
            "Player.Color == 'brown'", "images/Chibi_Cock_B.png",
            "Player.Color == 'green'", "images/Chibi_Cock_G.png",
            "True", Null(),
            ),
        )
    anchor (0.5,0.5)
image Chibi_Null:
    #The Blank Chibi-cock
    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    pos (75,675)
    zoom 0.5
image Chibi_Jackin:
    #the jackin it chibi cock
    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        "images/Chibi_Hand_M.png"
        pos (-10,-80)
        anchor (0.5,0.5)
        rotate 20
        block:
                ease .3 rotate -10 pos (0,50)
                ease .7 rotate 20 pos (-10,-80)
                repeat
    pos (75,675)
    zoom 0.5
image Chibi_Handy:
    #the girl handy chibicock
    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        ConditionSwitch(
            "StormX.Offhand == 'hand'", "images/Chibi_Hand_S.png",
            "True", "images/Chibi_Hand_G.png"
            )
#        "images/Chibi_Hand_G.png"
        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
                ease .3 rotate 0 pos (10,10)
                ease .7 rotate -10 pos (0,-130)
                repeat
    pos (75,675)
    zoom 0.5
image Chibi_Mouth_Mask:
    "images/Chibi_Mouth_Mask.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Rogue:
    "images/Chibi_Mouth_R.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Kitty:
    "images/Chibi_Mouth_K.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Emma:
    "images/Chibi_Mouth_E.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Storm:
    "images/Chibi_Mouth_S.png"
    anchor (0.5,0.5)
image Chibi_Sucking:
    # The core sucking image
    contains:
        "Chibi_SuckingB"
    pos (75,675)
image Chibi_SuckingB: #rkeljsvg
    #The composited Chibi UI cock
    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Partner is RogueX", "Chibi_Mouth_Rogue",
            "Partner is EmmaX", "Chibi_Mouth_Emma",
            "Partner is StormX", "Chibi_Mouth_Storm",
            "True", "Chibi_Mouth_Kitty"
            ),
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_Mouth_Mask")
        )
    subpixel True
    pos (7,0) #top
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout .25 rotate 0 pos (2,48) xzoom 1 #middle
        easein .25 rotate 0 pos (6,92) xzoom 1 #bottom
        easeout .5 rotate 0 pos (2,48) xzoom 1 #middle
        easein .5 rotate 0 pos (5,0) xzoom 0.71 #top
        repeat
image Chibi_Sucking_Cock:
    #The animation for the cock used in the sucking cock animation
    contains:
        subpixel True
        "Zero_Chibicock"
        pos (100,175) #top
        xzoom 1.5
        anchor (0.5,0.5)
#        alpha 0.5
        rotate 0
        block:
            easeout .25 rotate 0 pos (110,80) xzoom 1 #middle
            easein .25 rotate 0 pos (100,-10) xzoom 1 #bottom
            easeout .5 rotate 0 pos (110,80) xzoom 1 #middle
            easein .5 rotate 0 pos (100,175) xzoom 1.5 #top
            repeat


#>>>>>>>>>>
image Chibi_UI:
    # The basic chibi-UI image that is called
    contains:
        ConditionSwitch(
            "'cockout' not in Player.RecentActions or not Player.Male", Null(),
            "Trigger2 == 'jackin'", "Chibi_Jackin",
            "Ch_Focus.Offhand == 'hand' or (Partner and Partner.Offhand == 'hand')", "Chibi_Handy",
            "Partner and Partner.Offhand == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )
#    anchor (0.5,0.5)
#    pos (75,675)

# End chibicock stuff  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Cellphone:
    "images/Cellphone.png"
    xoffset 0 #-250
    yoffset 100
image PhoneSex:
    #this is the phone displayed during phone sex
    contains:
        #base
        "images/PhoneFrame.png"
    contains:
        #background plate for image
        AlphaMask("PhoneBG", "images/PhoneMask.png")
    contains:
        #characters
        ConditionSwitch(
            "Ch_Focus is RogueX",AlphaMask("PhoneScreen_Rogue", "images/PhoneMask.png"),
            "Ch_Focus is KittyX",AlphaMask("PhoneScreen_Kitty", "images/PhoneMask.png"),
            "Ch_Focus is EmmaX",AlphaMask("PhoneScreen_Emma", "images/PhoneMask.png"),
            "Ch_Focus is LauraX",AlphaMask("PhoneScreen_Laura", "images/PhoneMask.png"),
            "Ch_Focus is JeanX",AlphaMask("PhoneScreen_Jean", "images/PhoneMask.png"),
            "Ch_Focus is StormX",AlphaMask("PhoneScreen_Storm", "images/PhoneMask.png"),
            "Ch_Focus is JubesX",AlphaMask("PhoneScreen_Jubes", "images/PhoneMask.png"),
            "Ch_Focus is GwenX",AlphaMask("PhoneScreen_Gwen", "images/PhoneMask.png"),
            "Ch_Focus is BetsyX",AlphaMask("PhoneScreen_Betsy", "images/PhoneMask.png"),
            "Ch_Focus is DoreenX",AlphaMask("PhoneScreen_Doreen", "images/PhoneMask.png"),
            "Ch_Focus is WandaX",AlphaMask("PhoneScreen_Wanda", "images/PhoneMask.png"),
            )
    offset (300,50)
image PhoneBG:  #rkeljsvgb
    #this is the screen displayed on "PhoneSex", alpha-masked
    contains:
        #backdrop
        ConditionSwitch(
            "Ch_Focus.Loc == 'bg rogue'","PhoneRG",
            "Ch_Focus.Loc == 'bg kitty'", "bg_kitty",
            "Ch_Focus.Loc == 'bg emma'", "bg_emma",
            "Ch_Focus.Loc == 'bg laura'", "bg_laura",
            "Ch_Focus.Loc == 'bg jean'", "bg_jean",
            "Ch_Focus.Loc == 'bg storm'", "bg_storm",
            "Ch_Focus.Loc == 'bg jubes'", "bg_jubes",
            "Ch_Focus.Loc == 'bg gwen'", "bg_gwen",
            "Ch_Focus.Loc == 'bg betsy'", "bg_betsy",
            "Ch_Focus.Loc == 'bg doreen'", "bg_doreen",
            "Ch_Focus.Loc == 'bg wanda'", "bg_wanda",
            "Ch_Focus.Loc == 'bg classroom'", "bg_class",
            "Ch_Focus.Loc == 'bg teacher'", "bg_class",
            "True", "bg_shower",
            )
        offset (-800,-300)
        zoom 1.5
image PhoneRG:
    #Rogue's room for the phone (to make sure the bed is framed properly)
    "bg_rogue"
    xoffset 500
image PhoneScreen_Rogue:
        #this is the screen displayed on "PhoneSex", alpha-masked
        contains:
            #girl doggy
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Rogue_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,50) anchor (0.6,0) zoom 1
        contains:
            #girl sex
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Rogue_SexSprite",
                "True", Null()), pos (0,0) offset (320,100) anchor (0.6,0) zoom 1
        contains:
            #girl standing
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Rogue_Sprite"),  pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Kitty:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Kitty_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Kitty_SexSprite",
                "True", Null()), pos (0,0) offset (320,180) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Kitty_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Emma:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Emma_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Emma_SexSprite",
                "True", Null()), pos (0,0) offset (320,80) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Emma_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
        contains:
            ConditionSwitch(
                "Ch_Focus.Loc == 'bg teacher'", "bg_class",
                "True", Null()), offset (-2100,-500) zoom 3.5
image PhoneScreen_Laura:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Laura_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,80) anchor (0.6,0) zoom .9
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Laura_SexSprite",
                "True", Null()), pos (0,0) offset (190,180) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Laura_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Jean:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Jean_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Jean_SexSprite",
                "True", Null()), pos (0,0) offset (320,180) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Jean_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Storm:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Storm_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Storm_SexSprite",
                "True", Null()), pos (0,0) offset (320,220) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Storm_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
        contains:
            ConditionSwitch(
                "Ch_Focus.Loc == 'bg teacher'", "bg_class",
                "True", Null()), offset (-2100,-500) zoom 3.5
image PhoneScreen_Jubes:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Jubes_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Jubes_SexSprite",
                "True", Null()), pos (0,0) offset (320,240) anchor (0.6,0) zoom .95
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Jubes_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Gwen:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Gwen_Doggy_Animation",
                "True", Null()), pos (0,0) offset (320,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Gwen_SexSprite",
                "True", Null()), pos (0,0) offset (340,220) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Gwen_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Betsy:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Betsy_Doggy_Animation",
                "True", Null()), pos (0,0) offset (280,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Betsy_SexSprite",
                "True", Null()), pos (0,0) offset (340,220) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Betsy_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Doreen:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Doreen_Doggy_Animation",
                "True", Null()), pos (0,0) offset (280,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Doreen_SexSprite",
                "True", Null()), pos (0,0) offset (300,220) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Doreen_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image PhoneScreen_Wanda:
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy'", "Wanda_Doggy_Animation",
                "True", Null()), pos (0,0) offset (280,0) anchor (0.6,0) zoom 1
        contains:
            ConditionSwitch(
                "Girl.Pose == 'sex'", "Wanda_SexSprite",
                "True", Null()), pos (0,0) offset (330,180) anchor (0.6,0) zoom 1 #(300,220)
        contains:
            ConditionSwitch(
                "Girl.Pose == 'doggy' or Girl.Pose == 'sex'", Null(),
                "True", "Wanda_Sprite"), pos (0,0) offset (290,50) anchor (0.6,0) zoom 1.1
image DressScreen:
    #this is dressing screen displayed during wardrobe
    contains:
        #base
        "images/DressScreen.png"
    contains:
        #screen
        AlphaMask("images/DressScreenShadow.png","DressShadow")
    zoom 1
    offset (375,225)
image DressShadow: #rkeljsvgb
    #this is the shadow projected on that screen
    contains:
        #girl
        ConditionSwitch(
            "RogueX is Ch_Focus", "Rogue_Sprite",
            "KittyX is Ch_Focus", "Kitty_Sprite",
            "EmmaX is Ch_Focus", "Emma_Sprite",
            "LauraX is Ch_Focus", "Laura_Sprite",
            "JeanX is Ch_Focus", "Jean_Sprite",
            "StormX is Ch_Focus", "Storm_Sprite",
            "JubesX is Ch_Focus", "Jubes_Sprite",
            "GwenX is Ch_Focus", "Gwen_Sprite",
            "BetsyX is Ch_Focus", "Betsy_Sprite",
            "DoreenX is Ch_Focus", "Doreen_Sprite",
            "WandaX is Ch_Focus", "Wanda_Sprite",
#            "RogueX.Layer == 100", "Rogue_Sprite",
            "True", Null(),
            )
        offset (210,-170)
        zoom 1
image BlueScreen:
    #used by Historia
    alpha .1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))
image SilhouetteBase:
    #used by silhouettes
    alpha .95
    contains:
        Solid("#14142d", xysize=(1024, 768))
image Silhouettes:
    #this is dressing screen displayed during wardrobe

#    contains:
##        #screen
#        "SilhouetteBase"
    contains:
#        #screen
        AlphaMask("SilhouetteBase","Storm_Sprite") #tried to use master layer as a mask?
image Steam:
        #multiple steam clouds, intended to be used in sex poses
        contains:
            pause .5
            "Steamy"
        contains:
            "Steamy"
            offset (15,25)
            rotate 30
        contains:
            pause .2
            "Steamy"
            offset (25,-15)
            rotate -300
        zoom .5
        alpha .2
image Big_Steam:
        #multiple steam clouds, intended to be used in sex poses
        contains:
            pause .5
            "Steamy"
        contains:
            "Steamy"
            offset (15,25)
            rotate 30
        contains:
            pause .2
            "Steamy"
            offset (25,-15)
            rotate -300
        zoom 1
        alpha .4
#        rotate 180
image Shower_Steam:
        # mutliple steam clouds along the ground
        contains:
            pause .5
            "Steamy"
        contains:
            "Steamy"
            offset (150,25)
            rotate 30
        contains:
            pause 1 #.2
            "Steamy"
            offset (-150,-15)
            rotate -300
        zoom 2
image Steamy:
        #small steam cloud
        "images/Steam.png"
        transform_anchor True
        anchor (0.5,0.5)
#        zoom .5 # in
        parallel:
            zoom .7
            ease 4.5 zoom 1 #out
            pause .5
            zoom .7 #in
            repeat
        parallel:
            yoffset 0
            ease 4.5 yoffset -80 #out
            pause .5
            yoffset 0 #in
            repeat
        parallel:
            ease 1 alpha 1 #out
            ease 2.5 alpha .5 #in
            ease .5 alpha 0 #in
            pause 1
            repeat

#Xavier Sprite Compositing
image Professor:
    LiveComposite(
        (429,521),
        (0,0), "images/NPC/Xavier_body.png",
        (0,0), ConditionSwitch(
            "X_Brows == 'concentrate'", "images/NPC/Xavier_brows_concentrate.png",
            "X_Brows == 'happy'", "images/NPC/Xavier_brows_happy.png",
            "X_Brows == 'shocked'", "images/NPC/Xavier_brows_shocked.png",
            "X_Brows == 'neutral'", "images/NPC/Xavier_brows_neutral.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "X_Mouth == 'concentrate'", "images/NPC/Xavier_mouth_stern.png",
            "X_Mouth == 'happy'", "images/NPC/Xavier_mouth_smile.png",
            "X_Mouth == 'neutral'", "images/NPC/Xavier_mouth_neutral.png",
            "True", Null(),
            ),
        (0,0), "Xavier Blink",
        (0,0), ConditionSwitch(
            "X_Psychic == 1", "images/NPC/Xavier_psychic.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    offset (0,150)#200)
    zoom 1.1
image Xavier Blink:
    ConditionSwitch(
    "X_Eyes == 'concentrate'", "images/NPC/Xavier_eyes_closed.png",
    "X_Eyes == 'hypno'", "images/NPC/Xavier_eyes_hypno.png",
    "X_Eyes == 'shocked'", "images/NPC/Xavier_eyes_shocked.png",
    "True", "images/NPC/Xavier_eyes_happy.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/NPC/Xavier_eyes_closed.png"
    .25
    repeat


## Xavier Faces ///////////////////////////////
label XavierFace (Face = X_Emote):
        if Face == "psychic":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "concentrate"
                $ X_Psychic = 1
        if Face == "hypno":
                $ X_Mouth = "neutral"
                $ X_Brows = "neutral"
                $ X_Eyes = "hypno"
        if Face == "shocked":
                $ X_Mouth = "neutral"
                $ X_Brows = "shocked"
                $ X_Eyes = "shocked"
                $ X_Psychic = 0
        if Face == "happy":
                $ X_Mouth = "happy"
                $ X_Brows = "happy"
                $ X_Eyes = "happy"
                $ X_Psychic = 0
        if Face == "angry":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "happy"
                $ X_Psychic = 0
        return

#Night composite
image setting:
    LiveComposite(
    #dead aspect used only in older saves
    (1024,768),
    (0, 0), ConditionSwitch(
        "Time_Count >= 3", "images/sky_night.jpg",
        "Time_Count == 2", "images/sky_sunset.jpg",
        "True", "images/sky_day.jpg",
        ),
    (0, 0), ConditionSwitch(
        "bg_current == 'bg study'", "images/study.jpg",
        "bg_current == 'bg player'", "images/playerroom.png",
        "bg_current == 'bg dangerroom'", "images/dangerroom.jpg",
        "bg_current == 'bg showerroom'", "images/Shower.jpg",
        "bg_current == 'bg rogue'", "images/Rogueroom.png",
        "bg_current == 'bg movies'", "images/Movies.jpg",
        "bg_current == 'bg restaurant'", "images/Restaurant.jpg",
        "bg_current == 'bg kitty'", "images/kittyroom.png",
        "bg_current == 'bg emma'", "images/emmaroom.png",
#        "bg_current == 'bg classroom'", "images/ClassroomLit.jpg",
        # if bg_current == 'bg campus' or anything else
        "Time_Count >= 3",      "images/Crossroads_Night.jpg",
        "Time_Count == 2",    "images/Crossroads_Evening.jpg",
        "True",                         "images/Crossroads_Day.jpg",
        ),
    )
label Display_Background(Entry = 0): #rkeljsvgbdw
        # call Display_Background(1)
        #Displays the current background
        if Entry == 1:
                                scene bg_entry onlayer backdrop
        elif bg_current == "bg player":
                                scene bg_player onlayer backdrop
        elif bg_current == "bg rogue":
                                scene bg_rogue onlayer backdrop
        elif bg_current == "bg kitty":
                                scene bg_kitty onlayer backdrop
        elif bg_current == "bg emma":
                                scene bg_emma onlayer backdrop
        elif bg_current == "bg laura":
                                scene bg_laura onlayer backdrop
        elif bg_current == "bg jean":
                                scene bg_jean onlayer backdrop
        elif bg_current == "bg storm":
                                scene bg_storm onlayer backdrop
        elif bg_current == "bg jubes":
                                scene bg_jubes onlayer backdrop
        elif bg_current == "bg gwen":
                                scene bg_gwen onlayer backdrop
        elif bg_current == "bg betsy":
                                scene bg_betsy onlayer backdrop
        elif bg_current == "bg doreen":
                                scene bg_doreen onlayer backdrop
        elif bg_current == "bg wanda":
                                scene bg_wanda onlayer backdrop
        elif bg_current == "bg classroom":
                                scene bg_class onlayer backdrop
        elif bg_current == "bg dangerroom":
                                scene bg_danger onlayer backdrop
        elif bg_current == "bg showerroom":
                                scene bg_shower onlayer backdrop
        elif bg_current == "bg study":
                                scene bg_study onlayer backdrop
        elif bg_current == "bg movies":
                                scene bg_movies onlayer backdrop
        elif bg_current == "bg restaurant":
                                scene bg_rest onlayer backdrop
        elif bg_current == "bg pool":
                                scene bg_pool onlayer backdrop
        elif bg_current == "bg mall":
                                scene bg_mall onlayer backdrop
        elif bg_current == "bg shop":
                                scene bg_shop onlayer backdrop
        elif bg_current == "bg dressing":
                                scene bg_dressing onlayer backdrop
        elif bg_current == "HW Party":
                                scene bg_halloween onlayer backdrop
        else: # if 'bg campus' or anything else
                                scene bg_campus onlayer backdrop
        return

image bg_entry = "images/Door.jpg"

image bg_opendoor = "images/Door_Open.png"

image bg_player:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/playerroom.png"
image bg_rogue:
        LiveComposite(
            (1024,768),
            (0,0), ConditionSwitch(
                #panties down back
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                ),
            (0,0), "images/rogueroom.png"
            )
image bg_kitty:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/kittyroom.png"
image bg_emma:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/emmaroom.png"
image bg_laura: #rkeljsvg
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/lauraroom.png"
image bg_jean: #rkeljsvg
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/jeanroom.png"
image bg_storm: #rkeljsvg
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/stormroom_night.png",
                "Time_Count == 2", "images/stormroom_evening.png",
                "True", "images/stormroom_day.png",
                )
image bg_jubes: #rkeljsvg
        contains: #see if this works, if not remove it
             "images/jubesroom.png"
image bg_gwen: #rkeljsvg
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/gwenroom.png"
image bg_betsy: #rkeljsvgb
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/betsyroom.png"
image bg_doreen: #rkeljsvg
        contains:
            ConditionSwitch(
                "DoreenX not in ActiveGirls and Time_Count >= 3", "images/atticroom_night.png",
                "DoreenX not in ActiveGirls and Time_Count == 2", "images/atticroom_evening.png",
                "DoreenX not in ActiveGirls", "images/atticroom_day.png",

                "Time_Count >= 3", "images/doreenroom_night.png",
                "Time_Count == 2", "images/doreenroom_evening.png",
                "True", "images/doreenroom_day.png",
                )
image bg_wanda: #rkeljsvgb
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3", "images/sky_night.jpg",
                "Time_Count == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
        contains:
                "images/wandaroom.png"
image bg_campus:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3",      "images/Campus_Night.png",
                "Time_Count == 2",    "images/Campus_Evening.png",
                "True",                         "images/Campus_Day.png",
                )
image bg_pool:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count >= 3",      "images/pool_night.png",
                "Time_Count == 2",    "images/pool_evening.png",
                "True",                         "images/pool_day.png",
                )
image bg_class:
        contains:
            "images/Classroom.jpg"
        contains:
            ConditionSwitch(
                "EmmaX.Loc == 'bg teacher' and 'frisky' in EmmaX.RecentActions", "Emma_Behind_Podium",
                "EmmaX.Loc == 'bg teacher'", "Emma_At_Podium",
                "EmmaX.Loc == 'bg desk'", "Emma_At_Desk",
                "StormX.Loc == 'bg teacher' and 'frisky' in StormX.RecentActions", "Storm_Behind_Podium",
                "StormX.Loc == 'bg teacher'", "Storm_At_Podium",
                "StormX.Loc == 'bg desk'", "Storm_At_Desk",
                "True", Null(),
                )
        contains:
            #The overlay Podium
            "images/ClassroomFront.png"
        contains:
            ConditionSwitch(
                "Time_Count >= 2 or Weekday >= 5", Null(),
                "True", "images/ClassroomPupils.png",
                )
image bg_classzoom:
        contains:
            "images/ClassZoom.jpg"
image empty_class:
        contains:
            "images/Classroom.jpg"
image bg_study:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count > 2",      "images/StudyNight.jpg",
                "True",                         "images/StudyDay.jpg",
                )
image bg_mall:
        contains: #see if this works, if not remove it
            ConditionSwitch(
                "Time_Count > 1",      "images/mall_night.png",
                "True",                         "images/mall_day.png",
                )

#image bg_classlit = "images/ClassroomLit.jpg"
#image bg_classnight = "images/ClassroomNight.jpg"
image bg_halloween = "images/HalloweenParty.jpg"
image bg_danger = "images/dangerroom.jpg"
image bg_shower = "images/Shower.jpg"
#image bg_study = "images/study.jpg"
image bg_movies = "images/Movies.jpg"
image bg_rest = "images/Restaurant.jpg"
image bg_shop = "images/Shop.jpg"
image bg_dressing = "images/Dressingroom.jpg"
image dinnertable = "images/Restaurant_Table.png"

label RoomMask:          #rkeljsvgb
        if bg_current == "bg player":
                    show bg_playermask onlayer black:
                        alpha .2
        elif bg_current == "bg rogue":
                    show bg_roguemask onlayer black:
                        alpha .2
        elif bg_current == "bg kitty":
                    show bg_kittymask onlayer black:
                        alpha .2
        elif bg_current == "bg emma":
                    show bg_emmamask onlayer black:
                        alpha .2
        elif bg_current == "bg laura":
                    show bg_lauramask onlayer black:
                        alpha .2
        elif bg_current == "bg jean":
                    show bg_jeanmask onlayer black:
                        alpha .2
        elif bg_current == "bg storm":
                    show bg_stormmask onlayer black:
                        alpha .2
        elif bg_current == "bg jubes":
                    show bg_jubesmask onlayer black:
                        alpha .2
        elif bg_current == "bg gwen":
                    show bg_gwenmask onlayer black:
                        alpha .2
        elif bg_current == "bg betsy":
                    show bg_betsymask onlayer black:
                        alpha .2
        elif bg_current == "bg doreen":
                    show bg_doreenmask onlayer black:
                        alpha .2
        elif bg_current == "bg wanda":
                    show bg_wandamask onlayer black:
                        alpha .2
        return

image bg_playermask = "images/playerroom.png"

image bg_roguemask = "images/Rogueroom.png"

image bg_kittymask = "images/kittyroom.png"

image bg_emmamask = "images/emmaroom.png"

image bg_lauramask = "images/lauraroom.png"

image bg_jeanmask = "images/jeanroom.png"

image bg_stormmask = "images/stormroom_day.png"

image bg_jubesmask = "images/jubesroom.png"

image bg_gwenmask = "images/gwenroom.png"

image bg_betsymask = "images/betsyroom.png"

image bg_doreenmask = "images/doreenroom_day.png"

image bg_wandamask = "images/wandaroom.png"

image bg_classmask = "images/Classroom.jpg"

label Campus_Nearby:   #rkeljsvg
        # Displays each girl at a location on campus, if they are nearby
        if Nearby:
                $ renpy.random.shuffle(Nearby)
        else:
                return
        while len(Nearby) > 3:
                $ Nearby[0].Loc = Nearby[0].Home
                $ Nearby.remove(Nearby[0])
        if LauraX in Nearby:
                show Laura_Sprite at Smol(1000,350,0.1) zorder 25
        if JubesX in Nearby:
                show Jubes_Sprite at Smol(300,330,0.15) zorder 29
        if GwenX in Nearby:
                show Gwen_Sprite at Smol(900,330,0.15) zorder 32
        if StormX in Nearby:
                show Storm_Sprite at Smol(400,300,0.3) zorder 34
        if BetsyX in Nearby:
                show Betsy_Sprite at Smol(950,300,0.3) zorder 35
        if DoreenX in Nearby:
                show Doreen_Sprite at Smol(50,330,0.2) zorder 35
        if WandaX in Nearby:
                show Wanda_Sprite at Smol(250,300,0.3) zorder 35
        if EmmaX in Nearby:
                show Emma_Sprite at Smol(860,300,0.3) zorder 36
        if KittyX in Nearby:
                show Kitty_Sprite at Smol(820,300,0.4) zorder 39
        if RogueX in Nearby:
                show Rogue_Sprite at Smol(700,300,0.4) zorder 41
        if JeanX in Nearby:
                show Jean_Sprite at Smol(130,300,0.48) zorder 44
        return


label Show_In_Door(Girl):    #rkeljsvgb
        # Displays girl in the door frame, standing
        if Girl not in TotalGirls:
                return

        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Smol(630,150)])
#        if Girl is RogueX:
#                show Rogue_Sprite at Smol(700,150)
        return


label Class_Adjacent(TempNearby=[],XPos_N=0,YPos_N=0,Spin_N=0,Flip_N=1):   #rkeljsvg
        # Displays each girl at a location in the classroom, if they are next to you
        if not Present:
                return
        $ TempPresent = Present[:]
        if EmmaX in TempPresent:
                $ TempPresent.remove(EmmaX)
        if StormX in TempPresent:
                $ TempPresent.remove(StormX)
#        if Ch_Focus in Present and Present[0] is not Ch_Focus:
#                $ Present.reverse()
        while TempPresent:
            if len(TempPresent) < len(Present):
                    #if you have already removed one girl from the list,
                    #the only one left is the second girl, who is now placed
                    $ XPos_N  = 150
                    $ YPos_N  = 850
                    $ Spin_N  = 0
                    $ Flip_N  = -1
            else:
                    $ XPos_N  = 900
                    $ YPos_N  = 850
                    $ Spin_N  = 0
                    $ Flip_N  = 1
            $ TempPresent[0].Facing = 1

            $ renpy.hide(TempPresent[0].Tag+"_Sprite")
            $ renpy.show(TempPresent[0].Tag+"_Seated",at_list=[ClassSeated(XPos_N,YPos_N,1.5,Spin_N,Flip_N)],zorder=70)

#            if RogueX == TempPresent[0]:
#                    hide Rogue_Sprite
#                    show Rogue_Seated at ClassSeated(XPos_N,YPos_N,1.5,Spin_N,Flip_N) zorder 70
            $ TempPresent.remove(TempPresent[0])
        $ Count = 0
        return

label Class_Nearby(Shuffle=1,TempNearby=[],XPos_N=0,YPos_N=0,Spin_N=0,Flip_N=1):  #rkeljsvg
        # Displays each girl at a location in the classroom, if they are nearby
        if not Nearby:
                return
#        $ TempNearby = Nearby[:]
        $ Count = 0
#        if Shuffle:
#                $ renpy.random.shuffle(TempNearby)
#        while len(TempNearby) > 3:
#                $ TempNearby.remove(TempNearby[0])

        $ Count = len(Nearby) if len(Nearby) < 3 else 3

        while Count > 0:
            $ Count -= 1
            if Count == 2: #left
                    $ XPos_N  = 315
                    $ YPos_N  = 542
                    $ Spin_N  = 3
                    $ Flip_N  = -1
            elif Count == 1: #right
                    $ XPos_N  = 740
                    $ YPos_N  = 525
                    $ Zoom_N  = .55
                    $ Spin_N  = -7
                    $ Flip_N  = 1
            elif Count == 0: #mid
                    $ XPos_N  = 520
                    $ YPos_N  = 543
                    $ Zoom_N  = .55
                    $ Spin_N  = -2
                    $ Flip_N  = 1
            $ Nearby[Count].Facing = 1

            if Nearby[Count] in (EmmaX,StormX):
                    pass
            else:
                    $ renpy.hide(Nearby[Count].Tag+"_Sprite")
                    $ renpy.show(Nearby[Count].Tag+"_Seated",at_list=[ClassSeated(XPos_N,YPos_N,0.55,Spin_N,Flip_N)],zorder=50)

#            if RogueX == Nearby[Count]:
#                    hide Rogue_Sprite
#                    show Rogue_Seated at ClassSeated(XPos_N,YPos_N,0.55,Spin_N,Flip_N) zorder 50
        $ Count = 0
        return

label Clear_Seated:   #rkeljsvgbdw
        hide Rogue_Seated
        hide Kitty_Seated
        hide Laura_Seated
        hide Jean_Seated
        hide Jubes_Seated
        hide Gwen_Seated
        hide Betsy_Seated
        hide Doreen_Seated
        hide Wanda_Seated
        return

label Pool_Nearby:   #rkeljsvgbdw
        # Displays each girl at a location at the pool, if they are nearby
        # People in pool are zorder 50, pool water is zorder 60, playables are 75 and 100
        if Nearby:
                $ renpy.random.shuffle(Nearby)
        else:
                return
        while len(Nearby) > 3:
                $ Nearby[0].Loc = Nearby[0].Home
                $ Nearby.remove(Nearby[0])
        if BetsyX in Nearby:
                show Betsy_Sprite at Smol(450,210,0.3) zorder 29
        if DoreenX in Nearby:
                show Doreen_Sprite at Smol(700,230,0.3) zorder 29
        if WandaX in Nearby:
                show Wanda_Sprite at Smol(100,220,0.3) zorder 29
        if RogueX in Nearby:
                show Rogue_Sprite at Smol(750,250,0.5) zorder 66 #in front of pool
        if KittyX in Nearby:
                show Kitty_Sprite at Smol(850,200,0.4) zorder 36 #side of pool
        if EmmaX in Nearby:
                show Emma_Sprite at Smol(910,250,0.5) zorder 64
        if LauraX in Nearby:
                show Laura_Sprite at Smol(900,250,0.45) zorder 62
        if JeanX in Nearby:
                show Jean_Sprite at Smol(600,230,0.3) zorder 27
        if StormX in Nearby:
                show Storm_Sprite at Smol(400,250,0.5) zorder 64
        if JubesX in Nearby:
                show Jubes_Sprite at Smol(300,230,0.3) zorder 29
        if GwenX in Nearby:
                show Gwen_Sprite at Smol(200,250,0.5) zorder 65
        return

image DeskMask:
        #this is a blank solid I use block the desk's position.
        contains:
            Solid("#75d7ec", xysize=(500,500))
            alpha 1
            yoffset -150
            xoffset -50
transform ClassSeated(XPOS=800,YPOS=500,ZM=0.55,Spin=0,Flip=1):
        #this positions girls in a small state
        alpha 1
        xzoom Flip
        zoom ZM
        pos (XPOS,YPOS)#(700,150)#(0,50)
        anchor (.2,.5)
        transform_anchor True
        rotate Spin
#        offset (700,100)#(XPOS,YPOS)
#        block:
#            ease 1 rotate -10
#            ease 1 rotate 0
#            repeat

image Rogue_Seated:
        contains:
            AlphaMask("Rogue_Doggy_Body", "DeskMask")
image Kitty_Seated:
        contains:
            AlphaMask("Kitty_Doggy_Body", "DeskMask")
            xoffset 40#25
#image Emma_Seated:
#        contains:
#            AlphaMask("Emma_Doggy_Body", "DeskMask")
image Laura_Seated:
        contains:
            AlphaMask("Laura_Doggy_Body", "DeskMask")
            offset (-50,5)
image Jean_Seated:
        contains:
            AlphaMask("Jean_Doggy_Body", "DeskMask")
            offset (55,0)
#image Storm_Seated:
#        contains:
#            AlphaMask("Storm_Doggy_Body", "DeskMask")
image Jubes_Seated:
        contains:
            AlphaMask("Jubes_Doggy_Body", "DeskMask")
image Gwen_Seated:
        contains:
            AlphaMask("Gwen_Doggy_Body", "DeskMask")
image Betsy_Seated:
        contains:
            AlphaMask("Betsy_Doggy_Body", "DeskMask")
#            offset (-100,0)#(55,0)
image Doreen_Seated:
        contains:
            AlphaMask("Doreen_Seated_Basic", "DeskMask")
#            offset (0,100)#(55,0)
image Wanda_Seated:
        contains:
            AlphaMask("Wanda_Doggy_Body", "DeskMask")
image Doreen_Seated_Basic:
    #makes her slightly larger and higher up
    contains:
        "Doreen_Doggy_Body"
        yoffset -100
        zoom 1.1
label Girl_Kissing_Launch(Girl=Ch_Focus,T = Trigger,Set=1):
        # call Girl_Kissing_Launch(RogueX)
        call Girl_Hide(Girl) #call Rogue_Hide
        $ Trigger = T
        $ Girl.Pose = "kiss" if Set else Girl.Pose
        if not renpy.showing(Girl.Tag+"_Sprite"):
                $ renpy.show(Girl.Tag+"_Sprite",at_list=[Sprite_Set(Girl.SpriteLoc,50)],zorder=110)
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Kissing_Anim],zorder=110)
        return
transform Kissing_Anim:
        ease 0.5 pos (600,50) offset (0,0) zoom 2.5 alpha 1
#        ease 0.5 pos 550,50 offset (100,0) zoom 2 alpha 1

label Girl_Smooch_Launch(Girl=Ch_Focus):
        $ Girl.FaceChange("kiss")
        if not renpy.showing(Girl.Tag+"_Sprite"):
                $ renpy.show(Girl.Tag+"_Sprite",at_list=[Sprite_Set(Girl.SpriteLoc,50)],zorder=110)
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Smooch_Anim(Girl)],zorder=110)
        $ Girl.FaceChange("sexy")
        return
transform Smooch_Anim(Girl):
        ease 0.5 pos (600,50) offset (0,0) zoom 2.5 alpha 1
        pause 1
        ease 0.5 pos (Girl.SpriteLoc,50) offset (0,0) zoom 1 alpha 1

label Girl_Breasts_Launch(Girl=Ch_Focus,T = Trigger,Set=1):
        call Girl_Hide(Girl) #call Rogue_Hide
        $ Trigger = T
        $ Girl.Pose = "breasts" if Set else Girl.Pose
        if not renpy.showing(Girl.Tag+"_Sprite"):
                $ renpy.show(Girl.Tag+"_Sprite",at_list=[Sprite_Set(Girl.SpriteLoc,50)],zorder=110)
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Breasts_Launch_Anim],zorder=110)
        return
transform Breasts_Launch_Anim:
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
        pos (700,-50) offset (0,0) zoom 2 alpha 1

label Girl_Middle_Launch(Girl=Ch_Focus,T = Trigger,Set=1):
        call Girl_Hide(Girl) #call Rogue_Hide
        $ Trigger = T
        $ Girl.Pose = "mid" if Set else Girl.Pose
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Mid_Launch_Anim],zorder=110)
        return
transform Mid_Launch_Anim:
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
        pos (700,-50) offset (0,0) zoom 1.5 alpha 1

label Girl_Pussy_Launch(Girl=Ch_Focus,T = Trigger,Set=1):
        call Girl_Hide(Girl) #call Rogue_Hide
        $ Trigger = T
        $ Girl.Pose = "pussy" if Set else Girl.Pose
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Pussy_Launch_Anim],zorder=110)
        return
transform Pussy_Launch_Anim:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
        pos (700,-400) offset (0,0) zoom 2 alpha 1




# Glossary
# Rogue_Sprite and Rogue_Head

# Rogue_Doggy_Animation
# Zero_Doggy_Up (used in hotdogging and footjobs)
# Zero_Doggy_Insert (used in forward angled fucking, Emma's hotdogging)
# Pussy sex animations (static, heading, fingering, 2, 3)
# Doggy_Fucking_Dildo
# Zero_Doggy_Anal_Finger
# Rogue anal stuff
# Rogue FJ stuff
# beta Slap Ass animations
# Doggy Launch

# Rogue_SexSprite/sex animations/launcher

# BJ animation
# Blowcock (used in most blowjobs, TJs)
# Ghostcock (used in Emma's sex post, Kitty's FJ pose)
# BJ launchers

# Zero_Blowcock(used by Rogue's TJ, Laura's TJ and FJ, Jean TJ and Sex pose, Storm TJ and sex pose, Jubes TJ)
# Zero_Ghostcock (not used yet?)
# Rogue TJ poses and launcher

# Zero_Handcock (used by handies,psy)
# Rogue HJ animations/launcher

# Zero_Pussy (used in various girl Zero content)
# Rogue_CUN_Animation and Rogue_Finger_Animation

# Rogue_Kissing_Launch, Rogue_Kissing_Smooch, Rogue_Breasts_Launch, Rogue_Middle_Launch, Rogue_Pussy_Launch, Rogue_Pos_Reset, Rogue_Hide, Rogue_Smol_Launch

# Vibrate(),UI_Vibrator, GropeLeftBreast, GropeRightBreast, LickRightBreast, LickLeftBreast, GropeThigh,
# GropePussy, FingerPussy, Lickpussy,
# VibratorRightBreast, VibratorLeftBreast, VibratorPussy, VibratorAnal, VibratorPussyInsert, VibratorAnalInsert
# GirlGropeLeftBreast, GirlGropeRightBreast, GirlGropeThigh, GirlGropePussy, GirlFingerPussy
# GirlGropePussyX(), GirlFingerPussyX(), RogueMastHand, RogueFingerHand
# Lick_Anim
# Close_Launch
# Smol
# CloseZoom
# Les_Launch, Les_Launch_Doggy
# Anal Plug content

#Spunk_Drip, Spunk_Drip2, Wet_Drip, Wet_Drip2

#Zero_Chibicock

# Cellphone, PhoneSex
# DressScreen
# BlueScreen, SilhouetteBase, Silhouettes
# Steam, Shower_Steam, Steamy,

# Professor X stuff
# setting, Display_Background, and backgrounds, RoomMask, Campus_Nearby, Show_In_Door

# Gwen stuff
