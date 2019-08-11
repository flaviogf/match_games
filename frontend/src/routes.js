import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import Games from "./pages/Games";
import AdminAuthentication from "./pages/AdminAuthentication";
import AdminGames from "./pages/AdminGames";
import AdminGame from "./pages/AdminGame";

export default function Routes() {
  return (
    <Router>
      <Route path="/" exact component={Games} />
      <Route path="/admin/authentication" component={AdminAuthentication} />
      <Route path="/admin/games" exact component={AdminGames} />
      <Route path="/admin/games/create" component={AdminGame} />
    </Router>
  );
}
