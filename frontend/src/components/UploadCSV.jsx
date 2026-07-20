import { useState } from "react";
import API from "../services/api";

function UploadCSV({ setData }) {

    const [file, setFile] = useState(null);

    const uploadFile = async () => {

        if (!file) return;

        const formData = new FormData();

        formData.append("file", file);

        const response = await API.post("/upload", formData);

        setData(response.data);

        alert("CSV Uploaded Successfully");

    };

    return (

        <div>

            <input
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <button onClick={uploadFile}>
                Upload
            </button>

        </div>

    );

}

export default UploadCSV;