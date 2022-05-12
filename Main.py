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

# Importation des classes
from Patient import *
from Intervenant import *
from Medecin import *
from Infirmiere import *
from Rendez_vous import *

# Importation des interfaces graphiques
import InterfacegraphiqueMain
from DialoguePatient import *
from DialogueRdv import *
from DialogueIntervenant import *
from DialogueLsPatient import *
from DialogueLsRdv import *

# Importation des codes des interfaces graphiques
from CodeDialoguePatient import *
from CodeDialogueRdv import *
from CodeDialogueIntervenant import *

# Importation utilse au model des interfaces
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# Importation du module nécessaire à l'éxécution
import sys

# Importation pour le gestionnaire d'évènement
from PyQt5.QtCore import pyqtSlot

# Importation de la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets



##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################
ls_rendez_vous = []
ls_patient = []


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_patient_existe(p_Num_patient):
    """
    Fonction qui vérifie si le patient existe déjà dans la liste des patients
    :param Num_patient: Le numéro du patient
    :return: True si le patient est déjà dans la liste et False s'il y n'y était pas
    """

    for elt in ls_patient:
        if elt.Num_patient == p_Num_patient.capitalize():
            return True
    return False


#############################################################
######       DÉFINITIONS DE LA CLASSE FenetreMain      ######
#############################################################

class FenetreMain(QtWidgets.QMainWindow, InterfacegraphiqueMain.Ui_CliniqueMain):
    """
    Classe de la Fenêtre principale
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreMain
        :param parent: QtWidgets.QMainWindow et InterfacegraphiqueMain.Ui_CliniqueMain
        """
        super(FenetreMain, self).__init__(parent)
        self.setupUi(self)
        # Nommination de la fenêtre principale
        self.setWindowTitle("Clinique")


    @pyqtSlot()
    # Bouton Patient
    def on_pushButton_main_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Patient
        """
        #Instanciation d'un dialogue de la Fenêtre DialoguePatient
        dialog = FenetreDialoguePatient()
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    # Bouton Rendez-vous
    def on_pushButton_main_rdv_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Rendez-vous
        """
        # Instanciation d'un dialogue de la Fenêtre DialogueRdv
        dialog2 = FenetreDialogueRdv()
        dialog2.show()
        reply = dialog2.exec_()

    @pyqtSlot()
    # Bouton Intervenant
    def on_pushButton_main_intervenant_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Intervenant
        """
        # Instanciation d'un dialogue de la Fenêtre DialogueIntervenant
        dialog3 = FenetreDialogueIntervenant()
        dialog3.show()
        reply = dialog3.exec_()

    @pyqtSlot()
    # Bouton Quitter
    def on_pushButton_quitter_main_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Quitter
        """
        self.close()






#################################
###### PROGRAMME PRINCIPAL ######
#################################

def main():
    """
    Méthode main : permet l'exécution de l'application avec l'interface graphique
    reply= Dialog.exec_()
    """
    # Instanciation d'une application et de la fenêtre principale
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreMain()
    # Affichage de la fenêtre
    form.show()
    # Lancement de l'application
    app.exec()

if __name__ == "__main__":
    main()

# Test no1
# Instanciation d'un patient

#Patient1 = Patient("Félix Hotte-Tranchemontagne", 1234, 18, "Bras cassé", ls_rendez_vous, "Jasmin Thériault")
#print(Patient1)

# Test no2
# Instanciation d'un Intervenant

#Intervenant1 = Intervenant("Jasmin Thériault", 4, ls_patient)
#print(Intervenant1)

# Test no3
# Instanction d'un Médecin

#Medecin1 = Medecin("Gabriel Denis", 9, ls_patient, "Neurologue", 37)
#print(Medecin1)

# Test no4
# Instanciation d'une Infirmière

#Infirmiere1 = Infirmiere("Guylaine Gagnon", 2, ls_patient, "Jour", "Passer le balais", 44)
#print(Infirmiere1)

# Test no5
# Instanctiation d'un Rendez-vous

#Rendez_vous1 = Rendez_vous("A123", 2019, "Juin", 25, 8)
#print(Rendez_vous1)

