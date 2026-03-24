import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    proxy: {
      // http://localhost:5173/users -> http://localhost:8000/users
      '/users': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      // if we add this instead, we can then use /api/users
      // in the form action
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        // remove the /api prefix when forwarding to the backend
        rewrite: (path) => path.replace(/^\/api/, '')
    }
  }
})
