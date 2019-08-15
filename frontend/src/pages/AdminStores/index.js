import React, { useState, useEffect } from "react";

import { Link } from "react-router-dom";

import { MdAdd } from "react-icons/md";

import AdminTemplate from "../../components/AdminTemplate";

import Card, { CardHeader } from "../../components/Card";
import Table from "../../components/Table";

import { Container } from "./styles";

import api from "../../services/api";

export default function AdminStores() {
  const [stores, setStores] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [hasPrevious, setHasPrevious] = useState(false);
  const [hasNext, setHasNext] = useState(false);

  useEffect(() => {
    function loadStores() {
      api
        .get(`/api/v1/stores?page=${currentPage}`)
        .then(res => {
          setHasPrevious(res.headers["has_previous"] === "True");
          setHasNext(res.headers["has_next"] === "True");
          return res;
        })
        .then(res => res.data.data)
        .then(setStores)
        .catch(console.log);
    }

    loadStores();
  }, [currentPage, hasPrevious, hasNext]);

  return (
    <AdminTemplate>
      <Container>
        <Card>
          <CardHeader>
            <h2>Stores</h2>

            <Link to="/admin/stores/create">
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
              {stores.map(store => (
                <tr key={store.id}>
                  <td>{store.id}</td>
                  <td>{store.name}</td>
                  <td>{store.image}</td>
                </tr>
              ))}
            </tbody>
          </Table>

          {hasPrevious && <span>Previous</span>}
          <span>{currentPage}</span>
          {hasNext && <span>Next</span>}
        </Card>
      </Container>
    </AdminTemplate>
  );
}
