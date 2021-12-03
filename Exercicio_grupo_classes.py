import pandas as pd


class Sa:

    def __init__(self, parceiro: str, pedidos_de_compra: list, medicoes: bool):
        self.__parceiro = parceiro
        self.__pedidos_de_compra = pedidos_de_compra
        self.__medicoes = medicoes
        self.__aprovado = False
        if self.medicoes:
            self.__medicao_feita = False
        else:
            pass
        self.__estimate_criado = False
        self.__quote_criado = False

    @property
    def parceiro(self):
        return self.__parceiro

    @property
    def medicoes(self):
        return self.__medicoes

    @property
    def compra(self):
        return self.__pedidos_de_compra

    @property
    def aprovacao(self):
        return self.__aprovado

    @property
    def tabela(self):
        return self.__tabela_de_areas

    @property
    def estimate(self):
        return self.__estimate

    @property
    def quote(self):
        return self.__quote

    @property
    def medicao_concluida(self):
        return self.__medicao_feita

    @property
    def quote_criado(self):
        return self.__quote_criado

    @property
    def estimate_criado(self):
        return self.__estimate_criado

    def cisco_estimate(self, quantidades: list):
        if len(self.compra) != len(quantidades):
            raise ValueError(f"A lista de quantidade deve possuir o mesmo tamanho da lista de pedidos de compra, "
                             f"ou seja {len(self.compra)}")
        else:
            pedido = {}
            dataframe = pd.DataFrame(data=pedido)
            dataframe['Itens'] = self.compra
            dataframe['Quantidades'] = quantidades
            self.__estimate = dataframe
            self.__estimate_criado = True
            print("Estimate criado !")

    def direct(self, descontos: list):
        if len(self.compra) != len(descontos):
            raise ValueError("A lista de descontos precisa ter o mesmo tamanho da lista de pedidos de compra.")
        else:
            if not self.estimate_criado:
                raise ValueError("É preciso criar um estimate, antes de criar a Quote.")
            else:
                self.__quote = self.estimate
                self.quote['Descontos'] = descontos
                self.__quote_criado = True
                print("Quote criado !")

    def areas(self, localidades: int):
        if not self.medicoes:
            raise ValueError('Não há medições a serem realizadas para este pedido.')
        else:
            areas = []
            n = 0
            while n < localidades:
                dwg = float(input(f"\nInsira uma área para a localidade {n}: "))
                areas.append(dwg)
                n += 1

            dici = {}
            df = pd.DataFrame(data=dici)
            df['localidades'] = range(localidades)
            df['Areas'] = areas
            self.__tabela_de_areas = df
            self.__medicao_feita = True
            print("\n Medição realizada !")

    def avaliacao(self):
        if self.medicoes:
            if not self.medicao_concluida:
                raise ValueError("É preciso realizar a medição, antes de enviar para o cliente.")
            else:
                print(self.tabela)
                resp = ['Y', 'N']
                while (a := input('\nCliente está de acordo ? [Y/N]: ').title()) not in resp:
                    print("\nFavor digitar Y ou N.")
                if a == "Y":
                    self.__aprovado = True
                else:
                    print("\nÉ preciso refazer a medição.")
                    self.__medicao_feita = False

        else:
            pass

        if not self.quote_criado:
            raise ValueError("É preciso criar uma quote antes de envià-la para o cliente.")
        else:
            print(self.quote)
            resp = ['Y', 'N']
            while (a := input('\nCliente está de acordo ? [Y/N]: ').title()) not in resp:
                print("\nFavor digitar Y ou N.")

            if a == "Y":
                self.__aprovado = True
                print("\nItens vendidos ! :)")
            else:
                print("\nÉ preciso refazer a Quote.")
                self.__estimate_criado = False
                self.__quote_criado = False


petrobras = Sa("Petrobras", ['Router', 'Switch', "Access Point"], medicoes=False)

# petrobras.areas(5)

# petrobras.avaliacao()

# petrobras.cisco_estimate([5, 2])

# petrobras.cisco_estimate([5, 6, 7])

# petrobras.direct([67.4, 75.3, 80])

# petrobras.avaliacao()

rede_dor = Sa("Rede Dor", ["Router", "Switch"], medicoes=True)

# rede_dor.avaliacao()

# rede_dor.areas(3)

# rede_dor.cisco_estimate([3, 8])

# rede_dor.direct([76, 84])

# rede_dor.avaliacao()













