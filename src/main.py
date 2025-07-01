"""
Main Application - Whisper Transcriber
Orchestrates all services to provide voice-to-text functionality with Ctrl+Shift hotkey
"""

import sys
import signal
import logging
import time
from typing import Optional

from config.settings import Settings
from services.keyboard_service import KeyboardService
from services.audio_service import AudioService
from services.transcription_service import TranscriptionService
from services.text_injection_service import TextInjectionService

class WhisperTranscribers:
    def __init__(self):
        # Initialize settings and logging
        self.settings = Settings()
        self.settings.setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # Initialize services
        self.audio_service = AudioService(self.settings)
        self.transcription_service = TranscriptionService(self.settings.openai_api_key)
        self.text_injection_service = TextInjectionService()
        self.keyboard_service = KeyboardService(
            on_hotkey_press=self._on_recording_start,
            on_hotkey_release=self._on_recording_stop
        )
        
        # State management
        self.is_running = True
        self.current_audio_file: Optional[str] = None
        
        self.logger.info("Whisper Transcriber initialized")
    
    def start(self):
        """Start the transcriber application"""
        try:
            print("=" * 60)
            print("🎤 WHISPER TRANSCRIBER")
            print("=" * 60)
            print("✅ Anwendung gestartet!")
            print("🔥 Bereit für Sprachaufnahme")
            print("📋 Tastenkombination: Ctrl + Windows")
            print("🛑 Zum Beenden: Ctrl + C")
            print("=" * 60)
            
            # Start keyboard listener
            self.keyboard_service.start_listening()
            
            # Keep the application running
            self._run_main_loop()
            
        except KeyboardInterrupt:
            print("\n🛑 Anwendung wird beendet...")
            self.stop()
        except Exception as e:
            self.logger.error(f"Application error: {e}")
            print(f"❌ Fehler: {e}")
            self.stop()
    
    def stop(self):
        """Stop the transcriber application"""
        self.is_running = False
        
        # Stop services
        if self.keyboard_service:
            self.keyboard_service.stop_listening()
        
        if self.audio_service:
            self.audio_service.cleanup_temp_file()
        
        self.logger.info("Whisper Transcriber stopped")
        print("👋 Auf Wiedersehen!")
    
    def _run_main_loop(self):
        """Main application loop"""
        try:
            while self.is_running:
                time.sleep(0.1)  # Small delay to prevent high CPU usage
        except KeyboardInterrupt:
            pass
    
    def _on_recording_start(self):
        """Callback when recording starts (Ctrl+Shift pressed)"""
        try:
            self.logger.info("Recording started")
            self.audio_service.start_recording()
        except Exception as e:
            self.logger.error(f"Failed to start recording: {e}")
            print(f"❌ Aufnahme-Fehler: {e}")
    
    def _on_recording_stop(self):
        """Callback when recording stops (Ctrl+Shift released)"""
        try:
            self.logger.info("Recording stopped")
            
            # Stop recording and get audio file
            audio_file_path = self.audio_service.stop_recording()
            
            if not audio_file_path:
                print("⚠️ Keine Audiodaten aufgenommen")
                return
            
            self.current_audio_file = audio_file_path
            
            # Transcribe audio
            print("🔄 Sende Audio an Whisper API...")
            transcribed_text = self.transcription_service.transcribe_audio(
                audio_file_path, 
            )
            
            if transcribed_text:
                # Inject text into active field
                success = self.text_injection_service.inject_text(transcribed_text)
                
                if success:
                    print(f"📝 Transkription: \"{transcribed_text}\"")
                else:
                    print(f"⚠️ Text konnte nicht eingefügt werden: \"{transcribed_text}\"")
            else:
                print("❌ Transkription fehlgeschlagen")
            
            # Cleanup temporary file
            self.audio_service.cleanup_temp_file()
            self.current_audio_file = None
            
            print("✅ Bereit für nächste Aufnahme...")
            
        except Exception as e:
            self.logger.error(f"Failed to process recording: {e}")
            print(f"❌ Verarbeitungs-Fehler: {e}")
            
            # Cleanup on error
            if self.current_audio_file:
                self.audio_service.cleanup_temp_file()
                self.current_audio_file = None

                


class WhisperTranscriber:
    def __init__(self):
        self.settings = Settings()
        self.settings.setup_logging()
        # self.logger = logging.getLogger(__name__)

        # self.audio_service = AudioService()
        # self.transcription_service = TranscriptionService(self.settings.openai_api_key)
        # self.text_injection_service = TextInjectionService()

    def start(self):
        """Start the transcriber application"""
        print("=" * 60)
        print("🎤 WHISPER TRANSCRIBER")
        print("=" * 60)
        print("✅ Anwendung gestartet!")
        print("🔥 Bereit für Sprachaufnahme")


def main():
    """Main entry point"""
    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        print("\n🛑 Beende Anwendung...")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    

    # Create and start the transcriber
    transcriber = WhisperTranscribers()
    transcriber.start()
        

if __name__ == "__main__":
    main() 