import json
import os
from datetime import datetime

DATA_PATH = os.path.join("data", "movimentos.json")

def carregar_movimentos():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_movimentos(movimentos):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(movimentos, f, indent=4, ensure_ascii=False)

def adicionar_movimento(gesto, significado, genero, idioma, cor, playlist=None):
    movimentos = carregar_movimentos()

    # Verifica se já existe um gesto igual (igualdade exata)
    if any(m["gesto"] == gesto for m in movimentos):
        raise ValueError(f"Gesto '{gesto}' já existe.")

    # Verifica se o significado já existe, exceto se for 'toca_playlist' ou 'notifica_tempo'
    significado_lower = significado.lower()
    if significado_lower not in ['toca_playlist', 'notifica_tempo']:
        if any(m["significado"].lower() == significado_lower for m in movimentos):
            raise ValueError(f"Significado '{significado}' já existe.")

    novo_movimento = {
        "gesto": gesto,
        "significado": significado,
        "genero": genero,
        "cor": cor,
        "idioma": idioma
    }

    if significado_lower == "toca_playlist" and playlist:
        novo_movimento["playlist"] = playlist

    movimentos.append(novo_movimento)
    salvar_movimentos(movimentos)


import ast

def editar_movimento(gesto_antigo, novo_gesto, significado_antigo, novo_significado, nova_cor, novo_genero, novo_idioma):
    movimentos = listar_movimentos()
    novo_gesto = ast.literal_eval(novo_gesto)

    movimento = next((m for m in movimentos if m['gesto'] == gesto_antigo), None)
    if movimento is None:
        raise ValueError("Gesto não encontrado.")

    # Verifica se o novo gesto já existe em outro movimento
    for m in movimentos:
        if m['gesto'] == gesto_antigo:
            continue  # ignora o próprio gesto atual
        if m['gesto'] == novo_gesto:
            raise ValueError(f"Gesto '{novo_gesto}' já existe.")

    # Verifica se o novo significado já existe em outro movimento (exceto para 'toca_playlist')
    if novo_significado != significado_antigo and any(m['significado'] == novo_significado for m in movimentos) and novo_significado != 'toca_playlist':
        raise ValueError("O novo significado já existe.")

    # Atualiza os dados
    movimento['gesto'] = novo_gesto
    movimento['significado'] = novo_significado
    movimento['cor'] = nova_cor

    if novo_significado == 'toca_playlist':
        movimento['genero'] = novo_genero
    else:
        movimento['genero'] = ''

    if novo_significado == 'notifica_tempo':
        movimento['idioma'] = novo_idioma
    else:
        movimento['idioma'] = ''

    # Salva no JSON
    with open('data/movimentos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(movimentos, arquivo, ensure_ascii=False, indent=4)




def listar_movimentos():
    with open('data/movimentos.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)  # Retorna uma lista de dicionários


def remover_movimento(gesto):
    movimentos = carregar_movimentos()

    # Padroniza o gesto de entrada
    print(gesto)
    movimentos_nao_removidos = []
    for el in movimentos:
        print(el)
        if str(el["gesto"]) != str(gesto):
            print(el["gesto"])
            print("\n")
            movimentos_nao_removidos.append(el)

    print(movimentos_nao_removidos)
    salvar_movimentos(movimentos_nao_removidos)

