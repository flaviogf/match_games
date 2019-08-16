import styled from "styled-components";

export default styled.table`
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
      overflow-x: auto;
      padding: 8px;

      @media (min-width: 768px) {
        overflow: hidden;
      }
    }
  }
`;
