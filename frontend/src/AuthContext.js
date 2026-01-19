import { createContext, useState, useEffect, useContext } from "react";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "./constants";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  // Use a function in useState so it only runs once on initial load
  const [isLoggedIn, setIsLoggedIn] = useState(() => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    // Check if token exists and isn't the literal string "null" or "undefined"
    return !!token && token !== "undefined" && token !== "null";
  });

  const login = (token) => {
    if (token) {
      localStorage.setItem(ACCESS_TOKEN, token);
      setIsLoggedIn(true);
    }
  };

  const logout = () => {
    localStorage.removeItem(ACCESS_TOKEN);
    localStorage.removeItem(REFRESH_TOKEN);
    setIsLoggedIn(false);
  };

  useEffect(() => {
    const syncAuth = (event) => {
      if (event.key === ACCESS_TOKEN) {
        setIsLoggedIn(!!event.newValue && event.newValue !== "null");
      }
    };
    window.addEventListener("storage", syncAuth);
    return () => window.removeEventListener("storage", syncAuth);
  }, []);

  return (
    <AuthContext.Provider value={{ isLoggedIn, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
