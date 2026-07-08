# Questão 1 – Tokens e expressões regulares de LangC
**Compiladores – UFC Campus Quixadá**

---

## Definição das RegEx de cada Token

|    | **Token** | **Regex**                                                        |
|----|-----------|------------------------------------------------------------------|
| 1  | NUM       | `n.u.m`                                                          |
| 2  | TEXT      | `t.e.x.t`                                                        |
| 3  | BOOL      | `b.o.o.l`                                                        |
| 4  | SHOW      | `s.h.o.w`                                                        |
| 5  | TRUE      | `t.r.u.e`                                                        |
| 6  | FALSE     | `f.a.l.s.e`                                                      |
| 7  | NUM_LIT   | `(0-9).(0-9)*`                                                   |
| 8  | CONST     | `".(((a-z)\|(A-Z)\|(0-9)\|' ')*).*"`                             |
| 9  | VAR       | `((a-z)\|(A-Z)\|_).(((a-z)\|(A-Z)\|(0-9)\|_)*)`                 |
| 10 | EQ_EQ     | `=.=`                                                            |
| 11 | EQ        | `=`                                                              |
| 12 | ADD       | `+`                                                              |
| 13 | SUB       | `-`                                                              |
| 14 | MUL       | `*`                                                              |
| 15 | DIV       | `/`                                                              |
| 16 | GT        | `>`                                                              |
| 17 | LT        | `<`                                                              |
| 18 | SEMICOLON | `;`                                                              |
| 19 | LPAREN    | `(`                                                              |
| 20 | RPAREN    | `)`                                                              |

---