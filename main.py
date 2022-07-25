



#___________________________________________________________________________________
import os

from os import chdir
dossier = chdir("C:\\Users\\pc\\Desktop\\Formulaire  Python .csv~1\\Formulaire  Python .csv~1")  #SELONF VOTRE FIHCIER DE TRAVAILE


#___________________________________________________________________________________
#partie de menu



from class_menu import Menu
from class_fichier import Fichier
from class_repenses import repense_question
from class_personnes import personnes
from stats import Traitement_Stats
from stats import * 

menu=Menu()
Fichier_de_questionnaire=Fichier()
Fichier_extraire=Fichier()

L=['Le formulaire',             ### 0.1.2
   'Informaiton sur le formulaire.',
   'Statistiques',
   'Quitter']


L0=['remplir le formulaire.',
    'Les informations sur le formulaire',
    'retour',
    'Quitter']


L1=['Afficher les informations de l enquete',   # if choix 1   0.1.2.3
    'Afficher la liste des questions',
    'Affihcer les questions et les repenses possible',
    'Les informations sur les personnes interrogees',
    'retour',
    'Quitter']


L13=['Afficher le nombre des personnes interrogees',   # if choix 3 ddans L1
     'Afficher la liste des nom-prenom des personnes interrogees',
     'Afficher le nombre des femme interrogees',
     'Afficher le nombre des hommes interrogees',
     'Chercher un nom',
     'retour',
     'Quitter']



