from z3 import *
import argparse
import json
import sys
import sympy

sys.path.insert(0, '../KachuaCore/')

from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast
import pprint as p

# python ..\Submission\symbSubmission.py -b optimized.kw -e['x','y']
from sympy import symbols, Eq, solve, parse_expr

def example(s, constrinats_dict, variables_set):

    # s.addSymbVar('x')
    # s.addSymbVar('y')
    # s.addSymbVar('z')


    # s.addSymbVar('c1')
    # s.addSymbVar('c2')
    # s.addSymbVar('c3')

    for temp_var in variables_set:
        s.addSymbVar(temp_var)

    for key,value in constrinats_dict.items():
        temp = key + " == " + value
        
        print(temp)
        print(type(temp))

        s.addConstraint(temp)
   
    result = s.s.check()

    print("result :- ", result)
    if str(result)=="sat":
        m = s.s.model()
        print("model printing", m)

    # print("constraints added till now",s.s.assertions())
    # # To assign z=x+y
    # s.addAssignment('z','x+y')
    # # To get any variable assigned
    # print("variable assignment of z =",s.getVar('z'))

def checkEq(args,ir):

    file1 = open("../Submission/testDataHoles.json","r+")
    testData1 = json.loads(file1.read())
    file1.close()

    file2 = open("../Submission/testData2.json","r+")
    testData = json.loads(file2.read())
    file2.close()



    s = zs.z3Solver()
    testData1 = convertTestData(testData1)
    testData = convertTestData(testData)


    # print(testData1)
    print("_____________________________")

    # print(testData)


    # for key1_1,value1_1 in testData1.items():
    #     # print(key)
    #     for key1_2,value1_2 in value1_1.items():
    #         if(key1_2=="constraints"):
    #             print(value1_2)
        # print("next line")

    # for key2_1,value2_1 in testData.items():
    #     # print(key)
    #     for key2_2,value2_2 in value2_1.items():
    #         if(key2_2=="constraints"):
    #             print(value2_2)
    #     # print("next line")


    constrinats_dict = {}
    variables_list = []
    s.addSymbVar('c1')
    s.addSymbVar('c2')

    for (key1_1,value1_1),(key2_1,value2_1) in zip(testData1.items(),testData.items()):
            # print(key)
            # if(key1_1==key2_1):
                # print(key1_1)
                # print(key2_1)
                # print("keys match")

                for (key1_2,value1_2),(key2_2,value2_2) in zip(value1_1.items(),value2_1.items()):
                    # if(key1_2=="constraints"):
                    #     if(key2_2=="constraints"):
                    if(key1_2=="symbEnc"):
                        if(key2_2=="symbEnc"):
                            # print(value1_2)
                            # print(value2_2)
                            # if(value1_2 == value2_2):
                             for (key1_3,value1_3),(key2_3,value2_3) in zip(value1_2.items(),value2_2.items()):
                                variables_list.append(key1_3)
                              
                                if(key1_3=='y'):
                                    if(key2_3=='y'):
                                        constrinats_dict[value1_3] = value2_3

                                        # print(type(value1_3))
                                        # print(type(value2_3))


                                        # print(value1_3)
                                        # print(value2_3)
                                        # print("It's a matching constraint")

            # print("next line")
    print("Printing contraints:-")

    variables_set = set(variables_list)
    for i in variables_set:
        print(i)
    # print(type(i))

        # output = args.output

    example(s, constrinats_dict, variables_set)

    # TODO: write code to check equivalence


if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()