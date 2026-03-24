import json
from datetime import datetime, timezone

# Sample-Daten
data = [
    {
        "trend": "AI",
        "text": "Amazing new AI breakthrough announced today",
        "likes": 5000,
        "retweets": 2000,
        "replies": 1500,
        "date": str(datetime.now(timezone.utc)),
        "score": 450.75,
        "url": "https://twitter.com/example/1"
    },
    {
        "trend": "Bitcoin",
        "text": "Bitcoin reaches new all-time high",
        "likes": 3500,
        "retweets": 1200,
        "replies": 800,
        "date": str(datetime.now(timezone.utc)),
        "score": 325.50,
        "url": "https://twitter.com/example/2"
    }
]

print(f"✅ Bot läuft! {len(data)} Posts gefunden")

with open("viral_posts.json", "w") as f:
    json.dump(data, f, indent=2)

print("💾 Datei gespeichert!")
