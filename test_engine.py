import unittest
from engine import RuleEngine  # Import RuleEngine from engine.py

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        # Define your rules here
        self.rules = [
            ["age > 30", "department == 'Sales'"],
            ["age < 25", "department == 'Marketing'"]
        ]

        # Sample data to evaluate against the rules
        self.data_set = [
            {"age": 35, "department": "Sales"},
            {"age": 22, "department": "Marketing"},
            {"age": 40, "department": "Sales"},
            {"age": 29, "department": "HR"},
            {"age": 20, "department": "Marketing"}
        ]

        # Initialize the RuleEngine with the rules
        self.rule_engine = RuleEngine(self.rules)

    def test_evaluate_rule(self):
        expected_results = [
            [True, False],  # Data 1
            [False, True],  # Data 2
            [True, False],  # Data 3
            [False, False], # Data 4
            [False, True]   # Data 5
        ]

        for i, data in enumerate(self.data_set):
            for j, rule in enumerate(self.rules):
                rule_result = self.rule_engine.evaluate_rule(rule, data)
                self.assertEqual(rule_result, expected_results[i][j],
                                 f"Failed for Data {i + 1} with Rule {j + 1}")

    def test_evaluate_combined_rule(self):
        combined_expected_results = [
            True,  # Data 1
            True,  # Data 2
            True,  # Data 3
            False, # Data 4
            True   # Data 5
        ]

        for i, data in enumerate(self.data_set):
            combined_result = self.rule_engine.evaluate_combined_rule(self.rules, data)
            self.assertEqual(combined_result, combined_expected_results[i],
                             f"Combined rule evaluation failed for Data {i + 1}")

    def test_invalid_condition(self):
        with self.assertRaises(ValueError):
            self.rule_engine.parse_condition("invalid_condition")

        with self.assertRaises(ValueError):
            self.rule_engine.evaluate_condition("unknown_key > 30", {"age": 25})

if __name__ == '__main__':
    unittest.main()
