from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import logging
import time
import os

# Configure logging
logging.basicConfig(filename="test_logs.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load test data from a JSON file
with open("test_data.json", "r") as file:
    test_data = json.load(file)

username = test_data["username"]
password = test_data["password"]
card_number = test_data["card_number"]
expiry_date = test_data["expiry_date"]
cvv = test_data["cvv"]

# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def test_successful_payment():
    """Automates a successful payment transaction with improved checks and logging."""
    try:
        # Step 1: Open the Payment Page
        driver.get("https://tanamicapital.com/payment")
        logging.info("Opened Payment Page")

        # Step 2: Log in
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
        logging.info("User logged in successfully")
        time.sleep(2)

        # Step 3: Enter Payment Details
        driver.find_element(By.ID, "card_number").send_keys(card_number)
        driver.find_element(By.ID, "expiry_date").send_keys(expiry_date)
        driver.find_element(By.ID, "cvv").send_keys(cvv)
        logging.info("Entered payment details")

        # Step 4: Submit Payment
        driver.find_element(By.ID, "submit_payment").click()
        time.sleep(3)
        logging.info("Submitted payment")

        # Step 5: Validate Payment Success Message
        success_message = driver.find_element(By.ID, "success_message").text
        assert "Payment Successful" in success_message, "Test Failed: Payment did not go through."
        logging.info("Payment transaction was successful.")

        # Step 6: Validate Transaction ID
        transaction_id = driver.find_element(By.ID, "transaction_id").text
        assert transaction_id != "", "Test Failed: No transaction ID generated."
        logging.info(f"Transaction ID: {transaction_id}")

    except Exception as e:
        logging.error(f"Test Failed: {e}")
    finally:
        # Close Browser
        driver.quit()
        logging.info("Browser closed.")

# Run the test
test_successful_payment()
