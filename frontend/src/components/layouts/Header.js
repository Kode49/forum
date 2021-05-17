import React from 'react';
import styled from 'styled-components';

const Header = () => {
  return (
    <MainContainer>
      Header
    </MainContainer>
  )
}

export default Header;

// Main contener
const MainContainer = styled.header`
background-color: green;
height: 5rem;

h1{
  transform: translate{-50%, -50%}
  color: #fff;
  font-weight: 900;
  position: absolute;
  top
}
`;