def principale():
    TEST=True
    menu=Menu()
    Fichier_de_questionnaire=Fichier()
    Fichier_de_questionnaire.nomFichier="Formulaire.txt"
    T=Fichier_de_questionnaire.existe_fichier()
    
    if T==True:
        
                    Fichier_extraire=Fichier()
                    Fichier_de_questionnaire.get_les_info()
                    #extraire Formulaire_sans_questions_.txt et repenses.txt et questions.txt et personnes.txt par defaut
                    Fichier_de_questionnaire.fichier_questions_2() #fichier des questions Question.txt
                    Fichier_de_questionnaire.separe_les_personnes() #fichier des personnes  Personnes.txt
                    Fichier_de_questionnaire.separe_les_repenses() #fichier des repenses Repenses.txt    
                    Fichier_de_questionnaire.creer_Fomulaire_sans_questions()  # data3
                    
                    while TEST==True:
                            menu.list=L
                            menu.afficher_menu()
                            C=menu.choix()
                           
                            if C==0:
                                        TEST2=True
                                        
                                        while TEST2==True:
                                            menu2=Menu()
                                            menu2.list=L0
                                            menu2.afficher_menu()
                                            C2=menu2.choix()
                                            if str(C2)=='0':
                                                Fichier_de_questionnaire.questionnaire_sur_python()
                                                TEST2=True
                                            elif str(C2)=='1':
                                                Titre,description,date_de_debut,date_de_fin=Fichier_de_questionnaire.get_les_info()
                                                print("Titre :",str(Titre))
                                                print("Description: \n"+str(description))
                                                print("la date de debut de l'enquet :",date_de_debut)
                                                print("la date de fin de l'enquet :",date_de_fin)
                                                
                                            elif str(C2)=='2':
                                                print("\n---------------------------------------------------------------\n")
                                                print("\n################# return au menu principal  #####################\n")
                                                print("\n---------------------------------------------------------------\n")
                                                TEST=True
                                                TEST2=False                                               
                                          
                                            elif str(C2)=='3':
                                                print("\n---------------------------------------------------------------\n")
                                                print("\n#####################  Au revoir  #########################\n")
                                                print("\n---------------------------------------------------------------\n")
                                                TEST=False
                                                TEST2=False

                                        
                            elif C==1:
                                
                                TEST3=True
                                while TEST3==True:
                                            menu3=Menu()
                                            menu3.list=L1
                                            menu3.afficher_menu()
                                            C3=menu3.choix()
                                            if str(C3)=='0':
                                                    Fichier_extraire.nomFichier='Questions.txt'
                                                    Titre,desrp,date_D,Date_F=Fichier_extraire.get_info_enquet()
                                                    print("\nTitre :",str(Titre))
                                                    print("Description: \n"+str(desrp))
                                                    print("la date de debut de l'enquet :",date_D)
                                                    print("la date de fin de l'enquet :",Date_F)
                                                    
                                            elif str(C3)=='1':
                                                list_question=repense_question()
                                                list_question.nomFicherQuestions='Questions.txt'
                                                list_question.afficher_les_questions()
                                                
                                            elif str(C3)=='2':
                                                list_question=repense_question()
                                                list_question.nomFicherQuestions='Questions.txt'
                                                list_question.nomFichierR='repenses_possible.txt'
                                                list_question.afficher_les_repenses_possible()
                                                   
                                            elif str(C3)=='3':
                                                TEST4=True
                                                while TEST4==True:
                                                        menu4=Menu()
                                                        menu4.list=L13
                                                        menu4.afficher_menu()
                                                        C4=menu4.choix()
                                                        if str(C4)=='0':
                                                            nombre_per=personnes()
                                                            nombre_per.nomFichier='Personnes.txt'
                                                            N=nombre_per.count_nbr_personnes()
                                                            print("\nle nombre des personnes interrogees est :",N)
                                                        elif str(C4)=='1':
                                                            liste_per=personnes()
                                                            liste_per.nomFichier='Personnes.txt'
                                                            liste_per.afficher_nom_prenom()
                                                        elif str(C4)=='2':
                                                            nmbr_femme= personnes()
                                                            nmbr_femme.nomFichier='Personnes.txt'
                                                            N=nmbr_femme.count_nbr_femme()
                                                            print("\nle nombre des femme interrogees est :",N)
                                                        elif str(C4)=='3':
                                                            nmbr_homme= personnes()
                                                            nmbr_homme.nomFichier='Personnes.txt'
                                                            N=nmbr_homme.count_nbr_homme()
                                                            print("\nle nombre des hommes interrogees est :",N)       
                                                        elif str(C4)=='4':
                                                            chercher_nom= personnes()
                                                            chercher_nom.nomFichier='Personnes.txt'
                                                            chercher_nom.chercher_Nom()
                                                        elif str(C4)=='5':
                                                            print("\n---------------------------------------------------------------\n")
                                                            print("\n################# return au menu precedent  #####################\n")
                                                            print("\n---------------------------------------------------------------\n")
                                                            TEST=True
                                                            TEST2=True
                                                            TEST3=True
                                                            TEST4=False
                                                        elif str(C4)=='6':
                                                            print("\n---------------------------------------------------------------\n")
                                                            print("\n#####################  Au revoir  #########################\n")
                                                            print("\n---------------------------------------------------------------\n")
                                                            TEST=False
                                                            TEST2=False
                                                            TEST3=False
                                                            TEST4=False                                            
                                                            
                                          
                                            elif str(C3)=='4':
                                                print("\n---------------------------------------------------------------\n")
                                                print("\n################# return au menu precedent  #####################\n")
                                                print("\n---------------------------------------------------------------\n")
                                                TEST=True
                                                TEST2=True
                                                TEST3=False
                                            elif str(C3)=='5':
                                                print("\n---------------------------------------------------------------\n")
                                                print("\n#####################  Au revoir  #########################\n")
                                                print("\n---------------------------------------------------------------\n")
                                                TEST=False
                                                TEST2=False
                                                TEST3=False
                            
                                                
                            elif C==2:
                                traitementData = Traitement_Stats()
                                traitementData.traiterMenu_stats()
                                                                                   
                            elif C==3:   #QUITTER
                                print("\n---------------------------------------------------------------\n")
                                print("\n#####################  Au revoir  #########################\n")
                                print("\n---------------------------------------------------------------\n")
                                TEST=False
                            
                
                
                
    else:
        print("Le programme n'est pas trouve le fichier de base de donnees 'Formulaire.txt'.")





if __name__ == '__main__':
                    principale()
                    input("")
















