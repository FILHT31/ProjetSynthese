####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Classe (fille) Infirmiere
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
from Intervenant import *


class Infirmiere (Intervenant):
    """
    Classe dérivée Infirmiere de la classe parent Intervenant
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################

    def __init__(self, p_nom_intervenant="", p_annee_exp=0, p_ls_patient=[], p_quart_travail="", p_tache_inf="", p_num_inf=0):
        """
        Constructeur avec paramètres et valeurs par défaut de la classe fille Infirmiere
        :param p_nom_intervenant: Le nom de l'infirmière
        :param p_annee_exp: Le nombre d'année d'expérience de l'infirmière
        :param p_ls_patient : La liste des patients assignés à l'infirmière
        :param p_quart_travail : Le type de quart de travail de l'infirmière
        :param p_tache_inf : La tâche de l'infirmière
        :param p_num_inf : Le numéero de l'infirmière
        """
        Intervenant.__init__(self, p_nom_intervenant, p_annee_exp, p_ls_patient) # Appel du constructeur de la classe Intervenant
        self.Quart_travail = p_quart_travail
        self.__tache_inf = p_tache_inf
        self.__num_inf = p_num_inf

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété Tache_inf
    def _get_tache_inf(self):
        """
        Accesseur de l'attribut privé __tache_inf
        :return: La tâche de l'infirmière
        """
        return self.__tache_inf

    def _set_tache_inf(self, p_tache_inf):
        """
        Mutateur de l'attribut privé __tache_inf
        :param p_tache_inf: Variable représentant l'attribut privé __tache_inf
        """
        if p_tache_inf.isalpha() and p_tache_inf == " '-": # Ajout de l'espace, du tiret et de l'apostrophe pour inscrire des noms complets et composés
            self.__tache_inf = p_tache_inf

    Tache_inf = property(_get_tache_inf, _set_tache_inf)

    # Propriété Num_inf
    def _get_num_inf(self):
        """
        Accesseur de l'attriut privé __num_inf
        :return: Le numéro de l'infirmière
        """
        return self.__num_inf

    def _set_num_inf(self, p_num_inf):
        """
        Mutateur de l'attribut privé __num_inf
        :param p_num_inf: Variable représentant l'attribut privé __num_inf
        """
        if p_num_inf != 0 and p_num_inf.isnumeric() is True and len(p_num_inf) == 2 and p_num_inf > 0:
            self.__num_inf = p_num_inf

    Num_inf = property(_get_num_inf, _set_num_inf)


    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage
        :return: Chaine à afficher (objet instancié)
        """
        return " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le nom de l'infirmière : " + self.Nom_intervenant + "\n" + \
               "   Les années d'expérience de l'infirmière : " + str(self.Annee_exp) + " ans" + "\n" + \
               "   Les patients assignés à l'infirmière : " + str(self.Ls_patient) + "\n" + \
               "   Le type de quart de travail de l'infirmière : " + self.Quart_travail + "\n" + \
               "   La tâche de l'infirmière : " + self.Tache_inf + "\n"+ \
               "   Le numéro de l'infirmière : " + str(self.Num_inf) + "\n" + "*" * 60
