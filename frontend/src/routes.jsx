import React, { useEffect } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';

import Games from './pages/Games';
import AdminDashboard from './pages/AdminDashboard';
import AdminAuthentication from './pages/AdminAuthentication';
import AdminGames from './pages/AdminGames';
import AdminGame from './pages/AdminGame';
import AdminStores from './pages/AdminStores';
import AdminStore from './pages/AdminStore';
import AdminListGameStore from './pages/AdminListGameStore';
import AdminGameStore from './pages/AdminGameStore';

import api from './services/api';

export default function Routes() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Games} />

        <PrivateRoute path="/admin" exact component={AdminDashboard} />

        <Route path="/admin/authentication" component={AdminAuthentication} />

        <PrivateRoute path="/admin/games" exact component={AdminGames} />
        <PrivateRoute path="/admin/games/create" component={AdminGame} />
        <PrivateRoute path="/admin/games/:id" component={AdminGame} />

        <PrivateRoute path="/admin/stores" exact component={AdminStores} />
        <PrivateRoute path="/admin/stores/create" component={AdminStore} />
        <PrivateRoute path="/admin/stores/:id" component={AdminStore} />

        <PrivateRoute
          path="/admin/game-store"
          exact
          component={AdminListGameStore}
        />
        <PrivateRoute
          path="/admin/game-store/create"
          component={AdminGameStore}
        />
        <PrivateRoute path="/admin/game-store/:id" component={AdminGameStore} />

        <Redirect to="/" />
      </Switch>
    </Router>
  );
}

function PrivateRoute({ component: Component, ...rest }) {
  useEffect(() => {
    const headers = { Authorization: localStorage.getItem('__token') };
    api.post('/api/v1/authentication/validate-token', {}, { headers });
  });

  return <Route {...rest} render={(props) => <Component {...props} />} />;
}
