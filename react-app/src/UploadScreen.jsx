import React from "react";

const UploadScreen=()=>{
    return (
        <div className="flex flex-col">
         <button 
            className="absolute left-20 top-1/4  flex items-center text-[#EFFBF0] text-base py-3 px-12 rounded-full transition duration-500 ease-in-out bg-[#6BDB76]/20 backdrop-blur-md hover:bg-[#6BDB76]/40 active:text-[#6BDB76] select-none">
           <span class="material-symbols-outlined text-5xl">add</span>
            &nbsp;ADD QUESTION PAPER
            </button>
            <button 
            className="absolute left-20 top-1/3 flex items-center text-[#EFFBF0] text-base py-3 px-14 rounded-full transition duration-500 ease-in-out bg-[#6BDB76]/20 backdrop-blur-md hover:bg-[#6BDB76]/40 active:text-[#6BDB76] select-none">
           <span class="material-symbols-outlined text-5xl">add</span>
            &nbsp;ADD ANSWER SHEET
            </button>
            <button 
            className="absolute left-20 bottom-1/4 flex items-center text-[#EFFBF0] text-base py-3 px-20 rounded-full transition duration-500 ease-in-out bg-[#6BDB76]/20 backdrop-blur-md hover:bg-[#6BDB76]/40 active:text-[#6BDB76] select-none">
            EVALUATE&nbsp;
           <span class="material-symbols-outlined text-5xl">trending_flat</span>
            </button>
            <div className="absolute right-0 top-0 text-[#ADEBB3]/30">
            <svg
    xmlns="http://www.w3.org/2000/svg"
    width="1000"
    height="1000"
    viewBox="0 0 100 24"
    fill="currentColor"
    className="text-[#ADEBB3]/30"
  >
    <path d="M125 12H20 M30 2 L20 12 L30 22" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
        </div>

        </div>
    );
};

export default UploadScreen