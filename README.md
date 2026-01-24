# Doncaster Rovers Analytics Dashboard

This repository contains a data-driven analytics dashboard for analysing Doncaster Rovers’ performances in EFL League One. The dashboard compares **underlying performance** with **match outcomes**, helping to identify where results reflect the process on the pitch — and where they diverge.

The application is built using **Streamlit** and is designed as an exploratory tool for performance analysis, visualisation, and insight generation.

---

## Dashboard Overview

The dashboard is organised into three sections:

### Overview
Introduces the dashboard and explains how charts should be interpreted (including quadrant-based scatter plots).

### Performance
Assesses the *process* behind performances using:
- **Frequency** — how often shots are created and conceded.
- **Quality** — the standard of chances, using expected goals (**xG**) and expected goals against (**xGA**).

The dashboard also includes a **Performance Tracker**, showing rolling six-match averages of **xG**, **xGA**, and **xGD** across the season to highlight trends over time.
A **Justice League** view ranks teams by **expected points per game (xPts/Game)** to show how the table might look if underlying performances were consistently converted into results.


### Outcomes
Focuses on what happens on the scoreboard:
- Goals scored per game
- Goals conceded per game

This allows outcomes to be compared with performance to highlight potential over- or under-performance.

---

## Design & Layout

- Dark theme configured via `.streamlit/config.toml`
- Modular page structure (each page has its own `render()` function)
- Lightweight custom CSS for tabs/cards/layout
- Responsive layout behaviour for smaller screens
- Full-width visualisations to preserve readability of scatter plots and labels

---

## Project Structure

    .
    ├── dashboard.py              # Main Streamlit app (tabs + routing)
    ├── styles/
    │   └── base.css              # Custom CSS styling
    ├── src/
    │   ├── overview.py           # Overview page (render)
    │   ├── performance.py        # Performance page (render)
    │   ├── outcomes.py           # Outcomes page (render)
    │   ├── plots.py              # Plot helpers
    │   └── styles.py             # CSS loader utility
    ├── data/                     # Data files (not all tracked)
    └── .streamlit/
        └── config.toml           # Streamlit theme configuration

---

## Running the App Locally

1) Clone the repository:

    git clone https://github.com/dave-harvey/drfc-dashboard.git
    cd drfc-dashboard

2) Install dependencies:

    pip install -r requirements.txt

3) Run the Streamlit app:

    streamlit run dashboard.py

---

## Notes

- The dashboard displays the data cut-off date within the UI.
- This project is intended for analysis and exploration rather than prediction.
- Styling/layout are optimised for desktop/laptop but remain usable on smaller screens.

