import sys

def read_log_file(file_path):
    try:
        # Read the content of the log file.
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

def parse_log_line(line):
    # Parse a single line from the log file.
    cat_type, entry_time, exit_time = line.strip().split(',')
    return cat_type, int(entry_time), int(exit_time)

def analyze_cat_shelter_log(lines):
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break

        # Analyze each line from the log.
        cat_type, entry_time, exit_time = parse_log_line(line)

        if cat_type == 'OURS':
            cat_visits += 1
            total_time_in_house += exit_time - entry_time
            visit_lengths.append(exit_time - entry_time)
        elif cat_type == 'THEIRS':
            other_cats += 1

    return cat_visits, other_cats, total_time_in_house, visit_lengths

def format_time(minutes):
    # Format time in minutes to a human-readable format.
    hours, minutes = divmod(minutes, 60)
    return f"{hours} Hours, {minutes} Minutes"

def print_analysis(cat_visits, other_cats, total_time_in_house, visit_lengths):
    average_visit_length = (
        sum(visit_lengths) // len(visit_lengths)
        if visit_lengths
        else 0
    )
    longest_visit = max(visit_lengths) if visit_lengths else 0
    shortest_visit = min(visit_lengths) if visit_lengths else 0

    # Print the analysis results.
    print("\nLog File Analysis")
    print("==================\n")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}")
    print()
    print(f"Total Time in House: {format_time(total_time_in_house)}")
    print()
    print(f"Average Visit Length: {average_visit_length} Minutes")
    print(f"Longest Visit:        {longest_visit} Minutes")
    print(f"Shortest Visit:       {shortest_visit} Minutes")

def main():
    # The main entry point for the script.
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        sys.exit(1)

    log_file_path = sys.argv[1]
    lines = read_log_file(log_file_path)
    cat_visits, other_cats, total_time_in_house, visit_lengths = analyze_cat_shelter_log(lines)
    print_analysis(cat_visits, other_cats, total_time_in_house, visit_lengths)

if __name__ == "__main__":
    main()
