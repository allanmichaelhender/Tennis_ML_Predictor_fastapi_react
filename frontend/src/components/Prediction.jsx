import React from "react";

export default function Prediction({ prediction, onDelete, players }) {
  const player1Obj = players.find(
    (p) => String(p.value) === String(prediction.player1_id),
  );
  const player2Obj = players.find(
    (p) => String(p.value) === String(prediction.player2_id),
  );

  const formattedDate = new Date(prediction.submission_date).toLocaleDateString(
    "en-UK",
  );

  const formatOdds = (val) => (val != null ? Number(val).toFixed(3) : "N/A");

  const isWinner = (val1, val2) => (val1 > val2 ? "winner" : "");

 return (
    <div className="prediction-card">
      <div className="card-header">
        <div className="matchup">
          <span className="player-name">{player1Obj?.label || "Unknown"}</span>
          <span className="vs-badge">VS</span>
          <span className="player-name">{player2Obj?.label || "Unknown"}</span>
        </div>
        <p className="match-date">{prediction.match_date}</p>
      </div>

      <div className="stats-grid">
        <div className="model-labels">
          <div className="spacer" style={{ height: "20px" }}></div>
          <p>Logistic</p>
          <p>R-Forest</p>
          <p>D-Tree</p>
        </div>

        <div className="player-stats">
          <h4 className="player-sub-name">{player1Obj?.label.split(" ").pop()}</h4>
          <p className={`odds-val ${isWinner(prediction.player1WinOddsLogistic, prediction.player2WinOddsLogistic)}`}>
            {formatOdds(prediction.player1WinOddsLogistic)}%
          </p>
          <p className={`odds-val ${isWinner(prediction.player1WinOddsRForest, prediction.player2WinOddsRForest)}`}>
            {formatOdds(prediction.player1WinOddsRForest)}%
          </p>
          <p className={`odds-val ${isWinner(prediction.player1WinOddsDTree, prediction.player2WinOddsDTree)}`}>
            {formatOdds(prediction.player1WinOddsDTree)}%
          </p>
        </div>

        <div className="player-stats">
          <h4 className="player-sub-name">{player2Obj?.label.split(" ").pop()}</h4>
          <p className={`odds-val ${isWinner(prediction.player2WinOddsLogistic, prediction.player1WinOddsLogistic)}`}>
            {formatOdds(prediction.player2WinOddsLogistic)}%
          </p>
          <p className={`odds-val ${isWinner(prediction.player2WinOddsRForest, prediction.player1WinOddsRForest)}`}>
            {formatOdds(prediction.player2WinOddsRForest)}%
          </p>
          <p className={`odds-val ${isWinner(prediction.player2WinOddsDTree, prediction.player1WinOddsDTree)}`}>
            {formatOdds(prediction.player2WinOddsDTree)}%
          </p>
        </div>
      </div>

      <button className="delete-icon-button" onClick={() => onDelete(prediction.id)}>
        ×
      </button>
    </div>
  );
}
