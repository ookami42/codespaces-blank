def le_arquivo(caminho: str) -> str:
    with open(caminho, 'r', encoding='utf-8') as f:
        primeira_linha = f.readline()

        if not primeira_linha.startswith(';;chave='):
            return '', primeira_linha + f.read()
        
        primeira_linha = primeira_linha.removeprefix(';;chave=')
        primeira_linha = primeira_linha.rstrip('\r\n')
        return primeira_linha, f.read()
