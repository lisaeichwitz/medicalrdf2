import styled from 'styled-components'
import {Input, Button} from './index'

interface InputWidgetProps {
    text: string;
    setText: (text: string) => void;
    onExtract: () => void;
}

export const InputWidget = ({text, setText, onExtract}: InputWidgetProps) => {
    return (
        <SHeader>
            <h2>Text eingeben</h2>
            <SInputArea>
                <Input value={text} setText={setText}/>
                <Button onClick={onExtract}>Text speichern</Button>
            </SInputArea>

            <SUploadArea>
                oder
                <Button>Datei hochladen</Button>
            </SUploadArea>
        </SHeader>
    )
}

const SHeader = styled.div`
    display: flex;
    padding: 32px;
    background-color: #F1EDEE;
    margin: 32px;
    border-radius: 8px;
    flex-direction: column;
    justify-content: space-between;
    flex: 1;
`;

const SInputArea = styled.div`
    display: flex;
    gap: 16px;
    flex-direction: column;
`;

const SUploadArea = styled.div`
    display: flex;
    gap: 16px;
    flex-direction: column;
    align-items: center;
`;

