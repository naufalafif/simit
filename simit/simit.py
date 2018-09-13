"""
Author : Naufal Afif
Github Link : https://github.com/naufalafif/simit
Create Date : September 13, 2018

"""

import Levenshtein as lv
import sys
import pint

class SimUnit:
    def __init__(self):
        '''
        Define pint unit converter
        Get all unit in pint into list array, so the similarity between unit can be calculate
        '''
        self.ureg = pint.UnitRegistry()
        self.all_unit = list(dir(self.ureg))

    def conv(self,query):
        '''
        calculate similarity score using levenshten distance algorithm using Levenstein library
        '''
        score = [lv.distance(query,x) for x in self.all_unit]
        index = score.index(min(score))
        unit = self.all_unit[index]
        return self.str_to_class(unit)
        
    def str_to_class(self,string):
        '''
        Call pint converter using string
        '''
        return getattr(self.ureg,string)