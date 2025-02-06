import styled from 'styled-components'

interface ButtonProps {
    children: string;
}

export const Button = ({children}: ButtonProps) => {
    return (
        <SButton>{children}</SButton>
    )
}

const SButton = styled.button`
    background-color: #4D5382;
    border: none;
    height: 32px;
    border-radius: 4px;
    color: #fff;
    cursor: pointer;
`;