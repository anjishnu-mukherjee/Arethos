/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      animation : {
        "move-blur-bg": "moveBlurBg 105s ease-in-out infinite",
        "move-bg": "moveBg 80s ease-in-out infinite",

      },
      keyframes: {
        moveBlurBg: {
          "0%": { transform: "translateX(-30vw) translateY(50vw)" },
          "50%": { transform: "translateX(-90vw) translateY(10vw)" },
          "75%": { transform: "translateX(-80vw) translateY(50vw)" },
          "100%": { transform: "translateX(-30vw) translateY(50vw)" },
        },
        moveBg: {
          "0%": { transform: "translateX(30vw) translateY(-50vw)"},
          "50%": { transform: "translateX(30vw) translateY(-10vw)" },
          "100%": { transform: "translateX(30vw) translateY(-50vw)" },
        },

      },

      fontFamily : {
        ubuntu_monospace : ["Ubuntu Sans Mono","monospace"] 
      }
      // backgroundSize: {
      //   "size-200": "100% 100%",
      // },

    },
  },
  plugins: [],
};