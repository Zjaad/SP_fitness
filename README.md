# SP

A small command-line body calculator written in Python.

It asks a few questions, then shows your BMR, maintenance calories, macros, daily water, and vitamins and minerals. It can save a report.

## Run

```
python3 exec.py
```

Python 3 only. No libraries to install.

## Test

```
python3 -m unittest tests
```

## What it does

- BMR (Mifflin-St Jeor) and maintenance calories, from your workouts per week
- Goals: maintenance, cut, minicut, gain, dirty bulk
- Macros (protein, carbs, fat), with a carb minimum on bulks
- Water per day
- Vitamins and minerals (28 nutrients) by sex and age
- Metric or US units
- Workout split menu, with a custom option
- Saves a text report when you exit, and a JSON report if you ask for it

## Files

| File | What it does |
|---|---|
| `exec.py` | the app: questions, menu, reports |
| `pd.py` | `Person` and `TDEERMB` (BMR and maintenance) |
| `goal_calculator.py` | `Goal`: calories for each goal |
| `macros.py` | `Macro`: protein, carbs, fat |
| `Water_in.py` | `Water`: daily water |
| `units.py` + `internationalUnits.json` | unit conversion |
| `splits.py` + `splits.json` | workout splits |
| `vitamins.py` + `vitaminsMinerals.json` | vitamins and minerals |
| `cli.py` | colors, banner, frames |
| `tests.py` | automatic tests |
| `testpd.py` | manual test script |
| `VitaRDA.py` | the first vitamins list (old) |
| `Design/` | notes on the structure |

To add a unit or a split, add a line to its JSON file.

## Sources

Vitamins and minerals: [Dietary Reference Intakes Summary Tables](https://nap.nationalacademies.org/read/25353/chapter/28), National Academies, 2019.

## Note

This is general information, not medical advice.
