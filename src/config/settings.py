"""
Settings Configuration - Manages API keys and application settings
"""

import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # OpenAI API Configuration
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        # Audio Configuration
        self.audio_sample_rate = 16000  # Optimal for Whisper
        self.audio_channels = 1         # Mono
        self.audio_chunk_size = 1024
        
        self.max_audio_file_size = 25 * 1024 * 1024  # 25MB (Whisper API limit)
        
        # Keyboard Configuration
        self.hotkey_combination = "ctrl+shift"
        
        # Logging Configuration
        self.log_level = logging.INFO
        self.log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # Validate settings
        self._validate_settings()
    
    def _validate_settings(self):
        """Validate that required settings are present"""
        if not self.openai_api_key:
            self.logger.error("OPENAI_API_KEY not found in environment variables")
            raise ValueError("OPENAI_API_KEY is required. Please set it in your .env file")
        
        self.logger.info("Settings validated successfully")
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=self.log_level,
            format=self.log_format,
            handlers=[
                logging.StreamHandler(),  # Console output
                logging.FileHandler('whisper_transcriber.log')  # File output
            ]
        )
        
        # Reduce noise from some libraries
        logging.getLogger('openai').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING) 