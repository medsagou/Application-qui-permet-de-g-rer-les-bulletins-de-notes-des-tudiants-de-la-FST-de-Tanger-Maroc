# =============================================================================
# class  menu
# =============================================================================
L=["1. cherhcer un enquête.", "2. chercher un person." ,"3. le nombre total des personnes."]

#if 1
L1=["1. Affichier les information sur l'enquête.",
   "2. Affichier les informations ur les questions de l'enquête."
   "3. le nombres des personnes interrogees."
   "4. le nombre de feminines interrogees."
   "5. le nombre de masculins interrogees."]

#if 2
L2=["1. Affichier les infomations sur ce person.","2. Affichier les reponses donnees."]



# =============================================================================
# class fichier
# =============================================================================
import datetime as datetime
import os

from os import chdir
dossier = chdir("C:\\Users\\pc\\Desktop\\Formulaire  Python .csv~1\\Formulaire  Python .csv~1")

from class_repenses import repense_question
from class_menu import Menu


class Fichier():
    #____________________________________________________________________________________________________________________________________________________________
    # Le constructeur d'une instance d'un fichier
    # Ce constructeur permet d'attribuer à une instance de fichier son nom (vide par défaut) 
    # Ce constructeur permet de spécifier le séparateur des éléments s'il existe (également vide par défaut)
    # Un séparateur peut être un ";", une "," un "#', etc.  
    def __init__(self,NF="",sep="@"):       ###########################
        self.nomFichier=NF
        self.separateur=sep
        self.nomEnquete=NF
        self.Description=NF
        self.Date_d=NF
        self.Date_f=NF
    
    #____________________________________________________________________________________________________________________________________________________________
    # Vérifie si un fichier exite ou non.
    def existe_fichier(self):         ###########################
         if os.path.isfile(self.nomFichier):
             return True
         else:
             return False


    def specifier_info_enquet(self):  ###########################
        print("\n")
        D=input("Entrez la description de votre enquet :\n")
        D= D.replace("\n",".")
        self.Description=D
        
    def specifier_nom_enquet(self):  ###########################
        print("\n")
        self.nomFichier=input("Entrez le nom votre fichier (Entrer Formulaire.txt): "+"\n")
    

        
    def specifier_dates(self):     #############################
        J=self.lire_Contenu_Fichier()
        H=J[1].split(',')
        date_debu=H[0]
        K=J[-1].split(',')
        date_fin=K[0]
        return date_debu,date_fin

    def creer_fichier_1(self):
        f = open(self.nomFichier,"x") #Création d'un fichier vide. Ici, le fichier n'est pas écrasé contrairement au mode 'w'  
        f.close()
    
    #____________________________________________________________________________________________________________________________________________________________
    # Créer un fichier vide avec suppression du fichier de même nom s'il existe
    def creer_fichier_2(self):
        f = open(self.nomFichier,"w") #Création d'un fichier vide. Ici, le fichier existant qui porte le même nom est écrasé contrairement mode 'x'  
        f.close()

    def creer_fichier_3(self):
        if os.path.exists(self.nomFichier):         # Condition pour vérifier si jamais le fichier à créer existe déjà dans le répertoire courant
            print("Il existe un fichier qui porte le même nom"+"\n")
            print("Voulez-vous l'écraser ?")
            while True:                             # Itération (boucle infinie) pour prévenir les événetuelles erreurs de frappe (autre chose que '1' et '2') (Attention, il faut absolument provoquer quelque part dans la boucle une rupture avec "break" )
                # Menu local pour exposer les dexu cas de figures (on peut également créer une instance de la classe Menu ici)
                print("Veuillez choisir ce qu'il faut faire, selon les options suivantes : "+"\n")
                print("1. Ecraser le fichier existant")
                print("2. Garder le fichier")
                rep=input("Veuillez taper 1 ou 2 ")
                if rep=='1':                        # Cas où l'utilisateur choisit d'écraser le fichier existant 
                    self.creer_fichier_2()          # Appel à laméthode creer_fichier_2()
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                elif rep=='2':                      # Cas où l'utilisateur choisit de ne pas écraser le fichier existant (pas besoin dans ce cas de faire appel à la méthode creer_fichier_1()) 
                    break                           # rupture de la boucle d'itération => on sort de la boucle infinie while
                else:                               # cas où l'utilisateur n'a tapé ni "1", ni"2"
                    print("Erreur de frappe"+"\n")
        else:                                       # cas où le fichier à créer n'existe pas dans le répertoire courant
            self.creer_fichier_1()                  # Appel à laméthode creer_fichier_1()
    


     #____________________________________________________________________________________________________________________________________________________________
     # Lire le contenu d'un fichier et le retourne en le plaçant dans une liste
    def lire_Contenu_Fichier(self):
         with open(self.nomFichier,'r',encoding="utf8", errors='ignore') as F:   # Ouverture du fichier en mode lecture.
           return F.readlines()

        

