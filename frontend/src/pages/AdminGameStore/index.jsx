import React from 'react';

import AdminTemplate from '../../components/AdminTemplate';

import { Content, Form, Title, Select, Button } from './styles';

export default function AdminGameStore() {
  function onSubmit(e) {
    e.preventDefault();
  }

  return (
    <AdminTemplate>
      <Content>
        <Form onSubmit={onSubmit}>
          <Title>Game &gt; Store</Title>

          <Select>
            <option>Crash</option>
            <option>Fifa 19</option>
          </Select>
          <Select>
            <option>Shop B</option>
            <option>Big Boy</option>
          </Select>

          <Button>Salvar</Button>
        </Form>
      </Content>
    </AdminTemplate>
  );
}
