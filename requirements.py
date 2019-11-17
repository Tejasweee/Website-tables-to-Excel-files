import sys

def installer(package):
    print('Installing..', package)
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    import openpyxl
    print('Openpyxl already available...')
except ImportError:
    installer('openpyxl')

try:
    import lxml
    print('lxml already available...')
except ImportError:
    installer('lxml')

try:
    import pandas
    print('Pandas already installed...')
except ImportError:
    installer('pandas')

print('All requirements satisfied...')
