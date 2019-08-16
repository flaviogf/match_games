import React, { useState, useEffect } from "react";

import { toast } from "react-toastify";

import AdminTemplate from "../../components/AdminTemplate";
import Input from "../../components/Input";
import Upload from "../../components/Upload";

import { Container, Form, Button, Buttons } from "./styles";

import api from "../../services/api";

export default function AdminStore({ match, history }) {
  const [name, setName] = useState("");
  const [image, setImage] = useState("Select a image.");

  useEffect(() => {
    function loadStore() {
      if (!match.params.id) return;
      api
        .get(`/api/v1/stores/${match.params.id}`)
        .then(res => res.data.data)
        .then(store => {
          setName(store.name);
          setImage(store.image);
        });
    }

    loadStore();
  }, [match.params.id]);

  function onSubmit(e) {
    e.preventDefault();

    const form = new FormData();
    form.append("name", name);
    form.append("image", e.target.image.files[0]);

    const id = match.params.id ? `/${match.params.id}` : "";
    const method = match.params.id ? "put" : "post";

    api[method](`/api/v1/stores${id}`, form)
      .then(() => {
        history.push("/admin/stores");
        toast.info("Operation successfully performed.");
      })
      .catch(console.error);
  }

  function destroy(e) {
    e.preventDefault();

    api
      .delete(`/api/v1/stores/${match.params.id}`)
      .then(() => {
        history.push("/admin/stores");
        toast.info("Operation successfully performed.");
      })
      .then(console.error);
  }

  return (
    <AdminTemplate>
      <Container>
        <Form onSubmit={onSubmit}>
          <Input
            type="text"
            placeholder="Name"
            value={name}
            onChange={e => setName(e.target.value)}
          />

          <Upload
            onChange={e =>
              e.target.files.length && setImage(e.target.files[0].name)
            }
            image={image}
          />

          <Buttons>
            <Button type="submit" success>
              Save
            </Button>

            {match.params.id && (
              <Button type="button" danger onClick={destroy}>
                Delete
              </Button>
            )}
          </Buttons>
        </Form>
      </Container>
    </AdminTemplate>
  );
}
