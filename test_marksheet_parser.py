
from pprint import pprint

from src.advisor.marksheet_parser import parse_lms_results


sample_data = """
| # | Code | Title | Majors | Credit Hours | Grade | Grade Points | Product |
|---|---|---|---|---|---|---|---|
| 1 | CSC 308 | Professional Practices and Ethics | N/A | 2 | A | 4 | 8 |
| 2 | CSL 113 | Computer Programming Lab | N/A | 1 | D | 1 | 1 |
| 3 | CSC 113 | Computer Programming | N/A | 3 | D | 1 | 3 |
| 4 | GSC 221 | Discrete Mathematics | N/A | 3 | C- | 1.67 | 5.01 |
| 5 | ISL 101 | Islamic Studies/Ethic | N/A | 2 | B | 3 | 6 |
| 6 | CSL 114 | Introduction to ICT Lab | N/A | 1 | C+ | 2.33 | 2.33 |
| 7 | CSC 114 | Introduction to ICT | N/A | 2 | C+ | 2.33 | 4.66 |
| 8 | GSC 114 | Applied Physics | N/A | 2 | C+ | 2.33 | 4.66 |
| 9 | GSL 113 | Applied Physics Lab | N/A | 1 | A- | 3.67 | 3.67 |
| 10 | ISL 107 | Tajweed | N/A | 0 | A | 4 | 0 |
"""

results = parse_lms_results(sample_data)

print("Total courses:", len(results))

print("\nParsed results:")
pprint(results)

print("\nPassing status:")
for course in results:
    print(
        course["course_code"],
        course["grade"],
        course["is_passed"]
    )