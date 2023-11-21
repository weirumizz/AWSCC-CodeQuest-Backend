decide = input(f"A man has asked for shelter. Would you let him in? YES or NO: ")

if str(decide) == 'YES' or str(decide) == 'yes' or str(decide) == 'Yes':
    decide2 = input(f"Police has arrived. Have you seen the thief? YES or No: ")
    if str(decide2) == 'YES' or str(decide2) == 'yes' or str(decide2) == 'Yes':
        print(f"WIN! The thief has been caught!")
    elif str(decide2) == 'NO' or str(decide2) == 'no' or str(decide2) == 'No':
        print(f"GAME OVER.")
    else:
        print(f"ERROR! INPUT INVALID.")

elif str(decide) == 'NO' or str(decide) == 'no' or str(decide) == 'No':
    decide3 = input(f"The thief attacked you. Knock him down? YES or NO: ")
    if str(decide3) == 'YES' or str(decide3) == 'yes' or str(decide3) == 'Yes':
        print(f"wIN! The thief couldn't stand a chance against you.")
    elif str(decide3) == 'NO' or str(decide3) == 'no' or str(decide3) == 'No':
        print(f"GAME OVER.")
    else:
        print(f"ERROR! INPUT INVALID.")

else:
    print(f"ERROR! INPUT INVALID.")