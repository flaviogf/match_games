import React, { useEffect } from "react";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch
} from "react-router-dom";

import Games from "./pages/Games";
import AdminDashboard from "./pages/AdminDashboard";
import AdminAuthentication from "./pages/AdminAuthentication";
import AdminGames from "./pages/AdminGames";
import AdminGame from "./pages/AdminGame";
import AdminStores from "./pages/AdminStores";

import api from "./services/api";

export default function Routes() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Games} />
        <AnonymousRoute
          path="/admin/authentication"
          component={AdminAuthentication}
        />
        <PrivateRoute path="/admin" exact component={AdminDashboard} />
        <PrivateRoute path="/admin/games" exact component={AdminGames} />
        <PrivateRoute path="/admin/games/create" component={AdminGame} />
        <PrivateRoute path="/admin/stores" exact component={AdminStores} />
      </Switch>
    </Router>
  );
}

function PrivateRoute({ component: Component, ...rest }) {
  useEffect(() => {
    function validateToken() {
      const token = localStorage.getItem("__token");

      api.post(
        "/api/v1/authentication/validate-token",
        {},
        { headers: { Authorization: `Bearer ${token}` } }
      );
    }

    validateToken();
  });

  return (
    <Route
      {...rest}
      render={props =>
        localStorage.getItem("__token") ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: "/admin/authentication",
              state: { from: props.location }
            }}
          />
        )
      }
    />
  );
}

function AnonymousRoute({ component: Component, ...rest }) {
  return (
    <Route
      {...rest}
      render={props =>
        localStorage.getItem("__token") ? (
          <Redirect
            to={{
              pathname: "/admin",
              state: { from: props.location }
            }}
          />
        ) : (
          <Component {...props} />
        )
      }
    />
  );
}
