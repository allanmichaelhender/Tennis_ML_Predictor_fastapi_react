import pandas as pd
from data_cleaning import data
import numpy as np

index_range = len(data)

row_list = []   
for index in range(index_range):    
        guess = np.random.randint(0, 2)

        if guess == 1:
            player1 = data.iloc[index, data.columns.get_loc('w_id')]
            player2 = data.iloc[index, data.columns.get_loc('l_id')]

            ranking_diff = (data.iloc[index, data.columns.get_loc('winner_rank_points')]-data.iloc[index, data.columns.get_loc('loser_rank_points')])##/np.min([data.iloc[index, data.columns.get_loc('winner_rank_points')], data.iloc[index, data.columns.get_loc('loser_rank_points')]])

            player1_w_value = 1


        if guess == 0:
            player2 = data.iloc[index, data.columns.get_loc('w_id')]
            player1 = data.iloc[index, data.columns.get_loc('l_id')]

            ranking_diff = (data.iloc[index, data.columns.get_loc('loser_rank_points')] - data.iloc[index, data.columns.get_loc('winner_rank_points')])##/np.min([data.iloc[index, data.columns.get_loc('winner_rank_points')], data.iloc[index, data.columns.get_loc('loser_rank_points')]])

            player1_w_value = 0

        initial_date = data.iloc[index, data.columns.get_loc('tourney_date')]
        six_months_before = initial_date - pd.DateOffset(months=6)
        is_in_range = (data['tourney_date'] >= six_months_before) & (data['tourney_date'] < initial_date)
 
        #filter data to within 6 months
        data_in_range = data[is_in_range]

        player1_w_filter = (data_in_range["w_id"] == player1)
        player1_l_filter = (data_in_range["l_id"] == player1)

        player1_w = data_in_range[player1_w_filter]
        player1_l = data_in_range[player1_l_filter]

        player2_w_filter = (data_in_range["w_id"] == player2)
        player2_l_filter = (data_in_range["l_id"] == player2)

        player2_w = data_in_range[player2_w_filter]
        player2_l = data_in_range[player2_l_filter]


        if (len(player1_w) + len(player1_l) >= 10) & (len(player2_w) + len(player2_l) >= 10):

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

            player2_game_winloss = player2_total_game_wins / player2_total_game_losses

            total_matches = len(player2_w) + len(player2_l)


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

            row_list.append({
                "player1_win": player1_w_value,
                "ranking_diff": ranking_diff,
                "match_winloss_diff": match_winloss_diff,
                "game_winloss_diff": game_winloss_diff,
                "aces_per_serve_diff": aces_per_serve_diff,
                "bp_saved_per_faced_diff": bp_saved_per_faced_diff,
                "bp_won_per_achieved_diff": bp_won_per_faced_diff,
                "serve_winloss_diff": serve_winloss_diff,
                "nonserve_winloss_diff": nonserve_winloss_diff,
                "firstserve_win_diff": firstserve_win_diff})



ML_ready_data = pd.DataFrame(row_list)
ML_ready_data.to_csv("ML_ready_data.csv")




