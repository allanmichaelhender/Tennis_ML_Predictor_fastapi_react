import { useState, useEffect } from "react";
import api from "../api";
import PredictionsForm from "../components/PredictionsForm";
import Prediction from "../components/Prediction";
import "../styles/Home.css";

function Home({ isLoggedIn }) {
  const [predictions, setPredictions] = useState([]);
  console.log(isLoggedIn);

  // This effect now only handles FETCHING data when the login status is true
  useEffect(() => {
    if (isLoggedIn) {
      getPredictions();
    } else {
      // Clear predictions if they log out, or keep empty for guest
      setPredictions([]);
    }
  }, [isLoggedIn]); // Re-run whenever isLoggedIn prop changes

  const getPredictions = async () => {
    try {
      const res = await api.get("/api/predictions/");
      setPredictions(res.data);
    } catch (err) {
      alert(err);
    }
  };

  const handleNewPrediction = (predictionData) => {
    // For guests, predictionData is the direct JSON result from your POST response
    setPredictions((prev) => [predictionData, ...prev]);
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
    <div>
      <PredictionsForm
        onPredictionCreated={handleNewPrediction}
        isLoggedIn={isLoggedIn}
      />
      <div className="predictions-list">
        <h2>Predictions</h2>
        {predictions.map((p) => (
          <Prediction
            key={p.id}
            prediction={p}
            onDelete={() => deletePrediction(p.id)}
          />
        ))}
      </div>
    </div>
  );
}

export default Home;
