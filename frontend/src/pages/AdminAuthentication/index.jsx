import React, { useState, useEffect } from 'react';

import { Container, Title, Form } from './styles';

import Input from '../../components/Input';

import api from '../../services/api';

export default function AdminAuthentication({ history }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('__token');
    if (!token) return;
    history.push('/admin');
  }, [history]);

  function onSubmit(e) {
    e.preventDefault();

    api
      .post('/api/v1/authentication', {
        email,
        password
      })
      .then((res) => res.data.data)
      .then((data) => {
        localStorage.setItem('__user', JSON.stringify(data));
        localStorage.setItem('__token', `Bearer ${data.token}`);
        history.push('/admin');
      })
      .catch(console.error);
  }

  return (
    <Container>
      <Title>
        Welcome
        <small>Sign in to start.</small>
      </Title>

      <Form onSubmit={onSubmit}>
        <span>Login</span>

        <Input
          id="email"
          name="email"
          type="email"
          placeholder="E-mail"
          onChange={(e) => setEmail(e.target.value)}
          value={email}
        />

        <Input
          id="password"
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        />

        <button type="submit">Sign in</button>
      </Form>
    </Container>
  );
}
