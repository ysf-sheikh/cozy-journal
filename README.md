# Cozy Journal

A cozy, mood-driven digital journal built with Streamlit.

Cozy Journal transforms daily journaling into a calm and reflective experience. Each day begins with a simple question: **How was today?** After rating the day from 1 to 5 stars, users can capture their thoughts, summarize their emotions, and preserve memories in a clean, searchable journal.

Unlike traditional productivity-focused applications, Cozy Journal is designed to encourage mindfulness, reflection, and consistency through a warm and immersive interface inspired by cozy nighttime aesthetics.

---

## Features

### Daily Mood Rating

Rate each day on a simple five-star scale before writing your entry.

The selected mood influences the overall atmosphere of the application, creating a personalized journaling experience.

### Dynamic Themes

The interface adapts to your mood rating.

Examples:

| Rating  | Theme                   |
| ------- | ----------------------- |
| 5 Stars | Warm glowing room       |
| 4 Stars | Cozy evening ambience   |
| 3 Stars | Calm neutral night      |
| 2 Stars | Quiet cloudy atmosphere |
| 1 Star  | Rainy window reflection |

### Daily Reflection

Complete the prompt:

> Today felt like...

This single sentence acts as a snapshot of the day and becomes a quick way to revisit past emotions and memories.

### Full Journal Entry

Write a detailed diary entry describing your day, thoughts, experiences, achievements, or challenges.

### Journal History

Browse previous entries like turning through the pages of a personal diary.

Each entry stores:

- Date
- Mood rating
- Daily summary
- Full reflection

### Local-First Storage

Entries are stored locally using structured JSON files.

No accounts.

No cloud services.

No data collection.

Your journal remains yours.

### Smooth User Experience

- Soft transitions
- Gentle animations
- Cozy visual design
- Minimal distractions
- Reflection-focused workflow

---

## Project Structure

```text
cozy-journal/
│
├── app.py
├── assets/
│   ├── cozy_room.jpg
│   ├── night_room.jpg
│   └── rainy_window.jpg
│
├── data/
│   └── entries.json
│
├── utils/
│   ├── storage.py
│   ├── themes.py
│   └── helpers.py
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technology Stack

- Python
- Streamlit
- JSON
- HTML/CSS Styling
- Pillow (Image Handling)

---

## Goals

This project was built to explore:

- Streamlit application development
- Frontend design using Python
- Local data persistence
- User-centered application design
- Personal software development outside traditional cybersecurity and finance projects

---

## Future Enhancements

- Search previous entries
- Monthly mood statistics
- Entry tagging system
- Password-protected journals
- Markdown support
- Multiple theme packs
- Export journal to PDF

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/ysf-sheikh/cozy-journal
cd cozy-journal
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Philosophy

Most software is designed to make people faster.

Cozy Journal is designed to help people slow down.

Instead of tracking tasks, goals, or productivity metrics, it creates a small daily ritual: rate the day, write a few thoughts, and leave behind a page of your story.
