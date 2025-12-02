# -*- coding: utf-8 -*-
"""
Feuilles de style pour l'application.
"""

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


def apply_dark_theme(app):
    """Applique le thème sombre à l'application."""
    palette = QPalette()
    
    # Couleurs de base
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    
    # Couleurs désactivées
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
    
    app.setPalette(palette)
    
    # Styles CSS additionnels
    stylesheet = """
    QToolTip {
        color: #ffffff;
        background-color: #2a82da;
        border: 1px solid white;
    }
    
    QPushButton {
        padding: 6px;
        border-radius: 4px;
        background-color: #3d3d3d;
    }
    
    QPushButton:hover {
        background-color: #4d4d4d;
    }
    
    QPushButton:pressed {
        background-color: #2d2d2d;
    }
    
    QPushButton:checked {
        background-color: #2a82da;
    }
    
    QSlider::groove:horizontal {
        border: 1px solid #999999;
        height: 8px;
        background: #3d3d3d;
        margin: 2px 0;
        border-radius: 4px;
    }
    
    QSlider::handle:horizontal {
        background: #2a82da;
        border: 1px solid #5c5c5c;
        width: 18px;
        margin: -5px 0;
        border-radius: 9px;
    }
    
    QSlider::handle:horizontal:hover {
        background: #3a92ea;
    }
    
    QGroupBox {
        border: 2px solid #5c5c5c;
        border-radius: 5px;
        margin-top: 1ex;
        font-weight: bold;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        padding: 0 5px;
    }
    """
    
    app.setStyleSheet(stylesheet)


def apply_light_theme(app):
    """Applique le thème clair à l'application."""
    # Réinitialiser la palette par défaut
    app.setPalette(app.style().standardPalette())
    
    # Styles CSS pour le thème clair
    stylesheet = """
    QPushButton {
        padding: 6px;
        border-radius: 4px;
        background-color: #f0f0f0;
        border: 1px solid #c0c0c0;
    }
    
    QPushButton:hover {
        background-color: #e0e0e0;
    }
    
    QPushButton:pressed {
        background-color: #d0d0d0;
    }
    
    QPushButton:checked {
        background-color: #2196f3;
        color: white;
    }
    
    QSlider::groove:horizontal {
        border: 1px solid #bbb;
        height: 8px;
        background: #f0f0f0;
        margin: 2px 0;
        border-radius: 4px;
    }
    
    QSlider::handle:horizontal {
        background: #2196f3;
        border: 1px solid #1976d2;
        width: 18px;
        margin: -5px 0;
        border-radius: 9px;
    }
    
    QSlider::handle:horizontal:hover {
        background: #42a5f5;
    }
    
    QGroupBox {
        border: 2px solid #c0c0c0;
        border-radius: 5px;
        margin-top: 1ex;
        font-weight: bold;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        padding: 0 5px;
    }
    """
    
    app.setStyleSheet(stylesheet)