##############################################################################################################
    def get_dates(self):
        L=self.lire_Contenu_Fichier()
        A=L[1]
        B=A.split(',')
        self.Date_d=B[0]
        A=L[-1]
        B=A.split(',')
        self.Date_f=B[0]

    def separe_les_questions(self):
        L=self.lire_Contenu_Fichier()
        A=L[0].split(',')
        J=[]
        les_questions_rep=[]
        
        for element in A:
            if element not in [',','','\n',' ']:
                J.append(element)
        
        #=======================================================
        #pour afficher la liste des question.
        #les questions dans un tableux
        liste_des_question_sans_tableu=[]
        liste_des_index=[]
        c=0
        
        for element in J:
            
            c+=1
            if '[' in element:
                liste_des_index = liste_des_index + [c]
                K=''
                for i in range(len(element)):
                    if str(element[i]) != '[':
                        K=str(K)+str(element[i])
                    else:
                        if K not in les_questions_rep:
                            les_questions_rep.append(K) # la liste finale
                        break
                else:
                    continue
            else:
                liste_des_question_sans_tableu.append(element)
            
        
        dic_les_question_rep={}
        for i in range(len(les_questions_rep)):
            liste_categorie=[]
            for element in J:
                   if les_questions_rep[i] in element:
                       S=element.replace(les_questions_rep[i], '')
                       S=S.replace('[','')
                       S=S.replace(']','')
                       liste_categorie.append(S)
                       
            dic_les_question_rep[les_questions_rep[i]]=liste_categorie
                
        return liste_des_question_sans_tableu,dic_les_question_rep
    

        
    def fichier_questions_1(self):
        K,D=self.separe_les_questions()
        N=self.nomEnquete
        sep=self.separateur
        sep2='&'
        ch=str(N)
        for i in range(len(K)):
            ch=ch+sep+K[i]
       
        for c,v in D.items():
            ch=ch+sep+str(c)+sep2+str(v)+sep2
        nomfile='Questions.txt'
        f = open(nomfile,"w")
        f.write(ch)
        f.write(self.Description)
        f.close()        
        '''print("Action est Termine!!")                                              
        print("le nom de votre fichier est :",nomfile)'''
        
    
    
    
    
    
    def separe_les_questiions_2(self):
        L=self.lire_Contenu_Fichier()
        A=L[0].split(',')
        J=[]
        
        for element in A:
            if element not in [',','','\n',' ']:
                element=element.replace('\n','')
                J.append(element)
        return(J)
        
      
    def get_les_info(self):
        self.nomFichier='Formulaire.txt'
        self.titre='Vetement bejoux accessoires'
        self.Description =''
        L=self.lire_Contenu_Fichier()
        k=L[-1].split(',')
        self.Date_f =k[0]
        k=L[1].split(',')
        self.Date_d = k[0]
        return self.titre,self.Description,self.Date_d,self.Date_f
        
    def fichier_questions_2(self):
        J=self.separe_les_questiions_2()
        sep=self.separateur
        nomfile='Questions.txt'
        ch=''
        for elements in J:
            if elements != "Horodateur":
                ch=ch+str(elements)+sep
        f = open(nomfile,"w")
        f.write(ch)   
        f.write('\n')                                                      

        f.write(self.titre)
        f.write('\n')
        f.write(self.Description)
        f.write('\n')
        
        f.write(self.Date_d)
        f.write('\n')
        f.write(self.Date_f)
        f.close()                                                       
        '''print("le nom de votre fichier est :",nomfile)'''


    
    def separe_les_personnes(self):
        nomperfile='Personnes.txt'
        
        J=self.lire_Contenu_Fichier()
        J.pop(0)
        sep=self.separateur
        f = open(nomperfile,"w")
        f.close()
        for i in range(len(J)):
            ch=''
            info=[]
            H=J[i].split(',')
            for j in range(0,6,1):
                info.append(H[j])
            
            for i in range(len(info)):
                ch=ch+info[i]+sep
            f = open(nomperfile,"a")
            f.write(ch)
            f.write('\n')
               
        
        f.close()
        # cetter partie pour obtien la date de debut et la date de fin
        f=open(nomperfile,'r')
        L_D=f.readlines()
        f.close()
        De=L_D[1].split('@')
        self.Date_d=De[0]
        Df=L_D[-1].split('@')
        self.Date_d=Df[0]
        

    
        '''print("Action est Termine!!")
        print("le nom de votre fichier est :",nomperfile)'''






    def separe_les_repenses(self):
        nomrepensefile='Repenses.txt'
        Q=self.separe_les_questiions_2()
        J=self.lire_Contenu_Fichier()
        J.pop(0)
        sep=self.separateur
        
        sep2="#" #pour separe les question et les repense
        
        
        for i in range(len(J)):
                ch=''
                repens={}
                H=J[i].split(',')
                for j in range(1,len(H)):
                    repens[Q[j]]= H[j]
                  
                
        f = open( nomrepensefile,"w")
        f.close()
        for i in range(len(J)):
            ch=''
            repens={}
            H=J[i].split(',')
            for j in range(1,len(H)):
                repens[Q[j]]= H[j]
            for c,v in repens.items():
                ch=ch+sep+c+sep2+v
            f = open(nomrepensefile,"a",encoding="utf8", errors='ignore')
            f.write(ch)  
        f.close()  
          
        '''print("\nAction est Termine!!")
        print("----le nom de votre fichier est :",nomrepensefile,"----")'''
        
    def creer_Fomulaire_sans_questions(self):
        nom="Formulaire_sans_questions.txt"
        J=self.lire_Contenu_Fichier()
        J.pop(0)
        with open (nom,'w',encoding="utf8", errors='ignore') as f:
            f.writelines(J)
    
    
    def questionnaire_sur_python(self):
        repenses_f= repense_question()
        A=repenses_f.lire_les_quesiton()
        B=repenses_f.lire_les_repense()
        L=A[0].split("@")
        J=B.split("#")
        liste_menu=Menu()
        ch=''
        
        
        save_data=[]
        date_maintenant = str(datetime.datetime.today())
        save_data.append(date_maintenant)
        if L[-1]=='\n':
            L.pop(-1)
        i=0
        for j in range(2):
            i+= 1
            Data= input(str(i)+'. '+str(L[j])+': ')
            save_data.append(Data)
        
        i+=1
        print(str(i)+'. '+str(L[2])+': ')
        while True:
            try:
                DD = int(input("--le jour: "))
                assert DD > 0 and DD <= 31
            except ValueError:
                print("\n!!!Veuillez saisir un nombre entier!!!")
            except AssertionError:
                print("\n!!!  Invalid valeur  !!!\n")   
            else: 
                break
        while True:
            try:
                MM = int(input("--le moins: "))
                assert MM > 0 and MM <= 12
            except ValueError:
                print("\n!!!Veuillez saisir un nombre entier!!!")
            except AssertionError:
                print("\n!!!  Invalid valeur  !!!\n")   
            else: 
                break
            
        while True:
            try:
                YY = int(input("--Annee: "))
                assert YY > 1900 and YY <= 2018
            except ValueError:
                print("\n!!!Veuillez saisir un nombre entier!!!")
            except AssertionError:
                print("\n!!!  Invalid valeur  !!!\n")   
            else: 
                break
        
        Data=str(MM) + "/"+ str(DD) + "/" +str(YY)
        save_data.append(Data)
        
    
        for df in range(3,len(J)):
            liste_menu.list=[]
            i+=1
            K=J[df].split("@")
            
            F=K[1].split(',')
            print(str(i)+'. '+str(L[i-1]+',\n Type :'+str(K[0])))
            for j in range(len(F)):
                liste_menu.list.append(F[j])
            liste_des_choix=liste_menu.list
            liste_menu.afficher_menu()
            Data_number=liste_menu.choix()
            Data=liste_des_choix[Data_number]
            save_data.append(Data)
        for element in save_data:
            ch=ch+str(element)+ ','
        
        L_global=["Energester les reponses.","Afficher les reponses","retour."]
        TEST_ER= True
        while TEST_ER == True:
            Menu_global=Menu()
            Menu_global.list=L_global
            Menu_global.afficher_menu()
            Choix=Menu_global.choix()
            
            if Choix == 0:
                ch_sans=ch[:-1]
                with open('Formulaire.txt','a',encoding="utf8", errors='ignore') as F:
                    F.write('\n')
                    F.writelines(ch_sans)
                with open('Formulaire_sans_questions.txt','a',encoding="utf8", errors='ignore') as F:
                    F.write('\n')
                    F.writelines(ch_sans)
                TEST_ER=False
            elif Choix == 1:
                for j in range(len(L)):
                    print(str(j+1)+'. '+str(L[j])+" :"+str(save_data[j+1]))
        
            elif Choix == 2:
                TEST_ER=False
 
            






    def get_info_enquet(self):
        T=self.existe_fichier()
        if T==True:
            J=self.lire_Contenu_Fichier()
            Titre=J[1]
            description=J[2]
            date_de_debut=J[3]
            date_de_fin=J[-1]
            return Titre,description,date_de_debut,date_de_fin
        else:
            Titre='aucun information'
            description='aucun information'
            date_de_debut='aucun information'
            date_de_fin='aucun information'
            return Titre,description,date_de_debut,date_de_fin
           
       
        
        
        
        
        
        
        
