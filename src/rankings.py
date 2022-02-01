from requests import get

def get_current_rankings():
    api_url = "https://cricket-rankings-api.herokuapp.com/api/v1"
    batter_rankings = get(f"{api_url}/batters").json()
    bowler_rankings = get(f"{api_url}/bowlers").json()
    all_rounder_rankings = get(f"{api_url}/all_rounders").json()

    new_batter_rankings = {}
    for format in batter_rankings:
        new_batter_rankings[format["format"]] = format["data"][:10]

    new_bowler_rankings = {}
    for format in bowler_rankings:
        new_bowler_rankings[format["format"]] = format["data"][:10]

    new_all_rounder_rankings = {}
    for format in all_rounder_rankings:
        new_all_rounder_rankings[format["format"]] = format["data"][:10]

    return [
        {"_id": "batters", "data": new_batter_rankings},
        {"_id": "bowlers", "data": new_bowler_rankings},
        {"_id": "all_rounders", "data": new_all_rounder_rankings}
    ]