import React, { useEffect, useState } from 'react';

import AdminTemplate from '../../components/AdminTemplate';
import Input from '../../components/Input';

import { Content, Form, Title, Select, Button } from './styles';

import api from '../../services/api';

export default function AdminGameStore({ history }) {
  const [games, setGames] = useState([]);
  const [stores, setStores] = useState([]);

  const [game, setGame] = useState();
  const [store, setStore] = useState();
  const [value, setValue] = useState();

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

    api
      .post('/api/v1/game-store', {
        game_id: game,
        store_id: store,
        value
      })
      .then(() => history.push('/admin/game-store'))
      .catch(console.error);
  }

  return (
    <AdminTemplate>
      <Content>
        <Form onSubmit={onSubmit}>
          <Title>Game &gt; Store</Title>

          <Input
            placeholder="Value"
            value={value}
            onChange={(e) => setValue(e.target.value)}
          />

          <Select onChange={(e) => setGame(e.target.value)}>
            {games.map((it) => (
              <option key={it.id} value={it.id}>
                {it.name}
              </option>
            ))}
          </Select>

          <Select onChange={(e) => setStore(e.target.value)}>
            {stores.map((it) => (
              <option key={it.id} value={it.id}>
                {it.name}
              </option>
            ))}
          </Select>

          <Button>Salvar</Button>
        </Form>
      </Content>
    </AdminTemplate>
  );
}
