import styled from 'styled-components'

export const Input = ({value, setText}) => {
    return (
        <SInput rows={40} value={value} onChange={(ev) => setText(ev.target.value)}/>
    )
}

const SInput = styled.textarea`
    resize: none;
    display: flex;
    flex: 1;
    border: 2px solid #4D5382;
    border-radius: 4px;
    align-items: baseline;
    appearance: unset;
    padding: 8px;
`;