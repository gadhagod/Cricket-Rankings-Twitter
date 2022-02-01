from src.compare_rankings import compare
from src.tweet import post_tweet

ranking_changes = compare()
if(ranking_changes):
    post_tweet(ranking_changes)
    print("Tweet sent")
else:
    print("No changes")