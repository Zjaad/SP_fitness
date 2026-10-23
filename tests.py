#!/usr/bin/python3
import unittest

from goal_calculator import Goal
from macros import Macro , minCarb
from Water_in import Water
from units import convert , fromMetric , units
from vitamins import needs , notes , ageGroup
from splits import splits


def man(goal):
    return Goal('t' , 27 , 'male' , 'x' , 90 , 177 , 6 , goal)


class TestGoal(unittest.TestCase):

    def test_bmr_male(self):
        self.assertEqual(man('cut').BMR() , 1876.25)

    def test_bmr_female(self):
        woman = Goal('w' , 25 , 'female' , 'x' , 70 , 160 , 1 , 'maintenance')
        self.assertEqual(woman.BMR() , 1414)

    def test_wrong_gender_raises(self):
        with self.assertRaises(ValueError):
            Goal('x' , 25 , 'banana' , 'x' , 70 , 160 , 1).BMR()

    def test_activity_multipliers(self):
        expected = {0 : 1.2 , 1 : 1.2 , 2 : 1.375 , 3 : 1.375 , 4 : 1.55 , 5 : 1.55 , 6 : 1.73 , 7 : 1.73 , 8 : 1.9}
        for activity , multiplier in expected.items():
            user = Goal('t' , 27 , 'male' , 'x' , 90 , 177 , activity , 'maintenance')
            self.assertAlmostEqual(user.maintenance() , 1876.25 * multiplier)

    def test_goal_calories(self):
        maintenance = man('maintenance').adj_cal()
        self.assertAlmostEqual(man('cut').adj_cal() , maintenance - 400)
        self.assertAlmostEqual(man('gain').adj_cal() , maintenance + 400)
        self.assertAlmostEqual(man('dirty bulk').adj_cal() , maintenance + 800)
        self.assertAlmostEqual(man('minicut').adj_cal() , maintenance / 2 + 300)

    def test_goal_aliases_match(self):
        self.assertEqual(man('bulk').adj_cal() , man('gain').adj_cal())
        self.assertEqual(man('dirtybulk').adj_cal() , man('dirty bulk').adj_cal())
        self.assertEqual(man('supercut').adj_cal() , man('minicut').adj_cal())
        self.assertEqual(man('').adj_cal() , man('maintenance').adj_cal())
        self.assertEqual(man('BULK').adj_cal() , man('gain').adj_cal())

    def test_unknown_goal_raises(self):
        with self.assertRaises(ValueError):
            man('banana').adj_cal()


class TestMacro(unittest.TestCase):

    def test_every_goal_word_works(self):
        for goal in ['' , 'maintenance' , 'cut' , 'minicut' , 'supercut' , 'gain' , 'bulk' , 'dirty bulk' , 'dirtybulk']:
            Macro(3000 , 80 , goal).allMacros()

    def test_unknown_goal_raises(self):
        with self.assertRaises(ValueError):
            Macro(3000 , 80 , 'banana').protein()

    def test_normal_bulk_is_untouched(self):
        carbg , carbCal = Macro(2674.625 , 50 , 'gain').carb()
        self.assertAlmostEqual(carbg , 416.78125)
        self.assertAlmostEqual(carbCal , 1667.125)

    def test_low_carb_bulk_is_raised_to_minimum(self):
        macro = Macro(1900 , 90 , 'gain')
        self.assertEqual(macro.carb() , (minCarb , minCarb * 4))
        total = macro.protein()[1] + macro.carb()[1] + macro.fat()[1]
        self.assertGreater(total , 1900)

    def test_low_carb_cut_is_raised_too(self):
        self.assertEqual(Macro(1500 , 90 , 'cut').carb()[0] , minCarb)

    def test_aggressive_cut_keeps_low_carbs(self):
        self.assertAlmostEqual(Macro(1923 , 90 , 'minicut').carb()[0] , 64.5)

    def test_aggressive_cut_never_goes_negative(self):
        self.assertEqual(Macro(1390.5 , 90 , 'minicut').carb() , (0 , 0))
        self.assertEqual(Macro(1000 , 90 , 'supercut').carb() , (0 , 0))

    def test_grams_per_kg(self):
        macro = Macro(3000 , 80 , 'gain')
        self.assertEqual(macro.protein()[0] , 160)
        self.assertAlmostEqual(macro.fat()[0] , 108)

    def test_total_calories_has_two_decimals(self):
        text = Macro(2674.625 , 50 , 'gain').allMacros()[0]['total calories']
        self.assertEqual(text , '2674.62 kcal')


