# Web-Scraper: Retail Housing Data Scraper

## Overview
This repository contains a web scraper designed to extract retail housing data from specified URLs. It fetches the data using the `requests` module, parses it with `BeautifulSoup` and `html5lib`, and stores the data in a structured JSON format. Every step, whether successful or encountering errors, is logged for easy monitoring.

Stay tuned for an upcoming project that will utilize this data to make AI-driven predictions on the housing market!

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Upcoming AI Repo](#upcoming-ai-repo)
- [Contributing](#contributing)

## Requirements
- Python 3.11.0
- `requests`
- `BeautifulSoup`
- `html5lib`
  
  Make sure to run `pip install (module)` to install the latest module needed above.

## Installation
1. Clone the repository:
```bash
git clone <REPO_URL>
cd <REPO_DIRECTORY_NAME>
```

## Usage

To utilize the scraper, execute the following command:
```bash
python scraper.py
```

## Logging

All processes, from fetching to parsing and storing data, are logged in detail. This allows users to track the scraper's activities and troubleshoot any issues that might arise during its operation.

## Upcoming AI Repo

Keep an eye out for an upcoming repository where the scraped data will be fed into an AI model to make predictions about the housing market!

## Contributing

Contributions are always welcome! Here's how you can help:

1. **Fork the Repository:** Start by forking this repository to your own GitHub account.
2. **Clone the Repository:**
    ```bash
    git clone https://github.com/zajicekn/Web-Scraper.git
    ```
3. **Navigate to the Directory and Create a New Branch for your feature or fix:**
    ```bash
    cd Web-Scraper
    git checkout -b [name_of_new_branch]
    ```
4. **Make your changes and then commit them:**
    ```bash
    git commit -m "Description of changes made"
    ```
5. **Push your changes to your fork:**
    ```bash
    git push origin [name_of_new_branch]
    ```
6. Create a Pull Request from your forked repository to the main repository.
