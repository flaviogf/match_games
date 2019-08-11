import styled from "styled-components";

export const Container = styled.aside`
  grid-area: menu;
  background-color: #243447;
  justify-content: center;
  align-items: center;
  display: none;

  @media (min-width: 768px) {
    display: flex;
  }
`;
