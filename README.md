# 🌐 Nivel 1: Scraping a Static Page

This folder contains the first practice exercise of the Web Scraping in Python course by **Leonardo Kuffo**.

In this level, we learn how to:
- Make HTTP requests using `requests`
- Parse HTML using `lxml`
- Extract data using XPath
- Handle character encoding

---

## 🧪 Example: Wikipedia Languages

We extract the language names (like English, Español, Русский...) from the main page of [Wikipedia.org](https://www.wikipedia.org/).

### 📄 File

```bash
level-1-static-page/wikipedia_languages.py
```

### 🧰 Tools Used

- `requests` → for sending HTTP requests
- `lxml.html` → for parsing and navigating the HTML DOM
- `XPath` → for selecting elements from the HTML structure

---

## ▶️ How to Run

Make sure you have the required libraries installed:

```bash
pip install requests lxml
```

Then run the script:

```bash
python wikipedia_languages.py
```

You should see a list of languages printed in the terminal.

---

## 📦 Output Example

```
English
Español
Deutsch
Русский
Français
...
```

---

## 📚 Learnings

✅ How to inspect HTML structure  
✅ How to build XPath expressions  
✅ How to get clean text data from a static HTML file

---

## 👨‍🏫 Credits

Based on the educational content by **Leonardo Kuffo**.
