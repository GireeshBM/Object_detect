// File: cypress/e2e/main.cy.js
// ============================
import LoginPage from '../integration/LoginPage';
import AddConfigPage from '../integration/AddConfigPage';
import UserConfigPage from '../integration/UserConfigPage';
// import SignupPage from '../integration/SignupPage';

describe('Admin through positive flows steps', () => {
  let loginData;
  let addconfigData;
  let userconfigData;
  let webElements;
  let loginPage;
  let addConfigPage;
  let userConfigPage;
  // let signupPage;

  before(() => {
    cy.fixture('inputtext').then((data1) => {
      loginData = data1;
      addconfigData = data1;
      userconfigData = data1;
    });
    cy.fixture('WebElements').then((data2) => {
      webElements = data2;
    });
  });

  beforeEach(() => {
    loginPage = new LoginPage(webElements);
    addConfigPage = new AddConfigPage(webElements);
    userConfigPage = new UserConfigPage(webElements);
    // signupPage = new SignupPage(webElements);

    loginPage.visit1();
  });

  it('should login successfully with valid credentials', () => {
    loginPage.login(loginData.username, loginData.password);
  });

  // it('should signup successfully with valid inputs', () => {
  //   signupPage.visit();
  //   signupPage.Signup(
  //     loginData.companyName,
  //     loginData.email,
  //     loginData.firstName,
  //     loginData.lastName,
  //     loginData.userName,
  //     loginData.password1,
  //     loginData.confirmPassword
  //   );
  // });

  it('set user the config details', () => {
     userConfigPage.visitUserdataPage();
     userConfigPage.Useradd(userconfigData.hostname);
   });

  it('set up the config details', () => {
    loginPage.login(loginData.username, loginData.password);
    // addConfigPage.visit();
    addConfigPage.Add(
      addconfigData.CamName1,
      addconfigData.globalID1,
      addconfigData.rtsplink1,
      addconfigData.beltstopvalue,
      addconfigData.alarmendtimer,
      addconfigData.jammedboxvalue,
      // addconfigData.guidvalues,
      addconfigData.x1value1,
      addconfigData.y1value1,
      addconfigData.x2value1,
      addconfigData.y2value1,
      addconfigData.x3value1,
      addconfigData.y3value1,
      addconfigData.x4value1,
      addconfigData.y4value1,

    );
  });
});
