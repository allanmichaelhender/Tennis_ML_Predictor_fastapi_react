import React from "react";
import { useForm, useWatch, Controller } from "react-hook-form";
import axios from "axios";
import api from "../api";
import { useEffect, useState } from "react";
import Select from "react-select";

const getTodayString = () => new Date().toISOString().split('T')[0];
const todayDate = getTodayString();


const PredictionsForm = ({ isLoggedIn, onPredictionCreated, players }) => {

  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm({
    defaultValues: {
      match_date: todayDate,
    },
  });


  const today = new Date().toISOString().split("T")[0];

  const onSubmit = async (data) => {
    const endpoint = isLoggedIn
      ? "/api/predictions/"
      : "/api/predictions-guest/";

    try {
      const response = await api.post(endpoint, data);

      if (onPredictionCreated) {
        onPredictionCreated(response.data);
      }
    } catch (error) {
      console.error(
        "Submission failed:",
        error.response?.data || error.message,
      );
      alert("Failed to predict match.");
    }
  };

  const onError = (errors) => console.log("Form Validation Errors:", errors);

  return (
    <form className="form-container" onSubmit={handleSubmit(onSubmit, onError)}>
      <label>Player 1</label>
      <Controller
        name="player1_id"
        control={control}
        render={({ field: { onChange, value, ref } }) => (
          <Select
            inputRef={ref}
            options={players}
            classNames={{
              control: () => "form-input select-control",
              menu: () => "select-menu",
              option: (state) =>
                `select-option ${state.isFocused ? "is-focused" : ""} ${state.isSelected ? "is-selected" : ""}`,
            }}
            unstyled
            value={players.find((c) => c.value === value)}
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
            classNames={{
              control: () => "form-input select-control",
              menu: () => "select-menu",
              option: (state) =>
                `select-option ${state.isFocused ? "is-focused" : ""} ${state.isSelected ? "is-selected" : ""}`,
            }}
            unstyled
            value={players.find((c) => c.value === value)}
            onChange={(val) => onChange(val.value)}
          />
        )}
      />

      <label>Optional: Custom Historic Match Date</label>
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

      <button className="form-button" type="submit">
        Submit
      </button>
    </form>
  );
};

export default PredictionsForm;
