/** @type {import('tailwindcss').Config} */
export default {
  
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],

  
  darkMode: "class",

  theme: {
    extend: {
      colors: {
        // 💙 Your custom palette
        waveLight: "#f0f4ff", // good for backgrounds
        waveDark: "#0b1120",  // deep, dark base
        waveBlue: "#2563eb",  // accent blue (primary)
        waveAccent: "#38bdf8", // bright cyan accent
      },
    },
  },

  plugins: [],
};
