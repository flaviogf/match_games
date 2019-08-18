import React, { useState, useEffect } from 'react';

import { withRouter, Link } from 'react-router-dom';

import { MdArrowDropDown, MdExitToApp, MdWeb } from 'react-icons/md';

import { Container, Avatar, Menu, MenuItem } from './styles';

function Navbar({ history }) {
  const [visible, setvisible] = useState(false);
  const [username, setUsername] = useState('');

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem('__user'));
    if (!user) return;
    setUsername(user.name[0].toUpperCase());
  }, []);

  function logout() {
    localStorage.clear();
    history.push('/admin/authentication');
  }

  return (
    <Container>
      <Link to="/admin">
        <h1>Match Games</h1>
      </Link>

      <Avatar onClick={() => setvisible(!visible)}>
        <MdArrowDropDown size="25px" />
        <span>{username}</span>
      </Avatar>

      <Menu visible={visible}>
        <Link to="/">
          <MenuItem>
            <MdWeb />
            <span>Website</span>
          </MenuItem>
        </Link>

        <MenuItem onClick={logout}>
          <MdExitToApp />
          <span>Logout</span>
        </MenuItem>
      </Menu>
    </Container>
  );
}

export default withRouter(Navbar);
