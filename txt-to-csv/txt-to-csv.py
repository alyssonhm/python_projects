# converte txt para csv
# https://stackoverflow.com/questions/39642082/convert-txt-to-csv-python-script
import pandas as pd
df = pd.read_fwf('log.txt')
df.to_csv('log.csv')

# https://datatofish.com/convert-text-file-to-csv-using-python-tool-included/
import pandas as pd
read_file = pd.read_csv (r'Path where the Text file is stored\File name.txt')
read_file.to_csv (r'Path where the CSV will be saved\File name.csv', index=None)
