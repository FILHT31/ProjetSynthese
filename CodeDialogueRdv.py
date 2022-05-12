###########################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Code pour la programmation de l'interface graphique du rdv
###########################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import DialogueRdv
import DialogueLsRdv
from CodeDialogueLsRdv import *

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def cacher_labels_rdv(objet):
    """
    Procédure qui rend invisible les labels désirés (labels d'erreur majoritairement)
    :param objet: Un des labels à mettre invisible
    """

    objet.label_num_rdv_erreur.setVisible(False)
    objet.label_num_annee_rdv.setVisible(False)
    objet.label_jour_rdv_erreur.setVisible(False)
    objet.label_heure_rdv.setVisible(False)
    objet.label_rdv_existe_erreur.setVisible(False)

#############################################################
######   DÉFINITIONS DE LA CLASSE FenetreDialogueRdv   ######
#############################################################

class FenetreDialogueRdv(QtWidgets.QDialog, DialogueRdv.Ui_DialogRdv):
    """
    Classe de la Fenêtre DialogueRdv
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreDialogueRdv
        :param parent: QtWidgets.QDialog et DialogRdv.Ui_DialogRdv
        """
        # Appel du constructeur parent
        super(FenetreDialogueRdv, self).__init__(parent)
        # Préparation de l'interface pour l'utilisateur
        self.setupUi(self)
        # Nommination de la fenêtre DialogueRdv
        self.setWindowTitle("Rendez-vous")
        # Lancement de la procédure rendant les labels invisibles
        cacher_labels_rdv(self)


    @pyqtSlot()
    # Bouton Créer rdv
    def on_pushButton_creer_rdv_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Créer rdv
        """
        cacher_labels_rdv(self) #À CHANGER

    @pyqtSlot()
    # Bouton Voir liste rdv
    def on_pushButton_voir_liste_rdv_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Voir liste rdv
        """
        # Instanciation d'un dialogue de la Fenêtre DialogueLsPatient
        dialogLsRdv = FenetreDialogueLsRdv()
        dialogLsRdv.show()
        reply = dialogLsRdv.exec_()

    @pyqtSlot()
    # Bouton Quitter (Rendez-vous)
    def on_pushButton_quitter_rdv_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Quitter (Rendez-vous)
        """
        self.close()