class TestWater(unittest.TestCase):

    def make(self , activity , goal):
        return Water('t' , 27 , 'male' , 'x' , 90 , 177 , activity , goal)

    def test_water_with_workouts(self):
        self.assertEqual(self.make(6 , 'gain').calc() , 90 * 35 + 700)

    def test_water_without_workouts(self):
        self.assertEqual(self.make(0 , 'cut').calc() , 90 * 35)

    def test_dirty_bulk_uses_130_minutes(self):
        self.assertEqual(self.make(6 , 'dirty bulk').calc() , 90 * 35 + 1400)
        self.assertEqual(self.make(6 , 'dirtybulk').calc() , 90 * 35 + 1400)

    def test_goal_survives(self):
        self.assertEqual(self.make(6 , 'gain').GOAL , 'gain')

    def test_str(self):
        self.assertIn('3850' , str(self.make(6 , 'gain')))


class TestUnits(unittest.TestCase):

    def test_pounds(self):
        self.assertAlmostEqual(convert(150 , 'lb') , 68.0389 , places = 3)

    def test_feet_and_inches(self):
        self.assertAlmostEqual(convert(5 , 'ft') + convert(10 , 'in') , 177.8)

    def test_round_trips(self):
        for unit in units:
            self.assertAlmostEqual(fromMetric(convert(123.4 , unit) , unit) , 123.4)

    def test_kilojoules(self):
        self.assertAlmostEqual(fromMetric(2000 , 'kJ') , 8368 , places = 0)

    def test_unknown_unit_raises(self):
        with self.assertRaises(KeyError):
            convert(1 , 'stone')

    def test_table_is_complete(self):
        for unit , info in units.items():
            self.assertGreater(info['factor'] , 0)
            self.assertIn(info['metric'] , ['kg' , 'cm' , 'g' , 'ml' , 'kcal'])


class TestVitamins(unittest.TestCase):

    def test_age_groups(self):
        expected = {12 : '9-13' , 13 : '9-13' , 14 : '14-18' , 18 : '14-18' , 19 : '19-30' , 30 : '19-30' ,
                    31 : '31-50' , 50 : '31-50' , 51 : '51-70' , 70 : '51-70' , 71 : '71+' , 100 : '71+'}
        for age , group in expected.items():
            self.assertEqual(ageGroup(age) , group)

    def test_known_values(self):
        self.assertEqual(needs('male' , 30)['Vitamin C']['target'] , 90)
        self.assertEqual(needs('female' , 30)['Vitamin C']['target'] , 75)
        self.assertEqual(needs('female' , 25)['Iron']['target'] , 18)
        self.assertEqual(needs('female' , 72)['Iron']['target'] , 8)
        self.assertEqual(needs('male' , 80)['Vitamin D']['target'] , 20)
        self.assertEqual(needs('male' , 30)['Potassium']['target'] , 3400)
        self.assertEqual(needs('female' , 30)['Potassium']['target'] , 2600)

    def test_kinds_and_limits(self):
        man = needs('male' , 30)
        self.assertEqual(man['Vitamin C']['kind'] , 'RDA')
        self.assertEqual(man['Vitamin K']['kind'] , 'AI')
        self.assertIsNone(man['Potassium']['max'])
        self.assertEqual(man['Magnesium']['max'] , 350)
        self.assertEqual(man['Sodium']['max'] , 2300)

    def test_everybody_has_everything(self):
        for gender in ['male' , 'female']:
            for age in [12 , 15 , 25 , 40 , 60 , 80]:
                table = needs(gender , age)
                self.assertEqual(len(table) , 28)
                for nutrient , v in table.items():
                    self.assertGreater(v['target'] , 0 , nutrient)

    def test_notes_only_when_they_apply(self):
        self.assertTrue(any('Vitamin D' in n for n in notes('male' , 30)))
        self.assertFalse(any('B12' in n for n in notes('male' , 30)))
        self.assertTrue(any('B12' in n for n in notes('male' , 60)))
        self.assertTrue(any('folate' in n for n in notes('female' , 25)))
        self.assertFalse(any('folate' in n for n in notes('male' , 25)))
        self.assertFalse(any('folate' in n for n in notes('female' , 60)))


class TestSplits(unittest.TestCase):

    def test_every_split_is_complete(self):
        for name , info in splits.items():
            self.assertIsInstance(info['days'] , int , name)
            self.assertIsInstance(info['schedule'] , str , name)

    def test_custom_is_last_and_has_no_days(self):
        self.assertEqual(list(splits)[-1] , 'Custom (personal)')
        self.assertEqual(splits['Custom (personal)']['days'] , 0)

    def test_real_splits_have_1_to_7_days(self):
        for name , info in splits.items():
            if name != 'Custom (personal)':
                self.assertIn(info['days'] , range(1 , 8) , name)


if __name__ == '__main__':
    unittest.main()
