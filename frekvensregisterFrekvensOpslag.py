import pandas as pd
import sys

def filter_rows(input_path, output_path, decimal_number):
    # Reading the input ODS file
    xls = pd.ExcelFile(input_path)

    # Initializing an empty DataFrame to store filtered rows
    filtered_data = pd.DataFrame()

    for sheet_name in xls.sheet_names:
        # Reading each sheet in the ODS file
        sheet = pd.read_excel(xls, sheet_name)

        # Filtering rows based on the condition
        condition = (
            (sheet.iloc[:, 1].apply(lambda x: is_in_range(decimal_number, x, sheet_name))) |
            (sheet.iloc[:, 2].apply(lambda x: is_in_range(decimal_number, x, sheet_name)))
        )
        filtered_rows = sheet[condition]

        # Appending the filtered rows to the result DataFrame
        filtered_data = pd.concat([filtered_data, filtered_rows], ignore_index=True)

    # Saving the filtered data to the output ODS file
    with pd.ExcelWriter(output_path, engine='odf') as writer:
        filtered_data.to_excel(writer, index=False)

def is_in_range(decimal_number, range_str, sheet_name):
    start, end = map(float, map(str.strip, range_str.replace(',', '.').split('-')))
    return ((decimal_number - start) >= 0.0 and (end - decimal_number) >= 0.0)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file.ods> <output_file.ods> <decimal_number>")
        sys.exit(1)

    # Get input and output file paths and decimal number from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    decimal_number = float(sys.argv[3])

    # Filter rows and save to the output ODS file
    filter_rows(input_file, output_file, decimal_number)
