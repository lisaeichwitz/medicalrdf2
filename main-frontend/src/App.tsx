import React from 'react';
import './App.css';
import {Footer, Header, Main} from './components'
import styled from 'styled-components'

function App() {
    return (
        <SWrapper>
            <Header/>
            <Main/>
            <Footer/>
        </SWrapper>
    );
}

export default App;

const SWrapper = styled.div`
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
`;