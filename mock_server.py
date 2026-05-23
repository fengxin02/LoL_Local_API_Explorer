# mock_server.py
from flask import Flask, jsonify

app = Flask(__name__)

# This is a simplified mock dataset emulating the official API format
mock_game_data = {
    "activePlayer": {
        "summonerName": "TEST1"  # assume this is your ID
    },
    "allPlayers": [
        # you (self)
        {
            "summonerName": "TEST1",
            "team": "BLUE",  # BLUE represents the Blue side
            "championName": "Ahri",
            "summonerSpells": {
                "summonerSpellOne": {"displayName": "Flash"},
                "summonerSpellTwo": {"displayName": "Ignite"}
            }
        },
        # simulated enemy player 1
        {
            "summonerName": "EnemyYasuo",
            "team": "RED",  # RED represents the Red side (enemy)
            "championName": "Yasuo",
            "summonerSpells": {
                "summonerSpellOne": {"displayName": "Flash"},
                "summonerSpellTwo": {"displayName": "Teleport"}
            }
        },
        # simulated enemy player 2
        {
            "summonerName": "EnemyLeeSin",
            "team": "RED",
            "championName": "LeeSin",
            "summonerSpells": {
                "summonerSpellOne": {"displayName": "Flash"},
                "summonerSpellTwo": {"displayName": "Smite"}
            }
        }
    ]
}

# Expose a fake endpoint matching the official API path
@app.route('/liveclientdata/allgamedata', methods=['GET'])
def fake_lol_client():
    return jsonify(mock_game_data)

if __name__ == '__main__':
    print("====== Mock League client started! ======")
    print("Serving mock data on port 2999...")
    # Force run on port 2999
    app.run(port=2999)