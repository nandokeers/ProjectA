# Station feedback & info screens

First-year HBO-ICT project (Hogeschool Utrecht, 2022). A small system in three Python programs that lets
train travellers leave a message at a station, has a moderator review it, and shows approved messages
on a station display together with live weather and station facilities.

| Program | What it does |
|---|---|
| `Module 1.py` | **Kiosk:** a traveller enters their name (optional) and a message of max. 140 characters. It is saved to `berichten.txt` with the station and timestamp. |
| `Module 2.py` | **Moderation:** a moderator logs in, reads each pending message, approves or rejects it, and the result is stored in PostgreSQL. |
| `Module 3.py` | **Station screen:** shows the latest approved messages for a station, the current weather (OpenWeatherMap API) and the available facilities (lift, OV-fiets, P+R, toilet). |

**Tech:** Python · Tkinter · PostgreSQL (psycopg2) · OpenWeatherMap REST API · Pillow

## Security

- SQL queries are **parameterised** (`%s` placeholders), so user input cannot inject SQL.
- **No secrets in the code.** The database password, API key and moderator password are read from
  environment variables or a local `.env` file (see `config.py`). `.env` is in `.gitignore`.
  *Earlier versions of this repo had these values hardcoded. They have since been moved out of the code
  (see the commit history).*
- Weather requests use HTTPS.

## Running it

1. Install Python 3 and PostgreSQL, and create a database with the tables `bericht`, `moderator` and `station_service`.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your database password, a free
   [OpenWeatherMap](https://openweathermap.org/api) API key and a moderator password.
4. Start the programs:
   ```bash
   python "Module 1.py"   # kiosk
   python "Module 2.py"   # moderation
   python "Module 3.py"   # station screen
   ```

## What I would do differently now

This was one of my first programming projects. Looking back with my cybersecurity studies in mind:

- Moderators should have personal accounts with hashed passwords instead of one shared password.
- The kiosk should store messages directly in the database instead of a text file with a custom separator.
- Use one database connection per program, and handle errors explicitly instead of ignoring them.

---

*NL: Schoolproject HBO-ICT (2022). In module 1 laten reizigers een bericht achter, in module 2 keurt een
moderator het bericht goed of af en slaat het op in de database, en in module 3 toont een stationsscherm
de goedgekeurde berichten met het actuele weer en de faciliteiten van het station.*
