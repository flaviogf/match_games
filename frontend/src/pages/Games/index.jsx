import React, { useEffect, useState } from 'react';

import { Container, GameCard } from './styles';

import api from '../../services/api';

export default function Games() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    function loadGames() {
      api
        .get('/api/v1/games')
        .then((res) => res.data.data)
        .then((data) => setGames(data))
        .catch(console.error);
    }

    loadGames();
  }, []);

  return (
    <Container>
      {games.map((game) => (
        <GameCard>
          <img src={game.image_path} alt="Game cover." />
          <h2>{game.name}</h2>
          <span>Por:</span>
          <span>
            <small>R$</small>
            199,99
          </span>
        </GameCard>
      ))}
    </Container>
  );
}
