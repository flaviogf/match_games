import React, { useState } from "react";

import { Container, Title, Form } from "./styles";

import api from "../../services/api";

export default function AdminAuthentication({ history }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function onSubmit(e) {
    e.preventDefault();

    api
      .post("/api/v1/authentication", {
        email,
        password
      })
      .then(() => history.push("/admin/games"))
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

        <input
          id="email"
          name="email"
          type="email"
          placeholder="E-mail"
          onChange={e => setEmail(e.target.value)}
          value={email}
        />

        <input
          id="password"
          type="password"
          placeholder="Password"
          onChange={e => setPassword(e.target.value)}
          value={password}
        />

        <button type="submit">Sign in</button>
      </Form>
    </Container>
  );
}
