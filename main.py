# PJ VanDussesn
# 10/29/2024
# list-mc

score_list1 = []
score_list2= []
schools = ['Kingsley High school', 'Grand Traverse Academy']
courses = ['Chemistry', 'Art II']
students = ['VanDussen, Philemon', 'Gary, Eathon']
# student1_score = 70, 81, 96, 87
# student2_score = 87, 90, 78, 81
score_list1.append(70)
score_list1.append(81)
score_list1.append(96)
score_list1.append(87)

score_list2.append(87)
score_list2.append(90)
score_list2.append(78)
score_list2.append(81)

average_score = sum(score_list1) / len(score_list1)
average_score2 = sum(score_list2) / len(score_list2)



# score_list2.append(student2_score)

# average_score = sum(score_list1[0]) / len(score_list1[0])
# average_score2 = sum(score_list2[0]) / len(score_list2[0])

print(f'''        Semester 1 Grade Report
        ----------------------
        Student: {students[0]}
        School: {schools[0]}
        Course: {courses[0]}
        Average score: {average_score:.2f}

        Student: {students[1]}
        School: {schools[1]}
        Course:  {courses[1]}
        Average score: {average_score2:.2f}
      ''')
