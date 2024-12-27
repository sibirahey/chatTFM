import os
import streamlit as st
from services.openai_service import OpenAIService
from services.vector_db_service import VectorDBService
from services.chat_handler import ChatHandler


class ChatApp:
    def __init__(self, persist_directory):
        self.persist_directory = persist_directory
        self.chat_handler = None

    def initialize_services(self, api_key):
        """
        Inicializa los servicios necesarios para el chatbot.

        Args:
            api_key (str): Clave API de OpenAI.
        """
        os.environ["OPENAI_API_KEY"] = api_key
        vector_db_service = VectorDBService(persist_directory=self.persist_directory)
        openai_service = OpenAIService(api_key=api_key)
        self.chat_handler = ChatHandler(openai_service, vector_db_service)

    def show_sidebar(self):
        """
        Muestra la barra lateral con la configuración.
        """
        with st.sidebar:
            st.title("Configuración")
            st.write("Ingrese su clave de API de OpenAI.")

            # Input único para la clave de API
            api_key = st.text_input("OpenAI API Key", type="password", key="sidebar_openai_api_key")

            return api_key

    def show_chat(self):
        """
        Muestra el historial de mensajes y el campo de entrada.
        """
        st.title("💬 Chatbot")

        # Inicializar el historial de mensajes si no existe
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "¿Cómo puedo ayudarle?"}]

        # Mostrar el historial de mensajes
        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # Campo de entrada del usuario
        if user_input := st.chat_input("Escribe tu mensaje aquí..."):
            # Registrar el mensaje del usuario
            st.session_state["messages"].append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.write(user_input)
            return user_input

        return None

    def run(self):
        """
        Ejecuta la aplicación.
        """
        # Mostrar la barra lateral y obtener la clave de API
        api_key = self.show_sidebar()
        if not api_key:
            st.warning("Por favor, ingrese su clave de API.")
            st.stop()

        # Inicializar servicios si no están configurados
        if not self.chat_handler:
            self.initialize_services(api_key)

        # Mostrar la interfaz del chat
        if user_message := self.show_chat():
            # Generar la respuesta del asistente
            assistant_response = self.chat_handler.handle_message(user_message)

            # Registrar el mensaje del asistente
            st.session_state["messages"].append({"role": "assistant", "content": assistant_response})
            with st.chat_message("assistant"):
                st.write(assistant_response)


def main():
    persist_directory = "./db/"
    app = ChatApp(persist_directory)
    app.run()


if __name__ == "__main__":
    main()