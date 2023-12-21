it_student_data = [
    {
        "name": "Thomas Munster",
        "student_number": 34534,
        "course": "accelerated",
        "age": 21,
        "enrolled_subjects": ["IIIS001", "IAPP001", "INET001", "IDBF001"]
    },
    {
        "name": "John Smith",
        "student_number": 1111,
        "course": "standard",
        "age": 19,
        "enrolled_subjects": ["IWBS001", "IBRM001", "IAPP001"]
    },
    {
        "name": "Sarah Johnson",
        "student_number": 2222,
        "course": "accelerated",
        "age": 18,
        "enrolled_subjects": ["IBRM001", "IAPP001", "INET001", "IDBF001"]
    },
    {
        "name": "Emily Davis",
        "student_number": 3333,
        "course": "extended",
        "age": 20,
        "enrolled_subjects": ["IWBS001", "IIIS001", "IAPP001"]
    },
    {
        "name": "Michael Thompson",
        "student_number": 4444,
        "course": "standard",
        "age": 17,
        "enrolled_subjects": ["IWBS001", "IBRM001", "IPRG001"]
    },
    {
        "name": "Jessica Brown",
        "student_number": 5555,
        "course": "accelerated",
        "age": 21,
        "enrolled_subjects": ["IBRM001", "IAPP001", "INET001", "IDBF001"]
    },
    {
        "name": "Daniel Wilson",
        "student_number": 6666,
        "course": "extended",
        "age": 19,
        "enrolled_subjects": ["IWBS001", "IBRM001", "IPRG001"]
    },
    {
        "name": "Olivia Miller",
        "student_number": 7777,
        "course": "standard",
        "age": 18,
        "enrolled_subjects": ["IWBS001", "IIIS001", "IAPP001"]
    }
]

course_counts = {
    "standard": 0,
    "extended": 0,
    "accelerated": 0
}
age_counts = {}
enrolment_counts = {
    "Introduction to Technical Communication": 0,
    "Introduction to Information Systems": 0,
    "Programming 1": 0,
    "Web Systems": 0,
    "Business Requirements Modelling": 0,
    "Programming 2": 0,
    "Network Fundamentals": 0,
    "Database Fundamentals": 0
}


for student in it_student_data:
    #print(student["course"])
    if student["course"] == "standard":
        course_counts["standard"] = course_counts["standard"] + 1
    elif student["course"] == "extended":
        course_counts["extended"] = course_counts["extended"] + 1
    elif student["course"] == "accelerated":
        course_counts["accelerated"] = course_counts["accelerated"] + 1
    #age
    if student["age"] in age_counts:
        current = age_counts[student["age"]]
        age_counts[student["age"]] = current + 1
    else:
        age_counts[student["age"]] = 1
    # unit counts
    for unit in student["enrolled_subjects"]:
        if unit == "IITC001":
            enrolment_counts["Introduction to Technical Communication"] += 1
        if unit == "IIIS001":
            enrolment_counts["Introduction to Information Systems"] += 1
        if unit == "IPRO001":
            enrolment_counts["Programming 1"] += 1
        if unit == "IWBS001":
            enrolment_counts["Web Systems"] += 1
        if unit == "IBRM001":
            enrolment_counts["Business Requirements Modelling"] += 1
        if unit == "IPRO002":
            enrolment_counts["Programming 2"] += 1
        if unit == "INEF001":
            enrolment_counts["Network Fundamentals"] += 1
        if unit == "IDBF001":
            enrolment_counts["Database Fundamentals"] += 1
    
        
print(course_counts)
print(age_counts)
print(enrolment_counts)

# {'standard': 3, 'extended': 2, 'accelerated': 3}
# {21: 2, 19: 2, 18: 2, 20: 1, 17: 1}
# {'Introduction to Technical Communication': 0, 'Introduction to Information Systems': 3, 'Programming 1': 0, 'Web Systems': 5, 'Business Requirements Modelling': 5, 'Programming 2': 0, 'Network Fundamentals': 0, 'Database Fundamentals': 3}