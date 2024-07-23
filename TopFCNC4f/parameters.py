# This file was automatically created by FeynRules 2.4.35
# Mathematica version: 10.1.0  for Mac OS X x86 (64-bit) (March 24, 2015)
# Date: Thu 11 Feb 2016 16:03:33



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 172.5,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])
ii = 1

cpQ3x31 = Parameter(name = "cpQ3x31",	nature = "external",	type = "real",	value = 0.,	texname = "cpQ3x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cpQ3x32 = Parameter(name = "cpQ3x32",	nature = "external",	type = "real",	value = 0.,	texname = "cpQ3x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cpQ3Ix31 = Parameter(name = "cpQ3Ix31",	nature = "external",	type = "real",	value = 0.,	texname = "cpQ3Ix31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cpQ3Ix32 = Parameter(name = "cpQ3Ix32",	nature = "external",	type = "real",	value = 0.,	texname = "cpQ3Ix32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

cpQMx31 = Parameter(name = "cpQMx31",	nature = "external",	type = "real",	value = 0.,	texname = "cpQMx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cpQMx32 = Parameter(name = "cpQMx32",	nature = "external",	type = "real",	value = 0.,	texname = "cpQMx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cpQMIx31 = Parameter(name = "cpQMIx31",	nature = "external",	type = "real",	value = 0.,	texname = "cpQMIx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cpQMIx32 = Parameter(name = "cpQMIx32",	nature = "external",	type = "real",	value = 0.,	texname = "cpQMIx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

cptx31 = Parameter(name = "cptx31",	nature = "external",	type = "real",	value = 0.,	texname = "cptx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cptx32 = Parameter(name = "cptx32",	nature = "external",	type = "real",	value = 0.,	texname = "cptx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cptIx31 = Parameter(name = "cptIx31",	nature = "external",	type = "real",	value = 0.,	texname = "cptIx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cptIx32 = Parameter(name = "cptIx32",	nature = "external",	type = "real",	value = 0.,	texname = "cptIx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctGx13 = Parameter(name = "ctGx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctGx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGx23 = Parameter(name = "ctGx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctGx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGx31 = Parameter(name = "ctGx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctGx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGx32 = Parameter(name = "ctGx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctGx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGIx13 = Parameter(name = "ctGIx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctGIx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGIx23 = Parameter(name = "ctGIx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctGIx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGIx31 = Parameter(name = "ctGIx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctGIx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctGIx32 = Parameter(name = "ctGIx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctGIx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctAx13 = Parameter(name = "ctAx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctAx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAx23 = Parameter(name = "ctAx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctAx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAx31 = Parameter(name = "ctAx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctAx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAx32 = Parameter(name = "ctAx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctAx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAIx13 = Parameter(name = "ctAIx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctAIx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAIx23 = Parameter(name = "ctAIx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctAIx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAIx31 = Parameter(name = "ctAIx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctAIx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctAIx32 = Parameter(name = "ctAIx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctAIx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctZx13 = Parameter(name = "ctZx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctZx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZx23 = Parameter(name = "ctZx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctZx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZx31 = Parameter(name = "ctZx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctZx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZx32 = Parameter(name = "ctZx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctZx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZIx13 = Parameter(name = "ctZIx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctZIx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZIx23 = Parameter(name = "ctZIx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctZIx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZIx31 = Parameter(name = "ctZIx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctZIx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctZIx32 = Parameter(name = "ctZIx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctZIx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctpx13 = Parameter(name = "ctpx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctpx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpx23 = Parameter(name = "ctpx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctpx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpx31 = Parameter(name = "ctpx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctpx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpx32 = Parameter(name = "ctpx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctpx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpIx13 = Parameter(name = "ctpIx13",	nature = "external",	type = "real",	value = 0.,	texname = "ctpIx13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpIx23 = Parameter(name = "ctpIx23",	nature = "external",	type = "real",	value = 0.,	texname = "ctpIx23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpIx31 = Parameter(name = "ctpIx31",	nature = "external",	type = "real",	value = 0.,	texname = "ctpIx31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctpIx32 = Parameter(name = "ctpIx32",	nature = "external",	type = "real",	value = 0.,	texname = "ctpIx32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1


# 4f
## Qe
cQeIx1x31 = Parameter(name = "cQeIx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQeIx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQeIx1x32 = Parameter(name = "cQeIx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQeIx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQex1x31 = Parameter(name = "cQex1x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQex1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQex1x32 = Parameter(name = "cQex1x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQex1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMIx1x31 = Parameter(name = "cQlMIx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMIx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMIx1x32 = Parameter(name = "cQlMIx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMIx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMx1x31 = Parameter(name = "cQlMx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMx1x32 = Parameter(name = "cQlMx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

cQeIx2x31 = Parameter(name = "cQeIx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQeIx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQeIx2x32 = Parameter(name = "cQeIx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQeIx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQex2x31 = Parameter(name = "cQex2x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQex2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQex2x32 = Parameter(name = "cQex2x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQex2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMIx2x31 = Parameter(name = "cQlMIx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMIx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMIx2x32 = Parameter(name = "cQlMIx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMIx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMx2x31 = Parameter(name = "cQlMx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cQlMx2x32 = Parameter(name = "cQlMx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "cQlMx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

## te
ctex1x31 = Parameter(name = "ctex1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctex1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctex1x32 = Parameter(name = "ctex1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctex1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cteIx1x31 = Parameter(name = "cteIx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "cteIx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cteIx1x32 = Parameter(name = "cteIx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "cteIx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctex2x31 = Parameter(name = "ctex2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctex2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctex2x32 = Parameter(name = "ctex2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctex2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cteIx2x31 = Parameter(name = "cteIx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "cteIx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
cteIx2x32 = Parameter(name = "cteIx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "cteIx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

# tl
ctlx1x31 = Parameter(name = "ctlx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlx1x32 = Parameter(name = "ctlx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlIx1x31 = Parameter(name = "ctlIx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlIx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlIx1x32 = Parameter(name = "ctlIx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlIx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctlx2x31 = Parameter(name = "ctlx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlx2x32 = Parameter(name = "ctlx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlIx2x31 = Parameter(name = "ctlIx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlIx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlIx2x32 = Parameter(name = "ctlIx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlIx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1


# tlS
ctlSx1x13 = Parameter(name = "ctlSx1x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx1x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSx1x23 = Parameter(name = "ctlSx1x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx1x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSx1x31 = Parameter(name = "ctlSx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSx1x32 = Parameter(name = "ctlSx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx1x13 = Parameter(name = "ctlSIx1x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx1x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx1x23 = Parameter(name = "ctlSIx1x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx1x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx1x31 = Parameter(name = "ctlSIx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx1x32 = Parameter(name = "ctlSIx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctlSx2x13 = Parameter(name = "ctlSx2x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx2x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSx2x23 = Parameter(name = "ctlSx2x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx2x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSx2x31 = Parameter(name = "ctlSx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSx2x32 = Parameter(name = "ctlSx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx2x13 = Parameter(name = "ctlSIx2x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx2x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx2x23 = Parameter(name = "ctlSIx2x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx2x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx2x31 = Parameter(name = "ctlSIx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlSIx2x32 = Parameter(name = "ctlSIx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlSIx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1


# tlT
ctlTx1x13 = Parameter(name = "ctlTx1x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx1x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTx1x23 = Parameter(name = "ctlTx1x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx1x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTx1x31 = Parameter(name = "ctlTx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTx1x32 = Parameter(name = "ctlTx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx1x13 = Parameter(name = "ctlTIx1x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx1x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx1x23 = Parameter(name = "ctlTIx1x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx1x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx1x31 = Parameter(name = "ctlTIx1x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx1x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx1x32 = Parameter(name = "ctlTIx1x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx1x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1

ctlTx2x13 = Parameter(name = "ctlTx2x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx2x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTx2x23 = Parameter(name = "ctlTx2x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx2x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTx2x31 = Parameter(name = "ctlTx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTx2x32 = Parameter(name = "ctlTx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx2x13 = Parameter(name = "ctlTIx2x13",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx2x13",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx2x23 = Parameter(name = "ctlTIx2x23",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx2x23",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx2x31 = Parameter(name = "ctlTIx2x31",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx2x31",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1
ctlTIx2x32 = Parameter(name = "ctlTIx2x32",	nature = "external",	type = "real",	value = 0.,	texname = "ctlTIx2x32",	lhablock = "DIM6",	lhacode = [ ii ]); ii+=1



# NLOCT
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')


# by-hand conversion of ctw from ctA
ctWIx13 = Parameter(name = "ctWIx13",	nature = "internal",	type = "real",	value = 'sw*ctAIx13 + cw*ctZIx13',	texname = "ctWIx13")
ctWIx23 = Parameter(name = "ctWIx23",	nature = "internal",	type = "real",	value = 'sw*ctAIx23 + cw*ctZIx23',	texname = "ctWIx23")
ctWIx31 = Parameter(name = "ctWIx31",	nature = "internal",	type = "real",	value = 'sw*ctAIx31 + cw*ctZIx31',	texname = "ctWIx31")
ctWIx32 = Parameter(name = "ctWIx32",	nature = "internal",	type = "real",	value = 'sw*ctAIx32 + cw*ctZIx32',	texname = "ctWIx32")
ctWx13  = Parameter(name = "ctWx13",	nature = "internal",	type = "real",	value = 'sw*ctAx13 + cw*ctZx13',	texname = "ctWx13")
ctWx23  = Parameter(name = "ctWx23",	nature = "internal",	type = "real",	value = 'sw*ctAx23 + cw*ctZx23',	texname = "ctWx23")
ctWx31  = Parameter(name = "ctWx31",	nature = "internal",	type = "real",	value = 'sw*ctAx31 + cw*ctZx31',	texname = "ctWx31")
ctWx32  = Parameter(name = "ctWx32",	nature = "internal",	type = "real",	value = 'sw*ctAx32 + cw*ctZx32',	texname = "ctWx32")


IC1ctL = Parameter(name = "IC1ctL",	nature = "internal",	type = "real",	value = "(-1)*cpQMIx32+(-1)*cpQ3Ix32",	texname = "IC1ctL")
IC1ctR = Parameter(name = "IC1ctR",	nature = "internal",	type = "real",	value = "(-1)*cptIx32",	texname = "IC1ctR")
IC1utL = Parameter(name = "IC1utL",	nature = "internal",	type = "real",	value = "(-1)*cpQMIx31+(-1)*cpQ3Ix31",	texname = "IC1utL")
IC1utR = Parameter(name = "IC1utR",	nature = "internal",	type = "real",	value = "(-1)*cptIx31",	texname = "IC1utR")
IC3ctL = Parameter(name = "IC3ctL",	nature = "internal",	type = "real",	value = "(-1)*cpQ3Ix32",	texname = "IC3ctL")
IC3utL = Parameter(name = "IC3utL",	nature = "internal",	type = "real",	value = "(-1)*cpQ3Ix31",	texname = "IC3utL")
ICctB = Parameter(name = "ICctB",	nature = "internal",	type = "real",	value = "(cw)/(-ee*sw)*ctZIx32+(-cw**2)/(-ee*sw)*ctWIx32",	texname = "ICctB")
ICctG = Parameter(name = "ICctG",	nature = "internal",	type = "real",	value = "1/G*ctGIx32",	texname = "ICctG")
ICctW = Parameter(name = "ICctW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWIx32",	texname = "ICctW")
ICctphi = Parameter(name = "ICctphi",	nature = "internal",	type = "real",	value = "ctpIx32",	texname = "ICctphi")


ICtB = Parameter(name = "ICtB",	nature = "internal",	type = "real",	value = "(cw)/(-ee*sw)*ctZIx13+(-cw**2)/(-ee*sw)*ctWIx13",	texname = "ICtB")
ICtG = Parameter(name = "ICtG",	nature = "internal",	type = "real",	value = "1/G*ctGIx13",	texname = "ICtG")
ICtW = Parameter(name = "ICtW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWIx13",	texname = "ICtW")
ICtcB = Parameter(name = "ICtcB",	nature = "internal",	type = "real",	value = "(cw)/(-ee*sw)*ctZIx23+(-cw**2)/(-ee*sw)*ctWIx23",	texname = "ICtcB")
ICtcG = Parameter(name = "ICtcG",	nature = "internal",	type = "real",	value = "1/G*ctGIx23",	texname = "ICtcG")
ICtcW = Parameter(name = "ICtcW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWIx23",	texname = "ICtcW")
ICtcphi = Parameter(name = "ICtcphi",	nature = "internal",	type = "real",	value = "ctpIx23",	texname = "ICtcphi")
ICtphi = Parameter(name = "ICtphi",	nature = "internal",	type = "real",	value = "ctpIx13",	texname = "ICtphi")
ICuB = Parameter(name = "ICuB",	nature = "internal",	type = "real",	value = "(-cw**2)/(-ee*sw)*ctWIx31+(cw)/(-ee*sw)*ctZIx31",	texname = "ICuB")
ICuG = Parameter(name = "ICuG",	nature = "internal",	type = "real",	value = "1/G*ctGIx31",	texname = "ICuG")
ICuW = Parameter(name = "ICuW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWIx31",	texname = "ICuW")
ICuphi = Parameter(name = "ICuphi",	nature = "internal",	type = "real",	value = "ctpIx31",	texname = "ICuphi")
RC1ctL = Parameter(name = "RC1ctL",	nature = "internal",	type = "real",	value = "cpQMx32+cpQ3x32",	texname = "RC1ctL")
RC1ctR = Parameter(name = "RC1ctR",	nature = "internal",	type = "real",	value = "cptx32",	texname = "RC1ctR")
RC1utL = Parameter(name = "RC1utL",	nature = "internal",	type = "real",	value = "cpQ3x31+cpQMx31",	texname = "RC1utL")
RC1utR = Parameter(name = "RC1utR",	nature = "internal",	type = "real",	value = "cptx31",	texname = "RC1utR")
RC3ctL = Parameter(name = "RC3ctL",	nature = "internal",	type = "real",	value = "cpQ3x32",	texname = "RC3ctL")
RC3utL = Parameter(name = "RC3utL",	nature = "internal",	type = "real",	value = "cpQ3x31",	texname = "RC3utL")
RCctB = Parameter(name = "RCctB",	nature = "internal",	type = "real",	value = "(-cw**2)/(-ee*sw)*ctWx32+(cw)/(-ee*sw)*ctZx32",	texname = "RCctB")
RCctG = Parameter(name = "RCctG",	nature = "internal",	type = "real",	value = "1/G*ctGx32",	texname = "RCctG")
RCctW = Parameter(name = "RCctW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWx32",	texname = "RCctW")
RCctphi = Parameter(name = "RCctphi",	nature = "internal",	type = "real",	value = "ctpx32",	texname = "RCctphi")

RCtB = Parameter(name = "RCtB",	nature = "internal",	type = "real",	value = "(cw)/(-ee*sw)*ctZx13+(-cw**2)/(-ee*sw)*ctWx13",	texname = "RCtB")
RCtG = Parameter(name = "RCtG",	nature = "internal",	type = "real",	value = "1/G*ctGx13",	texname = "RCtG")
RCtW = Parameter(name = "RCtW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWx13",	texname = "RCtW")
RCtcB = Parameter(name = "RCtcB",	nature = "internal",	type = "real",	value = "(cw)/(-ee*sw)*ctZx23+(-cw**2)/(-ee*sw)*ctWx23",	texname = "RCtcB")
RCtcG = Parameter(name = "RCtcG",	nature = "internal",	type = "real",	value = "1/G*ctGx23",	texname = "RCtcG")
RCtcW = Parameter(name = "RCtcW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWx23",	texname = "RCtcW")
RCtcphi = Parameter(name = "RCtcphi",	nature = "internal",	type = "real",	value = "ctpx23",	texname = "RCtcphi")
RCtphi = Parameter(name = "RCtphi",	nature = "internal",	type = "real",	value = "ctpx13",	texname = "RCtphi")
RCuB = Parameter(name = "RCuB",	nature = "internal",	type = "real",	value = "(cw)/(-ee*sw)*ctZx31+(-cw**2)/(-ee*sw)*ctWx31",	texname = "RCuB")
RCuG = Parameter(name = "RCuG",	nature = "internal",	type = "real",	value = "1/G*ctGx31",	texname = "RCuG")
RCuW = Parameter(name = "RCuW",	nature = "internal",	type = "real",	value = "(sw)/(ee)*ctWx31",	texname = "RCuW")
RCuphi = Parameter(name = "RCuphi",	nature = "internal",	type = "real",	value = "ctpx31",	texname = "RCuphi")




cc = 'complexconjugate'

### eetu

RCeq13 = Parameter(name = "RCeq13",	nature = "internal",	type = "real",	value = "cQex1x31",	texname = "RCeq13")
RCeq23 = Parameter(name = "RCeq23",	nature = "internal",	type = "real",	value = "cQex1x32",	texname = "RCeq23")
RCeu13 = Parameter(name = "RCeu13",	nature = "internal",	type = "real",	value = "ctex1x31",	texname = "RCeu13")
RCeu23 = Parameter(name = "RCeu23",	nature = "internal",	type = "real",	value = "ctex1x32",	texname = "RCeu23")
RClequS13 = Parameter(name = "RClequS13",	nature = "internal",	type = "real",	value = "ctlSx1x13",	texname = "RClequS13")
RClequS23 = Parameter(name = "RClequS23",	nature = "internal",	type = "real",	value = "ctlSx1x23",	texname = "RClequS23")
RClequS31 = Parameter(name = "RClequS31",	nature = "internal",	type = "real",	value = "ctlSx1x31",	texname = "RClequS31")
RClequS32 = Parameter(name = "RClequS32",	nature = "internal",	type = "real",	value = "ctlSx1x32",	texname = "RClequS32")
RClequT13 = Parameter(name = "RClequT13",	nature = "internal",	type = "real",	value = "ctlTx1x13",	texname = "RClequT13")
RClequT23 = Parameter(name = "RClequT23",	nature = "internal",	type = "real",	value = "ctlTx1x23",	texname = "RClequT23")
RClequT31 = Parameter(name = "RClequT31",	nature = "internal",	type = "real",	value = "ctlTx1x31",	texname = "RClequT31")
RClequT32 = Parameter(name = "RClequT32",	nature = "internal",	type = "real",	value = "ctlTx1x32",	texname = "RClequT32")
RClqM13 = Parameter(name = "RClqM13",	nature = "internal",	type = "real",	value = "cQlMx1x31",	texname = "RClqM13")
RClqM23 = Parameter(name = "RClqM23",	nature = "internal",	type = "real",	value = "cQlMx1x32",	texname = "RClqM23")
RClu13 = Parameter(name = "RClu13",	nature = "internal",	type = "real",	value = "ctlx1x31",	texname = "RClu13")
RClu23 = Parameter(name = "RClu23",	nature = "internal",	type = "real",	value = "ctlx1x32",	texname = "RClu23")


ICeq13 = Parameter(name = "ICeq13",	nature = "internal",	type = "real",	value = "(-1)*cQeIx1x31",	texname = "ICeq13")
ICeq23 = Parameter(name = "ICeq23",	nature = "internal",	type = "real",	value = "(-1)*cQeIx1x32",	texname = "ICeq23")
ICeu13 = Parameter(name = "ICeu13",	nature = "internal",	type = "real",	value = "(-1)*cteIx1x31",	texname = "ICeu13")
ICeu23 = Parameter(name = "ICeu23",	nature = "internal",	type = "real",	value = "(-1)*cteIx1x32",	texname = "ICeu23")
IClequS13 = Parameter(name = "IClequS13",	nature = "internal",	type = "real",	value = "ctlSIx1x13",	texname = "IClequS13")
IClequS23 = Parameter(name = "IClequS23",	nature = "internal",	type = "real",	value = "ctlSIx1x23",	texname = "IClequS23")
IClequS31 = Parameter(name = "IClequS31",	nature = "internal",	type = "real",	value = "ctlSIx1x31",	texname = "IClequS31")
IClequS32 = Parameter(name = "IClequS32",	nature = "internal",	type = "real",	value = "ctlSIx1x32",	texname = "IClequS32")
IClequT13 = Parameter(name = "IClequT13",	nature = "internal",	type = "real",	value = "ctlTIx1x13",	texname = "IClequT13")
IClequT23 = Parameter(name = "IClequT23",	nature = "internal",	type = "real",	value = "ctlTIx1x23",	texname = "IClequT23")
IClequT31 = Parameter(name = "IClequT31",	nature = "internal",	type = "real",	value = "ctlTIx1x31",	texname = "IClequT31")
IClequT32 = Parameter(name = "IClequT32",	nature = "internal",	type = "real",	value = "ctlTIx1x32",	texname = "IClequT32")
IClqM13 = Parameter(name = "IClqM13",	nature = "internal",	type = "real",	value = "(-1)*cQlMIx1x31",	texname = "IClqM13")
IClqM23 = Parameter(name = "IClqM23",	nature = "internal",	type = "real",	value = "(-1)*cQlMIx1x32",	texname = "IClqM23")
IClu13 = Parameter(name = "IClu13",	nature = "internal",	type = "real",	value = "(-1)*ctlIx1x31",	texname = "IClu13")
IClu23 = Parameter(name = "IClu23",	nature = "internal",	type = "real",	value = "(-1)*ctlIx1x32",	texname = "IClu23")

ClqM13 = Parameter(name = 'ClqM13',	nature = 'internal',	type = 'complex',	value = 'RClqM13+complex(0,1)*IClqM13',	texname = "")
Clu13  = Parameter(name = 'Clu13',	nature = 'internal',	type = 'complex',	value = 'RClu13+complex(0,1)*IClu13',	texname = "")
Ceq13  = Parameter(name = 'Ceq13',	nature = 'internal',	type = 'complex',	value = 'RCeq13+complex(0,1)*ICeq13',	texname = "")
Ceu13  = Parameter(name = 'Ceu13',	nature = 'internal',	type = 'complex',	value = 'RCeu13+complex(0,1)*ICeu13',	texname = "")
ClqM31 = Parameter(name = 'ClqM31',	nature = 'internal',	type = 'complex',	value = cc+'(ClqM13)',	texname = "")
Clu31  = Parameter(name = 'Clu31',	nature = 'internal',	type = 'complex',	value = cc+'(Clu13)',	texname = "")
Ceq31  = Parameter(name = 'Ceq31',	nature = 'internal',	type = 'complex',	value = cc+'(Ceq13)',	texname = "")
Ceu31  = Parameter(name = 'Ceu31',	nature = 'internal',	type = 'complex',	value = cc+'(Ceu13)',	texname = "")

# 4f vector charm
ClqM23 = Parameter(name = 'ClqM23',	nature = 'internal',	type = 'complex',	value = 'RClqM23+complex(0,1)*IClqM23',	texname = "")
Clu23  = Parameter(name = 'Clu23',	nature = 'internal',	type = 'complex',	value = 'RClu23+complex(0,1)*IClu23',	texname = "")
Ceq23  = Parameter(name = 'Ceq23',	nature = 'internal',	type = 'complex',	value = 'RCeq23+complex(0,1)*ICeq23',	texname = "")
Ceu23  = Parameter(name = 'Ceu23',	nature = 'internal',	type = 'complex',	value = 'RCeu23+complex(0,1)*ICeu23',	texname = "")
ClqM32 = Parameter(name = 'ClqM32',	nature = 'internal',	type = 'complex',	value = cc+'(ClqM23)',	texname = "")
Clu32  = Parameter(name = 'Clu32',	nature = 'internal',	type = 'complex',	value = cc+'(Clu23)',	texname = "")
Ceq32  = Parameter(name = 'Ceq32',	nature = 'internal',	type = 'complex',	value = cc+'(Ceq23)',	texname = "")
Ceu32  = Parameter(name = 'Ceu32',	nature = 'internal',	type = 'complex',	value = cc+'(Ceu23)',	texname = "")
# 4f scalar up
ClequS31 = Parameter(name = 'ClequS31',	nature = 'internal',	type = 'complex',	value = 'RClequS31+complex(0,1)*IClequS31',	texname = "")
ClequS13 = Parameter(name = 'ClequS13',	nature = 'internal',	type = 'complex',	value = 'RClequS13+complex(0,1)*IClequS13',	texname = "")
# 4f scalar charm
ClequS32 = Parameter(name = 'ClequS32',	nature = 'internal',	type = 'complex',	value = 'RClequS32+complex(0,1)*IClequS32',	texname = "")
ClequS23 = Parameter(name = 'ClequS23',	nature = 'internal',	type = 'complex',	value = 'RClequS23+complex(0,1)*IClequS23',	texname = "")
# 4f tensor up
ClequT31 = Parameter(name = 'ClequT31',	nature = 'internal',	type = 'complex',	value = 'RClequT31+complex(0,1)*IClequT31',	texname = "")
ClequT13 = Parameter(name = 'ClequT13',	nature = 'internal',	type = 'complex',	value = 'RClequT13+complex(0,1)*IClequT13',	texname = "")
# 4f tensor charm
ClequT32 = Parameter(name = 'ClequT32',	nature = 'internal',	type = 'complex',	value = 'RClequT32+complex(0,1)*IClequT32',	texname = "")
ClequT23 = Parameter(name = 'ClequT23',	nature = 'internal',	type = 'complex',	value = 'RClequT23+complex(0,1)*IClequT23',	texname = "")


### mumutu

RCeq13mu = Parameter(name = "RCeq13mu",	nature = "internal",	type = "real",	value = "cQex2x31",	texname = "RCeq13mu")
RCeq23mu = Parameter(name = "RCeq23mu",	nature = "internal",	type = "real",	value = "cQex2x32",	texname = "RCeq23mu")
RCeu13mu = Parameter(name = "RCeu13mu",	nature = "internal",	type = "real",	value = "ctex2x31",	texname = "RCeu13mu")
RCeu23mu = Parameter(name = "RCeu23mu",	nature = "internal",	type = "real",	value = "ctex2x32",	texname = "RCeu23mu")
RClequS13mu = Parameter(name = "RClequS13mu",	nature = "internal",	type = "real",	value = "ctlSx2x13",	texname = "RClequS13mu")
RClequS23mu = Parameter(name = "RClequS23mu",	nature = "internal",	type = "real",	value = "ctlSx2x23",	texname = "RClequS23mu")
RClequS31mu = Parameter(name = "RClequS31mu",	nature = "internal",	type = "real",	value = "ctlSx2x31",	texname = "RClequS31mu")
RClequS32mu = Parameter(name = "RClequS32mu",	nature = "internal",	type = "real",	value = "ctlSx2x32",	texname = "RClequS32mu")
RClequT13mu = Parameter(name = "RClequT13mu",	nature = "internal",	type = "real",	value = "ctlTx2x13",	texname = "RClequT13mu")
RClequT23mu = Parameter(name = "RClequT23mu",	nature = "internal",	type = "real",	value = "ctlTx2x23",	texname = "RClequT23mu")
RClequT31mu = Parameter(name = "RClequT31mu",	nature = "internal",	type = "real",	value = "ctlTx2x31",	texname = "RClequT31mu")
RClequT32mu = Parameter(name = "RClequT32mu",	nature = "internal",	type = "real",	value = "ctlTx2x32",	texname = "RClequT32mu")
RClqM13mu = Parameter(name = "RClqM13mu",	nature = "internal",	type = "real",	value = "cQlMx2x31",	texname = "RClqM13mu")
RClqM23mu = Parameter(name = "RClqM23mu",	nature = "internal",	type = "real",	value = "cQlMx2x32",	texname = "RClqM23mu")
RClu13mu = Parameter(name = "RClu13mu",	nature = "internal",	type = "real",	value = "ctlx2x31",	texname = "RClu13mu")
RClu23mu = Parameter(name = "RClu23mu",	nature = "internal",	type = "real",	value = "ctlx2x32",	texname = "RClu23mu")


ICeq13mu = Parameter(name = "ICeq13mu",	nature = "internal",	type = "real",	value = "(-1)*cQeIx2x31",	texname = "ICeq13mu")
ICeq23mu = Parameter(name = "ICeq23mu",	nature = "internal",	type = "real",	value = "(-1)*cQeIx2x32",	texname = "ICeq23mu")
ICeu13mu = Parameter(name = "ICeu13mu",	nature = "internal",	type = "real",	value = "(-1)*cteIx2x31",	texname = "ICeu13mu")
ICeu23mu = Parameter(name = "ICeu23mu",	nature = "internal",	type = "real",	value = "(-1)*cteIx2x32",	texname = "ICeu23mu")
IClequS13mu = Parameter(name = "IClequS13mu",	nature = "internal",	type = "real",	value = "ctlSIx2x13",	texname = "IClequS13mu")
IClequS23mu = Parameter(name = "IClequS23mu",	nature = "internal",	type = "real",	value = "ctlSIx2x23",	texname = "IClequS23mu")
IClequS31mu = Parameter(name = "IClequS31mu",	nature = "internal",	type = "real",	value = "ctlSIx2x31",	texname = "IClequS31mu")
IClequS32mu = Parameter(name = "IClequS32mu",	nature = "internal",	type = "real",	value = "ctlSIx2x32",	texname = "IClequS32mu")
IClequT13mu = Parameter(name = "IClequT13mu",	nature = "internal",	type = "real",	value = "ctlTIx2x13",	texname = "IClequT13mu")
IClequT23mu = Parameter(name = "IClequT23mu",	nature = "internal",	type = "real",	value = "ctlTIx2x23",	texname = "IClequT23mu")
IClequT31mu = Parameter(name = "IClequT31mu",	nature = "internal",	type = "real",	value = "ctlTIx2x31",	texname = "IClequT31mu")
IClequT32mu = Parameter(name = "IClequT32mu",	nature = "internal",	type = "real",	value = "ctlTIx2x32",	texname = "IClequT32mu")
IClqM13mu = Parameter(name = "IClqM13mu",	nature = "internal",	type = "real",	value = "(-1)*cQlMIx2x31",	texname = "IClqM13mu")
IClqM23mu = Parameter(name = "IClqM23mu",	nature = "internal",	type = "real",	value = "(-1)*cQlMIx2x32",	texname = "IClqM23mu")
IClu13mu = Parameter(name = "IClu13mu",	nature = "internal",	type = "real",	value = "(-1)*ctlIx2x31",	texname = "IClu13mu")
IClu23mu = Parameter(name = "IClu23mu",	nature = "internal",	type = "real",	value = "(-1)*ctlIx2x32",	texname = "IClu23mu")

ClqM13mu = Parameter(name = 'ClqM13mu',	nature = 'internal',	type = 'complex',	value = 'RClqM13mu+complex(0,1)*IClqM13mu',	texname = "")
Clu13mu  = Parameter(name = 'Clu13mu',	nature = 'internal',	type = 'complex',	value = 'RClu13mu+complex(0,1)*IClu13mu',	texname = "")
Ceq13mu  = Parameter(name = 'Ceq13mu',	nature = 'internal',	type = 'complex',	value = 'RCeq13mu+complex(0,1)*ICeq13mu',	texname = "")
Ceu13mu  = Parameter(name = 'Ceu13mu',	nature = 'internal',	type = 'complex',	value = 'RCeu13mu+complex(0,1)*ICeu13mu',	texname = "")
ClqM31mu = Parameter(name = 'ClqM31mu',	nature = 'internal',	type = 'complex',	value = cc+'(ClqM13mu)',	texname = "")
Clu31mu  = Parameter(name = 'Clu31mu',	nature = 'internal',	type = 'complex',	value = cc+'(Clu13mu)',	texname = "")
Ceq31mu  = Parameter(name = 'Ceq31mu',	nature = 'internal',	type = 'complex',	value = cc+'(Ceq13mu)',	texname = "")
Ceu31mu  = Parameter(name = 'Ceu31mu',	nature = 'internal',	type = 'complex',	value = cc+'(Ceu13mu)',	texname = "")

# 4f vector charm
ClqM23mu = Parameter(name = 'ClqM23mu',	nature = 'internal',	type = 'complex',	value = 'RClqM23mu+complex(0,1)*IClqM23mu',	texname = "")
Clu23mu  = Parameter(name = 'Clu23mu',	nature = 'internal',	type = 'complex',	value = 'RClu23mu+complex(0,1)*IClu23mu',	texname = "")
Ceq23mu  = Parameter(name = 'Ceq23mu',	nature = 'internal',	type = 'complex',	value = 'RCeq23mu+complex(0,1)*ICeq23mu',	texname = "")
Ceu23mu  = Parameter(name = 'Ceu23mu',	nature = 'internal',	type = 'complex',	value = 'RCeu23mu+complex(0,1)*ICeu23mu',	texname = "")
ClqM32mu = Parameter(name = 'ClqM32mu',	nature = 'internal',	type = 'complex',	value = cc+'(ClqM23mu)',	texname = "")
Clu32mu  = Parameter(name = 'Clu32mu',	nature = 'internal',	type = 'complex',	value = cc+'(Clu23mu)',	texname = "")
Ceq32mu  = Parameter(name = 'Ceq32mu',	nature = 'internal',	type = 'complex',	value = cc+'(Ceq23mu)',	texname = "")
Ceu32mu  = Parameter(name = 'Ceu32mu',	nature = 'internal',	type = 'complex',	value = cc+'(Ceu23mu)',	texname = "")
# 4f scalar up
ClequS31mu = Parameter(name = 'ClequS31mu',	nature = 'internal',	type = 'complex',	value = 'RClequS31mu+complex(0,1)*IClequS31mu',	texname = "")
ClequS13mu = Parameter(name = 'ClequS13mu',	nature = 'internal',	type = 'complex',	value = 'RClequS13mu+complex(0,1)*IClequS13mu',	texname = "")
# 4f scalar charm
ClequS32mu = Parameter(name = 'ClequS32mu',	nature = 'internal',	type = 'complex',	value = 'RClequS32mu+complex(0,1)*IClequS32mu',	texname = "")
ClequS23mu = Parameter(name = 'ClequS23mu',	nature = 'internal',	type = 'complex',	value = 'RClequS23mu+complex(0,1)*IClequS23mu',	texname = "")
# 4f tensor up
ClequT31mu = Parameter(name = 'ClequT31mu',	nature = 'internal',	type = 'complex',	value = 'RClequT31mu+complex(0,1)*IClequT31mu',	texname = "")
ClequT13mu = Parameter(name = 'ClequT13mu',	nature = 'internal',	type = 'complex',	value = 'RClequT13mu+complex(0,1)*IClequT13mu',	texname = "")
# 4f tensor charm
ClequT32mu = Parameter(name = 'ClequT32mu',	nature = 'internal',	type = 'complex',	value = 'RClequT32mu+complex(0,1)*IClequT32mu',	texname = "")
ClequT23mu = Parameter(name = 'ClequT23mu',	nature = 'internal',	type = 'complex',	value = 'RClequT23mu+complex(0,1)*IClequT23mu',	texname = "")





## NLOCT
# User-defined parameters.
Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1000,
                   texname = '\\Lambda',
                   lhablock = 'DIM6',
                   lhacode = [ 0 ])


ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.5,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])


MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.5,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

C1ctL = Parameter(name = 'C1ctL',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*IC1ctL + RC1ctL',
                  texname = '\\text{Subsuperscript}[C,\\text{ctL},1]')

C1ctR = Parameter(name = 'C1ctR',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*IC1ctR + RC1ctR',
                  texname = '\\text{Subsuperscript}[C,\\text{ctR},1]')

C1utL = Parameter(name = 'C1utL',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*IC1utL + RC1utL',
                  texname = '\\text{Subsuperscript}[C,\\text{utL},1]')

C1utR = Parameter(name = 'C1utR',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*IC1utR + RC1utR',
                  texname = '\\text{Subsuperscript}[C,\\text{utR},1]')

C3ctL = Parameter(name = 'C3ctL',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*IC3ctL + RC3ctL',
                  texname = '\\text{Subsuperscript}[C,\\text{ctL},3]')

C3utL = Parameter(name = 'C3utL',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*IC3utL + RC3utL',
                  texname = '\\text{Subsuperscript}[C,\\text{utL},3]')

CctB = Parameter(name = 'CctB',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ICctB + RCctB',
                 texname = 'C_{\\text{ctB}}')

CctG = Parameter(name = 'CctG',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ICctG + RCctG',
                 texname = 'C_{\\text{ctG}}')

Cctphi = Parameter(name = 'Cctphi',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*ICctphi + RCctphi',
                   texname = 'C_{\\text{ct$\\phi $}}')

CctW = Parameter(name = 'CctW',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ICctW + RCctW',
                 texname = 'C_{\\text{ctW}}')

CtB = Parameter(name = 'CtB',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*ICtB + RCtB',
                texname = 'C_{\\text{tB}}')

CtcB = Parameter(name = 'CtcB',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ICtcB + RCtcB',
                 texname = 'C_{\\text{tcB}}')

CtcG = Parameter(name = 'CtcG',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ICtcG + RCtcG',
                 texname = 'C_{\\text{tcG}}')

Ctcphi = Parameter(name = 'Ctcphi',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*ICtcphi + RCtcphi',
                   texname = 'C_{\\text{tc$\\phi $}}')

CtcW = Parameter(name = 'CtcW',
                 nature = 'internal',
                 type = 'complex',
                 value = 'complex(0,1)*ICtcW + RCtcW',
                 texname = 'C_{\\text{tcW}}')

CtG = Parameter(name = 'CtG',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*ICtG + RCtG',
                texname = 'C_{\\text{tG}}')

Ctphi = Parameter(name = 'Ctphi',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*ICtphi + RCtphi',
                  texname = 'C_{\\text{t$\\phi $}}')

CtW = Parameter(name = 'CtW',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*ICtW + RCtW',
                texname = 'C_{\\text{tW}}')

CuB = Parameter(name = 'CuB',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*ICuB + RCuB',
                texname = 'C_{\\text{uB}}')

CuG = Parameter(name = 'CuG',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*ICuG + RCuG',
                texname = 'C_{\\text{uG}}')

Cuphi = Parameter(name = 'Cuphi',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)*ICuphi + RCuphi',
                  texname = 'C_{\\text{u$\\phi $}}')

CuW = Parameter(name = 'CuW',
                nature = 'internal',
                type = 'complex',
                value = 'complex(0,1)*ICuW + RCuW',
                texname = 'C_{\\text{uW}}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

