import os
import subprocess
import random
from datetime import datetime
import config

# 設定
REPO_PATH = config.path  
COMMIT_MESSAGE = 'Automated commit'
COMMITS = random.randint(1, 10)  

print("Starting script...")

# リポジトリのパスに移動
try:
    os.chdir(REPO_PATH)
    print(f"Changed directory to {REPO_PATH}")
except FileNotFoundError:
    print(f"Error: The directory {REPO_PATH} does not exist.")
    exit(1)

# コミットを行う
for i in range(COMMITS):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d %H:%M:%S')
    with open('file.txt', 'a') as file:
        file.write(f'Commit {i+1} on {date_str}\n')
    print(f"Added entry to file.txt for commit {i+1}")
    
    # Gitコマンドを実行
    subprocess.run(['git', 'add', '.'])
    print(f"git add executed for commit {i+1}")
    
    subprocess.run(['git', 'commit', '-m', f"{COMMIT_MESSAGE} {i+1}"])
    print(f"git commit executed for commit {i+1}")

# すべてのコミットをプッシュ
subprocess.run(['git', 'push', 'origin', 'main'])
print("All commits pushed to origin/main")

print("Script finished.")
