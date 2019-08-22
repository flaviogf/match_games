import React, { useEffect, useState } from 'react';

import AdminTemplate from '../../components/AdminTemplate';

import { Content, Form, Title, Select, Button } from './styles';

import api from '../../services/api';

export default function AdminGameStore() {
  const [games, setGames] = useState([]);
  const [stores, setStores] = useState([]);

  useEffect(() => {
    function loadGames() {
      api
        .get('/api/v1/games')
        .then((res) => res.data.data)
        .then(setGames)
        .catch(console.error);
    }

    function loadStores() {
      api
        .get('/api/v1/stores')
        .then((res) => res.data.data)
        .then(setStores)
        .catch(console.error);
    }

    loadGames();
    loadStores();
  }, []);

  function onSubmit(e) {
    e.preventDefault();
  }

  return (
    <AdminTemplate>
      <Content>
        <Form onSubmit={onSubmit}>
          <Title>Game &gt; Store</Title>

          <Select>
            {games.map((game) => (
              <option key={game.id} value={game.id}>
                {game.name}
              </option>
            ))}
          </Select>
          <Select>
            {stores.map((store) => (
              <option key={store.id} value={store.id}>
                {store.name}
              </option>
            ))}
          </Select>

          <Button>Salvar</Button>
        </Form>
      </Content>
    </AdminTemplate>
  );
}
