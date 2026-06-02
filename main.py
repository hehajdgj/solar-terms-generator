import argparse
from astronomy import calculate_astronomy
from exporters import export_json, export_cpp_header

def main():
    parser = argparse.ArgumentParser(description="Calculate 24 Solar Terms and export to JSON and C++.")
    parser.add_argument("start_year", type=int, help="The starting year (e.g., 2024)")
    parser.add_argument("end_year", type=int, help="The ending year (e.g., 2025)")
    
    # Optional flags for file names
    parser.add_argument("--json", type=str, default="solar_terms.json", help="Output JSON filename")
    parser.add_argument("--cpp", type=str, default="solar_terms.h", help="Output C++ header filename")
    
    args = parser.parse_args()
    
    print(f"Calculating solar terms from {args.start_year} to {args.end_year}...")
    
    master_data = calculate_astronomy(args.start_year, args.end_year)
    
    export_json(master_data, args.json)
    export_cpp_header(master_data, args.start_year, args.end_year, args.cpp)
    
    print("Success! All files generated.")

if __name__ == "__main__":
    main()