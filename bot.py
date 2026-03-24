import os
import json
from datetime import datetime, timezone

# Einfache Test-Version ohne externe API
def create_sample_data():
    """Erstellt Sample-Daten zum Testen"""
    results = [
        {
            "trend": "AI",
            "text": "Breaking: New AI model released today with amazing features...",
            "likes": 2500,
            "retweets": 890,
            "replies": 340,
            "date": str(datetime.now(timezone.utc)),
            "score": 425.67,
            "url": "https://twitter.com/example/status/123456789"
        },
        {
            "trend": "Bitcoin",
            "text": "Bitcoin breaks through $50k barrier in historic move...",
            "likes": 1800,
            "retweets": 650,
            "replies": 220,
            "date": str(datetime.now(timezone.utc)),
            "score": 312.45,
            "url": "https://twitter.com/example/status/987654321"
        },
        {
            "trend": "Tesla",
            "text": "Tesla announces new battery technology with 1000km range...",
            "likes": 3200,
            "retweets": 1100,
            "replies": 450,
            "date": str(datetime.now(timezone.utc)),
            "score": 524.89,
            "url": "https://twitter.com/example/status/555666777"
        }
    ]
    return results

# Versuche mit snscrape
try:
    import snscrape.modules.twitter as sntwitter
    
    MAX_TWEETS_PER_TREND = 50
    VIRAL_THRESHOLD = 300
    TRENDS = ["Breaking News", "AI", "Bitcoin", "Tesla"]
    
    def viral_score(tweet):
        try:
            now = datetime.now(timezone.utc)
            age_minutes = (now - tweet.date).total_seconds() / 60
            if age_minutes < 1:
                age_minutes = 1
            engagement = (
                tweet.likeCount * 1 +
                tweet.retweetCount * 2 +
                tweet.replyCount * 1.5
            )
            return engagement / age_minutes
        except:
            return 0

    def get_tweets(query):
        tweets = []
        try:
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
                if i >= MAX_TWEETS_PER_TREND:
                    break
                tweets.append(tweet)
            print(f"✓ {len(tweets)} tweets gefunden")
        except Exception as e:
            print(f"✗ Fehler: {e}")
        return tweets

    results = []
    for trend in TRENDS:
        print(f"🔍 Scanne: {trend}")
        tweets = get_tweets(trend)
        
        for t in tweets:
            score = viral_score(t)
            if score > VIRAL_THRESHOLD and t.likeCount > 100:
                results.append({
                    "trend": trend,
                    "text": t.content[:100],
                    "likes": t.likeCount,
                    "retweets": t.retweetCount,
                    "replies": t.replyCount,
                    "date": str(t.date),
                    "score": round(score, 2),
                    "url": t.url
                })
    
    if not results:
        print("⚠️ Keine vialen Posts gefunden, verwende Sample-Daten")
        results = create_sample_data()

except Exception as e:
    print(f"⚠️ snscrape funktioniert nicht: {e}")
    print("📝 Verwende Sample-Daten zum Testen...")
    results = create_sample_data()

# Speichern
print(f"\n✅ {len(results)} Posts gefunden")

with open("viral_posts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("💾 Datei gespeichert: viral_posts.json")
