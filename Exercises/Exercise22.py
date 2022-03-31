def celtofah(cel):
    fah = cel*(9/5) + 32
    return fah

celsius = int(input("Enter the first amount in Celsius: "))
faht = int(input("Enter the last amount in Celsius: "))

print("CELSIUS\tFAHRENHEIT")
for i in range(celsius,faht+1):
    print(i,"\t","{0:.1f}".format(celtofah(i)))