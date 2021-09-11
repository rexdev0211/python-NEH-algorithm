from NEH import NEH

# 
#  * Class for testing the NEH-algorithm.
#  * 
#  * @author maxkratz
#  * @version 0.1.8
#  
class Main(object):
    """ generated source for class Main """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  create an NEH-object
        myNEHObject = NEH()
        #  create an arraylist of ints
        jobList = []
        #  create int-arrays for jobs
        job1 = [54, 79, 16, 66, 58]
        job2 = [83, 3, 89, 58, 56]
        job3 = [15, 11, 49, 31, 20]
        job4 = [71, 99, 15, 68, 85]
        job5 = [77, 56, 89, 78, 53]
        job6 = [36, 70, 45, 91, 35]
        job7 = [53, 99, 60, 13, 53]
        job8 = [38, 60, 23, 59, 41]
        job9 = [27, 5, 57, 49, 69]
        job10 = [87, 56, 64, 85, 13]
        job11 = [76, 3, 7, 85, 86]
        job12 = [91, 61, 1, 9, 72]
        job13 = [14, 73, 63, 39, 8]
        job14 = [29, 75, 41, 41, 49]
        job15 = [12, 47, 63, 56, 47]
        job16 = [77, 14, 47, 40, 87]
        job17 = [32, 21, 26, 54, 58]
        job18 = [87, 86, 75, 77, 18]
        job19 = [68, 5, 77, 51, 68]
        job20 = [94, 77, 40, 31, 28]
        #  add the job-arrays to the arraylist
        jobList.append(job1)
        jobList.append(job2)
        jobList.append(job3)
        jobList.append(job4)
        jobList.append(job5)
        jobList.append(job6)
        jobList.append(job7)
        jobList.append(job8)
        jobList.append(job9)
        jobList.append(job10)
        jobList.append(job11)
        jobList.append(job12)
        jobList.append(job13)
        jobList.append(job14)
        jobList.append(job15)
        jobList.append(job16)
        jobList.append(job17)
        jobList.append(job18)
        jobList.append(job19)
        jobList.append(job20)
        # print jobList
        #  end of creating the test-sequences
        #  calculate the arraylist with the best order
        results = myNEHObject.calculateNEHOrder(jobList)
        print results
        #  calculate the total makespan
        totalMakespan = myNEHObject.calculateNTotalMakespan(results)
        print myNEHObject.calculateOrder(results, jobList)
        print "Total makespan: " + str(totalMakespan)


if __name__ == '__main__':
    import sys
    Main.main(sys.argv)

