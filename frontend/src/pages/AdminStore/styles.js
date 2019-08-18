import styled, { css } from 'styled-components';

export const Container = styled.div`
  grid: content;
  margin: 16px;
`;

export const Form = styled.form`
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.7);
  background-color: #1c2937;
  flex-direction: column;
  padding: 16px;
  display: flex;
`;

export const Buttons = styled.div`
  display: flex;
`;

export const Button = styled.button`
  border-radius: 2px;
  margin-right: 6px;
  padding: 8px;
  border: none;
  color: white;
  flex-grow: 1;

  @media (min-width: 768px) {
    flex-grow: unset;
    width: 75px;
  }

  :last-child {
    margin-right: 0px;
  }

  ${(props) =>
    props.success &&
    css`
      background-color: #6ebc3b;

      :hover {
        background-color: #528d2c;
      }

      :active {
        background-color: #365e1d;
      }
    `}

  ${(props) =>
    props.danger &&
    css`
      background-color: #ef5350;

      :hover {
        background-color: #db1714;
      }

      :active {
        background-color: #920f0d;
      }
    `}
`;
