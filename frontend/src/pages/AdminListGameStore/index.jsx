import React, { useState, useEffect } from 'react';

import { Link } from 'react-router-dom';

import { MdAdd } from 'react-icons/md';

import AdminTemplate from '../../components/AdminTemplate';

import { Card, CardHeader } from '../../components/Card';
import Table from '../../components/Table';
import Paginator from '../../components/Paginator';

import { Container } from './styles';

import api from '../../services/api';

export default function AdminListGameStore({ history }) {
  const [listGameStore, setListGameStore] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [hasPrevious, setHasPrevious] = useState(false);
  const [hasNext, setHasNext] = useState(false);

  useEffect(() => {
    function loadListGameStore() {
      api
        .get(`/api/v1/game-store?page=${currentPage}`)
        .then((res) => {
          setHasPrevious(res.headers.has_previous === 'True');
          setHasNext(res.headers.has_next === 'True');
          return res;
        })
        .then((res) => res.data.data)
        .then(setListGameStore)
        .catch(console.error);
    }

    loadListGameStore();
  }, [currentPage]);

  return (
    <AdminTemplate>
      <Container>
        <Card>
          <CardHeader>
            <h2>Game &gt; Store</h2>

            <Link to="/admin/game-store/create">
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
              {listGameStore.map((gameStore) => (
                <tr
                  key={gameStore.id}
                  onClick={() =>
                    history.push(`/admin/game-store/${gameStore.id}`)
                  }
                >
                  <td>{gameStore.game}</td>
                  <td>{gameStore.store}</td>
                  <td>{gameStore.value}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Card>
      </Container>
    </AdminTemplate>
  );
}
