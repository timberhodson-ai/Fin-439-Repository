# Project 2 — ETF allocation under a 7% hurdle

AI use: OpenAI Codex helped integrate the prior labs, run checks, and draft documentation. The student is responsible for verifying the analysis and approving the committee decision.

This is an educational exercise, not investment advice.

## Run the app

From this directory, with Python 3.14 and dependencies installed, run:

```sh
python -m streamlit run app.py
```

For first-time setup, install the dependencies with `python -m pip install -r requirements.txt`. Open the local URL printed in the terminal. The starting allocation and mandate verdicts appear on the main page. The sidebar controls the estimation window, annual cost, EEM limit, and VOO return haircut. **Frozen baseline and stress evidence** shows the reference results. The app uses the included prices and needs no market-data credentials or network calls during analysis.

Run `python -X utf8 analysis.py` to reproduce the [visible output](docs/visible-output.md) as Markdown.

- [Lab 20 DRIVER checkout](docs/lab-20.md)
- [Decision memo](docs/decision-memo.md)
- [Validation and AI use](docs/validation-and-ai-use.md)
- [Signal data card](docs/data-card.md)
- [Manifest](docs/manifest.md)
