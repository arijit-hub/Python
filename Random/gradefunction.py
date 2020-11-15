def input_file(reading):
    '''(file open for reading)->list of floats

    Returns a list of floats of grades from the file reading.

    >>>Name1 90.0
       Name2 95.0
    [90.0,95.0]
    '''

    first_line=reading.readline()
    first_line=reading.readline()

    grades_list=[]
    for line in reading:
        grade_index=line.find(' ')
        grades_list.append(float(line[grade_index+1:len(line)-1]))

    return grades_list

def grade_count(input_list):
    '''(list of floats)->list of int

    Returns the number of times a grade in range is repeated in input_list.
    '''

    grade_count_list=[0,0,0,0,0,0,0,0,0,0,0]

    for i in range(len(input_list)):

        if input_list[i]<10 and input_list[i]>=0:
            grade_count_list[0]=grade_count_list[0]+1

        elif input_list[i]<20 and input_list[i]>=10:
            grade_count_list[1]=grade_count_list[1]+1

        elif input_list[i]<30 and input_list[i]>=20:
            grade_count_list[2]=grade_count_list[2]+1

        elif input_list[i]<40 and input_list[i]>=30:
            grade_count_list[3]=grade_count_list[3]+1

        elif input_list[i]<50 and input_list[i]>=40:
            grade_count_list[4]=grade_count_list[4]+1

        elif input_list[i]<60 and input_list[i]>=50:
            grade_count_list[5]=grade_count_list[5]+1
            
        elif input_list[i]<70 and input_list[i]>=60:
            grade_count_list[6]=grade_count_list[6]+1

        elif input_list[i]<80 and input_list[i]>=70:
            grade_count_list[7]=grade_count_list[7]+1

        elif input_list[i]<90 and input_list[i]>=80:
            grade_count_list[8]=grade_count_list[8]+1

        elif input_list[i]<100 and input_list[i]>=90:
            grade_count_list[9]=grade_count_list[9]+1

        else:
            grade_count_list[10]=grade_count_list[10]+1

    return grade_count_list
            
        
def histogram_writeup(grade_list,write_file):

    write_file.write("Copy File\n\n")

    for i in range(len(grade_list)-1):
        upper=str(i*10+9)
        lower=str(i*10)

        write_file.write(lower+'-'+upper+':'+str(grade_list[i]*'*')+'\n')
        
    write_file.write('100:'+str(grade_list[i]*'*'))
