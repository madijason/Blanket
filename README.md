# Blanket - Windows Edition

![Blanket Logo](assets/icon.png)

**Écoutez différents sons d'ambiance pour améliorer votre concentration et productivité**

Version Windows native de [Blanket](https://github.com/rafaelmardojai/blanket) reconstruite avec PyQt6 pour une compatibilité Windows optimale.

## Fonctionnalités

- 🎵 Lecture simultanée de plusieurs sons d'ambiance
- 🎚️ Contrôle de volume individuel pour chaque son
- 💾 Système de presets personnalisables
- 🎨 Interface moderne avec thème clair/sombre
- 📁 Support des fichiers audio personnalisés (MP3, WAV, OGG)
- 🔊 Mixage audio en temps réel
- 💤 Minuteur d'arrêt automatique
- 🪟 Icône dans la barre des tâches système

## Sons inclus

### Nature
- Pluie
- Orage
- Vagues
- Ruisseau
- Oiseaux
- Vent
- Feu de camp

### Environnements
- Café
- Train
- Ventilateur
- Bruit blanc
- Bruit rose
- Bruit brun

## Installation

### Prérequis

- Python 3.9 ou supérieur
- Windows 10/11

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancement de l'application

```bash
python main.py
```

## Build de l'exécutable Windows

Pour créer un fichier .exe autonome :

```bash
pip install pyinstaller
pyinstaller blanket.spec
```

L'exécutable sera disponible dans le dossier `dist/`.

## Utilisation

1. **Sélectionner des sons** : Cliquez sur les icônes de sons pour les activer
2. **Régler le volume** : Utilisez les sliders pour ajuster le volume de chaque son
3. **Créer un preset** : Sauvegardez votre combinaison favorite de sons
4. **Mode sombre** : Basculez entre thème clair et sombre dans les paramètres
5. **Minuteur** : Définissez une durée d'arrêt automatique

## Structure du projet

```
Blanket/
├── main.py                 # Point d'entrée de l'application
├── src/
│   ├── ui/
│   │   ├── main_window.py  # Fenêtre principale
│   │   ├── sound_card.py   # Carte de son individuelle
│   │   ├── preset_dialog.py # Dialogue de gestion des presets
│   │   └── settings_dialog.py # Dialogue des paramètres
│   ├── audio/
│   │   ├── player.py       # Lecteur audio
│   │   └── mixer.py        # Mixeur audio
│   ├── core/
│   │   ├── settings.py     # Gestion des paramètres
│   │   └── preset.py       # Gestion des presets
│   └── resources/
│       ├── sounds/         # Sons par défaut
│       ├── icons/          # Icônes
│       └── styles/         # Feuilles de style Qt
├── assets/                 # Ressources graphiques
├── requirements.txt        # Dépendances Python
└── blanket.spec           # Configuration PyInstaller
```

## Développement

### Architecture

L'application utilise l'architecture MVC (Model-View-Controller) :

- **Model** : Gestion des données (presets, paramètres)
- **View** : Interface PyQt6
- **Controller** : Logique métier et gestion audio

### Technologies

- **PyQt6** : Framework d'interface graphique
- **pygame.mixer** : Backend audio multi-canal
- **QSettings** : Persistance des paramètres

## Crédits

Version Windows développée par Jason Madi

Basé sur [Blanket](https://github.com/rafaelmardojai/blanket) par Rafael Mardojai CM

### Licences des sons

Pour les informations détaillées sur les licences des sons, consultez [SOUNDS_LICENSING.md](SOUNDS_LICENSING.md)

## Licence

GNU General Public License v3.0 - Voir [LICENSE](LICENSE) pour plus de détails

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## Support

Si vous rencontrez des problèmes ou avez des questions, ouvrez une [issue](https://github.com/madijason/Blanket/issues).
