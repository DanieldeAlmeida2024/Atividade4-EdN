"""Testes de comportamento dos quatro exercícios interativos (sem rede)."""
import importlib.util
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def importar(nome, path):
    spec = importlib.util.spec_from_file_location(nome, ROOT / path)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

calc = importar("calculadora", "1/calculadora.py")
senha = importar("verificacao_de_senha", "3/verificacaoDeSenha.py")

def executar(arquivo, entradas):
    return subprocess.run(
        [sys.executable, str(ROOT / arquivo)],
        input=entradas, capture_output=True, text=True, timeout=10
    )

class TestesAtividade04(unittest.TestCase):
    def test_quatro_operacoes(self):
        for a, b, op, esperado in (
            (5, 2, '+', 7), (5, 2, '-', 3), (5, 2, '*', 10), (6, 2, '/', 3)
        ):
            with self.subTest(op=op):
                self.assertEqual(esperado, calc.calcular(a, b, op))

    def test_calculo_rejeita_invalidos(self):
        for a, b, op in (
            (5, 0, '/'), (2, 2, '%'), (float('nan'), 2, '+'),
            (2, float('inf'), '*'), (1e308, 1e308, '*')
        ):
            with self.subTest(a=a, b=b, op=op), self.assertRaises(ValueError):
                calc.calcular(a, b, op)

    def test_calculadora_recupera_de_divisao_por_zero(self):
        p = executar("1/calculadora.py", "6\n0\n/\n6\n2\n/\n")
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("Não é possível dividir por zero", p.stdout)
        self.assertIn("6.0 / 2.0 é: 3.0", p.stdout)

    def test_calculadora_encerrar_entrada_sem_traceback(self):
        p = executar("1/calculadora.py", "")
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("Entrada encerrada", p.stdout)

    def test_notas_ignora_invalidas_e_aceita_fim_com_espaco(self):
        p = executar("2/registroDeNotas.py", "9\n12\nxyz\n8\n fim \n")
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("2", p.stdout)
        self.assertIn("8.50", p.stdout)

    def test_senha_atende_so_aos_criterios_da_atividade(self):
        self.assertEqual((False, "A senha deve ter pelo menos 8 caracteres."),
                         senha.verificar_senha_forte("abc123"))
        valida, msg = senha.verificar_senha_forte("abcdefg1")
        self.assertTrue(valida)
        self.assertIn("critérios do exercício", msg)
        self.assertFalse(senha.verificar_senha_forte("abcdefgh")[0])

    def test_paridade_inclui_numeros_negativos(self):
        p = executar("4/verificadorParOuImpar.py", "-2\n3\nletra\n fim \n")
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("PARES inseridos: 1", p.stdout)
        self.assertIn("ÍMPARES inseridos: 1", p.stdout)


if __name__ == "__main__":
    unittest.main()
