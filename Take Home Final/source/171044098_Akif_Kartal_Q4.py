# 171044098
# Akif Kartal
# Final Exam-Q4 Real Code

def main():
    #create cost matrix
    cost_matrix = [[50, 13, 42, 80],
                   [7, 3, 3, 17],
                   [22, 72, 2, 1],
                   [6, 66, 666, 27]]
    n = len(cost_matrix[0])
    people = [-1] * n
    jobs = [-1] * n

    job_distribution(people, jobs, cost_matrix, n)
    print("-------Cost Matrix------------")
    for i in range(0, len(cost_matrix)):
        print(cost_matrix[i])
    print("------------------------------")
    print("Person job Assignment")
    for i in range(0, n):
        print("Person", i, "has job", people[i])
    print("------------------------------")
    print("job Person Assignment")
    for i in range(0, n):
        print("job", i, "has Person", jobs[i])
    print("------------------------------")

#while assinging ignore total cost
#just focus on number of maximum cost.
def job_distribution(people, jobs, costs, n):
    # first we need to find maximum cost for each job
    # in cost matrix(for each row).
    max_costs_indexes = [-1]*n
    max_index = -1
    all_max_has_same_index = True
    for i in range(0, n):
        max = -1
        for j in range(0, n):
            if max < costs[i][j]:
                max = costs[i][j]
                max_index = j
        max_costs_indexes[i] = max_index
        if i != 0 and max_costs_indexes[i-1] != max_index:
            all_max_has_same_index = False
    # check is same person has all maximum costs
    # in other words check if all maximum costs are in same index.
    if all_max_has_same_index:
        print("Number of Maximum Cost is", 1)
        for i in range(0, n):
            jobs[i] = i
            people[i] = i
    # maximum costs are distributed on people
    # assing jobs such that number of max costs is 0.
    else:
        for i in range(0, n):
            if i == n - 1:  # if last job
                jobs[i] = find_people(jobs, n, max_costs_indexes[i])
            else:
                is_found = False
                for k in range(i, n):
                    if (max_costs_indexes[k] != max_costs_indexes[i]) and (not is_found) and (jobs.count(max_costs_indexes[k]) == 0):
                        jobs[i] = max_costs_indexes[k]
                        is_found = True
                if not is_found:
                    jobs[i] = find_people(jobs, n, max_costs_indexes[i])
            people[jobs[i]] = i
        print("Number of Maximum Cost is", 0)

#get one person who wasn't chosen yet.
def find_people(jobs, n, current_person):
    pers = -1
    for j in range(0, n):
        if jobs.count(j) == 0 and j != current_person:
            pers = j
    return pers


main()
