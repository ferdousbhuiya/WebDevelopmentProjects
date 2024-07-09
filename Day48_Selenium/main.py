from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)

# driver = webdriver.Chrome()
# driver.get('https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/?_encoding=UTF8&pd_rd_w=UWWVV&content-id=amzn1.sym.3a9105c3-5c23-4606-a1b8-e2798f4bd814%3Aamzn1.symc.8b620bc3-61d8-46b3-abd9-110539785634&pf_rd_p=3a9105c3-5c23-4606-a1b8-e2798f4bd814&pf_rd_r=G04QBW69W8FYBPSJ7J5M&pd_rd_wg=wapoK&pd_rd_r=655b3c95-74a6-4be5-8892-6cf2b9c29b9d&ref_=pd_hp_d_btf_ci_mcx_mr_hp_d')
#
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
#
# print(f"The price is: {price_dollar.text}.{price_cents.text}")
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://python.org")

events = driver.find_elements(By.XPATH, value='/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul')

event_list = []

for i in events:
    event_list.append(i.text.replace("\n", ",").strip())
# Split the single string into individual elements
event_items = event_list[0].split(',')

# Initialize the dictionary
events_dict = {}

# Process the list to create a dictionary
for i in range(0, len(event_items), 2):
    # Extract date and program from the list
    date = event_items[i]
    program = event_items[i + 1]

    # Create a dictionary for the event
    event_details = {
        "time": date,
        "program": program
    }

    # Add the event details to the main dictionary
    events_dict[i // 2] = event_details

# Print the events dictionary
print(events_dict)

