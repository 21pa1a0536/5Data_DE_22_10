#Part_1: Reading and Cleaning the given File data, Returns a Formatted students data in a Dictonary format.
def read_data(filename):
    students = {}

    try:
        with open(filename, "r") as file:
            next(file) #To Skip the Header Line 

            #Removing Extra Spaces, Line Breaks and Empty Lines

            for line in file:

                #Takes each line in string format
                line = line.strip()  # remove spaces and \n
                if not line:
                    continue   # skip empty lines

                #Splitting Line String into List of items
                parts = line.split(",") 
                if len(parts) != 4:
                    print("Skipping invalid line:", line)
                    continue

                
                student_id, name, subject, marks = parts

                #Convverting Marks to Integer Format
                try:
                   marks = int(marks)
                except ValueError:
                    print("Invalid marks found:", marks)
                    continue

                #Checking if STudent ID is present in Students Dictonary or not, if not then add it and it's respected data
                if student_id not in students:
                    students[student_id] = {"name": name, "subjects": {}}

                students[student_id]["subjects"][subject] = marks


    except FileNotFoundError:
        print("File not found:", filename)

    return students 


#Part_2: Generating a report by performing calculations for each student i.e., performing calculations on dictonary formatted Student data.
#Returns a list of reports
def generate_report(students):
    report_data = []

    for student_id, info in students.items():
        name = info["name"]
        subjects = info["subjects"]
    
        total = sum(subjects.values())
        average = total / len(subjects)
        high_sub = max(subjects, key=subjects.get)
        low_sub = min(subjects, key=subjects.get)

 
    #Appending Each student Data in a dictonary format into report_Data List
        report_data.append({
                "id": student_id,
                "name": name,
                "total": total,
                "average": average,
                "high_sub": high_sub,
                "high_mark": subjects[high_sub],
                "low_sub": low_sub,
                "low_mark": subjects[low_sub]
        })
    
    return report_data

#Part_3: Writing the data to a new file
def write_summary(report_data, filename):
    with open(filename, "w") as file:
        for r in report_data:
            file.write(f"Student ID: {r['id']}\n")
            file.write(f"Name: {r['name']}\n")
            file.write(f"Total Marks: {r['total']}\n")
            file.write(f"Average Marks: {r['average']:.2f}\n")
            file.write(f"Highest Scored Subject: {r['high_sub']} ({r['high_mark']})\n")
            file.write(f"Lowest Scored Subject: {r['low_sub']} ({r['low_mark']})\n")
            file.write("--------------------------------------\n")

#Final Main Function
def main():
    students = read_data("data.txt")

    if not students:
        print("No data found!") #If there is a file and no data is found in it, Prints this
        return

    report_data = generate_report(students)
    write_summary(report_data, "report2.txt")
    print("Report is successfully written to report.txt!")

if __name__ == "__main__":
    main()




""" SUMMARY:
    PROBLEM STATEMENT:
      1.Given a File of student data, we need to clean it, 
      2.Generate report for each student according to the requirements given
      3.Write the generated report to a new File

    Used three different functions for the above three operations
       1. read_data() function: 
            Input: File of student data
            Output: A Dictonary of cleaned and formatted student data
            Operations: Skipping header line, Removing Extra Space and Empty Lines, Skipping line with more than 4 parameters which is invalid
                        Adding Student_ID, Name and Subjects to the students dictonary and Returning it

       2. generate_report() function:
            Input: Dictonary of cleaned Students data
            Output: A list of Reports of each student according to the Requirements
            Operations: Calculating the required reports data, Appending the calculated data to a report_data List and Returning it.

       3. write_summary() function:
            Input: A list of reports, new filename (where you want to write this student report)
            Output: Returns nothing but writes the Reports of each student into the new file in a structured required format
            Operations: opens the new file, writes each student data in a structured way.
            NOTE: Firstly checks for the file to open, if no file is found with the given name, then creates a new file with that name and writes in it.
    
    """
            



