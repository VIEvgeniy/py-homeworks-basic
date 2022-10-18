import datetime
import requests

url = 'https://api.stackexchange.com/2.3/questions'
date = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day-1)

params = {
    'site': 'stackoverflow',
    'fromdate': date
}
res = requests.get(url=url, params=params).json()
quests = res['items']
python_quests = []

for q in quests:
    if 'python' in q['tags']:
        python_quests.append(q)
# print(python_quests)
print('\n'.join(f'{quest["title"]} - {quest["link"]}' for quest in python_quests))