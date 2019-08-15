import styled from "styled-components";

export const Container = styled.div`
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
    cursor: pointer;
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
