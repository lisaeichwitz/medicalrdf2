import styled from 'styled-components'
import {Prism as SyntaxHighlighter} from "react-syntax-highlighter";
import {dracula} from "react-syntax-highlighter/dist/esm/styles/prism";

interface FormattedResultProps {
    triples: string;
}

export const FormattedResult = ({triples}: FormattedResultProps) => {

    // const schemaRegex = /@prefix\s[a-z]*\:\s<https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)>\s./gm
    //
    // const extractSchemas = () => {
    //     return schemaRegex.exec(triples);
    // }
    //
    // console.log(extractSchemas());

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
