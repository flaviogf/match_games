import React from "react";

import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import GlobalStyle from "./styles";

import Routes from "./routes";

toast.configure({});

export default function App() {
  return (
    <>
      <GlobalStyle />
      <Routes />
    </>
  );
}
