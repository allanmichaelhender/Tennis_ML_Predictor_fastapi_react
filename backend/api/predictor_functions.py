import joblib 
import pandas as pd
from pathlib import Path
from core.config import settings

# In FastAPI, we usually define paths relative to the file or via settings
# Assuming 'backend' is your root (where main.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent 

# Update these paths to match your folder structure
ML_models_dir = BASE_DIR / "api" / "ML_models"
random_forest_path = ML_models_dir / 'models/random_forest_model.joblib'
random_forest = joblib.load(random_forest_path)

logistic_regr_pipeline_path = ML_models_dir / 'models/logistic_regr_pipeline.joblib'
logistic_regr_pipeline = joblib.load(logistic_regr_pipeline_path)

decision_tree_pipeline_path = ML_models_dir / 'models/decision_tree_pipeline.joblib'
decision_tree_pipeline = joblib.load(decision_tree_pipeline_path)

data_path = ML_models_dir / 'data/new_data/data.csv'
data = pd.read_csv(data_path,index_col=0)
data['tourney_date'] = pd.to_datetime(data['tourney_date'])


def generate_data(player1_id, player2_id, match_date):
    today_timestamp = pd.to_datetime(match_date)
    six_months_ago = today_timestamp - pd.DateOffset(months=6)
    last_six_months = (data['tourney_date'] >= six_months_ago)
    data_last_six_months = data[last_six_months]
    data_last_six_months = data_last_six_months.sort_values(by='tourney_date', ascending=False)


    player1_w_filter = (data_last_six_months["w_id"] == player1_id)
    player1_l_filter = (data_last_six_months["l_id"] == player1_id)

    player1_w = data_last_six_months[player1_w_filter]
    player1_l = data_last_six_months[player1_l_filter]

    player2_w_filter = (data_last_six_months["w_id"] == player2_id)
    player2_l_filter = (data_last_six_months["l_id"] == player2_id)

    player2_w = data_last_six_months[player2_w_filter]
    player2_l = data_last_six_months[player2_l_filter]

    print("1:",player1_w.head())
    print("2:",player2_w.head())
    print("3:",player1_l.head())
    print("4:",player2_l.head())


    def find_ranking_points(player_w, player_l):
        w_ranking_points = player_w["winner_rank_points"].iloc[0] if not player_w.empty else 0
        l_ranking_points = player_l["loser_rank_points"].iloc[0] if not player_l.empty else 0

        if l_ranking_points < w_ranking_points:
            return l_ranking_points
        
        return w_ranking_points
    
    player1_ranking_points = find_ranking_points(player1_w, player1_l)
    player2_ranking_points = find_ranking_points(player2_w, player2_l)



    ranking_diff = player1_ranking_points - player2_ranking_points

    player1_match_winloss = len(player1_w)/(len(player1_w) + len(player1_l))

    player1_total_game_wins = player1_w["w_games_won"].sum() + player1_l["l_games_won"].sum()
    player1_total_game_losses = player1_w["l_games_won"].sum() + player1_l["w_games_won"].sum()

    player1_game_winloss = player1_total_game_wins / player1_total_game_losses

    total_matches = len(player1_w) + len(player1_l)
    
    player1_aces_per_serve_count = player1_w["w_aces_per_serve"].sum() + player1_l["l_aces_per_serve"].sum()
    player1_aces_per_serve = player1_aces_per_serve_count/total_matches
    
    player1_bp_saved_per_faced_count = player1_w["w_bp_saved_per_faced"].sum() + player1_l["l_bp_saved_per_faced"].sum()
    player1_bp_saved_per_faced = player1_bp_saved_per_faced_count/total_matches
    
    player1_bp_won_per_achieved_count = player1_w["w_bp_won_per_achieved"].sum() + player1_l["l_bp_won_per_achieved"].sum()
    player1_bp_won_per_achieved = player1_bp_won_per_achieved_count/total_matches

    player1_serve_winloss_count = player1_w["w_serve_winloss"].sum() + player1_l["l_serve_winloss"].sum()
    player1_serve_winloss = player1_serve_winloss_count/total_matches
    
    player1_nonserve_winloss_count = player1_w["w_nonserve_winloss"].sum() + player1_l["l_nonserve_winloss"].sum()
    player1_nonserve_winloss = player1_nonserve_winloss_count/total_matches

    player1_firstserve_win_count = player1_w["w_firstserve_win"].sum() + player1_l["w_firstserve_win"].sum()
    player1_firstserve_win = player1_firstserve_win_count/total_matches



    player2_match_winloss = len(player2_w)/(len(player2_w) + len(player2_l))

    player2_total_game_wins = player2_w["w_games_won"].sum() + player2_l["l_games_won"].sum()
    player2_total_game_losses = player2_w["l_games_won"].sum() + player2_l["w_games_won"].sum()

    total_matches = len(player2_w) + len(player2_l)

    player2_game_winloss = player2_total_game_wins / player2_total_game_losses

    player2_aces_per_serve_count = player2_w["w_aces_per_serve"].sum() + player2_l["l_aces_per_serve"].sum()
    player2_aces_per_serve = player2_aces_per_serve_count/total_matches

    player2_bp_saved_per_faced_count = player2_w["w_bp_saved_per_faced"].sum() + player2_l["l_bp_saved_per_faced"].sum()
    player2_bp_saved_per_faced = player2_bp_saved_per_faced_count/total_matches

    player2_bp_won_per_achieved_count = player2_w["w_bp_won_per_achieved"].sum() + player2_l["l_bp_won_per_achieved"].sum()
    player2_bp_won_per_achieved = player2_bp_won_per_achieved_count/total_matches

    player2_serve_winloss_count = player2_w["w_serve_winloss"].sum() + player2_l["l_serve_winloss"].sum()
    player2_serve_winloss = player2_serve_winloss_count/total_matches
    
    player2_nonserve_winloss_count = player2_w["w_nonserve_winloss"].sum() + player2_l["l_nonserve_winloss"].sum()
    player2_nonserve_winloss = player2_nonserve_winloss_count/total_matches

    player2_firstserve_win_count = player2_w["w_firstserve_win"].sum() + player2_l["w_firstserve_win"].sum()
    player2_firstserve_win = player2_firstserve_win_count/total_matches
    
    match_winloss_diff = (player1_match_winloss - player2_match_winloss)
    game_winloss_diff = (player1_game_winloss - player2_game_winloss)
    aces_per_serve_diff = (player1_aces_per_serve - player2_aces_per_serve)
    bp_saved_per_faced_diff = (player1_bp_saved_per_faced - player2_bp_saved_per_faced)
    bp_won_per_faced_diff = (player1_bp_won_per_achieved - player2_bp_won_per_achieved)
    serve_winloss_diff = (player1_serve_winloss - player2_serve_winloss)
    nonserve_winloss_diff = (player1_nonserve_winloss - player2_nonserve_winloss)
    firstserve_win_diff = (player1_firstserve_win - player2_firstserve_win)

    data_list = pd.DataFrame([{
                "ranking_diff": ranking_diff,
                "match_winloss_diff": match_winloss_diff,
                "game_winloss_diff": game_winloss_diff,
                "aces_per_serve_diff": aces_per_serve_diff,
                "bp_saved_per_faced_diff": bp_saved_per_faced_diff,
                "bp_won_per_achieved_diff": bp_won_per_faced_diff,
                "serve_winloss_diff": serve_winloss_diff,
                "nonserve_winloss_diff": nonserve_winloss_diff,
                "firstserve_win_diff": firstserve_win_diff}])
    return data_list



def random_forest_predict(player1_id, player2_id, match_date):

    formatted_data_list = generate_data(player1_id, player2_id, match_date)

    prediction = random_forest.predict_proba(formatted_data_list)

    return prediction


def logistic_regression_predict(player1_id, player2_id, match_date):
    
    formatted_data_list = generate_data(player1_id, player2_id, match_date)

    prediction = logistic_regr_pipeline.predict_proba(formatted_data_list)

    return prediction

def decision_tree_predict(player1_id, player2_id, match_date):
    
    formatted_data_list = generate_data(player1_id, player2_id, match_date)

    prediction = decision_tree_pipeline.predict_proba(formatted_data_list)

    return prediction

