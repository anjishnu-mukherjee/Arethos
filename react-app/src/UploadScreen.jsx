import React from "react";
import { useState } from "react";
import getFileUrl from "./BlobStorage"




const UploadScreen=( )=>{//{handleQuestionFileChange, questionFile ,handleAnswerFileChange , answerFile, handleUpload})=>{
  const [questionFile, setQuestionFile] = useState(null);
  const [answerFile, setAnswerFile] = useState(null);
  const [questionFileUploaded, setQuestionUploadState] = useState(false);
  const [answerFileUploaded, setAnswerUploadState] = useState(false);
  const [questionFileUrl, setQuestionFileUrl] = useState(null);
  const [answerFileUrl, setAnswerFileUrl] = useState(null);
  const [showHelp, setShowHelp] = useState(true);
  const [responseData, setResponseData] = useState(null);
  const [isLoading, setLoadingState] = useState(-1);


  const handleQuestionFileChange = async (event) => {
    setQuestionUploadState(true)
    const selectedFile = event.target.files[0]; // Get the File object
    if (!selectedFile){
      setQuestionUploadState(false)
      return;
    }
    setQuestionFile(selectedFile); // Store file in state if needed
    try {
        const uploadedFileUrl = await getFileUrl(selectedFile); // Upload the file
        setQuestionFileUrl(uploadedFileUrl)
        console.log("File uploaded successfully. URL:", uploadedFileUrl);
    } catch (error) {
        console.error("File upload failed:", error);
    }
    finally{
    // if (questionFileUrl!=null) {
    setQuestionUploadState(false); // Always runs after try/catch
    // }
  }
    
  };
  const handleAnswerFileChange = async (event) => {
    setAnswerUploadState(true)
    const selectedFile = event.target.files[0]; // Get the File object
    if (!selectedFile) return;
    setAnswerUploadState(false)
    setAnswerFile(selectedFile); // Store file in state if needed

    try {
        const uploadedFileUrl = await getFileUrl(selectedFile); // Upload the file
        setAnswerFileUrl(uploadedFileUrl)
        console.log("File uploaded successfully. URL:", uploadedFileUrl);
    } catch (error) {
        console.error("File upload failed:", error);
    }
    if(answerFileUrl) {
      setAnswerUploadState(false)
    }
    
  };


const handleUpload = () => {
    if (!questionFile || !answerFile) {
        alert("Please upload both files.");
        return;
    }
    if (!questionFileUrl || !answerFileUrl) {
        alert("Couldn't Generate SAS link. Please Try again. Uploads hold a cold start wait till the file is properly uploaded");
        return;
    }

    setLoadingState(0); // Start loading
// https://arethosapi.azurewebsites.net/api/geminiresponse?code=RKzCvpXOxUzBMrMsKUZ-eWX9sEWYPZapm303XQF7DNa7AzFu3gGPSQ==
    fetch("https://arethosapi.azurewebsites.net/api/geminiresponse?code=RKzCvpXOxUzBMrMsKUZ-eWX9sEWYPZapm303XQF7DNa7AzFu3gGPSQ==", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ questions: questionFileUrl, answers: answerFileUrl })
    })
    .then(response => {
        console.log("Response Status:", response.status);
        if (!response.ok) throw new Error("Network response was not ok");
        return response.json();
    })
    .then(data => {
      if (data && data.length > 0) {
        const extractedData = data[0].qa_pairs.map((qa) => ({
          question: qa.question,
          answer: qa.answer,
          feedback: qa.feedback,
          score: qa.score,
        }));
        
          setResponseData(extractedData);
          console.log(extractedData);
        }
        setLoadingState(1); // Success
        console.log("Recived Response");
    })
    .catch(error => {
        setLoadingState(-1); // Error
        console.error("Error calling API:", error);
    });
};

