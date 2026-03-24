# 🐦 Twitter Viral Bot

Ein automatisierter Bot, der virale Tweets findet und analysiert.

## 🚀 Features
- Scannt Twitter Trends automatisch
- Berechnet Viral-Score basierend auf Engagement
- Speichert Ergebnisse in JSON
- Läuft automatisch auf GitHub Actions

## 📅 Zeitplan
- Läuft automatisch alle 6 Stunden
- Kann manuell über GitHub Actions ausgelöst werden

## 📊 Ergebnisse
Die Ergebnisse werden in `viral_posts.json` gespeichert und automatisch committet.

## 🛠️ Lokal ausführen
```bash
pip install -r requirements.txt
python bot.py
```