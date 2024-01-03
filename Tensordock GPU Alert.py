import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from aiogram import Bot, types
import asyncio

# Create a 'Bot' instance
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'
bot = Bot(token=bot_token)

# Map GPU names to their xpaths
gpu_dict = {
    "A100 PCIe 80GB": '//*[@id="a100-pcie-80gb"]',
    "GeForce GTX 1070 PCIe 8GB": '//*[@id="geforcegtx1070-pcie-8gb"]',
    "GeForce RTX 3060 Ti PCIe 8GB": '//*[@id="geforcertx3060ti-pcie-8gb"]',
    "GeForce RTX 3080 Ti PCIe 12GB": '//*[@id="geforcertx3080ti-pcie-12gb"]',
    "GeForce RTX 3090 PCIe 24GB": '//*[@id="geforcertx3090-pcie-24gb"]',
    "GeForce RTX 4090 PCIe 24GB": '//*[@id="geforcertx4090-pcie-24gb"]',
    "L40 PCIe 48GB": '//*[@id="l40-pcie-48gb"]',
    "RTX A4000 PCIe 16GB": '//*[@id="rtxa4000-pcie-16gb"]',
    "RTX A5000 PCIe 24GB": '//*[@id="rtxa5000-pcie-24gb"]',
    "RTX A6000 PCIe 48GB": '//*[@id="rtxa6000-pcie-48gb"]',
    "V100 PCIe 16GB": '//*[@id="v100-pcie-16gb"]'
}

# Create a selection menu for the user
print("Please select the GPUs you are interested in (separated by commas):")
for i, gpu in enumerate(gpu_dict.keys(), start=1):
    print(f"{i}. {gpu}")

choices = input("Enter the numbers of your choices, separated by commas: ").split(',')
selected_gpus = [list(gpu_dict.keys())[int(choice) - 1] for choice in choices]

async def main():
    # Setup WebDriver
    print("Setting up WebDriver...")
    s=Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s)
    driver.set_page_load_timeout(600)  # Set the timeout limit to 600 seconds
    driver.get('https://marketplace.tensordock.com/order_list')
    print("WebDriver setup complete.")

    found_cards = set()

    while True:
        try:
            # Uncheck and check the checkboxes for the selected GPU models
            for selected_gpu in selected_gpus:
                print(f"Looking for the checkbox with xpath {gpu_dict[selected_gpu]}...")
                checkbox = driver.find_element(By.XPATH, gpu_dict[selected_gpu])
                if checkbox.is_selected():
                    print("Checkbox found. Unchecking the checkbox...")
                    checkbox.click()
                    print("Checkbox unchecked.")
                
                print("Checking the checkbox...")
                checkbox.click()
                print("Checkbox checked.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Check for the GPU model and location
        print("Looking for the GPU model and location...")
        elements = driver.find_elements(By.XPATH, '//span[contains(text(), "")]')
        locations = driver.find_elements(By.XPATH, '//span[@class="region-info"]')
        for element, location in zip(elements, locations):
            card_name = element.text.strip()  # remove leading and trailing whitespace
            server_location = location.text.strip()  # remove leading and trailing whitespace
            for selected_gpu in selected_gpus:
                if selected_gpu in card_name and card_name not in found_cards:
                    print(f"New {card_name} Server found at {server_location}!")
                    found_cards.add(card_name)
                    await bot.send_message(chat_id=chat_id, text=f"New {card_name} Server found at location {server_location}! Here is the link: https://marketplace.tensordock.com/order_list")

        time.sleep(10)  # wait for 10 seconds
        print("Refreshing the page...")
        driver.refresh()  # refresh the page
        print("Page refreshed.")

    # Close the aiohttp client session
    await bot.session.close()

# Run the main function
asyncio.run(main())
