/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      animation : {
        "move-blur-bg": "moveBlurBg 85s ease-in-out infinite",
        "move-bg": "moveBg 100s ease-in-out infinite",

      },
      keyframes: {
        moveBlurBg: {
          "0%": { transform: "translateX(50vw) translateY(-50vw)" },
          "20%": { transform: "translateX(38vw) translateY(30vw)" },
          "50%": { transform: "translateX(-50vw) translateY(10vw)" },
          "100%": { transform: "translateX(50vw) translateY(-50vw)" },
        },
        moveBg: {
          "0%": { transform: "translateX(20vw) translateY(30vw)" },
          "20%": { transform: "translateX(-50vw) translateY(-30vw)" },
          "80%": { transform: "translateX(50vw) translateY(-20vw)" },
          "100%": { transform: "translateX(20vw) translateY(30vw)" },
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