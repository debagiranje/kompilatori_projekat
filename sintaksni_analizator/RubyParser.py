# Generated from sintaksni_analizator/RubyParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u0278\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\7\2\u008a\n\2\f\2\16\2\u008d\13\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\6\3\u0095\n\3\r\3\16\3\u0096\3\3\7\3\u009a")
        buf.write("\n\3\f\3\16\3\u009d\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\u00a9\n\4\3\5\3\5\3\5\3\5\5\5\u00af\n\5")
        buf.write("\3\5\7\5\u00b2\n\5\f\5\16\5\u00b5\13\5\3\5\7\5\u00b8\n")
        buf.write("\5\f\5\16\5\u00bb\13\5\3\5\5\5\u00be\n\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6\u00c8\n\6\f\6\16\6\u00cb\13\6\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\f\5\f\u00e0\n\f\3\f\3\f\5\f\u00e4")
        buf.write("\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00f3\n\16\3\17\3\17\5\17\u00f7\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0100\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\7\21\u0108\n\21\f\21\16\21\u010b")
        buf.write("\13\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u0116\n\24\7\24\u0118\n\24\f\24\16\24\u011b\13\24")
        buf.write("\3\24\3\24\5\24\u011f\n\24\3\24\3\24\3\24\5\24\u0124\n")
        buf.write("\24\3\25\6\25\u0127\n\25\r\25\16\25\u0128\3\26\3\26\5")
        buf.write("\26\u012d\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u0137\n\27\f\27\16\27\u013a\13\27\3\30\3\30\5\30")
        buf.write("\u013e\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u014a\n\32\3\33\3\33\3\34\3\34\5\34\u0150")
        buf.write("\n\34\3\35\3\35\5\35\u0154\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\7\36\u015b\n\36\f\36\16\36\u015e\13\36\3\36\5\36\u0161")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u017c")
        buf.write("\n\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3%\3%\3%\3%")
        buf.write("\5%\u018d\n%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u0197\n%\f%\16")
        buf.write("%\u019a\13%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01a4\n&\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01ae\n\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\5(\u01b8\n(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\3,\7,\u01cd\n,\f,\16,\u01d0\13")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01dc\n-\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u01e4\n.\3.\3.\3.\3.\3.\3.\7.\u01ec\n.\f.\16")
        buf.write(".\u01ef\13.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01fb\n/")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0205\n")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u020b\n\61\3\62\3\62\5\62")
        buf.write("\u020f\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u0225\n\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\7\63\u023c\n\63\f\63\16\63\u023f")
        buf.write("\13\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\5=\u0256\n=\3=\3=\3=\3")
        buf.write("=\7=\u025c\n=\f=\16=\u025f\13=\3>\3>\3?\6?\u0264\n?\r")
        buf.write("?\16?\u0265\3@\3@\3A\3A\3B\3B\3C\3C\3C\3C\3C\3C\5C\u0274")
        buf.write("\nC\3D\3D\3D\2\t ,HVZdxE\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\2\n\3\2=?\3\2%")
        buf.write("*\3\2\32\34\3\2\30\31\3\2 #\3\2\36\37\3\2\r\16\3\2\25")
        buf.write("\27\2\u028e\2\u008b\3\2\2\2\4\u0094\3\2\2\2\6\u00a8\3")
        buf.write("\2\2\2\b\u00aa\3\2\2\2\n\u00c1\3\2\2\2\f\u00ce\3\2\2\2")
        buf.write("\16\u00d0\3\2\2\2\20\u00d4\3\2\2\2\22\u00d8\3\2\2\2\24")
        buf.write("\u00da\3\2\2\2\26\u00df\3\2\2\2\30\u00e7\3\2\2\2\32\u00f2")
        buf.write("\3\2\2\2\34\u00f6\3\2\2\2\36\u00ff\3\2\2\2 \u0101\3\2")
        buf.write("\2\2\"\u010c\3\2\2\2$\u010e\3\2\2\2&\u0123\3\2\2\2(\u0126")
        buf.write("\3\2\2\2*\u012a\3\2\2\2,\u0130\3\2\2\2.\u013d\3\2\2\2")
        buf.write("\60\u013f\3\2\2\2\62\u0149\3\2\2\2\64\u014b\3\2\2\2\66")
        buf.write("\u014f\3\2\2\28\u0153\3\2\2\2:\u0155\3\2\2\2<\u0164\3")
        buf.write("\2\2\2>\u0169\3\2\2\2@\u016d\3\2\2\2B\u0173\3\2\2\2D\u0181")
        buf.write("\3\2\2\2F\u0183\3\2\2\2H\u018c\3\2\2\2J\u01a3\3\2\2\2")
        buf.write("L\u01ad\3\2\2\2N\u01b7\3\2\2\2P\u01b9\3\2\2\2R\u01be\3")
        buf.write("\2\2\2T\u01c2\3\2\2\2V\u01c6\3\2\2\2X\u01db\3\2\2\2Z\u01e3")
        buf.write("\3\2\2\2\\\u01fa\3\2\2\2^\u0204\3\2\2\2`\u020a\3\2\2\2")
        buf.write("b\u020e\3\2\2\2d\u0224\3\2\2\2f\u0240\3\2\2\2h\u0242\3")
        buf.write("\2\2\2j\u0244\3\2\2\2l\u0246\3\2\2\2n\u0248\3\2\2\2p\u024a")
        buf.write("\3\2\2\2r\u024c\3\2\2\2t\u024e\3\2\2\2v\u0250\3\2\2\2")
        buf.write("x\u0255\3\2\2\2z\u0260\3\2\2\2|\u0263\3\2\2\2~\u0267\3")
        buf.write("\2\2\2\u0080\u0269\3\2\2\2\u0082\u026b\3\2\2\2\u0084\u0273")
        buf.write("\3\2\2\2\u0086\u0275\3\2\2\2\u0088\u008a\5x=\2\u0089\u0088")
        buf.write("\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008e\u008f\5\4\3\2\u008f\u0090\7\2\2\3\u0090\3\3\2\2")
        buf.write("\2\u0091\u0092\5\6\4\2\u0092\u0093\5x=\2\u0093\u0095\3")
        buf.write("\2\2\2\u0094\u0091\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u009b\3\2\2\2\u0098")
        buf.write("\u009a\5x=\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\5\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u00a9\5\b\5\2\u009f\u00a9\5\26\f")
        buf.write("\2\u00a0\u00a9\5\24\13\2\u00a1\u00a9\5:\36\2\u00a2\u00a9")
        buf.write("\5d\63\2\u00a3\u00a9\5$\23\2\u00a4\u00a9\5@!\2\u00a5\u00a9")
        buf.write("\5B\"\2\u00a6\u00a9\5L\'\2\u00a7\u00a9\5J&\2\u00a8\u009e")
        buf.write("\3\2\2\2\u00a8\u009f\3\2\2\2\u00a8\u00a0\3\2\2\2\u00a8")
        buf.write("\u00a1\3\2\2\2\u00a8\u00a2\3\2\2\2\u00a8\u00a3\3\2\2\2")
        buf.write("\u00a8\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\7\3\2\2\2\u00aa\u00ab")
        buf.write("\7\3\2\2\u00ab\u00ae\5r:\2\u00ac\u00ad\7 \2\2\u00ad\u00af")
        buf.write("\5r:\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b3")
        buf.write("\3\2\2\2\u00b0\u00b2\5|?\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b9\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b8\5\n\6\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bc\u00be\5\4\3\2\u00bd\u00bc\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\7\6\2\2")
        buf.write("\u00c0\t\3\2\2\2\u00c1\u00c2\5\f\7\2\u00c2\u00c3\7\67")
        buf.write("\2\2\u00c3\u00c9\5r:\2\u00c4\u00c5\7\66\2\2\u00c5\u00c6")
        buf.write("\7\67\2\2\u00c6\u00c8\5r:\2\u00c7\u00c4\3\2\2\2\u00c8")
        buf.write("\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\5")
        buf.write("|?\2\u00cd\13\3\2\2\2\u00ce\u00cf\t\2\2\2\u00cf\r\3\2")
        buf.write("\2\2\u00d0\u00d1\5b\62\2\u00d1\u00d2\7\35\2\2\u00d2\u00d3")
        buf.write("\5t;\2\u00d3\17\3\2\2\2\u00d4\u00d5\5t;\2\u00d5\u00d6")
        buf.write("\7\35\2\2\u00d6\u00d7\5\66\34\2\u00d7\21\3\2\2\2\u00d8")
        buf.write("\u00d9\5t;\2\u00d9\23\3\2\2\2\u00da\u00db\5&\24\2\u00db")
        buf.write("\25\3\2\2\2\u00dc\u00dd\5\u0080A\2\u00dd\u00de\5|?\2\u00de")
        buf.write("\u00e0\3\2\2\2\u00df\u00dc\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e3\5\32\16\2\u00e2\u00e4")
        buf.write("\5\30\r\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00e6\7\6\2\2\u00e6\27\3\2\2\2\u00e7")
        buf.write("\u00e8\5\4\3\2\u00e8\31\3\2\2\2\u00e9\u00ea\7\5\2\2\u00ea")
        buf.write("\u00eb\5\34\17\2\u00eb\u00ec\5|?\2\u00ec\u00f3\3\2\2\2")
        buf.write("\u00ed\u00ee\7\5\2\2\u00ee\u00ef\5\34\17\2\u00ef\u00f0")
        buf.write("\5\36\20\2\u00f0\u00f1\5|?\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00e9\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f3\33\3\2\2\2\u00f4")
        buf.write("\u00f7\5v<\2\u00f5\u00f7\5r:\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f7\35\3\2\2\2\u00f8\u00f9\7\60\2\2\u00f9")
        buf.write("\u0100\7\61\2\2\u00fa\u00fb\7\60\2\2\u00fb\u00fc\5 \21")
        buf.write("\2\u00fc\u00fd\7\61\2\2\u00fd\u0100\3\2\2\2\u00fe\u0100")
        buf.write("\5 \21\2\u00ff\u00f8\3\2\2\2\u00ff\u00fa\3\2\2\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100\37\3\2\2\2\u0101\u0102\b\21\1\2\u0102")
        buf.write("\u0103\5\"\22\2\u0103\u0109\3\2\2\2\u0104\u0105\f\3\2")
        buf.write("\2\u0105\u0106\7\66\2\2\u0106\u0108\5\"\22\2\u0107\u0104")
        buf.write("\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a!\3\2\2\2\u010b\u0109\3\2\2\2\u010c")
        buf.write("\u010d\5r:\2\u010d#\3\2\2\2\u010e\u010f\7\f\2\2\u010f")
        buf.write("\u0110\5\66\34\2\u0110%\3\2\2\2\u0111\u0119\5\u0084C\2")
        buf.write("\u0112\u0113\7$\2\2\u0113\u0115\5\34\17\2\u0114\u0116")
        buf.write("\5*\26\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0118\3\2\2\2\u0117\u0112\3\2\2\2\u0118\u011b\3\2\2\2")
        buf.write("\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0124\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011c\u011e\5\34\17\2\u011d")
        buf.write("\u011f\5*\26\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f\u0124\3\2\2\2\u0120\u0121\5\34\17\2\u0121\u0122")
        buf.write("\5(\25\2\u0122\u0124\3\2\2\2\u0123\u0111\3\2\2\2\u0123")
        buf.write("\u011c\3\2\2\2\u0123\u0120\3\2\2\2\u0124\'\3\2\2\2\u0125")
        buf.write("\u0127\5.\30\2\u0126\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129)\3\2\2")
        buf.write("\2\u012a\u012c\7\60\2\2\u012b\u012d\5,\27\2\u012c\u012b")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u012f\7\61\2\2\u012f+\3\2\2\2\u0130\u0131\b\27\1\2\u0131")
        buf.write("\u0132\5.\30\2\u0132\u0138\3\2\2\2\u0133\u0134\f\3\2\2")
        buf.write("\u0134\u0135\7\66\2\2\u0135\u0137\5.\30\2\u0136\u0133")
        buf.write("\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139-\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013e\5\60\31\2\u013c\u013e\5\62\32\2\u013d\u013b\3\2")
        buf.write("\2\2\u013d\u013c\3\2\2\2\u013e/\3\2\2\2\u013f\u0140\5")
        buf.write("Z.\2\u0140\61\3\2\2\2\u0141\u0142\5r:\2\u0142\u0143\7")
        buf.write("\35\2\2\u0143\u0144\5Z.\2\u0144\u014a\3\2\2\2\u0145\u0146")
        buf.write("\5r:\2\u0146\u0147\7\67\2\2\u0147\u0148\5Z.\2\u0148\u014a")
        buf.write("\3\2\2\2\u0149\u0141\3\2\2\2\u0149\u0145\3\2\2\2\u014a")
        buf.write("\63\3\2\2\2\u014b\u014c\5&\24\2\u014c\65\3\2\2\2\u014d")
        buf.write("\u0150\5Z.\2\u014e\u0150\5\22\n\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u014e\3\2\2\2\u0150\67\3\2\2\2\u0151\u0154\5^\60")
        buf.write("\2\u0152\u0154\5n8\2\u0153\u0151\3\2\2\2\u0153\u0152\3")
        buf.write("\2\2\2\u01549\3\2\2\2\u0155\u0156\7\7\2\2\u0156\u0157")
        buf.write("\58\35\2\u0157\u0158\5|?\2\u0158\u015c\5F$\2\u0159\u015b")
        buf.write("\5<\37\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0161\5> \2\u0160\u015f\3\2")
        buf.write("\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163")
        buf.write("\7\6\2\2\u0163;\3\2\2\2\u0164\u0165\7\t\2\2\u0165\u0166")
        buf.write("\58\35\2\u0166\u0167\5|?\2\u0167\u0168\5F$\2\u0168=\3")
        buf.write("\2\2\2\u0169\u016a\5z>\2\u016a\u016b\5|?\2\u016b\u016c")
        buf.write("\5F$\2\u016c?\3\2\2\2\u016d\u016e\7\n\2\2\u016e\u016f")
        buf.write("\58\35\2\u016f\u0170\5|?\2\u0170\u0171\5F$\2\u0171\u0172")
        buf.write("\7\6\2\2\u0172A\3\2\2\2\u0173\u0174\7\20\2\2\u0174\u0175")
        buf.write("\5r:\2\u0175\u017b\7\22\2\2\u0176\u0177\5l\67\2\u0177")
        buf.write("\u0178\5\u0082B\2\u0178\u0179\5l\67\2\u0179\u017c\3\2")
        buf.write("\2\2\u017a\u017c\5\\/\2\u017b\u0176\3\2\2\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\5|?\2\u017e\u017f")
        buf.write("\5F$\2\u017f\u0180\7\6\2\2\u0180C\3\2\2\2\u0181\u0182")
        buf.write("\5N(\2\u0182E\3\2\2\2\u0183\u0184\5H%\2\u0184G\3\2\2\2")
        buf.write("\u0185\u0186\b%\1\2\u0186\u0187\5\6\4\2\u0187\u0188\5")
        buf.write("x=\2\u0188\u018d\3\2\2\2\u0189\u018a\5f\64\2\u018a\u018b")
        buf.write("\5x=\2\u018b\u018d\3\2\2\2\u018c\u0185\3\2\2\2\u018c\u0189")
        buf.write("\3\2\2\2\u018d\u0198\3\2\2\2\u018e\u018f\f\4\2\2\u018f")
        buf.write("\u0190\5\6\4\2\u0190\u0191\5x=\2\u0191\u0197\3\2\2\2\u0192")
        buf.write("\u0193\f\3\2\2\u0193\u0194\5f\64\2\u0194\u0195\5x=\2\u0195")
        buf.write("\u0197\3\2\2\2\u0196\u018e\3\2\2\2\u0196\u0192\3\2\2\2")
        buf.write("\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199I\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c")
        buf.write("\5b\62\2\u019c\u019d\7\35\2\2\u019d\u019e\5d\63\2\u019e")
        buf.write("\u01a4\3\2\2\2\u019f\u01a0\5b\62\2\u01a0\u01a1\t\3\2\2")
        buf.write("\u01a1\u01a2\5d\63\2\u01a2\u01a4\3\2\2\2\u01a3\u019b\3")
        buf.write("\2\2\2\u01a3\u019f\3\2\2\2\u01a4K\3\2\2\2\u01a5\u01a6")
        buf.write("\5~@\2\u01a6\u01a7\7\35\2\2\u01a7\u01a8\5d\63\2\u01a8")
        buf.write("\u01ae\3\2\2\2\u01a9\u01aa\5~@\2\u01aa\u01ab\t\3\2\2\u01ab")
        buf.write("\u01ac\5d\63\2\u01ac\u01ae\3\2\2\2\u01ad\u01a5\3\2\2\2")
        buf.write("\u01ad\u01a9\3\2\2\2\u01aeM\3\2\2\2\u01af\u01b0\5b\62")
        buf.write("\2\u01b0\u01b1\7\35\2\2\u01b1\u01b2\5Z.\2\u01b2\u01b8")
        buf.write("\3\2\2\2\u01b3\u01b4\5b\62\2\u01b4\u01b5\t\3\2\2\u01b5")
        buf.write("\u01b6\5Z.\2\u01b6\u01b8\3\2\2\2\u01b7\u01af\3\2\2\2\u01b7")
        buf.write("\u01b3\3\2\2\2\u01b8O\3\2\2\2\u01b9\u01ba\5b\62\2\u01ba")
        buf.write("\u01bb\7\35\2\2\u01bb\u01bc\7\64\2\2\u01bc\u01bd\7\65")
        buf.write("\2\2\u01bdQ\3\2\2\2\u01be\u01bf\5X-\2\u01bf\u01c0\7\35")
        buf.write("\2\2\u01c0\u01c1\5Z.\2\u01c1S\3\2\2\2\u01c2\u01c3\7\64")
        buf.write("\2\2\u01c3\u01c4\5V,\2\u01c4\u01c5\7\65\2\2\u01c5U\3\2")
        buf.write("\2\2\u01c6\u01c7\b,\1\2\u01c7\u01c8\5Z.\2\u01c8\u01ce")
        buf.write("\3\2\2\2\u01c9\u01ca\f\3\2\2\u01ca\u01cb\7\66\2\2\u01cb")
        buf.write("\u01cd\5Z.\2\u01cc\u01c9\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cfW\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d1\u01d2\5r:\2\u01d2\u01d3\7\64\2\2")
        buf.write("\u01d3\u01d4\5Z.\2\u01d4\u01d5\7\65\2\2\u01d5\u01dc\3")
        buf.write("\2\2\2\u01d6\u01d7\5t;\2\u01d7\u01d8\7\64\2\2\u01d8\u01d9")
        buf.write("\5Z.\2\u01d9\u01da\7\65\2\2\u01da\u01dc\3\2\2\2\u01db")
        buf.write("\u01d1\3\2\2\2\u01db\u01d6\3\2\2\2\u01dcY\3\2\2\2\u01dd")
        buf.write("\u01de\b.\1\2\u01de\u01df\7\60\2\2\u01df\u01e0\5Z.\2\u01e0")
        buf.write("\u01e1\7\61\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e4\5\\/\2")
        buf.write("\u01e3\u01dd\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01ed\3")
        buf.write("\2\2\2\u01e5\u01e6\f\6\2\2\u01e6\u01e7\t\4\2\2\u01e7\u01ec")
        buf.write("\5Z.\7\u01e8\u01e9\f\5\2\2\u01e9\u01ea\t\5\2\2\u01ea\u01ec")
        buf.write("\5Z.\6\u01eb\u01e5\3\2\2\2\u01eb\u01e8\3\2\2\2\u01ec\u01ef")
        buf.write("\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write("[\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01fb\5r:\2\u01f1")
        buf.write("\u01fb\5l\67\2\u01f2\u01fb\5j\66\2\u01f3\u01fb\5h\65\2")
        buf.write("\u01f4\u01fb\5\u0086D\2\u01f5\u01fb\5n8\2\u01f6\u01fb")
        buf.write("\5p9\2\u01f7\u01fb\5&\24\2\u01f8\u01fb\5t;\2\u01f9\u01fb")
        buf.write("\5X-\2\u01fa\u01f0\3\2\2\2\u01fa\u01f1\3\2\2\2\u01fa\u01f2")
        buf.write("\3\2\2\2\u01fa\u01f3\3\2\2\2\u01fa\u01f4\3\2\2\2\u01fa")
        buf.write("\u01f5\3\2\2\2\u01fa\u01f6\3\2\2\2\u01fa\u01f7\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb]\3\2\2")
        buf.write("\2\u01fc\u01fd\5`\61\2\u01fd\u01fe\t\6\2\2\u01fe\u01ff")
        buf.write("\5`\61\2\u01ff\u0205\3\2\2\2\u0200\u0201\5`\61\2\u0201")
        buf.write("\u0202\t\7\2\2\u0202\u0203\5`\61\2\u0203\u0205\3\2\2\2")
        buf.write("\u0204\u01fc\3\2\2\2\u0204\u0200\3\2\2\2\u0205_\3\2\2")
        buf.write("\2\u0206\u020b\5Z.\2\u0207\u020b\5X-\2\u0208\u020b\5r")
        buf.write(":\2\u0209\u020b\5~@\2\u020a\u0206\3\2\2\2\u020a\u0207")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("a\3\2\2\2\u020c\u020f\5r:\2\u020d\u020f\5~@\2\u020e\u020c")
        buf.write("\3\2\2\2\u020e\u020d\3\2\2\2\u020fc\3\2\2\2\u0210\u0211")
        buf.write("\b\63\1\2\u0211\u0225\5b\62\2\u0212\u0225\5P)\2\u0213")
        buf.write("\u0225\5R*\2\u0214\u0225\5N(\2\u0215\u0225\5J&\2\u0216")
        buf.write("\u0225\5&\24\2\u0217\u0225\5n8\2\u0218\u0225\5j\66\2\u0219")
        buf.write("\u0225\5l\67\2\u021a\u0225\5p9\2\u021b\u0225\5Z.\2\u021c")
        buf.write("\u021d\7+\2\2\u021d\u0225\5d\63\13\u021e\u021f\7/\2\2")
        buf.write("\u021f\u0225\5d\63\4\u0220\u0221\7\60\2\2\u0221\u0222")
        buf.write("\5d\63\2\u0222\u0223\7\61\2\2\u0223\u0225\3\2\2\2\u0224")
        buf.write("\u0210\3\2\2\2\u0224\u0212\3\2\2\2\u0224\u0213\3\2\2\2")
        buf.write("\u0224\u0214\3\2\2\2\u0224\u0215\3\2\2\2\u0224\u0216\3")
        buf.write("\2\2\2\u0224\u0217\3\2\2\2\u0224\u0218\3\2\2\2\u0224\u0219")
        buf.write("\3\2\2\2\u0224\u021a\3\2\2\2\u0224\u021b\3\2\2\2\u0224")
        buf.write("\u021c\3\2\2\2\u0224\u021e\3\2\2\2\u0224\u0220\3\2\2\2")
        buf.write("\u0225\u023d\3\2\2\2\u0226\u0227\f\f\2\2\u0227\u0228\7")
        buf.write(",\2\2\u0228\u023c\5d\63\r\u0229\u022a\f\n\2\2\u022a\u022b")
        buf.write("\t\4\2\2\u022b\u023c\5d\63\13\u022c\u022d\f\t\2\2\u022d")
        buf.write("\u022e\t\5\2\2\u022e\u023c\5d\63\n\u022f\u0230\f\b\2\2")
        buf.write("\u0230\u0231\t\6\2\2\u0231\u023c\5d\63\t\u0232\u0233\f")
        buf.write("\7\2\2\u0233\u0234\t\7\2\2\u0234\u023c\5d\63\b\u0235\u0236")
        buf.write("\f\6\2\2\u0236\u0237\7-\2\2\u0237\u023c\5d\63\7\u0238")
        buf.write("\u0239\f\5\2\2\u0239\u023a\7.\2\2\u023a\u023c\5d\63\6")
        buf.write("\u023b\u0226\3\2\2\2\u023b\u0229\3\2\2\2\u023b\u022c\3")
        buf.write("\2\2\2\u023b\u022f\3\2\2\2\u023b\u0232\3\2\2\2\u023b\u0235")
        buf.write("\3\2\2\2\u023b\u0238\3\2\2\2\u023c\u023f\3\2\2\2\u023d")
        buf.write("\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023ee\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u0240\u0241\7\23\2\2\u0241g\3\2\2\2\u0242")
        buf.write("\u0243\7;\2\2\u0243i\3\2\2\2\u0244\u0245\7:\2\2\u0245")
        buf.write("k\3\2\2\2\u0246\u0247\79\2\2\u0247m\3\2\2\2\u0248\u0249")
        buf.write("\t\b\2\2\u0249o\3\2\2\2\u024a\u024b\7\17\2\2\u024bq\3")
        buf.write("\2\2\2\u024c\u024d\7@\2\2\u024ds\3\2\2\2\u024e\u024f\7")
        buf.write("B\2\2\u024fu\3\2\2\2\u0250\u0251\7C\2\2\u0251w\3\2\2\2")
        buf.write("\u0252\u0253\b=\1\2\u0253\u0256\78\2\2\u0254\u0256\5|")
        buf.write("?\2\u0255\u0252\3\2\2\2\u0255\u0254\3\2\2\2\u0256\u025d")
        buf.write("\3\2\2\2\u0257\u0258\f\6\2\2\u0258\u025c\78\2\2\u0259")
        buf.write("\u025a\f\5\2\2\u025a\u025c\5|?\2\u025b\u0257\3\2\2\2\u025b")
        buf.write("\u0259\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2")
        buf.write("\u025d\u025e\3\2\2\2\u025ey\3\2\2\2\u025f\u025d\3\2\2")
        buf.write("\2\u0260\u0261\7\b\2\2\u0261{\3\2\2\2\u0262\u0264\7F\2")
        buf.write("\2\u0263\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u0266}\3\2\2\2\u0267\u0268")
        buf.write("\7A\2\2\u0268\177\3\2\2\2\u0269\u026a\t\t\2\2\u026a\u0081")
        buf.write("\3\2\2\2\u026b\u026c\7\24\2\2\u026c\u0083\3\2\2\2\u026d")
        buf.write("\u0274\5r:\2\u026e\u0274\5~@\2\u026f\u0270\7\60\2\2\u0270")
        buf.write("\u0271\5\6\4\2\u0271\u0272\7\61\2\2\u0272\u0274\3\2\2")
        buf.write("\2\u0273\u026d\3\2\2\2\u0273\u026e\3\2\2\2\u0273\u026f")
        buf.write("\3\2\2\2\u0274\u0085\3\2\2\2\u0275\u0276\7<\2\2\u0276")
        buf.write("\u0087\3\2\2\2\66\u008b\u0096\u009b\u00a8\u00ae\u00b3")
        buf.write("\u00b9\u00bd\u00c9\u00df\u00e3\u00f2\u00f6\u00ff\u0109")
        buf.write("\u0115\u0119\u011e\u0123\u0128\u012c\u0138\u013d\u0149")
        buf.write("\u014f\u0153\u015c\u0160\u017b\u018c\u0196\u0198\u01a3")
        buf.write("\u01ad\u01b7\u01ce\u01db\u01e3\u01eb\u01ed\u01fa\u0204")
        buf.write("\u020a\u020e\u0224\u023b\u023d\u0255\u025b\u025d\u0265")
        buf.write("\u0273")
        return buf.getvalue()


class RubyParser ( Parser ):

    grammarFileName = "RubyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'module'", "'def'", "'end'", 
                     "'if'", "'else'", "'elsif'", "'while'", "'do'", "'return'", 
                     "'true'", "'false'", "'nil'", "'for'", "'alias'", "'in'", 
                     "'break'", "'..'", "'private'", "'public'", "'protected'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'.'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'**='", "'not'", "'**'", "'&&'", 
                     "'||'", "'!'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "':'", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'attr_accessor'", "'attr_reader'", "'attr_writer'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "MODULE", "DEF", "END", "IF", 
                      "ELSE", "ELSIF", "WHILE", "DO", "RETURN", "TRUE", 
                      "FALSE", "NIL", "FOR", "ALIAS", "IN", "BREAK", "DOTDOT", 
                      "PRIVATE", "PUBLIC", "PROTECTED", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "ASSIGN", "EQ", "NEQ", "LT", 
                      "GT", "LE", "GE", "DOT", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "EXP_ASSIGN", 
                      "NOT", "EXP", "AND", "OR", "BANG", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "COLON", 
                      "SEMI", "INT", "FLOAT", "STRING", "INTERPOLATED_STRING", 
                      "ATTR_ACCESSOR", "ATTR_READER", "ATTR_WRITER", "ID", 
                      "INSTANCE_VAR", "ID_GLOBAL", "ID_METHOD", "LINE_COMMENT", 
                      "ML_COMMENT", "CRLF", "WS" ]

    RULE_prog = 0
    RULE_expression_list = 1
    RULE_expression = 2
    RULE_class_definition = 3
    RULE_attribute_definition = 4
    RULE_attr_type = 5
    RULE_global_get = 6
    RULE_global_set = 7
    RULE_global_result = 8
    RULE_method_inline_call = 9
    RULE_method_definition = 10
    RULE_method_definition_body = 11
    RULE_method_definition_header = 12
    RULE_method_name = 13
    RULE_method_definition_params = 14
    RULE_method_definition_params_list = 15
    RULE_method_definition_param_id = 16
    RULE_return_statement = 17
    RULE_method_call = 18
    RULE_method_call_args = 19
    RULE_method_call_param_list = 20
    RULE_method_call_params = 21
    RULE_method_param = 22
    RULE_method_unnamed_param = 23
    RULE_method_named_param = 24
    RULE_method_call_assignment = 25
    RULE_all_result = 26
    RULE_cond_expression = 27
    RULE_if_statement = 28
    RULE_elsif_clause = 29
    RULE_else_clause = 30
    RULE_while_statement = 31
    RULE_for_statement = 32
    RULE_all_assignment = 33
    RULE_statement_body = 34
    RULE_statement_expression_list = 35
    RULE_assignment = 36
    RULE_instance_variable_assignment = 37
    RULE_dynamic_assignment = 38
    RULE_initial_array_assignment = 39
    RULE_array_assignment = 40
    RULE_array_definition = 41
    RULE_array_definition_elements = 42
    RULE_array_selector = 43
    RULE_dynamic_result = 44
    RULE_dynamic_ = 45
    RULE_comparison = 46
    RULE_comp_var = 47
    RULE_lvalue = 48
    RULE_rvalue = 49
    RULE_break_expression = 50
    RULE_str_t = 51
    RULE_float_t = 52
    RULE_int_t = 53
    RULE_bool_t = 54
    RULE_nil_t = 55
    RULE_id_ = 56
    RULE_id_global = 57
    RULE_id_method = 58
    RULE_terminator = 59
    RULE_else_token = 60
    RULE_crlf = 61
    RULE_instance_var = 62
    RULE_modif = 63
    RULE_dots = 64
    RULE_primary = 65
    RULE_inpterp = 66

    ruleNames =  [ "prog", "expression_list", "expression", "class_definition", 
                   "attribute_definition", "attr_type", "global_get", "global_set", 
                   "global_result", "method_inline_call", "method_definition", 
                   "method_definition_body", "method_definition_header", 
                   "method_name", "method_definition_params", "method_definition_params_list", 
                   "method_definition_param_id", "return_statement", "method_call", 
                   "method_call_args", "method_call_param_list", "method_call_params", 
                   "method_param", "method_unnamed_param", "method_named_param", 
                   "method_call_assignment", "all_result", "cond_expression", 
                   "if_statement", "elsif_clause", "else_clause", "while_statement", 
                   "for_statement", "all_assignment", "statement_body", 
                   "statement_expression_list", "assignment", "instance_variable_assignment", 
                   "dynamic_assignment", "initial_array_assignment", "array_assignment", 
                   "array_definition", "array_definition_elements", "array_selector", 
                   "dynamic_result", "dynamic_", "comparison", "comp_var", 
                   "lvalue", "rvalue", "break_expression", "str_t", "float_t", 
                   "int_t", "bool_t", "nil_t", "id_", "id_global", "id_method", 
                   "terminator", "else_token", "crlf", "instance_var", "modif", 
                   "dots", "primary", "inpterp" ]

    EOF = Token.EOF
    CLASS=1
    MODULE=2
    DEF=3
    END=4
    IF=5
    ELSE=6
    ELSIF=7
    WHILE=8
    DO=9
    RETURN=10
    TRUE=11
    FALSE=12
    NIL=13
    FOR=14
    ALIAS=15
    IN=16
    BREAK=17
    DOTDOT=18
    PRIVATE=19
    PUBLIC=20
    PROTECTED=21
    PLUS=22
    MINUS=23
    MUL=24
    DIV=25
    MOD=26
    ASSIGN=27
    EQ=28
    NEQ=29
    LT=30
    GT=31
    LE=32
    GE=33
    DOT=34
    PLUS_ASSIGN=35
    MINUS_ASSIGN=36
    MUL_ASSIGN=37
    DIV_ASSIGN=38
    MOD_ASSIGN=39
    EXP_ASSIGN=40
    NOT=41
    EXP=42
    AND=43
    OR=44
    BANG=45
    LPAREN=46
    RPAREN=47
    LBRACE=48
    RBRACE=49
    LBRACK=50
    RBRACK=51
    COMMA=52
    COLON=53
    SEMI=54
    INT=55
    FLOAT=56
    STRING=57
    INTERPOLATED_STRING=58
    ATTR_ACCESSOR=59
    ATTR_READER=60
    ATTR_WRITER=61
    ID=62
    INSTANCE_VAR=63
    ID_GLOBAL=64
    ID_METHOD=65
    LINE_COMMENT=66
    ML_COMMENT=67
    CRLF=68
    WS=69

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def EOF(self):
            return self.getToken(RubyParser.EOF, 0)

        def terminator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.TerminatorContext)
            else:
                return self.getTypedRuleContext(RubyParser.TerminatorContext,i)


        def getRuleIndex(self):
            return RubyParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = RubyParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RubyParser.SEMI or _la==RubyParser.CRLF:
                self.state = 134
                self.terminator(0)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.expression_list()
            self.state = 141
            self.match(RubyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RubyParser.ExpressionContext,i)


        def terminator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.TerminatorContext)
            else:
                return self.getTypedRuleContext(RubyParser.TerminatorContext,i)


        def getRuleIndex(self):
            return RubyParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = RubyParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.expression()
                self.state = 144
                self.terminator(0)
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.CLASS) | (1 << RubyParser.DEF) | (1 << RubyParser.IF) | (1 << RubyParser.WHILE) | (1 << RubyParser.RETURN) | (1 << RubyParser.TRUE) | (1 << RubyParser.FALSE) | (1 << RubyParser.NIL) | (1 << RubyParser.FOR) | (1 << RubyParser.PRIVATE) | (1 << RubyParser.PUBLIC) | (1 << RubyParser.PROTECTED) | (1 << RubyParser.NOT) | (1 << RubyParser.BANG) | (1 << RubyParser.LPAREN) | (1 << RubyParser.INT) | (1 << RubyParser.FLOAT) | (1 << RubyParser.STRING) | (1 << RubyParser.INTERPOLATED_STRING) | (1 << RubyParser.ID) | (1 << RubyParser.INSTANCE_VAR))) != 0) or _la==RubyParser.ID_GLOBAL or _la==RubyParser.ID_METHOD):
                    break

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RubyParser.SEMI or _la==RubyParser.CRLF:
                self.state = 150
                self.terminator(0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_definition(self):
            return self.getTypedRuleContext(RubyParser.Class_definitionContext,0)


        def method_definition(self):
            return self.getTypedRuleContext(RubyParser.Method_definitionContext,0)


        def method_inline_call(self):
            return self.getTypedRuleContext(RubyParser.Method_inline_callContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(RubyParser.If_statementContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(RubyParser.RvalueContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(RubyParser.Return_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(RubyParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(RubyParser.For_statementContext,0)


        def instance_variable_assignment(self):
            return self.getTypedRuleContext(RubyParser.Instance_variable_assignmentContext,0)


        def assignment(self):
            return self.getTypedRuleContext(RubyParser.AssignmentContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = RubyParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.class_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.method_definition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.method_inline_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.rvalue(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 161
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 162
                self.while_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 163
                self.for_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 164
                self.instance_variable_assignment()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 165
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.klasa = None # Id_Context
            self.nadklasa = None # Id_Context

        def CLASS(self):
            return self.getToken(RubyParser.CLASS, 0)

        def END(self):
            return self.getToken(RubyParser.END, 0)

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Id_Context)
            else:
                return self.getTypedRuleContext(RubyParser.Id_Context,i)


        def LT(self):
            return self.getToken(RubyParser.LT, 0)

        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def attribute_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Attribute_definitionContext)
            else:
                return self.getTypedRuleContext(RubyParser.Attribute_definitionContext,i)


        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_class_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_definition" ):
                listener.enterClass_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_definition" ):
                listener.exitClass_definition(self)




    def class_definition(self):

        localctx = RubyParser.Class_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RubyParser.CLASS)
            self.state = 169
            localctx.klasa = self.id_()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RubyParser.LT:
                self.state = 170
                self.match(RubyParser.LT)
                self.state = 171
                localctx.nadklasa = self.id_()


            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RubyParser.CRLF:
                self.state = 174
                self.crlf()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.ATTR_ACCESSOR) | (1 << RubyParser.ATTR_READER) | (1 << RubyParser.ATTR_WRITER))) != 0):
                self.state = 180
                self.attribute_definition()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.CLASS) | (1 << RubyParser.DEF) | (1 << RubyParser.IF) | (1 << RubyParser.WHILE) | (1 << RubyParser.RETURN) | (1 << RubyParser.TRUE) | (1 << RubyParser.FALSE) | (1 << RubyParser.NIL) | (1 << RubyParser.FOR) | (1 << RubyParser.PRIVATE) | (1 << RubyParser.PUBLIC) | (1 << RubyParser.PROTECTED) | (1 << RubyParser.NOT) | (1 << RubyParser.BANG) | (1 << RubyParser.LPAREN) | (1 << RubyParser.INT) | (1 << RubyParser.FLOAT) | (1 << RubyParser.STRING) | (1 << RubyParser.INTERPOLATED_STRING) | (1 << RubyParser.ID) | (1 << RubyParser.INSTANCE_VAR))) != 0) or _la==RubyParser.ID_GLOBAL or _la==RubyParser.ID_METHOD:
                self.state = 186
                self.expression_list()


            self.state = 189
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_type(self):
            return self.getTypedRuleContext(RubyParser.Attr_typeContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.COLON)
            else:
                return self.getToken(RubyParser.COLON, i)

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Id_Context)
            else:
                return self.getTypedRuleContext(RubyParser.Id_Context,i)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.COMMA)
            else:
                return self.getToken(RubyParser.COMMA, i)

        def getRuleIndex(self):
            return RubyParser.RULE_attribute_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_definition" ):
                listener.enterAttribute_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_definition" ):
                listener.exitAttribute_definition(self)




    def attribute_definition(self):

        localctx = RubyParser.Attribute_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.attr_type()
            self.state = 192
            self.match(RubyParser.COLON)
            self.state = 193
            self.id_()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RubyParser.COMMA:
                self.state = 194
                self.match(RubyParser.COMMA)
                self.state = 195
                self.match(RubyParser.COLON)
                self.state = 196
                self.id_()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.crlf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR_ACCESSOR(self):
            return self.getToken(RubyParser.ATTR_ACCESSOR, 0)

        def ATTR_READER(self):
            return self.getToken(RubyParser.ATTR_READER, 0)

        def ATTR_WRITER(self):
            return self.getToken(RubyParser.ATTR_WRITER, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_attr_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_type" ):
                listener.enterAttr_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_type" ):
                listener.exitAttr_type(self)




    def attr_type(self):

        localctx = RubyParser.Attr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.ATTR_ACCESSOR) | (1 << RubyParser.ATTR_READER) | (1 << RubyParser.ATTR_WRITER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Global_getContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_name = None # LvalueContext
            self.op = None # Token
            self.global_name = None # Id_globalContext

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_global_get

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_get" ):
                listener.enterGlobal_get(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_get" ):
                listener.exitGlobal_get(self)




    def global_get(self):

        localctx = RubyParser.Global_getContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_global_get)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            localctx.var_name = self.lvalue()
            self.state = 207
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 208
            localctx.global_name = self.id_global()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Global_setContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.global_name = None # Id_globalContext
            self.op = None # Token
            self.result = None # All_resultContext

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def all_result(self):
            return self.getTypedRuleContext(RubyParser.All_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_global_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_set" ):
                listener.enterGlobal_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_set" ):
                listener.exitGlobal_set(self)




    def global_set(self):

        localctx = RubyParser.Global_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_global_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            localctx.global_name = self.id_global()
            self.state = 211
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 212
            localctx.result = self.all_result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Global_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_global_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_result" ):
                listener.enterGlobal_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_result" ):
                listener.exitGlobal_result(self)




    def global_result(self):

        localctx = RubyParser.Global_resultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_global_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.id_global()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_inline_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_call(self):
            return self.getTypedRuleContext(RubyParser.Method_callContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_inline_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_inline_call" ):
                listener.enterMethod_inline_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_inline_call" ):
                listener.exitMethod_inline_call(self)




    def method_inline_call(self):

        localctx = RubyParser.Method_inline_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_inline_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.method_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.m = None # ModifContext

        def method_definition_header(self):
            return self.getTypedRuleContext(RubyParser.Method_definition_headerContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def method_definition_body(self):
            return self.getTypedRuleContext(RubyParser.Method_definition_bodyContext,0)


        def modif(self):
            return self.getTypedRuleContext(RubyParser.ModifContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition" ):
                listener.enterMethod_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition" ):
                listener.exitMethod_definition(self)




    def method_definition(self):

        localctx = RubyParser.Method_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PRIVATE) | (1 << RubyParser.PUBLIC) | (1 << RubyParser.PROTECTED))) != 0):
                self.state = 218
                localctx.m = self.modif()
                self.state = 219
                self.crlf()


            self.state = 223
            self.method_definition_header()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.CLASS) | (1 << RubyParser.DEF) | (1 << RubyParser.IF) | (1 << RubyParser.WHILE) | (1 << RubyParser.RETURN) | (1 << RubyParser.TRUE) | (1 << RubyParser.FALSE) | (1 << RubyParser.NIL) | (1 << RubyParser.FOR) | (1 << RubyParser.PRIVATE) | (1 << RubyParser.PUBLIC) | (1 << RubyParser.PROTECTED) | (1 << RubyParser.NOT) | (1 << RubyParser.BANG) | (1 << RubyParser.LPAREN) | (1 << RubyParser.INT) | (1 << RubyParser.FLOAT) | (1 << RubyParser.STRING) | (1 << RubyParser.INTERPOLATED_STRING) | (1 << RubyParser.ID) | (1 << RubyParser.INSTANCE_VAR))) != 0) or _la==RubyParser.ID_GLOBAL or _la==RubyParser.ID_METHOD:
                self.state = 224
                self.method_definition_body()


            self.state = 227
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_definition_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_definition_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition_body" ):
                listener.enterMethod_definition_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition_body" ):
                listener.exitMethod_definition_body(self)




    def method_definition_body(self):

        localctx = RubyParser.Method_definition_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_definition_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_definition_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(RubyParser.DEF, 0)

        def method_name(self):
            return self.getTypedRuleContext(RubyParser.Method_nameContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def method_definition_params(self):
            return self.getTypedRuleContext(RubyParser.Method_definition_paramsContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_definition_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition_header" ):
                listener.enterMethod_definition_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition_header" ):
                listener.exitMethod_definition_header(self)




    def method_definition_header(self):

        localctx = RubyParser.Method_definition_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_definition_header)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(RubyParser.DEF)
                self.state = 232
                self.method_name()
                self.state = 233
                self.crlf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(RubyParser.DEF)
                self.state = 236
                self.method_name()
                self.state = 237
                self.method_definition_params()
                self.state = 238
                self.crlf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_method(self):
            return self.getTypedRuleContext(RubyParser.Id_methodContext,0)


        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_name" ):
                listener.enterMethod_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_name" ):
                listener.exitMethod_name(self)




    def method_name(self):

        localctx = RubyParser.Method_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_name)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.ID_METHOD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.id_method()
                pass
            elif token in [RubyParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_definition_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(RubyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RubyParser.RPAREN, 0)

        def method_definition_params_list(self):
            return self.getTypedRuleContext(RubyParser.Method_definition_params_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_definition_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition_params" ):
                listener.enterMethod_definition_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition_params" ):
                listener.exitMethod_definition_params(self)




    def method_definition_params(self):

        localctx = RubyParser.Method_definition_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method_definition_params)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(RubyParser.LPAREN)
                self.state = 247
                self.match(RubyParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(RubyParser.LPAREN)
                self.state = 249
                self.method_definition_params_list(0)
                self.state = 250
                self.match(RubyParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.method_definition_params_list(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_definition_params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_definition_param_id(self):
            return self.getTypedRuleContext(RubyParser.Method_definition_param_idContext,0)


        def method_definition_params_list(self):
            return self.getTypedRuleContext(RubyParser.Method_definition_params_listContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_method_definition_params_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition_params_list" ):
                listener.enterMethod_definition_params_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition_params_list" ):
                listener.exitMethod_definition_params_list(self)



    def method_definition_params_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Method_definition_params_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_method_definition_params_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.method_definition_param_id()
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Method_definition_params_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_method_definition_params_list)
                    self.state = 258
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 259
                    self.match(RubyParser.COMMA)
                    self.state = 260
                    self.method_definition_param_id() 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_definition_param_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_definition_param_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_definition_param_id" ):
                listener.enterMethod_definition_param_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_definition_param_id" ):
                listener.exitMethod_definition_param_id(self)




    def method_definition_param_id(self):

        localctx = RubyParser.Method_definition_param_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_definition_param_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(RubyParser.RETURN, 0)

        def all_result(self):
            return self.getTypedRuleContext(RubyParser.All_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = RubyParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(RubyParser.RETURN)
            self.state = 269
            self.all_result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(RubyParser.PrimaryContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.DOT)
            else:
                return self.getToken(RubyParser.DOT, i)

        def method_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Method_nameContext)
            else:
                return self.getTypedRuleContext(RubyParser.Method_nameContext,i)


        def method_call_param_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Method_call_param_listContext)
            else:
                return self.getTypedRuleContext(RubyParser.Method_call_param_listContext,i)


        def method_call_args(self):
            return self.getTypedRuleContext(RubyParser.Method_call_argsContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call" ):
                listener.enterMethod_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call" ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = RubyParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_method_call)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.primary()
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 272
                        self.match(RubyParser.DOT)
                        self.state = 273
                        self.method_name()
                        self.state = 275
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                        if la_ == 1:
                            self.state = 274
                            self.method_call_param_list()

                 
                    self.state = 281
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.method_name()
                self.state = 284
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 283
                    self.method_call_param_list()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.method_name()
                self.state = 287
                self.method_call_args()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Method_paramContext)
            else:
                return self.getTypedRuleContext(RubyParser.Method_paramContext,i)


        def getRuleIndex(self):
            return RubyParser.RULE_method_call_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call_args" ):
                listener.enterMethod_call_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call_args" ):
                listener.exitMethod_call_args(self)




    def method_call_args(self):

        localctx = RubyParser.Method_call_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_method_call_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 291
                    self.method_param()

                else:
                    raise NoViableAltException(self)
                self.state = 294 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(RubyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RubyParser.RPAREN, 0)

        def method_call_params(self):
            return self.getTypedRuleContext(RubyParser.Method_call_paramsContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_call_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call_param_list" ):
                listener.enterMethod_call_param_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call_param_list" ):
                listener.exitMethod_call_param_list(self)




    def method_call_param_list(self):

        localctx = RubyParser.Method_call_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_method_call_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(RubyParser.LPAREN)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & ((1 << (RubyParser.TRUE - 11)) | (1 << (RubyParser.FALSE - 11)) | (1 << (RubyParser.NIL - 11)) | (1 << (RubyParser.LPAREN - 11)) | (1 << (RubyParser.INT - 11)) | (1 << (RubyParser.FLOAT - 11)) | (1 << (RubyParser.STRING - 11)) | (1 << (RubyParser.INTERPOLATED_STRING - 11)) | (1 << (RubyParser.ID - 11)) | (1 << (RubyParser.INSTANCE_VAR - 11)) | (1 << (RubyParser.ID_GLOBAL - 11)) | (1 << (RubyParser.ID_METHOD - 11)))) != 0):
                self.state = 297
                self.method_call_params(0)


            self.state = 300
            self.match(RubyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_param(self):
            return self.getTypedRuleContext(RubyParser.Method_paramContext,0)


        def method_call_params(self):
            return self.getTypedRuleContext(RubyParser.Method_call_paramsContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_method_call_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call_params" ):
                listener.enterMethod_call_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call_params" ):
                listener.exitMethod_call_params(self)



    def method_call_params(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Method_call_paramsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_method_call_params, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.method_param()
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Method_call_paramsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_method_call_params)
                    self.state = 305
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 306
                    self.match(RubyParser.COMMA)
                    self.state = 307
                    self.method_param() 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_unnamed_param(self):
            return self.getTypedRuleContext(RubyParser.Method_unnamed_paramContext,0)


        def method_named_param(self):
            return self.getTypedRuleContext(RubyParser.Method_named_paramContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_param" ):
                listener.enterMethod_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_param" ):
                listener.exitMethod_param(self)




    def method_param(self):

        localctx = RubyParser.Method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_param)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.method_unnamed_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.method_named_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_unnamed_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_unnamed_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_unnamed_param" ):
                listener.enterMethod_unnamed_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_unnamed_param" ):
                listener.exitMethod_unnamed_param(self)




    def method_unnamed_param(self):

        localctx = RubyParser.Method_unnamed_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_unnamed_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.dynamic_result(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_named_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def COLON(self):
            return self.getToken(RubyParser.COLON, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_method_named_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_named_param" ):
                listener.enterMethod_named_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_named_param" ):
                listener.exitMethod_named_param(self)




    def method_named_param(self):

        localctx = RubyParser.Method_named_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_named_param)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.id_()
                self.state = 320
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 321
                self.dynamic_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.id_()
                self.state = 324
                self.match(RubyParser.COLON)
                self.state = 325
                self.dynamic_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_call_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_call(self):
            return self.getTypedRuleContext(RubyParser.Method_callContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_method_call_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call_assignment" ):
                listener.enterMethod_call_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call_assignment" ):
                listener.exitMethod_call_assignment(self)




    def method_call_assignment(self):

        localctx = RubyParser.Method_call_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_call_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.method_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class All_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def global_result(self):
            return self.getTypedRuleContext(RubyParser.Global_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_all_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_result" ):
                listener.enterAll_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_result" ):
                listener.exitAll_result(self)




    def all_result(self):

        localctx = RubyParser.All_resultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_all_result)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.dynamic_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.global_result()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cond_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(RubyParser.ComparisonContext,0)


        def bool_t(self):
            return self.getTypedRuleContext(RubyParser.Bool_tContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_cond_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_expression" ):
                listener.enterCond_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_expression" ):
                listener.exitCond_expression(self)




    def cond_expression(self):

        localctx = RubyParser.Cond_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_cond_expression)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.comparison()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.bool_t()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RubyParser.IF, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def elsif_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Elsif_clauseContext)
            else:
                return self.getTypedRuleContext(RubyParser.Elsif_clauseContext,i)


        def else_clause(self):
            return self.getTypedRuleContext(RubyParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = RubyParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(RubyParser.IF)
            self.state = 340
            self.cond_expression()
            self.state = 341
            self.crlf()
            self.state = 342
            self.statement_body()
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RubyParser.ELSIF:
                self.state = 343
                self.elsif_clause()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RubyParser.ELSE:
                self.state = 349
                self.else_clause()


            self.state = 352
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Elsif_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSIF(self):
            return self.getToken(RubyParser.ELSIF, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_elsif_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsif_clause" ):
                listener.enterElsif_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsif_clause" ):
                listener.exitElsif_clause(self)




    def elsif_clause(self):

        localctx = RubyParser.Elsif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elsif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(RubyParser.ELSIF)
            self.state = 355
            self.cond_expression()
            self.state = 356
            self.crlf()
            self.state = 357
            self.statement_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_token(self):
            return self.getTypedRuleContext(RubyParser.Else_tokenContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_else_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_clause" ):
                listener.enterElse_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_clause" ):
                listener.exitElse_clause(self)




    def else_clause(self):

        localctx = RubyParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.else_token()
            self.state = 360
            self.crlf()
            self.state = 361
            self.statement_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(RubyParser.WHILE, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = RubyParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(RubyParser.WHILE)
            self.state = 364
            self.cond_expression()
            self.state = 365
            self.crlf()
            self.state = 366
            self.statement_body()
            self.state = 367
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(RubyParser.FOR, 0)

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def IN(self):
            return self.getToken(RubyParser.IN, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def int_t(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Int_tContext)
            else:
                return self.getTypedRuleContext(RubyParser.Int_tContext,i)


        def dots(self):
            return self.getTypedRuleContext(RubyParser.DotsContext,0)


        def dynamic_(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_Context,0)


        def getRuleIndex(self):
            return RubyParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = RubyParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(RubyParser.FOR)
            self.state = 370
            self.id_()
            self.state = 371
            self.match(RubyParser.IN)
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 372
                self.int_t()
                self.state = 373
                self.dots()
                self.state = 374
                self.int_t()
                pass

            elif la_ == 2:
                self.state = 376
                self.dynamic_()
                pass


            self.state = 379
            self.crlf()
            self.state = 380
            self.statement_body()
            self.state = 381
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class All_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamic_assignment(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_assignmentContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_all_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_assignment" ):
                listener.enterAll_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_assignment" ):
                listener.exitAll_assignment(self)




    def all_assignment(self):

        localctx = RubyParser.All_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_all_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.dynamic_assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_expression_list(self):
            return self.getTypedRuleContext(RubyParser.Statement_expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_statement_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_body" ):
                listener.enterStatement_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_body" ):
                listener.exitStatement_body(self)




    def statement_body(self):

        localctx = RubyParser.Statement_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_statement_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.statement_expression_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RubyParser.ExpressionContext,0)


        def terminator(self):
            return self.getTypedRuleContext(RubyParser.TerminatorContext,0)


        def break_expression(self):
            return self.getTypedRuleContext(RubyParser.Break_expressionContext,0)


        def statement_expression_list(self):
            return self.getTypedRuleContext(RubyParser.Statement_expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_statement_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_expression_list" ):
                listener.enterStatement_expression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_expression_list" ):
                listener.exitStatement_expression_list(self)



    def statement_expression_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Statement_expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_statement_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.CLASS, RubyParser.DEF, RubyParser.IF, RubyParser.WHILE, RubyParser.RETURN, RubyParser.TRUE, RubyParser.FALSE, RubyParser.NIL, RubyParser.FOR, RubyParser.PRIVATE, RubyParser.PUBLIC, RubyParser.PROTECTED, RubyParser.NOT, RubyParser.BANG, RubyParser.LPAREN, RubyParser.INT, RubyParser.FLOAT, RubyParser.STRING, RubyParser.INTERPOLATED_STRING, RubyParser.ID, RubyParser.INSTANCE_VAR, RubyParser.ID_GLOBAL, RubyParser.ID_METHOD]:
                self.state = 388
                self.expression()
                self.state = 389
                self.terminator(0)
                pass
            elif token in [RubyParser.BREAK]:
                self.state = 391
                self.break_expression()
                self.state = 392
                self.terminator(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 404
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.Statement_expression_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_expression_list)
                        self.state = 396
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 397
                        self.expression()
                        self.state = 398
                        self.terminator(0)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.Statement_expression_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_expression_list)
                        self.state = 400
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 401
                        self.break_expression()
                        self.state = 402
                        self.terminator(0)
                        pass

             
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(RubyParser.RvalueContext,0)


        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = RubyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.lvalue()
                self.state = 410
                self.match(RubyParser.ASSIGN)
                self.state = 411
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                localctx.var_id = self.lvalue()
                self.state = 414
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 415
                self.rvalue(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_variable_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # RvalueContext
            self.var_id = None # Instance_varContext
            self.op = None # Token

        def instance_var(self):
            return self.getTypedRuleContext(RubyParser.Instance_varContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def rvalue(self):
            return self.getTypedRuleContext(RubyParser.RvalueContext,0)


        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_instance_variable_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_variable_assignment" ):
                listener.enterInstance_variable_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_variable_assignment" ):
                listener.exitInstance_variable_assignment(self)




    def instance_variable_assignment(self):

        localctx = RubyParser.Instance_variable_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_instance_variable_assignment)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.instance_var()
                self.state = 420
                self.match(RubyParser.ASSIGN)
                self.state = 421
                localctx.value = self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                localctx.var_id = self.instance_var()
                self.state = 424
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 425
                self.rvalue(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dynamic_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_dynamic_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_assignment" ):
                listener.enterDynamic_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_assignment" ):
                listener.exitDynamic_assignment(self)




    def dynamic_assignment(self):

        localctx = RubyParser.Dynamic_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_dynamic_assignment)
        self._la = 0 # Token type
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                localctx.var_id = self.lvalue()
                self.state = 430
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 431
                self.dynamic_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                localctx.var_id = self.lvalue()
                self.state = 434
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 435
                self.dynamic_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Initial_array_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def LBRACK(self):
            return self.getToken(RubyParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(RubyParser.RBRACK, 0)

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_initial_array_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitial_array_assignment" ):
                listener.enterInitial_array_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitial_array_assignment" ):
                listener.exitInitial_array_assignment(self)




    def initial_array_assignment(self):

        localctx = RubyParser.Initial_array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_initial_array_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            localctx.var_id = self.lvalue()
            self.state = 440
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 441
            self.match(RubyParser.LBRACK)
            self.state = 442
            self.match(RubyParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.arr_def = None # Array_selectorContext
            self.op = None # Token
            self.arr_val = None # Dynamic_resultContext

        def array_selector(self):
            return self.getTypedRuleContext(RubyParser.Array_selectorContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_array_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_assignment" ):
                listener.enterArray_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_assignment" ):
                listener.exitArray_assignment(self)




    def array_assignment(self):

        localctx = RubyParser.Array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            localctx.arr_def = self.array_selector()
            self.state = 445
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 446
            localctx.arr_val = self.dynamic_result(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(RubyParser.LBRACK, 0)

        def array_definition_elements(self):
            return self.getTypedRuleContext(RubyParser.Array_definition_elementsContext,0)


        def RBRACK(self):
            return self.getToken(RubyParser.RBRACK, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_array_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_definition" ):
                listener.enterArray_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_definition" ):
                listener.exitArray_definition(self)




    def array_definition(self):

        localctx = RubyParser.Array_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(RubyParser.LBRACK)
            self.state = 449
            self.array_definition_elements(0)
            self.state = 450
            self.match(RubyParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_definition_elementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def array_definition_elements(self):
            return self.getTypedRuleContext(RubyParser.Array_definition_elementsContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_array_definition_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_definition_elements" ):
                listener.enterArray_definition_elements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_definition_elements" ):
                listener.exitArray_definition_elements(self)



    def array_definition_elements(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Array_definition_elementsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_array_definition_elements, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.dynamic_result(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 460
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Array_definition_elementsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_definition_elements)
                    self.state = 455
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 456
                    self.match(RubyParser.COMMA)
                    self.state = 457
                    self.dynamic_result(0) 
                self.state = 462
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Array_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def LBRACK(self):
            return self.getToken(RubyParser.LBRACK, 0)

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def RBRACK(self):
            return self.getToken(RubyParser.RBRACK, 0)

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_array_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_selector" ):
                listener.enterArray_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_selector" ):
                listener.exitArray_selector(self)




    def array_selector(self):

        localctx = RubyParser.Array_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_selector)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.id_()
                self.state = 464
                self.match(RubyParser.LBRACK)
                self.state = 465
                self.dynamic_result(0)
                self.state = 466
                self.match(RubyParser.RBRACK)
                pass
            elif token in [RubyParser.ID_GLOBAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.id_global()
                self.state = 469
                self.match(RubyParser.LBRACK)
                self.state = 470
                self.dynamic_result(0)
                self.state = 471
                self.match(RubyParser.RBRACK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dynamic_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def LPAREN(self):
            return self.getToken(RubyParser.LPAREN, 0)

        def dynamic_result(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Dynamic_resultContext)
            else:
                return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,i)


        def RPAREN(self):
            return self.getToken(RubyParser.RPAREN, 0)

        def dynamic_(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_Context,0)


        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIV(self):
            return self.getToken(RubyParser.DIV, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_dynamic_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_result" ):
                listener.enterDynamic_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_result" ):
                listener.exitDynamic_result(self)



    def dynamic_result(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Dynamic_resultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_dynamic_result, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 476
                self.match(RubyParser.LPAREN)
                self.state = 477
                self.dynamic_result(0)
                self.state = 478
                self.match(RubyParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 480
                self.dynamic_()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 489
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 483
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 484
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 485
                        self.dynamic_result(5)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 486
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 487
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 488
                        self.dynamic_result(4)
                        pass

             
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dynamic_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def int_t(self):
            return self.getTypedRuleContext(RubyParser.Int_tContext,0)


        def float_t(self):
            return self.getTypedRuleContext(RubyParser.Float_tContext,0)


        def str_t(self):
            return self.getTypedRuleContext(RubyParser.Str_tContext,0)


        def inpterp(self):
            return self.getTypedRuleContext(RubyParser.InpterpContext,0)


        def bool_t(self):
            return self.getTypedRuleContext(RubyParser.Bool_tContext,0)


        def nil_t(self):
            return self.getTypedRuleContext(RubyParser.Nil_tContext,0)


        def method_call(self):
            return self.getTypedRuleContext(RubyParser.Method_callContext,0)


        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def array_selector(self):
            return self.getTypedRuleContext(RubyParser.Array_selectorContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_dynamic_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_" ):
                listener.enterDynamic_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_" ):
                listener.exitDynamic_(self)




    def dynamic_(self):

        localctx = RubyParser.Dynamic_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_dynamic_)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.id_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.int_t()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.float_t()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 497
                self.str_t()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 498
                self.inpterp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 499
                self.bool_t()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 500
                self.nil_t()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 501
                self.method_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 502
                self.id_global()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 503
                self.array_selector()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Comp_varContext
            self.op = None # Token
            self.right = None # Comp_varContext

        def comp_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Comp_varContext)
            else:
                return self.getTypedRuleContext(RubyParser.Comp_varContext,i)


        def LT(self):
            return self.getToken(RubyParser.LT, 0)

        def GT(self):
            return self.getToken(RubyParser.GT, 0)

        def LE(self):
            return self.getToken(RubyParser.LE, 0)

        def GE(self):
            return self.getToken(RubyParser.GE, 0)

        def EQ(self):
            return self.getToken(RubyParser.EQ, 0)

        def NEQ(self):
            return self.getToken(RubyParser.NEQ, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = RubyParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                localctx.left = self.comp_var()
                self.state = 507
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.LT) | (1 << RubyParser.GT) | (1 << RubyParser.LE) | (1 << RubyParser.GE))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 508
                localctx.right = self.comp_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                localctx.left = self.comp_var()
                self.state = 511
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RubyParser.EQ or _la==RubyParser.NEQ):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 512
                localctx.right = self.comp_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def array_selector(self):
            return self.getTypedRuleContext(RubyParser.Array_selectorContext,0)


        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def instance_var(self):
            return self.getTypedRuleContext(RubyParser.Instance_varContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_comp_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_var" ):
                listener.enterComp_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_var" ):
                listener.exitComp_var(self)




    def comp_var(self):

        localctx = RubyParser.Comp_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_comp_var)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.dynamic_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.array_selector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.id_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.instance_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def instance_var(self):
            return self.getTypedRuleContext(RubyParser.Instance_varContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = RubyParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_lvalue)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.id_()
                pass
            elif token in [RubyParser.INSTANCE_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.instance_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def initial_array_assignment(self):
            return self.getTypedRuleContext(RubyParser.Initial_array_assignmentContext,0)


        def array_assignment(self):
            return self.getTypedRuleContext(RubyParser.Array_assignmentContext,0)


        def dynamic_assignment(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_assignmentContext,0)


        def assignment(self):
            return self.getTypedRuleContext(RubyParser.AssignmentContext,0)


        def method_call(self):
            return self.getTypedRuleContext(RubyParser.Method_callContext,0)


        def bool_t(self):
            return self.getTypedRuleContext(RubyParser.Bool_tContext,0)


        def float_t(self):
            return self.getTypedRuleContext(RubyParser.Float_tContext,0)


        def int_t(self):
            return self.getTypedRuleContext(RubyParser.Int_tContext,0)


        def nil_t(self):
            return self.getTypedRuleContext(RubyParser.Nil_tContext,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def NOT(self):
            return self.getToken(RubyParser.NOT, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.RvalueContext)
            else:
                return self.getTypedRuleContext(RubyParser.RvalueContext,i)


        def BANG(self):
            return self.getToken(RubyParser.BANG, 0)

        def LPAREN(self):
            return self.getToken(RubyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RubyParser.RPAREN, 0)

        def EXP(self):
            return self.getToken(RubyParser.EXP, 0)

        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIV(self):
            return self.getToken(RubyParser.DIV, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def LT(self):
            return self.getToken(RubyParser.LT, 0)

        def GT(self):
            return self.getToken(RubyParser.GT, 0)

        def LE(self):
            return self.getToken(RubyParser.LE, 0)

        def GE(self):
            return self.getToken(RubyParser.GE, 0)

        def EQ(self):
            return self.getToken(RubyParser.EQ, 0)

        def NEQ(self):
            return self.getToken(RubyParser.NEQ, 0)

        def AND(self):
            return self.getToken(RubyParser.AND, 0)

        def OR(self):
            return self.getToken(RubyParser.OR, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)



    def rvalue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.RvalueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_rvalue, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 527
                self.lvalue()
                pass

            elif la_ == 2:
                self.state = 528
                self.initial_array_assignment()
                pass

            elif la_ == 3:
                self.state = 529
                self.array_assignment()
                pass

            elif la_ == 4:
                self.state = 530
                self.dynamic_assignment()
                pass

            elif la_ == 5:
                self.state = 531
                self.assignment()
                pass

            elif la_ == 6:
                self.state = 532
                self.method_call()
                pass

            elif la_ == 7:
                self.state = 533
                self.bool_t()
                pass

            elif la_ == 8:
                self.state = 534
                self.float_t()
                pass

            elif la_ == 9:
                self.state = 535
                self.int_t()
                pass

            elif la_ == 10:
                self.state = 536
                self.nil_t()
                pass

            elif la_ == 11:
                self.state = 537
                self.dynamic_result(0)
                pass

            elif la_ == 12:
                self.state = 538
                self.match(RubyParser.NOT)
                self.state = 539
                self.rvalue(9)
                pass

            elif la_ == 13:
                self.state = 540
                self.match(RubyParser.BANG)
                self.state = 541
                self.rvalue(2)
                pass

            elif la_ == 14:
                self.state = 542
                self.match(RubyParser.LPAREN)
                self.state = 543
                self.rvalue(0)
                self.state = 544
                self.match(RubyParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 571
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 569
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 548
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 549
                        self.match(RubyParser.EXP)
                        self.state = 550
                        self.rvalue(11)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 551
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 552
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 553
                        self.rvalue(9)
                        pass

                    elif la_ == 3:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 554
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 555
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 556
                        self.rvalue(8)
                        pass

                    elif la_ == 4:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 557
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 558
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.LT) | (1 << RubyParser.GT) | (1 << RubyParser.LE) | (1 << RubyParser.GE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 559
                        self.rvalue(7)
                        pass

                    elif la_ == 5:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 560
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 561
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.EQ or _la==RubyParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 562
                        self.rvalue(6)
                        pass

                    elif la_ == 6:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 563
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 564
                        self.match(RubyParser.AND)
                        self.state = 565
                        self.rvalue(5)
                        pass

                    elif la_ == 7:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 566
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 567
                        self.match(RubyParser.OR)
                        self.state = 568
                        self.rvalue(4)
                        pass

             
                self.state = 573
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Break_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(RubyParser.BREAK, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_break_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_expression" ):
                listener.enterBreak_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_expression" ):
                listener.exitBreak_expression(self)




    def break_expression(self):

        localctx = RubyParser.Break_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_break_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(RubyParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Str_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RubyParser.STRING, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_str_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_t" ):
                listener.enterStr_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_t" ):
                listener.exitStr_t(self)




    def str_t(self):

        localctx = RubyParser.Str_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_str_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(RubyParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Float_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(RubyParser.FLOAT, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_float_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_t" ):
                listener.enterFloat_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_t" ):
                listener.exitFloat_t(self)




    def float_t(self):

        localctx = RubyParser.Float_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_float_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(RubyParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Int_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RubyParser.INT, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_int_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_t" ):
                listener.enterInt_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_t" ):
                listener.exitInt_t(self)




    def int_t(self):

        localctx = RubyParser.Int_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_int_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(RubyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bool_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RubyParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RubyParser.FALSE, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_bool_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_t" ):
                listener.enterBool_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_t" ):
                listener.exitBool_t(self)




    def bool_t(self):

        localctx = RubyParser.Bool_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_bool_t)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            _la = self._input.LA(1)
            if not(_la==RubyParser.TRUE or _la==RubyParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Nil_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(RubyParser.NIL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_nil_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNil_t" ):
                listener.enterNil_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNil_t" ):
                listener.exitNil_t(self)




    def nil_t(self):

        localctx = RubyParser.Nil_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_nil_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(RubyParser.NIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_id_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_" ):
                listener.enterId_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_" ):
                listener.exitId_(self)




    def id_(self):

        localctx = RubyParser.Id_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_id_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(RubyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_globalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_GLOBAL(self):
            return self.getToken(RubyParser.ID_GLOBAL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_id_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_global" ):
                listener.enterId_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_global" ):
                listener.exitId_global(self)




    def id_global(self):

        localctx = RubyParser.Id_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_id_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(RubyParser.ID_GLOBAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_METHOD(self):
            return self.getToken(RubyParser.ID_METHOD, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_id_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_method" ):
                listener.enterId_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_method" ):
                listener.exitId_method(self)




    def id_method(self):

        localctx = RubyParser.Id_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_id_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.match(RubyParser.ID_METHOD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(RubyParser.SEMI, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def terminator(self):
            return self.getTypedRuleContext(RubyParser.TerminatorContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_terminator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminator" ):
                listener.enterTerminator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminator" ):
                listener.exitTerminator(self)



    def terminator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.TerminatorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_terminator, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.SEMI]:
                self.state = 593
                self.match(RubyParser.SEMI)
                pass
            elif token in [RubyParser.CRLF]:
                self.state = 594
                self.crlf()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 603
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 601
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.TerminatorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terminator)
                        self.state = 597
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 598
                        self.match(RubyParser.SEMI)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.TerminatorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terminator)
                        self.state = 599
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 600
                        self.crlf()
                        pass

             
                self.state = 605
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Else_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(RubyParser.ELSE, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_else_token

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_token" ):
                listener.enterElse_token(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_token" ):
                listener.exitElse_token(self)




    def else_token(self):

        localctx = RubyParser.Else_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_else_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(RubyParser.ELSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CrlfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRLF(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.CRLF)
            else:
                return self.getToken(RubyParser.CRLF, i)

        def getRuleIndex(self):
            return RubyParser.RULE_crlf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrlf" ):
                listener.enterCrlf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrlf" ):
                listener.exitCrlf(self)




    def crlf(self):

        localctx = RubyParser.CrlfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_crlf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 608
                    self.match(RubyParser.CRLF)

                else:
                    raise NoViableAltException(self)
                self.state = 611 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANCE_VAR(self):
            return self.getToken(RubyParser.INSTANCE_VAR, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_instance_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_var" ):
                listener.enterInstance_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_var" ):
                listener.exitInstance_var(self)




    def instance_var(self):

        localctx = RubyParser.Instance_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_instance_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.match(RubyParser.INSTANCE_VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIVATE(self):
            return self.getToken(RubyParser.PRIVATE, 0)

        def PUBLIC(self):
            return self.getToken(RubyParser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(RubyParser.PROTECTED, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_modif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModif" ):
                listener.enterModif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModif" ):
                listener.exitModif(self)




    def modif(self):

        localctx = RubyParser.ModifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_modif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PRIVATE) | (1 << RubyParser.PUBLIC) | (1 << RubyParser.PROTECTED))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DotsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOTDOT(self):
            return self.getToken(RubyParser.DOTDOT, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_dots

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDots" ):
                listener.enterDots(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDots" ):
                listener.exitDots(self)




    def dots(self):

        localctx = RubyParser.DotsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_dots)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(RubyParser.DOTDOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(RubyParser.Id_Context,0)


        def instance_var(self):
            return self.getTypedRuleContext(RubyParser.Instance_varContext,0)


        def LPAREN(self):
            return self.getToken(RubyParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(RubyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(RubyParser.RPAREN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = RubyParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_primary)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.id_()
                pass
            elif token in [RubyParser.INSTANCE_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
                self.instance_var()
                pass
            elif token in [RubyParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 621
                self.match(RubyParser.LPAREN)
                self.state = 622
                self.expression()
                self.state = 623
                self.match(RubyParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InpterpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERPOLATED_STRING(self):
            return self.getToken(RubyParser.INTERPOLATED_STRING, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_inpterp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInpterp" ):
                listener.enterInpterp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInpterp" ):
                listener.exitInpterp(self)




    def inpterp(self):

        localctx = RubyParser.InpterpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_inpterp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(RubyParser.INTERPOLATED_STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.method_definition_params_list_sempred
        self._predicates[21] = self.method_call_params_sempred
        self._predicates[35] = self.statement_expression_list_sempred
        self._predicates[42] = self.array_definition_elements_sempred
        self._predicates[44] = self.dynamic_result_sempred
        self._predicates[49] = self.rvalue_sempred
        self._predicates[59] = self.terminator_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def method_definition_params_list_sempred(self, localctx:Method_definition_params_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def method_call_params_sempred(self, localctx:Method_call_paramsContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def statement_expression_list_sempred(self, localctx:Statement_expression_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def array_definition_elements_sempred(self, localctx:Array_definition_elementsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def dynamic_result_sempred(self, localctx:Dynamic_resultContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

    def rvalue_sempred(self, localctx:RvalueContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

    def terminator_sempred(self, localctx:TerminatorContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 3)
         




