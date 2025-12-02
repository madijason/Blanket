# -*- coding: utf-8 -*-
"""
Gestion des paramètres de l'application.
"""

from PyQt6.QtCore import QSettings
import json


class Settings:
    """Gestionnaire des paramètres de l'application."""
    
    def __init__(self):
        self.qsettings = QSettings()
        self.load()
    
    def load(self):
        """Charge les paramètres sauvegardés."""
        # Interface
        self.dark_mode = self.qsettings.value('ui/dark_mode', False, type=bool)
        self.minimize_to_tray = self.qsettings.value('ui/minimize_to_tray', True, type=bool)
        
        # Audio
        self.master_volume = self.qsettings.value('audio/master_volume', 1.0, type=float)
        self.auto_pause = self.qsettings.value('audio/auto_pause', False, type=bool)
        self.fade_enabled = self.qsettings.value('audio/fade_enabled', True, type=bool)
        self.fade_duration = self.qsettings.value('audio/fade_duration', 1000, type=int)
        
        # Minuteur
        self.timer_enabled = self.qsettings.value('timer/enabled', False, type=bool)
        self.timer_duration = self.qsettings.value('timer/duration', 30, type=int)
        
        # État des sons
        sound_states_json = self.qsettings.value('sounds/states', '{}')
        try:
            self.sound_states = json.loads(sound_states_json)
        except:
            self.sound_states = {}
        
        # Presets
        presets_json = self.qsettings.value('presets/saved', '{}')
        try:
            self.presets = json.loads(presets_json)
        except:
            self.presets = {}
    
    def save(self):
        """Sauvegarde les paramètres."""
        # Interface
        self.qsettings.setValue('ui/dark_mode', self.dark_mode)
        self.qsettings.setValue('ui/minimize_to_tray', self.minimize_to_tray)
        
        # Audio
        self.qsettings.setValue('audio/master_volume', self.master_volume)
        self.qsettings.setValue('audio/auto_pause', self.auto_pause)
        self.qsettings.setValue('audio/fade_enabled', self.fade_enabled)
        self.qsettings.setValue('audio/fade_duration', self.fade_duration)
        
        # Minuteur
        self.qsettings.setValue('timer/enabled', self.timer_enabled)
        self.qsettings.setValue('timer/duration', self.timer_duration)
        
        # État des sons
        self.qsettings.setValue('sounds/states', json.dumps(self.sound_states))
        
        # Presets
        self.qsettings.setValue('presets/saved', json.dumps(self.presets))
        
        self.qsettings.sync()
    
    def save_preset(self, name: str, sound_states: dict):
        """Sauvegarde un preset."""
        self.presets[name] = sound_states
        self.save()
    
    def load_preset(self, name: str) -> dict:
        """Charge un preset."""
        return self.presets.get(name, {})
    
    def delete_preset(self, name: str):
        """Supprime un preset."""
        if name in self.presets:
            del self.presets[name]
            self.save()
    
    def get_preset_names(self) -> list:
        """Retourne la liste des noms de presets."""
        return list(self.presets.keys())
