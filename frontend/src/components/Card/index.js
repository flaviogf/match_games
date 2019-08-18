import styled from 'styled-components';

export const Card = styled.div`
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.7);
  background-color: #1c2937;
  padding: 16px;
`;

export const CardHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;

  h2 {
    margin-bottom: 16px;
    font-size: 2rem;
  }
`;

export default Card;
