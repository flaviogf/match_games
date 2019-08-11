import styled from "styled-components";

export const Container = styled.main`
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 50px 1fr 40px;
  grid-template-areas:
    "navbar"
    "content"
    "footer";

  @media (min-width: 768px) {
    grid-template-columns: 275px 1fr;
    grid-template-areas:
      "navbar navbar"
      "menu content"
      "menu footer";
  }
`;

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

    span {
      margin-bottom: 10px;
      font-size: 1.5rem;
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

    button {
      background-color: #6ebc3b;
      border-radius: 2px;
      padding: 8px;
      border: none;
      color: white;

      :hover {
        background-color: #528d2c;
      }

      :active {
        background-color: #365e1d;
      }
    }
  }
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
