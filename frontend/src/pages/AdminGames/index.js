import React, { useEffect, useState } from "react";

import { Link } from "react-router-dom";

import { MdAdd } from "react-icons/md";

import AdminTemplate from "../../components/AdminTemplate";

import { Content, Card, Table, CardHeader } from "./styles";

import api from "../../services/api";

export default function AdminGames() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    function listGames() {
      api
        .get("/api/v1/games")
        .then(res => res.data)
        .then(body => setGames(body.data))
        .catch(console.error);
    }

    listGames();
  }, []);

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

          <Table>
            <thead>
              <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Image</th>
              </tr>
            </thead>
            <tbody>
              {games.map(game => (
                <tr key={game.id}>
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
