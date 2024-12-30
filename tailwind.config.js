/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      boxShadow: {
        underline: "inset 0 -2px 0 0",
      }
    },
  },
  plugins: [
    "@tailwindcss/typography",
    "@tailwindcss/forms",
  ],
}

