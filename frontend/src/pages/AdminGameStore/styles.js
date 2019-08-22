import styled from 'styled-components';

export const Content = styled.div`
  grid-area: content;
  padding: 16px;
`;

export const Form = styled.form`
  box-shadow: 0 1px 4px rgb(0, 0, 0, 0.7);
  background-color: #1c2937;
  padding: 16px;
  display: flex;
  flex-direction: column;
`;

export const Title = styled.h1`
  font-size: 2rem;
  color: #d8d8d8;
`;

export const Select = styled.select`
  background-color: #141e27;
  border: 1px solid #121213;
  border-radius: 2px;
  padding: 6px 8px;
  cursor: pointer;
  margin: 8px 0;
  color: white;
`;

export const Button = styled.button`
  background-color: #6ebc3b;
  border: none;
  border-radius: 2px;
  cursor: pointer;
  color: white;
  padding: 8px;
  width: 75px;

  &:hover {
    background-color: #528d2c;
  }

  &:active {
    background-color: #365e1d;
  }
`;
