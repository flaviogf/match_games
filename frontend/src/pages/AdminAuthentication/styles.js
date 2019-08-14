import styled from "styled-components";

import background from "../../assets/background.jpg";

export const Container = styled.main`
  justify-content: center;
  flex-direction: column;
  position: relative;
  padding: 16px;
  height: 100vh;
  display: flex;

  ::after {
    background-image: url(${background});
    background-size: cover;
    position: absolute;
    opacity: 0.1;
    content: "";
    z-index: -1;
    bottom: 0;
    right: 0;
    left: 0;
    top: 0;
  }

  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    display: grid;
    padding: 0;
  }
`;

export const Title = styled.h1`
  flex-direction: column;
  margin-bottom: 30px;
  text-align: center;
  font-size: 2.5rem;

  small {
    font-size: 1rem;
    display: none;
  }

  @media (min-width: 768px) {
    background-color: #141d26;
    justify-content: center;
    align-items: center;
    margin-bottom: 0;
    font-size: 4rem;
    display: flex;

    small {
      display: block;
    }
  }
`;

export const Form = styled.form`
  flex-direction: column;
  display: flex;

  span {
    font-size: 1.2rem;
  }

  input {
    background-color: #141e27;
    border: 1px solid #121213;
    border-radius: 2px;
    padding: 10px 8px;
    margin: 8px 0;
    height: 35px;
    color: white;

    :focus {
      box-shadow: 0 0 5px #6ebc3b;
      border: 1px solid #6ebc3b;
    }
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

  @media (min-width: 768px) {
    justify-content: center;
    max-width: 400px;
    margin: 0 auto;
    padding: 16px;
    width: 100%;
  }
`;
