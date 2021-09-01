import React from "react";
import Login from "../src/Components/Login/Login";
import { Canvas } from "./Canvas";
import { ClearCanvasButton } from "./ClearCanvasButton";

function App() {
  return (
    <>
      {/* <Login /> */}
      <Canvas />
      <ClearCanvasButton />
    </>
  );
}

export default App;
