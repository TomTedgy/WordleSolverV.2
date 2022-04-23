import pandas as pd

read_file = pd.read_csv (r'C:\Users\Tom\Desktop\wordle_solver-main\data\FiveLetters.txt')
read_file.to_csv (r'C:\Users\Tom\Desktop\wordle_solver-main\data\words.csv', index=None)