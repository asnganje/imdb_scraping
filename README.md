# IMDb Movie Data Scraper 🎬

A **Selenium-based Python web scraping project** for collecting structured movie data from the [IMDb](https://www.imdb.com/) website.

The project uses Selenium to interact with IMDb's dynamic web interface, perform advanced movie searches, apply filters, navigate through all available movie results, extract movie information, and export the collected records to an Excel spreadsheet.

## 🚀 Features

### 🎬 Movie Data Extraction

The scraper collects the following information for each movie:

* **Movie Name**
* **Release Year**
* **Duration**
* **Stars**
* **Number of Votes**
* **Metascore**
* **Description**

### 🔎 Advanced Movie Search

The project implements advanced movie searching using Selenium.

Movies can be searched and filtered using multiple criteria, including:

* **Movie name**
* **Genre**
* **Awards**

For example:

```text
Movie Name: [Search term]
Genre: Comedy
Awards: Oscar Nominated
```

Selenium interacts with IMDb's search interface, applies the selected filters, loads the matching results, and processes the movie records.

### 📄 Automatic Pagination

The scraper is also capable of navigating through multiple pages of IMDb search results.

Instead of processing only the first page, Selenium:

1. Detects the **Next** button.
2. Clicks the button automatically.
3. Waits for the next set of movie results to load.
4. Processes the newly loaded movies.
5. Continues clicking **Next**.
6. Repeats the process until all available movie results have been processed.

This allows the scraper to collect movie records across multiple pages without requiring manual navigation.

### 🤖 Browser Automation

The project demonstrates practical Selenium browser automation, including:

* Opening IMDb in a browser
* Interacting with search fields
* Selecting search filters
* Clicking buttons and interface elements
* Handling dynamically loaded content
* Detecting and clicking pagination controls
* Navigating through multiple result pages
* Navigating between search results and movie detail pages
* Extracting structured movie information
* Exporting collected data to Excel

## 📊 Scraping Results

The scraper successfully collected:

### **1,065 movie records**

The collected records were structured and saved into an **Excel (.xlsx) file**.

Each movie record contains fields such as:

| Field         | Description               |
| ------------- | ------------------------- |
| `name`        | Movie title               |
| `year`        | Movie release year        |
| `duration`    | Movie runtime             |
| `stars`       | Main cast/stars           |
| `votes`       | Number of IMDb votes      |
| `metascore`   | Metascore where available |
| `description` | Movie description         |

## 🛠️ Technologies Used

* **Python 3.14.7**
* **Selenium**
* **Pandas**
* **OpenPyXL**
* **uv 0.12.5**
* **Chrome / Selenium WebDriver**
* **Excel (.xlsx)**

## 📋 Requirements

Before running the project, make sure you have:

* Python **3.14.7**
* uv **0.12.5**
* Google Chrome or a compatible browser
* A working Selenium WebDriver setup
* Internet connection

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd <project-directory>
```

Install the project dependencies using `uv`:

```bash
uv sync
```

## ▶️ Running the Scraper

Run the main Python script:

```bash
uv run python main.py
```

Alternatively, if your environment is already configured:

```bash
python main.py
```

## 🧑‍💻 Manual Human Verification

IMDb may occasionally require human verification when the automated browser accesses the website.

The project therefore includes a manual verification step.

### Process

1. Start the scraper from the terminal.
2. Selenium opens IMDb in the browser.
3. Complete the **human verification** displayed by IMDb.
4. Wait until the IMDb page has successfully loaded.
5. Return to the terminal.
6. Press **Enter**.
7. The automated scraping process will continue.
8. Selenium performs the search and applies the selected filters.
9. The scraper navigates through the available result pages.
10. Movie information is extracted.
11. The collected records are saved to an Excel file.

> **Note:** The manual verification step is intentional. It allows the user to complete IMDb's verification before the automated collection continues.

## 🔄 Scraping Workflow

```text
Start Application
       │
       ▼
Open IMDb with Selenium
       │
       ▼
Manual Human Verification
       │
       ▼
Press Enter in Terminal
       │
       ▼
Perform Advanced IMDb Search
       │
       ▼
Apply Search Filters
       │
       ├── Movie Name
       ├── Genre
       └── Awards
       │
       ▼
Load Movie Results
       │
       ▼
Click "Next"
       │
       ▼
Load Next Results Page
       │
       ▼
Repeat Until All Pages Are Processed
       │
       ▼
Visit Movie Detail Pages
       │
       ▼
Extract Movie Data
       │
       ▼
Store Structured Records
       │
       ▼
Export to Excel
```

## 📁 Output

After the scraping process is completed, an Excel file is generated containing the collected movie records.

The Excel output can be opened using:

* Microsoft Excel
* LibreOffice Calc
* Google Sheets
* Other spreadsheet applications supporting `.xlsx` files

## 💡 Skills Demonstrated

This project demonstrates practical experience with Python, Selenium, web scraping, browser automation, and data processing.

### Python

* Functions
* Loops
* Exception handling
* Data structures
* File handling
* Package management with `uv`

### Selenium

* WebDriver automation
* CSS selectors
* XPath selectors
* Finding and interacting with elements
* Clicking buttons
* Filling search fields
* Browser navigation
* Handling dynamic content
* Waiting for elements
* Handling pagination
* Automating repeated clicks
* Navigating between search results and detail pages

### Web Scraping

* Extracting structured information from dynamic websites
* Performing advanced searches
* Applying multiple search filters
* Navigating through paginated results
* Visiting individual movie detail pages
* Collecting data across multiple pages
* Handling dynamically loaded movie content
* Automating multi-step scraping workflows

### Data Processing

* Structuring scraped records
* Managing collections of movie data
* Processing data with Pandas
* Exporting data to Excel with OpenPyXL

## 📈 Project Outcome

The project demonstrates an end-to-end automated movie data collection workflow:

```text
IMDb
  ↓
Selenium Browser Automation
  ↓
Advanced Search
  ↓
Genre & Awards Filtering
  ↓
Pagination Handling
  ↓
Movie Detail Pages
  ↓
Data Extraction
  ↓
Pandas / OpenPyXL
  ↓
Excel Dataset
```

### Final Result

**1,065 movie records successfully scraped and saved to Excel.**

The project demonstrates the ability to build a Selenium scraper capable of interacting with a dynamic website, performing searches, handling pagination, visiting individual records, extracting structured information, and producing a usable dataset.

## ⚠️ Disclaimer

This project was created for **educational and portfolio purposes** to demonstrate Python, Selenium, browser automation, web scraping, and data processing skills.

When scraping websites, users should respect the website's terms of service, applicable usage policies, rate limits, and relevant laws.
