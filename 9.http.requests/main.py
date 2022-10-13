import requests
from nice import nice_print as nprint


my_hero = ('Hulk', 'Captain America', 'Thanos')
def test_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)

    if response.status_code == 200:
        print("Ответ сервера OK")
        res = response.json()
        hero_intelligence = {f'{el["name"]}': f'{el["powerstats"]["intelligence"]}' for el in res}
        my_hero_intelligence = {f'{hero}': f'{hero_intelligence[hero]}' for hero in my_hero}
        sorted_my_hero = sorted(my_hero_intelligence.items(), key=lambda x: int(x[1]), reverse=True)
        nprint(sorted_my_hero[0][0], ' - самый умный герой среди героев: '+', '.join(f'{hero}' for hero in my_hero))
    else:
        print('Ошибка сервера:',response)

if __name__ == "__main__":
    test_request()
