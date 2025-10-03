from src.main import tokenize_fsm


def test_tokenizer():
    assert tokenize_fsm('10 10.0 +') == [('NUMBER', 10), ('FLOAT', 10.0), ('OPERATION', '+')]
    assert tokenize_fsm('10 2 //') == [('NUMBER', 10), ('NUMBER', 2), ('OPERATION', '//')]
    assert tokenize_fsm('200 2.0 ~120 405 +   + - // % **') == [('NUMBER', 200), ('FLOAT', 2.0), ('NUMBER', -120), ('NUMBER', 405), ('OPERATION', '+'), ('OPERATION', '+'), ('OPERATION', '-'), ('OPERATION', '//'), ('OPERATION', '%'), ('OPERATION', '**')]

