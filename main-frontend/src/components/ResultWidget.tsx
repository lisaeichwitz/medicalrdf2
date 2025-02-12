import styled from 'styled-components'

interface ResultWidgetProps {
    triples: string;
    error: boolean;
    loading: boolean;
}

export const ResultWidget = ({triples, error, loading}: ResultWidgetProps) => {
    return (
        <SHeader>
            Hier werden dann RDF Tripel, Graph und Tabelle angezeigt.<br/>
            Button einfügen, um zwischen den verschiedenen Views zu wechseln.
            {triples}
        </SHeader>
    )
}

const SHeader = styled.div`
    display: flex;
    padding: 16px;
    background-color: #F1EDEE;
    flex: 2;
`;
