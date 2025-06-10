// cypress.config.cjs
const { defineConfig } = require('cypress');
module.exports = {
  e2e: {
    baseUrl: "https://192.168.1.11",
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
};
