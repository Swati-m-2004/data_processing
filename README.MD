Task 9 --- Python Data Processing
Overview
A beginner-friendly Python program that processes structured student
records and calculates summary statistics.
Objectives
- Store structured records using a list of dictionaries.
- Validate required fields and marks/attendance ranges.
- Add a grade and Pass/Fail result to each record.
- Calculate overall and department-wise statistics.
Requirements
Python 3.9 or later. No external packages are needed.
Run
Open a terminal in this folder and execute:
python data_processing.py
On some Windows systems, use py data_processing.py.
Dataset
The sample dataset has six student records with ID, name, department,
marks, and attendance. Edit STUDENT_RECORDS in the Python file to add
or change records. Marks and attendance must be from 0 to 100.
Example grading rules
- A: 90--100
- B: 80--89
- C: 70--79
- D: 60--69
- Needs Improvement: below 60
- Pass: 40 marks or above; otherwise Fail
These are sample rules; adjust them if your mentor specifies different
criteria.
Functions
  Function                 Purpose
  validate_records()     Checks fields and numeric ranges
  grade_for()            Assigns a grade
  process_records()      Adds grade and result
  summarize()            Calculates overall statistics
  department_summary()   Calculates department averages and counts
  display_report()       Prints records and summaries
  main()                 Runs the workflow
Learning outcomes
Practice Python lists, dictionaries, loops, conditions, functions,
validation, and basic statistics.