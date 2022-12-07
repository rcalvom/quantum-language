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
        4,0,69,435,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,1,0,4,0,137,8,0,11,0,12,0,138,1,0,1,0,1,1,1,1,
        5,1,145,8,1,10,1,12,1,148,9,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,
        1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,
        1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,
        1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,38,
        1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,
        1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,
        1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,
        1,53,1,54,1,54,1,54,3,54,347,8,54,1,54,1,54,3,54,351,8,54,1,54,3,
        54,354,8,54,3,54,356,8,54,1,54,1,54,1,55,1,55,1,56,1,56,1,56,1,56,
        1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,5,60,374,8,60,10,60,12,60,
        377,9,60,1,61,1,61,5,61,381,8,61,10,61,12,61,384,9,61,1,61,1,61,
        1,61,5,61,389,8,61,10,61,12,61,392,9,61,1,61,3,61,395,8,61,1,62,
        1,62,5,62,399,8,62,10,62,12,62,402,9,62,1,62,3,62,405,8,62,1,63,
        1,63,3,63,409,8,63,1,63,1,63,1,64,1,64,1,64,4,64,416,8,64,11,64,
        12,64,417,1,65,1,65,4,65,422,8,65,11,65,12,65,423,1,65,1,65,1,66,
        1,66,4,66,430,8,66,11,66,12,66,431,1,66,1,66,2,382,390,0,67,1,3,
        3,4,5,5,7,6,9,7,11,8,13,9,15,10,17,11,19,12,21,13,23,14,25,15,27,
        16,29,17,31,18,33,19,35,20,37,21,39,22,41,23,43,24,45,25,47,26,49,
        27,51,28,53,29,55,30,57,31,59,32,61,33,63,34,65,35,67,36,69,37,71,
        38,73,39,75,40,77,41,79,42,81,43,83,44,85,45,87,46,89,47,91,48,93,
        49,95,50,97,51,99,52,101,53,103,54,105,55,107,56,109,57,111,58,113,
        59,115,60,117,61,119,62,121,63,123,64,125,65,127,66,129,67,131,68,
        133,69,1,0,9,2,0,9,9,32,32,2,0,10,10,12,13,2,0,65,90,97,122,4,0,
        48,57,65,90,95,95,97,122,1,0,49,57,1,0,48,57,1,0,48,48,2,0,74,74,
        106,106,3,0,43,43,45,45,48,49,450,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
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
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,1,136,1,0,0,0,3,142,1,0,0,0,5,151,1,0,0,0,7,153,1,0,
        0,0,9,155,1,0,0,0,11,157,1,0,0,0,13,159,1,0,0,0,15,162,1,0,0,0,17,
        164,1,0,0,0,19,167,1,0,0,0,21,169,1,0,0,0,23,171,1,0,0,0,25,174,
        1,0,0,0,27,177,1,0,0,0,29,180,1,0,0,0,31,183,1,0,0,0,33,186,1,0,
        0,0,35,188,1,0,0,0,37,190,1,0,0,0,39,194,1,0,0,0,41,201,1,0,0,0,
        43,207,1,0,0,0,45,214,1,0,0,0,47,217,1,0,0,0,49,222,1,0,0,0,51,227,
        1,0,0,0,53,233,1,0,0,0,55,237,1,0,0,0,57,240,1,0,0,0,59,244,1,0,
        0,0,61,252,1,0,0,0,63,259,1,0,0,0,65,262,1,0,0,0,67,266,1,0,0,0,
        69,270,1,0,0,0,71,273,1,0,0,0,73,278,1,0,0,0,75,283,1,0,0,0,77,289,
        1,0,0,0,79,295,1,0,0,0,81,300,1,0,0,0,83,309,1,0,0,0,85,315,1,0,
        0,0,87,318,1,0,0,0,89,323,1,0,0,0,91,325,1,0,0,0,93,327,1,0,0,0,
        95,329,1,0,0,0,97,331,1,0,0,0,99,333,1,0,0,0,101,335,1,0,0,0,103,
        337,1,0,0,0,105,339,1,0,0,0,107,341,1,0,0,0,109,355,1,0,0,0,111,
        359,1,0,0,0,113,361,1,0,0,0,115,365,1,0,0,0,117,367,1,0,0,0,119,
        369,1,0,0,0,121,371,1,0,0,0,123,394,1,0,0,0,125,404,1,0,0,0,127,
        408,1,0,0,0,129,412,1,0,0,0,131,419,1,0,0,0,133,427,1,0,0,0,135,
        137,7,0,0,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,1,0,0,0,138,
        139,1,0,0,0,139,140,1,0,0,0,140,141,6,0,0,0,141,2,1,0,0,0,142,146,
        5,35,0,0,143,145,8,1,0,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,150,
        6,1,0,0,150,4,1,0,0,0,151,152,5,43,0,0,152,6,1,0,0,0,153,154,5,45,
        0,0,154,8,1,0,0,0,155,156,5,42,0,0,156,10,1,0,0,0,157,158,5,47,0,
        0,158,12,1,0,0,0,159,160,5,47,0,0,160,161,5,47,0,0,161,14,1,0,0,
        0,162,163,5,37,0,0,163,16,1,0,0,0,164,165,5,42,0,0,165,166,5,42,
        0,0,166,18,1,0,0,0,167,168,5,60,0,0,168,20,1,0,0,0,169,170,5,62,
        0,0,170,22,1,0,0,0,171,172,5,61,0,0,172,173,5,61,0,0,173,24,1,0,
        0,0,174,175,5,62,0,0,175,176,5,61,0,0,176,26,1,0,0,0,177,178,5,60,
        0,0,178,179,5,61,0,0,179,28,1,0,0,0,180,181,5,60,0,0,181,182,5,62,
        0,0,182,30,1,0,0,0,183,184,5,33,0,0,184,185,5,61,0,0,185,32,1,0,
        0,0,186,187,5,124,0,0,187,34,1,0,0,0,188,189,5,61,0,0,189,36,1,0,
        0,0,190,191,5,100,0,0,191,192,5,101,0,0,192,193,5,102,0,0,193,38,
        1,0,0,0,194,195,5,114,0,0,195,196,5,101,0,0,196,197,5,116,0,0,197,
        198,5,117,0,0,198,199,5,114,0,0,199,200,5,110,0,0,200,40,1,0,0,0,
        201,202,5,114,0,0,202,203,5,97,0,0,203,204,5,105,0,0,204,205,5,115,
        0,0,205,206,5,101,0,0,206,42,1,0,0,0,207,208,5,97,0,0,208,209,5,
        115,0,0,209,210,5,115,0,0,210,211,5,101,0,0,211,212,5,114,0,0,212,
        213,5,116,0,0,213,44,1,0,0,0,214,215,5,105,0,0,215,216,5,102,0,0,
        216,46,1,0,0,0,217,218,5,101,0,0,218,219,5,108,0,0,219,220,5,105,
        0,0,220,221,5,102,0,0,221,48,1,0,0,0,222,223,5,101,0,0,223,224,5,
        108,0,0,224,225,5,115,0,0,225,226,5,101,0,0,226,50,1,0,0,0,227,228,
        5,119,0,0,228,229,5,104,0,0,229,230,5,105,0,0,230,231,5,108,0,0,
        231,232,5,101,0,0,232,52,1,0,0,0,233,234,5,102,0,0,234,235,5,111,
        0,0,235,236,5,114,0,0,236,54,1,0,0,0,237,238,5,105,0,0,238,239,5,
        110,0,0,239,56,1,0,0,0,240,241,5,116,0,0,241,242,5,114,0,0,242,243,
        5,121,0,0,243,58,1,0,0,0,244,245,5,102,0,0,245,246,5,105,0,0,246,
        247,5,110,0,0,247,248,5,97,0,0,248,249,5,108,0,0,249,250,5,108,0,
        0,250,251,5,121,0,0,251,60,1,0,0,0,252,253,5,101,0,0,253,254,5,120,
        0,0,254,255,5,99,0,0,255,256,5,101,0,0,256,257,5,112,0,0,257,258,
        5,116,0,0,258,62,1,0,0,0,259,260,5,111,0,0,260,261,5,114,0,0,261,
        64,1,0,0,0,262,263,5,97,0,0,263,264,5,110,0,0,264,265,5,100,0,0,
        265,66,1,0,0,0,266,267,5,110,0,0,267,268,5,111,0,0,268,269,5,116,
        0,0,269,68,1,0,0,0,270,271,5,105,0,0,271,272,5,115,0,0,272,70,1,
        0,0,0,273,274,5,78,0,0,274,275,5,111,0,0,275,276,5,110,0,0,276,277,
        5,101,0,0,277,72,1,0,0,0,278,279,5,84,0,0,279,280,5,114,0,0,280,
        281,5,117,0,0,281,282,5,101,0,0,282,74,1,0,0,0,283,284,5,70,0,0,
        284,285,5,97,0,0,285,286,5,108,0,0,286,287,5,115,0,0,287,288,5,101,
        0,0,288,76,1,0,0,0,289,290,5,99,0,0,290,291,5,108,0,0,291,292,5,
        97,0,0,292,293,5,115,0,0,293,294,5,115,0,0,294,78,1,0,0,0,295,296,
        5,112,0,0,296,297,5,97,0,0,297,298,5,115,0,0,298,299,5,115,0,0,299,
        80,1,0,0,0,300,301,5,99,0,0,301,302,5,111,0,0,302,303,5,110,0,0,
        303,304,5,116,0,0,304,305,5,105,0,0,305,306,5,110,0,0,306,307,5,
        117,0,0,307,308,5,101,0,0,308,82,1,0,0,0,309,310,5,98,0,0,310,311,
        5,114,0,0,311,312,5,101,0,0,312,313,5,97,0,0,313,314,5,107,0,0,314,
        84,1,0,0,0,315,316,5,112,0,0,316,317,5,105,0,0,317,86,1,0,0,0,318,
        319,5,112,0,0,319,320,5,108,0,0,320,321,5,111,0,0,321,322,5,116,
        0,0,322,88,1,0,0,0,323,324,5,40,0,0,324,90,1,0,0,0,325,326,5,41,
        0,0,326,92,1,0,0,0,327,328,5,91,0,0,328,94,1,0,0,0,329,330,5,93,
        0,0,330,96,1,0,0,0,331,332,5,123,0,0,332,98,1,0,0,0,333,334,5,125,
        0,0,334,100,1,0,0,0,335,336,5,46,0,0,336,102,1,0,0,0,337,338,5,44,
        0,0,338,104,1,0,0,0,339,340,5,58,0,0,340,106,1,0,0,0,341,342,5,59,
        0,0,342,108,1,0,0,0,343,344,4,54,0,0,344,356,3,1,0,0,345,347,5,13,
        0,0,346,345,1,0,0,0,346,347,1,0,0,0,347,348,1,0,0,0,348,351,5,10,
        0,0,349,351,2,12,13,0,350,346,1,0,0,0,350,349,1,0,0,0,351,353,1,
        0,0,0,352,354,3,1,0,0,353,352,1,0,0,0,353,354,1,0,0,0,354,356,1,
        0,0,0,355,343,1,0,0,0,355,350,1,0,0,0,356,357,1,0,0,0,357,358,6,
        54,1,0,358,110,1,0,0,0,359,360,5,64,0,0,360,112,1,0,0,0,361,362,
        5,40,0,0,362,363,5,88,0,0,363,364,5,41,0,0,364,114,1,0,0,0,365,366,
        5,84,0,0,366,116,1,0,0,0,367,368,5,39,0,0,368,118,1,0,0,0,369,370,
        5,116,0,0,370,120,1,0,0,0,371,375,7,2,0,0,372,374,7,3,0,0,373,372,
        1,0,0,0,374,377,1,0,0,0,375,373,1,0,0,0,375,376,1,0,0,0,376,122,
        1,0,0,0,377,375,1,0,0,0,378,382,5,39,0,0,379,381,9,0,0,0,380,379,
        1,0,0,0,381,384,1,0,0,0,382,383,1,0,0,0,382,380,1,0,0,0,383,385,
        1,0,0,0,384,382,1,0,0,0,385,395,5,39,0,0,386,390,5,34,0,0,387,389,
        9,0,0,0,388,387,1,0,0,0,389,392,1,0,0,0,390,391,1,0,0,0,390,388,
        1,0,0,0,391,393,1,0,0,0,392,390,1,0,0,0,393,395,5,34,0,0,394,378,
        1,0,0,0,394,386,1,0,0,0,395,124,1,0,0,0,396,400,7,4,0,0,397,399,
        7,5,0,0,398,397,1,0,0,0,399,402,1,0,0,0,400,398,1,0,0,0,400,401,
        1,0,0,0,401,405,1,0,0,0,402,400,1,0,0,0,403,405,7,6,0,0,404,396,
        1,0,0,0,404,403,1,0,0,0,405,126,1,0,0,0,406,409,3,129,64,0,407,409,
        3,125,62,0,408,406,1,0,0,0,408,407,1,0,0,0,409,410,1,0,0,0,410,411,
        7,7,0,0,411,128,1,0,0,0,412,413,3,125,62,0,413,415,5,46,0,0,414,
        416,7,5,0,0,415,414,1,0,0,0,416,417,1,0,0,0,417,415,1,0,0,0,417,
        418,1,0,0,0,418,130,1,0,0,0,419,421,3,19,9,0,420,422,7,8,0,0,421,
        420,1,0,0,0,422,423,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,
        425,1,0,0,0,425,426,3,33,16,0,426,132,1,0,0,0,427,429,3,33,16,0,
        428,430,7,8,0,0,429,428,1,0,0,0,430,431,1,0,0,0,431,429,1,0,0,0,
        431,432,1,0,0,0,432,433,1,0,0,0,433,434,3,21,10,0,434,134,1,0,0,
        0,17,0,138,146,346,350,353,355,375,382,390,394,400,404,408,417,423,
        431,2,6,0,0,1,54,0
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
    PIPE = 19
    ASSIGN = 20
    DEF = 21
    RETURN = 22
    RAISE = 23
    ASSERT = 24
    IF = 25
    ELIF = 26
    ELSE = 27
    WHILE = 28
    FOR = 29
    IN = 30
    TRY = 31
    FINALLY = 32
    EXCEPT = 33
    OR = 34
    AND = 35
    NOT = 36
    IS = 37
    NONE = 38
    TRUE = 39
    FALSE = 40
    CLASS = 41
    PASS = 42
    CONTINUE = 43
    BREAK = 44
    PI = 45
    PLOT = 46
    OPEN_PAREN = 47
    CLOSE_PAREN = 48
    OPEN_BRACK = 49
    CLOSE_BRACK = 50
    OPEN_BRACE = 51
    CLOSE_BRACE = 52
    DOT = 53
    COMMA = 54
    COLON = 55
    SEMI_COLON = 56
    NEWLINE = 57
    MATMUL = 58
    KRONECKER = 59
    HERMITIAN = 60
    CONJUGATE = 61
    TRANSPOSE = 62
    IDENTIFIER = 63
    STRING_LITERAL = 64
    INTEGER_LITERAL = 65
    IMAGINARY_LITERAL = 66
    FLOAT_LITERAL = 67
    BRA_LITERAL = 68
    KET_LITERAL = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", "'**'", "'<'", "'>'", 
            "'=='", "'>='", "'<='", "'<>'", "'!='", "'|'", "'='", "'def'", 
            "'return'", "'raise'", "'assert'", "'if'", "'elif'", "'else'", 
            "'while'", "'for'", "'in'", "'try'", "'finally'", "'except'", 
            "'or'", "'and'", "'not'", "'is'", "'None'", "'True'", "'False'", 
            "'class'", "'pass'", "'continue'", "'break'", "'pi'", "'plot'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "':'", 
            "';'", "'@'", "'(X)'", "'T'", "'''", "'t'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "SPACES", "COMMENTS", "ADD", "MINUS", "STAR", 
            "DIV", "IDIV", "MOD", "POWER", "LESS_THAN", "GREATER_THAN", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "PIPE", 
            "ASSIGN", "DEF", "RETURN", "RAISE", "ASSERT", "IF", "ELIF", 
            "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", 
            "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", 
            "CONTINUE", "BREAK", "PI", "PLOT", "OPEN_PAREN", "CLOSE_PAREN", 
            "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", "DOT", 
            "COMMA", "COLON", "SEMI_COLON", "NEWLINE", "MATMUL", "KRONECKER", 
            "HERMITIAN", "CONJUGATE", "TRANSPOSE", "IDENTIFIER", "STRING_LITERAL", 
            "INTEGER_LITERAL", "IMAGINARY_LITERAL", "FLOAT_LITERAL", "BRA_LITERAL", 
            "KET_LITERAL" ]

    ruleNames = [ "SPACES", "COMMENTS", "ADD", "MINUS", "STAR", "DIV", "IDIV", 
                  "MOD", "POWER", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "PIPE", "ASSIGN", 
                  "DEF", "RETURN", "RAISE", "ASSERT", "IF", "ELIF", "ELSE", 
                  "WHILE", "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", 
                  "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", 
                  "PASS", "CONTINUE", "BREAK", "PI", "PLOT", "OPEN_PAREN", 
                  "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                  "CLOSE_BRACE", "DOT", "COMMA", "COLON", "SEMI_COLON", 
                  "NEWLINE", "MATMUL", "KRONECKER", "HERMITIAN", "CONJUGATE", 
                  "TRANSPOSE", "IDENTIFIER", "STRING_LITERAL", "INTEGER_LITERAL", 
                  "IMAGINARY_LITERAL", "FLOAT_LITERAL", "BRA_LITERAL", "KET_LITERAL" ]

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
            actions[54] = self.NEWLINE_action 
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
            preds[54] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


