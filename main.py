"""
Atividade Prática: Sistema de Gerenciamento Escolar
ALGORITMOS E LÓGICA DE PROGRAMAÇÃO
"""

# 3.1. Gerenciamento de Dependências (Imports)
import sys

def obter_nota_valida(nome_prova):
    """
    Dica do Professor: Realiza a validação de dados de entrada.
    Um bom sistema impede valores menores que 0 ou maiores que 10.
    """
    while True:
        try:
            nota = float(input(f"Digite a nota da {nome_prova}: "))
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("⚠️ Erro: A nota deve estar entre 0.0 e 10.0. Tente novamente.")
        except ValueError:
            print("⚠️ Erro: Entrada inválida. Digite um número válido.")

def main():
    print("=" * 50)
    print("   SISTEMA DE GERENCIAMENTO ESCOLAR (SGE)   ")
    print("=" * 50)
    
    # 3.2. Menu Principal e Entrada de Dados (1º Menu)
    nome_aluno = input("Nome do Aluno: ").strip()
    cod_disciplina = input("Código da Disciplina (CÓD. DISC.): ").strip()
    
    print("\n--- Coleta Sequencial de Notas ---")
    # 3.3. Coleta sequencial das 6 notas da composição anual
    p1  = obter_nota_valida("P1")
    p2  = obter_nota_valida("P2")
    pd  = obter_nota_valida("PD")
    pp1 = obter_nota_valida("Pp1")
    pp2 = obter_nota_valida("Pp2")
    pp3 = obter_nota_valida("Pp3")
    
    # 3.3. Cálculo da Média Final (Respeitando a ordem de precedência dos operadores)
    media_final = (p1 + p2 + pd + pp1 + pp2 + pp3) / 6
    
    print("\n" + "=" * 50)
    print("PARECER FINAL SOBRE A SITUAÇÃO ACADÊMICA")
    print("-" * 50)
    print(f"Estudante: {nome_aluno}")
    print(f"Disciplina: {cod_disciplina}")
    print(f"Média Final Obtida: {media_final:.1f}")
    print("-" * 50)
    
    # 3.4. Regras de Negócio e Mensagens (MSN)
    if media_final >= 6.0:
        print("MSN: \"Aluno Aprovado\"")
    elif 4.0 <= media_final <= 5.9:
        print("MSN: \"Aluno em Recuperação\"")
    else:
        print("MSN: \"Aluno Reprovado\"")
    print("=" * 50)
    
    # === ESTA É A LINHA QUE MANTÉM A JANELA ABERTA ===
    print("\n")
    input("Pressione ENTER para fechar o programa...")

if __name__ == "__main__":
    main()
