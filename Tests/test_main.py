import os
from selene import have
from selene.support.shared import browser

def test_name(brwsr):
    browser.open('/automation-practice-form')

    #input data
    browser.element('[id=firstName]').type('Katrin')
    browser.element('[id=lastName]').type('Torsunova')
    browser.element('[id=userEmail]').type('Katrin@test.ru')
    browser.element('//label[contains(text(), "Female")]').click()
    browser.element('[id=userNumber]').type('8967625366')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="10"]').click()
    browser.element('[class=react-datepicker__year-select]').click()
    browser.element('[value="1994"]').click()
    browser.element('[class~=react-datepicker__day--015]').click()
    browser.element('#subjectsInput').type('B').press_enter()
    browser.element('//label[contains(text(), "Reading")]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo1687420339.jpeg'))
    browser.element('[id=currentAddress]').click()
    browser.element('[id=currentAddress]').type('ul. Kronverksky 49')
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("Haryana")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Karnal")).click()
    browser.element('[id=submit]').click()

    #checking data
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Katrin Torsunova'))
    browser.element('.modal-body').should(have.text('Katrin@test'))
    browser.element('.modal-body').should(have.text('Female'))
    browser.element('.modal-body').should(have.text('8967625366'))
    browser.element('.modal-body').should(have.text('15 November,1994'))
    browser.element('.modal-body').should(have.text('Biology'))
    browser.element('.modal-body').should(have.text('Reading'))
    browser.element('.modal-body').should(have.text('photo1687420339.jpeg'))
    browser.element('.modal-body').should(have.text('ul. Kronverksky 49'))
    browser.element('.modal-body').should(have.text('Haryana Karnal'))
