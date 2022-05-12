#################################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Code pour la programmation de l'interface graphique de l'intervenant
#################################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import DialogueIntervenant

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def cacher_labels_et_lineEdits_intervenant(objet):
    """
    Procédure qui rend invisible les labels et les lineEdits désirés (Pour le choix de médecin ou infirmière)
    :param objet: Le label ou lineEdit à rendre invisible
    """
    # Nom de l'intervenant
    objet.label_nom_intervenant.setVisible(False)
    objet.lineEdit_nom_intervenant.setVisible(False)
    objet.label_nom_intervenant_erreur.setVisible(False)

    # Années d'expériences
    objet.label_annee_exp.setVisible(False)
    objet.lineEdit_annee_exp.setVisible(False)
    objet.label_annee_exp_erreur.setVisible(False)

    # Numéro de l'infirmière
    objet.label_num_inf.setVisible(False)
    objet.lineEdit_num_inf.setVisible(False)
    objet.label_num_infirmiere_erreur.setVisible(False)

    # Type de quart de travail
    objet.label_quart_travail.setVisible(False)
    objet.comboBox_quart_travail.setVisible(False)

    # Tache de l'infirmière
    objet.label_tache_inf.setVisible(False)
    objet.lineEdit_tache_inf.setVisible(False)
    objet.label_tache_inf_erreur.setVisible(False)

    # Bouton ajouter intervenant
    objet.pushButton_ajouter_intervenant.setVisible(False)

    # Bouton supprimer intervenant
    objet.pushButton_supprimer_intervenant.setVisible(False)

    # Bouton modifier intervenant
    objet.pushButton_modifier_intervenant.setVisible(False)

    # Numéro du médecin
    objet.label_num_med.setVisible(False)
    objet.lineEdit_num_med.setVisible(False)
    objet.label_num_med_erreur.setVisible(False)

    # Spécialité du médecin
    objet.label_specialite_med.setVisible(False)
    objet.comboBox_specialite_med.setVisible(False)

    # TextBrowser et erreur
    objet.textBrowser_intervenant.setVisible(False)
    objet.label_intervenant_existe_erreur.setVisible(False)



#################################################################
###### DÉFINITIONS DE LA CLASSE FenetreDialogueIntervenant ######
#################################################################

class FenetreDialogueIntervenant(QtWidgets.QDialog, DialogueIntervenant.Ui_DialogIntervenant):
    """
    Classe de la Fenêtre DialogueIntervenant
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe FenetreDialogueIntervenant
        :param parent: QtWidgets.QDialog et DialogIntervenant.Ui_DialogIntervenant
        """
        # Appel du constructeur parent
        super(FenetreDialogueIntervenant, self).__init__(parent)
        # Préparation de l'interface pour l'utilisateur
        self.setupUi(self)
        # Nommination de la fenêtre DialogueIntervenant
        self.setWindowTitle("Intervenant")
        # Lancement de la procédure rendant les labels et les lineEdits invisibles
        cacher_labels_et_lineEdits_intervenant(self)


    @pyqtSlot()
    #  Bouton Ajouter intervenant
    def on_pushButton_ajouter_intervenant_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter Intervenant
        """
        cacher_labels_et_lineEdits_intervenant(self) #À CHANGER

    @pyqtSlot()
    # Bouton Supprimer interv.
    def on_pushButton_supprimer_intervenant_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer interv.
        """
        cacher_labels_et_lineEdits_intervenant(self) #À CHANGER

    @pyqtSlot()
    # Bouton Modifier intervenant
    def on_pushButton_modifier_intervenant_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier intervenant
        """
        cacher_labels_et_lineEdits_intervenant(self)  #À CHANGER

    @pyqtSlot()
    # Bouton Quitter (Intervenant)
    def on_pushButton_quitter_intervenant_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Quitter (Intervenant)
        """
        self.close()