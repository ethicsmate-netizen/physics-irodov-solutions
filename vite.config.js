import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/physics-irodov-solutions/',
  server: {
    port: 3000,
    open: false
  }
});