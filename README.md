# SP

A small command line body calculator written in Python. 

It asks a few questions, then shows your BMR, maintenance calories, macros, daily water, and vitamins and minerals. It can save a report.

## Run

```
python3 exec.py
```
or 
```
cd  ~/<PATH>/SP_fitness && ./exec.py
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

Calories, protein, fat and water, checked against published ranges:

- Protein 1.6-2.2 g/kg to build muscle and 2.3-3.1 g/kg when cutting: [ISSN protein position stand](https://pmc.ncbi.nlm.nih.gov/articles/PMC5477153/), [Helms 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4033492/), [Morton 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5867436/)
- Fat 0.5-1.5 g/kg and a surplus of 10-20% when bulking: [Iraki 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680710/)
- Weight loss of 0.5-1% of body weight per week: [ISSN diets and body composition](https://pmc.ncbi.nlm.nih.gov/articles/PMC5470183/)
- Water: the EFSA adequate intake of total water is 2.5 L for men and 2.0 L for women. The extra water for workouts is an estimate.
- The activity multipliers are rules of thumb. [FAO/WHO/UNU](https://www.fao.org/3/y5686e/y5686e07.htm) uses different values and says they are for groups, not individuals.

## Note

This is general information, not medical advice. ALWAYS SEARCH IN GOOGLE and Contact a doctor if you're facing any kind of medical issues . 
and the important thing is to accept yourself , if you cannot then try to improve it step by step. it's about the journey, enjoy your adventure. 
any contribution is acceptable (MIT license) 
