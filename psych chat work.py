# helper dictionary for age ranges
age_map = {
    "18-25": 0,
    "26-35": 1,
    "36-45": 2,
    "46-55": 3,
    "56-65": 4
}

gender = str(input("Are you a male or a female? "))

if gender.lower() == "female":
    # age
    fage = str(input("Enter your age range for female user (18-25, 26-35, 36-45, 46-55, 56-65): "))
    fmage = str(input("What age group do you want your partner from? "))
    agenum = age_map.get(fmage, -1)  # fallback -1 if invalid

    # nationality
    fnation = str(input("Enter your nationality: "))
    fmnation = str(input("What nationality do you want your partner to be from? "))

    # cycle
    fcycle = int(input("In how many days is the start of your ovulation cycle? (just a number): "))

    # attitude
    fkindness = int(input("How would you describe your kindness on a scale of 1-10? "))
    fmkindness = int(input("How kind do you prefer your partner 1-10? "))
    fattention = int(input("How much attention do you like on a scale of 1-10? "))
    fmattention = int(input("How much attention do you like to give your partner on a scale of 1-10? "))

elif gender.lower() == "male":
    # age
    mage = str(input("Enter your age range for male user (18-25, 26-35, 36-45, 46-55, 56-65): "))
    fmage = str(input("What age group do you want your partner from? "))
    agenum = age_map.get(fmage, -1)

    # nationality
    mnation = str(input("Enter your nationality: "))
    fmnation = str(input("What nationality do you want your partner to be from? "))

    # attitude
    mkindness = int(input("How would you describe your kindness on a scale of 1-10? "))
    fmkindness = int(input("How kind do you prefer your partner 1-10? "))
    mattention = int(input("How much attention do you like on a scale of 1-10? "))
    fmattention = int(input("How much attention do you like to give your partner on a scale of 1-10? "))

# partner’s turn
print("\nNow ask your partner to answer these questions:")

# age
page = str(input("Enter your age range (18-25, 26-35, 36-45, 46-55, 56-65): "))
ppage = str(input("What age group do you want your partner from? "))
agenum1 = age_map.get(page, -1)

# nationality
pnation = str(input("Enter your nationality: "))
ppnation = str(input("What nationality do you want your partner to be from? "))

# attitude
pkindness = int(input("How would you describe your kindness on a scale of 1-10? "))
ppkindness = int(input("How kind do you prefer your partner 1-10? "))
pattention = int(input("How much attention do you like on a scale of 1-10? "))
ppattention = int(input("How much attention do you like to give your partner on a scale of 1-10? "))

# --- compare ---
# age
if agenum != -1 and agenum1 != -1:
    diff = abs(agenum - agenum1)
    if 0 <= diff <= 4:
        agepercentage = 100 - diff * 25
    else:
        agepercentage = 0
else:
    agepercentage = 0

# nationality (basic match check)
nationality_match = 100 if fmnation.lower() == pnation.lower() else 0

# results
print("\n--- Compatibility Results ---")
print(f"Age compatibility: {agepercentage}%")
print(f"Nationality compatibility: {nationality_match}%")
