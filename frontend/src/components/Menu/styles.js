import styled from "styled-components";

export const Container = styled.aside`
  background-color: #243447;
  grid-area: menu;
  color: #acacac;
  display: none;

  @media (min-width: 768px) {
    flex-direction: column;
    display: flex;
  }
`;

export const Title = styled.h1`
  border-bottom: 1px solid rgba(0, 0, 0, 0.7);
  text-transform: uppercase;
  letter-spacing: 0.1rem;
  padding: 12px 16px;
`;

export const MenuList = styled.ul`
  flex-direction: column;
  flex-grow: 1;
  display: flex;
`;

export const MenuItem = styled.li`
  cursor: pointer;
  color: ${props => (props.active ? "#6ebc3b" : "inherit")};

  a {
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    color: inherit;
  }

  :hover {
    background-color: #6ebc3b;
    color: white;
  }
`;

export const Footer = styled.div`
  border-top: 1px solid rgba(0, 0, 0, 0.7);
  height: 41px;
`;
