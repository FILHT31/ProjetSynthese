#########################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Code pour la programmation de l'interface graphique de la liste des patients
##########################################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import DialogueLsPatient


##################################################################
######   DÉFINITIONS DE LA CLASSE FenetreDialogueLsPatient  ######
##################################################################

class FenetreDialogueLsPatient(QtWidgets.QDialog, DialogueLsPatient.Ui_DialogLsPatient):
    """
    Classe de la Fenêtre DialogueLsRdv
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreDialogueLsPatient
        :param parent: QtWidgets.QDialog et DialogLsPatient.Ui_DialogLsPatient
        """
        # Appel du constructeur parent
        super(FenetreDialogueLsPatient, self).__init__(parent)
        # Préparation de l'interface pour l'utilisateur
        self.setupUi(self)
        # Nommination de la fenêtre DialogueRdv
        self.setWindowTitle("Liste des patients")

    @pyqtSlot()
    # Bouton Quitter (Rendez-vous)
    def on_pushButton_quitter_liste_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Quitter (Liste Patient)
        """
        self.close()