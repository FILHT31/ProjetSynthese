####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Classe (fille) Medecin
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from Intervenant import *
import json


class Medecin (Intervenant):
    """
    Classe dérivée Medecin de la classe parent Intervenant
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################

    def __init__(self, p_nom_intervenant="", p_annee_exp=0, p_ls_patient=[], p_specialite="", p_num_med=0):
        """
        Constructeur avec paramètres et valeurs par défaut de la classe fille Medecin
        :param p_nom_intervenant: Le nom du médecin
        :param p_annee_exp: Les années d'expérience du médecin
        :param p_ls_patient: La liste des patients assigés au médecin
        :param p_specialite: La spécialité du médecin
        :param p_num_med: Le numéro du médecin
        """

        Intervenant.__init__(self, p_nom_intervenant, p_annee_exp, p_ls_patient) # Appel du constructeur de la classe Intervenant
        self.Specialite = p_specialite
        self.__num_med = p_num_med

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété Num_med
    def _get_num_med(self):
        """
        Accesseur de l'attriut privé __num_med
        :return: Le numéro du médecin
        """
        return self.__num_med

    def _set_num_med(self, p_num_med):
        """
        Mutateur de l'attribut privé __num_inf
        :param p_num_inf: Variable représentant l'attribut privé __num_inf
        """
        if p_num_med != 0 and p_num_med.isnumeric() is True and len(p_num_med) == 2 and p_num_med > 0:
            self.__num_med = p_num_med

    Num_med = property(_get_num_med, _set_num_med)


    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def serialiser_med(self, p_fichier_info_medecin):
        """
           Méthode permettant de sérialiser un objet de la classe (fille) Medecin
           :param p_fichier_info_patient : Le nom du fichier qui contiendra l'objet sérialisé
           :return: retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """
        self.__dict__["Informations du médecin"] = self.Nom_intervenant + "-" + str(self.Annee_exp) + "-" + \
                                                   self.Ls_patient + "-" + self.Specialite + "-" + \
                                                   self.Num_med

        try:
            with open(p_fichier_info_medecin , "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2

    def deserialiser_med(self, p_fichier_info_patient):
        """
            Méthode permettant de désérialiser un objet de la classe (fille) Medecin
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
            :return: retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture
        """

        with open(p_fichier_info_patient , "r") as fichier:
            self.__dict__ = json.load(fichier)

    def __str__(self):
        """
        Méthode spéciale d'affichage
        :return: Chaine à afficher (objet instancié)
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le nom du médecin : " + self.Nom_intervenant + "\n" + \
               "   Les années d'expérience du médecin : " + str(self.Annee_exp) + " ans" + "\n" + \
               "   Les patients assignés au médecin : " + str(self.Ls_patient) + "\n" + \
               "   La spécialité du médecin : " + self.Specialite + "\n"+ \
               "   Le numéro du médecin : " + str(self.Num_med) + "\n" + "*" * 60
