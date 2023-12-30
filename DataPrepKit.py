import pandas as pd

class file:

    def read_csv(file_path):
        return pd.read_csv(file_path)

    def read_excel(file_path):
       return pd.read_excel(file_path)

    def read_json(file_path):
        return pd.read_json(file_path)
    
    def data_summary(data):
        summary = {
            'average_values': data.mean(),
            'most_frequent_values': data.mode().iloc[0],
        }
        return summary

    def handle_missing_values(data, strategy='remove'):
        if strategy == 'remove':
            return data.dropna()
        elif strategy == 'impute_mean':
            return data.fillna(data.mean())
        elif strategy == 'impute_median':
            return data.fillna(data.median())
        else:
            raise ValueError("Invalid missing values strategy. Supported strategies: 'remove', 'impute_mean', 'impute_median'")

    def encode_categorical(data, cols):
        return pd.get_dummies(data, columns=cols)


data = file.read_csv(r"D:\NTI\Dr.Mostafa\data.csv")
data = file.handle_missing_values(data,"remove")
summary = file.data_summary(data)
print(summary['average_values'])
encoded_data = file.encode_categorical(data,['Duration'])
print(encoded_data)