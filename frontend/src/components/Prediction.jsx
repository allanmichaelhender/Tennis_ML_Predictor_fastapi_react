import React from "react";

export default function Prediction({ prediction, onDelete, players }) {
  const player1Obj = players.find((p) => String(p.value) === String(prediction.player1_id));
  const player2Obj = players.find((p) => String(p.value) === String(prediction.player2_id));

  const formattedDate = new Date(prediction.submission_date).toLocaleDateString(
    "en-UK",
  );

  const formatOdds = (val) => (val != null ? Number(val).toFixed(3) : "N/A");



return (
    <div className="prediction-container">
      <p className="prediction-content">
        {player1Obj?.label || "Loading..."} vs. {player2Obj?.label || "Loading..."}
      </p>
      <p className="prediction-content">Match Date: {prediction.match_date}</p>
      <br />
      
      <p>Logistic Regression Odds:</p>
      <p className="prediction-content">
        {player1Obj?.label}: {formatOdds(prediction.player1WinOddsLogistic)}
      </p>
      <p className="prediction-content">
        {player2Obj?.label}: {formatOdds(prediction.player2WinOddsLogistic)}
      </p>
      <br />
      
      <p>Random Forest Odds:</p>
      <p className="prediction-content">
        {player1Obj?.label}: {formatOdds(prediction.player1WinOddsRForest)}
      </p>
      <p className="prediction-content">
        {player2Obj?.label}: {formatOdds(prediction.player2WinOddsRForest)}
      </p>
      <br />
      
      <p>Decision Tree Odds:</p>
      <p className="prediction-content">
        {player1Obj?.label}: {formatOdds(prediction.player1WinOddsDTree)}
      </p>
      <p className="prediction-content">
        {player2Obj?.label}: {formatOdds(prediction.player2WinOddsDTree)}
      </p>
      
      <button className="delete-button" onClick={() => onDelete(prediction.id)}>
        Delete
      </button>
    </div>
  );
}