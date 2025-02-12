import React from 'react';
import './App.css';
import {Footer, Header, Main} from './components'
import styled from 'styled-components'

function App() {
    return (
        <SWrapper>
            <Header/>
            <Main/>
            <Footer/>
        </SWrapper>
    );
}

export default App;

const SWrapper = styled.div`
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
`;

// import React, {useState} from "react";
// import axios from "axios";
//
// interface Triple {
//     subject: string;
//     predicate: string;
//     object: string;
// }
//
// const App: React.FC = () => {
//     const [text, setText] = useState("");
//     const [triples, setTriples] = useState();
//     const [loading, setLoading] = useState(false);
//     const [error, setError] = useState("");
//
//     const handleExtractTriples = async () => {
//         setLoading(true);
//         setError("");
//
//         try {
//             const response = await axios.post("http://127.0.0.1:8000/extract_triples/", {
//                 text,
//             });
//
//             console.log(response.data);
//
//             setTriples(response.data);
//         } catch (err) {
//             setError("Error fetching triples.");
//         }
//
//         setLoading(false);
//     };
//
//     return (
//         <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
//             <h1 className="text-2xl font-bold mb-4">Disorder Triple Extractor</h1>
//             <textarea
//                 className="w-full max-w-2xl p-2 border rounded"
//                 rows={4}
//                 value={text}
//                 onChange={(e) => setText(e.target.value)}
//                 placeholder="Enter medical text..."
//             />
//             <button
//                 className="mt-3 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
//                 onClick={handleExtractTriples}
//                 disabled={loading}
//             >
//                 {loading ? "Extracting..." : "Extract Triples"}
//             </button>
//
//             {error && <p className="text-red-500 mt-2">{error}</p>}
//
//             {/*{triples.length > 0 && (*/}
//             {/*    <table className="mt-6 w-full max-w-3xl border border-gray-300">*/}
//             {/*        <thead>*/}
//             {/*        <tr className="bg-gray-200">*/}
//             {/*            <th className="border p-2">Subject</th>*/}
//             {/*            <th className="border p-2">Predicate</th>*/}
//             {/*            <th className="border p-2">Object</th>*/}
//             {/*        </tr>*/}
//             {/*        </thead>*/}
//             {/*        <tbody>*/}
//             {/*        {triples.map((triple, index) => (*/}
//             {/*            <tr key={index} className="bg-white border">*/}
//             {/*                <td className="border p-2">{triple.subject}</td>*/}
//             {/*                <td className="border p-2">{triple.predicate}</td>*/}
//             {/*                <td className="border p-2">{triple.object}</td>*/}
//             {/*            </tr>*/}
//             {/*        ))}*/}
//             {/*        </tbody>*/}
//             {/*    </table>*/}
//             {/*)}*/}
//             {triples}
//         </div>
//     );
// };
//
// export default App;