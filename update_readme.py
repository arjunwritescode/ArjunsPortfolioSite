import random
import time
from datetime import datetime

EMOJIS = ["🚀", "✨", "🔥", "💡", "📌", "🌟", "🛠️", "✅", "🎯", "📈"]
SPACES = ["", " ", "  ", "   ", "    "]

def make_random_change():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.readlines()

    # Choose a random line and modify it slightly
    if content:
        line_to_modify = random.randint(0, len(content)-1)
        change = random.choice(SPACES + EMOJIS)
        content[line_to_modify] = content[line_to_modify].rstrip() + change + "\n"
    else:
        content = [f"# Random README update {random.choice(EMOJIS)}\n"]

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(content)

# Initial timestamp for the day
with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# 🚀 Automated README Update\n\n")
    f.write(f"⏰ Last updated on: **{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC**\n\n")

# Perform 1 to 5 tiny changes + commit shell commands
num_changes = random.randint(1, 5)

for i in range(num_changes):
    make_random_change()

    # Write shell commands to commit each change individually
    print(f"echo Commit {i+1}")
    print("git add README.md")
    print(f"git commit -m '🤖 Auto commit #{i+1}' || echo 'No changes'")
    time.sleep(1)
