import { useState, useEffect } from "react";
import api from "../api";
import PredictionsForm from "../components/PredictionsForm";
import Prediction from "../components/Prediction";
import "../styles/Home.css";
import "../styles/Form.css";
import "../styles/Prediction.css";
import { v4 as uuidv4 } from 'uuid';

function Home({ isLoggedIn }) {
  const [predictions, setPredictions] = useState([]);
  const [players, setPlayers] = useState([]);
  

  useEffect(() => {
    if (isLoggedIn) {
      getPredictions();
    } else {
      setPredictions([]);
    }
  }, [isLoggedIn]);

  useEffect(() => {
    api
      .get("/api/players/")
      .then((response) => {
        const formattedPlayers = response.data.map((p) => ({
          value: p.player_id,
          label: p.full_name,
        })); 
        setPlayers(formattedPlayers);
      })
      .catch((err) => {
        console.error("API error:", err.message);
      });
  }, []);

  const getPredictions = async () => {
    try {
      const res = await api.get("/api/predictions/");
      setPredictions(res.data);
    } catch (err) {
      alert(err);
    }
  };

const handleNewPrediction = (predictionData) => {
  const predictionWithId = {
    ...predictionData,
    id: predictionData.id || uuidv4()
  };

  setPredictions((prev) => [predictionWithId, ...prev]);
};

  const deletePrediction = async (id) => {
    if (isLoggedIn) {
      try {
        const res = await api.delete(`/api/predictions/${id}/`);

        if (res.status === 204) {
          alert("Prediction deleted!");
        } else {
          alert("Failed to delete note.");
        }

        await getPredictions();
      } catch (err) {
        alert(err);
      }
    } else {
      setPredictions(predictions.filter((p) => p.id !== id));
    }
  };

  return (
    <div className="home-wrapper">
      <PredictionsForm
        onPredictionCreated={handleNewPrediction}
        isLoggedIn={isLoggedIn}
        players={players}
      />
      <div className="predictions-list">
        {predictions.map((p) => (
          <Prediction
            key={p.id}
            prediction={p}
            onDelete={() => deletePrediction(p.id)}
            players={players}
          />
        ))}
      </div>
    </div>
  );
}

export default Home;
