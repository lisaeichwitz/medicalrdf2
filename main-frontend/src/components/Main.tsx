import styled from 'styled-components'
import {InputWidget, ResultWidget} from "./index";

export const Main = () => {
    return (
        <SMain>
            <InputWidget></InputWidget>
            <ResultWidget></ResultWidget>
        </SMain>
    )
}

const SMain = styled.main`
    display: flex;
    flex: 1;
    overflow: hidden;
    background-color: #8AA29E;
    gap: 32px;
`;