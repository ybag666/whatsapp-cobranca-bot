# whatsapp-cobranca-bot

Automação em Python para envio automático de mensagens de cobrança via WhatsApp Web.

##  Funcionalidades

- Lê clientes de uma planilha Excel
- Verifica a data de vencimento
- Envia mensagem automaticamente no WhatsApp
- Registra erros em arquivo CSV

---

##  Tecnologias

- Python
- openpyxl
- PyAutoGUI
- WhatsApp Web

---

##  Estrutura da planilha

| Nome | Telefone | Vencimento |
|-----|-----|-----|
| João | 55999999999 | 10/03/2026 |

---

##  Como usar

1. Instale as dependências

---

##  Sobre a planilha de exemplo

A planilha **nomes.xlsx** presente neste repositório é apenas um **exemplo demonstrativo** para mostrar como o sistema funciona.

Os nomes, números de telefone e datas utilizados são **dados fictícios** e não correspondem a clientes reais.

Para utilizar o sistema em um cenário real, basta substituir os dados da planilha pelos dados reais dos clientes, mantendo a mesma estrutura de colunas.

---

## Arquivo `erros.csv`

O arquivo **erros.csv** é utilizado para registrar possíveis falhas durante o envio das mensagens.

Sempre que o script não consegue enviar uma mensagem para um cliente, o sistema adiciona automaticamente no arquivo:

- o nome do cliente
- o número de telefone

Isso permite identificar posteriormente quais contatos tiveram erro e realizar o envio manualmente se necessário.

---

### Por que o arquivo está vazio?

No repositório, o arquivo **erros.csv** pode aparecer vazio porque ele foi incluído apenas como **demonstração da estrutura utilizada pelo sistema**.

Como o projeto disponibilizado é apenas um exemplo, não foram gerados erros reais durante a execução do script.

Durante o uso do sistema em um ambiente real, o arquivo será preenchido automaticamente sempre que ocorrer alguma falha no envio das mensagens.

---

### Botão "Continuar no navegador"

Em alguns computadores, ao abrir o link de envio de mensagem, o WhatsApp pode mostrar a opção **"Continuar no navegador"** antes de abrir a conversa no WhatsApp Web.

Para evitar que isso interrompa a automação, o script utiliza a biblioteca PyAutoGUI para localizar o botão **continuar.png** na tela e clicar automaticamente nele.

Caso o WhatsApp Web abra diretamente na conversa (sem mostrar essa tela), essa parte do código não é necessária e pode ser removida sem afetar o funcionamento da automação.

