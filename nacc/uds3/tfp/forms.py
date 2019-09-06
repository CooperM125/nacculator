###############################################################################
# Copyright 2015-2016 University of Florida. All rights reserved.
# This file is part of UF CTS-IT's NACCulator project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################
import nacc.uds3

### BEGIN non-generated code
# WARNING: When generating new forms, do not overwrite this section
from datetime import date

# WARNING: When generating new forms, use CURRENT_YEAR instead of "CURRENT_YEAR"
# WARNING: When generating new forms, use CURRENT_YEAR-15 instead of "1999"
CURRENT_YEAR = date.today().year

### END non-generated code


def header_fields():
    fields = {}
    fields['PACKET'] = nacc.uds3.Field(name='PACKET', typename='Char', position=(1, 2), length=2, inclusive_range=None, allowable_values=[], blanks=[])
    fields['FORMID'] = nacc.uds3.Field(name='FORMID', typename='Char', position=(4, 6), length=3, inclusive_range=None, allowable_values=[], blanks=[])
    fields['FORMVER'] = nacc.uds3.Field(name='FORMVER', typename='Num', position=(8, 10), length=3, inclusive_range=(1, 3), allowable_values=[], blanks=[])
    fields['ADCID'] = nacc.uds3.Field(name='ADCID', typename='Num', position=(12, 13), length=2, inclusive_range=(2, 38), allowable_values=[], blanks=[])
    fields['PTID'] = nacc.uds3.Field(name='PTID', typename='Char', position=(15, 24), length=10, inclusive_range=None, allowable_values=[], blanks=[])
    fields['VISITMO'] = nacc.uds3.Field(name='VISITMO', typename='Num', position=(26, 27), length=2, inclusive_range=(1, 12), allowable_values=[], blanks=[])
    fields['VISITDAY'] = nacc.uds3.Field(name='VISITDAY', typename='Num', position=(29, 30), length=2, inclusive_range=(1, 31), allowable_values=[], blanks=[])
    fields['VISITYR'] = nacc.uds3.Field(name='VISITYR', typename='Num', position=(32, 35), length=4, inclusive_range=(2005, CURRENT_YEAR), allowable_values=[], blanks=[])
    fields['VISITNUM'] = nacc.uds3.Field(name='VISITNUM', typename='Char', position=(37, 39), length=3, inclusive_range=None, allowable_values=[], blanks=[])
    fields['INITIALS'] = nacc.uds3.Field(name='INITIALS', typename='Char', position=(41, 43), length=3, inclusive_range=None, allowable_values=[], blanks=[])
    return fields


