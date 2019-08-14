import { createGlobalStyle } from "styled-components";

export default createGlobalStyle`
    @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600,700&display=swap');
    @import url('https://fonts.googleapis.com/css?family=Oswald:400,700&display=swap');
    
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
        overflow-x: hidden;
        color: #d8d8d8;
    }

    button {
        cursor: pointer;
    }

    .Toastify__toast--success {
        background-color: #39A3F4;
    }

    .Toastify__toast--error {
        background-color: #EF5350;
    }
`;
