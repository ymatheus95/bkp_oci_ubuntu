# Backup de pasta do Ubuntu para OCI

Esse script realiza backup de pastas de sistema operacionais baseados em Debian e os envia para um bucket da Oracle Cloud, dispara mensagens via Telegram informando se o backup foi realizado com sucesso ou se falhou e registra em arquivo de logs o status de cada backup. 

Requisitos: 
- Python 3+ 
- Sistema operacional Debian 
- Pip 22+ 

Para disparar as mensagens do Telegram a biblioteca pyTelegramBotAPI deve ser instalada: 
- pip install pyTelegramBotAPI 

Estou aberto para dúvidas de como implanta-lo ou sugestão de como melhorá-lo.

