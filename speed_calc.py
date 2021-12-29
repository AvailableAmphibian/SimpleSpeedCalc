# === Constants ===

# Final multiplier
SPD_BUFF = 1.3
# Base Multipliers
TOTEM = 0.15
LEAD = 0.24
# Base speed
LUSHEN_BASE_SPD = 103  # Base monster used
HOMUNL_BASE_SPD = 101
JAMIRE_BASE_SPD = 113


# =================

# === Functions ===

def calc_speed_tune(jamire_bonus_speed, use_lead, nuker_base_speed):
    """
    Parameters:
        jamire_bonus_speed (int): The bonus speed of Jamire's rune.
        use_lead (bool): If the lead speed should be used or not.
        nuker_base_speed (int): The base speed of the nuker used, default is Lushen's
    Returns:
        ((int, int), (int,int)) the speed that Lushen and the Homunculus need to be perfectly speed tuned.
        The couples are as followed : ((lushen_total, lushen_bonus), (homun_total, homun_bonus))
    """

    base_mult = TOTEM  # = 0.15
    if use_lead:
        base_mult += LEAD  # = 0.39

    # --- jamire ---
    JAMIRE_ADDED_SPEED = JAMIRE_BASE_SPD * (1 + base_mult)  # = 113 * 1.39
    jamire_final_speed = JAMIRE_ADDED_SPEED + jamire_bonus_speed  # = BASE * 1.39 + runes
    # --------------

    # --- homunl ---
    homunl_total = int(
        jamire_final_speed - 1 - (HOMUNL_BASE_SPD * base_mult)) - 1  # = jamire final - homun lead+totem bonus
    homunl_rune_bonus = homunl_total - HOMUNL_BASE_SPD  # only runes

    homunl_return = (homunl_total, homunl_rune_bonus)
    # --------------

    # --- Nuker  ---
    NUKER__BASE_BONUS = LUSHEN_BASE_SPD * (1 + base_mult)  # 103 * 1.39
    nuker__rune_bonus = 0  # current rune bonus needed

    while (NUKER__BASE_BONUS + nuker__rune_bonus) * SPD_BUFF <= jamire_final_speed:
        nuker__rune_bonus += 1  # calculating the minimum speed required from runes

    lushen_total = LUSHEN_BASE_SPD + nuker__rune_bonus  # readable total (103 + rune bonus)

    lushen_return = (lushen_total, nuker__rune_bonus)
    # --------------

    return lushen_return, homunl_return


def display_for_it(jamire_bonus_speed, use_lead, nuker_bs=LUSHEN_BASE_SPD):
    ((lu_t, lu_rb), (ho_t, ho_rb)) = calc_speed_tune(jamire_bonus_speed, use_lead, nuker_bs)
    print("You need +" + str(ho_rb) + " speed on your light homun to reach " + str(ho_t) + " speed.")
    print("You need +" + str(lu_rb) + " speed on your Lushen to reach " + str(lu_t) + " speed.")


# =================

# Here we calc for a Jamire with a bonus of 200 from runes and using its lead
display_for_it(200, True)
