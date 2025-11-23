import hashlib

class SistemaAutenticacao:
    """
    Classe que gerencia o cadastro, login e exclusão de usuários de forma segura.
    As senhas são armazenadas como hash (SHA-256), simulando um banco de dados.
    """
    def __init__(self):
        # Dicionário para armazenar usuários: {matricula: hash_senha}
        self.usuarios = {} 
        print("Sistema de Autenticação IESB inicializado.")

    def _gerar_hash_senha(self, senha: str) -> str:
        """
        Função auxiliar para gerar o hash SHA-256 da senha digitada
        pelo usuário.
        """
        senha_bytes = senha.encode('utf-8') 
        hash_obj = hashlib.sha256(senha_bytes)
        return hash_obj.hexdigest()

    def cadastrar_usuario(self, matricula: str, senha: str) -> bool:
        """
        Cadastra um novo usuário no sistema.
        """
        if not matricula or not senha:
            print("Erro: Matrícula e senha não podem ser vazias!")
            return False

        if matricula in self.usuarios:
            print(f"Erro: A matrícula '{matricula}' já está cadastrada!")
            return False
        
        hash_senha = self._gerar_hash_senha(senha)
        self.usuarios[matricula] = hash_senha
        
        print(f"Usuário '{matricula}' cadastrado com sucesso!")
        return True

    def fazer_login(self, matricula: str, senha_fornecida: str) -> bool:

        if matricula not in self.usuarios:
            print(f"O Login Falhou: Matrícula '{matricula}' não encontrada.")
            return False

        hash_armazenado = self.usuarios[matricula]
        hash_fornecido = self._gerar_hash_senha(senha_fornecida)
        
        if hash_fornecido == hash_armazenado:
            print(f"Login Aprovado: Usuário '{matricula}' autenticado com sucesso!")
            return True
        else:
            print("Login Falhou: Senha incorreta.")
            return False

    def excluir_usuario(self, matricula: str) -> bool:
        """
        Exclui um usuário do sistema pela sua matrícula.
        """
        if matricula in self.usuarios:
            # Remove o item do dicionário usando a matrícula como chave
            del self.usuarios[matricula]
            print(f"Usuário '{matricula}' excluído com sucesso!")
            return True
        else:
            print(f"Erro: Matrícula '{matricula}' não encontrada para exclusão.")
            return False

# --- Teste de Execução e Demonstração ---

def menu_interativo():

    sistema = SistemaAutenticacao() 
    
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Excluir Usuário") 
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            matricula = input("Digite a Matrícula para cadastro: ")
            senha = input("Digite a Senha: ")
            sistema.cadastrar_usuario(matricula, senha)
            
        elif escolha == '2':
            matricula = input("Digite a Matrícula para login: ")
            senha = input("Digite a Senha: ")
            sistema.fazer_login(matricula, senha)
            
        elif escolha == '3':
            matricula = input("Digite a Matrícula a ser excluída: ")
            sistema.excluir_usuario(matricula)
            
        elif escolha == '4':
            print("Saindo do sistema de testes. Adeus!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_interativo()