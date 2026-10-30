# Event 2 kit: Plug It In

Get fake bank accounts and transactions on screen, with your keys stored safely. All data is fake.

## Missed Event 1?

You're not behind. This kit runs on its own, so you can start at Step 1 below and join any team.

To catch up on the project, teams, and roles, read these in the [event1-catchup](event1-catchup) folder:

- [Event 1 slides](event1-catchup/Event-1-Slides.pdf): what we're building, in 5 minutes
- [Event 1 student guide](event1-catchup/Event-1-Student-Guide.pdf): roles, team tasks, and setup help

Where the guide says `[STARTER REPO LINK]`, use this repo instead.

## Step 1: Open it

1. Click **Fork** at the top of this page, then **Create fork**.
2. On your fork: **Code → Codespaces → Create codespace on main**. Wait for it to load.

## Step 2: Lock your keys

In the terminal at the bottom:

```bash
cp .env.example .env
```

Open `.env` and paste your Plaid Sandbox keys after the `=` signs. They're at dashboard.plaid.com → Developers → Keys.

No Plaid account yet? Sign up free at dashboard.plaid.com, then come back here. If that takes a while, skip the keys for now: the app uses the CSV backup and you can add them later.

Now check that git can't see the file:

```bash
git status
```

**`.env` must NOT be in the list.** If it is, stop and call someone over.

## Step 3: Run it

```bash
python -m streamlit run app.py
```

Click **Open in Browser** when it pops up. Look at the line under the title:

- `Data source: Plaid Sandbox` means you're connected.
- `Data source: CSV backup` means no keys, or Plaid said no. It tells you why.

## Bonus quests

- **Silver:** Open `app.py` and delete the `#` on the Silver Quest lines. Charts appear.
- **Gold:** Rotate your key. Make a new Sandbox secret in the Plaid dashboard, put it in `.env`, restart the app, and prove it still connects.

## Bringing it into your team repo

Copy `bank.py` and both CSV files across, add `requests` and `python-dotenv` to your requirements, and make sure your `.gitignore` has `.env` in it. Then:

```python
import bank
accounts, tx, source = bank.load_bank()
```

## Stuck?

| You see | Fix |
|---|---|
| `Plaid said: INVALID_API_KEYS` | Use the Sandbox secret, not Production. No spaces or quotes. |
| `Plaid said: INVALID_FIELD` | Your client ID is wrong. Copy it again. |
| `No module named streamlit` | `pip install -r requirements.txt` |
| You edited `.env` and nothing changed | Stop the app with Ctrl C and run it again. |
| The page won't open | Ports tab in the bottom panel, then click the globe next to 8501. |
