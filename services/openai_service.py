import openai
from langchain_openai.chat_models import ChatOpenAI


class OpenAIService:
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        """
        Inicializa el servicio OpenAI con la configuración necesaria.

        Args:
            api_key (str): Clave API de OpenAI.
            model (str): Modelo a usar (por ejemplo, "gpt-3.5-turbo").
        """
        self.api_key = api_key
        self.model = model
        self.llm = None
        if api_key:
            self.set_api_key(api_key)

    def set_api_key(self, api_key):
        """
        Configura o actualiza la clave API y el modelo ChatOpenAI.

        Args:
            api_key (str): Clave API de OpenAI.
        """
        self.api_key = api_key
        openai.api_key = api_key  # Configura la clave de API globalmente en el módulo openai
        self.llm = ChatOpenAI(model=self.model)  # Configura el modelo de LangChain

    def get_llm(self):
        """
        Devuelve el objeto LLM configurado.

        Returns:
            ChatOpenAI: Instancia del modelo configurado.
        """
        if not self.llm:
            raise ValueError("API Key no configurada. Por favor configure la clave API primero.")
        return self.llm
