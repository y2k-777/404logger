# 404 IP Logger

This is a Python-based IP logger built using Flask. It captures a user's IP address and additional details like country, timezone, and ISP. The user is redirected to a URL of your choice after their IP is logged.

## Features
- Logs IP address, country, region, city, ZIP, latitude, longitude, timezone, ISP, and organization.
- Customizable redirect URL.
- Developed by Y2K.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ip-logger.git
    cd ip-logger
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask server:
    ```bash
    python ip_logger.py
    ```

2. Choose from the menu:
   - **Option 1**: Generate a link by starting the Flask server. Then expose it using `ngrok` by running:
     ```bash
     ngrok http 5000
     ```
     Share the generated `ngrok` URL to log visitor IPs.
   
   - **Option 2**: Set a custom redirect URL. Users will be redirected here after their IP is logged.

   - **Option 3**: Exit the application.

3. When someone visits the link, their IP and details will be logged in the terminal. 
     **NOTE: Send the ngrok forwarding link to the person you wish to IP log. You can customise this permanently with a paid ngrok account, or use an URL shortner to change the link.

## Example Output

--- New Visitor --- 
IP: 192.168.1.1 
Country: United States 
Region: California City: San Francisco 
ZIP: 94107 
Latitude: 37.7749 
Longitude: -122.4194 
Timezone: America/Los_Angeles 
ISP: Comcast Cable Org: Comcast Cable Communications LLC
