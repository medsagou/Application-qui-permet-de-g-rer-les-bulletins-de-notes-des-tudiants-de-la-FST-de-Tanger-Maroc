
class Menu():
    
    
    def __init__(self,L=[]):
        self.list=L
        
    def afficher_menu(self):
        for i in range(len(self.list)):
            print(i," : ",self.list[i])        

    def choix(self):
      while True:             
        try:
          i=int(input("\nSelon votre choix taper un nombre entre 0 et "+str(len(self.list)-1)+" -->  "))
          assert i >= 0 and i <= (len(self.list)-1)
        except ValueError:
          print("\n!!!Veuillez saisir un nombre entier!!!")
        except AssertionError:
          print("\n!!! Le nombre saisi doit être dans la liste!!!")        
        else:
          return i 
          break  



'''menu=Menu()
menu.list=L
menu.afficher_menu()
C= menu.choix()'''






















