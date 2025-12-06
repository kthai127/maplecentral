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
    Safeguard prevents booms from 15 to 18 stars.
    """

    # SF Rates; pull from table
    success, fail, boom = STARFORCE_TABLE[current_star]

    # Safeguard
    if safeguard and 15 <= current_star <= 17:
        fail += boom   # fail absorbs the boom rate
        boom = 0       # boom is removed entirely


    r = random.random()

    if r < success:
        return current_star + 1, "SUCCESS"

    elif r < success + fail:
        return current_star, "FAIL"

    else:
        return 0, "BOOM"



def manual_simulation():
    # Starting star input
    while True:
        try:
            start = int(input("Enter starting star (0 - 29): "))
            if 0 <= start <= 29:
                break
            else:
                print("Please enter a number between 0 and 29.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    current_star = start
    safeguard = False
    attempts_by_star = {}   # summary-level tracker

    print(f"\nStarting at {current_star} stars!")

    while True:
        print(f"\nCurrent Star: {current_star}")
        print(f"Safeguard: {'ON' if safeguard else 'OFF'}")
        print("Press ENTER to tap, 's' to toggle safeguard, 'q' to quit.")

        user = input("> ")

        if user.lower() == 'q':
            print("Ending simulation.")
            break

        if user.lower() == 's':
            safeguard = not safeguard
            print(f"Safeguard toggled to {'ON' if safeguard else 'OFF'}")
            continue

        # Count the attempt for THIS star
        attempts_by_star.setdefault(current_star, 0)
        attempts_by_star[current_star] += 1

        # Perform tap
        new_star, outcome = tap_once(current_star, safeguard)

        print(f"Outcome: {outcome}")
        print(f"Star: {current_star} → {new_star}")
        print("-" * 30)

        # Boom = immediate stop
        if outcome == "BOOM":
            boom_star = current_star   # where boom occurred
            break

        current_star = new_star

    # ----- SUMMARY -----
    print("\n===== SUMMARY =====")
    print(f"Started at: {start}")

    # If boom
    if 'boom_star' in locals():
        print(f"Boomed at:  {boom_star} → 0\n")
    else:
        print(f"Ended at:   {current_star}\n")

    print("Attempts by star level:\n")

    # print attempt counts in ascending order
    for star in sorted(attempts_by_star.keys()):
        if 'boom_star' in locals() and star == boom_star:
            print(f"{star:2d} → 0  : BOOM after {attempts_by_star[star]} attempts")
        else:
            print(f"{star:2d} → {star+1:2d} : {attempts_by_star[star]} attempts")


if __name__ == "__main__":
    manual_simulation()