from rockset import Client, Q
from .rankings import get_current_rankings
from .credentials import creds

query = Client(api_key=creds["rockset"]["api_token"], api_server="api.rs2.usw2.rockset.com").sql

def compare():
    result = "";
    old_rankings = query(Q("cricket-rankings-bot").select("_id", "data"))
    new_rankings = get_current_rankings()

    for new_position in new_rankings:
        position_change = False
        position_result = "\n" + new_position["_id"].upper().replace("_", " ")
        for old_position in old_rankings:
            if(old_position["_id"] == new_position["_id"]):
                break
        for new_format in new_position["data"]:
            new_data = new_position["data"][new_format]
            old_data = old_position["data"][new_format]

            for i in range(len(new_data)):
                new_player = new_data[i]
                old_player = old_data[i]
                if(new_player["name"] != old_player["name"]):
                    position_change = True
                    player_prev_rank = None
                    for new_new_player in old_data:
                        if(new_new_player["name"] == new_player["name"]):
                            player_prev_rank = new_new_player["rank"]

                            if(player_prev_rank > new_player["rank"]):
                                change = "⬆"
                            else:
                                change = "⬇️"
                    if not player_prev_rank:
                        change = "⬆"

                    player_name = new_player["name"][0] + new_player["name"][new_player["name"].find(" "):]
                    position_result += "\n" + change + player_name + " #" + str(new_player["rank"]) + " in " + new_format
            
        if(position_change):
            result += position_result

    if result:
        result = result[1:]

    return result