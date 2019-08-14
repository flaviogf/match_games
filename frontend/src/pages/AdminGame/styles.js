import styled, { css } from "styled-components";

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

    input {
      background-color: #141e27;
      border: 1px solid #121213;
      border-radius: 2px;
      padding: 10px 8px;
      margin: 8px 0;
      height: 35px;
      color: white;
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
  width: 75px;

  ${props =>
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

  ${props =>
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

export const Upload = styled.div`
  border: 1px dashed #121213;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  position: relative;
  height: 180px;
  margin: 8px 0;
  display: flex;

  input {
    height: 100% !important;
    position: absolute;
    width: 100%;
    opacity: 0;
    left: 0;
    top: 0;
  }

  span {
    font-size: 1.5rem;
    opacity: 0.2;
    top: 120px;
  }
`;
