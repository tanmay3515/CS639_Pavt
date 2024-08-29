#!/usr/bin/env python3

import argparse
import sys
import numpy as np
import math
sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv

def compute_activity_matrix_sum(activity_mat):
    # converting list as array for simplicity
    activity_mat_np = np.array(activity_mat, dtype=int)
    # Converting the activity_mat to a NumPy array for computation purpose
    matrix_sum = np.sum(activity_mat_np)     
    return matrix_sum

def uniqueness(activity_mat):
    # converting list as array for simplicity and finding unique column from activity matrix
    activity_mat_np = np.array(activity_mat, dtype=int)
    unique_columns = np.unique(activity_mat_np, axis=1)
    num_unique_columns = unique_columns.shape[1]
    total_columns = activity_mat_np.shape[1]
    uniquenes= num_unique_columns/total_columns
    return uniquenes

def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    activity_mat_sum = compute_activity_matrix_sum(activity_mat)
    num_elements = sum(len(row) for row in activity_mat)
    density = activity_mat_sum/num_elements

    uniquenes = uniqueness(activity_mat)

    count = {}    
    for row in activity_mat:
        activity = tuple(row)
        if activity in count:
            count[activity] += 1
        else:
            count[activity] = 1
    
    s = 0 
    for activity, count in count.items():
        s = s + (count * (count-1))

    length = (len(activity_mat) )
    div = 1
    if(length!=1):
        div = (1-(s/(length*(length-1))))
    
    density_dash= 1-abs(1-2*density)
    fitness_score= -1*density_dash*uniquenes*div
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite
    print(activity_mat)
    return fitness_score


# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """
        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        Cf = Cp = Nf = Np = 0
         
         
        sus_score = 0
        # ToDo : implement the suspiciousness score function.
        column = [row[comp_index] for row in self.activity_mat]

        for cindex in range(len(column)):
            if column[cindex] == 1 and self.errorVec[cindex] == 1:
                Cf += 1
            elif column[cindex] == 0 and self.errorVec[cindex] == 0:
                Np += 1
            elif column[cindex] == 1 and self.errorVec[cindex] == 0:
                Cp += 1
            else:
                Nf += 1
        if math.sqrt((Cf+Nf)*(Cf+Cp))==0:
            return sus_score
        sus_score= Cf/math.sqrt((Cf+Nf)*(Cf+Cp))

        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        """
        
        l=[]
        for i in range(len(self.activity_mat[0])):
            
            sus_score = self.suspiciousness(i)
            print(sus_score)
            l.append(["c"+ str(i+1),sus_score])
        
        

        rankList = []
        # ToDo : implement rankList
        l.sort(key=lambda x: x[1], reverse=True)

        rank = 1
    

        for i in range(len(l)):
            if i > 0 and l[i][1] < l[i - 1][1]:
                rank += 1
            rankList.append([l[i][0], rank])
        print(rankList)
        return rankList


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)
