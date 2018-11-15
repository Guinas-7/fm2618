

dateInput = input("write a date in dd/mm/yyyy format");
if len(dateInput) ==10:
    if (dateInput[2] =="/") & (dateInput[5] =="/"):
            if (int(dateInput[0])*10+int(dateInput[1])<=31):
                print("goodformat")
