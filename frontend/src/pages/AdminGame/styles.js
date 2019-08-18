import styled, { css } from 'styled-components';

export const Content = styled.section`
  grid-area: content;
  padding: 16px;

  form {
    box-shadow: 0px 2px 4px 1px rgba(0, 0, 0, 0.3);
    background-color: #1c2937;
    flex-direction: column;
    border-radius: 2px;
    display: flex;
    padding: 16px;

    h2 {
      margin-bottom: 16px;
      font-size: 2rem;
    }
  }
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
