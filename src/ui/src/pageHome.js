import React from "react";

import SignIn from "./componentSignIn";
import Chat from "./componentChat";
import { useContext } from "react";
import { UserContext } from "./App";

const Home = () => {
  const { user, setUser } = useContext(UserContext);
  console.log(user);

  if (user?.loggedIn) {
    return <Chat />;
  } else {
    return <SignIn />;
  }
};

export default Home;
