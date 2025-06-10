// File: cypress/integration/UserConfigPage.js
// ============================
class UserConfigPage {
  constructor(selectors) {
    this.selectors = selectors;
  }
  visitUserdataPage() {
     cy.visit('/userconfig', { failOnStatusCode: false });

  }
  enterhostname(hostname) {
    cy.get(this.selectors.hostnametext1).type(hostname);
  }
  Useradd(hostname) {
    this.enterhostname(hostname);
  }
}
export default UserConfigPage;
