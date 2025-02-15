import styled from 'styled-components'
import {FormattedResult} from "./FormattedResult";

interface ResultWidgetProps {
    triples: string;
    error: string;
    loading: boolean;
}

export const ResultWidget = ({triples, error, loading}: ResultWidgetProps) => {
    return (
        <SWrapper>
            <SHeader>
                Hier werden dann RDF Tripel, Graph und Tabelle angezeigt.<br/>
                Button einfügen, um zwischen den verschiedenen Views zu wechseln.
            </SHeader>
            <SMain>
                {triples.length ? <FormattedResult triples={triples}/> : <></>}
            </SMain>
        </SWrapper>
    )
}
const SWrapper = styled.div`
    display: flex;
    flex-direction: column;
    flex: 2;
`;

const SHeader = styled.div`
    display: flex;
    padding: 16px;
    background-color: #F1EDEE;
`;

const SMain = styled.div`
    display: flex;
    padding: 16px;
    background-color: #F1EDEE;
    flex: 1;
`;
