#https://www.hackerrank.com/challenges/battery/problem
if __name__ == '__main__':
    timeCharged = float(input())
    file=open("trainingdata.txt",'r')
    df=file.readlines()
    # after reading the file in a csv format and ploting a graph the following was understood

    if timeCharged>=4:
        print('8.0')
    else:
        print('{:.2f}'.format(timeCharged*2))
