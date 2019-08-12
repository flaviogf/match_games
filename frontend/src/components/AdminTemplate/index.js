import React from "react";

import Navbar from "../Navbar";
import Menu from "../Menu";
import Footer from "../Footer";

import { Container } from "./styles";

export default function AdminTemplate(props) {
  return (
    <Container>
      <Navbar />
      <Menu />
      {props.children}
      <Footer />
    </Container>
  );
}
