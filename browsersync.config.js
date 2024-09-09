module.exports = {
    proxy: "localhost:8080",  // Proxy to Django’s development server
    files: ["static/css/*.css", "templates/**/*.html"],  // Paths to watch for changes
    open: false,  // Don’t open a new tab automatically
    notify: false,  // Disable BrowserSync notifications in the browser
    injectChanges: true,  // Inject CSS changes without a full page reload
  };
  