# %%
import pandas as pd

# %%
import pandas as pd
import random


nomes_masculinos = ['Pedro', 'Lucas', 'Gabriel', 'Miguel', 'Rafael', 'Matheus', 'João', 'Gustavo', 'Daniel', 'Felipe','Carlos', 'Eduardo', 'André', 'Bruno', 'Vinícius', 'Leonardo', 'Thiago', 'Alexandre', 'Henrique','Davi', 'Marcelo', 'Antônio', 'Rodrigo', 'Luiz', 'Ricardo', 'Arthur', 'Diego', 'Francisco', 'Igor','Cauã', 'Enzo', 'Benjamim', 'Samuel', 'Victor', 'Nathan', 'Guilherme', 'Renato', 'Bernardo', 'Fernando','Fábio', 'Otávio', 'Augusto', 'Cristiano', 'Tiago', 'Leandro', 'Marcus', 'Júlio', 'Eduardo', 'Hélio','Ismael']
nomes_femininos = ['Maria', 'Laura', 'Sophia', 'Alice', 'Valentina', 'Isabella', 'Manuela', 'Helena', 'Luiza', 'Júlia','Lorena', 'Lívia', 'Mariana', 'Beatriz', 'Yasmin', 'Gabriela', 'Clara', 'Eloá', 'Isadora', 'Giovanna','Sarah', 'Camila', 'Letícia', 'Ana', 'Rafaela', 'Vitória', 'Lara', 'Bianca', 'Esther', 'Heloísa', 'Lavinia','Cecília', 'Maitê', 'Amanda', 'Carolina', 'Fernanda', 'Elisa', 'Isabel', 'Nina', 'Antonella', 'Eduarda','Luna', 'Agatha', 'Valentina', 'Jade', 'Pietra', 'Stella', 'Emilly', 'Isis', 'Larissa', 'Natália']
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Rodrigues', 'Almeida', 'Costa', 'Carvalho', 'Ferreira','Martins', 'Rocha', 'Rezende', 'Lima', 'Gomes', 'Ribeiro', 'Barbosa', 'Melo', 'Cardoso', 'Freitas','Araújo', 'Nascimento', 'Cavalcanti', 'Moura', 'Dias', 'Castro', 'Campos', 'Moreira', 'Teixeira','Fernandes', 'Siqueira', 'Vieira', 'Monteiro', 'Mendes', 'Coelho', 'Correia', 'Peixoto', 'Machado','Pinto', 'Borges', 'Nogueira', 'Sousa', 'Braga', 'Batista', 'Fogaça', 'Guimarães', 'Gonçalves', 'Lopes','Lima', 'Andrade', 'Montenegro', 'Veiga', 'Tavares', 'Alves', 'Ramos', 'Freire', 'Azevedo', 'Bessa','Peçanha', 'Saraiva', 'Leal', 'Figueiredo', 'Lobato', 'Peixe', 'Miranda', 'Junqueira', 'Bittencourt','Dantas', 'Xavier', 'Vargas', 'Passos', 'Caldeira', 'Bueno', 'Cunha', 'Vianna', 'Salgado', 'Bastos','Bandeira', 'Vasconcelos', 'Amorim', 'Viana', 'Cavalcante', 'Marques', 'Queirós', 'Aragão', 'Ferraz','Pimentel', 'Magalhães', 'Goulart', 'Fonseca', 'Peixoto', 'Couto', 'Rabelo', 'Barros', 'Medeiros', 'Valente']


