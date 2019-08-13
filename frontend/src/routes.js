import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import Games from "./pages/Games";
import AdminDashboard from "./pages/AdminDashboard";
import AdminAuthentication from "./pages/AdminAuthentication";
import AdminGames from "./pages/AdminGames";
import AdminGame from "./pages/AdminGame";
import AdminStores from "./pages/AdminStores";

export default function Routes() {
  return (
    <Router>
      <Route path="/" exact component={Games} />
      <Route path="/admin" exact component={AdminDashboard} />
      <Route path="/admin/authentication" component={AdminAuthentication} />
      <Route path="/admin/games" exact component={AdminGames} />
      <Route path="/admin/games/create" component={AdminGame} />
      <Route path="/admin/stores" exact component={AdminStores} />
    </Router>
  );
}
