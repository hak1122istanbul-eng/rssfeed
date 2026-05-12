import json
import sys
import os

CATEGORIES_PATH = "docs/data/categories.json"

def main():
    if not os.path.exists(CATEGORIES_PATH):
        print(f"Error: {CATEGORIES_PATH} not found.")
        sys.exit(1)
        
    with open(CATEGORIES_PATH, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format: {e}")
            sys.exit(1)
            
    if 'categories' not in data:
        print("Missing 'categories' key.")
        sys.exit(1)
        
    for cat in data['categories']:
        for key in ['id', 'label', 'color', 'keywords']:
            if key not in cat:
                print(f"Category missing key: {key} in {cat}")
                sys.exit(1)
                
    print("Categories validation passed.")

if __name__ == "__main__":
    main()
