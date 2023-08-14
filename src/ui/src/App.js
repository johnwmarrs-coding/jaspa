import logo from "./logo.svg";
import { createContext, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pageHome";
import Chat from "./pageChat";
import Layout from "./componentLayout";

const UserContext = createContext();

function App() {
  const [user, setUser] = useState({
    authToken: null,
    displayName: "John",
    loggedIn: true,
  });
  return (
    <UserContext.Provider value={user}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="chat" element={<Chat />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </UserContext.Provider>
  );
}

export { App, UserContext };
