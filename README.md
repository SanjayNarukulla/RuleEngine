# Rule Engine with Abstract Syntax Tree (AST)

## Objective
This project is a simple 3-tier rule engine application designed to determine user eligibility based on attributes like age, department, income, and spending. It utilizes an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, and modification of these rules.

## Data Structure
The engine defines a data structure to represent the AST, which includes:
- **Node**
  - `type`: A string indicating the node type ("operator" for AND/OR, "operand" for conditions).
  - `left`: Reference to another Node (left child).
  - `right`: Reference to another Node (right child for operators).
  - `value`: An optional value for operand nodes (e.g., a number for comparisons).

## Data Storage
The project uses SQLite for storing rules and application metadata. The schema includes tables for rules and user attributes.

## Sample Rules
- `rule1`: `((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)`
- `rule2`: `((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)`

## API Design
### Functions:
1. **create_rule(rule_string)**: Converts a string representing a rule into a Node object representing the corresponding AST.
2. **combine_rules(rules)**: Combines multiple rule strings into a single AST while minimizing redundant checks.
3. **evaluate_rule(data)**: Evaluates the combined rule's AST against provided data and returns True or False based on user eligibility.

## Test Cases
1. Create individual rules from examples using `create_rule` and verify their AST representation.
2. Combine example rules using `combine_rules` and ensure the resulting AST reflects the combined logic.
3. Implement sample JSON data and test `evaluate_rule` for different scenarios.
4. Explore combining additional rules and test the functionality.

## Bonus Features
- Error handling for invalid rule strings or data formats.
- Validations for attributes as part of a catalog.
- Functionality for modifying existing rules.
- Extension for user-defined functions within the rule language.

## Installation
To run this project, clone the repository and install the necessary dependencies:

```bash
git clone <your-repo-url>
cd RuleEngine
pip install -r requirements.txt

Usage
Run the application using:

python engine.py

Testing
To run the unit tests for this project, use:

bash

python -m unittest test_engine.py
Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions.

License
This project is licensed under the MIT License.