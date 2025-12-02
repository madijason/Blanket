# -*- coding: utf-8 -*-
"""
Mixeur audio pour la gestion simultanée de plusieurs sons.
"""

import pygame
from pathlib import Path
from typing import Dict, Optional


class AudioMixer:
    """Gère le mixage audio de plusieurs sons simultanément."""
    
    def __init__(self, frequency=44100, size=-16, channels=2, buffer=512):
        """
        Initialise le mixeur audio.
        
        Args:
            frequency: Fréquence d'échantillonnage (Hz)
            size: Taille des échantillons
            channels: Nombre de canaux (1=mono, 2=stereo)
            buffer: Taille du buffer
        """
        pygame.mixer.init(frequency, size, channels, buffer)
        pygame.mixer.set_num_channels(32)  # Permet jusqu'à 32 sons simultanés
        
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.channels: Dict[str, pygame.mixer.Channel] = {}
        self.master_volume = 1.0
        self.paused = False
        
    def play_sound(self, sound_id: str, file_path: str, volume: float = 0.5) -> bool:
        """
        Joue un son en boucle.
        
        Args:
            sound_id: Identifiant unique du son
            file_path: Chemin vers le fichier audio
            volume: Volume initial (0.0 - 1.0)
            
        Returns:
            True si le son a été lancé avec succès
        """
        try:
            # Charger le son s'il n'est pas déjà chargé
            if sound_id not in self.sounds:
                sound_path = Path(file_path)
                if not sound_path.exists():
                    print(f"Erreur: Fichier audio introuvable: {file_path}")
                    return False
                    
                self.sounds[sound_id] = pygame.mixer.Sound(str(sound_path))
            
            # Obtenir un canal disponible
            channel = pygame.mixer.find_channel()
            if channel is None:
                print("Erreur: Aucun canal audio disponible")
                return False
            
            # Définir le volume
            self.sounds[sound_id].set_volume(volume * self.master_volume)
            
            # Jouer le son en boucle
            channel.play(self.sounds[sound_id], loops=-1)
            self.channels[sound_id] = channel
            
            return True
            
        except Exception as e:
            print(f"Erreur lors de la lecture du son {sound_id}: {e}")
            return False
    
    def stop_sound(self, sound_id: str):
        """Arrête un son spécifique."""
        if sound_id in self.channels:
            self.channels[sound_id].stop()
            del self.channels[sound_id]
    
    def set_volume(self, sound_id: str, volume: float):
        """
        Définit le volume d'un son spécifique.
        
        Args:
            sound_id: Identifiant du son
            volume: Nouveau volume (0.0 - 1.0)
        """
        if sound_id in self.sounds:
            self.sounds[sound_id].set_volume(volume * self.master_volume)
    
    def set_master_volume(self, volume: float):
        """
        Définit le volume principal.
        
        Args:
            volume: Nouveau volume principal (0.0 - 1.0)
        """
        self.master_volume = max(0.0, min(1.0, volume))
        
        # Mettre à jour le volume de tous les sons actifs
        for sound_id, sound in self.sounds.items():
            if sound_id in self.channels:
                current_volume = sound.get_volume()
                sound.set_volume(current_volume / self.master_volume * self.master_volume)
    
    def pause_all(self):
        """Met en pause tous les sons."""
        pygame.mixer.pause()
        self.paused = True
    
    def resume_all(self):
        """Reprend tous les sons en pause."""
        pygame.mixer.unpause()
        self.paused = False
    
    def stop_all(self):
        """Arrête tous les sons."""
        pygame.mixer.stop()
        self.channels.clear()
    
    def is_playing(self, sound_id: str) -> bool:
        """
        Vérifie si un son est en cours de lecture.
        
        Args:
            sound_id: Identifiant du son
            
        Returns:
            True si le son est en lecture
        """
        return sound_id in self.channels and self.channels[sound_id].get_busy()
    
    def fade_out(self, sound_id: str, duration_ms: int = 1000):
        """
        Effectue un fondu de sortie sur un son.
        
        Args:
            sound_id: Identifiant du son
            duration_ms: Durée du fondu en millisecondes
        """
        if sound_id in self.channels:
            self.channels[sound_id].fadeout(duration_ms)
    
    def fade_out_all(self, duration_ms: int = 1000):
        """Effectue un fondu de sortie sur tous les sons."""
        for channel in self.channels.values():
            channel.fadeout(duration_ms)
    
    def cleanup(self):
        """Nettoie les ressources audio."""
        self.stop_all()
        self.sounds.clear()
        pygame.mixer.quit()
