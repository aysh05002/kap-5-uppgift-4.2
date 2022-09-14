pris=int(input("Hur mycket kostar en liter bensin? "))
if pris>0 and pris<=10:
    print("Det var billigt!")
elif pris>10 and pris<=15:
    print("Tanka full tank")
elif pris>15 and pris<=20:
    print("Tanka tio liter")
else:
    print("Nu saljer jag bilen och cyklar istallet")