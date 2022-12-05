
'''
Fonction qui retourne la représentation 2D des municipalités sous forme de liste de liste 
Etree : nom de fichier de l'exemplaire
Sortie : matrice sous forme de liste de liste de la représentation 2D des municipalités
'''



'''
1ere version de la fonction qui calcule le nombre de municipalités par circonscriptions k 
Entree : nombre total des municipalités n 
         le paramètre d’entrée m
Sortie : entier k le nombre de municipalités par circonscriptions 
'''
def calcul_k(n,m):
    return n // m

# # test de la fonction calcul_distanc:
# print(calcul_k(20,3))

'''
Fonction qui calcule la distance manhattan entre deux municipalités 
Entree : deux variables x et y qui représente les coordonnées des deux municipalités 
Sortie : entier qui représente la distance calculée
'''
def calcul_distance(x,y) :
    distance = abs(x[0]-y[0]) + abs(x[1]-y[1])
    return distance

# # test de la fonction calcul_distanc:
# print(calcul_distance((1,0),(2,2)))


file_name = "exemplaires/5_10_0.txt"

with open(file_name, 'r') as f: 
    d = f.readline().split(" ")
    n = int(d[0]) * int(d[1])
    m = 16
    k = calcul_k(n,m)
    distance_max = (n // (2*m)) + 1
    print("distance_max: ", distance_max)
    print(k)

    liste_des_circonscriptions = []
    circonscription = []

    compteur_max = (k//2) + 1
    compteur = 0
    for i in range(int(d[1])):
        line = f.readline().split("  ")
        #print(line)
        for j in range(int(d[0])):
            if int(line[j]) > 50 :
                if i == j == 0 :
                    circonscription.append((int(line[j]), str(i)+","+str(j)))
                    compteur+=1
                elif calcul_distance((i,j-1),(i,j)) < distance_max :
                    circonscription.append((int(line[j]), str(i)+","+str(j)))
                    compteur+=1
            if compteur == compteur_max :
                liste_des_circonscriptions.append(circonscription)
                compteur = 0
                circonscription = []
    for x in liste_des_circonscriptions:
        print(x)





'''
  i=0
    j=0
    
    line = f.readline().split("  ")
    if int(line[j]) > 50 :
        circonscription.append((int(line[j]), str(i)+","+str(j)))
        compteur+=1
    if compteur == compteur_max :
        liste_des_circonscriptions.append(circonscription)
        compteur = 0
        circonscription = []
    i+=1'''
