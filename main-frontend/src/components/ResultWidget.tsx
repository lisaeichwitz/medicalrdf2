import styled from 'styled-components'

export const ResultWidget = () => {
    return (
        <SHeader>
            Hier werden dann RDF Tripel, Graph und Tabelle angezeigt.<br/>
            Button einfügen, um zwischen den verschiedenen Views zu wechseln.
        </SHeader>
    )
}

const SHeader = styled.div`
    display: flex;
    padding: 16px;
    background-color: #F1EDEE;
    flex: 2;
`;
