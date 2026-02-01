import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

function LoginForm({ onLoginSuccess, route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const title = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();

    try {
      let res;
      if (method === "login") {
        const formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);

        res = await api.post(route, formData);

        localStorage.setItem(ACCESS_TOKEN, res.data.access_token);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh_token);

        if (onLoginSuccess) onLoginSuccess();
        navigate("/");
      } else {
    await api.post(route, { 
        username: username, 
        password: password 
    });
    
    alert("Registration successful! Please login.");
    navigate("/login");
}
    } catch (error) {
      const errorDetail = error.response?.data?.detail || error.message;
      alert(`Error: ${JSON.stringify(errorDetail)}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>{title}</h1>
      <input
        className="form-input"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        className="form-input"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      {loading && <LoadingIndicator />}
      <button className="form-button" type="submit">
        {title}
      </button>
    </form>
  );
}

export default LoginForm;
