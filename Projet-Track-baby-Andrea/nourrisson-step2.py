# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv


# Récupération des mesures dans les fichiers à faire

# Création de la liste sur le poids caractere poids garçon (à paramétrer plus tard .... pour taille + périmètre cranien)
# genre : Valeur F pour fille ou G pour garçon (à paramétrer plus tard....)
# percent : Valeur 5,25,50,75,95 (%tage considéré dans statistiques des standards)

def creation_liste(fic_loc,percent) :
        
    L_caract_g_P_cumul = []
        
    with open(fic_loc,'r') as fic_name :
        for line in fic_name :
            L_caract_g_all = line.rstrip().split(";")    # créer une liste en ramplaçant les séparateur ';' par ','
           
            L_caract_g_P =L_caract_g_all[percent]        # Pour P05 : la liste a créer est sur les 2eme éléments (indice 1 donc)
            L_caract_g_P_cumul.append(L_caract_g_P)      # Cumuler les éléments obtenus de la liste ci-dessus

        
    del L_caract_g_P_cumul[0]                           # Supprimer l'entête comportant P05/P25/P50/P75/P95
        
    return  L_caract_g_P_cumul

Poids_fic_path = '/home/bnp-renault-005/Bureau/Andrea/GITHUB/Projet-Track-baby-Andrea/constantes-nourrissons-light/poids-age-garcon-0-60-light.csv'

# Liste Poids garçon %tage de 5 % :
L_poids_G_05_cumul=[]

L_poids_G_05_cumul= creation_liste(Poids_fic_path,1)
print(f'Poids garçon 5 % : {L_poids_G_05_cumul}')

# Liste Poids garçon %tage de 25 % :
L_poids_G_25_cumul=[]

L_poids_G_25_cumul= creation_liste(Poids_fic_path,2)
print(f'Poids garçon 25 % : {L_poids_G_25_cumul}')

# Liste Poids garçon %tage de 50 % :
L_poids_G_50_cumul=[]

L_poids_G_50_cumul= creation_liste(Poids_fic_path,3)
print(f'Poids garçon 50 % : {L_poids_G_50_cumul}')

# Liste Poids garçon %tage de 75 % :
L_poids_G_75_cumul=[]

L_poids_G_75_cumul= creation_liste(Poids_fic_path,4)
print(f'Poids garçon 75 % : {L_poids_G_75_cumul}')

# Liste Poids garçon %tage de 95 % :
L_poids_G_95_cumul=[]

L_poids_G_95_cumul= creation_liste(Poids_fic_path,5)
print(f'Poids garçon 95 % : {L_poids_G_95_cumul}')



#---------------------------------------------------------------------
# Affichage des graphiques à faire
#--------------------------------------------------------------------


