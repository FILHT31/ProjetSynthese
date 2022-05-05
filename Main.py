####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from Patient import *
from Intervenant import *
from Medecin import *
from Infirmiere import *
from Rendez_vous import *

##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
ls_rendez_vous = []
ls_patient = []


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################




#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Test no1
# Instanciation d'un patient

Patient1 = Patient("Félix Hotte-Tranchemontagne", 1234, 18, "Bras cassé", ls_rendez_vous, "Jasmin Thériault")
print(Patient1)

# Test no2
# Instanciation d'un Intervenant

Intervenant1 = Intervenant("Jasmin Thériault", 4, ls_patient)
print(Intervenant1)

# Test no3
# Instanction d'un Médecin

Medecin1 = Medecin("Gabriel Denis", 9, ls_patient, "Neurologue", 37)
print(Medecin1)

# Test no4
# Instanciation d'une Infirmière

Infirmiere1 = Infirmiere("Guylaine Gagnon", 2, ls_patient, "Jour", "Passer le balais", 44)
print(Infirmiere1)

# Test no5
# Instanctiation d'un Rendez-vous

Rendez_vous1 = Rendez_vous("A123", 2019, "Juin", 25, 8)
print(Rendez_vous1)

