# Generated from QuantumLanguageLexer.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))


def serializedATN():
    return [
        4,0,81,509,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,1,0,4,0,161,8,0,11,0,12,0,162,1,0,1,0,1,1,1,1,5,1,169,8,
        1,10,1,12,1,172,9,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,
        1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,
        1,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,42,1,42,1,43,
        1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,
        1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,50,1,50,
        1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,
        1,56,1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,1,62,
        1,62,1,63,1,63,1,64,1,64,1,64,3,64,401,8,64,1,64,1,64,3,64,405,8,
        64,1,64,3,64,408,8,64,3,64,410,8,64,1,64,1,64,1,65,1,65,1,66,1,66,
        1,66,1,66,1,67,1,67,1,68,1,68,1,69,1,69,1,70,1,70,5,70,428,8,70,
        10,70,12,70,431,9,70,1,71,1,71,1,71,5,71,436,8,71,10,71,12,71,439,
        9,71,1,71,1,71,1,72,1,72,1,72,5,72,446,8,72,10,72,12,72,449,9,72,
        1,72,1,72,1,73,1,73,5,73,455,8,73,10,73,12,73,458,9,73,1,73,1,73,
        1,73,5,73,463,8,73,10,73,12,73,466,9,73,1,73,3,73,469,8,73,1,74,
        1,74,5,74,473,8,74,10,74,12,74,476,9,74,1,74,3,74,479,8,74,1,75,
        1,75,3,75,483,8,75,1,75,1,75,1,76,1,76,1,76,4,76,490,8,76,11,76,
        12,76,491,1,77,1,77,4,77,496,8,77,11,77,12,77,497,1,77,1,77,1,78,
        1,78,4,78,504,8,78,11,78,12,78,505,1,78,1,78,2,456,464,0,79,1,3,
        3,4,5,5,7,6,9,7,11,8,13,9,15,10,17,11,19,12,21,13,23,14,25,15,27,
        16,29,17,31,18,33,19,35,20,37,21,39,22,41,23,43,24,45,25,47,26,49,
        27,51,28,53,29,55,30,57,31,59,32,61,33,63,34,65,35,67,36,69,37,71,
        38,73,39,75,40,77,41,79,42,81,43,83,44,85,45,87,46,89,47,91,48,93,
        49,95,50,97,51,99,52,101,53,103,54,105,55,107,56,109,57,111,58,113,
        59,115,60,117,61,119,62,121,63,123,64,125,65,127,66,129,67,131,68,
        133,69,135,70,137,71,139,72,141,73,143,74,145,75,147,76,149,77,151,
        78,153,79,155,80,157,81,1,0,9,2,0,9,9,32,32,2,0,10,10,12,13,2,0,
        65,90,97,122,4,0,48,57,65,90,95,95,97,122,1,0,49,57,1,0,48,57,1,
        0,48,48,2,0,74,74,106,106,3,0,43,43,45,45,48,49,526,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,
        1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,
        1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,
        1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,
        1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,
        1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,
        1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,
        1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,
        1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,
        0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,
        0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,
        131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,
        0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,
        1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,
        1,160,1,0,0,0,3,166,1,0,0,0,5,175,1,0,0,0,7,177,1,0,0,0,9,179,1,
        0,0,0,11,181,1,0,0,0,13,183,1,0,0,0,15,186,1,0,0,0,17,188,1,0,0,
        0,19,191,1,0,0,0,21,193,1,0,0,0,23,195,1,0,0,0,25,198,1,0,0,0,27,
        201,1,0,0,0,29,204,1,0,0,0,31,207,1,0,0,0,33,210,1,0,0,0,35,212,
        1,0,0,0,37,216,1,0,0,0,39,223,1,0,0,0,41,229,1,0,0,0,43,236,1,0,
        0,0,45,239,1,0,0,0,47,244,1,0,0,0,49,249,1,0,0,0,51,255,1,0,0,0,
        53,259,1,0,0,0,55,262,1,0,0,0,57,266,1,0,0,0,59,274,1,0,0,0,61,281,
        1,0,0,0,63,284,1,0,0,0,65,288,1,0,0,0,67,292,1,0,0,0,69,295,1,0,
        0,0,71,300,1,0,0,0,73,305,1,0,0,0,75,311,1,0,0,0,77,317,1,0,0,0,
        79,322,1,0,0,0,81,331,1,0,0,0,83,337,1,0,0,0,85,339,1,0,0,0,87,341,
        1,0,0,0,89,343,1,0,0,0,91,345,1,0,0,0,93,347,1,0,0,0,95,351,1,0,
        0,0,97,359,1,0,0,0,99,363,1,0,0,0,101,366,1,0,0,0,103,369,1,0,0,
        0,105,372,1,0,0,0,107,375,1,0,0,0,109,377,1,0,0,0,111,379,1,0,0,
        0,113,381,1,0,0,0,115,383,1,0,0,0,117,385,1,0,0,0,119,387,1,0,0,
        0,121,389,1,0,0,0,123,391,1,0,0,0,125,393,1,0,0,0,127,395,1,0,0,
        0,129,409,1,0,0,0,131,413,1,0,0,0,133,415,1,0,0,0,135,419,1,0,0,
        0,137,421,1,0,0,0,139,423,1,0,0,0,141,425,1,0,0,0,143,432,1,0,0,
        0,145,442,1,0,0,0,147,468,1,0,0,0,149,478,1,0,0,0,151,482,1,0,0,
        0,153,486,1,0,0,0,155,493,1,0,0,0,157,501,1,0,0,0,159,161,7,0,0,
        0,160,159,1,0,0,0,161,162,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,
        0,163,164,1,0,0,0,164,165,6,0,0,0,165,2,1,0,0,0,166,170,5,35,0,0,
        167,169,8,1,0,0,168,167,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,
        170,171,1,0,0,0,171,173,1,0,0,0,172,170,1,0,0,0,173,174,6,1,0,0,
        174,4,1,0,0,0,175,176,5,43,0,0,176,6,1,0,0,0,177,178,5,45,0,0,178,
        8,1,0,0,0,179,180,5,42,0,0,180,10,1,0,0,0,181,182,5,47,0,0,182,12,
        1,0,0,0,183,184,5,47,0,0,184,185,5,47,0,0,185,14,1,0,0,0,186,187,
        5,37,0,0,187,16,1,0,0,0,188,189,5,42,0,0,189,190,5,42,0,0,190,18,
        1,0,0,0,191,192,5,60,0,0,192,20,1,0,0,0,193,194,5,62,0,0,194,22,
        1,0,0,0,195,196,5,61,0,0,196,197,5,61,0,0,197,24,1,0,0,0,198,199,
        5,62,0,0,199,200,5,61,0,0,200,26,1,0,0,0,201,202,5,60,0,0,202,203,
        5,61,0,0,203,28,1,0,0,0,204,205,5,60,0,0,205,206,5,62,0,0,206,30,
        1,0,0,0,207,208,5,33,0,0,208,209,5,61,0,0,209,32,1,0,0,0,210,211,
        5,61,0,0,211,34,1,0,0,0,212,213,5,100,0,0,213,214,5,101,0,0,214,
        215,5,102,0,0,215,36,1,0,0,0,216,217,5,114,0,0,217,218,5,101,0,0,
        218,219,5,116,0,0,219,220,5,117,0,0,220,221,5,114,0,0,221,222,5,
        110,0,0,222,38,1,0,0,0,223,224,5,114,0,0,224,225,5,97,0,0,225,226,
        5,105,0,0,226,227,5,115,0,0,227,228,5,101,0,0,228,40,1,0,0,0,229,
        230,5,97,0,0,230,231,5,115,0,0,231,232,5,115,0,0,232,233,5,101,0,
        0,233,234,5,114,0,0,234,235,5,116,0,0,235,42,1,0,0,0,236,237,5,105,
        0,0,237,238,5,102,0,0,238,44,1,0,0,0,239,240,5,101,0,0,240,241,5,
        108,0,0,241,242,5,105,0,0,242,243,5,102,0,0,243,46,1,0,0,0,244,245,
        5,101,0,0,245,246,5,108,0,0,246,247,5,115,0,0,247,248,5,101,0,0,
        248,48,1,0,0,0,249,250,5,119,0,0,250,251,5,104,0,0,251,252,5,105,
        0,0,252,253,5,108,0,0,253,254,5,101,0,0,254,50,1,0,0,0,255,256,5,
        102,0,0,256,257,5,111,0,0,257,258,5,114,0,0,258,52,1,0,0,0,259,260,
        5,105,0,0,260,261,5,110,0,0,261,54,1,0,0,0,262,263,5,116,0,0,263,
        264,5,114,0,0,264,265,5,121,0,0,265,56,1,0,0,0,266,267,5,102,0,0,
        267,268,5,105,0,0,268,269,5,110,0,0,269,270,5,97,0,0,270,271,5,108,
        0,0,271,272,5,108,0,0,272,273,5,121,0,0,273,58,1,0,0,0,274,275,5,
        101,0,0,275,276,5,120,0,0,276,277,5,99,0,0,277,278,5,101,0,0,278,
        279,5,112,0,0,279,280,5,116,0,0,280,60,1,0,0,0,281,282,5,111,0,0,
        282,283,5,114,0,0,283,62,1,0,0,0,284,285,5,97,0,0,285,286,5,110,
        0,0,286,287,5,100,0,0,287,64,1,0,0,0,288,289,5,110,0,0,289,290,5,
        111,0,0,290,291,5,116,0,0,291,66,1,0,0,0,292,293,5,105,0,0,293,294,
        5,115,0,0,294,68,1,0,0,0,295,296,5,78,0,0,296,297,5,111,0,0,297,
        298,5,110,0,0,298,299,5,101,0,0,299,70,1,0,0,0,300,301,5,84,0,0,
        301,302,5,114,0,0,302,303,5,117,0,0,303,304,5,101,0,0,304,72,1,0,
        0,0,305,306,5,70,0,0,306,307,5,97,0,0,307,308,5,108,0,0,308,309,
        5,115,0,0,309,310,5,101,0,0,310,74,1,0,0,0,311,312,5,99,0,0,312,
        313,5,108,0,0,313,314,5,97,0,0,314,315,5,115,0,0,315,316,5,115,0,
        0,316,76,1,0,0,0,317,318,5,112,0,0,318,319,5,97,0,0,319,320,5,115,
        0,0,320,321,5,115,0,0,321,78,1,0,0,0,322,323,5,99,0,0,323,324,5,
        111,0,0,324,325,5,110,0,0,325,326,5,116,0,0,326,327,5,105,0,0,327,
        328,5,110,0,0,328,329,5,117,0,0,329,330,5,101,0,0,330,80,1,0,0,0,
        331,332,5,98,0,0,332,333,5,114,0,0,333,334,5,101,0,0,334,335,5,97,
        0,0,335,336,5,107,0,0,336,82,1,0,0,0,337,338,5,88,0,0,338,84,1,0,
        0,0,339,340,5,72,0,0,340,86,1,0,0,0,341,342,5,90,0,0,342,88,1,0,
        0,0,343,344,5,89,0,0,344,90,1,0,0,0,345,346,5,83,0,0,346,92,1,0,
        0,0,347,348,5,83,0,0,348,349,5,68,0,0,349,350,5,71,0,0,350,94,1,
        0,0,0,351,352,5,84,0,0,352,353,5,111,0,0,353,354,5,102,0,0,354,355,
        5,102,0,0,355,356,5,111,0,0,356,357,5,108,0,0,357,358,5,105,0,0,
        358,96,1,0,0,0,359,360,5,84,0,0,360,361,5,68,0,0,361,362,5,71,0,
        0,362,98,1,0,0,0,363,364,5,82,0,0,364,365,5,88,0,0,365,100,1,0,0,
        0,366,367,5,82,0,0,367,368,5,89,0,0,368,102,1,0,0,0,369,370,5,82,
        0,0,370,371,5,90,0,0,371,104,1,0,0,0,372,373,5,67,0,0,373,374,5,
        88,0,0,374,106,1,0,0,0,375,376,5,80,0,0,376,108,1,0,0,0,377,378,
        5,40,0,0,378,110,1,0,0,0,379,380,5,41,0,0,380,112,1,0,0,0,381,382,
        5,91,0,0,382,114,1,0,0,0,383,384,5,93,0,0,384,116,1,0,0,0,385,386,
        5,123,0,0,386,118,1,0,0,0,387,388,5,125,0,0,388,120,1,0,0,0,389,
        390,5,46,0,0,390,122,1,0,0,0,391,392,5,44,0,0,392,124,1,0,0,0,393,
        394,5,58,0,0,394,126,1,0,0,0,395,396,5,59,0,0,396,128,1,0,0,0,397,
        398,4,64,0,0,398,410,3,1,0,0,399,401,5,13,0,0,400,399,1,0,0,0,400,
        401,1,0,0,0,401,402,1,0,0,0,402,405,5,10,0,0,403,405,2,12,13,0,404,
        400,1,0,0,0,404,403,1,0,0,0,405,407,1,0,0,0,406,408,3,1,0,0,407,
        406,1,0,0,0,407,408,1,0,0,0,408,410,1,0,0,0,409,397,1,0,0,0,409,
        404,1,0,0,0,410,411,1,0,0,0,411,412,6,64,1,0,412,130,1,0,0,0,413,
        414,5,64,0,0,414,132,1,0,0,0,415,416,5,40,0,0,416,417,5,88,0,0,417,
        418,5,41,0,0,418,134,1,0,0,0,419,420,5,84,0,0,420,136,1,0,0,0,421,
        422,5,39,0,0,422,138,1,0,0,0,423,424,5,116,0,0,424,140,1,0,0,0,425,
        429,7,2,0,0,426,428,7,3,0,0,427,426,1,0,0,0,428,431,1,0,0,0,429,
        427,1,0,0,0,429,430,1,0,0,0,430,142,1,0,0,0,431,429,1,0,0,0,432,
        433,5,124,0,0,433,437,7,2,0,0,434,436,7,3,0,0,435,434,1,0,0,0,436,
        439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,440,1,0,0,0,439,
        437,1,0,0,0,440,441,5,62,0,0,441,144,1,0,0,0,442,443,5,60,0,0,443,
        447,7,2,0,0,444,446,7,3,0,0,445,444,1,0,0,0,446,449,1,0,0,0,447,
        445,1,0,0,0,447,448,1,0,0,0,448,450,1,0,0,0,449,447,1,0,0,0,450,
        451,5,124,0,0,451,146,1,0,0,0,452,456,5,39,0,0,453,455,9,0,0,0,454,
        453,1,0,0,0,455,458,1,0,0,0,456,457,1,0,0,0,456,454,1,0,0,0,457,
        459,1,0,0,0,458,456,1,0,0,0,459,469,5,39,0,0,460,464,5,34,0,0,461,
        463,9,0,0,0,462,461,1,0,0,0,463,466,1,0,0,0,464,465,1,0,0,0,464,
        462,1,0,0,0,465,467,1,0,0,0,466,464,1,0,0,0,467,469,5,34,0,0,468,
        452,1,0,0,0,468,460,1,0,0,0,469,148,1,0,0,0,470,474,7,4,0,0,471,
        473,7,5,0,0,472,471,1,0,0,0,473,476,1,0,0,0,474,472,1,0,0,0,474,
        475,1,0,0,0,475,479,1,0,0,0,476,474,1,0,0,0,477,479,7,6,0,0,478,
        470,1,0,0,0,478,477,1,0,0,0,479,150,1,0,0,0,480,483,3,153,76,0,481,
        483,3,149,74,0,482,480,1,0,0,0,482,481,1,0,0,0,483,484,1,0,0,0,484,
        485,7,7,0,0,485,152,1,0,0,0,486,487,3,149,74,0,487,489,5,46,0,0,
        488,490,7,5,0,0,489,488,1,0,0,0,490,491,1,0,0,0,491,489,1,0,0,0,
        491,492,1,0,0,0,492,154,1,0,0,0,493,495,5,124,0,0,494,496,7,8,0,
        0,495,494,1,0,0,0,496,497,1,0,0,0,497,495,1,0,0,0,497,498,1,0,0,
        0,498,499,1,0,0,0,499,500,5,62,0,0,500,156,1,0,0,0,501,503,5,60,
        0,0,502,504,7,8,0,0,503,502,1,0,0,0,504,505,1,0,0,0,505,503,1,0,
        0,0,505,506,1,0,0,0,506,507,1,0,0,0,507,508,5,124,0,0,508,158,1,
        0,0,0,19,0,162,170,400,404,407,409,429,437,447,456,464,468,474,478,
        482,491,497,505,2,6,0,0,1,64,0
    ]

class QuantumLanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    SPACES = 3
    COMMENTS = 4
    ADD = 5
    MINUS = 6
    STAR = 7
    DIV = 8
    IDIV = 9
    MOD = 10
    POWER = 11
    LESS_THAN = 12
    GREATER_THAN = 13
    EQUALS = 14
    GT_EQ = 15
    LT_EQ = 16
    NOT_EQ_1 = 17
    NOT_EQ_2 = 18
    ASSIGN = 19
    DEF = 20
    RETURN = 21
    RAISE = 22
    ASSERT = 23
    IF = 24
    ELIF = 25
    ELSE = 26
    WHILE = 27
    FOR = 28
    IN = 29
    TRY = 30
    FINALLY = 31
    EXCEPT = 32
    OR = 33
    AND = 34
    NOT = 35
    IS = 36
    NONE = 37
    TRUE = 38
    FALSE = 39
    CLASS = 40
    PASS = 41
    CONTINUE = 42
    BREAK = 43
    X = 44
    H = 45
    Z = 46
    Y = 47
    S = 48
    SDG = 49
    T = 50
    TDG = 51
    RX = 52
    RY = 53
    RZ = 54
    CX = 55
    P = 56
    OPEN_PAREN = 57
    CLOSE_PAREN = 58
    OPEN_BRACK = 59
    CLOSE_BRACK = 60
    OPEN_BRACE = 61
    CLOSE_BRACE = 62
    DOT = 63
    COMMA = 64
    COLON = 65
    SEMI_COLON = 66
    NEWLINE = 67
    MATMUL = 68
    KRONECKER = 69
    HERMITIAN = 70
    CONJUGATE = 71
    TRANSPOSE = 72
    IDENTIFIER = 73
    QUBIT_IDENTIFIER = 74
    QUBIT_TRANSPOSE_IDENTIFIER = 75
    STRING_LITERAL = 76
    INTEGER_LITERAL = 77
    IMAGINARY_LITERAL = 78
    FLOAT_LITERAL = 79
    QUBIT_STATE_LITERAL = 80
    QUBIT_TRANSPOSE_STATE_LITERAL = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", "'**'", "'<'", "'>'", 
            "'=='", "'>='", "'<='", "'<>'", "'!='", "'='", "'def'", "'return'", 
            "'raise'", "'assert'", "'if'", "'elif'", "'else'", "'while'", 
            "'for'", "'in'", "'try'", "'finally'", "'except'", "'or'", "'and'", 
            "'not'", "'is'", "'None'", "'True'", "'False'", "'class'", "'pass'", 
            "'continue'", "'break'", "'X'", "'H'", "'Z'", "'Y'", "'S'", 
            "'SDG'", "'Toffoli'", "'TDG'", "'RX'", "'RY'", "'RZ'", "'CX'", 
            "'P'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", 
            "':'", "';'", "'@'", "'(X)'", "'T'", "'''", "'t'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "SPACES", "COMMENTS", "ADD", "MINUS", "STAR", 
            "DIV", "IDIV", "MOD", "POWER", "LESS_THAN", "GREATER_THAN", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", 
            "DEF", "RETURN", "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
            "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", "NOT", 
            "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", "CONTINUE", 
            "BREAK", "X", "H", "Z", "Y", "S", "SDG", "T", "TDG", "RX", "RY", 
            "RZ", "CX", "P", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
            "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "DOT", "COMMA", 
            "COLON", "SEMI_COLON", "NEWLINE", "MATMUL", "KRONECKER", "HERMITIAN", 
            "CONJUGATE", "TRANSPOSE", "IDENTIFIER", "QUBIT_IDENTIFIER", 
            "QUBIT_TRANSPOSE_IDENTIFIER", "STRING_LITERAL", "INTEGER_LITERAL", 
            "IMAGINARY_LITERAL", "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", 
            "QUBIT_TRANSPOSE_STATE_LITERAL" ]

    ruleNames = [ "SPACES", "COMMENTS", "ADD", "MINUS", "STAR", "DIV", "IDIV", 
                  "MOD", "POWER", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", "DEF", 
                  "RETURN", "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                  "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", 
                  "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", 
                  "CONTINUE", "BREAK", "X", "H", "Z", "Y", "S", "SDG", "T", 
                  "TDG", "RX", "RY", "RZ", "CX", "P", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", 
                  "DOT", "COMMA", "COLON", "SEMI_COLON", "NEWLINE", "MATMUL", 
                  "KRONECKER", "HERMITIAN", "CONJUGATE", "TRANSPOSE", "IDENTIFIER", 
                  "QUBIT_IDENTIFIER", "QUBIT_TRANSPOSE_IDENTIFIER", "STRING_LITERAL", 
                  "INTEGER_LITERAL", "IMAGINARY_LITERAL", "FLOAT_LITERAL", 
                  "QUBIT_STATE_LITERAL", "QUBIT_TRANSPOSE_STATE_LITERAL" ]

    grammarFileName = "QuantumLanguageLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens
    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents
    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened
    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken
    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value
    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None
    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)
    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)
    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent
    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)
    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count
    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[64] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass
            # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
            # satisfy the final newline needed by the single_put rule used by the REPL.
            try:
                nextnext_la = self._input.LA(2)
                nextnext_la_char = chr(nextnext_la)
            except ValueError:
                nextnext_eof = True
            else:
                nextnext_eof = False
            if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[64] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


