from datetime import datetime

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# 🚀 \n\n")
    f.write(f"⏰ Last updated on: **{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC**\n")
