# -*- coding: utf-8 -*-
"""
Définition des sons disponibles dans l'application.
"""

from pathlib import Path

# Répertoire des ressources
RESOURCES_DIR = Path(__file__).parent.parent / "resources"
SOUNDS_DIR = RESOURCES_DIR / "sounds"

# Données des sons par catégorie
SOUNDS_DATA = {
    # Nature
    'rain': {
        'name': 'Pluie',
        'icon': '🌧️',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'rain.ogg'),
        'description': 'Son apaisant de la pluie'
    },
    'storm': {
        'name': 'Orage',
        'icon': '⛈️',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'storm.ogg'),
        'description': 'Orage avec tonnerre'
    },
    'waves': {
        'name': 'Vagues',
        'icon': '🌊',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'waves.ogg'),
        'description': 'Vagues de l\'océan'
    },
    'stream': {
        'name': 'Ruisseau',
        'icon': '🏞️',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'stream.ogg'),
        'description': 'Ruisseau qui coule'
    },
    'birds': {
        'name': 'Oiseaux',
        'icon': '🐦',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'birds.ogg'),
        'description': 'Chants d\'oiseaux'
    },
    'wind': {
        'name': 'Vent',
        'icon': '🍃',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'wind.ogg'),
        'description': 'Vent dans les arbres'
    },
    'fire': {
        'name': 'Feu',
        'icon': '🔥',
        'category': 'nature',
        'file': str(SOUNDS_DIR / 'fire.ogg'),
        'description': 'Feu de camp crépitant'
    },
    
    # Environnements
    'coffee_shop': {
        'name': 'Café',
        'icon': '☕',
        'category': 'environment',
        'file': str(SOUNDS_DIR / 'coffee_shop.ogg'),
        'description': 'Ambiance de café'
    },
    'train': {
        'name': 'Train',
        'icon': '🚂',
        'category': 'environment',
        'file': str(SOUNDS_DIR / 'train.ogg'),
        'description': 'Train en mouvement'
    },
    'fan': {
        'name': 'Ventilateur',
        'icon': '🌬️',
        'category': 'environment',
        'file': str(SOUNDS_DIR / 'fan.ogg'),
        'description': 'Bruit de ventilateur'
    },
    
    # Bruits blancs
    'white_noise': {
        'name': 'Bruit blanc',
        'icon': '📡',
        'category': 'noise',
        'file': str(SOUNDS_DIR / 'white_noise.ogg'),
        'description': 'Bruit blanc pur'
    },
    'pink_noise': {
        'name': 'Bruit rose',
        'icon': '🎵',
        'category': 'noise',
        'file': str(SOUNDS_DIR / 'pink_noise.ogg'),
        'description': 'Bruit rose'
    },
    'brown_noise': {
        'name': 'Bruit brun',
        'icon': '🔉',
        'category': 'noise',
        'file': str(SOUNDS_DIR / 'brown_noise.ogg'),
        'description': 'Bruit brun'
    },
}

# Catégories
CATEGORIES = {
    'nature': 'Nature',
    'environment': 'Environnements',
    'noise': 'Bruits blancs'
}
