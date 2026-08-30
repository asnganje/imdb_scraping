# IMDb Movie Data Scraper

A **Python Selenium-based web scraping project** for collecting movie records from the [IMDb](https://www.imdb.com/) website.

The project automates the collection of movie information from IMDb and saves the results into an Excel file for further analysis.

## Features

The scraper collects the following movie information:

* **Movie Name**
* **Release Year**
* **Duration**
* **Stars**
* **Number of Votes**
* **Metascore**
* **Description**

A total of **1,065 movie records** were successfully scraped and saved to an Excel file.

## Requirements

Before running the project, make sure you have:

* **Python 3.14.7**
* **uv 0.12.5**
* **Internet connection**
* A working web browser supported by Selenium

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <project-directory>
```

Install the project dependencies using `uv`:

```bash
uv sync
```

## How to Run

Start the scraper from your terminal:

```bash
uv run python main.py
```

### Manual Human Verification

Because IMDb may require human verification during automated browsing, the scraper requires a short manual step:

1. Run the scraper using the command above.
2. The Selenium-controlled browser will open IMDb.
3. Complete the **manual human verification** displayed on the website.
4. Once IMDb has loaded successfully, return to the terminal.
5. Press **Enter** to allow the scraper to continue.
6. The scraper will automatically begin collecting the movie records.
7. Wait for the scraping process to finish.
8. Open the generated **Excel file** to view the collected data.

## Output

The scraper generates an Excel file containing the collected movie records.

Each record contains:

| Field         | Description                           |
| ------------- | ------------------------------------- |
| `name`        | Movie title                           |
| `year`        | Movie release year                    |
| `duration`    | Movie runtime                         |
| `stars`       | Main cast/stars                       |
| `votes`       | Number of IMDb votes                  |
| `metascore`   | IMDb/Metascore rating where available |
| `description` | Movie description/plot summary        |

## Project Workflow

The general scraping workflow is:

```text
Start Script
     ↓
Open IMDb with Selenium
     ↓
Manual Human Verification
     ↓
Press Enter in Terminal
     ↓
Load Movie Records
     ↓
Visit Movie Pages
     ↓
Extract Movie Information
     ↓
Store Records
     ↓
Export to Excel
```

## Technologies Used

* **Python**
* **Selenium**
* **Pandas**
* **OpenPyXL**
* **uv**
* **Chrome / Selenium WebDriver**

## Results

The project successfully collected:

**1,065 movie records**

The extracted data was structured and exported into an **Excel spreadsheet** for easy viewing and further analysis.

## Disclaimer

This project is intended for **learning and demonstration purposes**, particularly for practicing Python, Selenium, browser automation, web scraping, and data processing.

When scraping websites, always respect the website's terms of service, robots.txt where applicable, rate limits, and applicable laws.