# Dicionário com as cidades por estado
cidades_por_estado = {
    'AC': ['Rio Branco', 'Cruzeiro do Sul', 'Sena Madureira', 'Feijó', 'Tarauacá'],
    'AL': ['Maceió', 'Arapiraca', 'Palmeira dos Índios', 'Rio Largo', 'Marechal Deodoro'],
    'AP': ['Macapá', 'Santana', 'Laranjal do Jari', 'Oiapoque', 'Porto Grande'],
    'AM': ['Manaus', 'Parintins', 'Itacoatiara', 'Manacapuru', 'Coari'],
    'BA': ['Salvador', 'Feira de Santana', 'Vitória da Conquista', 'Camaçari', 'Itabuna'],
    'CE': ['Fortaleza', 'Caucaia', 'Juazeiro do Norte', 'Maracanaú', 'Sobral'],
    'DF': ['Brasília'],
    'ES': ['Vitória', 'Vila Velha', 'Serra', 'Cariacica', 'Cachoeiro de Itapemirim'],
    'GO': ['Goiânia', 'Aparecida de Goiânia', 'Anápolis', 'Rio Verde', 'Luziânia'],
    'MA': ['São Luís', 'Imperatriz', 'São José de Ribamar', 'Timon', 'Caxias'],
    'MT': ['Cuiabá', 'Várzea Grande', 'Rondonópolis', 'Sinop', 'Cáceres'],
    'MS': ['Campo Grande', 'Dourados', 'Três Lagoas', 'Corumbá', 'Ponta Porã'],
    'MG': ['Belo Horizonte', 'Uberlândia', 'Contagem', 'Juiz de Fora', 'Betim'],
    'PA': ['Belém', 'Ananindeua', 'Santarém', 'Marabá', 'Castanhal'],
    'PB': ['João Pessoa', 'Campina Grande', 'Santa Rita', 'Patos', 'Bayeux'],
    'PR': ['Curitiba', 'Londrina', 'Maringá', 'Ponta Grossa', 'Cascavel'],
    'PE': ['Recife', 'Jaboatão dos Guararapes', 'Olinda', 'Caruaru', 'Paulista'],
    'PI': ['Teresina', 'Parnaíba', 'Picos', 'Campo Maior', 'Floriano'],
    'RJ': ['Rio de Janeiro', 'São Gonçalo', 'Duque de Caxias', 'Nova Iguaçu', 'Niterói'],
    'RN': ['Natal', 'Mossoró', 'Parnamirim', 'São Gonçalo do Amarante', 'Macau'],
    'RS': ['Porto Alegre', 'Caxias do Sul', 'Canoas', 'Pelotas', 'Santa Maria'],
    'RO': ['Porto Velho', 'Ji-Paraná', 'Ariquemes', 'Vilhena', 'Cacoal'],
    'RR': ['Boa Vista', 'Rorainópolis', 'Caracaraí', 'São João da Baliza', 'Mucajaí'],
    'SC': ['Florianópolis', 'Joinville', 'Blumenau', 'São José', 'Criciúma'],
    'SP': ['São Paulo', 'Guarulhos', 'Campinas', 'São Bernardo do Campo', 'Santo André'],
    'SE': ['Aracaju', 'Nossa Senhora do Socorro', 'Lagarto', 'Itabaiana', 'São Cristóvão'],
    'TO': ['Palmas', 'Araguaína', 'Gurupi', 'Porto Nacional', 'Paraíso do Tocantins']
}

# Dicionário com os setores e profissões relacionadas
setores_e_profissoes = {
    'Tecnologia da Informação': ['Desenvolvedor de Software', 'Engenheiro de Dados', 'Analista de Sistemas', 'Cientista de Dados', 'Arquiteto de Soluções', 'Gerente de Projetos de TI', 'Administrador de Banco de Dados', 'Analista de Segurança da Informação', 'Designer UX/UI', 'Especialista em Redes'],
    'Saúde': ['Médico', 'Enfermeiro', 'Fisioterapeuta', 'Nutricionista', 'Psicólogo', 'Farmacêutico', 'Terapeuta Ocupacional', 'Dentista', 'Técnico de Enfermagem', 'Educador Físico'],
    'Educação': ['Professor', 'Pedagogo', 'Coordenador Pedagógico', 'Diretor Escolar', 'Orientador Educacional', 'Assistente de Sala de Aula', 'Professor de Educação Física', 'Professor de Língua Estrangeira', 'Professor de Matemática', 'Professor de História'],
    'Engenharia': ['Engenheiro Civil', 'Engenheiro Mecânico', 'Engenheiro Eletricista', 'Engenheiro de Produção', 'Engenheiro Ambiental', 'Engenheiro de Controle e Automação', 'Engenheiro Químico', 'Engenheiro de Telecomunicações', 'Engenheiro de Petróleo', 'Engenheiro de Segurança do Trabalho'],
    'Marketing': ['Gerente de Marketing', 'Analista de Marketing Digital', 'Consultor de SEO', 'Especialista em Mídias Sociais', 'Analista de Pesquisa de Mercado', 'Coordenador de Eventos', 'Designer Gráfico', 'Redator Publicitário', 'Planejador de Campanhas Publicitárias', 'Especialista em E-mail Marketing'],
    'Jurídico': ['Advogado', 'Juiz', 'Promotor de Justiça', 'Defensor Público', 'Delegado de Polícia', 'Consultor Jurídico', 'Escriturário Judicial', 'Tabelião', 'Oficial de Justiça', 'Assistente Jurídico'],
    'Finanças': ['Analista Financeiro', 'Controller', 'Analista de Investimentos', 'Gerente de Contas a Pagar e Receber', 'Especialista em Planejamento Financeiro', 'Auditor Financeiro', 'Analista de Crédito', 'Técnico Contábil', 'Economista', 'Analista de Tesouraria'],
    'Comunicação': ['Jornalista', 'Relações Públicas', 'Assessor de Imprensa', 'Editor de Conteúdo', 'Produtor Audiovisual', 'Apresentador de TV/Rádio', 'Repórter', 'Diretor de Arte', 'Fotógrafo', 'Social Media Manager'],
    'Administração': ['Gerente Administrativo', 'Assistente Administrativo', 'Analista de Recursos Humanos', 'Gestor de Projetos', 'Analista de Compras', 'Analista de Logística', 'Analista de Qualidade', 'Gerente de Operações', 'Supervisor de Atendimento ao Cliente', 'Analista de Planejamento Estratégico'],
    'Artes': ['Artista Plástico', 'Escultor', 'Pintor', 'Ilustrador', 'Designer de Moda', 'Fotógrafo de Moda', 'Cenógrafo', 'Designer de Interiores', 'Dançarino', 'Ator'],
}

