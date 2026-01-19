import React from "react";
import { useForm, useWatch, Controller } from "react-hook-form";
import axios from "axios";
import api from "../api";
import { useEffect, useState } from "react";
import Select from "react-select";

const PredictionsForm = ({isLoggedIn, onPredictionCreated}) => {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm({
    defaultValues: {
      player1_id: null,
    },
  });

  const [players, setPlayers] = useState([]);

  useEffect(() => {
    api
      .get("/api/players/")
      .then((response) => {
        // Axios puts the response data in a 'data' property
        const formattedPlayers = response.data.map((p) => ({
          value: p.player_id,
          label: p.full_name,
        }));
        setPlayers(formattedPlayers);
      })
      .catch((err) => {
        // Axios automatically catches 4xx and 5xx errors
        console.error("API error:", err.message);
      });
  }, []);

  const today = new Date().toISOString().split("T")[0];

const onSubmit = async (data) => {
    // 1. Determine endpoint
    const endpoint = isLoggedIn ? "/api/predictions/" : "/api/predictions-guest/";

    try {
        const response = await api.post(endpoint, data);
        alert("Match Predicted!");

        // 2. Use the new prop 'onPredictionCreated' for BOTH cases.
        // Even if logged in, passing response.data is faster than re-fetching the whole list.
        if (onPredictionCreated) {
            onPredictionCreated(response.data);
        }

    } catch (error) {
        console.error("Submission failed:", error.response?.data || error.message);
        alert("Failed to predict match.");
    }
};

  const onError = (errors) => console.log("Form Validation Errors:", errors);

  return (
    <form onSubmit={handleSubmit(onSubmit, onError)}>
      <label>Player 1</label>
      <Controller
        name="player1_id"
        control={control}
        render={({ field: { onChange, value, ref } }) => (
          <Select
            inputRef={ref}
            options={players}
            // Match the current ID value to the correct object in 'players' list
            value={players.find((c) => c.value === value)}
            // Send only the ID (val.value) back to react-hook-form
            onChange={(val) => onChange(val.value)}
          />
        )}
      />

      <label>Player 2</label>
      <Controller
        name="player2_id"
        control={control}
        render={({ field: { onChange, value, ref } }) => (
          <Select
            inputRef={ref}
            options={players}
            // Match the current ID value to the correct object in 'players' list
            value={players.find((c) => c.value === value)}
            // Send only the ID (val.value) back to react-hook-form
            onChange={(val) => onChange(val.value)}
          />
        )}
      />

      <input
        type="date"
        className="date-input-field"
        {...register("match_date", {
          required: "A date is required",
          min: {
            value: "2024-01-01",
            message: "Date cannot be before January 1st, 2024",
          },
          max: {
            value: today,
            message: "Date cannot be in the future",
          },
        })}
      />
      {errors.start_date && <span>{errors.start_date.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
};

export default PredictionsForm;