'''Fichier_de_questionnaire=Fichier()
Fichier_de_questionnaire.questionnaire_sur_python()   '''
        
        
        
        
        
                    
        
        
#==================================================================
'''Fichier_de_questionnaire=Fichier()
Fichier_de_questionnaire.nomFichier="Formulaire.txt"
Fichier_de_questionnaire.nomEnquete="VBA"
Fichier_de_questionnaire.Description ="some description to test"

Fichier_de_questionnaire.Date_d,Fichier_de_questionnaire.Date_f=Fichier_de_questionnaire.specifier_dates()

Fichier_de_questionnaire.specifier_info_enquet()
T=Fichier_de_questionnaire.existe_fichier()

if T==True:
    print("le fichier existe")
elif T==False:
    print("le fichier n'existe pas")

#===================================================================
Fichier_de_questionnaire.fichier_questions_2()
Fichier_de_questionnaire.separe_les_repenses()

Fichier_de_questionnaire.separe_les_personnes()





for i in range(1,len(K),1):
    print(str(i)+". "+str(K[i]))
    print(" ")
for c,v in L.items():
    i+=1
    print(str(i)+". "+str(c),end=" ")
    for element in v:
        print(str(element)+",",end=" ")
    print('\n')'''
    
#Fichier_de_questionnaire.fichier_questions()'''
    

    
    
    

