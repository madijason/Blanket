# -*- coding: utf-8 -*-
"""
Carte de son individuelle avec contrôles.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QSlider, QPushButton, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class SoundCard(QFrame):
    """Widget représentant un son individuel."""
    
    def __init__(self, sound_id, sound_data, audio_mixer):
        super().__init__()
        self.sound_id = sound_id
        self.sound_data = sound_data
        self.audio_mixer = audio_mixer
        self.playing = False
        
        self.init_ui()
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        
    def init_ui(self):
        """Initialise l'interface de la carte."""
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Icône/Emoji
        icon_label = QLabel(self.sound_data['icon'])
        icon_font = QFont()
        icon_font.setPointSize(48)
        icon_label.setFont(icon_font)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)
        
        # Nom
        name_label = QLabel(self.sound_data['name'])
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_font = QFont()
        name_font.setPointSize(12)
        name_font.setBold(True)
        name_label.setFont(name_font)
        layout.addWidget(name_label)
        
        # Slider de volume
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.setEnabled(False)
        self.volume_slider.valueChanged.connect(self.on_volume_changed)
        layout.addWidget(self.volume_slider)
        
        # Label de volume
        self.volume_label = QLabel("50%")
        self.volume_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.volume_label)
        
        # Bouton lecture
        self.play_button = QPushButton("▶ Lecture")
        self.play_button.setCheckable(True)
        self.play_button.clicked.connect(self.toggle_sound)
        layout.addWidget(self.play_button)
        
        self.setLayout(layout)
        self.setMinimumWidth(200)
        self.setMaximumWidth(280)
        
    def toggle_sound(self):
        """Active/désactive le son."""
        if self.playing:
            self.stop_sound()
        else:
            self.start_sound()
            
    def start_sound(self):
        """Démarre la lecture du son."""
        success = self.audio_mixer.play_sound(
            self.sound_id,
            self.sound_data['file'],
            self.volume_slider.value() / 100.0
        )
        
        if success:
            self.playing = True
            self.play_button.setText("⏸ Pause")
            self.play_button.setChecked(True)
            self.volume_slider.setEnabled(True)
            self.setStyleSheet("QFrame { background-color: #e3f2fd; border: 2px solid #2196f3; }")
        
    def stop_sound(self):
        """Arrête la lecture du son."""
        self.audio_mixer.stop_sound(self.sound_id)
        self.playing = False
        self.play_button.setText("▶ Lecture")
        self.play_button.setChecked(False)
        self.volume_slider.setEnabled(False)
        self.setStyleSheet("")
        
    def on_volume_changed(self, value):
        """Gère le changement de volume."""
        self.volume_label.setText(f"{value}%")
        if self.playing:
            self.audio_mixer.set_volume(self.sound_id, value / 100.0)
            
    def reset_volume(self):
        """Réinitialise le volume à 50%."""
        self.volume_slider.setValue(50)
        
    def is_playing(self):
        """Retourne si le son est en lecture."""
        return self.playing
        
    def get_volume(self):
        """Retourne le volume actuel (0-1)."""
        return self.volume_slider.value() / 100.0
        
    def set_volume(self, volume):
        """Définit le volume (0-1)."""
        self.volume_slider.setValue(int(volume * 100))
