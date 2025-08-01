import random
import string
import time
from datetime import datetime

FILENAME = "README.md"

# Start fresh header
with open(FILENAME, "w", encoding="utf-8") as f:
    f.write(f"# 🚀 Automated README Update\n\n")
    f.write(f"⏰ Last updated on: **{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC**\n\n")

# Emoji and whitespace pool
EMOJIS = ["🚀", "✨", "🔥", "💡", "📌", "🌟", "🛠️", "✅", "🎯", "📈"]
SPACES = [" ", "  ", "   ", "    "]

# Number of commits for the day
num_commits = random.randint(1, 5)

for i in range(num_commits):
    # Open and read
    with open(FILENAME, "a", encoding="utf-8") as f:
        rand_char = random.choice(EMOJIS + SPACES + list(string.ascii_letters))
        f.write(f"\n<!-- noise-{i+1} {rand_char} -->\n")

    print(f"echo 'Commit {i+1}'")
    print("git add README.md")
    print(f"git commit -m '🤖 Auto noise commit #{i+1}' || echo 'No changes'")
    time.sleep(1)
