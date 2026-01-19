import { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Register from "./pages/Register";
import Home from "./pages/Home";
import { ACCESS_TOKEN } from "./constants";

function Logout({ onLogout }) {
  localStorage.clear();
  useEffect(() => { onLogout(); }, [onLogout]);
  return <Navigate to="/login" />;
}

function App() {
  // Use state so all children re-render when this changes
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem(ACCESS_TOKEN));

  // Function to refresh the login state
  const updateAuthStatus = () => {
    setIsLoggedIn(!!localStorage.getItem(ACCESS_TOKEN));
  };

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          // Pass the reactive isLoggedIn state down to Home
          element={<Home isLoggedIn={isLoggedIn} />}
        />
        <Route 
          path="/login" 
          // Pass the update function so Login can trigger a re-render
          element={<Login onLoginSuccess={updateAuthStatus} />} 
        />
        <Route path="/logout" element={<Logout onLogout={updateAuthStatus} />} />
        <Route path="/register" element={<Register />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
