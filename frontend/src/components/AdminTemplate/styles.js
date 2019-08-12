import styled from "styled-components";

export const Container = styled.main`
  display: grid;
  height: 100vh;
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
