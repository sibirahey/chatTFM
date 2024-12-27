from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


class VectorDBService:
    def __init__(self, persist_directory: str):
        """
        Inicializa el servicio para interactuar con ChromaDB.

        Args:
            persist_directory (str): Directorio donde se almacena la base de datos Chroma.
            api_key (str): Clave API de OpenAI para generar embeddings.
        """
        self.persist_directory = persist_directory
        self.embedding_function = OpenAIEmbeddings()
        self.vectordb = None
        self._load_vector_db()

    def _load_vector_db(self):
        """
        Carga la base de datos Chroma desde el directorio de persistencia.
        """
        try:
            self.vectordb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embedding_function
            )
            print(f"Base de datos cargada con {self.vectordb.collection.count()} documentos.")
        except Exception as e:
            print(f"Error al cargar la base de datos Chroma: {str(e)}")
            raise

    def as_retriever(self, search_type="similarity", k=5):
        """
        Devuelve un `retriever` para realizar búsquedas en la base de datos vectorial.

        Args:
            search_type (str): Tipo de búsqueda a realizar (por ejemplo, "similarity").
            k (int): Número de resultados relevantes a recuperar.

        Returns:
            Retriever: Objeto retriever para usar en LangChain chains.
        """
        return self.vectordb.as_retriever(search_type=search_type, search_kwargs={"k": k})
