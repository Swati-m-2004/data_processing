"""Task 9: Python Data Processing — run with: python data_processing.py"""
from statistics import mean

STUDENT_RECORDS = [
    {"id": 101, "name": "Asha", "department": "CSE", "marks": 88, "attendance": 92},
    {"id": 102, "name": "Rahul", "department": "ECE", "marks": 74, "attendance": 85},
    {"id": 103, "name": "Meena", "department": "CSE", "marks": 95, "attendance": 97},
    {"id": 104, "name": "Kiran", "department": "ISE", "marks": 61, "attendance": 78},
    {"id": 105, "name": "Pooja", "department": "ECE", "marks": 82, "attendance": 89},
    {"id": 106, "name": "Arjun", "department": "CSE", "marks": 47, "attendance": 70},
]

def validate_records(records):
    required = {"id", "name", "department", "marks", "attendance"}
    for number, record in enumerate(records, 1):
        missing = required - record.keys()
        if missing:
            raise ValueError(f"Record {number} missing: {', '.join(sorted(missing))}")
        for field in ("marks", "attendance"):
            if not isinstance(record[field], (int, float)) or not 0 <= record[field] <= 100:
                raise ValueError(f"Record {number}: {field} must be between 0 and 100")

def grade_for(marks):
    if marks >= 90: return "A"
    if marks >= 80: return "B"
    if marks >= 70: return "C"
    if marks >= 60: return "D"
    return "Needs Improvement"

def process_records(records):
    processed = []
    for record in records:
        item = record.copy()
        item["grade"] = grade_for(item["marks"])
        item["result"] = "Pass" if item["marks"] >= 40 else "Fail"
        processed.append(item)
    return processed

def summarize(records):
    if not records:
        return {"total_students": 0, "average_marks": 0, "highest_marks": None,
                "lowest_marks": None, "pass_count": 0, "fail_count": 0,
                "average_attendance": 0}
    marks = [r["marks"] for r in records]
    attendance = [r["attendance"] for r in records]
    return {
        "total_students": len(records),
        "average_marks": round(mean(marks), 2),
        "highest_marks": max(marks),
        "lowest_marks": min(marks),
        "pass_count": sum(mark >= 40 for mark in marks),
        "fail_count": sum(mark < 40 for mark in marks),
        "average_attendance": round(mean(attendance), 2),
    }

def department_summary(records):
    grouped = {}
    for record in records:
        grouped.setdefault(record["department"], []).append(record["marks"])
    return {dept: {"student_count": len(marks), "average_marks": round(mean(marks), 2)}
            for dept, marks in sorted(grouped.items())}

def display_report(records):
    print("\nPROCESSED STUDENT RECORDS")
    print(f"{'ID':<6}{'Name':<12}{'Dept':<8}{'Marks':<8}{'Attend.':<10}{'Grade':<22}{'Result'}")
    print("-" * 82)
    for r in records:
        print(f"{r['id']:<6}{r['name']:<12}{r['department']:<8}{r['marks']:<8}"
              f"{r['attendance']:<10}{r['grade']:<22}{r['result']}")
    print("\nOVERALL SUMMARY")
    for key, value in summarize(records).items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print("\nDEPARTMENT SUMMARY")
    for dept, stats in department_summary(records).items():
        print(f"{dept}: {stats['student_count']} student(s), average marks = {stats['average_marks']}")

def main():
    validate_records(STUDENT_RECORDS)
    display_report(process_records(STUDENT_RECORDS))

if __name__ == "__main__":
    main()
