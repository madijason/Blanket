# -*- coding: utf-8 -*-
"""
Fenêtre principale de l'application Blanket.
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QScrollArea, QLabel, QPushButton, QSlider, QGridLayout,
    QSystemTrayIcon, QMenu
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QAction, QIcon

from src.audio.mixer import AudioMixer
from src.ui.sound_card import SoundCard
from src.ui.preset_dialog import PresetDialog
from src.ui.settings_dialog import SettingsDialog
from src.core.settings import Settings
from src.core.sounds import SOUNDS_DATA


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application."""
    
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.audio_mixer = AudioMixer()
        self.sound_cards = {}
        
        self.init_ui()
        self.setup_tray_icon()
        self.load_saved_state()
        
    def init_ui(self):
        """Initialise l'interface utilisateur."""
        self.setWindowTitle("Blanket")
        self.setMinimumSize(900, 600)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Barre supérieure
        self.create_top_bar(main_layout)
        
        # Contrôle du volume principal
        self.create_master_volume(main_layout)
        
        # Grille de sons
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        sounds_widget = QWidget()
        self.sounds_layout = QGridLayout(sounds_widget)
        self.sounds_layout.setSpacing(15)
        
        # Créer les cartes de sons
        self.create_sound_cards()
        
        scroll_area.setWidget(sounds_widget)
        main_layout.addWidget(scroll_area)
        
        # Barre d'état
        self.statusBar().showMessage("Prêt")
        
        # Menu bar
        self.create_menu_bar()
        
    def create_menu_bar(self):
        """Crée la barre de menu."""
        menubar = self.menuBar()
        
        # Menu Fichier
        file_menu = menubar.addMenu("&Fichier")
        
        open_action = QAction("&Ouvrir un fichier audio...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_audio_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        quit_action = QAction("&Quitter", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)
        
        # Menu Presets
        preset_menu = menubar.addMenu("&Presets")
        
        save_preset = QAction("&Sauvegarder preset...", self)
        save_preset.triggered.connect(self.show_preset_dialog)
        preset_menu.addAction(save_preset)
        
        load_preset = QAction("&Charger preset...", self)
        load_preset.triggered.connect(self.load_preset)
        preset_menu.addAction(load_preset)
        
        # Menu Paramètres
        settings_menu = menubar.addMenu("&Paramètres")
        
        settings_action = QAction("&Préférences...", self)
        settings_action.setShortcut("Ctrl+,")
        settings_action.triggered.connect(self.show_settings)
        settings_menu.addAction(settings_action)
        
        # Menu Aide
        help_menu = menubar.addMenu("&Aide")
        
        about_action = QAction("&À propos", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def create_top_bar(self, parent_layout):
        """Crée la barre supérieure avec les contrôles."""
        top_bar = QHBoxLayout()
        
        # Titre
        title = QLabel("<h1>Blanket</h1>")
        top_bar.addWidget(title)
        
        top_bar.addStretch()
        
        # Bouton lecture/pause
        self.play_button = QPushButton("⏸ Pause")
        self.play_button.setCheckable(True)
        self.play_button.setChecked(True)
        self.play_button.clicked.connect(self.toggle_playback)
        self.play_button.setMinimumWidth(120)
        top_bar.addWidget(self.play_button)
        
        # Bouton reset volumes
        reset_button = QPushButton("🔄 Réinitialiser")
        reset_button.clicked.connect(self.reset_volumes)
        top_bar.addWidget(reset_button)
        
        parent_layout.addLayout(top_bar)
        
    def create_master_volume(self, parent_layout):
        """Crée le contrôle de volume principal."""
        volume_layout = QHBoxLayout()
        
        label = QLabel("Volume principal:")
        volume_layout.addWidget(label)
        
        self.master_slider = QSlider(Qt.Orientation.Horizontal)
        self.master_slider.setMinimum(0)
        self.master_slider.setMaximum(100)
        self.master_slider.setValue(100)
        self.master_slider.valueChanged.connect(self.on_master_volume_changed)
        volume_layout.addWidget(self.master_slider)
        
        self.volume_label = QLabel("100%")
        self.volume_label.setMinimumWidth(50)
        volume_layout.addWidget(self.volume_label)
        
        parent_layout.addLayout(volume_layout)
        
    def create_sound_cards(self):
        """Crée les cartes de sons."""
        row = 0
        col = 0
        max_cols = 3
        
        for sound_id, sound_data in SOUNDS_DATA.items():
            card = SoundCard(sound_id, sound_data, self.audio_mixer)
            self.sound_cards[sound_id] = card
            
            self.sounds_layout.addWidget(card, row, col)
            
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
                
    def setup_tray_icon(self):
        """Configure l'icône de la barre des tâches."""
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.windowIcon())
        
        # Menu contextuel
        tray_menu = QMenu()
        
        show_action = QAction("Afficher", self)
        show_action.triggered.connect(self.show)
        tray_menu.addAction(show_action)
        
        tray_menu.addSeparator()
        
        play_action = QAction("Lecture/Pause", self)
        play_action.triggered.connect(self.toggle_playback)
        tray_menu.addAction(play_action)
        
        tray_menu.addSeparator()
        
        quit_action = QAction("Quitter", self)
        quit_action.triggered.connect(self.close)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_activated)
        self.tray_icon.show()
        
    def tray_icon_activated(self, reason):
        """Gère le clic sur l'icône de la barre des tâches."""
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()
                self.activateWindow()
                
    def toggle_playback(self):
        """Bascule entre lecture et pause."""
        if self.play_button.isChecked():
            self.audio_mixer.resume_all()
            self.play_button.setText("⏸ Pause")
        else:
            self.audio_mixer.pause_all()
            self.play_button.setText("▶ Lecture")
            
    def reset_volumes(self):
        """Réinitialise tous les volumes."""
        for card in self.sound_cards.values():
            card.reset_volume()
            
    def on_master_volume_changed(self, value):
        """Gère le changement du volume principal."""
        self.volume_label.setText(f"{value}%")
        self.audio_mixer.set_master_volume(value / 100.0)
        
    def open_audio_file(self):
        """Ouvre un fichier audio personnalisé."""
        from PyQt6.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Ouvrir un fichier audio",
            "",
            "Fichiers audio (*.mp3 *.wav *.ogg);;Tous les fichiers (*.*)"
        )
        if file_path:
            # TODO: Ajouter le fichier personnalisé
            self.statusBar().showMessage(f"Fichier chargé: {file_path}", 3000)
            
    def show_preset_dialog(self):
        """Affiche le dialogue de sauvegarde de preset."""
        dialog = PresetDialog(self)
        if dialog.exec():
            preset_name = dialog.get_preset_name()
            self.save_preset(preset_name)
            
    def save_preset(self, name):
        """Sauvegarde le preset actuel."""
        preset_data = {}
        for sound_id, card in self.sound_cards.items():
            if card.is_playing():
                preset_data[sound_id] = card.get_volume()
        
        self.settings.save_preset(name, preset_data)
        self.statusBar().showMessage(f"Preset '{name}' sauvegardé", 3000)
        
    def load_preset(self):
        """Charge un preset."""
        # TODO: Implémenter le dialogue de sélection de preset
        pass
        
    def show_settings(self):
        """Affiche le dialogue des paramètres."""
        dialog = SettingsDialog(self, self.settings)
        if dialog.exec():
            # Recharger les paramètres
            self.apply_settings()
            
    def apply_settings(self):
        """Applique les nouveaux paramètres."""
        # TODO: Implémenter l'application des paramètres
        pass
        
    def show_about(self):
        """Affiche la boîte de dialogue À propos."""
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.about(
            self,
            "À propos de Blanket",
            "<h2>Blanket - Windows Edition</h2>"
            "<p>Version 1.0.0</p>"
            "<p>Application de sons d'ambiance pour améliorer la concentration.</p>"
            "<p>Développé par Jason Madi</p>"
            "<p>Basé sur Blanket par Rafael Mardojai CM</p>"
            "<p><a href='https://github.com/madijason/Blanket'>GitHub</a></p>"
        )
        
    def load_saved_state(self):
        """Charge l'état sauvegardé."""
        # Charger le volume principal
        volume = self.settings.master_volume
        self.master_slider.setValue(int(volume * 100))
        
        # Charger l'état des sons
        sound_states = self.settings.sound_states
        for sound_id, state in sound_states.items():
            if sound_id in self.sound_cards:
                card = self.sound_cards[sound_id]
                if state.get('playing', False):
                    card.set_volume(state.get('volume', 0.5))
                    card.toggle_sound()
                    
    def save_state(self):
        """Sauvegarde l'état actuel."""
        # Sauvegarder le volume principal
        self.settings.master_volume = self.master_slider.value() / 100.0
        
        # Sauvegarder l'état des sons
        sound_states = {}
        for sound_id, card in self.sound_cards.items():
            sound_states[sound_id] = {
                'playing': card.is_playing(),
                'volume': card.get_volume()
            }
        self.settings.sound_states = sound_states
        self.settings.save()
        
    def closeEvent(self, event):
        """Gère la fermeture de la fenêtre."""
        if self.settings.minimize_to_tray:
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Blanket",
                "L'application continue de fonctionner en arrière-plan",
                QSystemTrayIcon.MessageIcon.Information,
                2000
            )
        else:
            self.save_state()
            self.audio_mixer.cleanup()
            event.accept()
