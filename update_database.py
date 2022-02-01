from src.rankings import get_current_rankings
from src.credentials import creds
from rockset import Client

if __name__ == "__main__":
    db = Client(api_key=creds["rockset"]["api_token"], api_server="api.rs2.usw2.rockset.com").Collection.retrieve("cricket-rankings-bot")
    db.add_docs(get_current_rankings())