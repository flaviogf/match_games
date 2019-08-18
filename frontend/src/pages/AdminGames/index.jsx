import React, { useEffect, useState } from 'react';

import { Link } from 'react-router-dom';

import { MdAdd } from 'react-icons/md';

import AdminTemplate from '../../components/AdminTemplate';
import Table from '../../components/Table';
import Card, { CardHeader } from '../../components/Card';
import Paginator from '../../components/Paginator';

import { Content } from './styles';

import api from '../../services/api';

export default function AdminGames({ history }) {
  const [games, setGames] = useState([]);
  const [hasPrevious, setHasPrevious] = useState(false);
  const [hasNext, setHasNext] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    function listGames() {
      api
        .get(`/api/v1/games?page=${currentPage}`)
        .then((res) => {
          setHasPrevious(res.headers['has_previous'] === 'True');
          setHasNext(res.headers['has_next'] === 'True');
          return res;
        })
        .then((res) => res.data)
        .then((body) => setGames(body.data))
        .catch(console.error);
    }

    listGames();
  }, [currentPage, hasPrevious, hasNext]);

  return (
    <AdminTemplate>
      <Content>
        <Card>
          <CardHeader>
            <h2>Games</h2>

            <Link to="/admin/games/create">
              <MdAdd size="24px" color="#d8d8d8" />
            </Link>
          </CardHeader>

          <Paginator
            hasPrevious={hasPrevious}
            onClickPrevious={() => setCurrentPage(currentPage - 1)}
            hasNext={hasNext}
            onClickNext={() => setCurrentPage(currentPage + 1)}
            currentPage={currentPage}
          />

          <Table>
            <thead>
              <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Image</th>
              </tr>
            </thead>
            <tbody>
              {games.map((game) => (
                <tr
                  key={game.id}
                  onClick={() => history.push(`/admin/games/${game.id}`)}
                >
                  <td>{game.id}</td>
                  <td>{game.name}</td>
                  <td>{game.image}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Card>
      </Content>
    </AdminTemplate>
  );
}
