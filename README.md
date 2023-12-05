# eMadariss

## Overview
eMadariss is a project designed to streamline the homework management process for students frustrated with their school's interface. It's a program specifically crafted to extract homework details from the school's website and seamlessly export them into the popular Trello to-do list app. Say goodbye to clunky interfaces and hello to organized, manageable tasks!

## Problematic
Do you find your school's interface cumbersome and frustrating? eMadariss was born out of the need to navigate a less-than-ideal school website. It aims to simplify the process of accessing and managing homework by automatically fetching assignments from the school's platform.

## Features
- **Web Scraping:** eMadariss employs web scraping techniques to extract homework details, eliminating the need for manual entry.
- **Trello Integration:** Seamlessly export fetched homework assignments to Trello boards for efficient task management.
- **Customizable Settings:** Tailor the program to your needs with customizable settings for different classes, subjects, or assignment types.

## How It Works
1. **Web Scraping:** The program logs into the school's website using your credentials and fetches homework details from the specified classes or subjects.
2. **Trello Export:** Utilizing Trello's API, eMadariss transfers the retrieved homework items into your Trello boards, categorizing them based on your preferences.

## Setup Instructions
To set up eMadariss on your system:
1. Clone the repository: `git clone https://github.com/yourusername/eMadariss.git`
2. Install required dependencies: `pip install -r requirements.txt`
3. Configure your school's website login details in the `.env` file.
5. Run the program: `python main.py`

## Contributions
Contributions are welcome! If you'd like to improve eMadariss or add new features, feel free to fork the repository and submit a pull request.

## Disclaimer
eMadariss is an independent project and is not affiliated with any specific educational institution. Use this program responsibly and in accordance with your school's policies and guidelines.

Feel free to expand upon this template with additional details, installation instructions, or any other information pertinent to your project.

Also note that this is just a fun project and I'm not responsible if you miss any of your homeworks!