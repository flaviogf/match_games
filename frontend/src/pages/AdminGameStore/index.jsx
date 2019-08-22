import React, { useEffect, useState } from 'react';

import { toast } from 'react-toastify';

import AdminTemplate from '../../components/AdminTemplate';
import Input from '../../components/Input';

import { Content, Form, Title, Select, Button, Buttons } from './styles';

import api from '../../services/api';

export default function AdminGameStore({ history, match }) {
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

  useEffect(() => {
    if (!match.params.id) return;

    api
      .get(`/api/v1/game-store/${match.params.id}`)
      .then((res) => res.data.data)
      .then((gameStore) => {
        setGame(gameStore.game_id);
        setStore(gameStore.store_id);
        setValue(gameStore.value);
      })
      .catch(console.error);
  }, [match.params.id]);

  function onSubmit(e) {
    e.preventDefault();

    const id = match.params.id ? `/${match.params.id}` : '';
    const method = match.params.id ? 'put' : 'post';

    api[method](`/api/v1/game-store${id}`, {
      game_id: game,
      store_id: store,
      value
    })
      .then(() => {
        history.push('/admin/game-store');
        toast.info('Operation successfully performed.');
      })
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
            <option>Select a game</option>

            {games.map((it) => (
              <option key={it.id} value={it.id} selected={game === it.id}>
                {it.name}
              </option>
            ))}
          </Select>

          <Select onChange={(e) => setStore(e.target.value)}>
            <option>Select a store</option>

            {stores.map((it) => (
              <option key={it.id} value={it.id} selected={store === it.id}>
                {it.name}
              </option>
            ))}
          </Select>

          <Buttons>
            <Button type="submit">Save</Button>
            <Button type="button" danger>
              Delete
            </Button>
          </Buttons>
        </Form>
      </Content>
    </AdminTemplate>
  );
}
