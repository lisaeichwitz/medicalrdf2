import styled from 'styled-components'

export const Input = () => {
    return (
        <SInput rows={40}/>
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