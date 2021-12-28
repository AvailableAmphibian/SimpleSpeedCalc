# === Constants ===

# Final multiplier
SPD_BUFF = 1.3
# Base Multipliers
TOTEM = 0.15
LEAD = 0.24
# Base speed
LUSHEN_BASE_SPD = 103
HOMUNL_BASE_SPD = 101
JAMIRE_BASE_SPD = 113
# Atb tick
ATB_TICK = 0.07

# =================

# === Functions ===

def calcSpeedTune(jamire_bonus_speed, use_lead):
    """
    Parameters:
        jamire_bonus_speed (int): The bonus speed of Jamire's rune.
        use_lead (bool): If the lead speed should be used or not.
    
    Returns:
        ((int, int), (int,int)) the speed that Lushen and the Homunculus need to be perfectly speed tuned.
        The couples are as followed : ((lushen_total, lushen_bonus), (homun_total, homun_bonus))
    """
    
    base_mult = TOTEM
    if use_lead:
        base_mult += LEAD
    
    JAMIRE_ADDED_SPEED = JAMIRE_BASE_SPD * (1 + base_mult)
    jamire_final_speed = JAMIRE_ADDED_SPEED + jamire_bonus_speed
    
    LUSHEN_BASE_BONUS = LUSHEN_BASE_SPD * (1 + base_mult)
    
    homunl_total = int( jamire_final_speed - 1 - (HOMUNL_BASE_SPD * base_mult) ) - 1
    homunl_rune_bonus = homunl_total - HOMUNL_BASE_SPD
    
    homunl_return = (homunl_total, homunl_rune_bonus)
    
    lushen_rune_bonus = 0
    
    while (LUSHEN_BASE_BONUS + lushen_rune_bonus) * SPD_BUFF <= jamire_final_speed:
        lushen_rune_bonus += 1
        
    lushen_total = LUSHEN_BASE_SPD + lushen_rune_bonus
    
    lushen_return = (lushen_total, lushen_rune_bonus)
    
    return (lushen_return, homunl_return)

def display_for_it(jamire_bonus_speed, use_lead):
    ((lu_t, lu_rb), (ho_t, ho_rb)) = calcSpeedTune(jamire_bonus_speed, use_lead)
    print("You need +"+ str(ho_rb) + " speed on your light homun to reach " + str(ho_t) + " speed.")
    print("You need +" + str(lu_rb) +" speed on your Lushen to reach " + str(lu_t) + " speed.")
    
# =================

display_for_it(200, False)
