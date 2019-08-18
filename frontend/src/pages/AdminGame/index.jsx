import React, { useState, useEffect } from 'react';

import { toast } from 'react-toastify';

import AdminTemplate from '../../components/AdminTemplate';
import Input from '../../components/Input';
import Upload from '../../components/Upload';

import { Content, Button, Buttons } from './styles';

import api from '../../services/api';

export default function AdminGame({ history, match }) {
  const [name, setName] = useState('');
  const [image, setImage] = useState('Select a image.');

  useEffect(() => {
    function loadGame() {
      if (!match.params.id) return;
      api
        .get(`/api/v1/games/${match.params.id}`)
        .then((res) => res.data.data)
        .then((data) => {
          setName(data.name);
          setImage(data.image);
        })
        .catch(console.error);
    }

    loadGame();
  }, [match.params.id]);

  function onSubmit(e) {
    e.preventDefault();

    const form = new FormData();

    form.append('name', name);
    form.append('image', e.target.image.files[0]);

    const method = match.params.id ? 'put' : 'post';
    const id = match.params.id ? `/${match.params.id}` : '';

    api[method](`/api/v1/games${id}`, form)
      .then(() => {
        toast.success('Operation successfully performed.');
        history.push('/admin/games');
      })
      .catch(console.error);
  }

  function destroy() {
    api
      .delete(`/api/v1/games/${match.params.id}`)
      .then(() => {
        toast.success('Operation successfully performed.');
        history.push('/admin/games');
      })
      .catch(console.error);
  }

  return (
    <AdminTemplate>
      <Content>
        <form onSubmit={onSubmit}>
          <h2>Game</h2>

          <Input
            id="name"
            name="name"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <Upload
            onChange={(e) =>
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
        </form>
      </Content>
    </AdminTemplate>
  );
}
