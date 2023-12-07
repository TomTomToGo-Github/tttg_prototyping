import time
import sys
import json
from pathlib import Path


def main(path=None, filename=None):
    print("Calling from:", Path.cwd())
    time.sleep(2)
    print(f"Saving file '{filename}' in:", path)
    with open(path / filename, 'w') as f:
        f.write('Hello, world!')
    data_for_js = {'content': 'Some interesting text'}
    print('Data json: ', json.dumps(data_for_js))
    return json.dumps(data_for_js)

if __name__ == '__main__':
    path = Path(json.loads(sys.argv[1]).get('path', Path.home() / 'Desktop'))
    filename = json.loads(sys.argv[1]).get('filename', 'word_result.txt')
    main(path=path, filename=filename)