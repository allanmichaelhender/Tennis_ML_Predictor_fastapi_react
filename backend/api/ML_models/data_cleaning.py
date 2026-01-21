import pandas as pd
import numpy as np
from data_functions import calculate_games_add_tiebreak

# data_2015 = pd.read_csv('Data/atp_matches_2015.csv')
# data_2016 = pd.read_csv('Data/atp_matches_2016.csv')
# data_2017 = pd.read_csv('Data/atp_matches_2017.csv')
# data_2018 = pd.read_csv('Data/atp_matches_2018.csv')
# data_2019 = pd.read_csv('Data/atp_matches_2019.csv')
# data_2020 = pd.read_csv('Data/atp_matches_2020.csv')
# data_2021 = pd.read_csv('Data/atp_matches_2021.csv')
# data_2022 = pd.read_csv('Data/atp_matches_2022.csv')
# data_2023 = pd.read_csv('Data/atp_matches_2023.csv')
data_2024 = pd.read_csv('Data/new_data/2024.csv')
data_2025 = pd.read_csv('Data/new_data/2025.csv')
data_2026 = pd.read_csv('Data/new_data/2026.csv')




# index_range = len(data_2024) + len(data_2023) + len(data_2022) + len(data_2021) + len(data_2020) + len(data_2019) + len(data_2018) + len(data_2017) + len(data_2016)
# index_range = len(data_2026) + len(data_2025) + len(data_2024)
# print(index_range)

data = pd.concat([data_2026,data_2025,data_2024]).sort_values('tourney_date').reset_index(drop=True)
data.drop(columns=["winner_seed", "winner_entry","loser_seed", "loser_entry", "minutes"], inplace=True)
data.dropna(inplace=True)
data.reset_index(drop=True)
data['tourney_date'] = pd.to_datetime(data['tourney_date'], format='%Y%m%d')
data[['w_games_won', 'l_games_won']] = data['score'].apply(lambda x: pd.Series(calculate_games_add_tiebreak(x)))

data["w_aces_per_serve"] = np.where(
    data["w_svpt"] == 0,  
    np.nan,                  
    data["w_ace"] / data["w_svpt"] 
    )
data["l_aces_per_serve"] = np.where(
    data["l_svpt"] == 0, 
    np.nan,                
    data["l_ace"] / data["l_svpt"] 
    )

data["w_bp_saved_per_faced"] = np.where(
    data["w_bpFaced"] == 0,  
    np.nan,                  
    data["w_bpSaved"] / data["w_bpFaced"]
    )

data["l_bp_saved_per_faced"] = np.where(
    data["l_bpFaced"] == 0, 
    np.nan,                  
    data["l_bpSaved"] / data["l_bpFaced"]
    )

data["w_bp_won_per_achieved"] = 1 - data["l_bp_saved_per_faced"]
data["l_bp_won_per_achieved"] = 1 - data["w_bp_saved_per_faced"]

data["w_serve_winloss"] = ( data['w_1stWon'] + data['w_2ndWon'] ) / data['w_svpt']
data["l_serve_winloss"] = ( data['l_1stWon'] + data['l_2ndWon'] ) / data['l_svpt']

data["w_nonserve_winloss"] = 1 - data["l_serve_winloss"]
data["l_nonserve_winloss"] = 1 - data["w_serve_winloss"]

data["w_firstserve_win"] = data['w_1stWon']/data['w_svpt']
data["l_firstserve_win"] = data['l_1stWon']/data['w_svpt']

column_mapping = {"winner_id": "w_id", "loser_id": "l_id"}
data.rename(columns=column_mapping, inplace=True)

data = data[['tourney_date', 
             'w_id', 
             'w_games_won', 
             "w_aces_per_serve", 
             "w_bp_saved_per_faced", 
             "w_bp_won_per_achieved", 
             "w_serve_winloss", 
             "w_nonserve_winloss", 
             "w_firstserve_win", 
             "winner_rank_points",
             'l_id', 
             'l_games_won', 
             "l_aces_per_serve", 
             "l_bp_saved_per_faced", 
             "l_bp_won_per_achieved", 
             "l_serve_winloss", 
             "l_nonserve_winloss", 
             "l_firstserve_win", 
             "loser_rank_points"]]

data = data.sort_values(by=['tourney_date', "w_id"], ascending=[False, True])
data = data.reset_index(drop=True)

data.to_csv("data.csv")
