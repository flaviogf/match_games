import React, { useState } from "react";

import AdminTemplate from "../../components/AdminTemplate";
import Input from "../../components/Input";
import Upload from "../../components/Upload";

import { Container, Form, Button, Buttons } from "./styles";

export default function AdminStore({ match }) {
  const [image, setImage] = useState("Select a image.");

  function onSubmit(e) {
    e.preventDefault();

    console.log("Save");
  }

  function destroy(e) {
    e.preventDefault();

    console.log("Destroy");
  }

  return (
    <AdminTemplate>
      <Container>
        <Form onSubmit={onSubmit}>
          <Input type="text" placeholder="Name" />

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
