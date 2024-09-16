from flask import Flask, render_template, request, redirect, url_for
from plyer import notification
from youtubesearchpython import VideosSearch
import time
import webbrowser
import os

# Function to display a desktop notification
def printNotification(message):
    notification.notify(
        title='Alert',
        message=message,
        app_name='Shutdown Alert',
        app_icon=None,
        timeout=10
    )

app = Flask(__name__)  # Create a Flask app

@app.route('/')  # Home route
def index():
    return render_template('index.html')

# Route to shutdown the computer
@app.route('/goodnight', methods=['POST'])
def goodnight():
    printNotification('The computer will shutdown now')  # Display desktop notification
    time.sleep(10)  # Sleep for 10 seconds
    os.system("shutdown /s /t 1")  # Shutdown the computer in 1 second
    return redirect(url_for('index'))   # Return a message

#Route for Sleep Timer
@app.route('/sleep', methods=['POST'])
def sleepTimer():
    print("The Computer will shutdown in 45 minutes")
    time.sleep(2700) # Sleep for 45 minutes
    os.system("shutdown /s /t 1") # Shutdown the computer
    return redirect(url_for('index')) # Return a message


def GetIPfromCSV():
    #Store the IP addresses in a list
    addresses = []
    with open('ip.csv', 'r') as file:
        for line in file:
            addresses.append(line.strip())
    return addresses


if __name__ == '__main__':
    AtUni = True
    addresses = GetIPfromCSV()
    if AtUni:
        app.run(debug=True, host=addresses[0], port=5000)  # Run the Flask app on specified host and port
    else:
        app.run(debug=True, host=addresses[1], port=5000)  # Run the Flask app on specified host and port
