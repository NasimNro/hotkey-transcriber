"""
Transcription Service - Handles OpenAI Whisper API integration
Sends audio files to Whisper API and returns transcribed text
"""




from openai import OpenAI
import openai
import logging
from typing import Optional
import os
from pathlib import Path

class TranscriptionService:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.logger = logging.getLogger(__name__)
        
    def transcribe_audio(self, audio_file_path: str) -> Optional[str]:
        """
        Transcribe audio file using OpenAI Whisper API
        
        Args:
            audio_file_path: Path to the audio file
            language: Language code (default: "de" for German)
            
        Returns:
            Transcribed text or None if failed
        """
        try:
            if not os.path.exists(audio_file_path):
                self.logger.error(f"Audio file not found: {audio_file_path}")
                return None
            
            # Check file size (Whisper API has 25MB limit)
            file_size = os.path.getsize(audio_file_path)
            if file_size > 25 * 1024 * 1024:  # 25MB
                self.logger.error(f"Audio file too large: {file_size} bytes")
                return None
            
            self.logger.info(f"Transcribing audio file: {audio_file_path}")
            
            # Open and transcribe the audio file
            with open(audio_file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                )
            
            # The response is directly the text when using response_format="text"
            transcribed_text = transcript.text
            self.logger.info(f"Transcription: {transcribed_text}")
            
            if transcribed_text:
                self.logger.info(f"Transcription successful: {len(transcribed_text)} characters")
                return transcribed_text
            else:
                self.logger.warning("Transcription returned empty text")
                return None
                
        except openai.APIError as e:
            self.logger.error(f"OpenAI API error: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Transcription failed: {e}")
            return None
    
    