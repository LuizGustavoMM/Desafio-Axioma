import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransparencyAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_datasets(self, pagina=1, nome_conjunto=None, dados_abertos=True):
        """
        Consulta a lista de conjuntos de dados da API de Transparência.
        """
        endpoint = f"{self.base_url}/dados/api/publico/conjuntos-dados"
        
        params = {
            "pagina": pagina,
            "dadosAbertos": str(dados_abertos).lower(),
        }
        
        if nome_conjunto:
            params["nomeConjuntoDados"] = nome_conjunto

        try:
            logging.info(f"Consultando API: {endpoint} | Pagina: {pagina}")
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao consultar API: {e}")
            return None

class N8nIntegration:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_data(self, payload):
        """Envia os dados processados para o n8n"""
        try:
            response = requests.post(self.webhook_url, json=payload)
            if response.status_code == 200:
                logging.info("Dados enviados ao n8n com sucesso!")
                return True
            else:
                logging.warning(f"n8n retornou status {response.status_code}")
                return False
        except Exception as e:
            logging.error(f"Falha na integração com n8n: {e}")
            return False