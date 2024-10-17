class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def evaluate_condition(self, condition, data):
        key, operator, value = self.parse_condition(condition)

        if key not in data:
            raise ValueError(f"Key '{key}' not found in data")
        
        # Convert value to numeric if the data type is numeric
        if isinstance(data[key], (int, float)):
            numeric_value = float(value)
        else:
            numeric_value = value

        # Evaluate based on the operator
        if operator == '>':
            return data[key] > numeric_value
        elif operator == '<':
            return data[key] < numeric_value
        elif operator == '==':
            return data[key] == numeric_value
        else:
            raise ValueError(f"Unknown operator '{operator}' in condition")

    def parse_condition(self, condition):
        for operator in ['>', '<', '==']:
            if operator in condition:
                key, value = condition.split(operator, 1)
                return key.strip(), operator, value.strip().strip("'\"")
        raise ValueError(f"Invalid condition format: '{condition}'")

    def evaluate_rule(self, rule, data):
        return all(self.evaluate_condition(condition, data) for condition in rule)

    def evaluate_combined_rule(self, rules, data):
        return any(self.evaluate_rule(rule, data) for rule in rules)
