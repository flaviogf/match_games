import React, { useState } from "react";

import { MdFileUpload } from "react-icons/md";

import AdminTemplate from "../../components/AdminTemplate";

import { Content, Upload } from "./styles";

import api from "../../services/api";

export default function AdminGame({ history }) {
  const [name, setName] = useState("");
  const [image, setImage] = useState("Select a image.");

  function onSubmit(e) {
    e.preventDefault();

    const form = new FormData();

    form.append("name", name);
    form.append("image", e.target.image.files[0]);

    api
      .post("/api/v1/games", form)
      .then(() => history.push("/admin/games"))
      .catch(console.error);
  }

  return (
    <AdminTemplate>
      <Content>
        <form onSubmit={onSubmit}>
          <h2>Game</h2>

          <input
            id="name"
            name="name"
            placeholder="Name"
            value={name}
            onChange={e => setName(e.target.value)}
          />

          <Upload>
            <MdFileUpload size="125px" opacity="0.1" />
            <span>{image}</span>
            <input
              id="image"
              name="image"
              placeholder="Image"
              type="file"
              accept="image/*"
              onChange={e =>
                e.target.files.length && setImage(e.target.files[0].name)
              }
            />
          </Upload>

          <button type="submit">Save</button>
        </form>
      </Content>
    </AdminTemplate>
  );
}
