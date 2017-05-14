# -*- coding: utf-8 -*-


from os import listdir
from os.path import isfile, join
class Frame():
    
   def __init__(self):
       self.choix=0
       mypath = ''
       while(True):
            choix = input("Voulez vous générer une politique choix : 1\nVoulez vous utilisé une politique déja Existante choix : 2\n")
            choix = int(choix)
            if(type(choix) == 'int'):
                print("mauvaise valeur saisie recommencer")
            elif(choix == 1):
                self.choix=1
                tmp=True
                while(tmp):
                    mypath='../BD/'
                    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
                    print("Veuillez choisir le(s) type(s) de pertinence que vous désirez, pour choisir la 3 et la 4 entrez : 3 4\n")
                    for i in range(len(onlyfiles)):
                        print("choix : ",i+1," ",onlyfiles[i])
                    choix = input('\n')
                    choix = choix.split()
                    tmp=False
                       
                    for i in range(len(choix)):
                        if int(choix[i]) < 0 or int(choix[i]) > len(onlyfiles):
                            print("merci de rentrer des valeurs cohérentes")
                            tmp=True
                            break
                break
            elif(choix == 2):
                self.choix=1
                tmp=True
                while(tmp):
                    mypath='../Policies/'
                    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
                    print("Veuillez choisir la politique que vous désirez, pour choisir la 1 entrez : 1\n")
                    for i in range(len(onlyfiles)):
                        print("choix : ",i+1," ",onlyfiles[i])
                    choix = input('\n')
                    choix = choix.split()
                    if(len(choix)>2):
                        print("merci de ne rentrer que une valeur")
                    else:
                        tmp=False
                       
                        for i in range(len(choix)):
                            if int(choix[i]) < 0 or int(choix[i]) > len(onlyfiles):
                                print("merci de rentrer des valeurs cohérentes")
                                tmp=True
                                break
                        
                    
                                
                break
            else:
                print("mauvaise valeur saisie recommencer")
            
            
       if(self.choix==1):
            self.listRel=[]
            for i in range(len(choix)):
                self.listRel.append("BD/%s" % onlyfiles[int(choix[i])-1])
       elif(self.choix==2):
            pass
       else:
            print("aucun choix valables merci de recommencer")
            
            
       
        