import json
import re

def load_categories(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def classify_item(item, categories_config):
    matching_rule = categories_config.get('matching_rule', {})
    fields = matching_rule.get('fields', ['title', 'description'])
    case_sensitive = matching_rule.get('case_sensitive', False)
    multi_match = matching_rule.get('multi_match', True)
    
    matched = []
    
    text_to_search = ""
    for field in fields:
        if field in item and item[field]:
            text_to_search += " " + item[field]
            
    if not case_sensitive:
        text_to_search = text_to_search.lower()
        
    for category in categories_config.get('categories', []):
        keywords = category.get('keywords', [])
        for keyword in keywords:
            search_keyword = keyword if case_sensitive else keyword.lower()
            if search_keyword in text_to_search:
                matched.append(category['label'])
                break # Found one keyword for this category
                
    if not multi_match and matched:
        return [matched[0]]
        
    return matched
