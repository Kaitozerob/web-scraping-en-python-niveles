# 🌐 Level 1: Scraping a Static Page

This folder contains the first practice exercises of the Web Scraping in Python course by **Leonardo Kuffo**.

In this level, we learn how to:
- Make HTTP requests using `requests`
- Parse HTML using `lxml` or `BeautifulSoup`
- Extract data using XPath or CSS selectors
- Handle character encoding

---

## 🧪 Examples in This Level

<details>
<summary>1. Wikipedia Languages (wikipedia_languages.py)</summary>

This script extracts the names of languages from the [Wikipedia homepage](https://www.wikipedia.org/) using `requests` and `lxml`.

### 📄 File

```bash
level-1-static-page/wikipedia_languages.py
```

### 🧰 Tools Used

- `requests` → for sending HTTP requests
- `lxml.html` → for parsing and navigating the HTML DOM
- `XPath` → for selecting elements from the HTML structure

### ▶️ How to Run

```bash
pip install requests lxml
python wikipedia_languages.py
```

### 📦 Output Example

```
English
Español
Deutsch
Русский
Français
...
```

</details>

---

<details>
<summary>2. StackOverflow Questions (stackoverflow_questions.py)</summary>

This script scrapes the titles of the most recent questions on [StackOverflow](https://stackoverflow.com/questions) using `requests` and `BeautifulSoup`.

### 📄 File

```bash
level-1-static-page/stackoverflow_questions.py
```

### 🧰 Tools Used

- `requests`
- `beautifulsoup4`
- `lxml`

### ▶️ How to Run

```bash
pip install requests beautifulsoup4 lxml
python stackoverflow_questions.py
```

</details>

---

## 📚 Learnings

✅ How to inspect HTML and CSS structure  
✅ How to build XPath and CSS selector expressions  
✅ How to get clean text data from static HTML content

---

## 👨‍🏫 Credits

Based on the educational content by **Leonardo Kuffo**.
