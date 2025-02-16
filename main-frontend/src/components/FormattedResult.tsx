import styled from 'styled-components'
import {Prism as SyntaxHighlighter} from "react-syntax-highlighter";
import {dracula} from "react-syntax-highlighter/dist/esm/styles/prism";

interface FormattedResultProps {
    triples: string;
}

export const FormattedResult = ({triples}: FormattedResultProps) => {
    return (
        <SWrapper>
            <SyntaxHighlighter language="xml" style={dracula}
                               lineProps={{style: {wordBreak: 'break-all', whiteSpace: 'pre-wrap'}}}
                               wrapLines={true}>
                {triples}
            </SyntaxHighlighter>
        </SWrapper>
    )
}
const SWrapper = styled.div`
    display: flex;
    flex-direction: column;
`;