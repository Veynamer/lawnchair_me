import git
import os
import requests

github_event_before = os.getenv('GITHUB_EVENT_BEFORE')
github_sha = os.getenv('GITHUB_SHA')
telegram_ci_bot_token = os.getenv('TELEGRAM_CI_BOT_TOKEN')
telegram_ci_channel_id = os.getenv('TELEGRAM_CI_CHANNEL_ID')

repository = git.Repo('.')
commits = repository.iter_commits(f'{github_event_before}...{github_sha}')
message = ''

for index, commit in enumerate(commits):
  commit_message = commit.message.replace('\n', '').replace('_', '\\_')
  message += f'''– {commit_message}. [View on GitHub](https://github.com/LawnchairLauncher/lawnchair/commit/{commit.hexsha})'''

requests.get(f'''https://api.telegram.org/bot{telegram_ci_bot_token}/sendMessage?chat_id={telegram_ci_channel_id}&parse_mode=Markdown&text={message}&disable_web_page_preview=true''')