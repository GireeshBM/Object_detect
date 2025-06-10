class AddConfigPage {
  constructor(selectors) {
    this.selectors = selectors;
  }

  visitLiveStreamPage() {
    cy.visit('/LiveStream');
  }
  clickAdd() {
    cy.contains("Add Camera", { timeout: 10000 }).should('exist').click();
  }
  // clickadd11(){
  // Check if config is already done by verifying a field is missing or "Save" is not visible
//   cy.get('button.Config_nextButton__qwb_c').then(($btn) => {
//     if ($btn.is(':visible')) {
//       cy.get("[name='host_name']").clear().type("server-01");
//       cy.get("[name='host_ip']").clear().type("192.168.1.11");
//       cy.get("[name='g_core_ip']").clear().type("192.168.1.0");
//       cy.get("[name='sender_mail']").clear().type("reporting@bluepolicy.de");
//       cy.get("[name='sender_password']").clear().type("zxbcjhvxdcxj");    
//       cy.wrap($btn).contains('Save').click();
//     } else {
//       cy.log('Configuration already done, skipping Save.');
//     }
//   });
// }
  //clickadd11(){
    // cy.get("[name='host_name']").type("server-01");
     //cy.get("[name='host_ip']").type("192.168.1.11");
     //cy.get("[name='g_core_ip']").type("192.168.1.0");
     //cy.get("[name='sender_mail']").type("reporting@bluepolicy.de");
     //cy.get("[name='sender_password']").type("zxbcjhvxdcxj");    
     //cy.get('button.Config_nextButton__qwb_c').contains('Save').click();
   //}
  entercamname(CamName1) {
    cy.get(this.selectors.camnametext1).type(CamName1);
  }
  enterglobalid(globalID1) {
    cy.get(this.selectors.globalidtext1).type(globalID1);
  }
  enterrtsplink1(rtsplink1) {
    cy.get(this.selectors.RTSPlinktext1).type(rtsplink1);
  }
  // selectServiceType(servicetype1) {
  //   cy.get('.Home_dropdownComp__CnvfF') // container holding dropdown items
  //     .contains('p', servicetype1)            // match the text of the dropdown option
  //     .click();                         // click to select
  // }

  clickarrow() {
    cy.get(this.selectors.arrowicon).click();
  }
  enterbeltstopvalue(beltstopvalue) {
    cy.get(this.selectors.beltstoptimer).type(beltstopvalue);
  }
  enteralarmendtime(alarmendtimer) {
    cy.get(this.selectors.alarmendtime).type(alarmendtimer);
  }
  enterjammedbox(jammedboxvalue) {
    cy.get(this.selectors.jammedbox).type(jammedboxvalue);
  }
  // enterguidvalue(guidcam1) {
  //   cy.get(this.selectors.guidtext1).type(guidcam1);
  // }  
  // enterpagescroll(){
  //   cy.scrollTo(0, 2500);
  // }
  enterx1value(x1value1) {
    cy.get(this.selectors.x1value1text1).type(x1value1);
  }
  entery1value(y1value1) {
    cy.get(this.selectors.y1value1text1).type(y1value1);
  }
  enterx2value(x2value1) {
    cy.get(this.selectors.x2value1text1).type(x2value1);
  }
  entery2value(y2value1) {
    cy.get(this.selectors.y2value1text1).type(y2value1);
  }
  enterx3value(x3value1) {
    cy.get(this.selectors.x3value1text1).type(x3value1);
  }
  entery3value(y3value1) {
    cy.get(this.selectors.y3value1text1).type(y3value1);
  }
  enterx4value(x4value1) {
    cy.get(this.selectors.x4value1text1).type(x4value1);
  }
  entery4value(y4value1) {
    cy.get(this.selectors.y4value1text1).type(y4value1);
  }
  clickAdd1() {
    cy.xpath('//*[@id="__next"]/div/main/div/div[6]/button')
      .scrollIntoView()
      .should('be.visible')
      .click({ force: true });
  }

  clickapply() {
    cy.get(this.selectors.applychanges).click();
  }
// cy.contains('button', 'Add')
//   .scrollIntoView()
//   .should('be.visible')
//   .click({ force: true });


  Add(CamName1, globalID1, rtsplink1, beltstopvalue, alarmendtimer, jammedboxvalue, x1value1, y1value1, x2value1, y2value1, x3value1, y3value1, x4value1, y4value1) {
    this.clickAdd();
    // this.clickadd11();
    this.entercamname(CamName1);
    this.enterglobalid(globalID1);
    this.enterrtsplink1(rtsplink1);
    // this.selectServiceType(servicetype1); 
    this.clickarrow();
    this.enterbeltstopvalue(beltstopvalue);
    this.enteralarmendtime(alarmendtimer);
    this.enterjammedbox(jammedboxvalue);
    // this.enterguidvalue(guidcam1);
    // this.enterpagescroll();
    this.enterx1value(x1value1);
    this.entery1value(y1value1);
    this.enterx2value(x2value1);
    this.entery2value(y2value1); 
    this.enterx3value(x3value1);
    this.entery3value(y3value1);
    this.enterx4value(x4value1);
    this.entery4value(y4value1);
    this.clickAdd1();
    this.clickapply();

  }
}

export default AddConfigPage;

