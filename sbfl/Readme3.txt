All 5 test Cases and its Buggy file are present in the testcases folder under ChironCore folder.


5 test Cases are named as:-
	sfl1.tl	        sfl1_bug.tl		contains 3 variables x,y,z
	sfl2.tl	        sfl2_bug.tl		contains 3 variables x,y,z
	sfl3.tl	        sfl3_bug.tl		contains 3 variables x,y,z
	sfl4.tl	        sfl4_bug.tl		contains 3 variables x,y,z
	sfl5.tl	        sfl5_bug.tl		contains 3 variables x,y,z

To run sbflSubmission.py file use the below command,
python ./chiron.py --SBFL ./tests/sbfl1.tl --buggy ./tests/sbfl1_bug.tl -vars '[":x", ":y", ":z"]' --timeout      10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True 

