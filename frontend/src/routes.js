import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import Games from "./pages/Games";
import AdminAuthentication from "./pages/AdminAuthentication";
import AdminGame from "./pages/AdminGame";

export default function Routes() {
  return (
    <Router>
      <Route path="/" exact component={Games} />
      <Route path="/admin/authentication" component={AdminAuthentication} />
      <Route path="/admin/games" component={AdminGame} />
    </Router>
  );
}
