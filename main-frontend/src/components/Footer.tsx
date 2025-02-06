import styled from 'styled-components'

export const Footer = () => {
    return (
        <SFooter>
            © Lisa Eichwitz | FernUniversität in Hagen | {new Date().getFullYear().toString()}
        </SFooter>
    )
}

const SFooter = styled.footer`
    display: flex;
    padding: 16px;
    font-size: 12px;
    justify-content: center;
    background-color: #4D5382;
    color: #fff;
`;