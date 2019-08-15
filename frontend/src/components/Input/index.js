import styled from "styled-components";

export default styled.input`
  background-color: #141e27;
  border: 1px solid #121213;
  transition: all 0.2s;
  border-radius: 2px;
  padding: 10px 8px;
  margin: 8px 0;
  height: 35px;
  color: white;

  :focus {
    border: 1px solid #6ebc3b;
    box-shadow: 0 0 5px #6ebc3b;
  }
`;
