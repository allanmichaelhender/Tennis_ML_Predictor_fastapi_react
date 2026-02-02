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
        <div className="model-column">
          <h4>Logistic</h4>
          <div className="odds-row">
            <span className="odds-val">
              {formatOdds(prediction.player1WinOddsLogistic)}
            </span>
            <span className="odds-val">
              {formatOdds(prediction.player2WinOddsLogistic)}
            </span>
          </div>
        </div>

        <div className="model-column">
          <h4>R-Forest</h4>
          <div className="odds-row">
            <span className="odds-val">
              {formatOdds(prediction.player1WinOddsRForest)}
            </span>
            <span className="odds-val">
              {formatOdds(prediction.player2WinOddsRForest)}
            </span>
          </div>
        </div>

        <div className="model-column">
          <h4>D-Tree</h4>
          <div className="odds-row">
            <span className="odds-val">
              {formatOdds(prediction.player1WinOddsDTree)}
            </span>
            <span className="odds-val">
              {formatOdds(prediction.player2WinOddsDTree)}
            </span>
          </div>
        </div>
      </div>

      <button
        className="delete-icon-button"
        onClick={() => onDelete(prediction.id)}
        title="Delete Prediction"
      >
        ×
      </button>
    </div>
  );
}
