import random, time
from fiches_anglais import fiche6,fiche10
def fiche ( dictionnaire): #return list; z = {**x,**y}
    fichelis =[]
    for anglais, francais in dictionnaire.items():
        fichelis.append( (anglais,francais))
    return fichelis #(anglais,francais)

def creerfiche (): #return dic
    fiche = dict()
    espace  = "260418"
    valider = "280418"
    while espace !='ok' :  
        anglais = input("Votre mot en anglais:")
        francais= input("La traduction en français de '" + anglais +"' est:")
        print( "MG>>>Confirmez-vous:(_" +anglais + ":" + francais+ "_)")
        while valider !='ok':
            reponse = input("MG>>>validé(entrée) corriger: anglais(a),français(f),les deux(d) fini(espace):")
            if reponse == '':
                fiche[anglais]=francais
                valider = 'ok'
            if reponse == 'a':
                while reponse != '' :
                    anglais = input("Changer" + anglais + " en: ")
                    print("vous validez "+ anglais+":")
                    reponse = input(" Oui(Entrée)  Non(touche):")
                    if reponse == '':
                        fiche[anglais]=francais
                        valider ='ok'
            if reponse == 'f':
                while reponse != '' :
                    francais = input("Changer" + francais + " en: ")
                    print("vous validez "+ francais +":")
                    reponse = input(" Oui(Entrée)  Non(touche):")
                    if reponse == '':
                        fiche[anglais]=francais
                        valider ='ok'
            if reponse == 'd':
                valider ='ok'
            if reponse ==' ':
                fiche[anglais]=francais
                valider ='ok'
                espace  ='ok'
        valider = "Michel.Guo"
    return fiche 
    
def bleu( mot):
    return "\033[34m"+mot+"\033[37m"

def rouge( mot):
    return "\033[31m"+mot+"\033[37m"

def vert( mot):
    return "\033[32m"+mot+"\033[37m"
    
def testcomplet( vocliste):
    resultattc = []
    for i in vocliste:
        #while passer != "ok":
            anglais = i[0]
            francais = i[1]
            reponse = input( anglais + ":")
            note += correction(anglais, reponse)
            if correction(anglais,reponse) ==0:
                resultattc.append((anglais, reponse ))
    return resultattc
    print( reponse + "/" + len(vocliste))

def correction(mot1, mot2):
    if mot1 == mot2:
        return 1
    else:
        return 0

def revision(vocliste):
    liste0805 = vocliste.copy()
    while len(liste0805) !=0:
        for i in liste0805:
            a = input(i[1])
            print(liste0805.index(i) ,"/" ,len(liste0805) ,i[0])
            time.sleep(0.5)
            if a =="":
                liste0805.remove(i)
        
#def faute( mot1, mot2): #mot.replace('lettre1','lettre2')

def execution():
    print(" bienvenue !\n")
    time.sleep(0.5)
    print ("vous voulez :\n1.réviser\n2.faire le test\n3.sortir")
    
    
  
        
if __name__ == '__main__':
    print("Mode d'emploi: 1) je te conseil de d'abord consulter fiches_anglais.py \n"
         +"2) après tu ne presses que sur Entrer et regarde ce que ça donne")
    print("normalement il faut saisir le mot en anglais correspondant...")
    revision(fiche(fiche6)+fiche(fiche10))
         
    
    
    
    