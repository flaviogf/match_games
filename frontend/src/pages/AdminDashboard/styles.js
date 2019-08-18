import styled from 'styled-components';

export const Container = styled.div`
  flex-direction: column;
  grid: content;
  display: flex;
  padding: 16px;

  @media (min-width: 768px) {
    flex-direction: row;
  }
`;

export const Stats = styled.div`
  background-image: ${(props) => props.color};
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  padding: 16px;
  height: 125px;
  color: white;
  flex-grow: 1;
  margin: 8px;

  h3 {
    text-transform: uppercase;
    font-size: 0.9rem;
  }

  span {
    font-size: 1.4rem;
    font-weight: bold;
  }

  img {
    position: absolute;
    bottom: 0;
    width: 100%;
  }
`;
