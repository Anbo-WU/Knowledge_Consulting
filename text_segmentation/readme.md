1.This code defines a `split_text_file` function, which takes an input file path and then splits the file content according to the specified `CHUNK_SIZE` and `OVERLAP`. 

2.Each part after the split is saved as a new text file, with the file name being the original file name plus a part number. All files are saved in the same directory as the original file. The file 'test4trans.txt' is the template for text partition.

3.I've struck on a new means to fulfil the requirements by using special character list so that I do not need to segment the target file into so many pieces just now.

4.The code file with the suffix 'ipynb' can be open in Jupyter Notebook while that with the suffix 'py' obviously can be open in most python interpreters(e.g. PyCharm).

5.Some annotation should be added n at least one new means should to write. It is plain to see that I may update this file. Hope I could do it soon.

-- v1.0  by Abbott  04/03/2024--


1. Added a new means to materialise text partition without changing the canonical form put forward before. Now the segmented pieces will all be settled in only csv file, which is more judicious considering the cooperation with the API code. See the file: segment_to_context.ipynb

2.Some annotation should be added. Maybe I will write the special character method although it is deprecated for assignment now. I am not sure.


-- v2.0  by Abbott  15/03/2024--



