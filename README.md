# App de Previsão do Tempo

Este é um aplicativo simples de previsão do tempo que utiliza a API do OpenWeather para fornecer dados sobre o clima de uma cidade. O app exibe a temperatura atual, sensação térmica, e horários de nascer e pôr do sol

## Tecnologias Usadas

- **Flask**: Framework Python para desenvolvimento web.
- **Requests**: Biblioteca Python para fazer requisições HTTP.
- **Python-dotenv**: Para carregar variáveis de ambiente a partir de um arquivo `.env`.
- **OpenWeather API**: API para obter dados de previsão do tempo.

## Funcionalidades

- O usuário pode inserir o nome de uma cidade no formulário.
- O aplicativo retorna informações sobre:
  - Temperatura atual
  - Temperatura mínima e máxima
  - Sensação térmica
  - Horários de nascer e pôr do sol

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/indiaraelis/app-clima-indi.git
   cd app-clima-indi
2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use venv\\Scripts\\activate
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
4. Crie um arquivo .env na raiz do projeto e adicione a sua chave da API do OpenWeather:
   ```bash
   API_KEY=SUA_CHAVE_AQUI

## Rodando o App

1. Execute o servidor Flask:
   `python app.py`
2. Acesse o aplicativo no navegador em http://xxx.x.x.x:5001.

## Deploy

Este aplicativo pode ser facilmente deployado em plataformas como **Render** ou **Heroku**. Para configurar o deploy, defina a variável de ambiente `PORT` na plataforma de deploy.

## Contribuições

Contribuições são bem-vindas! Se você quiser melhorar ou adicionar novas funcionalidades ao projeto, faça um fork e envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](https://github.com/indiaraelis/app-clima-indi/blob/main/LICENSE) para mais detalhes. 
