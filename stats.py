
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##########################################################################################################################################################
################### ---------------------------------------- Gestion des statistiques ---------------------------------------- ###################
##########################################################################################################################################################

class Stats:
    "classe générique de gestion de statistique"

    def __init__(self,Rffichier="",sep=","):
        self.Reference = Rffichier
        self.separateur = sep

    def nombre_person(self):
        nbrperson = 0
        with open(self.Reference,'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                nbrperson += 1
        return nbrperson

    def nombre_homme(self):
        nbrhomme = 0
        with open(self.Reference,'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                l = self.extrait_liste_de_Travaille(ligne)
                if "Un homme" in l[4].capitalize():
                    nbrhomme += 1
        return nbrhomme

    def nombre_femme(self):
        nbrfemme = 0
        with open(self.Reference, 'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                l = self.extrait_liste_de_Travaille(ligne)
                if "Une femme" in l[4].capitalize():
                    nbrfemme += 1
        return nbrfemme


    def Nbr_Person_Pas_Repond(self):
        return self.nombre_person()-(self.nombre_femme()+self.nombre_homme())

    # pour les choix multiples on va construire une sous liste que quentien ses reponse :
    def Fusionner(self, l):
        #on peut poser une question en utilisateur pour donner position de les choix multipli et travaile par cette position si on a un autre fichier
        l[10] = [l[10], l[11]]
        l.remove(l[11])
        l[11] = [l[11], l[12], l[13], l[14], l[15], l[16], l[17], l[18], l[19]]
        for i in range(8):
            l.remove(l[12])
        return l

    def Fichier_De_GoogleForme_Ou_non(self):
        teste = False
        with open(self.Reference, 'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                comp = 0
                comp = ligne.count('"')
        if comp >= 40:
            teste = True

        return teste

    def extrait_liste_de_Travaille(self, ligne):
        teste = self.Fichier_De_GoogleForme_Ou_non()
        if teste == True:
            l = ligne.split('"')
            l.remove(l[0])
            for i in range(1, 26):
                l.remove(l[i])
            l.remove(l[-1])
            l.remove(l[-1])
            l = self.Fusionner(l)
        else:
            l = ligne.split(self.separateur)
            l = self.Fusionner(l)
        return l

    def affichage_liste_Data(self):
        with open(self.Reference,'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                l = self.extrait_liste_de_Travaille(ligne)
                print(l)

    def comptage(self,element,indice):
        comp = 0
        with open(self.Reference, 'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                l = self.extrait_liste_de_Travaille(ligne)
                if element in l[indice]:
                    comp += 1
        return comp

    #Quel est votre dernier niveau de scolarité complété?
    def pourcentage_niveau_scolarite(self):
        l = ['Secondaire',
             "licence ou cpge",
             "Master",
             "Doctorat",
             "Aucune de ces réponses"
             ]
        message = "Quel est votre dernier niveau de scolarité complété?"
        self.affiche_pourcentage(message,l,5)


    def dict_nbr_choix_par_person(self ,l ,i):
        dict = {}
        for j in range(len(l)):
            dict[l[j]] = self.comptage(l[j],i)
        return dict


    def affiche_pourcentage(self,message,l,indice):
        dico = self.dict_nbr_choix_par_person(l,indice)
        nbr_personne = self.nombre_person()
        nbrPersonne = []
        niveauEtude = []
        print("\npour la question :  {} \n".format(message))
        
        for c, v in dico.items():
            print("il y a comme nombre ", v, " de ",c, "dans votre Data c'est a dire en pourcentage ", format((v / nbr_personne) * 100, ".2f"), "% ", c)

            nbrPersonne += [((v/nbr_personne) * 100)] 
            niveauEtude += [c]
        
        plt.pie(nbrPersonne, labels=niveauEtude, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')
        plt.show()
    #A quelle fréquence achetez-vous des vêtements ?
    def pourcentage_Achate_vetements_bijout(self):

        while True:
            rep = input("stp veuillez saisir:  \n-> V ou v pour vetement. \n-> B ou b pour bijout. \n   ").lower()
            if rep == 'b' or rep == 'v':
                break
        l = ["Au moinsune fois toutes les 2 semaine",
             "Toutes les semaines",
             "Au moins une fois par mois",
             "Au moins une fois tous les 3 mois",
             "Au moins une fois tous les 6 mois",
             "Plus rarement"
             ]
        if rep == 'v':
            message = "A quelle fréquence achetez-vous des vêtements ?"
            self.affiche_pourcentage(message,l,7)
        elif rep == 'b':
            message = "A quelle fréquence achetez-vous des bijouts ?"
            self.affiche_pourcentage(message,l,7)
        else:
            print("Erreur")

    #En moyenne quel budget mensuel dépensez-vous pour l’achat?
    def pourcentage_moyenne_budget_achat(self):
        l = ["Moins de 200dh",
             "Entre 200dh et 499dh",
             "Ente 500dh et 999dh",
             "Entre 1000dh et 1999dh",
             "Entre 2000dh et 4999dh",
             "5000dh ou plus"
             ]
        message = "pourcentage de reponse au question : En moyenne quel budget mensuel dépensez-vous pour l’achat?"
        self.affiche_pourcentage(message,l,8)

    #Quelle est la méthode de paiement préférée ?
    def pourcentage_de_paiement_preferee(self):
        l = ['Especes',
             'Paiement carte',
             'Virement',
             'Cheque'
             ]
        message = "pourcentage de reponse au question : Quelle est la méthode de paiement préférée ?"
        self.affiche_pourcentage(message,l,9)


    def comptage2(self,element,indice1,indice2):
        comp = 0
        with open(self.Reference, 'r',encoding="utf8", errors='ignore') as mon_fichier:
            for ligne in mon_fichier.readlines():
                l = self.extrait_liste_de_Travaille(ligne)
                if element in l[indice1][indice2]:
                    comp += 1
        return comp

    def nbr_occasion_achetez(self):
        nbrcv1 = self.comptage2('Pour un cadeau',10,0)
        nbrcv2 = self.comptage2('Routine quotidienne.', 10, 0)
        nbrcv3 = self.comptage2('Pour remplacer de vieux', 10, 0)
        nbrcv4 = self.comptage2('Aucune de ces reponses', 10, 0)
        nbrcb1 = self.comptage2('Pour un cadeau',10,1)
        nbrcb2 = self.comptage2('Routine quotidienne.', 10, 1)
        nbrcb3 = self.comptage2('Pour remplacer de vieux', 10, 1)
        nbrcb4 = self.comptage2('Aucune de ces reponses', 10, 1)
        nbr_personne = self.nombre_person()
        print("\npour qustion de choix multiple : occasion d'achate\n")
        print("parmi", nbr_personne, "personnnes on a pour : \n")
        print("pour un cadeaux il y a", nbrcv1, "Vétement et", nbrcb1, "bijeaux")
        print("Rotine quotidienne il y a", nbrcv2, "Vétement et", nbrcb2, "bijeaux")
        print("Pour remplacer de vieux il y a", nbrcv3, "Vétement et", nbrcb3, "bijeaux")
        print("Aucune de ces reponses il y a", nbrcv4, "Vétement et", nbrcb4, "bijeaux")
        nbrcv = [nbrcv1,nbrcv2,nbrcv3,nbrcv4]
        nom_nbrcv =  ["Cadeaux","Routine \nquotidienne","Pour remplacer \n l'ancien","Aucune \n de ses \nréponses"]
        nbrcb = [nbrcb1,nbrcb2,nbrcb3,nbrcb4]
        nom_nbrcb = ["Cadeaux","Routine \nquotidienne","Pour remplacer \n l'ancien","Aucune \n de ses \nréponses"]
        fig, (ax1_b, ax2_v) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
        plt.suptitle('Histogrammes des personnes pour des occasions', fontsize=16)
        ax1_b.bar(nom_nbrcb,nbrcb)
        ax2_v.bar(nom_nbrcv, nbrcv,  color='green')
        ax1_b.set_title('Bijoûx')
        ax2_v.set_title('Vêtements')
        plt.subplots_adjust(left=0.2, wspace=0.2, top=0.85) # ajuster la position et l'espacement des graphes
        plt.show()

    # Où achetez-vous principalement vos vêtements/bijoux/accessoires ? ( sélectionner un ou plusieurs )
    def pourcentage_achete_principalement_vetements_bijoux_accessoires(self):
        '''l = ['Grand Magasin (ZARA LC WAIKIKI  )',
             'Boutique de pret-a-porter independante.(Magasins de quartier)',
             'Rue commerciale',
             'Internet (Amazon Marketplace Shein... )',
             'Dans les hypermarches (Carrefour Aswak Assalam)'
             ]
        message = "Où achetez-vous principalement vos vêtements/bijoux/accessoires ?"
        self.affiche_pourcentage(message,l,12)'''
        #pour jute modifier le message on va faire:
        nbr1 = self.comptage('Grand Magasin (ZARA LC WAIKIKI  )', 12)
        nbr2 = self.comptage('Boutique de pret-a-porter independante.(Magasins de quartier)', 12)
        nbr3 = self.comptage('Rue commerciale', 12)
        nbr4 = self.comptage('Internet (Amazon Marketplace Shein... )', 12)
        nbr5 = self.comptage('Dans les hypermarches (Carrefour Aswak Assalam)', 12)
        nbr_personne = self.nombre_person()
        print("\npour la question a choix multiple :  Où achetez-vous principalement vos vêtements/bijoux/accessoires ?\n")
        print("il y a",format((nbr1/nbr_personne)*100,".2f"),"% qui preferent Grand Magasin (ZARA LC WAIKIKI...)")
        print("il y a", format((nbr2 / nbr_personne) * 100, ".2f"), "% qui preferent Boutique de pret-a-porter independante.(Magasins de quartier)")
        print("il y a", format((nbr3 / nbr_personne) * 100, ".2f"), "% qui preferent Rue commerciale")
        print("il y a", format((nbr4 / nbr_personne) * 100, ".2f"), "% qui preferent Internet (Amazon Marketplace Shein... )")
        print("il y a", format((nbr5 / nbr_personne) * 100, ".2f"), "% qui preferent Dans les hypermarches (Carrefour Aswak Assalam)")


    #Suivez-vous les tendances de la mode ?
    def suivent_tendences(self):
        nbr1 = self.comptage("Je m'y interesse mais je ne les suis pas vraiment", 13)
        nbr2 = self.comptage("Non ", 13)
        nbr3 = self.comptage("Oui ", 13)
        return nbr1,nbr2,nbr3

    def affichage_pourcentage_qui_suivent_tendences(self):
        nbr1, nbr2, nbr3 = self.suivent_tendences()
        nbr_personne = self.nombre_person()
        nbrPersonne = [nbr1,nbr2,nbr3]
        labbels = ["Je m'y interesse mais je ne les suis pas vraiment", "Non je ne m'y interesse pas", "Oui je les suis etroitement"]
        print("\npour la question : Suivez-vous les tendances de la mode ? \n")
        print("il y a ",nbr1," c-a-d ",format((nbr1/nbr_personne)*100,".2f"),"%  Je m'y interesse mais je ne les suis pas vraiment")
        print("il y a ",nbr2," c-a-d ",format((nbr2 / nbr_personne) * 100, ".2f"), "%  Non je ne m'y interesse pas")
        print("il y a ",nbr3," c-a-d ",format((nbr3 / nbr_personne) * 100, ".2f"), "%  Oui je les suis etroitement")
        
        plt.pie(nbrPersonne, labels=labbels, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')
        plt.show()

    #Quelle importance accordez-vous au service de relooking ?
    def dict_choix_echelle_lineaire(self):
        dico = {}
        for i in range(1,6):
            dico[str(i)] = self.comptage(str(i),14)
        return dico

    def affichage_choix_echelle_lineaire(self):
        dico = self.dict_choix_echelle_lineaire()
        nbr_personne = self.nombre_person()
        print("\npour la question :  Quelle importance accordez-vous au service de relooking ?\n")
        print("Aucune importance :  1 - 2 - 3 - 4 - 5  : Beaucoup d’importance")
        for c,v in dico.items():
            print("il y a ", v, " c-a-d ", format((v / nbr_personne) * 100, ".2f"),"%  de",c)

    #def fichier_contient_Data_statistique(self):


class Menu_stats():
    "classe générique de gestion de menu"

    def __init__(self, L):
        self.list = L

    def afficher_menu(self):
        for i in range(len(self.list)):
            print(i + 1, " : ", self.list[i], "\n")

    def choix(self):
        while True:
            try:
                i = int(input("Selon votre choix taper un nombre entre 1 et " + str(len(self.list)) + " -->  "))
                assert i > 0
            except ValueError:
                print("! Veuillez saisir un nombre entier.\n")
            except AssertionError:
                print("! Le nombre saisi doit être supérieur à 0.\n")
            else:
                break

        return i

class Traitement_Stats(Menu_stats):  # Cette classe hérite les caractéristiques de la classe mere "Menu"
    "class pour traiter les techniques statistiques possible qui nous avons"


    def __init__(self):
        Menu_stats.__init__(self, self.liste_de_choix())

    def liste_de_choix(self):
        l = ["Nombre de peronnes interrogées",
             "Nombre de peronnes Hommes interrogées",
             "Nombre de peronnes Femmes interrogées",
             "Nombre de person qui pas repondre en certaine question",
             "afficher liste de Data qui on a appartir de google forme",
             "pourcentage moyenne des niveau scolarite",
             "frequence ou pourcentage moyenne d'achat vetements ou bijoux",
             "pourcentage moyenne des personnes avec votre budget mensuel d'achat",
             "pourcentage moyenne des personnes avec votre paiement preferee",
             "nombre moyenne des personnes avec votre occasion preferee d'achat",
             "pour choix multiple : pourcentage moyenne des personnes avel votre localisation preferee d'achate vêtements/bijoux/accessoires  ",
             "pourcentage des personnes que suivent la tendance de mode pour achetez",
             "pour choix d'echelle lineaire :  pourcentage d'importance accorde au service de relloking",
             "pour return a la menu principal",
             ]
        return l

    def traiterMenu_stats(self):
        l = self.liste_de_choix()
        print("\n")
        print("\n")
        print("Interface de gestion statistiques pour traiter chacun question paraporte a la nombre de reponse et pourcentage de reponse a question :\n")
        #pour un autre fichier saisir une autre reference de votre fichier
        sondage = Stats('Formulaire_sans_questions.txt')    # Création d'une instance d'un objet de la classe Stats()
        while True:
            print("\n")
            self.afficher_menu()
            choix = self.choix()
            if choix == 1:
                print("\n---------------------------------------------------------------\n")
                print("\nNombre de peronnes interrogées : ",sondage.nombre_person())
                values = [sondage.nombre_femme(),sondage.nombre_homme()]
                names = ["Femme", "Homme"]
                plt.bar(names, values)
                plt.suptitle('Diagramme Homme et Femme')
                plt.show()
                print("\n---------------------------------------------------------------\n")
            elif choix == 2:
                print("\n---------------------------------------------------------------\n")
                print("Nombre de peronnes Hommes interrogées : ",sondage.nombre_homme())
                print("\n---------------------------------------------------------------\n")
            elif choix == 3:
                print("\n---------------------------------------------------------------\n")
                print("Nombre de peronnes Femmes interrogées : ", sondage.nombre_femme())
                print("\n---------------------------------------------------------------\n")
            elif choix == 4:
                print("\n---------------------------------------------------------------\n")
                print("la sondage de google forme avec chois obligatoire de repondre donc tous les questions avec reponse")
                print("\n---------------------------------------------------------------\n")
            elif choix == 5:
                print("\n---------------------------------------------------------------\n")
                sondage.affichage_liste_Data()
                print("\n---------------------------------------------------------------\n")
            elif choix == 6:
                print("\n---------------------------------------------------------------\n")
                sondage.pourcentage_niveau_scolarite()
                print("\n---------------------------------------------------------------\n")
            elif choix == 7:
                print("\n---------------------------------------------------------------\n")
                sondage.pourcentage_Achate_vetements_bijout()
                print("\n---------------------------------------------------------------\n")
            elif choix == 8:
                print("\n---------------------------------------------------------------\n")
                sondage.pourcentage_moyenne_budget_achat()
                print("\n---------------------------------------------------------------\n")
            elif choix == 9:
                print("\n---------------------------------------------------------------\n")
                sondage.pourcentage_de_paiement_preferee()
                print("\n---------------------------------------------------------------\n")
            elif choix == 10:
                print("\n---------------------------------------------------------------\n")
                sondage.nbr_occasion_achetez()
                print("\n---------------------------------------------------------------\n")
            elif choix == 11:
                print("\n---------------------------------------------------------------\n")
                sondage.pourcentage_achete_principalement_vetements_bijoux_accessoires()
                print("\n---------------------------------------------------------------\n")
            elif choix == 12:
                print("\n---------------------------------------------------------------\n")
                sondage.affichage_pourcentage_qui_suivent_tendences()
                print("\n---------------------------------------------------------------\n")
            elif choix == 13:
                print("\n---------------------------------------------------------------\n")
                sondage.affichage_choix_echelle_lineaire()
                print("\n---------------------------------------------------------------\n")
            elif choix == 14:
                print("\n---------------------------------------------------------------\n")
                print("\n################# sortire en programe de statistique #####################\n")
                print("\n---------------------------------------------------------------\n")
                break
            else:
                print("Erreur : ", '\n'," recommencez svp et veuillez saisir un nombre entre 1 et " + str(len(l)) + " : \n")


if __name__ == '__main__':
    traitementData = Traitement_Stats()
    traitementData.traiterMenu_stats()

    '''sondage = Stats('Data3')
    print("\n  Nombre de peronnes interrogées : ",sondage.nombre_person())
    print(sondage.nombre_homme(),sondage.nombre_femme(), sondage.Nbr_Person_Pas_Repond())
    sondage.affichage_liste_Data()
    sondage.pourcentage_Achate_vetements_bijout()
    sondage.pourcentage_de_paiement_preferee()
    sondage.pourcentage_niveau_scolarite()
    sondage.pourcentage_moyenne_budget_achat()
    sondage.nbr_occasion_achetez()
    sondage.pourcentage_achete_principalement_vetements_bijoux_accessoires()
    sondage.affichage_pourcentage_qui_suivent_tendences()
    sondage.affichage_choix_echelle_lineaire()'''


