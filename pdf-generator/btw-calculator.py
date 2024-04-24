# De calculator kan voor nu maar één product/prijs hanteren en berekenen. 
# Dus eventueel een while loop maken voor regel 9

btw_hoog = 21
btw_laag = 9
huidig_percentage = 100
btw_gebruiken = 0

prijs_excl = int(input("Wat is de prijs? "))

while True:
    hoog_laag = int(input(f"Is de btw {btw_hoog} of {btw_laag} "))
    if hoog_laag == btw_hoog:
        btw_gebruiken = 21
        break    
    elif hoog_laag == btw_laag:
        btw_gebruiken = 9
        break
    else:
        print("Dat is geen gebruikte btw percentage. ")

print(f"De prijs zonder btw is {prijs_excl} euro. ")
btw_bedrag = prijs_excl / 100 * hoog_laag
print(f"De btw is {hoog_laag} procent. Dan is de btw-prijs {btw_bedrag} euro. ")
hoog_laag += 100
prijs_incl = prijs_excl / 100 * hoog_laag
print(f"De prijs inclusief de btw is {prijs_incl} euro. ")