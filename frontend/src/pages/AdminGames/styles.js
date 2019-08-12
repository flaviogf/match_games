import styled from "styled-components";

export const Content = styled.section`
  grid-area: content;
  padding: 16px;
`;

export const Card = styled.div`
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.7);
  background-color: #1c2937;
  padding: 16px;

  h2 {
    margin-bottom: 16px;
    font-size: 2rem;
  }
`;

export const Table = styled.table`
  table-layout: fixed;
  width: 100%;

  thead {
    background-color: #1b3548;

    th {
      border: 1px solid #121213;
      text-align: center;
      cursor: pointer;
      padding: 8px;

      :hover {
        background-color: #91cf68;
        color: #323232;
      }
    }
  }

  tbody {
    tr {
      cursor: pointer;

      :nth-child(odd) {
        background-color: #15222f;
      }

      :nth-child(even) {
        background-color: #1c2937;
      }

      :hover {
        background-color: #91cf68;
        color: #323232;
      }
    }

    td {
      border: 1px solid #121213;
      white-space: nowrap;
      overflow-x: scroll;
      padding: 8px;

      @media (min-width: 768px) {
        overflow: hidden;
      }
    }
  }
`;
