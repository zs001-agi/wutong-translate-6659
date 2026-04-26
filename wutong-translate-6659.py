import argparse
import requests
import json

def translate_text(text, target_lang):
    api_key = 'your_api_key_here'
    url = f'https://translation.googleapis.com/language/translate/v2?key={api_key}'
    data = {
        'q': text,
        'target': target_lang
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()['data']['translations'][0]['translatedText']
    else:
        raise Exception(f"Error: {response.text}")

def main():
    parser = argparse.ArgumentParser(description='CLI translator using free API')
    parser.add_argument('text', help='The text to translate')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--output', type=argparse.FileType('w'), default=None, help='Write output to a file')
    args = parser.parse_args()

    try:
        translated_text = translate_text(args.text, 'en')  # Translate to English by default
        if args.json:
            result = {'original': args.text, 'translated': translated_text}
            print(json.dumps(result))
        else:
            print(translated_text)
        
        if args.output:
            args.output.write(translated_text)
    except Exception as e:
        parser.error(str(e))

if __name__ == '__main__':
    main()