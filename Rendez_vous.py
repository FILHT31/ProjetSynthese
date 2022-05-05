####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Classe Rendez_vous
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################


class Rendez_vous:
    """
    Classe Rendez_vous
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################

    def __init__(self, p_num_rdv="", p_annee_rdv=0, p_mois_rdv="", p_jour_rdv=0, p_heure_rdv=""):
        """
        Constructeur avec paramètres et valeurs par défaut de la classe Rendez_vous
        :param p_mois_rdv: Le mois du rendez-vous
        :param p_jour_rdv: Le jour du rendez-vous (1, 2, 3 (et non lundi, mardi, mercredi))
        :param p_heure_rdv: L'heure du rendez-vous
        :param p_intervenant: L'intervenant qui s'occupe du Patient lors du rendez-vous
        """
        self.__num_rdv = p_num_rdv
        self.__annee_rdv = p_annee_rdv
        self.Mois_rdv = p_mois_rdv
        self.__jour_rdv = p_jour_rdv
        self.__heure_rdv = p_heure_rdv

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété Num_rdv
    def _get_num_rdv(self):
        """
        Accesseur de l'attribut privé __num_rdv
        :return: Le numéro de rendez-vous
        """
        return self.__num_rdv

    def _set_num_rdv(self, p_num_rdv):
        """
        Mutateur de l'attribut privé __num_rdv
        :param p_num_rdv: Variable représentant l'attribut privé __num_rdv
        """
        if p_num_rdv[0].isalpha() and len(p_num_rdv) == 4 and p_num_rdv[1:3].isnumeric() is True:
            self.__num_rdv = p_num_rdv

    Num_rdv = property(_get_num_rdv, _set_num_rdv)

    # Propriété Annee_rdv
    def _get_annee_rdv(self):
        """
        Accesseur de l'attribut privé __annee_rdv
        :return: L'année du rendez-vous
        """
        return self.__annee_rdv

    def _set_annee_rdv(self, p_annee_rdv):
        """
        Mutateur de l'attribut privé __annee_rdv
        :param p_annee_rdv: Variable représentant l'attribut privé __annee_rdv
        """
        if p_annee_rdv != 0 and p_annee_rdv.isnumeric is True and p_annee_rdv <= 2022 and p_annee_rdv > 2010:
            self.__annee_rdv = p_annee_rdv

    Annee_rdv = property(_get_annee_rdv, _set_annee_rdv)

    # Propriété Jour_rdv
    def _get_jour_rdv(self):
        """
        Accesseur de l'attribut privé __jour_rdv
        :return: Le jour du rendez-vous
        """
        return self.__jour_rdv

    def _set_jour_rdv(self, p_jour_rdv):
        """
        Mutateur de l'attribut privé __jour_rdv
        :param p_jour_rdv: Variable représentant l'attribut privé __jour_rdv
        """
        if p_jour_rdv != 0 and p_jour_rdv.isnumeric() is True and p_jour_rdv <= 31 and p_jour_rdv > 0:
            self.__jour_rdv = p_jour_rdv

    Jour_rdv = property(_get_jour_rdv, _set_jour_rdv)

    # Propriété Heure_rdv
    def _get_heure_rdv(self):
        """
        Accesseur de l'attribut privé __heure_rdv
        :return: L'heure du rdv
        """
        return self.__heure_rdv

    def _set_heure_rdv(self, p_heure_rdv):
        """
        Mutateur de l'attribut privé __heure_rdv
        :param p_heure_rdv: Variable représentant l'attribut privé __heure_rdv
        """
        if p_heure_rdv != 0 and p_heure_rdv.isnumeric() is True and p_heure_rdv <= 24 and p_heure_rdv > 0:
            self.__heure_rdv = p_heure_rdv

    Heure_rdv = property(_get_heure_rdv, _set_heure_rdv)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage
        :return: Chaine à afficher (objet instancié)
        """
        chaine = " "*60+"\n"+"*"*60+"\n\n"+ "   Le numéro du rendez-vous : " + self.Num_rdv + "\n" + \
                 "   L'année du rendez-vous : " + str(self.Annee_rdv) + "\n" + \
                 "   Le mois du rendez-vous : " + self.Mois_rdv + "\n" + \
                 "   Le jour du rendez-vous : " + str(self.Jour_rdv) + "\n" + \
                 "   L'heure du rendez-vous : " + str(self.Heure_rdv) + " heures" + "\n" + \
                 "   \n"+"*"*60

        return chaine