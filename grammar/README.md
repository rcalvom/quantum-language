Execute to generate grammar (into `grammar/` folder):

```
antlr4 -o ../recognition/generated/ -no-listener -visitor -Dlanguage=Python3 -lib . -Werror QuantumLanguageLexer.g4 QuantumLanguageParser.g4
```