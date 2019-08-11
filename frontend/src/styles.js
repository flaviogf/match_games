import { createGlobalStyle } from "styled-components";

export default createGlobalStyle`
    @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600,700&display=swap');

    * {
        box-sizing: border-box;
        outline: none;
    }

    html,
    body,
    #root {
        height: 100vh;
    }

    body {
        font-family: 'Source Sans Pro', sans-serif;
        -webkit-font-smoothing: antialiased;
        background-color: #141d26;
        color: #d8d8d8;
    }

    button {
        cursor: pointer;
    }
`;
