// Generated from /home/ricardo/Documents/Personal/quantum-language/grammar/QuantumLanguageParser.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class QuantumLanguageParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INDENT=1, DEDENT=2, IDENTIFIER=3, STRING_LITERAL=4, INTEGER_LITERAL=5, 
		IMAGINARY_LITERAL=6, FLOAT_LITERAL=7, QUBIT_STATE_LITERAL=8, ADD=9, MINUS=10, 
		STAR=11, DIV=12, IDIV=13, MOD=14, POWER=15, OR_OP=16, XOR=17, AND_OP=18, 
		LEFT_SHIFT=19, RIGHT_SHIFT=20, LESS_THAN=21, GREATER_THAN=22, EQUALS=23, 
		GT_EQ=24, LT_EQ=25, NOT_EQ_1=26, NOT_EQ_2=27, ASSIGN=28, DEF=29, RETURN=30, 
		RAISE=31, ASSERT=32, IF=33, ELIF=34, ELSE=35, WHILE=36, FOR=37, IN=38, 
		TRY=39, FINALLY=40, EXCEPT=41, OR=42, AND=43, NOT=44, IS=45, NONE=46, 
		TRUE=47, FALSE=48, CLASS=49, PASS=50, CONTINUE=51, BREAK=52, OPEN_PAREN=53, 
		CLOSE_PAREN=54, OPEN_BRACK=55, CLOSE_BRACK=56, OPEN_BRACE=57, CLOSE_BRACE=58, 
		DOT=59, COMMA=60, COLON=61, SEMI_COLON=62, NEWLINE=63, COMMENTS=64, SPACES=65;
	public static final int
		RULE_start = 0, RULE_sentence = 1, RULE_if = 2, RULE_elif = 3, RULE_else = 4, 
		RULE_for = 5, RULE_while = 6, RULE_try = 7, RULE_except = 8, RULE_function_execution = 9, 
		RULE_function_declaration = 10, RULE_assign = 11, RULE_identifier = 12, 
		RULE_expression = 13, RULE_binary_operator = 14, RULE_unitary_operator = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "sentence", "if", "elif", "else", "for", "while", "try", "except", 
			"function_execution", "function_declaration", "assign", "identifier", 
			"expression", "binary_operator", "unitary_operator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "'+'", "'-'", "'*'", 
			"'/'", "'//'", "'%'", "'**'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'<'", 
			"'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", "'='", "'def'", "'return'", 
			"'raise'", "'assert'", "'if'", "'elif'", "'else'", "'while'", "'for'", 
			"'in'", "'try'", "'finally'", "'except'", "'or'", "'and'", "'not'", "'is'", 
			"'None'", "'True'", "'False'", "'class'", "'pass'", "'continue'", "'break'", 
			"'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "':'", "';'", 
			"'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INDENT", "DEDENT", "IDENTIFIER", "STRING_LITERAL", "INTEGER_LITERAL", 
			"IMAGINARY_LITERAL", "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", "ADD", "MINUS", 
			"STAR", "DIV", "IDIV", "MOD", "POWER", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", 
			"RIGHT_SHIFT", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
			"NOT_EQ_1", "NOT_EQ_2", "ASSIGN", "DEF", "RETURN", "RAISE", "ASSERT", 
			"IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", "EXCEPT", 
			"OR", "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", "CONTINUE", 
			"BREAK", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
			"CLOSE_BRACE", "DOT", "COMMA", "COLON", "SEMI_COLON", "NEWLINE", "COMMENTS", 
			"SPACES"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "QuantumLanguageParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public QuantumLanguageParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(QuantumLanguageParser.EOF, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(32);
					sentence();
					{
					setState(34);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(33);
						match(SEMI_COLON);
						}
					}

					setState(36);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(42);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			{
			setState(43);
			sentence();
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(44);
				match(SEMI_COLON);
				}
			}

			}
			setState(47);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SentenceContext extends ParserRuleContext {
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public ForContext for_() {
			return getRuleContext(ForContext.class,0);
		}
		public WhileContext while_() {
			return getRuleContext(WhileContext.class,0);
		}
		public TryContext try_() {
			return getRuleContext(TryContext.class,0);
		}
		public Function_executionContext function_execution() {
			return getRuleContext(Function_executionContext.class,0);
		}
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public Function_declarationContext function_declaration() {
			return getRuleContext(Function_declarationContext.class,0);
		}
		public SentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentence; }
	}

	public final SentenceContext sentence() throws RecognitionException {
		SentenceContext _localctx = new SentenceContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentence);
		try {
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				if_();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(50);
				for_();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(51);
				while_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(52);
				try_();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(53);
				function_execution();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(54);
				assign();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(55);
				function_declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(QuantumLanguageParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<ElifContext> elif() {
			return getRuleContexts(ElifContext.class);
		}
		public ElifContext elif(int i) {
			return getRuleContext(ElifContext.class,i);
		}
		public ElseContext else_() {
			return getRuleContext(ElseContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_if);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(IF);
			setState(59);
			expression(0);
			setState(60);
			match(COLON);
			setState(61);
			match(INDENT);
			setState(70);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(62);
					sentence();
					{
					setState(64);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(63);
						match(SEMI_COLON);
						}
					}

					setState(66);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(72);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			{
			setState(73);
			sentence();
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(74);
				match(SEMI_COLON);
				}
			}

			}
			setState(77);
			match(DEDENT);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF) {
				{
				{
				setState(78);
				elif();
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(84);
				else_();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElifContext extends ParserRuleContext {
		public TerminalNode ELIF() { return getToken(QuantumLanguageParser.ELIF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public ElifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elif; }
	}

	public final ElifContext elif() throws RecognitionException {
		ElifContext _localctx = new ElifContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_elif);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(ELIF);
			setState(88);
			expression(0);
			setState(89);
			match(COLON);
			setState(90);
			match(INDENT);
			setState(99);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(91);
					sentence();
					{
					setState(93);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(92);
						match(SEMI_COLON);
						}
					}

					setState(95);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(101);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			{
			setState(102);
			sentence();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(103);
				match(SEMI_COLON);
				}
			}

			}
			setState(106);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElseContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(QuantumLanguageParser.ELSE, 0); }
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public ElseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else; }
	}

	public final ElseContext else_() throws RecognitionException {
		ElseContext _localctx = new ElseContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_else);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(ELSE);
			setState(109);
			match(COLON);
			setState(110);
			match(INDENT);
			setState(119);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(111);
					sentence();
					{
					setState(113);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(112);
						match(SEMI_COLON);
						}
					}

					setState(115);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(121);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			{
			setState(122);
			sentence();
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(123);
				match(SEMI_COLON);
				}
			}

			}
			setState(126);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(QuantumLanguageParser.FOR, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode IN() { return getToken(QuantumLanguageParser.IN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public ForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for; }
	}

	public final ForContext for_() throws RecognitionException {
		ForContext _localctx = new ForContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_for);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(FOR);
			setState(129);
			identifier();
			setState(130);
			match(IN);
			setState(131);
			expression(0);
			setState(132);
			match(COLON);
			setState(133);
			match(INDENT);
			setState(142);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(134);
					sentence();
					{
					setState(136);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(135);
						match(SEMI_COLON);
						}
					}

					setState(138);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(144);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			{
			setState(145);
			sentence();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(146);
				match(SEMI_COLON);
				}
			}

			}
			setState(149);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(QuantumLanguageParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public WhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while; }
	}

	public final WhileContext while_() throws RecognitionException {
		WhileContext _localctx = new WhileContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_while);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(WHILE);
			setState(152);
			expression(0);
			setState(153);
			match(COLON);
			setState(154);
			match(INDENT);
			setState(163);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(155);
					sentence();
					{
					setState(157);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(156);
						match(SEMI_COLON);
						}
					}

					setState(159);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(165);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			{
			setState(166);
			sentence();
			setState(168);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(167);
				match(SEMI_COLON);
				}
			}

			}
			setState(170);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TryContext extends ParserRuleContext {
		public TerminalNode TRY() { return getToken(QuantumLanguageParser.TRY, 0); }
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public ExceptContext except() {
			return getRuleContext(ExceptContext.class,0);
		}
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public TryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_try; }
	}

	public final TryContext try_() throws RecognitionException {
		TryContext _localctx = new TryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_try);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(TRY);
			setState(173);
			match(COLON);
			setState(174);
			match(INDENT);
			setState(183);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(175);
					sentence();
					{
					setState(177);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(176);
						match(SEMI_COLON);
						}
					}

					setState(179);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(185);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			{
			setState(186);
			sentence();
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(187);
				match(SEMI_COLON);
				}
			}

			}
			setState(190);
			match(DEDENT);
			setState(191);
			except();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExceptContext extends ParserRuleContext {
		public TerminalNode EXCEPT() { return getToken(QuantumLanguageParser.EXCEPT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<SentenceContext> sentence() {
			return getRuleContexts(SentenceContext.class);
		}
		public SentenceContext sentence(int i) {
			return getRuleContext(SentenceContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(QuantumLanguageParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(QuantumLanguageParser.NEWLINE, i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(QuantumLanguageParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(QuantumLanguageParser.SEMI_COLON, i);
		}
		public ExceptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_except; }
	}

	public final ExceptContext except() throws RecognitionException {
		ExceptContext _localctx = new ExceptContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_except);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(EXCEPT);
			setState(194);
			expression(0);
			setState(195);
			match(COLON);
			setState(196);
			match(INDENT);
			setState(205);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(197);
					sentence();
					{
					setState(199);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI_COLON) {
						{
						setState(198);
						match(SEMI_COLON);
						}
					}

					setState(201);
					match(NEWLINE);
					}
					}
					} 
				}
				setState(207);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			{
			setState(208);
			sentence();
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(209);
				match(SEMI_COLON);
				}
			}

			}
			setState(212);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_executionContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(QuantumLanguageParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(QuantumLanguageParser.CLOSE_PAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(QuantumLanguageParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(QuantumLanguageParser.COMMA, i);
		}
		public Function_executionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_execution; }
	}

	public final Function_executionContext function_execution() throws RecognitionException {
		Function_executionContext _localctx = new Function_executionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_function_execution);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			identifier();
			setState(215);
			match(OPEN_PAREN);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IDENTIFIER) | (1L << STRING_LITERAL) | (1L << INTEGER_LITERAL) | (1L << IMAGINARY_LITERAL) | (1L << FLOAT_LITERAL) | (1L << QUBIT_STATE_LITERAL) | (1L << ADD) | (1L << MINUS) | (1L << NOT) | (1L << TRUE) | (1L << FALSE) | (1L << OPEN_PAREN))) != 0)) {
				{
				setState(216);
				expression(0);
				setState(221);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(217);
					match(COMMA);
					setState(218);
					expression(0);
					}
					}
					setState(223);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(226);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declarationContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(QuantumLanguageParser.DEF, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode OPEN_PAREN() { return getToken(QuantumLanguageParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(QuantumLanguageParser.CLOSE_PAREN, 0); }
		public TerminalNode COLON() { return getToken(QuantumLanguageParser.COLON, 0); }
		public TerminalNode INDENT() { return getToken(QuantumLanguageParser.INDENT, 0); }
		public SentenceContext sentence() {
			return getRuleContext(SentenceContext.class,0);
		}
		public TerminalNode DEDENT() { return getToken(QuantumLanguageParser.DEDENT, 0); }
		public List<TerminalNode> COMMA() { return getTokens(QuantumLanguageParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(QuantumLanguageParser.COMMA, i);
		}
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_function_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(DEF);
			setState(229);
			identifier();
			setState(230);
			match(OPEN_PAREN);
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(231);
				identifier();
				setState(236);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(232);
					match(COMMA);
					setState(233);
					identifier();
					}
					}
					setState(238);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(241);
			match(CLOSE_PAREN);
			setState(242);
			match(COLON);
			setState(243);
			match(INDENT);
			setState(244);
			sentence();
			setState(245);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(QuantumLanguageParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			identifier();
			setState(248);
			match(ASSIGN);
			setState(249);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(QuantumLanguageParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(QuantumLanguageParser.IDENTIFIER, i);
		}
		public List<TerminalNode> DOT() { return getTokens(QuantumLanguageParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(QuantumLanguageParser.DOT, i);
		}
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_identifier);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(IDENTIFIER);
			setState(256);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(252);
					match(DOT);
					setState(253);
					match(IDENTIFIER);
					}
					} 
				}
				setState(258);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(QuantumLanguageParser.OPEN_PAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(QuantumLanguageParser.CLOSE_PAREN, 0); }
		public Unitary_operatorContext unitary_operator() {
			return getRuleContext(Unitary_operatorContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Function_executionContext function_execution() {
			return getRuleContext(Function_executionContext.class,0);
		}
		public TerminalNode INTEGER_LITERAL() { return getToken(QuantumLanguageParser.INTEGER_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(QuantumLanguageParser.STRING_LITERAL, 0); }
		public TerminalNode IMAGINARY_LITERAL() { return getToken(QuantumLanguageParser.IMAGINARY_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(QuantumLanguageParser.FLOAT_LITERAL, 0); }
		public TerminalNode TRUE() { return getToken(QuantumLanguageParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(QuantumLanguageParser.FALSE, 0); }
		public TerminalNode QUBIT_STATE_LITERAL() { return getToken(QuantumLanguageParser.QUBIT_STATE_LITERAL, 0); }
		public Binary_operatorContext binary_operator() {
			return getRuleContext(Binary_operatorContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				{
				setState(260);
				match(OPEN_PAREN);
				setState(261);
				expression(0);
				setState(262);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				{
				setState(264);
				unitary_operator();
				setState(265);
				expression(10);
				}
				break;
			case 3:
				{
				setState(267);
				identifier();
				}
				break;
			case 4:
				{
				setState(268);
				function_execution();
				}
				break;
			case 5:
				{
				setState(269);
				match(INTEGER_LITERAL);
				}
				break;
			case 6:
				{
				setState(270);
				match(STRING_LITERAL);
				}
				break;
			case 7:
				{
				setState(271);
				match(IMAGINARY_LITERAL);
				}
				break;
			case 8:
				{
				setState(272);
				match(FLOAT_LITERAL);
				}
				break;
			case 9:
				{
				setState(273);
				match(TRUE);
				}
				break;
			case 10:
				{
				setState(274);
				match(FALSE);
				}
				break;
			case 11:
				{
				setState(275);
				match(QUBIT_STATE_LITERAL);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(284);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(278);
					if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
					setState(279);
					binary_operator();
					setState(280);
					expression(12);
					}
					} 
				}
				setState(286);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Binary_operatorContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(QuantumLanguageParser.ADD, 0); }
		public TerminalNode MINUS() { return getToken(QuantumLanguageParser.MINUS, 0); }
		public TerminalNode STAR() { return getToken(QuantumLanguageParser.STAR, 0); }
		public TerminalNode DIV() { return getToken(QuantumLanguageParser.DIV, 0); }
		public TerminalNode IDIV() { return getToken(QuantumLanguageParser.IDIV, 0); }
		public TerminalNode MOD() { return getToken(QuantumLanguageParser.MOD, 0); }
		public TerminalNode POWER() { return getToken(QuantumLanguageParser.POWER, 0); }
		public TerminalNode LESS_THAN() { return getToken(QuantumLanguageParser.LESS_THAN, 0); }
		public TerminalNode GREATER_THAN() { return getToken(QuantumLanguageParser.GREATER_THAN, 0); }
		public TerminalNode EQUALS() { return getToken(QuantumLanguageParser.EQUALS, 0); }
		public TerminalNode GT_EQ() { return getToken(QuantumLanguageParser.GT_EQ, 0); }
		public TerminalNode LT_EQ() { return getToken(QuantumLanguageParser.LT_EQ, 0); }
		public TerminalNode NOT_EQ_1() { return getToken(QuantumLanguageParser.NOT_EQ_1, 0); }
		public TerminalNode NOT_EQ_2() { return getToken(QuantumLanguageParser.NOT_EQ_2, 0); }
		public Binary_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binary_operator; }
	}

	public final Binary_operatorContext binary_operator() throws RecognitionException {
		Binary_operatorContext _localctx = new Binary_operatorContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_binary_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << MINUS) | (1L << STAR) | (1L << DIV) | (1L << IDIV) | (1L << MOD) | (1L << POWER) | (1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << EQUALS) | (1L << GT_EQ) | (1L << LT_EQ) | (1L << NOT_EQ_1) | (1L << NOT_EQ_2))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Unitary_operatorContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(QuantumLanguageParser.ADD, 0); }
		public TerminalNode MINUS() { return getToken(QuantumLanguageParser.MINUS, 0); }
		public TerminalNode NOT() { return getToken(QuantumLanguageParser.NOT, 0); }
		public Unitary_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unitary_operator; }
	}

	public final Unitary_operatorContext unitary_operator() throws RecognitionException {
		Unitary_operatorContext _localctx = new Unitary_operatorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_unitary_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADD) | (1L << MINUS) | (1L << NOT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001A\u0124\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0003\u0000#\b\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000\'\b\u0000\n\u0000\f\u0000*\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0003\u0000.\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"9\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002A\b\u0002\u0001\u0002\u0001\u0002\u0005\u0002"+
		"E\b\u0002\n\u0002\f\u0002H\t\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"L\b\u0002\u0001\u0002\u0001\u0002\u0005\u0002P\b\u0002\n\u0002\f\u0002"+
		"S\t\u0002\u0001\u0002\u0003\u0002V\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003^\b\u0003\u0001"+
		"\u0003\u0001\u0003\u0005\u0003b\b\u0003\n\u0003\f\u0003e\t\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003i\b\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004r\b"+
		"\u0004\u0001\u0004\u0001\u0004\u0005\u0004v\b\u0004\n\u0004\f\u0004y\t"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004}\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u0089\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0005\u0005\u008d\b\u0005\n\u0005\f\u0005\u0090\t\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005\u0094\b\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u009e\b\u0006\u0001\u0006\u0001\u0006\u0005\u0006\u00a2\b\u0006\n\u0006"+
		"\f\u0006\u00a5\t\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u00a9\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007\u00b2\b\u0007\u0001\u0007\u0001\u0007\u0005\u0007"+
		"\u00b6\b\u0007\n\u0007\f\u0007\u00b9\t\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u00bd\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u00c8\b\b\u0001\b\u0001\b\u0005"+
		"\b\u00cc\b\b\n\b\f\b\u00cf\t\b\u0001\b\u0001\b\u0003\b\u00d3\b\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0005\t\u00dc\b\t\n"+
		"\t\f\t\u00df\t\t\u0003\t\u00e1\b\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\n\u00eb\b\n\n\n\f\n\u00ee\t\n\u0003\n"+
		"\u00f0\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u00ff"+
		"\b\f\n\f\f\f\u0102\t\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u0115\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0005"+
		"\r\u011b\b\r\n\r\f\r\u011e\t\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0000\u0001\u001a\u0010\u0000\u0002\u0004\u0006\b\n"+
		"\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e\u0000\u0002\u0002"+
		"\u0000\t\u000f\u0015\u001b\u0002\u0000\t\n,,\u0143\u0000(\u0001\u0000"+
		"\u0000\u0000\u00028\u0001\u0000\u0000\u0000\u0004:\u0001\u0000\u0000\u0000"+
		"\u0006W\u0001\u0000\u0000\u0000\bl\u0001\u0000\u0000\u0000\n\u0080\u0001"+
		"\u0000\u0000\u0000\f\u0097\u0001\u0000\u0000\u0000\u000e\u00ac\u0001\u0000"+
		"\u0000\u0000\u0010\u00c1\u0001\u0000\u0000\u0000\u0012\u00d6\u0001\u0000"+
		"\u0000\u0000\u0014\u00e4\u0001\u0000\u0000\u0000\u0016\u00f7\u0001\u0000"+
		"\u0000\u0000\u0018\u00fb\u0001\u0000\u0000\u0000\u001a\u0114\u0001\u0000"+
		"\u0000\u0000\u001c\u011f\u0001\u0000\u0000\u0000\u001e\u0121\u0001\u0000"+
		"\u0000\u0000 \"\u0003\u0002\u0001\u0000!#\u0005>\u0000\u0000\"!\u0001"+
		"\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000"+
		"$%\u0005?\u0000\u0000%\'\u0001\u0000\u0000\u0000& \u0001\u0000\u0000\u0000"+
		"\'*\u0001\u0000\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000"+
		"\u0000)+\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000+-\u0003\u0002"+
		"\u0001\u0000,.\u0005>\u0000\u0000-,\u0001\u0000\u0000\u0000-.\u0001\u0000"+
		"\u0000\u0000./\u0001\u0000\u0000\u0000/0\u0005\u0000\u0000\u00010\u0001"+
		"\u0001\u0000\u0000\u000019\u0003\u0004\u0002\u000029\u0003\n\u0005\u0000"+
		"39\u0003\f\u0006\u000049\u0003\u000e\u0007\u000059\u0003\u0012\t\u0000"+
		"69\u0003\u0016\u000b\u000079\u0003\u0014\n\u000081\u0001\u0000\u0000\u0000"+
		"82\u0001\u0000\u0000\u000083\u0001\u0000\u0000\u000084\u0001\u0000\u0000"+
		"\u000085\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000087\u0001\u0000"+
		"\u0000\u00009\u0003\u0001\u0000\u0000\u0000:;\u0005!\u0000\u0000;<\u0003"+
		"\u001a\r\u0000<=\u0005=\u0000\u0000=F\u0005\u0001\u0000\u0000>@\u0003"+
		"\u0002\u0001\u0000?A\u0005>\u0000\u0000@?\u0001\u0000\u0000\u0000@A\u0001"+
		"\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000BC\u0005?\u0000\u0000CE\u0001"+
		"\u0000\u0000\u0000D>\u0001\u0000\u0000\u0000EH\u0001\u0000\u0000\u0000"+
		"FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GI\u0001\u0000\u0000"+
		"\u0000HF\u0001\u0000\u0000\u0000IK\u0003\u0002\u0001\u0000JL\u0005>\u0000"+
		"\u0000KJ\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0001\u0000"+
		"\u0000\u0000MQ\u0005\u0002\u0000\u0000NP\u0003\u0006\u0003\u0000ON\u0001"+
		"\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000"+
		"\u0000TV\u0003\b\u0004\u0000UT\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000"+
		"\u0000V\u0005\u0001\u0000\u0000\u0000WX\u0005\"\u0000\u0000XY\u0003\u001a"+
		"\r\u0000YZ\u0005=\u0000\u0000Zc\u0005\u0001\u0000\u0000[]\u0003\u0002"+
		"\u0001\u0000\\^\u0005>\u0000\u0000]\\\u0001\u0000\u0000\u0000]^\u0001"+
		"\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_`\u0005?\u0000\u0000`b\u0001"+
		"\u0000\u0000\u0000a[\u0001\u0000\u0000\u0000be\u0001\u0000\u0000\u0000"+
		"ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000df\u0001\u0000\u0000"+
		"\u0000ec\u0001\u0000\u0000\u0000fh\u0003\u0002\u0001\u0000gi\u0005>\u0000"+
		"\u0000hg\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0001\u0000"+
		"\u0000\u0000jk\u0005\u0002\u0000\u0000k\u0007\u0001\u0000\u0000\u0000"+
		"lm\u0005#\u0000\u0000mn\u0005=\u0000\u0000nw\u0005\u0001\u0000\u0000o"+
		"q\u0003\u0002\u0001\u0000pr\u0005>\u0000\u0000qp\u0001\u0000\u0000\u0000"+
		"qr\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0005?\u0000\u0000"+
		"tv\u0001\u0000\u0000\u0000uo\u0001\u0000\u0000\u0000vy\u0001\u0000\u0000"+
		"\u0000wu\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000xz\u0001\u0000"+
		"\u0000\u0000yw\u0001\u0000\u0000\u0000z|\u0003\u0002\u0001\u0000{}\u0005"+
		">\u0000\u0000|{\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}~\u0001"+
		"\u0000\u0000\u0000~\u007f\u0005\u0002\u0000\u0000\u007f\t\u0001\u0000"+
		"\u0000\u0000\u0080\u0081\u0005%\u0000\u0000\u0081\u0082\u0003\u0018\f"+
		"\u0000\u0082\u0083\u0005&\u0000\u0000\u0083\u0084\u0003\u001a\r\u0000"+
		"\u0084\u0085\u0005=\u0000\u0000\u0085\u008e\u0005\u0001\u0000\u0000\u0086"+
		"\u0088\u0003\u0002\u0001\u0000\u0087\u0089\u0005>\u0000\u0000\u0088\u0087"+
		"\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0001\u0000\u0000\u0000\u008a\u008b\u0005?\u0000\u0000\u008b\u008d\u0001"+
		"\u0000\u0000\u0000\u008c\u0086\u0001\u0000\u0000\u0000\u008d\u0090\u0001"+
		"\u0000\u0000\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008e\u008f\u0001"+
		"\u0000\u0000\u0000\u008f\u0091\u0001\u0000\u0000\u0000\u0090\u008e\u0001"+
		"\u0000\u0000\u0000\u0091\u0093\u0003\u0002\u0001\u0000\u0092\u0094\u0005"+
		">\u0000\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000"+
		"\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u0096\u0005\u0002"+
		"\u0000\u0000\u0096\u000b\u0001\u0000\u0000\u0000\u0097\u0098\u0005$\u0000"+
		"\u0000\u0098\u0099\u0003\u001a\r\u0000\u0099\u009a\u0005=\u0000\u0000"+
		"\u009a\u00a3\u0005\u0001\u0000\u0000\u009b\u009d\u0003\u0002\u0001\u0000"+
		"\u009c\u009e\u0005>\u0000\u0000\u009d\u009c\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000\u009f"+
		"\u00a0\u0005?\u0000\u0000\u00a0\u00a2\u0001\u0000\u0000\u0000\u00a1\u009b"+
		"\u0001\u0000\u0000\u0000\u00a2\u00a5\u0001\u0000\u0000\u0000\u00a3\u00a1"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a6"+
		"\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a6\u00a8"+
		"\u0003\u0002\u0001\u0000\u00a7\u00a9\u0005>\u0000\u0000\u00a8\u00a7\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001"+
		"\u0000\u0000\u0000\u00aa\u00ab\u0005\u0002\u0000\u0000\u00ab\r\u0001\u0000"+
		"\u0000\u0000\u00ac\u00ad\u0005\'\u0000\u0000\u00ad\u00ae\u0005=\u0000"+
		"\u0000\u00ae\u00b7\u0005\u0001\u0000\u0000\u00af\u00b1\u0003\u0002\u0001"+
		"\u0000\u00b0\u00b2\u0005>\u0000\u0000\u00b1\u00b0\u0001\u0000\u0000\u0000"+
		"\u00b1\u00b2\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000"+
		"\u00b3\u00b4\u0005?\u0000\u0000\u00b4\u00b6\u0001\u0000\u0000\u0000\u00b5"+
		"\u00af\u0001\u0000\u0000\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000\u00b7"+
		"\u00b5\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8"+
		"\u00ba\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00ba"+
		"\u00bc\u0003\u0002\u0001\u0000\u00bb\u00bd\u0005>\u0000\u0000\u00bc\u00bb"+
		"\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000\u0000\u00bd\u00be"+
		"\u0001\u0000\u0000\u0000\u00be\u00bf\u0005\u0002\u0000\u0000\u00bf\u00c0"+
		"\u0003\u0010\b\u0000\u00c0\u000f\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005"+
		")\u0000\u0000\u00c2\u00c3\u0003\u001a\r\u0000\u00c3\u00c4\u0005=\u0000"+
		"\u0000\u00c4\u00cd\u0005\u0001\u0000\u0000\u00c5\u00c7\u0003\u0002\u0001"+
		"\u0000\u00c6\u00c8\u0005>\u0000\u0000\u00c7\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c7\u00c8\u0001\u0000\u0000\u0000\u00c8\u00c9\u0001\u0000\u0000\u0000"+
		"\u00c9\u00ca\u0005?\u0000\u0000\u00ca\u00cc\u0001\u0000\u0000\u0000\u00cb"+
		"\u00c5\u0001\u0000\u0000\u0000\u00cc\u00cf\u0001\u0000\u0000\u0000\u00cd"+
		"\u00cb\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce"+
		"\u00d0\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d2\u0003\u0002\u0001\u0000\u00d1\u00d3\u0005>\u0000\u0000\u00d2\u00d1"+
		"\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005\u0002\u0000\u0000\u00d5\u0011"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d7\u0003\u0018\f\u0000\u00d7\u00e0\u0005"+
		"5\u0000\u0000\u00d8\u00dd\u0003\u001a\r\u0000\u00d9\u00da\u0005<\u0000"+
		"\u0000\u00da\u00dc\u0003\u001a\r\u0000\u00db\u00d9\u0001\u0000\u0000\u0000"+
		"\u00dc\u00df\u0001\u0000\u0000\u0000\u00dd\u00db\u0001\u0000\u0000\u0000"+
		"\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00e1\u0001\u0000\u0000\u0000"+
		"\u00df\u00dd\u0001\u0000\u0000\u0000\u00e0\u00d8\u0001\u0000\u0000\u0000"+
		"\u00e0\u00e1\u0001\u0000\u0000\u0000\u00e1\u00e2\u0001\u0000\u0000\u0000"+
		"\u00e2\u00e3\u00056\u0000\u0000\u00e3\u0013\u0001\u0000\u0000\u0000\u00e4"+
		"\u00e5\u0005\u001d\u0000\u0000\u00e5\u00e6\u0003\u0018\f\u0000\u00e6\u00ef"+
		"\u00055\u0000\u0000\u00e7\u00ec\u0003\u0018\f\u0000\u00e8\u00e9\u0005"+
		"<\u0000\u0000\u00e9\u00eb\u0003\u0018\f\u0000\u00ea\u00e8\u0001\u0000"+
		"\u0000\u0000\u00eb\u00ee\u0001\u0000\u0000\u0000\u00ec\u00ea\u0001\u0000"+
		"\u0000\u0000\u00ec\u00ed\u0001\u0000\u0000\u0000\u00ed\u00f0\u0001\u0000"+
		"\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ef\u00e7\u0001\u0000"+
		"\u0000\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00f1\u0001\u0000"+
		"\u0000\u0000\u00f1\u00f2\u00056\u0000\u0000\u00f2\u00f3\u0005=\u0000\u0000"+
		"\u00f3\u00f4\u0005\u0001\u0000\u0000\u00f4\u00f5\u0003\u0002\u0001\u0000"+
		"\u00f5\u00f6\u0005\u0002\u0000\u0000\u00f6\u0015\u0001\u0000\u0000\u0000"+
		"\u00f7\u00f8\u0003\u0018\f\u0000\u00f8\u00f9\u0005\u001c\u0000\u0000\u00f9"+
		"\u00fa\u0003\u001a\r\u0000\u00fa\u0017\u0001\u0000\u0000\u0000\u00fb\u0100"+
		"\u0005\u0003\u0000\u0000\u00fc\u00fd\u0005;\u0000\u0000\u00fd\u00ff\u0005"+
		"\u0003\u0000\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00ff\u0102\u0001"+
		"\u0000\u0000\u0000\u0100\u00fe\u0001\u0000\u0000\u0000\u0100\u0101\u0001"+
		"\u0000\u0000\u0000\u0101\u0019\u0001\u0000\u0000\u0000\u0102\u0100\u0001"+
		"\u0000\u0000\u0000\u0103\u0104\u0006\r\uffff\uffff\u0000\u0104\u0105\u0005"+
		"5\u0000\u0000\u0105\u0106\u0003\u001a\r\u0000\u0106\u0107\u00056\u0000"+
		"\u0000\u0107\u0115\u0001\u0000\u0000\u0000\u0108\u0109\u0003\u001e\u000f"+
		"\u0000\u0109\u010a\u0003\u001a\r\n\u010a\u0115\u0001\u0000\u0000\u0000"+
		"\u010b\u0115\u0003\u0018\f\u0000\u010c\u0115\u0003\u0012\t\u0000\u010d"+
		"\u0115\u0005\u0005\u0000\u0000\u010e\u0115\u0005\u0004\u0000\u0000\u010f"+
		"\u0115\u0005\u0006\u0000\u0000\u0110\u0115\u0005\u0007\u0000\u0000\u0111"+
		"\u0115\u0005/\u0000\u0000\u0112\u0115\u00050\u0000\u0000\u0113\u0115\u0005"+
		"\b\u0000\u0000\u0114\u0103\u0001\u0000\u0000\u0000\u0114\u0108\u0001\u0000"+
		"\u0000\u0000\u0114\u010b\u0001\u0000\u0000\u0000\u0114\u010c\u0001\u0000"+
		"\u0000\u0000\u0114\u010d\u0001\u0000\u0000\u0000\u0114\u010e\u0001\u0000"+
		"\u0000\u0000\u0114\u010f\u0001\u0000\u0000\u0000\u0114\u0110\u0001\u0000"+
		"\u0000\u0000\u0114\u0111\u0001\u0000\u0000\u0000\u0114\u0112\u0001\u0000"+
		"\u0000\u0000\u0114\u0113\u0001\u0000\u0000\u0000\u0115\u011c\u0001\u0000"+
		"\u0000\u0000\u0116\u0117\n\u000b\u0000\u0000\u0117\u0118\u0003\u001c\u000e"+
		"\u0000\u0118\u0119\u0003\u001a\r\f\u0119\u011b\u0001\u0000\u0000\u0000"+
		"\u011a\u0116\u0001\u0000\u0000\u0000\u011b\u011e\u0001\u0000\u0000\u0000"+
		"\u011c\u011a\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000\u0000\u0000"+
		"\u011d\u001b\u0001\u0000\u0000\u0000\u011e\u011c\u0001\u0000\u0000\u0000"+
		"\u011f\u0120\u0007\u0000\u0000\u0000\u0120\u001d\u0001\u0000\u0000\u0000"+
		"\u0121\u0122\u0007\u0001\u0000\u0000\u0122\u001f\u0001\u0000\u0000\u0000"+
		"\"\"(-8@FKQU]chqw|\u0088\u008e\u0093\u009d\u00a3\u00a8\u00b1\u00b7\u00bc"+
		"\u00c7\u00cd\u00d2\u00dd\u00e0\u00ec\u00ef\u0100\u0114\u011c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}