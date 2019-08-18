import styled from 'styled-components';

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const Content = styled.span`
  display: block;
  width: 55px;
  height: 55px;
  border-radius: 50%;
  border: 4px solid #71cafb;
  position: relative;
  border-left-color: #068dd6;
  animation: spin 1s linear infinite;
  visibility: ${(props) => (props.visible ? 'visible' : 'hidden')};

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
`;

export default Container;
