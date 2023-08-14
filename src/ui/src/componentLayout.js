import { useContext } from "react";
import { Outlet, Link } from "react-router-dom";
import { UserContext } from "./App";

const Layout = () => {
  const user = useContext(UserContext);
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/chat">Chat</Link>
          </li>
          <li>User: {user?.displayName ? user.displayName : "None"}</li>
        </ul>
      </nav>

      <Outlet />
    </>
  );
};

export default Layout;
