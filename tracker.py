import requests
import urllib3
import json

# disable SSL warnings since the local API uses a self-signed certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Local League of Legends API URL (running locally)
LOCAL_API_URL = "http://127.0.0.1:2999/liveclientdata/allgamedata"

def get_live_data():
    try:
        # verify=False is required to avoid SSL certificate errors
        response = requests.get(LOCAL_API_URL, verify=False, timeout=2)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve data, status code: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Game process not detected. Ensure you are in a game (loading screen or at fountain).")
        return None

def analyze_enemy_spells():
    data = get_live_data()
    if not data:
        return

    # Determine your team (identify allies vs. enemies)
    my_team = None
    active_player_name = data.get('activePlayer', {}).get('summonerName')
    
    all_players = data.get('allPlayers', [])
    for player in all_players:
        if player.get('summonerName') == active_player_name:
            my_team = player.get('team')
            break
            
    print("====== Enemy Summoner Spells ======")
    for player in all_players:
        # Only consider players not on your team
        if player.get('team') != my_team:
            champion = player.get('championName')
            # Summoner spells (usually two)
            spell_1 = player.get('summonerSpells', {}).get('summonerSpellOne', {}).get('displayName')
            spell_2 = player.get('summonerSpells', {}).get('summonerSpellTwo', {}).get('displayName')
            
            # TODO: Later you can parse runes and items to calculate CDR reductions
            # (e.g., Cosmic Insight rune, CDR boots)
            
            print(f"Champion: {champion:<10} | Spell1: {spell_1:<8} | Spell2: {spell_2}")

if __name__ == "__main__":
    analyze_enemy_spells()