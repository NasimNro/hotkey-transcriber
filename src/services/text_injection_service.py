"""
Text Injection Service - Handles inserting transcribed text into active input field
Uses the clipboard and keyboard simulation to insert text
"""

import time
import logging
import pyperclip
from pynput.keyboard import Key, Controller
import subprocess

class TextInjectionService:
    def __init__(self):
        self.keyboard = Controller()
        self.logger = logging.getLogger(__name__)
        
    def inject_text(self, text: str) -> bool:
        """
        Inject transcribed text into the currently active input field
        
        Args:
            text: The text to inject
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not text or not text.strip():
                self.logger.warning("No text to inject")
                return False
            
            # Clean the text
            cleaned_text = text.strip()
            
            # Get current active window info for logging
            active_window = self._get_active_window_info()
            self.logger.info(f"Injecting text into: {active_window}")
            
            # Method 1: Try clipboard method (more reliable for longer text)
            success = self._inject_via_clipboard(cleaned_text)
            
            if not success:
                # Method 2: Fallback to direct typing (for simple cases)
                self.logger.info("Clipboard method failed, trying direct typing")
                success = self._inject_via_typing(cleaned_text)
            
            if success:
                self.logger.info(f"Text injection successful: {len(cleaned_text)} characters")
                print(f"✅ Text eingefügt: {cleaned_text[:50]}{'...' if len(cleaned_text) > 50 else ''}")
            else:
                self.logger.error("Text injection failed")
                print("❌ Fehler beim Einfügen des Textes")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Text injection failed: {e}")
            print(f"❌ Fehler beim Einfügen: {e}")
            return False
    
    def _inject_via_clipboard(self, text: str) -> bool:
        """Inject text using clipboard and Ctrl+V"""
        try:
            # Save current clipboard content
            original_clipboard = ""
            try:
                original_clipboard = pyperclip.paste()
            except:
                pass  # Clipboard might be empty or inaccessible
            
            # Set our text to clipboard
            pyperclip.copy(text)
            
            # Small delay to ensure clipboard is set
            time.sleep(0.1)
            
            # Paste using Ctrl+V
            self.keyboard.press(Key.ctrl)
            self.keyboard.press('v')
            self.keyboard.release('v')
            self.keyboard.release(Key.ctrl)
            
            # Small delay before restoring clipboard
            time.sleep(0.2)
            
            # Restore original clipboard content
            try:
                if original_clipboard:
                    pyperclip.copy(original_clipboard)
            except:
                pass  # Don't fail if we can't restore clipboard
            
            return True
            
        except Exception as e:
            self.logger.error(f"Clipboard injection failed: {e}")
            return False
    
    def _inject_via_typing(self, text: str) -> bool:
        """Inject text by simulating typing (fallback method)"""
        try:
            # Limit text length for typing method to avoid issues
            if len(text) > 500:
                self.logger.warning("Text too long for typing method, truncating")
                text = text[:500] + "..."
            
            # Type the text character by character
            for char in text:
                if char == '\n':
                    self.keyboard.press(Key.enter)
                    self.keyboard.release(Key.enter)
                else:
                    self.keyboard.type(char)
                
                # Small delay between characters to avoid issues
                time.sleep(0.001)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Typing injection failed: {e}")
            return False
    
    def _get_active_window_info(self) -> str:
        """Get information about the currently active window on Linux"""
        try:
            # Using xdotool to get active window title on Linux
            result = subprocess.run(
                ['xdotool', 'getactivewindow', 'getwindowname'],
                capture_output=True, text=True, check=True
            )
            window_title = result.stdout.strip()
            return f"{window_title} (Linux/X11)"
        except (subprocess.CalledProcessError, FileNotFoundError):
            # xdotool might not be installed or might fail
            self.logger.warning("Failed to get active window info. Is xdotool installed?")
            return "Unknown Window (Linux)"
        except Exception as e:
            self.logger.error(f"Failed to get active window info: {e}")
            return "Unknown Window"
    
    def is_input_field_active(self) -> bool:
        """
        Check if an input field is currently active/focused.
        This check is simplified for Linux and defaults to True.
        """
        return True 