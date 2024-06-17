from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, txt = "Felipe da Silva Faria", ln = True, align = 'C')

# Contact Info
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "E-mail: felipe.sfaria@hotmail.com", ln = True)
pdf.cell(200, 10, txt = "LinkedIn: https://www.linkedin.com/in/felipe-da-silva-faria-a92641138", ln = True)
pdf.cell(200, 10, txt = "Localização: Taguatinga, Distrito Federal, Brasil", ln = True)

# Add a line break
pdf.ln(10)

# Summary
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt = "Resumo Profissional", ln = True)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt = """
Analista de Dados com sólida experiência em Python para análise de dados e Microsoft Power BI. Especialista em ingestão e validação de dados, processos de ETL utilizando SQL, Pentaho, SSIS, e Python. Experiência na criação de indicadores, dashboards e insights utilizando Power BI, Data Studio e Excel para áreas Comerciais, Controladoria e Logística.
""")

# Experience
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt = "Experiência Profissional", ln = True)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt = "FiBrasil - Infraestrutura e Fibra Ótica", ln = True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Analista Sistema SR-Architecture & Data Analytics", ln = True)
pdf.cell(200, 10, txt = "Novembro de 2022 - Presente (1 ano 8 meses)", ln = True)
pdf.cell(200, 10, txt = "Brasília, Distrito Federal, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Desenvolvimento e manutenção de arquiteturas de sistemas e análises de dados.
- Implementação de processos de ETL e integração de dados.
""")

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt = "Vivo (Telefônica Brasil)", ln = True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Analista Gestão Vendas SR (BI)", ln = True)
pdf.cell(200, 10, txt = "Fevereiro de 2022 - Outubro de 2022 (9 meses)", ln = True)
pdf.cell(200, 10, txt = "Brasília, Distrito Federal, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Análise e gestão de vendas utilizando ferramentas de BI.
""")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Analista Suporte Vendas PL (BI)", ln = True)
pdf.cell(200, 10, txt = "Maio de 2021 - Fevereiro de 2022 (10 meses)", ln = True)
pdf.cell(200, 10, txt = "Brasília, Distrito Federal, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Suporte e análise de dados para a equipe de vendas.
""")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Analista Gestão Vendas JR (BI)", ln = True)
pdf.cell(200, 10, txt = "Outubro de 2019 - Maio de 2021 (1 ano 8 meses)", ln = True)
pdf.cell(200, 10, txt = "Brasília e Região, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Desenvolvimento de relatórios e dashboards para a gestão de vendas.
""")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Assistente Técnico (BI)", ln = True)
pdf.cell(200, 10, txt = "Março de 2015 - Outubro de 2019 (4 anos 8 meses)", ln = True)
pdf.cell(200, 10, txt = "Brasília e Região, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Suporte técnico e análise de dados.
""")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Auxiliar LA", ln = True)
pdf.cell(200, 10, txt = "Abril de 2014 - Março de 2015 (1 ano)", ln = True)
pdf.cell(200, 10, txt = "Brasília e Região, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Atividades auxiliares relacionadas ao suporte técnico.
""")

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt = "Amplimaster Antenas e Serviços (NET)", ln = True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Técnico de Instalação", ln = True)
pdf.cell(200, 10, txt = "Dezembro de 2011 - Abril de 2014 (2 anos 5 meses)", ln = True)
pdf.cell(200, 10, txt = "Brasília e Região, Brasil", ln = True)
pdf.multi_cell(0, 10, txt = """
Responsabilidades:
- Instalação e manutenção de sistemas de TV a cabo.
""")

# Education
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt = "Formação Acadêmica", ln = True)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt = "Faculdade Senac DF", ln = True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Pós-graduação Lato Sensu - Especialização em Banco de Dados e Business Intelligence com Ênfase em Tecnologia da Informação", ln = True)
pdf.cell(200, 10, txt = "2021 - 2023", ln = True)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt = "Estácio", ln = True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "MBA em Business Intelligence, Tecnologia da Informação", ln = True)
pdf.cell(200, 10, txt = "2018 - 2020", ln = True)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt = "Estácio", ln = True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Graduação em Redes de Computadores, Tecnologia da Informação", ln = True)
pdf.cell(200, 10, txt = "2016 - 2018", ln = True)

# Certifications
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt = "Certificações", ln = True)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "Google Cloud Platform (GCP) do Zero ao Avançado", ln = True)
pdf.cell(200, 10, txt = "Business Intelligence com Power BI - Estudos de Caso", ln = True)
pdf.cell(200, 10, txt = "Master DAX - Power BI Orientado a Projeto", ln = True)
pdf.cell(200, 10, txt = "Curso Básico de DAX Studio", ln = True)
pdf.cell(200, 10, txt = "Curso Básico de Power BI", ln = True)

# Skills
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, txt = "Competências Técnicas", ln = True)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt = """
- SQL Azure
- Azure Data Factory
- Azure Data Lake
- Python
- SQL Server
- Oracle SQL
- MySQL
- PostgreSQL
- Power BI
- Google Cloud Platform
- MongoDB
""")

# # Summary of Qualifications
# pdf.set_font("Arial", style='B', size=14)
# pdf.cell(200, 10, txt = "Resumo das Qualificações", ln = True)

