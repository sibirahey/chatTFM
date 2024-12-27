from langchain.chains import ConversationalRetrievalChain


class ChatHandler:
    def __init__(self, openai_service, vector_db_service):
        """
        Inicializa el ChatHandler.

        Args:
            openai_service (OpenAIService): Servicio para interactuar con el modelo OpenAI.
            vector_db_service (VectorDBService): Servicio para interactuar con ChromaDB.
        """
        self.openai_service = openai_service
        self.vector_db_service = vector_db_service
        self.chat_history = []  # Historial de la conversación
        self.conversational_chain = None

    def initialize_chain(self):
        """
        Inicializa la cadena conversacional con el LLM y el retriever.
        """
        llm = self.openai_service.get_llm()
        retriever = self.vector_db_service.as_retriever(k=5)
        self.conversational_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            return_generated_question=True
        )

    def handle_message(self, user_message):
        """
        Maneja un mensaje del usuario y devuelve la respuesta generada.

        Args:
            user_message (str): Mensaje ingresado por el usuario.

        Returns:
            str: Respuesta generada por el modelo.
        """
        if not self.conversational_chain:
            self.initialize_chain()

        # Preparar los inputs, incluyendo el historial de conversación
        inputs = {
            "chat_history": self.chat_history,  # Asegurarse de pasar el historial de conversación
            "question": user_message
        }

        # Usar invoke en lugar de __call__
        result = self.conversational_chain.invoke(inputs)

        # Actualizar el historial de conversación
        self.chat_history.append({"role": "user", "content": user_message})
        self.chat_history.append({"role": "assistant", "content": result["answer"]})

        # Devolver la respuesta del asistente
        return result["answer"]
