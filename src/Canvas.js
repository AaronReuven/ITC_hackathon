import React, { useEffect } from "react";
import { useCanvas } from "./CanvasContext";
import "./canvas.css";

export function Canvas() {
  const { canvasRef, prepareCanvas, startDrawing, finishDrawing, draw } =
    useCanvas();

  useEffect(() => {
    prepareCanvas();
  }, []);

  return (
    <canvas
      className="canvas"
      onMouseDown={startDrawing}
      onMouseUp={finishDrawing}
      onMouseMove={draw}
      ref={canvasRef}
    />
  );
}
