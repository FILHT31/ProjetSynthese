###################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Code pour la programmation de l'interface graphique de la liste des rdv
####################################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import DialogueLsRdv


###############################################################
######   DÉFINITIONS DE LA CLASSE FenetreDialogueLsRdv   ######
###############################################################

class FenetreDialogueLsRdv(QtWidgets.QDialog, DialogueLsRdv.Ui_DialogLsRdv):
    """
    Classe de la Fenêtre DialogueLsRdv
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreDialogueLsRdv
        :param parent: QtWidgets.QDialog et DialogLsRdv.Ui_DialogLsRdv
        """
        # Appel du constructeur parent
        super(FenetreDialogueLsRdv, self).__init__(parent)
        # Préparation de l'interface pour l'utilisateur
        self.setupUi(self)
        # Nommination de la fenêtre DialogueRdv
        self.setWindowTitle("Liste des rendez-vous")

    @pyqtSlot()
    # Bouton Quitter (Rendez-vous)
    def on_pushButton_quitter_liste_rdv_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Quitter (Liste Rendez-vous)
        """
        self.close()