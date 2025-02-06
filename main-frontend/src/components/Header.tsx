import styled from 'styled-components'

export const Header = () => {
    return (
        <SHeader>
            Automatische Erstellung einer Wissensrepräsentation in RDF aus
            einem medizinischen Text mittels eines NLP-Frameworks
        </SHeader>
    )
}

const SHeader = styled.header`
    display: flex;
    padding: 16px;
    background-color: #4D5382;
    color: #fff;
`;

