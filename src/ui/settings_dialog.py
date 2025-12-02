# -*- coding: utf-8 -*-
"""
Dialogue des paramètres de l'application.
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QCheckBox, QSpinBox, QPushButton, QGroupBox,
    QComboBox, QFormLayout
)
from PyQt6.QtCore import Qt


class SettingsDialog(QDialog):
    """Dialogue de configuration de l'application."""
    
    def __init__(self, parent=None, settings=None):
        super().__init__(parent)
        self.settings = settings
        self.init_ui()
        self.load_settings()
        
    def init_ui(self):
        """Initialise l'interface du dialogue."""
        self.setWindowTitle("Paramètres")
        self.setModal(True)
        self.setMinimumWidth(500)
        
        layout = QVBoxLayout()
        
        # Groupe Interface
        ui_group = QGroupBox("Interface")
        ui_layout = QFormLayout()
        
        self.dark_mode_check = QCheckBox("Mode sombre")
        ui_layout.addRow("Thème:", self.dark_mode_check)
        
        self.minimize_tray_check = QCheckBox("Réduire dans la barre des tâches")
        ui_layout.addRow("Fermeture:", self.minimize_tray_check)
        
        ui_group.setLayout(ui_layout)
        layout.addWidget(ui_group)
        
        # Groupe Audio
        audio_group = QGroupBox("Audio")
        audio_layout = QFormLayout()
        
        self.auto_pause_check = QCheckBox("Pause automatique lors de la mise en veille")
        audio_layout.addRow("Comportement:", self.auto_pause_check)
        
        self.fade_check = QCheckBox("Fondu enchainé")
        audio_layout.addRow("Transition:", self.fade_check)
        
        self.fade_duration = QSpinBox()
        self.fade_duration.setRange(100, 5000)
        self.fade_duration.setSingleStep(100)
        self.fade_duration.setSuffix(" ms")
        audio_layout.addRow("Durée du fondu:", self.fade_duration)
        
        audio_group.setLayout(audio_layout)
        layout.addWidget(audio_group)
        
        # Groupe Minuteur
        timer_group = QGroupBox("Minuteur")
        timer_layout = QFormLayout()
        
        self.timer_enabled_check = QCheckBox("Activer le minuteur d'arrêt")
        timer_layout.addRow("Minuteur:", self.timer_enabled_check)
        
        self.timer_duration = QSpinBox()
        self.timer_duration.setRange(1, 120)
        self.timer_duration.setSuffix(" minutes")
        timer_layout.addRow("Durée:", self.timer_duration)
        
        timer_group.setLayout(timer_layout)
        layout.addWidget(timer_group)
        
        layout.addStretch()
        
        # Boutons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Enregistrer")
        save_button.clicked.connect(self.save_and_close)
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton("Annuler")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
    def load_settings(self):
        """Charge les paramètres actuels."""
        if self.settings:
            self.dark_mode_check.setChecked(self.settings.dark_mode)
            self.minimize_tray_check.setChecked(self.settings.minimize_to_tray)
            self.auto_pause_check.setChecked(self.settings.auto_pause)
            self.fade_check.setChecked(self.settings.fade_enabled)
            self.fade_duration.setValue(self.settings.fade_duration)
            self.timer_enabled_check.setChecked(self.settings.timer_enabled)
            self.timer_duration.setValue(self.settings.timer_duration)
            
    def save_and_close(self):
        """Sauvegarde les paramètres et ferme le dialogue."""
        if self.settings:
            self.settings.dark_mode = self.dark_mode_check.isChecked()
            self.settings.minimize_to_tray = self.minimize_tray_check.isChecked()
            self.settings.auto_pause = self.auto_pause_check.isChecked()
            self.settings.fade_enabled = self.fade_check.isChecked()
            self.settings.fade_duration = self.fade_duration.value()
            self.settings.timer_enabled = self.timer_enabled_check.isChecked()
            self.settings.timer_duration = self.timer_duration.value()
            self.settings.save()
        
        self.accept()
