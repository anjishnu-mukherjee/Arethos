import logo from './logo.svg';
import './App.css';
import LandingPage from './LandingPage';
import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import UploadScreen from './UploadScreen';


function App() {
  const [showConCircles, setShowConCircles] = useState(true);
  const [showCircles, setShowCircles] = useState(true);
  const [pageCount, setPageCount] = useState(0);
  
  const [showHelp, setShowHelp] = useState(false);

  


  
  const onBackClick = () => {
    setShowCircles(true);
    setPageCount(0);
    // setQuestionFile(null);
  //  setAnswerFile(null);
  }

  const LandingPageButtonClick = () => {
    // setShowConCircles(false);
    setShowCircles(false);
    setPageCount(1);
  };
  const circles = [
    { size: 1200, opacity: 0.5 },
    { size: 1000, opacity: 0.4 },
    { size: 700, opacity: 0.4 },
    { size: 500, opacity: 0.4 },
    { size: 300, opacity: 0.4 },
  ];

  const getVariants = (pageCount) => {
    switch (pageCount) {
      case 0:
        return {
          initial: {
            x: "0vw",
            y: "60vw",
            opacity: 0.4, // ✅ Reset to visible
            filter: "blur(0px)", // ✅ No blur
          },
          animate: {
            x: ["30vw", "20vw", "40vw", "30vw"],
            y: ["-50vw", "-20vw", "-50vw", "-50vw"],
            opacity: 0.4, // ✅ Stay at 0.4
            // filter: "blur(0px)", // ✅ Keep blur at 0
  
            transition: {
              duration: 115,
              repeat: Infinity,
              ease: "easeInOut",
            },
          },
          exit: {
            opacity: 0, // ✅ Fully fades out
            filter: "blur(0px)", // ✅ No blur on exit
            transition: { duration: 1 },
          },
        };
  
      case 1:
        return {
          initial: {
            x: "0vw",
            y: "60vw",
            opacity: 0, // ✅ Start fully invisible
            filter: "blur(30px)", // ✅ Start with heavy blur
          },
          animate: {
            x: ["-50vw"],
            y: ["0vw"],
            opacity: [0, 0.4], // ✅ Gradually fade in
            filter: ["blur(0px)", "blur(30px)"], // ✅ Smooth blur transition
  
            transition: {
              duration: 2,
              ease: "linear",
            },
          },
          exit: {
            opacity: 0, // ✅ Fully fades out when leaving
            filter: "blur(30px)", // ✅ Increase blur before disappearing
            transition: { duration: 1 },
          },
        };
  
      default:
        return {};
    }
  };
  

  const circleVariants = {
    initial: {
      x: "0vw",
      y: "60vw",
      opacity: 0.4, 
    },
    animate: {
      x: ["30vw", "20vw", "40vw","30vw"], 
      y: ["-50vw", "-20vw", "-50vw","-50vw"],
      opacity: 0.4, 
      transition: {
        duration: 115, 
        repeat: Infinity,
        ease: "easeInOut",
      },
    },
    exit: {
      opacity: 0, 
      transition: { duration: 1 },
    },
  };

  const lowerCircleVariants = {
    initial: {
      x: "0vw",
      y: "60vw",
      opacity: 0.4, 
    },
    animate: {
      x: ["-30vw", "-80vw", "-80vw","-30vw"], 
      y: ["50vw", "0vw", "70vw","50vw"],
      opacity: 0.4, 
      transition: {
        duration: 110, 
        repeat: Infinity,
        ease: "easeInOut",
      },
    },
    exit: {
      opacity: 0, 
      transition: { duration: 1 },
    },
  };

  return (
    <div className="App">
      <div className="relative flex items-center justify-center min-h-screen bg-black overflow-hidden">
        <AnimatePresence>
          {showCircles && 
          <motion.div className="absolute w-[900px] h-[900px] bg-[#53ba5e] rounded-full  opacity-20" 
              variants={lowerCircleVariants}
              initial="initial"
              animate="animate"
              exit="exit"
          ></motion.div>}
        </AnimatePresence>
        <AnimatePresence>
        {showConCircles &&
          circles.map((circle, index) => (
            <motion.div
              key={index}
              className="absolute bg-[#53ba5e] rounded-full shadow-lg"
              style={{ width: `${circle.size}px`, height: `${circle.size}px`, opacity: circle.opacity }}
              variants={ 
                getVariants(pageCount)
                }
              initial="initial"
              animate="animate"
              exit="exit"
            />
          ))}
      </AnimatePresence>

        <div className="relative w-full min-h-screen flex items-center justify-center px-8">
          <div className='absolute left-10 top-1 py-1 flex flex-row items-center'>
            {pageCount>0 ?  (
            <button
            onClick={onBackClick}>
            <span className="material-symbols-outlined text-4xl text-[#EFFBF0]/40 px-e-5 py-1">
            keyboard_backspace
              </span>
            </button>
            ):(
              <div className='py-6'></div>
            )}
          <h1 onClick={onBackClick}  className="text-m text-[#EFFBF0]/40 select-none cursor-pointer">
          FLIPBIT
          </h1>
        </div>
        <AnimatePresence mode="wait">
          {(() => {
            switch (pageCount) {
              case 0:
                return (
                  <motion.div
                    key="landing"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 1 }}
                  >
                    <LandingPage onLandingPageClick={LandingPageButtonClick} />
                  </motion.div>
                );

              case 1:
                return (
                  <motion.div
                    key="page1"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 1 }}
                  >
                    <UploadScreen /> 
                     {/* handleQuestionFileChange={handleQuestionFileChange} questionFile={questionFile} handleAnswerFileChange={handleAnswerFileChange} answerFile={answerFile} handleUpload={handleUpload} /> */}
                  </motion.div>
                );

              default:
                return null;
            }
          })()}
        </AnimatePresence>

        </div>
        </div>
        
      </div>

  );
}

export default App;
