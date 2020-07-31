## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file /home/archdoc/git-repos/AAG-College-Algebra/buildExams/Module2C.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_138 = Integer(138); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_82 = Integer(82); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_41 = Integer(41); _sage_const_64 = Integer(64); _sage_const_32 = Integer(32); _sage_const_63 = Integer(63); _sage_const_46 = Integer(46); _sage_const_86 = Integer(86); _sage_const_117 = Integer(117); _sage_const_81 = Integer(81); _sage_const_68 = Integer(68); _sage_const_33 = Integer(33); _sage_const_119 = Integer(119); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_50 = Integer(50); _sage_const_123 = Integer(123); _sage_const_99 = Integer(99); _sage_const_100 = Integer(100); _sage_const_104 = Integer(104)## This file (Module2C.sagetex.sage) was *autogenerated* from Module2C.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('Module2C', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_35 
_st_.blockbegin()
try:
 load("../Code/generalPurposeMethods.sage")
 load("../Code/keyGeneration.sage")
 load("../Code/commonlyUsedFunctions.sage")
 keyFileName = "Module2"
 version = "C"
except:
 _st_.goboom(_sage_const_41 )
_st_.blockend()
_st_.current_tex_line = _sage_const_46 
_st_.blockbegin()
try:
 moduleNumber="2"
 problemNumber=_sage_const_6 
 load("../Code/02linear/linearParOrPer.sage")
except:
 _st_.goboom(_sage_const_50 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_0 , latex(displayStem))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_1 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_2 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_3 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_4 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_5 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_6 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_63 )
_st_.current_tex_line = _sage_const_64 
_st_.blockbegin()
try:
 moduleNumber="2"
 problemNumber=_sage_const_7 
 load("../Code/02linear/linearTwoPoints.sage")
except:
 _st_.goboom(_sage_const_68 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_7 , latex(displayStem))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_8 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_9 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_10 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_11 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_12 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_13 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_81 )
_st_.current_tex_line = _sage_const_82 
_st_.blockbegin()
try:
 moduleNumber="2"
 problemNumber=_sage_const_8 
 load("../Code/02linear/solveIntegerLinear.sage")
except:
 _st_.goboom(_sage_const_86 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_14 , latex(displayStem))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_15 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_16 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_17 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_18 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_19 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_20 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_99 )
_st_.current_tex_line = _sage_const_100 
_st_.blockbegin()
try:
 moduleNumber="2"
 problemNumber=_sage_const_9 
 load("../Code/02linear/solveRationalLinear.sage")
except:
 _st_.goboom(_sage_const_104 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_21 , latex(displayStem))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_22 , latex(displayProblem))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_23 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_24 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_25 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_26 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_27 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_117 )
_st_.current_tex_line = _sage_const_119 
_st_.blockbegin()
try:
   moduleNumber="2"
   problemNumber=_sage_const_10 
   load("../Code/02linear/linearGraphToStandard.sage")
   
except:
 _st_.goboom(_sage_const_123 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_28 , latex(displayStem))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_29 , latex(choices[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_30 , latex(choices[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_31 , latex(choices[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_32 , latex(choices[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_33 , latex(choices[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_138 )
_st_.endofdoc()

