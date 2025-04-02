import axios from "axios";

const getFileUrl = async (file) => {
    if (!file) {
        throw new Error("Please provide a valid file!");
    }

    try {
        // Step 1: Get SAS token from Azure Function
        const sasResponse = await axios.get(`https://arethosapi.azurewebsites.net/api/sasurl?code=RKzCvpXOxUzBMrMsKUZ-eWX9sEWYPZapm303XQF7DNa7AzFu3gGPSQ==&filename=${file.name}`);
        
        console.log("SAS Response:", sasResponse.data); // Debugging line
        
        const sasUrl = sasResponse.data.blob_url;
        if (!sasUrl) {
            throw new Error("SAS URL is undefined. Check Azure Function response.");
        }

        // Step 2: Upload file directly to Azure Blob Storage using the SAS URL
        await axios.put(sasUrl, file, {
            headers: {
                "x-ms-blob-type": "BlockBlob",
                "Content-Type": file.type,
            },
        });

        console.log("File uploaded successfully:", sasUrl);
        return sasUrl;
    } catch (error) {
        console.error("Upload error:", error);
        throw new Error("Upload failed. Please try again.");
    }
};



export default getFileUrl;