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
        4,0,66,435,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,1,0,4,0,131,
        8,0,11,0,12,0,132,1,0,1,0,1,1,1,1,5,1,139,8,1,10,1,12,1,142,9,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,
        1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,36,1,36,
        1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,
        1,40,1,40,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,
        1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,3,49,327,8,49,
        1,49,1,49,3,49,331,8,49,1,49,3,49,334,8,49,3,49,336,8,49,1,49,1,
        49,1,50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,1,
        55,1,55,5,55,354,8,55,10,55,12,55,357,9,55,1,56,1,56,1,56,5,56,362,
        8,56,10,56,12,56,365,9,56,1,56,1,56,1,57,1,57,1,57,5,57,372,8,57,
        10,57,12,57,375,9,57,1,57,1,57,1,58,1,58,5,58,381,8,58,10,58,12,
        58,384,9,58,1,58,1,58,1,58,5,58,389,8,58,10,58,12,58,392,9,58,1,
        58,3,58,395,8,58,1,59,1,59,5,59,399,8,59,10,59,12,59,402,9,59,1,
        59,3,59,405,8,59,1,60,1,60,3,60,409,8,60,1,60,1,60,1,61,1,61,1,61,
        4,61,416,8,61,11,61,12,61,417,1,62,1,62,4,62,422,8,62,11,62,12,62,
        423,1,62,1,62,1,63,1,63,4,63,430,8,63,11,63,12,63,431,1,63,1,63,
        2,382,390,0,64,1,3,3,4,5,5,7,6,9,7,11,8,13,9,15,10,17,11,19,12,21,
        13,23,14,25,15,27,16,29,17,31,18,33,19,35,20,37,21,39,22,41,23,43,
        24,45,25,47,26,49,27,51,28,53,29,55,30,57,31,59,32,61,33,63,34,65,
        35,67,36,69,37,71,38,73,39,75,40,77,41,79,42,81,43,83,44,85,45,87,
        46,89,47,91,48,93,49,95,50,97,51,99,52,101,53,103,54,105,55,107,
        56,109,57,111,58,113,59,115,60,117,61,119,62,121,63,123,64,125,65,
        127,66,1,0,9,2,0,9,9,32,32,2,0,10,10,12,13,2,0,65,90,97,122,4,0,
        48,57,65,90,95,95,97,122,1,0,49,57,1,0,48,57,1,0,48,48,2,0,73,73,
        105,105,3,0,43,43,45,45,48,49,452,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,
        0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,
        0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,
        0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,
        0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,
        0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,
        0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,1,130,1,0,0,0,3,136,1,0,0,0,5,
        145,1,0,0,0,7,147,1,0,0,0,9,149,1,0,0,0,11,151,1,0,0,0,13,153,1,
        0,0,0,15,156,1,0,0,0,17,158,1,0,0,0,19,161,1,0,0,0,21,163,1,0,0,
        0,23,165,1,0,0,0,25,168,1,0,0,0,27,171,1,0,0,0,29,174,1,0,0,0,31,
        177,1,0,0,0,33,180,1,0,0,0,35,182,1,0,0,0,37,186,1,0,0,0,39,193,
        1,0,0,0,41,199,1,0,0,0,43,206,1,0,0,0,45,209,1,0,0,0,47,214,1,0,
        0,0,49,219,1,0,0,0,51,225,1,0,0,0,53,229,1,0,0,0,55,232,1,0,0,0,
        57,236,1,0,0,0,59,244,1,0,0,0,61,251,1,0,0,0,63,254,1,0,0,0,65,258,
        1,0,0,0,67,262,1,0,0,0,69,265,1,0,0,0,71,270,1,0,0,0,73,275,1,0,
        0,0,75,281,1,0,0,0,77,287,1,0,0,0,79,292,1,0,0,0,81,301,1,0,0,0,
        83,307,1,0,0,0,85,309,1,0,0,0,87,311,1,0,0,0,89,313,1,0,0,0,91,315,
        1,0,0,0,93,317,1,0,0,0,95,319,1,0,0,0,97,321,1,0,0,0,99,335,1,0,
        0,0,101,339,1,0,0,0,103,341,1,0,0,0,105,345,1,0,0,0,107,347,1,0,
        0,0,109,349,1,0,0,0,111,351,1,0,0,0,113,358,1,0,0,0,115,368,1,0,
        0,0,117,394,1,0,0,0,119,404,1,0,0,0,121,408,1,0,0,0,123,412,1,0,
        0,0,125,419,1,0,0,0,127,427,1,0,0,0,129,131,7,0,0,0,130,129,1,0,
        0,0,131,132,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,134,1,0,
        0,0,134,135,6,0,0,0,135,2,1,0,0,0,136,140,5,35,0,0,137,139,8,1,0,
        0,138,137,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,
        0,141,143,1,0,0,0,142,140,1,0,0,0,143,144,6,1,0,0,144,4,1,0,0,0,
        145,146,5,43,0,0,146,6,1,0,0,0,147,148,5,45,0,0,148,8,1,0,0,0,149,
        150,5,42,0,0,150,10,1,0,0,0,151,152,5,47,0,0,152,12,1,0,0,0,153,
        154,5,47,0,0,154,155,5,47,0,0,155,14,1,0,0,0,156,157,5,37,0,0,157,
        16,1,0,0,0,158,159,5,42,0,0,159,160,5,42,0,0,160,18,1,0,0,0,161,
        162,5,60,0,0,162,20,1,0,0,0,163,164,5,62,0,0,164,22,1,0,0,0,165,
        166,5,61,0,0,166,167,5,61,0,0,167,24,1,0,0,0,168,169,5,62,0,0,169,
        170,5,61,0,0,170,26,1,0,0,0,171,172,5,60,0,0,172,173,5,61,0,0,173,
        28,1,0,0,0,174,175,5,60,0,0,175,176,5,62,0,0,176,30,1,0,0,0,177,
        178,5,33,0,0,178,179,5,61,0,0,179,32,1,0,0,0,180,181,5,61,0,0,181,
        34,1,0,0,0,182,183,5,100,0,0,183,184,5,101,0,0,184,185,5,102,0,0,
        185,36,1,0,0,0,186,187,5,114,0,0,187,188,5,101,0,0,188,189,5,116,
        0,0,189,190,5,117,0,0,190,191,5,114,0,0,191,192,5,110,0,0,192,38,
        1,0,0,0,193,194,5,114,0,0,194,195,5,97,0,0,195,196,5,105,0,0,196,
        197,5,115,0,0,197,198,5,101,0,0,198,40,1,0,0,0,199,200,5,97,0,0,
        200,201,5,115,0,0,201,202,5,115,0,0,202,203,5,101,0,0,203,204,5,
        114,0,0,204,205,5,116,0,0,205,42,1,0,0,0,206,207,5,105,0,0,207,208,
        5,102,0,0,208,44,1,0,0,0,209,210,5,101,0,0,210,211,5,108,0,0,211,
        212,5,105,0,0,212,213,5,102,0,0,213,46,1,0,0,0,214,215,5,101,0,0,
        215,216,5,108,0,0,216,217,5,115,0,0,217,218,5,101,0,0,218,48,1,0,
        0,0,219,220,5,119,0,0,220,221,5,104,0,0,221,222,5,105,0,0,222,223,
        5,108,0,0,223,224,5,101,0,0,224,50,1,0,0,0,225,226,5,102,0,0,226,
        227,5,111,0,0,227,228,5,114,0,0,228,52,1,0,0,0,229,230,5,105,0,0,
        230,231,5,110,0,0,231,54,1,0,0,0,232,233,5,116,0,0,233,234,5,114,
        0,0,234,235,5,121,0,0,235,56,1,0,0,0,236,237,5,102,0,0,237,238,5,
        105,0,0,238,239,5,110,0,0,239,240,5,97,0,0,240,241,5,108,0,0,241,
        242,5,108,0,0,242,243,5,121,0,0,243,58,1,0,0,0,244,245,5,101,0,0,
        245,246,5,120,0,0,246,247,5,99,0,0,247,248,5,101,0,0,248,249,5,112,
        0,0,249,250,5,116,0,0,250,60,1,0,0,0,251,252,5,111,0,0,252,253,5,
        114,0,0,253,62,1,0,0,0,254,255,5,97,0,0,255,256,5,110,0,0,256,257,
        5,100,0,0,257,64,1,0,0,0,258,259,5,110,0,0,259,260,5,111,0,0,260,
        261,5,116,0,0,261,66,1,0,0,0,262,263,5,105,0,0,263,264,5,115,0,0,
        264,68,1,0,0,0,265,266,5,78,0,0,266,267,5,111,0,0,267,268,5,110,
        0,0,268,269,5,101,0,0,269,70,1,0,0,0,270,271,5,84,0,0,271,272,5,
        114,0,0,272,273,5,117,0,0,273,274,5,101,0,0,274,72,1,0,0,0,275,276,
        5,70,0,0,276,277,5,97,0,0,277,278,5,108,0,0,278,279,5,115,0,0,279,
        280,5,101,0,0,280,74,1,0,0,0,281,282,5,99,0,0,282,283,5,108,0,0,
        283,284,5,97,0,0,284,285,5,115,0,0,285,286,5,115,0,0,286,76,1,0,
        0,0,287,288,5,112,0,0,288,289,5,97,0,0,289,290,5,115,0,0,290,291,
        5,115,0,0,291,78,1,0,0,0,292,293,5,99,0,0,293,294,5,111,0,0,294,
        295,5,110,0,0,295,296,5,116,0,0,296,297,5,105,0,0,297,298,5,110,
        0,0,298,299,5,117,0,0,299,300,5,101,0,0,300,80,1,0,0,0,301,302,5,
        98,0,0,302,303,5,114,0,0,303,304,5,101,0,0,304,305,5,97,0,0,305,
        306,5,107,0,0,306,82,1,0,0,0,307,308,5,40,0,0,308,84,1,0,0,0,309,
        310,5,41,0,0,310,86,1,0,0,0,311,312,5,91,0,0,312,88,1,0,0,0,313,
        314,5,93,0,0,314,90,1,0,0,0,315,316,5,46,0,0,316,92,1,0,0,0,317,
        318,5,44,0,0,318,94,1,0,0,0,319,320,5,58,0,0,320,96,1,0,0,0,321,
        322,5,59,0,0,322,98,1,0,0,0,323,324,4,49,0,0,324,336,3,1,0,0,325,
        327,5,13,0,0,326,325,1,0,0,0,326,327,1,0,0,0,327,328,1,0,0,0,328,
        331,5,10,0,0,329,331,2,12,13,0,330,326,1,0,0,0,330,329,1,0,0,0,331,
        333,1,0,0,0,332,334,3,1,0,0,333,332,1,0,0,0,333,334,1,0,0,0,334,
        336,1,0,0,0,335,323,1,0,0,0,335,330,1,0,0,0,336,337,1,0,0,0,337,
        338,6,49,1,0,338,100,1,0,0,0,339,340,5,64,0,0,340,102,1,0,0,0,341,
        342,5,40,0,0,342,343,5,88,0,0,343,344,5,41,0,0,344,104,1,0,0,0,345,
        346,5,84,0,0,346,106,1,0,0,0,347,348,5,39,0,0,348,108,1,0,0,0,349,
        350,5,116,0,0,350,110,1,0,0,0,351,355,7,2,0,0,352,354,7,3,0,0,353,
        352,1,0,0,0,354,357,1,0,0,0,355,353,1,0,0,0,355,356,1,0,0,0,356,
        112,1,0,0,0,357,355,1,0,0,0,358,359,5,124,0,0,359,363,7,2,0,0,360,
        362,7,3,0,0,361,360,1,0,0,0,362,365,1,0,0,0,363,361,1,0,0,0,363,
        364,1,0,0,0,364,366,1,0,0,0,365,363,1,0,0,0,366,367,5,62,0,0,367,
        114,1,0,0,0,368,369,5,60,0,0,369,373,7,2,0,0,370,372,7,3,0,0,371,
        370,1,0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,373,374,1,0,0,0,374,
        376,1,0,0,0,375,373,1,0,0,0,376,377,5,124,0,0,377,116,1,0,0,0,378,
        382,5,39,0,0,379,381,9,0,0,0,380,379,1,0,0,0,381,384,1,0,0,0,382,
        383,1,0,0,0,382,380,1,0,0,0,383,385,1,0,0,0,384,382,1,0,0,0,385,
        395,5,39,0,0,386,390,5,34,0,0,387,389,9,0,0,0,388,387,1,0,0,0,389,
        392,1,0,0,0,390,391,1,0,0,0,390,388,1,0,0,0,391,393,1,0,0,0,392,
        390,1,0,0,0,393,395,5,34,0,0,394,378,1,0,0,0,394,386,1,0,0,0,395,
        118,1,0,0,0,396,400,7,4,0,0,397,399,7,5,0,0,398,397,1,0,0,0,399,
        402,1,0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,405,1,0,0,0,402,
        400,1,0,0,0,403,405,7,6,0,0,404,396,1,0,0,0,404,403,1,0,0,0,405,
        120,1,0,0,0,406,409,3,123,61,0,407,409,3,119,59,0,408,406,1,0,0,
        0,408,407,1,0,0,0,409,410,1,0,0,0,410,411,7,7,0,0,411,122,1,0,0,
        0,412,413,3,119,59,0,413,415,5,46,0,0,414,416,7,5,0,0,415,414,1,
        0,0,0,416,417,1,0,0,0,417,415,1,0,0,0,417,418,1,0,0,0,418,124,1,
        0,0,0,419,421,5,124,0,0,420,422,7,8,0,0,421,420,1,0,0,0,422,423,
        1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,425,1,0,0,0,425,426,
        5,62,0,0,426,126,1,0,0,0,427,429,5,60,0,0,428,430,7,8,0,0,429,428,
        1,0,0,0,430,431,1,0,0,0,431,429,1,0,0,0,431,432,1,0,0,0,432,433,
        1,0,0,0,433,434,5,124,0,0,434,128,1,0,0,0,19,0,132,140,326,330,333,
        335,355,363,373,382,390,394,400,404,408,417,423,431,2,6,0,0,1,49,
        0
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
    OPEN_PAREN = 44
    CLOSE_PAREN = 45
    OPEN_BRACK = 46
    CLOSE_BRACK = 47
    DOT = 48
    COMMA = 49
    COLON = 50
    SEMI_COLON = 51
    NEWLINE = 52
    MATMUL = 53
    KRONECKER = 54
    HERMITIAN = 55
    CONJUGATE = 56
    TRANSPOSE = 57
    IDENTIFIER = 58
    QUBIT_IDENTIFIER = 59
    QUBIT_TRANSPOSE_IDENTIFIER = 60
    STRING_LITERAL = 61
    INTEGER_LITERAL = 62
    IMAGINARY_LITERAL = 63
    FLOAT_LITERAL = 64
    QUBIT_STATE_LITERAL = 65
    QUBIT_TRANSPOSE_STATE_LITERAL = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", "'**'", "'<'", "'>'", 
            "'=='", "'>='", "'<='", "'<>'", "'!='", "'='", "'def'", "'return'", 
            "'raise'", "'assert'", "'if'", "'elif'", "'else'", "'while'", 
            "'for'", "'in'", "'try'", "'finally'", "'except'", "'or'", "'and'", 
            "'not'", "'is'", "'None'", "'True'", "'False'", "'class'", "'pass'", 
            "'continue'", "'break'", "'('", "')'", "'['", "']'", "'.'", 
            "','", "':'", "';'", "'@'", "'(X)'", "'T'", "'''", "'t'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "SPACES", "COMMENTS", "ADD", "MINUS", "STAR", 
            "DIV", "IDIV", "MOD", "POWER", "LESS_THAN", "GREATER_THAN", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", 
            "DEF", "RETURN", "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
            "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", "NOT", 
            "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", "CONTINUE", 
            "BREAK", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
            "DOT", "COMMA", "COLON", "SEMI_COLON", "NEWLINE", "MATMUL", 
            "KRONECKER", "HERMITIAN", "CONJUGATE", "TRANSPOSE", "IDENTIFIER", 
            "QUBIT_IDENTIFIER", "QUBIT_TRANSPOSE_IDENTIFIER", "STRING_LITERAL", 
            "INTEGER_LITERAL", "IMAGINARY_LITERAL", "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", 
            "QUBIT_TRANSPOSE_STATE_LITERAL" ]

    ruleNames = [ "SPACES", "COMMENTS", "ADD", "MINUS", "STAR", "DIV", "IDIV", 
                  "MOD", "POWER", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", "DEF", 
                  "RETURN", "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                  "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", 
                  "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", 
                  "CONTINUE", "BREAK", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                  "CLOSE_BRACK", "DOT", "COMMA", "COLON", "SEMI_COLON", 
                  "NEWLINE", "MATMUL", "KRONECKER", "HERMITIAN", "CONJUGATE", 
                  "TRANSPOSE", "IDENTIFIER", "QUBIT_IDENTIFIER", "QUBIT_TRANSPOSE_IDENTIFIER", 
                  "STRING_LITERAL", "INTEGER_LITERAL", "IMAGINARY_LITERAL", 
                  "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", "QUBIT_TRANSPOSE_STATE_LITERAL" ]

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
            actions[49] = self.NEWLINE_action 
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
            preds[49] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


