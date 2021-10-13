has_high_income=False
has_good_credit=True
has_criminal_record=False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

tempearture =31

if tempearture>30:
    print ("It's a hot day")
else:
    print("It's not a hot day")

if tempearture==30:
    print ("It's a hot day")
else:
    print("It's not a hot day")

name= "Sham"

print(len(name))

if len(name)<3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name must be max 50 characters")
else:
    print("Name all good!")

