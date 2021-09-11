# 
#  * Class for the NEG-algorithm.
#  * 
#  * @author maxkratz
#  * @version 0.1.8
#  
class NEH:
    
    # 
    #    * Method for step nr 1. Returns an ArrayList with the totaltime for each job.
    #    * 
    #    * @param jobs ArrayList of jobs (input)
    #    * @return totaltimes ArrayList with the totaltime for each job
    def step_one(self, jobs):
        #  create an empy ArrayList of integers
        totalTimes = []
        i = 0
        while i < len(jobs):
            #  variable for summing
            #  go through each job
            sum = 0
            j = 0
            while j < len(jobs[i]):
                sum = sum + jobs[i][j]
                #  sum up
                j += 1
            totalTimes.append(sum)
            i += 1
        return totalTimes

    # 
    #    * Step 2: Sort the list (descending order)
    #    * 
    #    * @param jobs ArrayList of all jobs
    #    * @return list of jobs descending order
    #    
    def step_two(self, jobs):
        numberAndJobs = []
        #  add all jobs to an ArrayList
        i = 0
        while i < len(jobs):
            tempElement = [i, jobs[i]]
            #  temporary Array with the job-number and the jobs
            numberAndJobs.append(tempElement)
            #  add the temporaray Array to the ArrayList
            i += 1
        #  sort ArrayList descending
        numberAndJobs.sort(self.jobComparator)
        return numberAndJobs
    
    #  comparator for sorting the jobs
    def jobComparator(self, elem1, elem2):
        if elem1[1] > elem2[1]:
            return -1
        elif elem1[1] == elem2[1]:
            return 0
        else:
            return 1
    #  end of comparator

    # 
    #    * Searches for the biggest two elements and puts them in the best order.
    #    * 
    #    * @param sortedList descending sorted list with all jobs
    #    * @param first the first element
    #    * @param second the second element
    #    * @return List list with the biggest two elements (sorted)
    #    * 
    #    
    def sortFirstTwoElements(self, sortedList, first, second):
        #  search for the to biggest elemets:
        one = 0
        oneValue = 0
        twoValue = 0
        #  find the biggest job:
        i = 0
        while i < len(sortedList):
            if sortedList[i][1] > oneValue:
                oneValue = sortedList[i][1]
                one = sortedList[i][0]
            i += 1
        #  search for the second largest element:
        i = 0
        while i < len(sortedList):
            if sortedList[i][1] > twoValue and sortedList[i][0] != one:
                twoValue = sortedList[i][1]
            i += 1
        # 
        #      * Until now, the first and the second largest jobs are found. Todo: Test both sequences (1
        #      * first, 2 second or 2 first, 1 secon).
        #      
        resultList = []
        makespan1 = self.calculateTotalMakespan(first, second)
        makespan2 = self.calculateTotalMakespan(second, first)
        if makespan1 > makespan2:
            resultList.append(sortedList[1])
            resultList.append(sortedList[0])
        else:
            resultList.append(sortedList[0])
            resultList.append(sortedList[1])
        return resultList

    # 
    #    * Returns the makespan of n jobs.
    #    * 
    #    * @param jobs ArrayList of jobs
    #    * 
    #    * @return makespan calculated makespan
    #    
    def calculateNTotalMakespan(self, jobs):
        totalMakespan = 0
        myJobSumList = []
        #  create a job1-array with the summings
        # myJobSumList.append(len(job[0]))
        myJobSumList.append([])
        myJobSumList[0].insert(0, jobs[0][0])
        #  summing
        i = 1
        while i < len(jobs[0]):
            myJobSumList[0].insert(i, myJobSumList[0][i - 1] + jobs[0][i])
            i += 1
        #  end of job1-array creating
        #  add all other "empty" job-arrays to the list
        i = 1
        while i < len(jobs):
            myJobSumList.insert(i, [])
            i += 1
        #  fill the first row (from left to right summing)
        i = 1
        while i < len(myJobSumList):
            myJobSumList[i].append(myJobSumList[i - 1][0] + jobs[i][0])
            i += 1
        #  go through all jobs each
        i = 1
        while i < len(jobs):
            j = 1
            while j < len(myJobSumList[i]):
                #  is the first time of the first job larger, chose it ...
                if myJobSumList[i - 1][j] > myJobSumList[i][j - 1]:
                    myJobSumList[i][j] = myJobSumList[i - 1][j] + jobs[i][j]
                else:
                    #  is the time of the second job larger, chose it ...
                    myJobSumList[i][j] = myJobSumList[i][j - 1] + jobs[i][j]
                j += 1
            i += 1
        totalMakespan = myJobSumList[len(myJobSumList) - 1][len(myJobSumList[len(myJobSumList) - 1]) - 1]
        return totalMakespan

    # 
    #    * Return the makespan of two jobs.
    #    * 
    #    * @param job1 first job
    #    * @param job2 second job
    #    * @return makespan calculated makespan
    #    
    def calculateTotalMakespan(self, job1, job2):
        #  create a job1-array with the summing
        # job1_d = len(job1)
        job1_d = []
        job1_d.append(job1[0])
        #  add first place
        #  summing
        i = 1
        while i < len(job1):
            job1_d.insert(i, job1_d[i - 1] + job1[i])
            i += 1
        #  end of creation of the job1-array (with summing)
        #  create a job2-array with summing (with case destinction)
        job2_d = []
        job2_d.insert(0, job1_d[0] + job2[0])
        #  add first place
        #  add all other places
        # 
        #      * Is the job of the first machine or the first job faster? Chose the higher result for
        #      * calculatin.
        #      
        i = 1
        while i < len(job2):
            #  is the first time of the first job larger, chose it ...
            if job1_d[i] > job2_d[i - 1]:
                job2_d.insert(i, job1_d[i] + job2[i])
            else:
                #  is the time of the second job larger, chose it ...
                job2_d.insert(i, job2_d[i - 1] + job2[i])
            i += 1
        return job2_d[len(job2_d) - 1]
        #  zurueckgeben

    # 
    #    * Creates the sum of each job-time.
    #    * 
    #    * @param job array of a job
    #    * 
    #    * @return sum sum of each job-time
    #    
    def calculateJobTotalTime(self, job):
        value = 0
        #  summing
        i = 0
        while i < len(job):
            value = value + job[i]
            i += 1
        return value

    # 
    #    * Calculates the best order for all jobs.
    #    * 
    #    * @param jobs ArrayList of all jobs (as int-array)
    #    * 
    #    * @return jobs in order arraylist of all jobs (as int-array) in order with the smallest makespan
    #    
    def calculateNEHOrder(self, jobs):
        #  list for the first two jobs
        firstTwoElemetList = []
        #  list for the total times
        sumList = []
        #  sumList filling:
        i = 0
        while i < len(jobs):
            sumList.append(self.calculateJobTotalTime(jobs[i]))
            i += 1
        #  create sorted list
        sortierteListe = self.step_two(sumList)
        #  add the first two elements
        firstTwoElemetList.append(jobs[sortierteListe[0][0]])
        firstTwoElemetList.append(jobs[sortierteListe[1][0]])
        print firstTwoElemetList
        #  add the first two jobs in the final list
        myList_2 = self.sortFirstTwoElements(firstTwoElemetList, jobs[sortierteListe[0][0]], jobs[sortierteListe[1][0]])
        #  iterate through all jobs
        j = 2
        while j < len(sortierteListe):
            tempMakeSpan = 100000000
            gutePosition = 0
            #  iterate through all positons
            i = 0
            while i <= len(myList_2):
                tempMyList = []
                tempMyList = tempMyList + myList_2
                tempMyList.insert(i, jobs[sortierteListe[j][0]])
                #  if the actual position is better than the one before, go with it ...
                if self.calculateNTotalMakespan(tempMyList) < tempMakeSpan:
                    tempMakeSpan = self.calculateNTotalMakespan(tempMyList)
                    gutePosition = i
                i += 1
            #  If the second iteration is finished, the best place is found:
            myList_2.insert(gutePosition, jobs[sortierteListe[j][0]])
            j += 1
        #  DEBUGGING:
        #  print this.gibAktuelleReihenfolge(myList_2, jobs);
        return myList_2

    # 
    #    * Returns the actual order as String (for debugging).
    #    * 
    #    * @param jobListeAct list of jobs
    #    * @param jobs list of jobs (before sorting)
    #    * 
    #    * @return Order order of jobs as String
    #    
    def calculateOrder(self, jobListeAct, jobs):
        #  create an arraylist for the order of the jobs (number of jobs)
        orderNumber = []
        print "Order of jobs: "
        orderString = ""
        #  go through all jobs an find the representing numbers of each job
        i = 0
        while i < len(jobListeAct):
            k = 0
            while k < len(jobs):
                if jobListeAct[i] == jobs[k]:
                    orderNumber.append(k + 1)
                    #  add job in list
                    #  add the number of the job to the string (separated with commas)
                    orderString = orderString + str(k + 1)
                    orderString = orderString + ", "
                k += 1
            i += 1
        return orderString

