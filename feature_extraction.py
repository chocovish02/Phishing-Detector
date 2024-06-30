import re

def extract_features(URL):
    features = {}

    # Basic features
    features['url_length'] = len(URL)  # Length of the URL
    features['num_digits'] = sum(c.isdigit() for c in URL)  # Number of digits in the URL
    features['num_special_chars'] = len(re.findall(r'\W', URL))  # Number of special characters

    # Protocol related features
    features['has_http'] = 1 if re.search(r'http://|https://', URL) else 0  # Presence of 'http://' or 'https://'
    features['has_https'] = 1 if URL.startswith('https') else 0  # Presence of 'https://' at the beginning

    # Domain related features
    segments = URL.split('/')
    domain = segments[2] if len(segments) > 2 else segments[0]
    features['num_dots'] = domain.count('.')  # Number of dots in the domain
    features['num_hyphens'] = domain.count('-')  # Number of hyphens in the domain

    # New features
    features['domain_length'] = len(domain)  # Length of the domain
    features['num_params'] = URL.count('?')  # Number of parameters in the URL
    features['path_length'] = sum(len(segment) for segment in segments[3:])  # Length of the URL path
    
    return features
