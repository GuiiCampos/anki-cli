# anki-cli

CLI para gerenciar e enviar flashcards ao Anki em lote, sem precisar digitar palavra por palavra.

---

## Dependências

- [Python 3.8+](https://www.python.org/downloads/)
- [Anki](https://apps.ankiweb.net/) instalado e aberto
- [AnkiConnect](https://ankiweb.net/shared/info/2055492159) — extensão do Anki (código: `2055492159`)

---

## Instalação

### Linux

```bash
git clone https://github.com/GuiiCampos/anki-cli.git
cd anki-cli
git checkout linux-support
pip3 install -e . --break-system-packages
```

> Em algumas distribuições pode ser necessário instalar o pip antes:
> ```bash
> sudo apt install python3-pip
> ```

### Windows

```bash
git clone https://github.com/GuiiCampos/anki-cli.git
cd anki-cli
pip install -e .
```

---

## Configuração inicial

Após a instalação, na primeira execução o CLI cria automaticamente os arquivos necessários em `~/.anki-cli/`:

- `config.txt` — configurações como deck e modelo de card
- `queue.txt` — fila de palavras a serem enviadas
- `history.txt` — histórico de cards enviados

Para verificar se está tudo funcionando:

```bash
anki-cli status
```

---

## Comandos

```
anki-cli add <word>        Adiciona uma palavra rapidamente à fila
anki-cli addcard           Criação interativa de cartões
anki-cli list              Exibe os itens da fila
anki-cli edit <index>      Edita um item específico da fila
anki-cli remove <index>    Remove um item da fila
anki-cli clear             Limpa toda a fila
anki-cli open              Abre o arquivo de fila (queue.txt)
anki-cli history           Abre o histórico (history.txt)
anki-cli config            Abre o arquivo de configuração (config.txt)
anki-cli process           Processa a fila e envia os flashcards ao Anki
anki-cli status            Exibe o deck atual, itens na fila e status do Anki
anki-cli deck change       Lista os decks do Anki e troca o atual
anki-cli deck new          Cria um novo deck no Anki
anki-cli help              Mostra a mensagem de ajuda
```

---

## Formato da fila

Cada linha do `queue.txt` segue o formato:

```
palavra|tradução|tipo|exemplo
```

Onde o tipo pode ser:
- `t` — card de tradução simples (frente: palavra, verso: tradução)
- `c` — card de contexto (frente: frase de exemplo com pergunta, verso: tradução)

Exemplo:

```
hold|segurar|t|
endure|aguentar|c|She had to endure the pain alone.
```

---

## Exemplos de uso

```bash
# Adicionar uma palavra rapidamente
anki-cli add hold

# Criar um card interativamente
anki-cli addcard

# Ver o que está na fila
anki-cli list

# Enviar tudo ao Anki
anki-cli process

# Trocar o deck atual
anki-cli deck change
```

---

## Observações

- O Anki precisa estar aberto para os comandos que se comunicam com ele (`process`, `status`, `deck change`, `deck new`)
- O AnkiConnect roda em `http://127.0.0.1:8765` por padrão
- Após o `process`, a fila é limpa automaticamente e os itens são salvos em `history.txt`
