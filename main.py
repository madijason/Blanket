#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blanket - Windows Edition
Application de sons d'ambiance pour améliorer la concentration

Auteur: Jason Madi
Basé sur Blanket par Rafael Mardojai CM
Licence: GPL-3.0
"""

import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QLocale
from PyQt6.QtGui import QIcon

from src.ui.main_window import MainWindow
from src.core.settings import Settings

# Version de l'application
VERSION = "1.0.0"


def main():
    """Point d'entrée principal de l'application."""
    # Configuration de l'application
    QApplication.setApplicationName("Blanket")
    QApplication.setApplicationVersion(VERSION)
    QApplication.setOrganizationName("Jason Madi")
    QApplication.setOrganizationDomain("github.com/madijason")
    
    # Active le support des hautes résolutions
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    # Créer l'application Qt
    app = QApplication(sys.argv)
    
    # Définir l'icône de l'application
    icon_path = Path(__file__).parent / "assets" / "icon.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    
    # Charger les paramètres
    settings = Settings()
    
    # Appliquer le thème
    if settings.dark_mode:
        app.setStyle("Fusion")
        from src.ui.styles import apply_dark_theme
        apply_dark_theme(app)
    
    # Créer et afficher la fenêtre principale
    window = MainWindow()
    window.show()
    
    # Lancer la boucle d'événements
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
