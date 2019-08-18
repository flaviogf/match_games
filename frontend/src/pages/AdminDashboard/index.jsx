import React, { useEffect, useState } from 'react';

import AdminTemplate from '../../components/AdminTemplate';

import { Container, Stats } from './styles';

import api from '../../services/api';

const wave = require('../../assets/wave.svg');

export default function AdminDashboard() {
  const [games, setGames] = useState(0);
  const [stores, setStores] = useState(0);
  const [users, setUsers] = useState(0);

  useEffect(() => {
    function loadStats() {
      api
        .get('/api/v1/stats')
        .then((res) => res.data.data)
        .then((stats) => {
          setGames(stats.games);
          setStores(stats.stores);
          setUsers(stats.users);
        });
    }

    loadStats();
  }, [games, stores, users]);

  return (
    <AdminTemplate>
      <Container>
        <Stats color="linear-gradient(to bottom, #39a3f4 1%, #279cf5 99%)">
          <h3>Games</h3>
          <span>{games}</span>
          <img src={wave} alt="icon" />
        </Stats>

        <Stats color="linear-gradient(to bottom, #76be45, #66b92d)">
          <h3>Stores</h3>
          <span>{stores}</span>
          <img src={wave} alt="icon" />
        </Stats>

        <Stats color="linear-gradient(to bottom, #dea242, #d5942e)">
          <h3>Users</h3>
          <span>{users}</span>
          <img src={wave} alt="icon" />
        </Stats>
      </Container>
    </AdminTemplate>
  );
}
