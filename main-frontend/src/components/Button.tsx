import styled from 'styled-components'

interface ButtonProps {
    children: string;
    onClick?: () => void;
}

export const Button = ({children, onClick}: ButtonProps) => {
    return (
        <SButton onClick={onClick}>{children}</SButton>
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