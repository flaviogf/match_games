import styled from 'styled-components';

export const Container = styled.div`
  font-family: 'Roboto', sans-serif;
  background-color: #292929;
  min-height: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 350px;
  grid-gap: 10px;
  padding: 16px;

  @media (min-width: 768px) {
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: 410px;
  }
`;

export const GameCard = styled.div`
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: all 0.2s;
  padding: 8px;

  img {
    flex-grow: 1;
    display: block;
    height: auto;
    max-width: 150px;
    width: 100%;
    margin-bottom: 16px;
    border-radius: 5px;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
    background-color: #ccc;
    padding: 0.3em 0.3em 0.3em 0;
  }

  h2 {
    margin-bottom: 10px;
    text-transform: uppercase;
    font-weight: bold;
    font-size: 0.8rem;
    color: white;
  }

  span:nth-of-type(1) {
    margin-bottom: 10px;
    text-transform: uppercase;
    font-size: 0.7rem;
    font-weight: 100;
    color: #595959;
  }

  span:nth-of-type(2) {
    color: #068dd6;
    font-weight: bold;
    font-size: 1.8rem;

    small {
      text-transform: uppercase;
      font-size: 0.7rem;
    }
  }

  @media (min-width: 768px) {
    img {
      max-width: 180px;
    }

    h2 {
      font-size: 1rem;
    }
  }

  &:hover {
    transform: translateY(-2px);
  }
`;
