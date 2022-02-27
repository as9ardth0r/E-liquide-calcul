from os import system, name  

def clear(): 
  
    
    if name == 'nt': 
        _ = system('cls') 
  
    
    else: 
        _ = system('clear') 

print("Sélectionner votre base")
print("1  70/30")
print("2  50/50")
print("3  30/70")
print("4  20/80")
print("5  0/100")
pgvg = input("Enter votre choix (1/2/3/4/5) \n")
if pgvg not in ('1', '2', '3', '4', '5'):
	print("Faites votre choix entre 1 et 5 \n")

print("Sélectionner la quantité de nicotine")
tauxnicotine = input("Enter votre choix entre 0, 3, 6, 9 ou 12 \n")
if tauxnicotine not in ('0', '3', '6', '9', '12'):
	print("Enter votre choix entre 0, 3, 6, 9 ou 12 \n")

print("Sélectionner la quantité totale de e-liquide voulu \n")
liquide = input("Enter votre choix en ML \n")
liquide2 = int(liquide)
nicotineBooster = 20
if pgvg == "1":
	concentration = float('9.6')
if pgvg == "2":
	concentration = float('12')
if pgvg == "3":
	concentration = float('15.9')
if pgvg == "4":
	concentration = float('17.6')
if pgvg == "5":
	concentration = float('20')
    
    
arome = liquide2 * (concentration / 100.00); 
booster = int(liquide) * int(tauxnicotine) / int(nicotineBooster)
base = int(liquide) - (int(booster) + int(arome));

clear() 

print("Pour votre préparation il vous faut " + str(round(base)) + "ML de base")
print(str(round(booster)) + "ML de booster de nicotine")
print('et de ' + str(round(arome)) + 'ML d\'arôme')