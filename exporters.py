import json
from astronomy import SolarTerm
from string import Template
from zoneinfo import ZoneInfo
from mapper import SOLAR_TERMS_EN

def format_cpp_array(data_list, items_per_line):
    """Chunks a long list into neatly indented rows for C++ formatting."""
    chunks = [", ".join(data_list[i:i + items_per_line]) for i in range(0, len(data_list), items_per_line)]
    return ",\n    ".join(chunks)

def export_json(data: list[SolarTerm], filename):
    """Formats the raw SolarTerm objects into a human-readable JSON file."""
    hk_tz = ZoneInfo("Asia/Hong_Kong")
    json_data = []
    
    for item in data:
        hk_time = item.time.astimezone(hk_tz)
        
        json_data.append({
            "term_index": item.term_index,
            "name": SOLAR_TERMS_EN[item.term_index],
            "date_utc": item.time.utc_iso(),
            "date_hk": hk_time.isoformat(),
            "epoch": item.epoch
        })
        
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
        
    print(f"[-] JSON written to {filename}")

def export_cpp_header(data: list[SolarTerm], start_year, end_year, filename):
    """Strips the raw SolarTerm objects down to arrays and writes the C++ header."""
    
    # Extract the epochs directly from the dataclass object
    epochs_str = format_cpp_array([str(item.epoch) for item in data], items_per_line=5)
    
    # Extract the term index directly from the dataclass object
    terms_str = format_cpp_array([str(item.term_index) for item in data], items_per_line=12)
    
    # Prepare the English names array (0 to 23)
    names_list = [f'"{SOLAR_TERMS_EN[i]}"' for i in range(24)]
    term_names_str = format_cpp_array(names_list, items_per_line=4)
    
    # Read the raw template file
    with open('templates/template.h', 'r', encoding='utf-8') as f:
        raw_template = f.read()
        
    # Inject the variables
    cpp_template = Template(raw_template)
    final_cpp = cpp_template.substitute(
        start_year=start_year,
        end_year=end_year,
        data_length=len(data),
        epochs=epochs_str,
        terms=terms_str,
        term_names=term_names_str
    )
    
    # Write to disk
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_cpp)
        
    print(f"[-] C++ Header written to {filename}")