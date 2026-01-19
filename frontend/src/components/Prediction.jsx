import React from "react";
import "../styles/Note.css";

export default function Prediction({ prediction, onDelete }) {
  const formattedDate = new Date(prediction.submission_date).toLocaleDateString(
    "en-UK"
  );

  return (
    <div className="note-container">
      <h1>ID: {prediction.id}</h1>
      <p className="note-title">player1_id {prediction.player1_id}</p>
      <p className="note-content">player2_id {prediction.player2_id}</p>
      <p className="note-content">match_date {prediction.match_date}</p>
      <p className="note-content">player1WinOddsLogistic {prediction.player1WinOddsLogistic}</p>
      <p className="note-content">player2WinOddsLogistic {prediction.player2WinOddsLogistic}</p>
      <p className="note-content">player1WinOddsRForest {prediction.player1WinOddsRForest}</p>
      <p className="note-content">player2WinOddsRForest {prediction.player2WinOddsRForest}</p>
      <p className="note-content">player1WinOddsDTree {prediction.player1WinOddsDTree}</p>
      <p className="note-content">player2WinOddsDTree {prediction.player2WinOddsDTree}</p>
      <button className="delete-button" onClick={() => onDelete(prediction.id)}>
        Delete
      </button>
    </div>
  );
}
