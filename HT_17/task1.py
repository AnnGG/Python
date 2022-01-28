# Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:

# https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link

# заповнити і відправити її.
# Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
# В репозиторії скріншоти зберегти.


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link")

get_title = driver.title

search_box = driver.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
driver.implicitly_wait(0.6)

search_box.click()
search_box.send_keys("Nadia")
driver.save_screenshot("filling.png")

search_button = driver.find_element(By.CSS_SELECTOR, 'span.exportLabel')
search_button.click()
driver.save_screenshot("sending.png")

print(get_title)

driver.quit()
