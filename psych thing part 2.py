gender = str(input("Are you a male or a female?"))
if gender == "female" :
    #age
    fage = str(input("Enter your age range for female user, 18-25, 26-35, 36-45, 46-55, 56-65: "))
    fmage = str(input("What age group do you want your partner from: "))
    if fmage == "18-25" :
        agenum = 0
    elif fmage == "26-35" :
        agenum = 1
    elif fmage == "36-45" :
        agenum = 2
    elif fmage == "46-55" :
        agenum = 3
    elif fmage == "56-65" :
        agenum = 4
    #nationality
    fnation = str(input("Enter your nationality: "))
    fmnation = str(input("What nationality do you want your partner to be from?: "))
    fcycle = int(input("In how many days is the start of your ovulation cycle?(answer in just number, for example 3): "))
    #attitude
    fkindness = int(input("How would you describe your kindness on a scale of 1-10?: "))
    fmkindness = int(input("How kind do you prefer your partner 1-10?: "))
    fattention = int(input("How much attention do you like on a scale of 1-10?: "))
    fmattention = int(input("How much attention do you like to give your partner on a scale of 1-10?: "))
elif gender == "male" :
    #age
    fage = str(input("Enter your age range for male user, 18-25, 26-35, 36-45, 46-55, 56-65: "))
    fmage = str(input("What age group do you want your partner from: "))
    if fmage == "18-25" :
        agenum = 0
    elif fmage == "26-35" :
        agenum = 1
    elif fmage == "36-45" :
        agenum = 2
    elif fmage == "46-55" :
        agenum = 3
    elif fmage == "56-65" :
        agenum = 4
    #nationality
    fnation = str(input("Enter your nationality: "))
    fmnation = str(input("What nationality do you want your partner to be from?: "))
    #attitude
    fkindness = int(input("How would you describe your kindness on a scale of 1-10?: "))
    fmkindness = int(input("How kind do you prefer your partner 1-10?: "))
    fattention = int(input("How much attention do you like on a scale of 1-10?: "))
    fmattention = int(input("How much attention do you like to give your partner on a scale of 1-10?: "))
else:
    print("Invalid Input")
#partners time to work
print("\nNow ask your partner to answer these questions:")
#age
page = str(input("Enter your age range for male user, 18-25, 26-35, 36-45, 46-55, 56-65: "))
ppage = str(input("What age group do you want your partner from?: "))
if page == "18-25" :
    agenum1 = 0
elif page == "26-35" :
     agenum1 = 1
elif page == "36-45" :
     agenum1 = 2
elif page == "46-55" :
     agenum1 = 3
elif page == "56-65" :
     agenum1 = 4
#nationality
pnation = str(input("Enter your nationality: "))
ppnation = str(input("What nationality do you want your partner to be from?: "))
#attitude
pkindness = int(input("How would you describe your kindness on a scale of 1-10?: "))
ppkindness = int(input("How kind do you prefer your partner 1-10?: "))
pattention = int(input("How much attention do you like on a scale of 1-10?: "))
ppattention = int(input("How much attention do you like to give your partner on a scale of 1-10?: "))
#compare
#age
diff = abs(agenum - agenum1)
if 0 <= diff <= 4:
    agepercentage = 100 - diff * 25
else:
    agepercentage = 0
#add the other age thing aswell
#nationality
if fmnation == pnation or ppnation == fnation :
    nationalitypercentage = 100
else:
    nationalitypercentage = 50
# kindness
if pkindness == fmkindness or ppkindness == fkindness:
    kindpercentage = 100
elif pkindness - fmkindness == 1:
    kindpercentage = 98
elif pkindness - fmkindness == 2:
    kindpercentage = 95
elif pkindness - fmkindness == 3:
    kindpercentage = 90
else:
    kindpercentage = 40
#attention
if abs(ppattention - fattention)>=5 :
    attentionpercentage = 100
else:
    attentionpercentage = 10
totalpercentage = (agepercentage + nationalitypercentage + kindpercentage + attentionpercentage)/4
print("\nCompatibility Results:")
print("Compatibility: ", totalpercentage, "%")
if fmkindness <5:
    print("\nTo increase percentage buy yourself a hot beverage on your next date.")
else:
    print("\nTo increase percentage buy yourself a cold beverage on your next date.")
print("To increase the percentage go on your next date in", fcycle,"days")