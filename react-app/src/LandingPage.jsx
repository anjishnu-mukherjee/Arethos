import React from "react";



const LandingPage = () => {
    return (
        <div className="relative flex items-center justify-center min-h-screen bg-black overflow-hidden">
        <div className="absolute w-[900px] h-[900px] bg-[#53ba5e] rounded-full  opacity-20 animate-move-blur-bg"></div>
        
        <div className="absolute w-[1200px] h-[1200px] bg-[#53ba5e] rounded-full opacity-50  animate-move-bg"></div>
        <div className="absolute w-[1000px] h-[1000px] bg-[#53ba5e] rounded-full opacity-40  animate-move-bg shadow-lg"></div>
        <div className="absolute w-[700px] h-[700px] bg-[#53ba5e] rounded-full opacity-40  animate-move-bg shadow-lg"></div>
        <div className="absolute w-[500px] h-[500px] bg-[#53ba5e] rounded-full opacity-40  animate-move-bg shadow-lg"></div>
        <div className="absolute w-[300px] h-[300px] bg-[#53ba5e] rounded-full opacity-40  animate-move-bg shadow-lg"></div>
        <div className="relative w-full min-h-screen flex items-center justify-center px-8">
        <h1 className="absolute left-10 top-1 py-10 text-m text-[#EFFBF0]/40 select-none">
        ARETHOS
        </h1>
        <h1 className="absolute left-10 top-1/25  text-base text-[#6BDB76]/50 select-none">
            UPLOAD.<br />
            EVALUATE.<br />
            LEARN.
        </h1>
        <div className="flex flex-col items-center text-center select-none">
            <div className="flex flex-row">
            <h1 className="text-[#EFFBF0] text-[22px]">GET STARTED WITH YOUR</h1>
            <h1 className="text-[#6BDB76] text-[22px]">&nbsp;LEARNING&nbsp;</h1>
            <h1 className="text-[#EFFBF0] text-[22px]">JOURNEY!</h1>
            </div>

            <div className="h-10"></div>

            <button className="flex items-center justify-center text-[#EFFBF0] text-base py-3 px-12 rounded-full transition duration-500 ease-in-out bg-[#6BDB76]/20 backdrop-blur-md hover:bg-[#6BDB76]/40 active:text-[#6BDB76] select-none">
            LET'S BEGIN&nbsp;
            <span className="material-symbols-outlined text-6xl ">
                trending_flat
            </span>
            </button>
        
        </div>
        
        <h1 className="absolute left-10 bottom-0 py-9 text-xs text-[#6BDB76]/30 select-none">
            © {new Date().getFullYear()} Arethos. All rights reserved.
        </h1>
        <a href="https://github.com/anjishnu-mukherjee/Arethos" target="_blank" className="absolute right-10 bottom-0 py-9 text-xs text-[#6BDB76]/40 hover:text-[#6BDB76]/60 underline select-none">
            Github
        </a>
        <a href="https://github.com/anjishnu-mukherjee/Arethos" target="_blank" className="absolute right-20 bottom-0 px-5 py-9 text-xs text-[#6BDB76]/40 hover:text-[#6BDB76]/60 underline select-none">
            Disclaimer
        </a>
        </div>

      </div>
    );
};

export default LandingPage;