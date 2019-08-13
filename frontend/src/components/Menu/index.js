import React from "react";

import { Link } from "react-router-dom";

import { Container, Title, MenuList, MenuItem, Footer } from "./styles";

export default function Menu() {
  return (
    <Container>
      <Title>Menu</Title>

      <MenuList>
        <MenuItem>
          <Link to="/admin">Dashboard</Link>
        </MenuItem>

        <MenuItem>
          <Link to="/admin/games">Games</Link>
        </MenuItem>

        <MenuItem>
          <Link to="/admin/stores">Stores</Link>
        </MenuItem>
      </MenuList>

      <Footer />
    </Container>
  );
}
