import React, { useState, useEffect } from "react";
import io from "socket.io-client";
import "./Login.css";

let socket;
const CONNECTION_PORT = "localhost:3002/";

function Login() {
  // Before Login
  const [loggedIn, setLoggedIn] = useState(false);
  const [room, setRoom] = useState("");
  const [userName, setUserName] = useState("");

  useEffect(() => {
    socket = io(CONNECTION_PORT);
  }, [CONNECTION_PORT]);

  const connectToRoom = () => {
    setLoggedIn(true);
    socket.emit("join_room", room);
    console.log(room);
  };

  return (
    <div className="App">
      {!loggedIn ? (
        <div className="logIn">
          <div className="inputs">
            <input
              type="text"
              placeholder="Name..."
              onChange={(e) => {
                setUserName(e.target.value);
              }}
            />
            <input
              type="text"
              placeholder="Room..."
              onChange={(e) => {
                setRoom(e.target.value);
              }}
            />
          </div>
          <button onClick={connectToRoom}>Enter Chat</button>
        </div>
      ) : (
        <div className="chatContainer">hello</div>
      )}
    </div>
  );
}

export default Login;
