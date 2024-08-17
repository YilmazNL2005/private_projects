from string import ascii_lowercase
while True:
    def get_letter() -> str:
        vraag_letter = input("Typ 1 letter. ")
        if vraag_letter not in ascii_lowercase:
            print("Je moet wel een kleine letter invullen.")
        elif len(vraag_letter) != 1:
            print("Voer 1 letter in!")
        else:
            return print(vraag_letter)
    break

geraden_letter = get_letter()

te_raden = "astronaut"
status_woord = "_"
status_woord = status_woord * len(te_raden)
print(len(status_woord))

if str(geraden_letter) in str(te_raden):
    print("Zit er in.")
for x in range(len(te_raden)):
    if geraden_letter == te_raden[x]:
        status_woord[x] = geraden_letter
    print(status_woord)



# 1 vraag de gebruiker om een letter.
# 2 check of de letter in het woord zit.


# 3a Ja. Letter plaatsen (a____a____)
# 3b Nee. Bijhouden welke letters al genoemd zijn en hoe vaak het fout geraden is.
