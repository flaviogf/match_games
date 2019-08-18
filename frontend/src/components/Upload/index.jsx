import React from 'react';

import { MdFileUpload } from 'react-icons/md';

import { Container } from './styles';

export default function Upload({ image, onChange }) {
  return (
    <Container>
      <MdFileUpload size="125px" opacity="0.1" />
      <span>{image}</span>
      <input
        id="image"
        name="image"
        placeholder="Image"
        type="file"
        accept="image/*"
        onChange={onChange}
      />
    </Container>
  );
}
