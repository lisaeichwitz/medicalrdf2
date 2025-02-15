import styled from 'styled-components'

interface ButtonProps {
    children: string;
    disabled: boolean;
    onClick?: () => void;
}

export const Button = ({children, onClick, disabled}: ButtonProps) => {
    return (
        <SButton onClick={onClick} disabled={disabled}>{children}</SButton>
    )
}

const SButton = styled.button<{ disabled: boolean }>`
    background-color: ${({disabled}) => disabled ? '#ebebeb' : '#4D5382'};
    border: none;
    height: 32px;
    border-radius: 4px;
    color: #fff;
    cursor: ${({disabled}) => disabled ? 'not-allowed' : 'pointer'};
`;