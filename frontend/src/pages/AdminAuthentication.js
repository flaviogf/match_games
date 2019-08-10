import React, { useState } from "react";
import { MdPerson } from "react-icons/md";

import "./AdminAuthentication.css";

import api from "../services/api";

export default function AdminAuthentication({ history }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function onSubmit(e) {
    e.preventDefault();

    api
      .post("/api/v1/admin/authentication", {
        email,
        password
      })
      .then(() => history.push("/"))
      .catch(console.error);
  }

  return (
    <main className="admin-authentication__container">
      <form onSubmit={onSubmit}>
        <header>
          <MdPerson />
        </header>

        <div>
          <label htmlFor="email">E-mail</label>
          <input
            id="email"
            name="email"
            type="email"
            placeholder="E-mail"
            onChange={e => setEmail(e.target.value)}
            value={email}
          />
        </div>

        <div>
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            placeholder="Password"
            onChange={e => setPassword(e.target.value)}
            value={password}
          />
        </div>

        <div>
          <button type="submit">Sign In</button>
        </div>
      </form>
    </main>
  );
}