class FormT1(nacc.uds3.FieldBag):
    def __init__(self):
        self.fields['TELCOG'] = nacc.uds3.Field(name='TELCOG', typename='Num', position=(45, 45), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['TELILL'] = nacc.uds3.Field(name='TELILL', typename='Num', position=(47, 47), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['TELHOME'] = nacc.uds3.Field(name='TELHOME', typename='Num', position=(49, 49), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['TELREFU'] = nacc.uds3.Field(name='TELREFU', typename='Num', position=(51, 51), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['TELOTHR'] = nacc.uds3.Field(name='TELOTHR', typename='Num', position=(53, 53), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['TELOTHRX'] = nacc.uds3.Field(name='TELOTHRX', typename='Num', position=(55, 114), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 1e TELOTHER ne 1 (Yes)'])
        self.fields['TELINPER'] = nacc.uds3.Field(name='TELINPER', typename='Num', position=(116, 116), length=1, inclusive_range=(0, 1), allowable_values=['0', '1', '9'], blanks=['If Question 2 = 0 (No) then end from'])
        self.fields['TELMILE'] = nacc.uds3.Field(name='TELMILE', typename='Num', position=(118, 118), length=1, inclusive_range=(0, 1), allowable_values=['0', '1', '9'], blanks=['Blank if Question 2 TELINPER = 0 (No)','Blank if Question 2 TELINPER = 9 (Unknown) and this is first telephone packet'])

class FormA1(nacc.uds3.FieldBag):
    def __init__(self):
        self.fields['BIRTHMO'] = nacc.uds3.Field(name='BIRTHMO', typename='Num', position=(45, 46), length=2, inclusive_range=(1, 12), allowable_values=[], blanks=[])
        self.fields['BIRTHYR'] = nacc.uds3.Field(name='BIRTHYR', typename='Num', position=(48, 51), length=4, inclusive_range=(1875, CURRENT_YEAR-15), allowable_values=[], blanks=[])
        self.fields['MARISTAT'] = nacc.uds3.Field(name='MARISTAT', typename='Num', position=(53, 53), length=1, inclusive_range=(1, 6), allowable_values=['9', '3', '2', '1', '6', '5', '4'], blanks=[])
        self.fields['SEX'] = nacc.uds3.Field(name='SEX', typename='Num', position=(55, 55), length=1, inclusive_range=(1, 2), allowable_values=['2', '1'], blanks=[])
        self.fields['LIVSITUA'] = nacc.uds3.Field(name='LIVSITUA', typename='Num', position=(57, 57), length=1, inclusive_range=(1, 6), allowable_values=['9', '3', '2', '1', '6', '5', '4'], blanks=[])
        self.fields['INDEPEND'] = nacc.uds3.Field(name='INDEPEND', typename='Num', position=(59, 59), length=1, inclusive_range=(1, 4), allowable_values=['9', '3', '2', '1', '4'], blanks=[])
        self.fields['RESIDENC'] = nacc.uds3.Field(name='RESIDENC', typename='Num', position=(61, 61), length=1, inclusive_range=(1, 4), allowable_values=['9', '3', '2', '1', '4'], blanks=[])
        self.fields['ZIP'] = nacc.uds3.Field(name='RESIDENC', typename='Char', position=(63, 65), length=1, inclusive_range=(6, 999), allowable_values=[], blanks=[])


class FormA2(nacc.uds3.FieldBag):
    def __init__(self):
        self.fields['INBIRMO'] = nacc.uds3.Field(name='INBIRMO', typename='Num', position=(45, 46), length=2, inclusive_range=(1, 12), allowable_values=['99'], blanks=[])
        self.fields['INBIRYR'] = nacc.uds3.Field(name='INBIRYR', typename='Num', position=(48, 51), length=4, inclusive_range=(1875, CURRENT_YEAR-15), allowable_values=['9999'], blanks=[])
        self.fields['INSEX'] = nacc.uds3.Field(name='INSEX', typename='Num', position=(53, 53), length=1, inclusive_range=(1, 2), allowable_values=['1', '2'], blanks=[])
        self.fields['NEWINF'] = nacc.uds3.Field(name='NEWINF', typename='Num', position=(55, 55), length=1, inclusive_range=(0, 1), allowable_values=['1', '0'], blanks=['If Question 3 NEWINF = 0 (No) then skip to Question 9'])
        self.fields['INHISP'] = nacc.uds3.Field(name='INHISP', typename='Num', position=(57, 57), length=1, inclusive_range=(0, 1), allowable_values=['1', '0'], blanks=['Blank if Question 3 INHISP = 0 (No)', 'If Question 4 INHISP = 0 (No) then skip to Question 5', 'IF Question 4 INHISP = 9 (Unknown) then skip to Question 5'])
        self.fields['INHISPOR'] = nacc.uds3.Field(name='INHISPOR', typename='Num', position=(59, 60), length=2, inclusive_range=(1, 6), allowable_values=['99', '50'], blanks=['Blank if Question 4 INHISP ne 1 (Yes)'])
        self.fields['INHISPOX'] = nacc.uds3.Field(name='INHISPOX', typename='Char', position=(62, 121), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 4a INHISPOR ne 50 (Other)'])
        self.fields['INRACE'] = nacc.uds3.Field(name='INRACE', typename='Num', position=(123, 124), length=2, inclusive_range=(1, 5), allowable_values=['50', '99'], blanks=['Blank if Question 3 NEWINF = 0 (No)'])
        self.fields['INRACEX'] = nacc.uds3.Field(name='INRACEX', typename='Char', position=(126, 185), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 5 INRACE ne 50 (Other)'])
        self.fields['INRASEC'] = nacc.uds3.Field(name='INRASEC', typename='Num', position=(187, 188), length=2, inclusive_range=(1, 5), allowable_values=['50', '88', '99'], blanks=['Blank if Question 3 NEWINF = 0 (No)'])
        self.fields['INRASECX'] = nacc.uds3.Field(name='INRASECX', typename='Char', position=(190, 249), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 6 INRASEC ne 50 (Other)'])
        self.fields['INRATER'] = nacc.uds3.Field(name='INRATER', typename='Num', position=(251, 252), length=2, inclusive_range=(1, 5), allowable_values=['50','88','99'], blanks=['Blank if Question 3 NEWINF = 0 (No)'])
        self.fields['INRATERX'] = nacc.uds3.Field(name='INRATERX', typename='Char', position=(254, 313), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 7 INTATER ne 50 (Other)'])
        self.fields['INEDUC'] = nacc.uds3.Field(name='INEDUC', typename='Num', position=(315, 316), length=2, inclusive_range=(0, 3), allowable_values=['0','1','2','3'], blanks=['Blank if Question 3 NEWINF = 0 (No)'])
        self.fields['INRELTO'] = nacc.uds3.Field(name='INRELTO', typename='Num', position=(318, 318), length=1, inclusive_range=(1, 6), allowable_values=[], blanks=[])
        self.fields['INKNOWN'] = nacc.uds3.Field(name='INKNOWN', typename='Num', position=(320, 322), length=3, inclusive_range=(0, 120), allowable_values=['999'], blanks=[])
        self.fields['INLIVWTH'] = nacc.uds3.Field(name='INLIVWTH', typename='Num', position=(324, 324), length=1, inclusive_range=(0, 1), allowable_values=[], blanks=['If Question 10 INLIVWTH = 1 (Yes) then skip to Question 11'])
        self.fields['INVISITS'] = nacc.uds3.Field(name='INVISITS', typename='Num', position=(326, 326), length=1, inclusive_range=(1, 6), allowable_values=[], blanks=['Blank if Question 10 INLIVWTH = 1 (Yes)'])
        self.fields['INCALLS'] = nacc.uds3.Field(name='INCALLS', typename='Num', position=(328, 328), length=1, inclusive_range=(1, 6), allowable_values=[], blanks=['Blank if Question 10 INLIVWTH = 1 (Yes)'])
        self.fields['INRELY'] = nacc.uds3.Field(name='INRELY', typename='Num', position=(330, 330), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])


class FormA3(nacc.uds3.FieldBag):
    def __init__(self):
        self.fields['NWINFMUT'] = nacc.uds3.Field(name='NWINFMUT', typename='Num', position=(45, 45), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=['If Question 1 NWINFMUT = 0 (No) then skip to Question 5', 'If Question 1 NWINFMUT = 9 (Unknown) then skip to Question 5'])
        self.fields['FADMUT'] = nacc.uds3.Field(name='FADMUT', typename='Num', position=(47, 47), length=1, inclusive_range=(0, 3), allowable_values=['8', '9'], blanks=['Blank if Question 1 NWINFMUT ne 1 (Yes)', 'If Question 2a FADMUT = 0 (No) then skip to Question 3a', 'If Question 2a FADMUT = 9 (Unkown) then skip to Question 3a'])
        self.fields['FADMUTX'] = nacc.uds3.Field(name='FADMUTX', typename='Char', position=(49, 108), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 2a FADMUT ne 8 (Other)', 'Blank if Question 1 NWINFMUT ne 1 (Yes)'])
        self.fields['FADMUSO'] = nacc.uds3.Field(name='FADMUSO', typename='Num', position=(110, 110), length=1, inclusive_range=(1, 3), allowable_values=['8', '9'], blanks=['Blank if Question 2a FADMUT'])
        self.fields['FADMUSOX'] = nacc.uds3.Field(name='FADMUSOX', typename='Char', position=(112, 171), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 2a FADMUT', 'Blank if Question 2a = 9 (Unknown)', 'Blank if question 2b FADMUSO ne 8 (Other)', 'Blank if Question 1 NEWINFMUT ne 1 (Yes)'])
        self.fields['FFTDMUT'] = nacc.uds3.Field(name='FFTDMUT', typename='Num', position=(173, 173), length=1, inclusive_range=(0, 4), allowable_values=['8', '9'], blanks=['Blank if Question 1 NWINFMUT ne 1 (Yes)', 'If Question 3a FFTDMUT = 0 (No) then skip to Question 4a', 'If Question 3a FFTDMUT = 9 (Unknown) then skip to Question 4a'])
        self.fields['FFTDMUTX'] = nacc.uds3.Field(name='FFTDMUTX', typename='Char', position=(175, 234), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 3a FFTDMUT ne 8 (Other)', 'Blank if Question 1 NWINFMUT ne 1 (Yes)'])
        self.fields['FFTDMUSO'] = nacc.uds3.Field(name='FFTDMUSO', typename='Num', position=(236, 236), length=1, inclusive_range=(1, 3), allowable_values=['8', '9'], blanks=['Blank if Question 3a FFTDMUT = 0 (No)', 'Blank if Question 3a FFTDMUT = 9 (Unknown)', 'Blank if Question 1 NWINFMUT ne 1 (Yes)'])
        self.fields['FFTDMUSX'] = nacc.uds3.Field(name='FFTDMUSX', typename='Char', position=(238, 297), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 3a FFTDMUT = 0 (No)', 'Blank if Question 3a FFTDMUT = 9 (Unknown)', 'Blank if Question 3b FFTDMUSO ne 8 (Other)', 'Blank if Question 1 NWQINFMUT ne 1 (Yes)'])
        self.fields['FOTHMUT'] = nacc.uds3.Field(name='FOTHMUT', typename='Num', position=(299, 299), length=1, inclusive_range=(0, 1), allowable_values=['9'], blanks=['Blank if Question 1 NWINFMUT ne 1 (Yes)', 'If Question 4a FOTHMUT = 0 (No) then skip to Question 5', 'If Question 4a FOTHMUT = 9 (Unknown) then skip to Question 5'])
        self.fields['FOTHMUTX'] = nacc.uds3.Field(name='FOTHMUTX', typename='Char', position=(301, 360), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 4a FOTHMUT ne 1 (Yes)', 'Blank if Question 1 NWINFMUT ne 1 (Yes)'])
        self.fields['FOTHMUSO'] = nacc.uds3.Field(name='FOTHMUSO', typename='Num', position=(362, 362), length=1, inclusive_range=(1, 3), allowable_values=['8', '9'], blanks=['Blank if Question 4a FOTHMUT = 0 (No)', 'Blank if Question 4a FOTHMUT = 9 (Unknown)', 'Blank if Question 1 NWINFMUT ne 1 (Yes)'])
        self.fields['FOTHMUSX'] = nacc.uds3.Field(name='FOTHMUSX', typename='Char', position=(364, 423), length=60, inclusive_range=None, allowable_values=[], blanks=['Blank if Question 4a FOTHMUT = 0 (No)', 'Blank if Question 4a FOTHMUT = 9 (Unknown)', 'Blank if Question 4b FOTHMUSO ne 8 (Other)','Blank if Question 1 NEWINFMUT ne 1 (Yes)'])
        self.fields['NWINFPAR'] = nacc.uds3.Field(name='NWINFPAR', typename='Num', position=(425, 425), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=['If Question 5 NWINFPAR = 0 (No) then skip to Question 6'])
        self.fields['MOMMOB'] = nacc.uds3.Field(name='MOMMOB', typename='Num', position=(427, 428), length=2, inclusive_range=(1, 12), allowable_values=['99'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)'])
        self.fields['MOMYOB'] = nacc.uds3.Field(name='MOMYOB', typename='Num', position=(430, 433), length=4, inclusive_range=(1875, CURRENT_YEAR-15), allowable_values=['9999'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)'])
        self.fields['MOMDAGE'] = nacc.uds3.Field(name='MOMDAGE', typename='Num', position=(435, 437), length=3, inclusive_range=(0, 110), allowable_values=['888', '999'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)'])
        self.fields['MOMNEUR'] = nacc.uds3.Field(name='MOMNEUR', typename='Num', position=(439, 439), length=1, inclusive_range=(1, 5), allowable_values=['8', '9'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'If Question 5a4 MOMNEUR = 8 (N/A) then skip the remaining question in the row','If Question 5a4 MOMNEUR = 9 (Unknown) then skip the remaining question in the row'])
        self.fields['MOMPRDX'] = nacc.uds3.Field(name='MOMPRDX', typename='Num', position=(441, 443), length=3, inclusive_range=(40, 490), allowable_values=['999'], blanks=['Blank if Question 5 NWINFPAR = 0(No)', 'Blank if Question 5a4 MOMNEUR = 8 (N/A)', 'Blank if Question 5a4 MOMNEUR = 9 (Unknown)'])
        self.fields['MOMMOE'] = nacc.uds3.Field(name='MOMMOE', typename='Num', position=(445, 445), length=1, inclusive_range=(1, 7), allowable_values=[], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'Blank if Question 5a4 MOMNEUR = 8 (N/A)', 'Blank if Question 5a4 MOMNEUR = 9 (Unknown)'])
        self.fields['MOMAGEO'] = nacc.uds3.Field(name='MOMAGEO', typename='Num', position=(447, 449), length=3, inclusive_range=(0, 110), allowable_values=['999'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'Blank if Question 5a4 MOMNEUR = 8 (N/A)', 'Blank if Question 5a4 MOMNUR = 9 (Unknown)'])
        self.fields['DADMOB'] = nacc.uds3.Field(name='DADMOB', typename='Num', position=(451, 452), length=2, inclusive_range=(1, 12), allowable_values=['99'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)'])
        self.fields['DADYOB'] = nacc.uds3.Field(name='DADYOB', typename='Num', position=(454, 457), length=4, inclusive_range=(1875, CURRENT_YEAR-15), allowable_values=['9999'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)'])
        self.fields['DADDAGE'] = nacc.uds3.Field(name='DADDAGE', typename='Num', position=(459, 461), length=3, inclusive_range=(0, 110), allowable_values=['999', '888'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)'])
        self.fields['DADNEUR'] = nacc.uds3.Field(name='DADNEUR', typename='Num', position=(463, 463), length=1, inclusive_range=(1, 5), allowable_values=['8', '9'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'If Queston 5b4 DADNEUR = 8 (N/A) skip the remaing questions in the rom', 'If Question 5a4 DADNEUR = 9 (Unknown) skip the remaining questions in the row'])
        self.fields['DADPRDX'] = nacc.uds3.Field(name='DADPRDX', typename='Num', position=(465, 467), length=3, inclusive_range=(40, 490), allowable_values=['999'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'Blank if Question 5b4 DADNEUR = 8 (N/A)', 'Blank if Question 5b4 DADNEUR = 9 (Unknown)'])
        self.fields['DADMOE'] = nacc.uds3.Field(name='DADMOE', typename='Num', position=(469, 469), length=1, inclusive_range=(1, 7), allowable_values=[], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'Blank if Question 5b4 DADNEUR = 8 (N/A)', 'Blank if Question 5B4 DADNEUR = 9 (Unknown)'])
        self.fields['DADAGEO'] = nacc.uds3.Field(name='DADAGEO', typename='Num', position=(471, 473), length=3, inclusive_range=(0, 110), allowable_values=['999'], blanks=['Blank if Question 5 NWINFPAR = 0 (No)', 'Blank if Question 5b4 DADNEUR = 8 (N/A)', 'Blank if Question 5B4 DADNEUR = 9 (Unknown)'])
        self.fields['SIBS'] = nacc.uds3.Field(name='SIBS', typename='Num', position=(475, 476), length=2, inclusive_range=(0, 20), allowable_values=['77'], blanks=['If Question 6 SIBS = 0 then skip to Question 7', 'If Question 6 SIBS = 77 then skip to Question 7'])
        self.fields['NWINFSIB'] = nacc.uds3.Field(name='NWINFSIB', typename='Num', position=(478, 478), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'If Question 6a NWINFSIB = 0 (No) then skip to Question 7'])
        
        self.fields['SIB1MOB'] = nacc.uds3.Field(name='SIB1MOB', typename='Num', position=(480, 481), length=2, inclusive_range=(1, 12), allowable_values=['99'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)'])
        self.fields['SIB1YOB'] = nacc.uds3.Field(name='SIB1YOB', typename='Num', position=(483, 486), length=4, inclusive_range=(1875, CURRENT_YEAR-15), allowable_values=['9999'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)'])
        self.fields['SIB1AGD'] = nacc.uds3.Field(name='SIB1AGD', typename='Num', position=(488, 490), length=3, inclusive_range=(0, 110), allowable_values=['888', '999'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)'])
        self.fields['SIB1NEU'] = nacc.uds3.Field(name='SIB1NEU', typename='Num', position=(492, 492), length=1, inclusive_range=(1, 5), allowable_values=['8', '9'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)', 'If Question 6aa4 SIB1NEU = 8 then skip the remaining Questions in the row', 'IF Question 6aa4 SIB1NEU = 9 (Unknown) then skip the remainign Questions in the row'])
        self.fields['SIB1PDX'] = nacc.uds3.Field(name='SIB1PDX', typename='Num', position=(494, 496), length=3, inclusive_range=(40, 490), allowable_values=['999'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)', 'Blank if Question 6aa4 SIB1NEU = 8 (N/A)', 'Blank if Question 6aa4 SIB1NEU = 9 (Unknown)'])
        self.fields['SIB1MOE'] = nacc.uds3.Field(name='SIB1MOE', typename='Num', position=(498, 498), length=1, inclusive_range=(1, 7), allowable_values=[], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)', 'Blank if Question 6aa4 SIB1NEU = 8 (N/A)', 'Blank if Question 6aa4 SIB1NEU = 9 (Unknown)'])
        self.fields['SIB1AGO'] = nacc.uds3.Field(name='SIB1AGO', typename='Num', position=(500, 502), length=3, inclusive_range=(0, 110), allowable_values=['999'], blanks=['Blank if Question 6 SIBS = 0', 'Blank if Question 6 SIBS = 77', 'Blank if Question 6a NWINFSIB = 0 (No)', 'Blank if Question 6aa4 SIB1NEU = 8 (N/A)', 'Blank if Question 6aa4 SIB1NEU = 9 (Unknown)'])
        # Repeate for each sibling TODO double check


class FormZ1X(nacc.uds3.FieldBag):
    def __init__(self):
        self.fields = header_fields()
        self.fields['LANGT1'] = nacc.uds3.Field(name='LANGT1', typename='Num', position=(45, 45), length=1, inclusive_range=(1, 2), allowable_values=['2', '1'], blanks=[])
        self.fields['LANGA1'] = nacc.uds3.Field(name='LANGA1', typename='Num', position=(47, 47), length=1, inclusive_range=(1, 2), allowable_values=['2', '1'], blanks=[])
        self.fields['LANGA2'] = nacc.uds3.Field(name='LANGA2', typename='Num', position=(49, 49), length=1, inclusive_range=(1, 2), allowable_values=['2', '1'], blanks=['Blank if Question 2 A2SUB = 0 (No)'])
        self.fields['LANGA3'] = nacc.uds3.Field(name='LANGA3', typename='Num', position=(51, 51), length=1, inclusive_range=(1, 2), allowable_values=['2', '1'], blanks=['Blank if Question 4b A3SUB = 0 (No)'])
        self.fields['A3SUB'] = nacc.uds3.Field(name='A3SUB', typename='Num', position=(53, 53), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['A3NOT'] = nacc.uds3.Field(name='A3NOIT', typename='Num', position=(55, 56), length=2, inclusive_range=(95, 98), allowable_values=['98', '97', '96', '95'], blanks=['Blank if Question 4b A3SUB = 1 (Yes)'])
        self.fields['LANGA4'] = nacc.uds3.Field(name='LANGA4', typename='Num', position=(58, 58), length=1, inclusive_range=(1, 2), allowable_values=['1', '2'], blanks=['Blank if Question 5b = 0 (No)'])
        self.fields['A4SUB'] = nacc.uds3.Field(name='A4SUB', typename='Num', position=(60, 60), length=1, inclusive_range=(0, 1), allowable_values=['0', '1'], blanks=[])
        self.fields['A4NOT'] = nacc.uds3.Field(name='A4NOT', typename='Num', position=(62, 63), length=2, inclusive_range=(95, 98), allowable_values=['98', '97', '96', '95'], blanks=['Blank if Question 5b = 0 (No)'])
        self.fields['LANGB4'] = nacc.uds3.Field(name='LANGB4', typename='Num', position=(65, 65), length=1, inclusive_range=(1, 2), allowable_values=['1', '2'], blanks=[])
        self.fields['LANGB5'] = nacc.uds3.Field(name='LANGB5', typename='Num', position=(67, 67), length=1, inclusive_range=(1, 2), allowable_values=['2','1'], blanks=['Blank if Question 7b B5SUB = 0 (No)'])
        self.fields['B5SUB'] = nacc.uds3.Field(name='B5SUB', typename='Num', position=(69, 69), length=1, inclusive_range=(0, 1), allowable_values=['1','0'], blanks=[])
        self.fields['B5NOT'] = nacc.uds3.Field(name='B5NOT', typename='Num', position=(71, 72), length=2, inclusive_range=(95, 98), allowable_values=['98','97','96','95'], blanks=['Blank if Question 7b B5SUB = 1 (Yes)'])
        self.fields['LANGB7'] = nacc.uds3.Field(name='LANGB7', typename='Num', position=(74, 74), length=1, inclusive_range=(1,2), allowable_values=['2','1'], blanks=['Blank if Question 8b B7SUB = 0 (No)'])
        self.fields['B7SUB'] = nacc.uds3.Field(name='B7SUB', typename='Num', position=(76, 76), length=1, inclusive_range=(0,1), allowable_values=['1','0'], blanks=[])
        self.fields['B7NOT'] = nacc.uds3.Field(name='B7NOT', typename='Num', position=(78, 79), length=2, inclusive_range=(95,98), allowable_values=['98','97','96','95'], blanks=['Blank if Question 8b B7SUB = 1 (Yes)'])
        self.fields['LANGB9'] = nacc.uds3.Field(name='LANGB9', typename='Num', position=(81, 81), length=1, inclusive_range=(1,2), allowable_values=['2','1'], blanks=[])
        self.fields['LANGD1'] = nacc.uds3.Field(name='LANGD1', typename='Num', position=(83, 83), length=1, inclusive_range=(1,2), allowable_values=['2','1'], blanks=[])
        self.fields['LANGD2'] = nacc.uds3.Field(name='LANGD2', typename='Num', position=(85, 85), length=1, inclusive_range=(1,2), allowable_values=['2','1'], blanks=[])
        self.fields['LANGCLS'] = nacc.uds3.Field(name='LANGCLS', typename='Num', position=(87, 87), length=1, inclusive_range=(1,2), allowable_values=['2','1'], blanks=['Blank if Question 12b CLSSUB = 0 (No)'])
        self.fields['CLSSUB'] = nacc.uds3.Field(name='CLSSUB', typename='Num', position=(89, 89), length=1, inclusive_range=(0,1), allowable_values=['1','0'], blanks=[])


