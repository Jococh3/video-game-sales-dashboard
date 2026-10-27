# Video Game Sales Dashboard

[Open the live dashboard](https://video-game-sales-dashboard-d4z4scm3appquymxbhzfte.streamlit.app/)

An interactive Streamlit dashboard for exploring reported video game sales by release year, genre, and platform.

## What you can explore

Use the sidebar to select a year range and one or more genres. The dashboard updates:

- Number of games in the filtered selection
- Total and average reported global sales
- Global sales by genre and platform
- Sales by year
- A table of the 10 highest-selling games in the selected data

The default year selection is 2000–2015. The app removes rows without a year before building the filters and charts.

## Built with

Python, Streamlit, pandas, and Plotly.

## Run locally

Requires Python and the packages listed in `requirements.txt`.

```bash
git clone https://github.com/Jococh3/video-game-sales-dashboard.git
cd video-game-sales-dashboard
python -m venv .venv
```

Activate the environment, then install dependencies and start Streamlit:

```bash
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/dashboard.py
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`, then run the install and launch commands.

The app reads `data/vgsales.csv` relative to the repository root.

## Data and interpretation

The repository includes `data/vgsales.csv`, which contains game, platform, year, genre, publisher, regional sales, and global sales fields. The dashboard sums the supplied `Global_Sales` values; it does not estimate sales or adjust for inflation.

The repository currently does not document the dataset's original source, methodology, or redistribution license. Add the source citation and license before redistributing the data or presenting the values as independently verified market totals. Sales figures should be understood as reported dataset values.

## Project structure

- `app/dashboard.py` — data loading, filters, metrics, charts, and top-games table
- `data/vgsales.csv` — dashboard dataset
- `requirements.txt` — Python dependencies
