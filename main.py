import os
import subprocess
import random
from datetime import datetime
import config

# 設定
REPO_PATH = config.path # r'' を使用してエスケープシーケンスを避ける
COMMIT_MESSAGE = 'Automated commit'
COMMITS = random.randint(1, 3)  

print("Starting script...")

# リポジトリのパスに移動
try:
    if os.path.exists(REPO_PATH):
        os.chdir(REPO_PATH)
        print(f"Changed directory to {REPO_PATH}")
    else:
        print(f"Error: The directory {REPO_PATH} does not exist.")
        exit(1)
except OSError as e:
    print(f"Error: {e}")
    exit(1)

# コミットを行う
for i in range(COMMITS):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d %H:%M:%S')
    with open('file.txt', 'a') as file:
        file.write(f'Commit {i+1} on {date_str}\n')
    print(f"Added entry to file.txt for commit {i+1}")
    
    # Gitコマンドを実行
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        print(f"git add executed for commit {i+1}")
        
        subprocess.run(['git', 'commit', '-m', f"{COMMIT_MESSAGE} {i+1}"], check=True)
        print(f"git commit executed for commit {i+1}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")
        exit(1)

# すべてのコミットをプッシュ
try:
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    print("All commits pushed to origin/main")
except subprocess.CalledProcessError as e:
    print(f"Error during git push: {e}")
    exit(1)

print("Script finished.")
