from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    firefox_options = Options()
    service = Service(GeckoDriverManager().install())
    firefox_options.set_capability("pageLoadStrategy", "eager")
    firefox_driver = webdriver.Firefox(service=service, options=firefox_options)
    firefox_driver.maximize_window()
    yield firefox_driver


def test_send_info(driver):
    input_data = 'text_for_check'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


def test_send_student_registration_form(driver):
    name = 'Max'
    last_name = 'Fray'
    email = 'max_fray@gmail.com'
    mobile_number = '9612555555'
    subject = 'co'
    current_address = 'Astana, Turan 46'
    state = 'NCR'
    city = 'Delhi'

    driver.get('https://demoqa.com/automation-practice-form')

    input_name = driver.find_element(By.ID, 'firstName')
    input_name.send_keys(name)

    input_last_name = driver.find_element(By.ID, 'lastName')
    input_last_name.send_keys(last_name)

    input_email = driver.find_element(By.ID, 'userEmail')
    input_email.send_keys(email)

    input_mobile = driver.find_element(By.ID, 'userNumber')
    input_mobile.send_keys(mobile_number)

    # Изменение даты рождения
    date_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'dateOfBirthInput'))
    )
    date_input.click()

    month_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@class='react-datepicker__month-select']"))
    )
    month_dropdown.click()
    month_option = driver.find_element(By.XPATH, "//option[@value='10']")
    month_option.click()

    year_dropdown = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
    year_dropdown.click()
    year_option = driver.find_element(By.XPATH, "//option[@value='1995']")
    year_option.click()

    day = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__"
                              "day--012 react-datepicker__day--weekend']")
    day.click()

    input_current_address = driver.find_element(By.ID, 'currentAddress')
    input_current_address.send_keys(current_address)

    choose_state = driver.find_element(By.ID, 'react-select-3-input')
    choose_state.send_keys(state)
    choose_state.send_keys(Keys.ARROW_DOWN)
    choose_state.send_keys(Keys.ENTER)

    choose_city = driver.find_element(By.ID, 'react-select-4-input')
    choose_city.send_keys(city)
    choose_city.send_keys(Keys.ARROW_DOWN)
    choose_city.send_keys(Keys.ENTER)

    checkbox_gender = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'gender-radio-1'))
    )
    checkbox_hobbies_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'hobbies-checkbox-1'))
    )
    checkbox_hobbies_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'hobbies-checkbox-2'))
    )

    # Из-за перекрытия элементов, использую ActionChains для клика по элементу
    actions = ActionChains(driver)
    actions.move_to_element(checkbox_gender).click().perform()
    actions.move_to_element(checkbox_hobbies_1).click().perform()
    actions.move_to_element(checkbox_hobbies_2).click().perform()

    input_subject = driver.find_element(By.ID, 'subjectsInput')
    input_subject.send_keys(subject)
    input_subject.send_keys(Keys.ENTER)

    sub_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'submit'))
    )
    # Скроллинг до элемента и клик по нему с помощью JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", sub_button)
    driver.execute_script("arguments[0].click();", sub_button)

    modal_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'modal-content'))
    )

    rows = modal_content.find_elements(By.XPATH, "//table[@class='table table-dark "
                                                 "table-striped table-bordered table-hover']/tbody/tr")

    # Печать информации из таблицы
    for row in rows:
        label = row.find_element(By.XPATH, "./td[1]").text
        value = row.find_element(By.XPATH, "./td[2]").text
        print(f"{label}: {value}")


def test_check_select(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_visible_text('Python')
    chosen_value = dropdown.first_selected_option.text
    driver.find_element(By.ID, 'submit-id-submit').click()
    result = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result.text == chosen_value


def test_check_text(driver):
    text = "Hello World!"
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.XPATH, "//div[@id='start']/button").click()
    result_string = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'finish'))
    )
    assert result_string.text == text
