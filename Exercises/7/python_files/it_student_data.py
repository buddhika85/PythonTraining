# this looks like a list of dictionaries
# list - because you have [...]
# list contains dictionaries with key: value pairs
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

counts_dict = {
    "accelerated": 0,
    "standard": 0,
    "extended": 0
};

counts_by_age = {}

for student in it_student_data:
    # print(student["course"])
    if (student["course"] == "accelerated"):
        counts_dict["accelerated"] = counts_dict["accelerated"] + 1
    elif (student["course"] == "standard"):
        counts_dict["standard"] = counts_dict["standard"] + 1
    elif (student["course"] == "extended"):
        counts_dict["extended"] = counts_dict["extended"] + 1

print(counts_dict)

for student in it_student_data:
    #print(student["age"])
    if (student["age"] in counts_by_age):
        counts_by_age[student["age"]] = counts_by_age[student["age"]] + 1
    else:
        counts_by_age[student["age"]] = 1

print(counts_by_age)

# Stage 1
# IITC001 Introduction to Technical Communication
# IIIS001 Introduction to Information Systems
# IPRO001 Programming 1
# IWBS001 Web Systems
# Stage 2
# IBRM001 Business Requirements Modelling *
# IPRO002 Programming 2 **
# INEF001 Network Fundamentals
# IDBF001 Database Fundamentals **
counts_by_subject = {
    "Introduction to Technical Communication": 0,
    "Introduction to Information Systems": 0,
    "Programming 1": 0,
    "Web Systems": 0,
    "Business Requirements Modelling": 0,
    "Programming 2": 0,
    "Network Fundamentals": 0,
    "Database Fundamentals": 0
}

for entry in it_student_data:
    # print(entry["enrolled_subjects"])
    for subject in entry["enrolled_subjects"]:
        if subject == "IITC001":
            counts_by_subject["Introduction to Technical Communication"] = counts_by_subject["Introduction to Technical Communication"] + 1
        elif subject == "IIIS001":
            counts_by_subject["Introduction to Information Systems"] = counts_by_subject["Introduction to Information Systems"] + 1
        elif subject == "IPRO001":
            counts_by_subject["Programming 1"] = counts_by_subject["Programming 1"] + 1
        elif subject == "IWBS001":
            counts_by_subject["Web Systems"] = counts_by_subject["Web Systems"] + 1
        elif subject == "IBRM001":
            counts_by_subject["Business Requirements Modelling"] = counts_by_subject["Business Requirements Modelling"] + 1
        elif subject == "IPRO002":
            counts_by_subject["Programming 2"] = counts_by_subject["Programming 2"] + 1
        elif subject == "INEF001":
            counts_by_subject["Network Fundamentals"] = counts_by_subject["Network Fundamentals"] + 1
        elif subject == "IDBF001":
            counts_by_subject["Database Fundamentals"] = counts_by_subject["Database Fundamentals"] + 1

#print(counts_by_subject)
for key in counts_by_subject.keys():
    print(f"{key}: {counts_by_subject[key]}")