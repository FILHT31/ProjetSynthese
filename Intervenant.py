####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Classe (mère) Intervenant
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################



class Intervenant:
    """
    Classe Intervenant
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################

    def __init__(self, p_nom_intervenant="", p_annee_exp=0, p_ls_patient=[]):
        """
        Constructeur avec paramètres et valeurs par défaut de la classe parent Intervenant
        :param p_nom_intervenant: Le nom de l'intervenan
        :param p_annee_exp: Le nombre d'années d'expérience de l'intervenant
        :param p_ls_patient : La liste des patients assignés à l'inervenant
        """
        self.__nom_intervenant = p_nom_intervenant
        self.__annee_exp = p_annee_exp
        self.Ls_patient = p_ls_patient

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété Nom_intervenant
    def _get_nom_intervenant(self):
        """
        Accesseur de l'attribut privé __nom_intervenant
        :return: Le nom de l'intervenant
        """
        return self.__nom_intervenant

    def _set_nom_intervenant(self, p_nom_intervenant):
        """
        Mutateur de l'attribut privé __nom_intervenant
        :param p_nom_intervenant: Variable représentant l'attribut privé __nom_intervenant
        """
        if p_nom_intervenant.isaplha() and p_nom_intervenant == " -": # Ajout de l'espace et le tiret pour inscrire des noms complets et composés
            self.__nom_intervenant = p_nom_intervenant

    Nom_intervenant = property(_get_nom_intervenant, _set_nom_intervenant)

    # Propriété Annee_exp
    def _get_annee_exp(self):
        """
        Accesseur de l'attribut privé __annee_exp
        :return: Les années d'expériences d'un intervenant
        """
        return self.__annee_exp

    def _set_annee_exp(self, p_annee_exp):
        """
        Mutateur de l'attribut privé __annee_exp
        :param p_annee_exp: Variable représentant l'attribut privé __annee_exp
        """
        if p_annee_exp.isnumeric() is True and p_annee_exp <= 50: # 50 serait le nombre d'année d'expérience maximum
            self.__annee_exp = p_annee_exp

    Annee_exp = property(_get_annee_exp, _set_annee_exp)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage
        :return: Chaine à afficher (objet instancié)
        """
        chaine = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le nom de l'intervenant : " + self.Nom_intervenant + "\n" + \
                 "   Les années d'expérience de l'intervenant : " + str(self.Annee_exp) + " ans" + "\n" + \
                 "   Les patients assignés à ce Intervenant : " + str(self.Ls_patient) + "\n" + \
                 "   \n" + "*" * 60

        return chaine