import logo from './logo.svg';
import './App.css';
import LandingPage from './LandingPage';
import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";


function App() {
  const [showCircles, setShowCircles] = useState(true);

  const LandingPageButtonClick = () => {
    setShowCircles(false);
  };
  const circles = [
    { size: 1200, opacity: 0.5 },
    { size: 1000, opacity: 0.4 },
    { size: 700, opacity: 0.4 },
    { size: 500, opacity: 0.4 },
    { size: 300, opacity: 0.4 },
  ];
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
        duration: 90, 
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
        duration: 90, 
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
        {showCircles &&
          circles.map((circle, index) => (
            <motion.div
              key={index}
              className="absolute bg-[#53ba5e] rounded-full shadow-lg"
              style={{ width: `${circle.size}px`, height: `${circle.size}px`, opacity: circle.opacity }}
              variants={circleVariants}
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

        <LandingPage onLandingPageClick={LandingPageButtonClick}/>

        </div>
        </div>
        
      </div>

  );
}

export default App;
