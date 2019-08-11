import React, { useState } from "react";

import { MdArrowDropDown, MdPerson, MdExitToApp } from "react-icons/md";

import { Container, Avatar, Menu, MenuItem } from "./styles";

export default function Navbar() {
  const [visible, setvisible] = useState(false);

  return (
    <Container>
      <h1>Match Games</h1>

      <Avatar onClick={() => setvisible(!visible)}>
        <MdArrowDropDown size="25px" />
        <span>F</span>
      </Avatar>

      <Menu visible={visible}>
        <MenuItem>
          <MdPerson />
          <span>Account</span>
        </MenuItem>

        <MenuItem>
          <MdExitToApp />
          <span>Logout</span>
        </MenuItem>
      </Menu>
    </Container>
  );
}
