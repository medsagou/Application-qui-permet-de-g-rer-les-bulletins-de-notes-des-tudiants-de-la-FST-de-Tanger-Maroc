import os

from os import chdir
dossier = chdir("C:\\Users\\pc\\Desktop\\Formulaire  Python .csv~1\\Formulaire  Python .csv~1")










class personnes():
    
       
    def __init__(self,NF="",sep="@"):       
        self.nomFichier=NF
        self.separateur=sep
        self.nom_per=NF
        
    
    #___________________

    def lire_Contenu_Fichier(self):
         with open(self.nomFichier,'r',encoding="utf8", errors='ignore') as F:   # Ouverture du fichier en mode lecture.
           return F.readlines()
       
    def existe_fichier(self):         ###########################
         if os.path.isfile(self.nomFichier):
             return True
         else:
             return False    
       
    def afficher_nom_prenom(self):
        print("nom               prenome\n")
        T=self.existe_fichier()
        if T==True:
            L=self.lire_Contenu_Fichier()
            for element in L:
                espace='                  '
                K=element.split(self.separateur)
                for j in range(len(str(K[2]))):
                    espace=espace.replace(' ','',1)
                
                    
                print(str(K[2])+str(espace)+str(K[1]))
        else:
            print("\nle programme n'est pas trouve le fichier des personnes!!\n")
      
    def count_nbr_personnes(self):
        T=self.existe_fichier()
        if T==True:
            L=self.lire_Contenu_Fichier()
            return len(L)
        else:
            print("\nle programme n'est pas trouve le fichier des personnes!!\n")
      
            
    def count_nbr_femme(self):
        T=self.existe_fichier()
        if T==True:
            count=0
            F='Une femme'
            L=self.lire_Contenu_Fichier()
            for element in L:
                K=element.split(self.separateur)
                if F in K:
                    count+=1
                
            return count      
                
        else:
            print("\nle programme n'est pas trouve le fichier des personnes!!\n")
            
    def count_nbr_homme(self):
        T=self.existe_fichier()
        if T==True:
            count=0
            F='Un homme'
            L=self.lire_Contenu_Fichier()
            for element in L:
                K=element.split(self.separateur)
                if F in K:
                    count+=1
                
            return count      
                
        else:
            print("\nle programme n'est pas trouve le fichier des personnes!!\n")
            
            
                   
    def chercher_Nom(self):
        print("\n")
        self.nom_per =input("\nEntrez le nom de personne a cherche :--> ")
        print(' ')
        T=self.existe_fichier()
        E=['Horodateur','pernom','nom','la date de naissance','genre','niveau scolaire']
        D={}
        T2=False
        if T==True:
            L=self.lire_Contenu_Fichier()
            for element in L:
                K=element.split(self.separateur)
                for i in range(len(K)):
                    if self.nom_per==K[i]:
                       for j in range(len(E)):
                           D[E[j]]= K[j]
                       T2=True
            if T2==False:
                print("\nil n'existe aucun person interrogees avec le nom {} .".format(self.nom_per)) 
            else:
                for c,v in D.items():
                    espace='                             '
                    for j in range(len(str(c))):
                        espace=espace.replace(' ','',1)
                    print(str(c)+str(espace)+str(v))       
                
        else:
            print("\nle programme n'est pas trouve le fichier des personnes!!\n")
                   
'''            
test=personnes()
test.nomFichier='Personnes_VBA.txt'

test.afficher_nom_prenom()
print(test.count_nbr_personnes())
print(test.count_nbr_femme())
print(test.count_nbr_homme())

test.chercher_Nom()'''
      













