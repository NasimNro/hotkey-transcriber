# �� Hotkey Transcriber (Linux Version)

Eine Linux-Anwendung für Sprache-zu-Text-Transkription mit der OpenAI Whisper API.

## ✨ Features

- **Globale Tastenkombination**: `Ctrl + Shift` zum Aktivieren der Aufnahme.
- **Echtzeit-Aufnahme**: Audio wird aufgenommen, solange die Tastenkombination gehalten wird.
- **OpenAI Whisper Integration**: Nutzt die leistungsstarke Whisper API für hochqualitative Transkriptionen.
- **Automatische Text-Einfügung**: Der transkribierte Text wird direkt in das aktive Eingabefeld eingefügt.

## 📋 Systemanforderungen

- **Linux-Distribution** (getestet unter Ubuntu/Debian)
- **Python 3.10+**
- **Mikrofon** (für die Audioaufnahme)
- **OpenAI API Key**

## 🚀 Installation & Einrichtung

### 1. System-Abhängigkeiten installieren

Diese Anwendung benötigt `xdotool` zur Steuerung von Fenstern und `portaudio19-dev` für die Audioverarbeitung.

```bash
sudo apt-get update && sudo apt-get install xdotool portaudio19-dev
```
*(Hinweis: Bei anderen Linux-Distributionen als Debian/Ubuntu können die Paketnamen abweichen.)*

### 2. Repository klonen

```bash
git clone https://github.com/NasimNro/hotkey-transcriber.git
cd hotkey-transcriber
```

### 3. Virtuelle Umgebung erstellen und aktivieren

Es ist essenziell, eine virtuelle Umgebung (venv) zu verwenden, um die Projekt-Abhängigkeiten sauber vom System zu isolieren.

```bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Umgebung aktivieren (dieser Schritt muss in jeder neuen Terminalsitzung wiederholt werden)


```
*Nach der Aktivierung erscheint `(venv)` am Anfang Ihrer Kommandozeilen-Eingabe.*

### 4. Python-Abhängigkeiten installieren

Installieren Sie alle benötigten Python-Pakete in der aktiven virtuellen Umgebung.

```bash
pip install -r requirements.txt
```

### 5. OpenAI API Key konfigurieren

Erstellen Sie eine `.env`-Datei im Hauptverzeichnis des Projekts und fügen Sie Ihren OpenAI API Key ein:

```bash
echo 'OPENAI_API_KEY="HIER_DEINEN_API_KEY_EINFÜGEN"' > .env
```
*Ersetzen Sie `HIER_DEINEN_API_KEY_EINFÜGEN` mit Ihrem tatsächlichen Schlüssel.*


## 🎯 Verwendung

### 1. Anwendung starten

Stellen Sie sicher, dass Ihre virtuelle Umgebung aktiviert ist (`source venv/bin/activate`). Starten Sie dann die Anwendung aus dem Hauptverzeichnis des Projekts:

```bash
python3 src/main.py
```

### 2. Bedienung

1.  **Anwendung läuft im Hintergrund.**
2.  **Eingabefeld auswählen:** Klicken Sie in ein beliebiges Textfeld (z.B. in einem Texteditor oder Browser).
3.  **Aufnahme starten:** Drücken und halten Sie `Ctrl + Shift`.
4.  **Sprechen:** Sprechen Sie deutlich in Ihr Mikrofon.
5.  **Aufnahme beenden:** Lassen Sie die Tasten los.
6.  **Text wird eingefügt:** Der transkribierte Text erscheint kurz darauf automatisch an der Cursor-Position.
7.  **Beenden:** Drücken Sie `Ctrl + C` im Terminal, in dem die Anwendung läuft.

## 📁 Projektstruktur

```
hotkey-transcriber/
├── src/
│   ├── main.py                 # Hauptanwendung
│   ├── config/
│   │   └── settings.py         # Konfiguration
│   └── services/
│       ├── keyboard_service.py # Tastatur-Events
│       ├── audio_service.py    # Audio-Aufnahme
│       ├── transcription_service.py # Whisper API
│       └── text_injection_service.py # Text-Einfügung
├── .env                        # Hier steht Ihr API Key (wird nicht versioniert)
├── requirements.txt            # Python-Abhängigkeiten
└── README.md                   # Diese Datei
```

## 🛠️ Entwicklung

Logs werden in die Datei `whisper_transcriber.log` im Hauptverzeichnis geschrieben.

## 🔒 Datenschutz

- Audio wird nur temporär lokal für die Verarbeitung gespeichert.
- Die temporären Audiodateien werden nach der Transkription sofort gelöscht.
- Audio-Daten werden zur Transkription an die OpenAI Whisper API gesendet. Beachten Sie hierzu die Datenschutzrichtlinien von OpenAI.


