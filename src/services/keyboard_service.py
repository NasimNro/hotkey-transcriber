"""
Keyboard Service - Handles global hotkey detection
Listens for Ctrl+Shift combination to trigger recording
"""

import threading
from pynput import keyboard
from typing import Callable, Optional
import logging

class KeyboardService:
    def __init__(self, on_hotkey_press: Callable, on_hotkey_release: Callable):
        self.on_hotkey_press = on_hotkey_press
        self.on_hotkey_release = on_hotkey_release
        self.listener: Optional[keyboard.Listener] = None
        self.is_recording = False
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.logger = logging.getLogger(__name__)
        
    def start_listening(self):
        """Start listening for global keyboard events"""
        try:
            self.listener = keyboard.Listener(
                on_press=self._on_key_press,
                on_release=self._on_key_release
            )
            self.listener.start()
            self.logger.info("Keyboard listener started - Waiting for Ctrl+Shift...")
            print("🎤 Whisper Transcriber gestartet!")
            print("📝 Drücken Sie Ctrl+Shift zum Aufnehmen")
            
        except Exception as e:
            self.logger.error(f"Failed to start keyboard listener: {e}")
            raise
    
    def stop_listening(self):
        """Stop listening for keyboard events"""
        if self.listener:
            self.listener.stop()
            self.logger.info("Keyboard listener stopped")
    
    def _on_key_press(self, key):
        """Handle key press events"""
        try:
            # Check for Ctrl key
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.ctrl_pressed = True
                
            # Check for Shift key
            elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                self.shift_pressed = True
            
            # If both Ctrl and Shift are pressed and we're not already recording
            if self.ctrl_pressed and self.shift_pressed and not self.is_recording:
                self.is_recording = True
                self.logger.info("Hotkey activated - Starting recording")
                print("🔴 Aufnahme gestartet...")
                threading.Thread(target=self.on_hotkey_press, daemon=True).start()
                
        except Exception as e:
            self.logger.error(f"Error in key press handler: {e}")
    
    def _on_key_release(self, key):
        """Handle key release events"""
        try:
            # Check for Ctrl key release
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.ctrl_pressed = False
                
            # Check for Shift key release  
            elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                self.shift_pressed = False
            
            # If either key is released and we're recording, stop recording
            if self.is_recording and (not self.ctrl_pressed or not self.shift_pressed):
                self.is_recording = False
                self.logger.info("Hotkey released - Stopping recording")
                print("⏹️ Aufnahme beendet - Transkribiere...")
                threading.Thread(target=self.on_hotkey_release, daemon=True).start()
                
        except Exception as e:
            self.logger.error(f"Error in key release handler: {e}") 