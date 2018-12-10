# What this is
An application written in python designed to make use of the ourmanna API in order to fetch the verse of the day and post it to a list of slack channels of your choice.

## What you need
1. If you do not have Python, download and install python (Developed using 3.6.2)
2. Clone this repository
3. If you do not have pip, Run "get-pip.py" from inside the repository root folder in your command line interface
4. Execute `pip install slackclient` in your command line interface
5. Configure your Slack Legacy Token information and Channels to Post to in settings.json in the config folder
5. Run runner.py from inside the repository root folder in your command line interface

## Coming soon:
- Support for 0Auth2 authentication and authorization
- A full installer for managing python, pip, and dependencies
- Class-based refactor of code for maintainability