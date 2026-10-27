#iki oyuncu novbe ile secimini yazir das qayci kagiz
secim1=input("oyuncu 1 secimini yazir:")
secim2 =input ("oyuncu 2 secimiz yazir:")
if secim1 == secim2:
    print("berabere")
elif secim1=="das" and secim2=="qayci":
    print("oyuncu 1 qazanie:")
elif secim1=="qayci" and secim2=="kagiz":
    print("pyuncu 1 qazanir:")
elif secim1=="kagiz" and secim2=="das":
    print("oyuncu 1 qazanir:")
elif secim1=="yanlis soz " or secim2=="yansil soz":
    print("bele secim yoxdur:")    