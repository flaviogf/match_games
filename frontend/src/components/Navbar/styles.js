import styled from 'styled-components';

export const Container = styled.nav`
  grid-area: navbar;
  justify-content: space-between;
  background-color: #6ebc3b;
  align-items: center;
  position: relative;
  padding: 0 16px;
  display: flex;
  color: white;
  z-index: 20;

  a {
    text-decoration: none;
    color: inherit;
  }

  h1 {
    font-family: 'Oswald', sans-serif;
    text-transform: uppercase;
    font-size: 1.5rem;
  }
`;

export const Avatar = styled.div`
  align-items: center;
  user-select: none;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  z-index: 20;

  span {
    border: 1px solid rgba(0, 0, 0, 0.1);
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    display: flex;
    height: 40px;
    width: 40px;
  }
`;

export const Menu = styled.ul`
  transform: ${(props) =>
    props.visible ? 'translateY(0px);' : 'translateY(-30px);'};
  opacity: ${(props) => (props.visible ? '1' : '0')};
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  background-color: #6ebc3b;
  transition: all 0.2s;
  position: absolute;
  padding: 8px;
  width: 175px;
  z-index: 10;
  top: 50px;
  right: 0;
`;

export const MenuItem = styled.li`
  align-items: center;
  padding: 5px 8px;
  cursor: pointer;
  display: flex;
  color: white;

  span {
    margin-left: 8px;
  }
`;
