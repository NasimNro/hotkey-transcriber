# 🚀 Desktop & Autostart Setup

## ✅ Was wurde eingerichtet:

### 1. Startskript (`start_transcriber.sh`)
- Aktiviert automatisch das Virtual Environment
- Startet die Whisper Transcriber Anwendung
- Prüft alle Abhängigkeiten vor dem Start

### 2. Desktop-Verknüpfung
- **Datei:** `~/Desktop/whisper-transcriber.desktop`
- **Verwendung:** Doppelklick auf dem Desktop zum Starten

### 3. Autostart (beim Systemstart)
- **Datei:** `~/.config/autostart/whisper-transcriber.desktop`
- **Verhalten:** Startet automatisch beim Anmelden

## 🎯 Verwendung:

### Desktop-Verknüpfung verwenden:
1. Suchen Sie das "Whisper Transcriber" Icon auf Ihrem Desktop
2. Doppelklicken Sie darauf
3. Ein Terminal öffnet sich und die Anwendung startet

### Autostart aktivieren/deaktivieren:
```bash
# Autostart aktivieren
cp whisper-transcriber.desktop ~/.config/autostart/

# Autostart deaktivieren  
rm ~/.config/autostart/whisper-transcriber.desktop
```

### Manuelle Ausführung:
```bash
cd /home/nasim/Desktop/hotkey-transcriber
./start_transcriber.sh
```

## 🔧 Anpassungen:

### Startskript bearbeiten:
```bash
nano start_transcriber.sh
```

### Desktop-Verknüpfung bearbeiten:
```bash
nano whisper-transcriber.desktop
```

## 🎤 Bedienung:
- **Aufnahme:** `Ctrl + Windows-Taste` halten
- **Beenden:** `Ctrl + C` im Terminal

## 📋 Hinweise:
- Das Terminal bleibt offen, um Statusmeldungen zu sehen
- Bei Fehlern werden diese im Terminal angezeigt
- Die Anwendung läuft im Hintergrund und wartet auf die Tastenkombination 