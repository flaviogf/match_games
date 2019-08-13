import React, { useState, useEffect } from "react";

import { MdArrowDropDown, MdPerson, MdExitToApp } from "react-icons/md";

import { Container, Avatar, Menu, MenuItem } from "./styles";

export default function Navbar() {
  const [visible, setvisible] = useState(false);
  const [username, setUsername] = useState("");

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem("__user"));
    setUsername(user.name[0].toUpperCase());
  }, [username]);

  return (
    <Container>
      <h1>Match Games</h1>

      <Avatar onClick={() => setvisible(!visible)}>
        <MdArrowDropDown size="25px" />
        <span>{username}</span>
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
