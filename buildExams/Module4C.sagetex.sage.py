## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file /home/archdoc/git-repos/AAG-College-Algebra/buildExams/Module4C.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_66 = Integer(66); _sage_const_41 = Integer(41); _sage_const_89 = Integer(89); _sage_const_47 = Integer(47); _sage_const_84 = Integer(84); _sage_const_85 = Integer(85); _sage_const_67 = Integer(67); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_126 = Integer(126); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_51 = Integer(51); _sage_const_122 = Integer(122); _sage_const_120 = Integer(120); _sage_const_71 = Integer(71); _sage_const_102 = Integer(102); _sage_const_103 = Integer(103); _sage_const_107 = Integer(107); _sage_const_141 = Integer(141)## This file (Module4C.sagetex.sage) was *autogenerated* from Module4C.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module4C', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_35 
_st_.blockbegin()
try:
 load("../Code/generalPurposeMethods.sage")
 load("../Code/keyGeneration.sage")
 load("../Code/commonlyUsedFunctions.sage")
 keyFileName = "Module4"
 version = "C"
except:
 _st_.goboom(_sage_const_41 )
_st_.blockend()
_st_.current_tex_line = _sage_const_47 
_st_.blockbegin()
try:
 moduleNumber="4"
 problemNumber=_sage_const_16 
 load("../Code/04quadratic/quadraticEquationToGraph.sage")
except:
 _st_.goboom(_sage_const_51 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_66 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_66 )
try:
 _st_.current_tex_line = _sage_const_66 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_66 )
_st_.current_tex_line = _sage_const_67 
_st_.blockbegin()
try:
 moduleNumber="4"
 problemNumber=_sage_const_17 
 load("../Code/04quadratic/quadraticFormula.sage")
except:
 _st_.goboom(_sage_const_71 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_2 , latex(displayStem))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_3 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_7 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_8 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_84 )
_st_.current_tex_line = _sage_const_85 
_st_.blockbegin()
try:
 moduleNumber="4"
 problemNumber=_sage_const_18 
 load("../Code/04quadratic/factorLeadingOver1Composite.sage")
except:
 _st_.goboom(_sage_const_89 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_9 , latex(displayStem))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_10 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_13 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_14 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_15 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_102 )
_st_.current_tex_line = _sage_const_103 
_st_.blockbegin()
try:
 moduleNumber="4"
 problemNumber=_sage_const_19 
 load("../Code/04quadratic/solveQuadraticFactorComposites.sage")
except:
 _st_.goboom(_sage_const_107 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_16 , latex(displayStem))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_17 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_21 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_22 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_120 )
_st_.current_tex_line = _sage_const_122 
_st_.blockbegin()
try:
   moduleNumber="4"
   problemNumber=_sage_const_20 
   load("../Code/04quadratic/quadraticGraphToEquation.sage")
   
except:
 _st_.goboom(_sage_const_126 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_23 , latex(displayStem))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_28 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_141 )
_st_.endofdoc()

