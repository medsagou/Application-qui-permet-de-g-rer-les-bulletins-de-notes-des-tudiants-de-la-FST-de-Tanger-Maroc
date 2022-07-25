Travaille à faire : Pr. Abdellah AZMANI

	Fichier Texte : lignes et des paragraphes
					Dictionnaire
					Bases de données, les champs sont séparés par un séparateur
					Utilisation de la méthode 'Split(séparateur)' pour créer une liste à partir d'une chaîne de caractère
					Utilisation de 'separateur.join()' pour transformer une liste en chaîne dont les mots sont séparés par le séparateur indiqué
	Problème :
		On cherche à créer une application qui permet de gérer les bulletins de notes des étudiants de la FST de Tanger, Maroc
		Pour cela, on enregistre un étudiant dans un fichier en utilisant les informations  :

		Identité :
			CNE#
			CIN#
			Nom#
			Prénom#
			Date_de_Naissance#
			Nationalité#
		Coordonnées :
			Adresse%
			CodePostal%
			Ville%
			Pays%
			Tel%
			eMail

			['4589621','K89999','Azmani','Abdellah','01/01/1900','Marocain','54 Bd de la liberté%90000%Tanger%Maroc%060605050404%a.azmani@uae.ac.ma']

		Les notes sont enregistrées dans un autre fichier organisé ainsi :

			N°CNE#
			Année_Universitaire#
			Code_Filiaire#
			'{
				Code_Module_1 :
					{
						'cc1':note1,
						'cc2':note2,
						'TP':note3,
						'Mini-Projet':note4
					},

				Code_Module_2 :
					{
						'cc1':note1,
						'cc2':note2
					},

			}'

		Il existe un fichier de configuration
			Code_Module_i#
			Désignation_Module#
				'{
					'cc1':Coef.,
					'cc2':Coef.,
					'TP':Coef.,
					'Mini-Projet':Coef.
				}'

			Code_Module_2#Désignation_Module#{'cc1':Coef., 'cc2':Coef.}

		Il est demandé d'écrire les fonctions suivantes :
			1. Enregistrer un étudiant en vérifiant s'il ne l'est pas déjà
			2. Enregistrer la configuration des modules
			3. Enregistrer les notes d'un étudiant par filière
			4. Calculer la moyenne d'un module pour un étudiant

			5. Calculer la moyenne générale d'un étudiant
			6. Calculer la moyenne d'une filière / module'
			7. Calculer l'écart type d'une filière / module'
			8. Calculer la moyenne d'une filière'
			9. Calculer l'écart type d'une filière / module'
			10. Donner le classement des étudiants / module
			11. Donner le classement des étudiants / Filière
			12. Ajouter les mentions
			13. Donner le graphique / les personnes ayant validé, etc.
			...



	Processus de gestion de projet :
		1. Découper le projet en modules
			a. Module gestion de menu
			b. Module gestion de fichiers
			c. Module gestion de dictionnaires
			d. Module gestion de listes
			e. Module gestion des dates
			f. Module gestion du fichier configurations
			g. Module Gestion du fichier "Etudiants"
			h. Module Gestion du fichier notes
			i. Module Gestion traitement des données et gestionn des statistiques
			j. Module Programme principal

		2. Identifier le travail à faire
			a. Développement informatique :
				- identification des besoins,
				- analyse de l'existant,
				- recherche des éléments manquants,
				- préparation des modules
				- commenter les différents programme au fur et à mesure de leur création
			b. Réalisation des tests :
				- préparation d'un jeu de données pour faire des essais,
				- identification des bugs et cas manquants,
				- demande de correction et d'amélioration,
				- Re-commenter le programme pour mettre en évidence les éléments manquants et les cas traités et non traités
			b. Rédaction d'un rapport :
				- Page de garde avec Titre et les auteurs
				- Résumé : 5 lignes
				- Introduction  : 15 à 20 lignes
				- Contexte applicatif : gestion des notes des étudiants de la FSTT
				- Travail réalisé en précisant qui a fait quoi
				- Bilan et conclusion
		3. Organiser le travail par membre du groupe : qui fait quoi ?
		4. Planifier le travail sur une période précise : tâches et modules à faire en parallèle.
		5. Créer un espace de communication du groupe : ex. WhatsApp
		6. Créer un espace de réalisation du projet : ex GitHub ou Colab


Information sur le projet:

	1. Modifier l'espace d'enverment celon votre dossier avant de commencer la simulation.
		import os
		Dossier=chdire(C:\\users...)

	2. Les trois  fichiers  suivant sont la base de donnees de ce programme , sans ces trois fichiers le programme ne marche pas:
		Formulaire.txt 		: est le ficheir initial telecharge de google forms.
		Data3.txt 		: est le meme que Formulaire.txt mais sont les questions (Formulaire.txt sauf la premiers ligne)
		repenses_possible.txt   : est contient les repenses possible de chaque question dans le questionaire.

	3. Apres le programme on obtient au maximum les 3 fichier suiviant:
		.
		.
		.

	4. la structure des menu dans principale
		0. Le formulaire===============================================================================
			0.0. remplir le formulaire.
			0.1. Informaiton sur le formulaire.
			0.2. retour
			0.3. Quitter
		1.Informaiton sur le formulaire==============================================================================
			1.0. Afficher la liste des questions
			1.1. Affihcer les questions et les repenses possible
			1.2. Les informations sur les personnes interrogees----------------------------------------
				1.2.0. Afficher la liste des nom-prenom des personnes interrogees
				1.2.1. Afficher le nombre des femme interrogees
				1.2.2. Afficher le nombre des hommes interrogees
				1.2.3. Chercher un nom
				1.2.4 retour
				1.2.5 Quitter
			1.4. retour
			1.5. Quitter
		2. Statistiques=======================================================================================
				1.3.0. Nombre de peronnes interrogées.
				1.3.1. Nombre de peronnes Hommes interrogées.
				1.3.2. Nombre de peronnes Femmes interrogées.
				1.3.3. Nombre de person qui pas repondre en certaine question.
				1.3.4. Afficher liste de Data qui on a appartir de google forme
				1.3.5. Pourcentage moyenne des niveau scolarite.
				1.3.6. Frequence ou pourcentage moyenne d'achat vetements ou bijoux.
				1.3.7. Pourcentage moyenne des personnes avec votre budget mensuel d'achat.
				1.3.8. pourcentage moyenne des personnes avec votre paiement preferee.
				1.3.9. Nombre moyenne des personnes avec votre occasion preferee d'achat.
				1.3.10. Pour choix multiple : pourcentage moyenne des personnes avel votre localisation preferee d'achate vêtements/bijoux/accessoires
				1.3.11. pourcentage des personnes que suivent la tendance de mode pour achetez.
				1.3.12.	pour choix d'echelle lineaire :  pourcentage d'importance accorde au service de relloking.
				1.3.13. retour.
		3. Quitter============================================================================================




