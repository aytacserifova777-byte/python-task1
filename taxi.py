#mesafeni ve saati daxil edin 
mesafe=int (input("mesafeni daxil edin:"))
saat=int(input("saati daxil edin:"))
# gedis 2 aznden baslayir ve 1 km ocun 0,80azn elave olur
gedis=2+mesafe*0.80
print("gedis:",gedis)
#gece saatlari 23:00-06:00 arasi 20% artir
if saat>=23 or saat<=6:
   gedis=gedis *1.2
   print("gece saatlari 20% artir:")