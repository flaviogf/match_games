import React, { useState } from "react";

import { MdFileUpload } from "react-icons/md";

import Navbar from "../../components/Navbar";
import Menu from "../../components/Menu";
import Footer from "../../components/Footer";

import { Container, Content, Upload } from "./styles";

export default function AdminGame() {
  const [name, setName] = useState("");
  const [image, setImage] = useState("Select a image.");

  function onSubmit(e) {
    e.preventDefault();
  }

  return (
    <Container>
      <Navbar />
      <Menu />
      <Content>
        <form onSubmit={onSubmit}>
          <span>Game</span>

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
              onChange={e => setImage(e.target.value)}
            />
          </Upload>

          <button type="submit">Save</button>
        </form>
      </Content>

      <Footer />
    </Container>
  );
}
