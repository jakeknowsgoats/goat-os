/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        bg: "#0e1014",
        card: "#171a21",
        card2: "#1f2430",
        line: "#2a303c",
        mut: "#9aa3b2",
        goat: "#e67e22",
        goat2: "#f39c4b",
      },
    },
  },
  plugins: [],
};