# Dicionário com os adjetivos e substantivos relacionados aos setores para nomes de empresas
adjetivos_substantivos = {
    'Tecnologia da Informação': {
        'adjetivos': ['Digital', 'Tech', 'Inovadora', 'Global', 'Ágil', 'Eficaz', 'Inteligente', 'Conectada', 'Data', 'Inovadora'],
        'substantivos': ['Soluções', 'Tech', 'Softwares', 'Tecnologia', 'Sistemas', 'Digital', 'Informática', 'Data', 'Apps', 'Inovação']
    },
    'Saúde': {
        'adjetivos': ['Saúde', 'Vida', 'Bem-Estar', 'Med', 'Farma', 'Bio', 'Cura', 'Clin', 'Health', 'Fit'],
        'substantivos': ['Saúde', 'Vida', 'Cuidados', 'Farmácia', 'Bem-Estar', 'Médica', 'Clínica', 'Health', 'Fit', 'Biotech']
    },
    'Educação': {
        'adjetivos': ['Educa', 'Learn', 'Knowledge', 'Academy', 'School', 'Sabedoria', 'Bright', 'Tutor', 'Educat', 'Tech'],
        'substantivos': ['Educação', 'Aprendizado', 'Knowledge', 'Academia', 'Escola', 'Saberes', 'Bright', 'Tutor', 'Educat', 'Tech']
    },
    'Engenharia': {
        'adjetivos': ['Engen', 'Tech', 'Constru', 'Innov', 'Soluções', 'Smart', 'Engene', 'Creat', 'Expert', 'Effic'],
        'substantivos': ['Engenharia', 'Tecnologia', 'Construção', 'Inovação', 'Soluções', 'Smart', 'Engene', 'Criatividade', 'Expert', 'Eficiência']
    },
    'Marketing': {
        'adjetivos': ['Market', 'Advert', 'Digit', 'Branding', 'Media', 'Tech', 'Innov', 'Brand', 'Commun', 'Creat'],
        'substantivos': ['Marketing', 'Publicidade', 'Digital', 'Branding', 'Mídia', 'Tech', 'Inovação', 'Branding', 'Comunicação', 'Criatividade']
    },
    'Jurídico': {
        'adjetivos': ['Law', 'Justi', 'Advoc', 'Legal', 'Tech', 'Soluções', 'Smart', 'Expert', 'Innov', 'Legal'],
        'substantivos': ['Jurídico', 'Justiça', 'Advocacia', 'Legal', 'Tech', 'Soluções', 'Smart', 'Expert', 'Inovação', 'Legal']
    },
    'Finanças': {
        'adjetivos': ['Financ', 'Money', 'Invest', 'Wealth', 'Capital', 'Tech', 'Soluções', 'Smart', 'Expert', 'Innov'],
        'substantivos': ['Finanças', 'Dinheiro', 'Investimentos', 'Wealth', 'Capital', 'Tech', 'Soluções', 'Smart', 'Expert', 'Inovação']
    },
    'Comunicação': {
        'adjetivos': ['Commun', 'Media', 'Digit', 'Creative', 'Branding', 'Tech', 'Soluções', 'Innov', 'Social', 'Advert'],
        'substantivos': ['Comunicação', 'Mídia', 'Digital', 'Criatividade', 'Branding', 'Tech', 'Soluções', 'Inovação', 'Social', 'Publicidade']
    },
    'Administração': {
        'adjetivos': ['Admin', 'Soluções', 'Tech', 'Smart', 'Expert', 'Efficient', 'Innov', 'Manage', 'Business', 'Creat'],
        'substantivos': ['Administração', 'Soluções', 'Tech', 'Smart', 'Expert', 'Eficiência', 'Inovação', 'Gestão', 'Negócios', 'Criatividade']
    },
    'Artes': {
        'adjetivos': ['Art', 'Creat', 'Design', 'Innov', 'Talent', 'Bright', 'Inspire', 'Culture', 'Visual', 'Media'],
        'substantivos': ['Artes', 'Criatividade', 'Design', 'Inovação', 'Talentos', 'Bright', 'Inspiração', 'Cultura', 'Visual', 'Mídia']
    }
}