const isUploading = questionFileUploaded || answerFileUploaded;
    return (
      <div className="flex flex-col">
        <div className="flex flex-col">
            <div className="absolute left-20 top-1/4 flex flex-col">
            <label
          className={`flex items-center text-[#EFFBF0] text-base py-3 px-12 rounded-full transition duration-500 ease-in-out 
          bg-[#6BDB76]/20 backdrop-blur-md select-none 
          ${isUploading ? 'opacity-50 pointer-events-none' : 'hover:bg-[#6BDB76]/40 active:text-[#6BDB76] cursor-pointer'}`}>
          
          {questionFileUploaded ? (
            <span className="animate-spin material-symbols-outlined text-5xl">progress_activity</span>
          ) : questionFile ? (
            <span className="material-symbols-outlined text-5xl">remove</span>
          ) : (
            <span className="material-symbols-outlined text-5xl">add</span>
          )}

          &nbsp;
          {questionFile ? questionFile.name : "ADD QUESTION PAPER"}

          <input 
            type="file" 
            accept=".txt,.png,.jpeg,.jpg,.pdf"
            onChange={handleQuestionFileChange} 
            className="hidden" 
          />
        </label>

        <div className="h-7"></div>

        {/* Answer File Upload */}
        <label
          className={`flex items-center text-[#EFFBF0] text-base py-3 px-14 rounded-full transition duration-500 ease-in-out 
          bg-[#6BDB76]/20 backdrop-blur-md select-none 
          ${isUploading ? 'opacity-50 pointer-events-none' : 'hover:bg-[#6BDB76]/40 active:text-[#6BDB76] cursor-pointer'}`}>

          {answerFileUploaded ? (
            <span className="animate-spin material-symbols-outlined text-5xl">progress_activity</span>
          ) : answerFile ? (
            <span className="material-symbols-outlined text-5xl">remove</span>
          ) : (
            <span className="material-symbols-outlined text-5xl">add</span>
          )}

          &nbsp;
          {answerFile ? answerFile.name : "ADD ANSWER SHEET"}

          <input 
            type="file" 
            accept=".txt,.png,.jpeg,.jpg,.pdf"
            onChange={handleAnswerFileChange} 
            className="hidden" 
          />
        </label>
            </div>
            <button 
  onClick={handleUpload}
  disabled={!answerFileUrl || !questionFileUrl}
  className={`absolute left-20 bottom-1/4 flex items-center text-[#EFFBF0] text-base py-3 px-20 rounded-full 
  transition duration-500 ease-in-out bg-[#6BDB76]/20 backdrop-blur-md
  ${!answerFileUrl || !questionFileUrl ? 'opacity-50 pointer-events-none' : 'hover:bg-[#6BDB76]/40 active:text-[#6BDB76] cursor-pointer'}`}>
  
  {
    (!answerFileUrl || !questionFileUrl)
    ? (
      <div className="flex items-center gap-2">
        <span className="animate-spin material-symbols-outlined text-5xl">progress_activity</span>
        Waiting For Files...
      </div>
    )
    : (
      <>
        EVALUATE&nbsp;
        <span className="material-symbols-outlined text-5xl">trending_flat</span>
      </>
    )
  }

</button>
            { isLoading===-1 &&
            <HelpSection showHelp={showHelp} setShowHelp={setShowHelp} />
          }
        </div>
        <div className="absolute right-20 top-1/2 transform -translate-y-1/2 max-h-[85vh] space-y-8 p-4">
        {isLoading===0&&
        <div className="flex justify-center items-center h-40">
        <div className="w-40 h-40 border-4 border-t-transparent border-[#6BDB76]/70 rounded-full animate-spin"></div>
        </div>
        }
        </div>
        <div className="absolute right-5 top-1/2 transform -translate-y-1/2 max-h-[85vh] overflow-y-auto space-y-8 p-4">
        {isLoading===1 && responseData && responseData.length > 0 && 
          responseData.map((qa, index) => (
            <ResponseSecion 
              key={index} 
              question={qa.question} 
              answer={qa.answer}
              feedback={qa.feedback}
              score={qa.score}
            />
          ))
        }
        </div>
      </div>
    );
};

const HelpSection = ({showHelp,setShowHelp})=>{
  return(
    <>
    <div className="absolute right-0 top-0 text-[#ADEBB3]/30">
            <button 
            onClick={() => setShowHelp(!showHelp)}
            className="fixed top-6 right-8 flex items-center text-[#ADEBB3] hover:underline transition">
              Help
             </button>
             {showHelp ? (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="1000"
              height="1000"
              viewBox="0 0 100 24"
              fill="currentColor"
              className="text-[#ADEBB3]/30"
            >
            <path d="M125 12H20 M30 2 L20 12 L30 22" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>) : (
              <HelpText />
            )}
            </div>
    </>
  )
}

const HelpText = () => {
  return (
    <div className="absolute top-1/2 right-2 flex flex-col transform translate-y-1/2 p-6 rounded-xl shadow-lg text-left text-white">
      <h2 className="text-2xl font-semibold text-[#ADEBB3]/60 ">File Format Guidelines</h2>

      <div className="flex flex-row w-[700px]">
        <div className="mt-3">
          <h3 className="text-lg text-[#EFFBF0] font-semibold">Question Paper Format</h3>
          <p className="text-sm text-[#EFFBF0] mt-1">
            All question papers must be in <b>.txt or .pdf or common image formats</b> format and follow this structure:
          </p>
          <pre className="bg-[#ADEBB3]/30 p-2 mt-2 text-sm rounded-xl whitespace-pre-wrap">
  {`SECTION
  [Write questions here]
  .
  .
  .`}
          </pre>
        </div>
        <div className="w-10"></div>
        <div className="mt-3">
          <h3 className="text-lg text-[#EFFBF0] font-semibold">Answer Sheet Format</h3>
          <p className="text-smtext-[#EFFBF0] mt-1">
            Answer sheets must also be in <b>.txt or .pdf or common image formats</b> format and follow this structure:
          </p>
          <pre className="bg-[#ADEBB3]/30 p-2 mt-2 text-sm rounded-xl whitespace-pre-wrap">
  {`SECTION
  [Answers for section]
  .
  .
  .`}
          </pre>
        </div>
      </div>
      <h2 className="text-sm text-[#EFFBF0] mt-10 ">- If the Evaluate button is not enabled after both file upload. Please wait upload functions are to cold start.</h2>
    </div>
    
  );
};


const ResponseSecion=({question,answer,feedback,score})=>{
  return(
    <div className="flex flex-col w-[1000px] ">
      <h1 className="text-left text-[#EFFBF0] p-7 bg-[#6BDB76]/10 rounded-3xl">{question}</h1>
      <div className="h-3"></div>
      <div className="text-left text-[#EFFBF0] p-7 bg-[#6BDB76]/20 rounded-3xl">
        <h1 className="text-left text-[#ADEBB3] px-7">Score: {score}</h1>
        <h1 className="text-left text-[#ADEBB3] px-7 pt-5 text-sm">Your Answer:</h1>
        <h1 className="text-left text-[#EFFBF0] px-7 ">{answer}</h1>
        <h1 className="text-left text-[#ADEBB3] px-7 pt-5 text-sm">Feedback:</h1>
        <h1 className="text-left text-[#EFFBF0] px-7 ">{feedback}</h1>
      </div>
    </div>
  );
};

export default UploadScreen