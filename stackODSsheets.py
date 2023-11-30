import pandas as pd
import sys

def split_range(range_str):
    # Function to split a range string into two values
    start, end = map(int, range_str.split('-'))
    return start, end

def process_sheet(sheet, skip_first_row=False):
    # Function to process a single sheet
    # Assuming the second and third columns contain ranges
    # and the result should be in emit1, emit2, receive1, receive2 columns

    # Handling the case where sheet is a DataFrame or a sheet name
    if isinstance(sheet, pd.DataFrame):
        ranges_data = sheet.iloc[:, [1, 2]]
        # Splitting the ranges into four columns
        sheet[['emit1', 'emit2']] = pd.DataFrame(ranges_data.iloc[:, 0].apply(split_range).tolist(), index=sheet.index)
        sheet[['receive1', 'receive2']] = pd.DataFrame(ranges_data.iloc[:, 1].apply(split_range).tolist(), index=sheet.index)

        # Dropping the original columns with ranges
        sheet = sheet.drop(sheet.columns[[1, 2]], axis=1)

        # Skip the first row for sheets other than the first one
        if skip_first_row and sheet.index[0] == 0:
            sheet = sheet.iloc[1:]
    else:
        # When sheet is a sheet name (string), we don't process it
        sheet = pd.read_excel(input_file, sheet_name=sheet)

    return sheet

def stack_sheets(file_path):
    # Function to stack the contents of multiple sheets in an ODS file
    # and apply the processing to each sheet

    # Reading the ODS file
    xls = pd.ExcelFile(file_path)

    # Handling single-sheet scenario
    if len(xls.sheet_names) == 1:
        # If there is only one sheet, process it directly
        stacked_data = process_sheet(xls.sheet_names[0])
    else:
        # Stacking the sheets
        stacked_data = pd.concat([process_sheet(sheet, skip_first_row=(i != 0)) for i, sheet in enumerate(xls.sheet_names)], ignore_index=True)

    return stacked_data

def save_to_ods(data, output_path):
    # Function to save the processed data to a new ODS file
    with pd.ExcelWriter(output_path, engine='odf') as writer:
        data.to_excel(writer, index=False)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file.ods> <output_file.ods>")
        sys.exit(1)

    # Get input and output file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Process sheets and save to the output ODS file
    result = stack_sheets(input_file)
    save_to_ods(result, output_file)
