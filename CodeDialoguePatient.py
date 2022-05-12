#########################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Code pour la programmation de l'interface graphique du patient
###########################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import DialoguePatient
import DialogueLsPatient
from CodeDialogueLsPatient import *


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def cacher_labels_patient(objet):
    """
    Procédure qui rend invisible les labels désirés (labels d'erreur majoritairement)
    :param objet: Un des labels à mettre invisible
    """

    objet.label_nom_patient_erreur.setVisible(False)
    objet.label_num_patient_erreur.setVisible(False)
    objet.label_age_patient_erreur.setVisible(False)
    objet.label_patient_existe_erreur.setVisible(False)

#############################################################
###### DÉFINITIONS DE LA CLASSE FenetreDialoguePatient ######
#############################################################

class FenetreDialoguePatient(QtWidgets.QDialog, DialoguePatient.Ui_DialogPatient):
    """
    Classe de la Fenêtre DialoguePatient
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreDialoguePatient
        :param parent: QtWidgets.QDialog et DialogPatient.Ui_DialogPatient
        """
        # Appel du constructeur parent
        super(FenetreDialoguePatient, self).__init__(parent)
        # Préparation de l'interface pour l'utilisateur
        self.setupUi(self)
        # Nommination de la fenêtre DialoguePatient
        self.setWindowTitle("Patient")
        # Lancement de la procédure rendant les labels invisibles
        cacher_labels_patient(self)


    @pyqtSlot()
    # Bouton Ajouter patient
    def on_pushButton_ajouter_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter patient
        """
        # Appel de la procédure qui rend les labels désirés invisibles (erreurs)
        cacher_labels_patient(self)

         #À CHANGER

    @pyqtSlot()
    # Bouton Serialiser patient
    def on_pushButton_serialiser_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Serialiser patient
        """
        # Appel de la procédure qui rend les labels désirés invisibles (erreurs)
        cacher_labels_patient(self)

        #À CHANGER

    @pyqtSlot()
    # Bouton Déserialiser patient
    def on_pushButton_deserialiser_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Déserialiser patient
        """
        # Appel de la procédure qui rend les labels désirés invisibles (erreurs)
        cacher_labels_patient(self)

        #À CHANGER

    @pyqtSlot()
    # Bouton Voir liste patient
    def on_pushButton_voir_liste_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Voir liste patient
        """
        # Instanciation d'un dialogue de la Fenêtre DialogueLsPatient
        dialogLsPatient = FenetreDialogueLsPatient()
        dialogLsPatient.show()
        reply = dialogLsPatient.exec_()

    @pyqtSlot()
    # Bouton Modifier patient
    def on_pushButton_modifier_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier patient
        """
        # Appel de la procédure qui rend les labels désirés invisibles (erreurs)
        cacher_labels_patient(self)

        #À CHANGER

    @pyqtSlot()
    # Bouton Supprimer patient
    def on_pushButton_supprimer_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer patient
        """
        # Appel de la procédure qui rend les labels désirés invisibles (erreurs)
        cacher_labels_patient(self)

        #À CHANGER

    @pyqtSlot()
    # Bouton Quitter (Patient)
    def on_pushButton_quitter_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Quitter (Patient)
        """
        self.close()