# Dicionário com os intervalos de salário para cada setor
salarios_por_setor = {
    'Tecnologia da Informação': (5000, 15000),
    'Saúde': (4000, 12000),
    'Educação': (3000, 8000),
    'Engenharia': (6000, 18000),
    'Marketing': (4000, 12000),
    'Jurídico': (5000, 15000),
    'Finanças': (6000, 18000),
    'Comunicação': (4000, 12000),
    'Administração': (5000, 15000),
    'Artes': (3000, 8000)
}


def gerar_salario_medio(setor):
    intervalo_salario = salarios_por_setor.get(setor)
    if intervalo_salario:
        salario_minimo, salario_maximo = intervalo_salario
        # Calcular a quantidade de passos de 500 dentro do intervalo de salário
        num_passos = (salario_maximo - salario_minimo) // 500
        # Escolher aleatoriamente um passo entre 0 e o número de passos e multiplicar por 500
        passo_aleatorio = random.randint(0, num_passos) * 500
        return salario_minimo + passo_aleatorio
    else:
        raise ValueError("Setor inválido ou sem salário definido.")

def gerar_dados_aleatorios(numero_linhas, nomes_masculinos, nomes_femininos, sobrenomes, nome_arquivo="mock_setores_profissoes.xlsx"):
    colunas = {
        "nome": [],
        "sobrenome": [],
        "sexo": [],
        "endereco": [],
        "cidade": [],
        "sigla_uf": [],
        "setor": [],
        "profissao": [],
        "salario": [],
        "empresa": []
    }

    for _ in range(numero_linhas):
        # Gerar dados aleatórios de nome, sobrenome e sexo
        if random.random() < 0.5:
            nome = random.choice(nomes_masculinos)
            sexo = "Masculino"
        else:
            nome = random.choice(nomes_femininos)
            sexo = "Feminino"
        sobrenome = random.choice(sobrenomes)

        colunas["nome"].append(nome)
        colunas["sobrenome"].append(sobrenome)
        colunas["sexo"].append(sexo)

        # Gerar endereço aleatório
        sigla_uf, cidade = random.choice(list(cidades_por_estado.items()))
        cidade = random.choice(cidade)
        colunas["endereco"].append(f"{random.choice(['Rua', 'Avenida', 'Travessa', 'Alameda', 'Estrada'])} Bairro {random.randint(1, 100)} {random.choice(['Verde', 'Azul', 'Amarelo', 'Branco', 'Vermelho', 'Largo', 'Estreito', 'Velho', 'Novo', 'Antigo', 'Bonito', 'Alegre','Iluminado', 'Cheio','Sossegado', 'Movimentado', 'Barulhento', 'Silencioso', 'Calmo', 'Agitado'])}")

        colunas["cidade"].append(cidade)
        colunas["sigla_uf"].append(sigla_uf)

        # Escolher aleatoriamente um setor e uma profissão relacionada ao setor
        setor = random.choice(list(setores_e_profissoes.keys()))
        profissao = random.choice(setores_e_profissoes[setor])
        colunas["setor"].append(setor)
        colunas["profissao"].append(profissao)

        # Gerar salário aleatório considerando intervalos de 1000 em 1000
        salario = gerar_salario_medio(setor)
        colunas["salario"].append(salario)

        # Escolher aleatoriamente o nome de uma empresa relacionada ao setor
        empresa = f"{random.choice(adjetivos_substantivos[setor]['adjetivos'])} {random.choice(adjetivos_substantivos[setor]['substantivos'])}"
        colunas["empresa"].append(empresa)

    df = pd.DataFrame(colunas)

    # Exportar os dados para um arquivo Excel
    df.to_excel(nome_arquivo, index=False)

# %%


if __name__ == "__main__":
    gerar_dados_aleatorios(500, nomes_masculinos, nomes_femininos, sobrenomes)
