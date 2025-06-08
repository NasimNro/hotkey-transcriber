"""
Audio Service - Handles microphone recording
Records audio while hotkey is pressed and saves to temporary file
"""

import sounddevice as sd
import soundfile as sf
import threading
import tempfile
import os
import logging
import numpy as np
from typing import Optional

class AudioService:
    def __init__(self):
        self.recording_data = []
        self.is_recording = False
        self.temp_file_path: Optional[str] = None
        self.logger = logging.getLogger(__name__)
        
        # Audio settings
        self.channels = 1
        self.rate = 16000  # 16kHz is optimal for Whisper
        self.dtype = np.float32
        
    def start_recording(self):
        """Start recording audio from microphone"""
        try:
            if self.is_recording:
                return
                
            self.is_recording = True
            self.recording_data = []
            
            self.logger.info("Audio recording started")
            
            # Start recording in separate thread
            self.recording_thread = threading.Thread(target=self._record_audio, daemon=True)
            self.recording_thread.start()
            
        except Exception as e:
            self.logger.error(f"Failed to start audio recording: {e}")
            self.is_recording = False
            raise
    
    def stop_recording(self) -> Optional[str]:
        """Stop recording and save to temporary file"""
        try:
            if not self.is_recording:
                return None
                
            self.is_recording = False
            
            # Wait for recording thread to finish
            if hasattr(self, 'recording_thread'):
                self.recording_thread.join(timeout=2.0)
            
            # Save recorded audio to temporary file
            if self.recording_data:
                self.temp_file_path = self._save_audio_to_temp_file()
                self.logger.info(f"Audio saved to: {self.temp_file_path}")
                return self.temp_file_path
            else:
                self.logger.warning("No audio data recorded")
                return None
                
        except Exception as e:
            self.logger.error(f"Failed to stop audio recording: {e}")
            return None
    
    def _record_audio(self):
        """Record audio data while is_recording is True"""
        try:
            def audio_callback(indata, frames, time, status):
                if status:
                    self.logger.warning(f"Audio callback status: {status}")
                if self.is_recording:
                    self.recording_data.extend(indata.copy())
            
            # Start recording with sounddevice
            with sd.InputStream(
                samplerate=self.rate,
                channels=self.channels,
                dtype=self.dtype,
                callback=audio_callback
            ):
                while self.is_recording:
                    sd.sleep(100)  # Sleep for 100ms
                    
        except Exception as e:
            self.logger.error(f"Error during audio recording: {e}")
    
    def _save_audio_to_temp_file(self) -> str:
        """Save recorded data to a temporary WAV file"""
        try:
            # Create temporary file
            temp_fd, temp_path = tempfile.mkstemp(suffix='.wav', prefix='whisper_')
            os.close(temp_fd)
            
            # Convert list to numpy array
            audio_data = np.array(self.recording_data, dtype=self.dtype)
            
            # Write WAV file using soundfile
            sf.write(temp_path, audio_data, self.rate)
            
            return temp_path
            
        except Exception as e:
            self.logger.error(f"Failed to save audio file: {e}")
            raise
    
    def cleanup_temp_file(self):
        """Delete the temporary audio file"""
        try:
            if self.temp_file_path and os.path.exists(self.temp_file_path):
                os.remove(self.temp_file_path)
                self.logger.info(f"Temporary file deleted: {self.temp_file_path}")
                self.temp_file_path = None
        except Exception as e:
            self.logger.error(f"Failed to delete temporary file: {e}")
    
    def __del__(self):
        """Cleanup when object is destroyed"""
        try:
            self.cleanup_temp_file()
        except:
            pass 