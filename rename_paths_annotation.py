import pandas as pd
import re

# Переписывает пути для картинок в нужный формат
def rename_paths(data):
        return 'images/' + re.findall(r'[^\\]+\.*$', data)[0]

if __name__ == "__main__":
    data = pd.read_csv('./annotation.csv', sep=';') 
    data['image_path_new'] = data.image_path.apply(rename_paths)
    data = data.drop('image_path', axis=1).rename(columns={'image_path_new': 'image_path'})
    data.to_csv('./annotation.csv', sep=';', encoding='utf-8-sig', index=False)