# pdf.set_font("Arial", size=12)
# pdf.multi_cell(0, 10, txt = """
# Felipe da Silva Faria é um analista de dados experiente, especializado em Business Intelligence e análise de dados. Com um forte background em tecnologias como SQL, Python e Power BI, Felipe tem demonstrado habilidades excepcionais em processos de ETL e na criação de soluções analíticas que geram insights valiosos para diversas áreas de negócios. Sua formação acadêmica e certificações adicionais reforçam suas competências técnicas e seu compromisso contínuo com o desenvolvimento profissional.
# """)
pdf.output("felipedasilvafaria.pdf")






###markdown




# Felipe da Silva Faria

**Contato:**
- E-mail: [felipe.sfaria@hotmail.com](mailto:felipe.sfaria@hotmail.com)
- LinkedIn: [Felipe da Silva Faria](https://www.linkedin.com/in/felipe-da-silva-faria-a92641138)

**Localização:**
- Taguatinga, Distrito Federal, Brasil

---

## Resumo
Analista de Dados com sólida experiência em Python para análise de dados e Microsoft Power BI. Especialista em ingestão e validação de dados, processos de ETL utilizando SQL, Pentaho, SSIS, e Python. Experiência na criação de indicadores, dashboards e insights utilizando Power BI, Data Studio e Excel para áreas Comerciais, Controladoria e Logística.

---

## Experiência Profissional

**FiBrasil - Infraestrutura e Fibra Ótica**
- **Cargo:** Analista Sistema SR-Architecture & Data Analytics
- **Período:** Novembro de 2022 - Presente (1 ano 8 meses)
- **Localização:** Brasília, Distrito Federal, Brasil
- **Responsabilidades:**
  - Desenvolvimento e manutenção de arquiteturas de sistemas e análises de dados.
  - Implementação de processos de ETL e integração de dados.

**Vivo (Telefônica Brasil)**
- **Cargo:** Analista Gestão Vendas SR (BI)
- **Período:** Fevereiro de 2022 - Outubro de 2022 (9 meses)
- **Localização:** Brasília, Distrito Federal, Brasil
- **Responsabilidades:**
  - Análise e gestão de vendas utilizando ferramentas de BI.

- **Cargo:** Analista Suporte Vendas PL (BI)
- **Período:** Maio de 2021 - Fevereiro de 2022 (10 meses)
- **Localização:** Brasília, Distrito Federal, Brasil
- **Responsabilidades:**
  - Suporte e análise de dados para a equipe de vendas.

- **Cargo:** Analista Gestão Vendas JR (BI)
- **Período:** Outubro de 2019 - Maio de 2021 (1 ano 8 meses)
- **Localização:** Brasília e Região, Brasil
- **Responsabilidades:**
  - Desenvolvimento de relatórios e dashboards para a gestão de vendas.

- **Cargo:** Assistente Técnico (BI)
- **Período:** Março de 2015 - Outubro de 2019 (4 anos 8 meses)
- **Localização:** Brasília e Região, Brasil
- **Responsabilidades:**
  - Suporte técnico e análise de dados.

- **Cargo:** Auxiliar LA
- **Período:** Abril de 2014 - Março de 2015 (1 ano)
- **Localização:** Brasília e Região, Brasil
- **Responsabilidades:**
  - Atividades auxiliares relacionadas ao suporte técnico.

**Amplimaster Antenas e Serviços (NET)**
- **Cargo:** Técnico de Instalação
- **Período:** Dezembro de 2011 - Abril de 2014 (2 anos 5 meses)
- **Localização:** Brasília e Região, Brasil
- **Responsabilidades:**
  - Instalação e manutenção de sistemas de TV a cabo.

---

## Formação Acadêmica

**Faculdade Senac DF**
- **Pós-graduação Lato Sensu - Especialização** em Banco de Dados e Business Intelligence com Ênfase em Tecnologia da Informação
- **Período:** 2021 - 2023

**Estácio**
- **MBA em Business Intelligence**, Tecnologia da Informação
- **Período:** 2018 - 2020

**Estácio**
- **Graduação em Redes de Computadores**, Tecnologia da Informação
- **Período:** 2016 - 2018

---

## Certificações

- **Google Cloud Platform (GCP) do Zero ao Avançado**
- **Business Intelligence com Power BI - Estudos de Caso**
- **Master DAX - Power BI Orientado a Projeto**
- **Curso Básico de DAX Studio**
- **Curso Básico de Power BI**

---

## Principais Competências

- SQL Azure
- Azure Data Factory
- Azure Data Lake
- Python
- SQL Server
- Oracle SQL
- MySQL
- PostgreSQL
- Power BI
- Google Cloud Platform
- MongoDB

---

## Resumo das Qualificações

Felipe da Silva Faria é um analista de dados experiente, especializado em Business Intelligence e análise de dados. Com um forte background em tecnologias como SQL, Python e Power BI, Felipe tem demonstrado habilidades excepcionais em processos de ETL e na criação de soluções analíticas que geram insights valiosos para diversas áreas de negócios. Sua formação acadêmica e certificações adicionais reforçam suas competências técnicas e seu compromisso contínuo com o desenvolvimento profissional.
