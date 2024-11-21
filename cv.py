import datetime

def Personal_Information():
    # Gather Personal Information
    First_Name = input("Enter your first name: ")
    Last_Name = input("Enter your last name: ")
    Email = input("Enter your email: ")
    Phone = input("Enter your phone number: ")
    Country = input("Enter your country name: ")
    City = input("Enter your city name: ")
    Nationality = input("Enter your nationality: ")
    Job_Title_App = input("Enter your j ob title you want to apply for: ")
    Birth_Date = input("Enter your date of birth: ")
    Address = input("Enter your Address: ")
    Postal_Code = input("Enter your postal code: ")
    Gender = input("Enter your gender M/F: ")
    Hobbies = input("Enter your hobbies like reading, skydiving etc...: ")
    # Gather professional summary
    Objective_Summary = input("Write a short professional summary about your objectives, goals, career and motivation: ")
    return First_Name, Last_Name, Email, Phone, Country, City, Nationality, Job_Title_App,Birth_Date, Address, Postal_Code, Gender, Hobbies, Objective_Summary

def Employment_History():
    # Gather Work Experience
    Job_Title = input("Enter your job title: ")
    Employer = input("Enter the employer name: ")
    Designation = input("Enter the designation: ")
    Start_End_Date_Emp = input("Enter the start and end date (e.g. 5-2-2023 to 6-3-2024): ")
    Country_Emp = input("Enter the country name: ")
    City_Emp = input("Enter the city name: ")
    Job_Description = input("Enter your key responsibilities (separate with commas): ")
    return Job_Title, Employer, Designation, Start_End_Date_Emp, Country_Emp, City_Emp, Job_Description


def Education_Detail():
    # Gather Education Detail
    Institution_Name = input("Enter university name: ")
    Degree_Title = input("Enter your degree title: ")
    Start_End_Date_Edu = input("Enter the start and end date (e.g. 5-2-2023 to 6-3-2024): ")
    Country_Edu = input("Enter the country name: ")
    City_Edu = input("Enter the city name: ")
    Thesis_Description = input("Enter your thesis description if available otherwise mention none: ")
    return Institution_Name, Degree_Title, Start_End_Date_Edu, Country_Edu, City_Edu, Thesis_Description


def Skills_Information():
    # Gather Skill Information
    Skill = input("Enter your significant skill: ")
    Level = input("Enter the level of skill (low/intermediate/high): ")
    return Skill, Level

def Refrences():
    # Gather Reference Details
    Reference_Name = input("Enter your reference full name : ")
    Company_Name = input("Enter company name: ")
    Designation_Ref = input("Enter Referee Designation: ")
    Email_Ref = input("Enter email: ")
    Phone_Ref = input("Enter phone number: ")
    return Reference_Name, Company_Name, Designation_Ref, Email_Ref, Phone_Ref

####### Display the CV Information #########
def Display_Personal(First_Name, Last_Name, Email, Phone, Country, City, Nationality, Job_Title_App,Birth_Date, Address, Postal_Code, Gender, Hobbies, Objective_Summary):
    # Print the CV
    print("\n=== Simple CV ===")
    print()
    print("\n=== Personal Information ===")
    print()
    print(f"First Name: {First_Name}")
    print(f"Last Name: {Last_Name}")
    print(f"Email: {Email}")
    print(f"Contact Number: {Phone}")
    print(f"Country: {Country}")
    print(f"City: {City}")
    print(f"Nationality: {Nationality}")
    print(f"Job Title: {Job_Title_App}")
    print(f"Date of Birth: {Birth_Date}")
    print(f"Current Address: {Address}")
    print(f"Postal Code: {Postal_Code}")
    print(f"Gender: {Gender}")
    print(f"Hobbies: {Hobbies}")
    print(f"Objective Summary: {Objective_Summary}")

def Display_Employment(Job_Title, Employer, Designation, Start_End_Date_Emp, Country_Emp, City_Emp, Job_Description):
    print("\n=== Employment History ===")
    print()
    print(f"Job Title: {Job_Title}")
    print(f"Employer Name: {Employer}")
    print(f"Designation: {Designation}")
    print(f"Job Duration: {Start_End_Date_Emp}")
    print(f"Country: {Country_Emp}")
    print(f"City: {City_Emp}")
    print(f"My Job Responsibilities are: {Job_Description}")

def Display_Education(Institution_Name, Degree_Title, Start_End_Date_Edu, Country_Edu, City_Edu, Thesis_Description):
    print("\n=== Education Detail ===")
    print()
    print(f"Institution Name: {Institution_Name}")
    print(f"My Degree is: {Degree_Title}")
    print(f"Duration: {Start_End_Date_Edu}")
    print(f"Country: {Country_Edu}")
    print(f"City: {City_Edu}")
    print(f"Thesis Description: {Thesis_Description}")

def Display_Skill(Skill, Level):
    print("\n=== Skill Detail ===")
    print()
    print(f"Skills are: {Skill}")
    print(f"Skill Level: {Level}")

def Display_Reference(Reference_Name, Company_Name, Designation_Ref, Email_Ref, Phone_Ref):
    print("\n=== Reference Information ===")
    print()
    print(f"Reference Name: {Reference_Name}")
    print(f"Company Name: {Company_Name}")
    print(f"Referee Designation: {Designation_Ref}")
    print(f"Email Referee: {Email_Ref}")
    print(f"Contact Referee: {Phone_Ref}")
    print("===================")


def Create_Simple_CV():
    First_Name, Last_Name, Email, Phone, Country, City, Nationality, Job_Title_App,Birth_Date, Address, Postal_Code, Gender, Hobbies, Objective_Summary= Personal_Information()
    Job_Title, Employer, Designation, Start_End_Date_Emp, Country_Emp, City_Emp, Job_Description = Employment_History()
    Institution_Name, Degree_Title, Start_End_Date_Edu, Country_Edu, City_Edu, Thesis_Description = Education_Detail()
    Skill, Level = Skills_Information()
    Reference_Name, Company_Name, Designation_Ref, Email_Ref, Phone_Ref = Refrences()
    Display_Personal(First_Name, Last_Name, Email, Phone, Country, City, Nationality, Job_Title_App, Birth_Date, Address, Postal_Code, Gender, Hobbies, Objective_Summary)
    Display_Employment(Job_Title, Employer, Designation, Start_End_Date_Emp, Country_Emp, City_Emp, Job_Description)
    Display_Education(Institution_Name, Degree_Title, Start_End_Date_Edu, Country_Edu, City_Edu, Thesis_Description)
    Display_Skill(Skill, Level)
    Display_Reference(Reference_Name, Company_Name, Designation_Ref, Email_Ref, Phone_Ref)


#### Calling Main Function ###
Create_Simple_CV()
