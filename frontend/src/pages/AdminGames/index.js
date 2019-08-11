import React from "react";

import Navbar from "../../components/Navbar";
import Menu from "../../components/Menu";
import Footer from "../../components/Footer";

import { Container, Content, Card, Table } from "./styles";

export default function AdminGames() {
  return (
    <Container>
      <Navbar />
      <Menu />
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
              <tr>
                <td>1</td>
                <td>Pokemon Let's Go Eevee</td>
                <td>5cf34155f8ed4736.jpg</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Pokemon Let's Go Pikachu</td>
                <td>5cf34155f8ed4736.jpg</td>
              </tr>
            </tbody>
          </Table>
        </Card>
      </Content>
      <Footer />
    </Container>
  );
}
