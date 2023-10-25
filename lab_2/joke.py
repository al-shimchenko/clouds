
import requests

from colorama import Fore

def get_random_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    else:
        return "Не удалось получить шутку"

if __name__ == "__main__":
    #print(get_random_joke())
    print(Fore.GREEN + get_random_joke())
    