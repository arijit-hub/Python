import tkinter.filedialog
import gradefunction

read_file=tkinter.filedialog.askopenfilename()

reading=open(read_file,'r')

write_file=tkinter.filedialog.asksaveasfilename()

writing=open(write_file,'w')

inputing=gradefunction.input_file(reading)

grade_range_list=gradefunction.grade_count(inputing)

histogram=gradefunction.histogram_writeup(grade_range_list,writing)

reading.close()
writing.close()


