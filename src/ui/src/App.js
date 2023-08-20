import logo from "./logo.svg";
import { createContext, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pageHome";
import Layout from "./componentLayout";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

const UserContext = createContext();

function App() {
  const [user, setUser] = useState({
    authToken: null,
    name: null,
    loggedIn: false,
  });

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <UserContext.Provider value={{ user, setUser }}>
        <BrowserRouter>
          <Routes>
            <Route index element={<Home />} />
          </Routes>
        </BrowserRouter>
      </UserContext.Provider>
    </LocalizationProvider>
  );
}

export { App, UserContext };
