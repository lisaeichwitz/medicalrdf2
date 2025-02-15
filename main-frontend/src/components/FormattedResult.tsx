import styled from 'styled-components'
import {Prism as SyntaxHighlighter} from "react-syntax-highlighter";
import {dracula} from "react-syntax-highlighter/dist/esm/styles/prism";

interface FormattedResultProps {
    triples: string;
}

export const FormattedResult = ({triples}: FormattedResultProps) => {
    return (
        <SWrapper>
            <SyntaxHighlighter language="turtle" style={dracula}>
                {triples}
            </SyntaxHighlighter>
        </SWrapper>
    )
}
const SWrapper = styled.div`
    display: flex;
    flex-direction: column;
`;

const SMain = styled.div`
    display: flex;
    padding: 16px;
    background-color: #F1EDEE;
    flex: 2;
    flex-direction: row;
`;
