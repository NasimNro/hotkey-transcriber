# 🎤 Hotkey Transcriber

Eine Windows-Anwendung für Sprache-zu-Text-Transkription mit OpenAI Whisper API.

## ✨ Features

- **Globale Tastenkombination**: Ctrl + Shift zum Aktivieren
- **Echtzeit-Aufnahme**: Audio wird während des Drückens der Tasten aufgenommen
- **OpenAI Whisper Integration**: Hochqualitative Transkription
- **Automatische Text-Einfügung**: Text wird direkt in das aktive Eingabefeld eingefügt

## 🚀 Installation

### 1. Repository klonen

```bashgit push -u origin main
git clone https://github.com/NasimNro/hotkey-transcriber.git
```

### 2. Python-Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. OpenAI API Key konfigurieren

Erstellen Sie eine `.env` Datei im Hauptverzeichnis:

```
OPENAI_API_KEY=ihr_openai_api_key_hier
```

## 📋 Systemanforderungen

- **Windows 10/11**
- **Python 3.8+**
- **Mikrofon** (für Audioaufnahme)
- **OpenAI API Key** (für Whisper API)

## 🎯 Verwendung

### Anwendung starten

```bash
cd src
python main.py
```

### Bedienung

1. **Anwendung starten** - Die App läuft im Hintergrund
2. **Eingabefeld auswählen** - Klicken Sie in ein beliebiges Textfeld
3. **Aufnahme starten** - Drücken und halten Sie `Ctrl + Shift`
4. **Sprechen** - Sprechen Sie während die Tasten gedrückt sind
5. **Aufnahme beenden** - Lassen Sie die Tasten los
6. **Text wird eingefügt** - Der transkribierte Text erscheint automatisch


## 🔧 Konfiguration

Die Konfiguration erfolgt in `src/config/settings.py`:

- **Audio-Qualität**: 16kHz Mono (optimal für Whisper)
- **Tastenkombination**: Ctrl + Shift

## 📁 Projektstruktur

```
whisper-transcriber/
├── src/
│   ├── main.py                 # Hauptanwendung
│   ├── config/
│   │   └── settings.py         # Konfiguration
│   └── services/
│       ├── keyboard_service.py # Tastatur-Events
│       ├── audio_service.py    # Audio-Aufnahme
│       ├── transcription_service.py # Whisper API
│       └── text_injection_service.py # Text-Einfügung
├── requirements.txt            # Python-Abhängigkeiten
└── README.md                   # Diese Datei
```

## 🛠️ Entwicklung

### Logging

Logs werden in `whisper_transcriber.log` gespeichert.


## 🔒 Datenschutz

- Audio wird nur temporär lokal gespeichert
- Dateien werden nach Transkription gelöscht
- Audio wird an OpenAI Whisper API gesendet (siehe OpenAI Datenschutzrichtlinien)


**Viel Spaß mit Ihrem neuen Sprache-zu-Text-Tool! 🎉**
