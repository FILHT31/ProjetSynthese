####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse (Clinique)
###  Nom: Félix Hotte-Tranchemontagne
###  No étudiant: 2134152
###  No Groupe: 002
###  Description du fichier: Classe Patient
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
import json
from Intervenant import *


class Patient:
    """
    Classe Patient
    """

    ##################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ##################################

    def __init__(self, p_nom_patient="",p_num_patient=0 , p_age_patient=0, p_raison_rdv="", p_ls_rendez_vous=[], p_intervenant=Intervenant()):
        """
        Constructeur avec paramètres et valeurs par défaut de la classe Patient
        :param p_nom_patient: Le nom du patient
        :param: p_num_patient: Le numéro du patient
        :param p_age_patient: L'âge du patient
        :param p_raison_rdv: La raison du rendez-vous
        :param: p_ls_rendez_vous: Liste des rendez-vous
        :param: p_intervenant : L'intervenant qui s'occupe du rendez-vous
        """
        self.__nom_patient = p_nom_patient
        self.__num_patient = p_num_patient
        self.__age_patient = p_age_patient
        self.Raison_rdv = p_raison_rdv
        self.Ls_rendez_vous = p_ls_rendez_vous
        self.Intervenant = p_intervenant

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété Nom_patient
    def _get_nom_patient(self):
        """
        Accesseur de l'attribut privé __nom_patient
        :return: Le nom du patient
        """
        return self.__nom_patient

    def _set_nom_patient(self, p_nom_patient):
        """
        Mutateur de l'attribut privé __nom_patient
        :param p_nom_patient: Variable représentant l'attribut privé __nom_patient
        """
        if p_nom_patient.isaplha() and p_nom_patient == " -": # Ajout de l'espace et le tiret pour inscrire des noms complets et composés
            self.__nom_patient = p_nom_patient

    Nom_patient = property(_get_nom_patient, _set_nom_patient)

    # Propriété Num_patient
    def _get_num_patient(self):
        """
        Accesseur de l'attribut privé __num_patient
        :return: Le numéro du patient
        """
        return self.__num_patient

    def _set_num_patient(self, p_num_patient):
        """
        Mutateur de l'attribut privé __nom_patient
        :param p_nom_patient: Variable représentant l'attribut privé __num_patient
        """
        if p_num_patient != 0 and p_num_patient.isnumeric() is True and len(p_num_patient) == 4:
            self.__num_patient = p_num_patient


    Num_patient = property(_get_num_patient, _set_num_patient)

    # Propriété Age_patient
    def _get_age_patient(self):
        """
        Accesseur de l'attribut privé __age_patient
        :return: L'âge du patient
        """
        return self.__age_patient

    def _set_age_patient(self, p_age_patient):
        """
        Mutateur de l'attribut privé __age_patient
        :param p_age_patient: Variable représentant l'attribut privé __age_patient
        """
        if p_age_patient != 0 and p_age_patient.isnumeric() is True and p_age_patient <= 105: # 105 serait l'âge maximum d'un patient
            self.__age_patient = p_age_patient

    Age_patient = property(_get_age_patient, _set_age_patient)

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale d'affichage
        :return: Chaine à afficher (objet instancié)
        """
        chaine = " "*60+"\n"+"*"*60+"\n\n"+"   Le nom du patient : " + self.Nom_patient + "\n" + \
                 "   Le numéro du patient : " + str(self.Num_patient) + "\n" + \
                 "   L'âge du patient : " + str(self.Age_patient) + "\n" + \
                 "   La raison du rendez-vous : " + self.Raison_rdv + "\n" + \
                 "   Les rendez-vous du patient : " + str(self.Ls_rendez_vous) + "\n" + \
                 "   L'intervenant qui s'occupe du patient : " + str(self.Intervenant) + "\n" + \
                 "\n"+"*"*60

        return chaine

    def serialiser_patient(self, p_fichier_info_patient):
        """
           Méthode permettant de sérialiser un objet de la classe Patient
           :param p_fichier_info_patient : Le nom du fichier qui contiendra l'objet sérialisé
           :return: retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """
        self.__dict__["Informations du patient"] = self.Nom_patient + "-" + str(self.Num_patient) + "-" + \
                                                 str(self.Age_patient) + "-" + self.Raison_rdv + "-" + \
                                                 str(self.Ls_rendez_vous) + "-" + str(self.Intervenant)

        try:
            with open(p_fichier_info_patient , "w") as fichier:
                try:
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2

    def deserialiser_patient(self, p_fichier_info_patient):
        """
            Méthode permettant de désérialiser un objet de la classe Patient
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
            :return: retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture
        """

        with open(p_fichier_info_patient , "r") as fichier:
            self.__dict__ = json.load(fichier)