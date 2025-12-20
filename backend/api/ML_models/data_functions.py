import re

def calculate_games_add_tiebreak(score_string):

    games_p1, games_p2 = 0, 0
    set_scores = score_string.split()
    
    for set_score in set_scores:
        if "RET" in set_score:
            break
        
        match = re.match(r'(\d+)-(\d+)(?:\(\d+\))?', set_score)
        if match:
            p1_games_in_set = int(match.group(1))
            p2_games_in_set = int(match.group(2))
            
            games_p1 += p1_games_in_set
            games_p2 += p2_games_in_set
            
    return games_p1, games_p2