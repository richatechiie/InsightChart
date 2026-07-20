import { useState } from "react";
import UploadCSV from "./components/UploadCSV";

function App() {

    const [data, setData] = useState(null);

    return (

        <div>

            <h1>CSV Analytics Dashboard</h1>

            <UploadCSV setData={setData}/>

            {data && (

                <div>

                    <h2>Rows</h2>

                    <p>{data.rows}</p>

                    <h2>Columns</h2>

                    <pre>

                        {JSON.stringify(data.columns,null,2)}

                    </pre>

                </div>

            )}

        </div>

    );

}

export default App;