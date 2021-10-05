# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV qualifying loans.

"""
import csv
from pathlib import Path





header = ['bank_data', 'credit_score', 'debt', 'income', 'loan', 'home_value']

out_path = Path("save_qualifying_loans.csv")

def save_cs():
    """Saves the CSV files from path provided.
    Args:
        csvpath (path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
        geader (list): An optional header for the CSV
    
    """
with open( out_path, 'w', newline= '') as savefile:
        data = []       
        csvwriter = csv.writer(savefile)
        csvwriter.writerow(header)
        for row in data:
            csvwriter.writerow(row.values())
    
