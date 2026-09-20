/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        paper: {
          50: '#fbfbfb',
          100: '#f7f7f7',
          200: '#e5e5e5',
          300: '#d4d4d4',
          800: '#262626',
          900: '#171717',
          950: '#0f0f0f'
        },
        ink: {
          50: '#f6f6f7',
          100: '#e2e3e5',
          200: '#c5c7cb',
          400: '#71767f',
          600: '#434751',
          800: '#202227',
          900: '#111215',
        }
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        serif: ['Charter', 'Bitstream Charter', 'Sitka Text', 'Cambria', 'serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
      }
    },
  },
  plugins: [],
}
