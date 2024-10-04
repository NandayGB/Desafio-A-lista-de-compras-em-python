class Nanday:
    def __init__(self):
        self.produtos = []
        self.id_produto = 1
        self.unidades_medida = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]

    def menu_principal(self):
        print("\n" + "="*40)
        print("Lista de Compras Simples")
        print("="*40 + "\n")

        self.listar_produtos()

        print("Lista de compras Nanday")
        print("\nMenu de Opções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Pesquisar produtos")
        print("4. Sair do programa")

        return input("Escolha uma opção: ")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto adicionado.")
            return

        print("Produtos na lista:")
        for produto in self.produtos:
            print(f"{produto['id']}: {produto['nome']} ({produto['quantidade']} {produto['unidade']}) - {produto['descricao']}")

    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        
        print("\nUnidades de medida disponíveis:")
        for i, unidade in enumerate(self.unidades_medida, start=1):
            print(f"{i}. {unidade}")
        
        while True:
            try:
                escolha_unidade = int(input("Escolha a unidade de medida (digite o número): "))
                if 1 <= escolha_unidade <= len(self.unidades_medida):
                    unidade = self.unidades_medida[escolha_unidade - 1]
                    break
                else:
                    print("Opção inválida. Por favor, escolha um número válido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")

        while True:
            try:
                quantidade = float(input("Digite a quantidade do produto: "))
                if quantidade > 0:
                    break
                else:
                    print("Quantidade deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

        descricao = input("Digite uma descrição para o produto: ")

        novo_produto = {
            'id': self.id_produto,
            'nome': nome,
            'unidade': unidade,
            'quantidade': quantidade,
            'descricao': descricao
        }

        self.produtos.append(novo_produto)
        self.id_produto += 1

        print(f"\nProduto '{nome}' adicionado com sucesso!")

    def remover_produto(self):
        if not self.produtos:
            print("Não há produtos para remover.")
            return

        id_remover = input("Digite o ID do produto para remover: ")

        for produto in self.produtos:
            if str(produto['id']) == id_remover:
                self.produtos.remove(produto)
                print(f"Produto '{produto['nome']}' removido com sucesso!")
                return

        print("ID de produto não encontrado.")

    def pesquisar_produtos(self):
        if not self.produtos:
            print("Não há produtos para pesquisar.")
            return

        termo_pesquisa = input("Digite o termo para pesquisa: ").lower()

        resultados = [p for p in self.produtos if termo_pesquisa in p['nome'].lower()]

        if resultados:
            print(f"\n{len(resultados)} resultado(s) encontrado(s):")
            for produto in resultados:
                print(f"{produto['id']}: {produto['nome']} ({produto['quantidade']} {produto['unidade']}) - {produto['descricao']}")
        else:
            print("Nenhum resultado encontrado.")

    def run(self):
        while True:
            opcao = self.menu_principal()
            
            if opcao == "1":
                self.adicionar_produto()
            elif opcao == "2":
                self.remover_produto()
            elif opcao == "3":
                self.pesquisar_produtos()
            elif opcao == "4":
                print("Programa encerrado. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    app = Nanday()
    app.run()