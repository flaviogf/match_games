import React, { useEffect, useState } from 'react';

import { Container, GameCard } from './styles';

import Loader from '../../components/Loader';

import api from '../../services/api';

export default function Games() {
  const [currentPage, setCurrentPage] = useState(1);
  const [hasNext, setHasNext] = useState(false);
  const [games, setGames] = useState([]);

  useEffect(() => {
    function loadGames() {
      api
        .get(`/api/v1/games?page=${currentPage}`)
        .then((res) => {
          setHasNext(res.headers.has_next === 'True');
          return res;
        })
        .then((res) => res.data.data)
        .then((data) => setGames([...games, ...data]))
        .catch(console.error);
    }

    loadGames();
  }, [currentPage]);

  return (
    <Container>
      {games.map((game) => (
        <GameCard key={game.id}>
          <img src={game.image_path} alt="Game cover." />
          <h2>{game.name}</h2>
          <span>Por:</span>
          <span>
            <small>R$</small>
            199,99
          </span>
        </GameCard>
      ))}
      <Loader onHit={() => hasNext && setCurrentPage(currentPage + 1)} />
    </Container>
  );
}
