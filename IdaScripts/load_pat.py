import idaapi
import idc
import idautils
import os

def load_pat_file(pat_file):
    pat_data = {}
    with open(pat_file, 'r') as f:
        for line in f:
            line_parts = line.split()
            if len(line_parts) == 2:
                addr_str = line_parts[0].replace('.', '')  # Remove dots from address string
                name_str = line_parts[1]
                pat_data[int(addr_str, 16)] = name_str
    return pat_data

def main():
    # Prompt user to select .pat file
    pat_file = idaapi.ask_file(0, "*.pat", "Select .pat file")
    if not pat_file:
        print("No file selected.")
        return

    pat_data = load_pat_file(pat_file)

    # Rename functions
    for function_ea in idautils.Functions():
        if function_ea in pat_data:
            new_name = pat_data[function_ea]
            idc.MakeNameEx(function_ea, new_name, idc.SN_FORCE)
            print("Renamed function: %s" % idc.GetFunctionName(function_ea))

if __name__ == '__main__':
    main()