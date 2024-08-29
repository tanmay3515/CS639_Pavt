the test Cases are present in tests folder inside the Kachuacore folder

First, we need to generate JSON Files for both P1 and P2.
the 
the test Cases are named as:-
	eqtest1, eqtest1_holes
	eqtest_2, eqtest_2_holes
	eqtest3, eqtest3_holes
	eqtest4, eqtest4_holes
	
JSON files of each test case file are named as:-
	testData1, testData1Holes
	testData_2, testData_2_holes
	testData3, testData3_holes
	testData4, testData4_holes

eqtest2.kw file is present in Submission Folder

To generate JSON file use, go to the KachuaCore directory
	
	For program with unknown holes :- python ./kachua.py -t 100 -se example/eqtest4_1.tl -d '{\":x\": 55, \":y\": 100, \":z\": 50}' -c '{\":c1\": 2, \":c2\": 3}'

	For program with no holes :- python ./kachua.py -t 100 -se example/eqtest5_1.tl -d '{\":x\": 55, \":y\": 100, \":z\": 50}' 

To generate kw file use,
	python kachua.py -O filename.

To run symbSubmission.py file use,
	python symbSubmission.py -b eqtest2.kw -e '[\"x\", \"y\"]'

