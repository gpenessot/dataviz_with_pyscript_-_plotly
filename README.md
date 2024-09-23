# Projet de DataViz avec PyScript et Plotly

Bienvenue dans ce projet de visualisation de données (DataViz) qui utilise **PyScript** et **Plotly** pour créer des graphiques interactifs. Ce projet illustre le changement de température mondiale et les émissions de CO2 au fil des siècles.

## Table des Matières

- [Aperçu](#aperçu)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure des fichiers](#structure-des-fichiers)
- [Données](#données)
- [Contributions](#contributions)
- [Licence](#licence)
- [Contact](#contact)

## Aperçu

Ce projet génère des graphiques interactifs à l'aide de données sur la température mondiale et les émissions de CO2. Les visualisations permettent d'analyser les tendances au fil des années.

### Exemples de visualisations

- **Graphique 1** : Évolution de la température mondiale
- **Graphique 2** : Émissions annuelles de CO2

## Installation

Pour exécuter ce projet, vous devez avoir Python et les bibliothèques nécessaires installées. Voici comment procéder :

1. Clonez ce repository :

   ```bash
   git clone https://github.com/votre_nom_utilisateur/dataviz-pyscript-plotly.git
   cd dataviz-pyscript-plotly
   ```

2. Assurez-vous d'avoir un environnement Python actif. Vous pouvez utiliser venv ou conda.

3. Installez les dépendances nécessaires. Vous pouvez créer un fichier requirements.txt si vous le souhaitez, mais le fichier pyconfig.toml peut suffire pour gérer les configurations.

## Utilisation

Pour une exécution locale, exécutez la commande suivante depuis le répertoire :

```bash
python -m http.server
```
Ouvrez ouvrez un navigateur à l'adresse `http://localhost:8000/` pour voir le dashboard.
Les graphiques se mettront à jour automatiquement en fonction des données fournies.

## Structure des fichiers

```bash
.
├── index.html          # Page principale avec le code HTML et PyScript
├── pyconfig.toml      # Configuration des dépendances pour PyScript
├── main.py             # Code Python pour générer les visualisations
├── globaltemp.csv      # Données sur la température mondiale
└── hadcrutworld.csv    # Données sur les émissions de CO2
```

## Données

Les données utilisées dans ce projet proviennent de sources fiables. Les fichiers CSV contiennent les informations nécessaires pour générer les graphiques.

- `globaltemp.csv` : Données sur la température mondiale de 1880 à 2023.
- `hadcrutworld.csv` : Données sur les émissions de CO2.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos modifications (`git commit -m 'Ajout d\'une nouvelle fonctionnalité'`).
4. Poussez vers la branche (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Contact

Pour toute question ou suggestion, n'hésitez pas à me contacter :

LinkedIn : [Gaël Penessot](https://www.linkedin.com/in/gael-penessot/)  
Email : gael.penessot@data-decision.io  
GitHub : [gpenessot](https://github.com/gpenessot)  

Merci d'avoir consulté ce projet ! 🎉
