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
        return{
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
            }
          
        };
    case 1:
      return {
        initial: {
          x: "0vw",
          y: "60vw",
          opacity: 0, 
          filter: "blur(0px)", // Start with blur
        },
        animate: {
          x: ["-50vw"], 
          y: ["0vw"],
          opacity: [0, 0.15],  // Fade in and out
          filter: ["blur(10px)","blur(30px)"], // Blur transition
          transition: {
            duration: 2, 
            repeat: 0,
            ease: "linear",
          },
        },
        exit: {
          opacity: 0, 
          filter: "blur(10px)", // Blur before exiting
          transition: { duration: 1 },
        }
      };

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
        <h1 className="absolute left-10 top-1 py-10 text-m text-[#EFFBF0]/40 select-none">
        ARETHOS
        </h1>
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
