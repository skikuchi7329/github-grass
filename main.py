import os
import subprocess
from datetime import datetime, timedelta

# 設定
REPO_PATH = 'github-grass'  # リポジトリのパス
COMMIT_MESSAGE = 'Automated commit'
DAYS = 30  # 何日分のコミットを行うか

# リポジトリのパスに移動
os.chdir(REPO_PATH)

# コミットを行う日付を生成
start_date = datetime.now() - timedelta(days=DAYS)

for i in range(DAYS):
    commit_date = start_date + timedelta(days=i)
    date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    with open('file.txt', 'a') as file:
        file.write(f'Commit on {date_str}\n')
    
    # Gitコマンドを実行
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '--date', date_str, '-m', COMMIT_MESSAGE])

# すべてのコミットをプッシュ
subprocess.run(['git', 'push', 'origin', 'main'])
