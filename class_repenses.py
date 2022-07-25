import os

from os import chdir
dossier = chdir("C:\\Users\\pc\\Desktop\\Formulaire  Python .csv~1\\Formulaire  Python .csv~1")





class repense_question():
    
    
    def __init__(self,sep1="#",sep2="@",sep3=','):       ###########################
      self.nomFichierR="repenses_possible.txt"
      self.nomFicherQuestions="Questions.txt"
      self.sepDeGenre=sep1
      self.sepDeGenreRepenses=sep2
      self.sepDeRepenses=sep3
    

    def lire_les_quesiton(self):
        with open(self.nomFicherQuestions,'r',encoding="utf8", errors='ignore') as F:
            return F.readlines()
        

    def lire_les_repense(self):
        with open(self.nomFichierR,encoding="utf8", errors='ignore') as F:
            return F.readline()
    
    def afficher_les_repenses_possible(self):
        A=self.lire_les_quesiton()
        B=self.lire_les_repense()
        L=A[0].split(self.sepDeGenreRepenses)
        if L[-1]=='\n':
            L.pop(-1)
        J=B.split(self.sepDeGenre)
        i=0
        for element in J:
            i+=1
            K=element.split(self.sepDeGenreRepenses)
            if len(K)>1:
                F=K[1].split(self.sepDeRepenses)
                print(str(i)+'. '+str(L[i-1]+',\n Type :'+str(K[0])))
                print('Repenses possible :')
                for j in range(len(F)):
                    print('-'+str(F[j]))
            else:
                F=K[0].split(self.sepDeRepenses)
                print(str(i)+'. '+str(L[i-1]+',\n Type :'+str(F[0])))
            
        

    def afficher_les_questions(self):
        A=self.lire_les_quesiton()
        L=A[0].split(self.sepDeGenreRepenses)
        if L[-1]=='\n':
            L.pop(-1)
        for i in range(len(L)):
            print(str(i+1)+'. '+str(L[i]))

'''
list_question.nomFicherQuestions='Questions_VBA.txt'
list_question.nomFichierR='repenses_possible.txt'
repense=repense_question()
repense.afficher_les_questions()'''




















