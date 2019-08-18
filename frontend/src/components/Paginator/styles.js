import styled from 'styled-components';

export const Container = styled.div`
  background-color: #243447;
  border: 1px solid #121213;
  border-bottom: none;
  justify-content: center;
  align-items: center;
  display: flex;
  height: 37px;

  span {
    justify-content: center;
    align-items: center;
    border-radius: 2px;
    user-select: none;
    cursor: pointer;
    margin: 0 2px;
    display: flex;
    height: 25px;
    padding: 2px;
    width: 25px;

    &[data-current] {
      background-color: #6ebc3b;
      font-weight: bold;
      color: white;
    }

    :hover {
      background-color: #b4df98;
      color: #323232;
    }
  }
`;
