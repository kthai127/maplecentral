import random

# Starforce table (Pass, Fail, Boom) 
STARFORCE_TABLE = {
    0:  (0.95, 0.05, 0.00),
    1:  (0.90, 0.10, 0.00),
    2:  (0.85, 0.15, 0.00),
    3:  (0.85, 0.15, 0.00),
    4:  (0.80, 0.20, 0.00),
    5:  (0.75, 0.25, 0.00),
    6:  (0.70, 0.30, 0.00),
    7:  (0.65, 0.35, 0.00),
    8:  (0.60, 0.40, 0.00),
    9:  (0.55, 0.45, 0.00),
    10: (0.50, 0.50, 0.00),
    11: (0.45, 0.55, 0.00),
    12: (0.40, 0.60, 0.00),
    13: (0.35, 0.65, 0.00),
    14: (0.30, 0.70, 0.00),
    15: (0.30, 0.679, 0.021),
    16: (0.30, 0.679, 0.021),
    17: (0.15, 0.782, 0.068),
    18: (0.15, 0.782, 0.068),
    19: (0.15, 0.765, 0.085),
    20: (0.30, 0.595, 0.105),
    21: (0.15, 0.7225, 0.1275),
    22: (0.15, 0.68, 0.17),
    23: (0.10, 0.72, 0.18),
    24: (0.10, 0.72, 0.18),
    25: (0.10, 0.72, 0.18),
    26: (0.07, 0.744, 0.186),
    27: (0.05, 0.76, 0.19),
    28: (0.03, 0.778, 0.194),
    29: (0.01, 0.792, 0.198), 
}

def tap_once(current_star: int, safeguard: bool):
    """
    Performs one starforce attempt.
    Safeguard removes boom chance for 15-17.
    """
    success, fail, boom = STARFORCE_TABLE[current_star]

    # Apply safeguard logic
    if safeguard and 15 <= current_star <= 17:
        fail += boom
        boom = 0

    r = random.random()

    if r < success:
        return current_star + 1, "SUCCESS"
    elif r < success + fail:
        return current_star, "FAIL"
    else:
        return 0, "BOOM"
    
def get_rates(current_star: int, safeguard: bool):
    """
    Returns the actual rates (success, fail, boom) for UI display,
    including safeguard adjustments.
    """
    success, fail, boom = STARFORCE_TABLE[current_star]

    if safeguard and 15 <= current_star <= 17:
        fail += boom
        boom = 0

    return success, fail, boom
