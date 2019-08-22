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
  margin-bottom: 8px;
  font-size: 2rem;
  color: #d8d8d8;
`;

export const Select = styled.select`
  background-color: #141e27;
  border: 1px solid #121213;
  border-radius: 2px;
  padding: 10px 8px;
  cursor: pointer;
  margin: 8px 0;
  color: white;
`;

export const Buttons = styled.div`
  display: flex;
`;

export const Button = styled.button`
  background-color: ${(props) => (props.danger ? '#EF5350' : '#6ebc3b')};
  border-radius: 2px;
  margin-right: 5px;
  cursor: pointer;
  border: none;
  color: white;
  padding: 8px;
  flex-grow: 1;

  &:hover {
    background-color: ${(props) => (props.danger ? '#db1714' : '#528d2c')};
  }

  &:active {
    background-color: ${(props) => (props.danger ? '#920f0d' : '#365e1d')};
  }

  @media (min-width: 768px) {
    max-width: 75px;
  }
`;
