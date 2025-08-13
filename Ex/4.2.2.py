def parse_ranges(ranges_string):
    range_parts = ((int(start), int(stop)) for start, stop in 
        (part.split('-') for part in ranges_string.split(',')))
    for start, stop in range_parts:
        if start > stop:
            raise ValueError(f"Invalid range: {start}-{stop}")
    range_parts = ((int(start), int(stop)) for start, stop in 
        (part.split('-') for part in ranges_string.split(',')))
    return (num for start, stop in range_parts for num in range(start, stop + 1))



def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))

if __name__ == "__main__":
    main()