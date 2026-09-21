"""
Sample Selenium test for DevTrack.
Run with: pytest tests/selenium/test_bug_flow.py -v
Requires: pip install selenium pytest webdriver-manager
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000"  # frontend URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()


def test_login_flow(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("testpass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )
    assert "/dashboard" in driver.current_url


def test_create_bug(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("testpass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))

    driver.get(f"{BASE_URL}/bugs/new")
    driver.find_element(By.NAME, "title").send_keys("Login button unresponsive on Safari")
    driver.find_element(By.NAME, "severity").send_keys("High")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Login button unresponsive')]"))
    )
    assert "Login button unresponsive" in driver.page_source


def test_bug_status_update(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("testpass123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))

    driver.get(f"{BASE_URL}/bugs")
    first_bug = driver.find_element(By.CSS_SELECTOR, ".bug-row")
    first_bug.click()

    status_dropdown = driver.find_element(By.NAME, "status")
    status_dropdown.send_keys("Resolved")

    driver.find_element(By.NAME, "root_cause").send_keys("CSS z-index conflict on overlay")
    driver.find_element(By.NAME, "resolution").send_keys("Fixed z-index stacking order")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Resolved')]"))
    )
    assert "Resolved" in driver.page_source
