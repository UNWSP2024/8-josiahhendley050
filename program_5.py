# Program #5: Course Info
#3/20/26
#Josiah Hendley
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
# ---------------------------------------------------------
# PSEUDOCODE
#
# Create an empty dictionary called courses
#
# Display message telling user to enter course ID and name
#
# Loop forever
#     Ask user for course ID
#     If course ID is "done"
#         Exit loop
#     Ask user for course name
#     Store course name in dictionary using course ID as key
# End Loop
#
# Ask user for a subject (example: "COS")
#
# Display "Courses with that subject:"
#
# For each course ID in the dictionary
#     If the course ID starts with the subject entered
#         Display the course ID and the course name
# End For
# ---------------------------------------------------------


def course_info():

    courses = {}  # dictionary to store course ID : course name pairs

    print("Enter course ID and course name. Type 'done' to stop.")

    while True:
        course_id = input("Course ID: ")

        if course_id.lower() == "done":
            break

        course_name = input("Course name: ")
        courses[course_id] = course_name

    subject = input("Enter a subject to search for (example: COS): ")

    print("\nCourses with that subject:")

    for cid in courses:
        if cid.startswith(subject):
            print(cid, "-", courses[cid])


# Example usage
if __name__ == "__main__":
    course_info()
