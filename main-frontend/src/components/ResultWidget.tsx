import styled from 'styled-components'
import {FormattedResult} from "./FormattedResult";

interface ResultWidgetProps {
    triples: string;
    error: string;
    loading: boolean;
}

export const ResultWidget = ({triples, error, loading}: ResultWidgetProps) => {
    console.log(triples.length);
    return (
        <SWrapper>
            <SHeader>
                Resultat
            </SHeader>
            <SMain>
                {triples.length > 120 ? <FormattedResult triples={triples}/> : triples.length === 120 ? <>Es konnten
                    keine
                    Tripel gefunden werden.</> : <></>}
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
