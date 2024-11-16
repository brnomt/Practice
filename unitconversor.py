#Conversor de unidades

#A few days ago I asked ChatGPT to give me some stuff to code and practice a bit
#Today it told me to do a a unit conversor.

#I experimented a bit with classes and methods on this one, just to try them a bit
#This was fun to make, but a lit confusing, since it have been a while since i don't code
#I know i can make some try catch n stuff, but, to practice, i think it's okay :p

#https://github.com/brnomt


class temperatures():
    def c_to_f(celc):
        #(0 °C × 9/5) + 32 = 32 °F

        res = (celc * 1.8) + 32
        return res
    
    def f_to_c(far):
        #(32 °F − 32) × 5/9 = 0 °C

        res = (far -32) * 0.555
        return round(res,1)

class weights():
    def kg_to_lb(kg):
        #1kg = 2.2lb
        res = kg * 2.2
        return round(res,2)
    
    def lb_to_kg(lb):
        res = lb /2.2
        return round(res,2)

class distances():
    def mts_to_feet(mts):
        # 1 meter = 3.28084 feet
        res = mts * 3.28084
        return round(res, 2)
    
    def feet_to_mts(feet):
        # 1 foot = 0.3048 meters
        res = feet * 0.3048
        return round(res, 2)


print("What you want to convert?")
print("1.- Temps\n2.-Weigh\n3.-Distance\n4.-Exit")
print("Select your option: ")
opc = int(input())

if opc not in (1, 2, 3):
    print("bye!")
    exit()

if opc == 1:
    opc = 0
    print("1.-C° to F°\n2.-F° to C°")
    opc = int(input("Select your option: "))

    if opc == 1:
        print("Please, input the temperature in Celcius: ")
        c = float(input())
        print(f"{c}°C, is {temperatures.c_to_f(c)}°F.")

    if opc == 2:
        print("Please, input the temperature in Farenheit: ")
        f = float(input())
        print(f"{f}°F, is {temperatures.f_to_c(f)}°C.")

if opc == 2:
    #Weigh
    opc = 0
    print("1.-KG° to lb°\n2.-lb° to KG°")
    opc = int(input("Select your option: "))
    
    if opc == 1:
        opc = 0
        k = float(input("Please, input the weight in Kilograms: "))
        print(f"{k} Kilograms in pounds are: {weights.kg_to_lb(k)}lb.")

    if opc == 2:
        opc = 0
        l = float(input("Please, input the weight in pounds: "))
        print(f"{l} pounds in kilograms are: {weights.lb_to_kg(l)}kg.")

if opc == 3:
    op = 0
    print("1.- Meters to Feet\n2.- Feet to Meters")
    opc = int(input("Select your option: "))

    if opc == 1:
        opc = 0
        mts = float(input("Please, input the distance in meters: "))
        print(f"{mts} meters is {distances.mts_to_feet(mts)} feet.")


    if opc == 2:
        feet = float(input("Please, input the distance in feet: "))
        print(f"{feet} feet is {distances.feet_to_mts(feet)} meters.")