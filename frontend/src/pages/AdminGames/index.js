import React, { useEffect, useState } from "react";

import AdminTemplate from "../../components/AdminTemplate";

import { Content, Card, Table } from "./styles";

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
          <h2>Games</h2>

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
