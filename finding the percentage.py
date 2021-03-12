if __name__ == '__main__':
    n = int(input())
#takes the n input for n number of students

    student_marks = {}
#creating an empty dictionary

    for _ in range(n):
#loop to input n student details

        name, *line = input().split()
#input().split() takes multiple input and assigns the first into name but assigns the rest into line
        scores = list(map(float, line))
#converts the items of line into floats and again makes a list of scores

        student_marks[name] = scores
#appending the dictionary with name as key and scores as value

    query_name = input()
#queries the name of student to be checked

    a = (sum(student_marks[query_name]))

#(student_marks[query_name]) is returns the scores of the students whose name is query name
#(sum(student_marks[query_name])) sums all the numbers in the list

    b = len((student_marks[query_name]))
#gives the total number of elements in the list of the scores

    percentage = '{:.2f}'.format(a/b)

#converts the percentage into two decimal place
    print(percentage)
