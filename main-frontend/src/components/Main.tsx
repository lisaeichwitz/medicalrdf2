import styled from 'styled-components'
import {InputWidget, ResultWidget} from "./index";
import {useState} from "react";
import axios from "axios";

export const Main = () => {
    const [text, setText] = useState("");
    const [triples, setTriples] = useState<string>('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string>("");

    const handleExtractTriples = async () => {
        setLoading(true);
        setError("");

        try {
            const response = await axios.post("http://127.0.0.1:8000/extract_triples/", {
                text,
            });

            console.log(response.data);

            setTriples(response.data);
        } catch (err) {
            setError("Error fetching triples.");
        }

        setLoading(false);
    };


    return (
        <SMain>
            <InputWidget text={text} setText={setText} onExtract={handleExtractTriples}></InputWidget>
            <ResultWidget triples={triples} error={error} loading={loading}></ResultWidget>
        </SMain>
    )
}

const SMain = styled.main`
    display: flex;
    flex: 1;
    overflow: hidden;
    background-color: #8AA29E;
    gap: 32px;
`;