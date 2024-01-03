# Tensordock-GPU-Alert
TensorDock GPU Alert is a Python script that monitors GPU server availability on TensorDock. It identifies new servers, extracts details, and sends alerts via Telegram.

Welcome to this repository, This is a powerful tool designed to monitor the availability of GPU servers on the TensorDock Marketplace. This Python script continuously checks the marketplace and identifies new servers as they become available.

The script is designed to provide detailed information about each server, including the model of the GPU and its location. This allows users to quickly identify servers that meet their specific requirements.

One of the key features of this script is its integration with Telegram. When a new server is identified, the script automatically sends a message to a specified Telegram chat. This ensures that users are immediately notified of new servers, allowing them to react quickly to changes in availability.



# How to Use

**Step 1: Install Python**

First, you need to have Python installed on your machine. You can download it from the official website: https://www.python.org/downloads/

**Step 2: Install Firefox**

You need to have Firefox installed as the script uses Firefox’s WebDriver. You can download Firefox from here: https://www.mozilla.org/en-US/firefox/new/

**Step 3: Install Required Libraries**

You will need several Python libraries. You can install them using pip, which is a package installer for Python.

open your terminal or command prompt at the location where you placed TensordockGPUAlert.py  and type the following command:

``` pip install -r requirements.txt ```


**Step 4: Get Your Telegram Bot Token and Chat ID**

You need to create a bot on Telegram to get your bot token. You can do this by talking to BotFather on Telegram. More details can be found here:

https://core.telegram.org/bots#botfather

To get your chat ID Invite @RawDataBot to a newly made group.

Upon joining it will output a JSON file where your chat id will be located at message.chat.id.

**Step 5: Update the Python Script**

Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' in the Python script with your actual bot token and chat ID.


Finally, you can run the script. Save it as a .py file and run it using Python from your terminal or command prompt:

python your_script.py

And that’s it! Your bot should now be up and running. If you have any questions or run into any issues, feel free to ask. 😊
