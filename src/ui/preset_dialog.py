# -*- coding: utf-8 -*-
"""
Dialogue de gestion des presets.
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QListWidget
)
from PyQt6.QtCore import Qt


class PresetDialog(QDialog):
    """Dialogue pour sauvegarder et charger des presets."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.preset_name = ""
        self.init_ui()
        
    def init_ui(self):
        """Initialise l'interface du dialogue."""
        self.setWindowTitle("Sauvegarder un preset")
        self.setModal(True)
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout()
        
        # Label
        label = QLabel("Nom du preset:")
        layout.addWidget(label)
        
        # Champ de texte
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Mon preset...")
        self.name_input.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.name_input)
        
        # Boutons
        button_layout = QHBoxLayout()
        
        self.save_button = QPushButton("Sauvegarder")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.accept)
        button_layout.addWidget(self.save_button)
        
        cancel_button = QPushButton("Annuler")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
    def on_text_changed(self, text):
        """Active le bouton de sauvegarde si le texte n'est pas vide."""
        self.save_button.setEnabled(len(text.strip()) > 0)
        
    def get_preset_name(self):
        """Retourne le nom du preset."""
        return self.name_input.text().strip()


class PresetLoadDialog(QDialog):
    """Dialogue pour charger un preset."""
    
    def __init__(self, presets, parent=None):
        super().__init__(parent)
        self.presets = presets
        self.selected_preset = None
        self.init_ui()
        
    def init_ui(self):
        """Initialise l'interface du dialogue."""
        self.setWindowTitle("Charger un preset")
        self.setModal(True)
        self.setMinimumSize(400, 300)
        
        layout = QVBoxLayout()
        
        # Label
        label = QLabel("Sélectionnez un preset:")
        layout.addWidget(label)
        
        # Liste des presets
        self.preset_list = QListWidget()
        self.preset_list.addItems(self.presets.keys())
        self.preset_list.itemDoubleClicked.connect(self.on_preset_selected)
        layout.addWidget(self.preset_list)
        
        # Boutons
        button_layout = QHBoxLayout()
        
        load_button = QPushButton("Charger")
        load_button.clicked.connect(self.on_preset_selected)
        button_layout.addWidget(load_button)
        
        delete_button = QPushButton("Supprimer")
        delete_button.clicked.connect(self.delete_preset)
        button_layout.addWidget(delete_button)
        
        cancel_button = QPushButton("Annuler")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
    def on_preset_selected(self):
        """Charge le preset sélectionné."""
        current_item = self.preset_list.currentItem()
        if current_item:
            self.selected_preset = current_item.text()
            self.accept()
            
    def delete_preset(self):
        """Supprime le preset sélectionné."""
        current_item = self.preset_list.currentItem()
        if current_item:
            from PyQt6.QtWidgets import QMessageBox
            reply = QMessageBox.question(
                self,
                "Confirmer la suppression",
                f"Voulez-vous vraiment supprimer le preset '{current_item.text()}' ?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                preset_name = current_item.text()
                del self.presets[preset_name]
                self.preset_list.takeItem(self.preset_list.row(current_item))
                
    def get_selected_preset(self):
        """Retourne le preset sélectionné."""
        return self.selected_preset
