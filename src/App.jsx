import React from "react";
import "./styles/app.scss";
import SettingBar from "./components/SettingBar";
import Toolbar from "./components/Toolbar";
import Canvas from "./components/Canvas";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";
import Canvas2 from "./components/Canvas2";

const App = () => {
  return (
    <BrowserRouter>
      <div className="app">
        <Switch>
          <Route path="/:id">
            <Toolbar />
            <SettingBar />
            <div className="canvases">
              <Canvas />
              <Canvas2 />
            </div>
          </Route>
          <Redirect to={`f${(+new Date()).toString(16)}`} />
        </Switch>
      </div>
    </BrowserRouter>
  );
};

export default App;
