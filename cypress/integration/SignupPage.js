// File: cypress/integration/SignupPage.js
// ============================
class SignupPage {
  constructor(selectors) {
    this.selectors = selectors;
  }
  visit() {
    cy.visit('/SignUp');
  }
  enterCompanyName(companyName) {
    cy.get(this.selectors.companyNameText).type(companyName);
  }
  enterEmail(email) {
    cy.get(this.selectors.emailText).type(email);
  }
  enterFirstName(firstName) {
    cy.get(this.selectors.firstNameText).type(firstName);
  }
  enterLastName(lastName) {
    cy.get(this.selectors.lastNameText).type(lastName);
  }
  enterUserName(userName) {
    cy.get(this.selectors.userNameText).type(userName);
  }
  enterPassword(password1) {
    cy.get(this.selectors.passwordText).type(password1);
  }
  enterConfirmPassword(confirmPassword) {
    cy.get(this.selectors.confirmPasswordText).type(confirmPassword);
  }
  clickSignup() {
    cy.get(this.selectors.signupButton).click();
  }
  Signup(companyName, email, firstName, lastName, userName, password1, confirmPassword) {
    this.enterCompanyName(companyName);
    this.enterEmail(email);
    this.enterFirstName(firstName);
    this.enterLastName(lastName);
    this.enterUserName(userName);
    this.enterPassword(password1);
    this.enterConfirmPassword(confirmPassword);
    this.clickSignup();
  }
}
export default SignupPage;
