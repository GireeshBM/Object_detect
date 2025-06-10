// File: cypress/integration/LoginPage.js
// ============================
class LoginPage {
  constructor(selectors) {
    this.selectors = selectors;
  }
  visit1() {
    cy.visit('/');
  }
  enterUsername(username) {
    cy.get(this.selectors.usernametext).type(username);
  }
  enterPassword(password) {
    cy.get(this.selectors.passwordtext).type(password);
  }
  clickLogin() {
    cy.get(this.selectors.Loginbutton).click();
  }
  login(username, password) {
    this.enterUsername(username);
    this.enterPassword(password);
    this.clickLogin();
  }
}
export default LoginPage;