import React from 'react';

import { MdArrowBack, MdArrowForward } from 'react-icons/md';

import { Container } from './styles';

export default function Paginator({
  hasPrevious,
  onClickPrevious,
  hasNext,
  onClickNext,
  currentPage
}) {
  return (
    <Container>
      {hasPrevious ? (
        <span onClick={onClickPrevious}>
          <MdArrowBack />
        </span>
      ) : (
        <span>
          <MdArrowBack />
        </span>
      )}
      <span data-current>{currentPage}</span>
      {hasNext ? (
        <span onClick={onClickNext}>
          <MdArrowForward />
        </span>
      ) : (
        <span>
          <MdArrowForward />
        </span>
      )}
    </Container>
  );
}
