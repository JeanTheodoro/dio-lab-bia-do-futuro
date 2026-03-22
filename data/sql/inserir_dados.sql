
INSERT INTO dio_bank.clientes 
(nome, idade, profissao, renda_mensal, perfil_investidor, objetivo_principal, aceita_risco)
VALUES
('João Silva', 35, 'Engenheiro', 12000.00, 'moderado', 'Aposentadoria tranquila', TRUE),
('Maria Souza', 28, 'Analista de Marketing', 6500.00, 'conservador', 'Reserva de emergência', FALSE),
('Carlos Pereira', 42, 'Empresário', 25000.00, 'arrojado', 'Expansão patrimonial', TRUE),
('Ana Costa', 31, 'Desenvolvedora', 9000.00, 'moderado', 'Compra de imóvel', TRUE),
('Fernanda Lima', 50, 'Professora', 7000.00, 'conservador', 'Segurança financeira', FALSE);


-- =========================
-- Criação das transacoes de cada usuario considerando 3 meses retroativo
-- =========================
ALTER TABLE dio_bank.transacoes
ALTER COLUMN created_at TYPE DATE;


INSERT INTO dio_bank.transacoes
(conta_corrente_id, descricao, categoria, valor, tipo_operacao, created_at)
VALUES

-- =========================
-- JOÃO SILVA
-- =========================

(1,'Salário mensal Janeiro','salario',12000.00,'credito','2026-01-05'),
(1,'Projeto freelance engenharia','renda_extra',2500.00,'credito','2026-01-10'),
(1,'Aluguel apartamento','aluguel',3200.00,'debito','2026-01-08'),
(1,'Supermercado mensal','supermercado',950.00,'debito','2026-01-12'),
(1,'Combustível carro','combustivel',620.00,'debito','2026-01-15'),
(1,'Farmácia','farmacia',180.00,'debito','2026-01-18'),
(1,'Conta de luz','conta_luz',210.00,'debito','2026-01-20'),
(1,'Conta de água','conta_agua',120.00,'debito','2026-01-21'),
(1,'Restaurante fim de semana','lazer',420.00,'debito','2026-01-25'),

(1,'Pagamento IPTU','iptu',850.00,'debito','2026-03-10'),
(1,'Pagamento IPVA','ipva',1600.00,'debito','2026-03-15'),

(1,'Salário mensal Fevereiro','salario',12000.00,'credito','2026-02-05'),
(1,'Consultoria engenharia','renda_extra',1800.00,'credito','2026-02-11'),
(1,'Aluguel apartamento','aluguel',3200.00,'debito','2026-02-08'),
(1,'Supermercado mensal','supermercado',910.00,'debito','2026-02-12'),
(1,'Combustível carro','combustivel',600.00,'debito','2026-02-15'),
(1,'Farmácia','farmacia',140.00,'debito','2026-02-17'),
(1,'Conta de luz','conta_luz',205.00,'debito','2026-02-19'),
(1,'Conta de água','conta_agua',115.00,'debito','2026-02-20'),
(1,'Cinema e jantar','lazer',380.00,'debito','2026-02-24'),

(1,'Salário mensal Março','salario',12000.00,'credito','2026-03-05'),
(1,'Projeto estrutural','renda_extra',2100.00,'credito','2026-03-10'),
(1,'Aluguel apartamento','aluguel',3200.00,'debito','2026-03-08'),
(1,'Supermercado mensal','supermercado',930.00,'debito','2026-03-12'),
(1,'Combustível carro','combustivel',610.00,'debito','2026-03-15'),
(1,'Farmácia','farmacia',150.00,'debito','2026-03-18'),
(1,'Conta de luz','conta_luz',220.00,'debito','2026-03-20'),
(1,'Conta de água','conta_agua',118.00,'debito','2026-03-22'),
(1,'Viagem curta','lazer',650.00,'debito','2026-03-27'),

        
-- =========================
-- MARIA SOUZA (Marketing - 6500)   
-- =========================

(2,'Salário mensal Janeiro','salario',6500.00,'credito','2026-01-05'),
(2,'Freelance redes sociais','renda_extra',900.00,'credito','2026-01-12'),
(2,'Aluguel apartamento','aluguel',1800.00,'debito','2026-01-08'),
(2,'Supermercado mensal','supermercado',520.00,'debito','2026-01-10'),
(2,'Combustível','combustivel',250.00,'debito','2026-01-14'),
(2,'Farmácia','farmacia',90.00,'debito','2026-01-16'),
(2,'Conta de luz','conta_luz',130.00,'debito','2026-01-18'),
(2,'Conta de água','conta_agua',75.00,'debito','2026-01-19'),
(2,'Cinema e bar','lazer',260.00,'debito','2026-01-23'),

(2,'Pagamento IPTU','iptu',600.00,'debito','2026-03-07'),
(2,'Pagamento IPVA','ipva',950.00,'debito','2026-03-09'),

(2,'Salário mensal Fevereiro','salario',6500.00,'credito','2026-02-05'),
(2,'Freelance marketing digital','renda_extra',750.00,'credito','2026-02-11'),
(2,'Aluguel apartamento','aluguel',1800.00,'debito','2026-02-08'),
(2,'Supermercado mensal','supermercado',500.00,'debito','2026-02-10'),
(2,'Combustível','combustivel',240.00,'debito','2026-02-14'),
(2,'Farmácia','farmacia',110.00,'debito','2026-02-16'),
(2,'Conta de luz','conta_luz',125.00,'debito','2026-02-18'),
(2,'Conta de água','conta_agua',70.00,'debito','2026-02-19'),
(2,'Passeio shopping','lazer',220.00,'debito','2026-02-23'),

(2,'Salário mensal Março','salario',6500.00,'credito','2026-03-05'),
(2,'Gestão redes sociais','renda_extra',820.00,'credito','2026-03-11'),
(2,'Aluguel apartamento','aluguel',1800.00,'debito','2026-03-08'),
(2,'Supermercado mensal','supermercado',540.00,'debito','2026-03-10'),
(2,'Combustível','combustivel',260.00,'debito','2026-03-14'),
(2,'Farmácia','farmacia',95.00,'debito','2026-03-16'),
(2,'Conta de luz','conta_luz',135.00,'debito','2026-03-18'),
(2,'Conta de água','conta_agua',78.00,'debito','2026-03-19'),
(2,'Happy hour','lazer',240.00,'debito','2026-03-26'),

-- =========================
-- CARLOS PEREIRA (Empresário - 25000)
-- =========================

(3,'Pró-labore empresa','salario',25000.00,'credito','2026-01-05'),
(3,'Dividendos empresa','renda_extra',8000.00,'credito','2026-01-12'),
(3,'Aluguel casa','aluguel',6500.00,'debito','2026-01-08'),
(3,'Supermercado premium','supermercado',1800.00,'debito','2026-01-10'),
(3,'Combustível SUV','combustivel',950.00,'debito','2026-01-14'),
(3,'Farmácia','farmacia',320.00,'debito','2026-01-16'),
(3,'Conta de luz','conta_luz',420.00,'debito','2026-01-18'),
(3,'Conta de água','conta_agua',210.00,'debito','2026-01-19'),
(3,'Restaurante e lazer','lazer',1200.00,'debito','2026-01-23'),

(3,'Pagamento IPTU','iptu',2100.00,'debito','2026-03-07'),
(3,'Pagamento IPVA','ipva',4200.00,'debito','2026-03-09'),

(3,'Pró-labore empresa','salario',25000.00,'credito','2026-02-05'),
(3,'Dividendos empresa','renda_extra',7000.00,'credito','2026-02-11'),
(3,'Aluguel casa','aluguel',6500.00,'debito','2026-02-08'),
(3,'Supermercado premium','supermercado',1700.00,'debito','2026-02-10'),
(3,'Combustível SUV','combustivel',910.00,'debito','2026-02-14'),
(3,'Farmácia','farmacia',280.00,'debito','2026-02-16'),
(3,'Conta de luz','conta_luz',410.00,'debito','2026-02-18'),
(3,'Conta de água','conta_agua',205.00,'debito','2026-02-19'),
(3,'Viagem fim semana','lazer',2400.00,'debito','2026-02-25'),

(3,'Pró-labore empresa','salario',25000.00,'credito','2026-03-05'),
(3,'Dividendos empresa','renda_extra',7500.00,'credito','2026-03-11'),
(3,'Aluguel casa','aluguel',6500.00,'debito','2026-03-08'),
(3,'Supermercado premium','supermercado',1750.00,'debito','2026-03-10'),
(3,'Combustível SUV','combustivel',920.00,'debito','2026-03-14'),
(3,'Farmácia','farmacia',310.00,'debito','2026-03-16'),
(3,'Conta de luz','conta_luz',430.00,'debito','2026-03-18'),
(3,'Conta de água','conta_agua',215.00,'debito','2026-03-19'),
(3,'Clube e lazer','lazer',1500.00,'debito','2026-03-27'),
-- =========================
-- ANA COSTA
-- =========================

(4,'Salário mensal','salario',9000.00,'credito','2026-01-05'),
(4,'Freelance desenvolvimento','renda_extra',2200.00,'credito','2026-01-12'),
(4,'Aluguel apartamento','aluguel',2400.00,'debito','2026-01-08'),
(4,'Supermercado','supermercado',700.00,'debito','2026-01-10'),
(4,'Combustível','combustivel',380.00,'debito','2026-01-14'),
(4,'Farmácia','farmacia',130.00,'debito','2026-01-16'),
(4,'Conta de luz','conta_luz',180.00,'debito','2026-01-18'),
(4,'Conta de água','conta_agua',90.00,'debito','2026-01-19'),
(4,'Streaming e lazer','lazer',300.00,'debito','2026-01-23'),
(4,'Pagamento IPTU','iptu',750.00,'debito','2026-01-07'),
(4,'Pagamento IPVA','ipva',1400.00,'debito','2026-01-09'),

(4,'Salário mensal','salario',9000.00,'credito','2026-02-05'),
(4,'Freelance desenvolvimento','renda_extra',1800.00,'credito','2026-02-12'),
(4,'Aluguel apartamento','aluguel',2400.00,'debito','2026-02-08'),
(4,'Supermercado','supermercado',690.00,'debito','2026-02-10'),
(4,'Combustível','combustivel',350.00,'debito','2026-02-14'),
(4,'Farmácia','farmacia',120.00,'debito','2026-02-16'),
(4,'Conta de luz','conta_luz',175.00,'debito','2026-02-18'),
(4,'Conta de água','conta_agua',85.00,'debito','2026-02-19'),
(4,'Cinema','lazer',260.00,'debito','2026-02-24'),

(4,'Salário mensal','salario',9000.00,'credito','2026-03-05'),
(4,'Freelance desenvolvimento','renda_extra',2000.00,'credito','2026-03-11'),
(4,'Aluguel apartamento','aluguel',2400.00,'debito','2026-03-08'),
(4,'Supermercado','supermercado',710.00,'debito','2026-03-10'),
(4,'Combustível','combustivel',370.00,'debito','2026-03-14'),
(4,'Farmácia','farmacia',110.00,'debito','2026-03-16'),
(4,'Conta de luz','conta_luz',190.00,'debito','2026-03-18'),
(4,'Conta de água','conta_agua',88.00,'debito','2026-03-19'),
(4,'Bar com amigos','lazer',320.00,'debito','2026-03-26'),


-- =========================
-- FERNANDA LIMA
-- =========================

(5,'Salário mensal','salario',7000.00,'credito','2026-01-05'),
(5,'Aulas particulares','renda_extra',1200.00,'credito','2026-01-12'),
(5,'Aluguel','aluguel',2000.00,'debito','2026-01-08'),
(5,'Supermercado','supermercado',620.00,'debito','2026-01-10'),
(5,'Combustível','combustivel',280.00,'debito','2026-01-14'),
(5,'Farmácia','farmacia',150.00,'debito','2026-01-16'),
(5,'Conta de luz','conta_luz',160.00,'debito','2026-01-18'),
(5,'Conta de água','conta_agua',80.00,'debito','2026-01-19'),
(5,'Passeio e lazer','lazer',210.00,'debito','2026-01-22'),
(5,'Pagamento IPTU','iptu',620.00,'debito','2026-01-07'),
(5,'Pagamento IPVA','ipva',980.00,'debito','2026-01-09'),

(5,'Salário mensal','salario',7000.00,'credito','2026-02-05'),
(5,'Aulas particulares','renda_extra',1100.00,'credito','2026-02-11'),
(5,'Aluguel','aluguel',2000.00,'debito','2026-02-08'),
(5,'Supermercado','supermercado',610.00,'debito','2026-02-10'),
(5,'Combustível','combustivel',260.00,'debito','2026-02-14'),
(5,'Farmácia','farmacia',170.00,'debito','2026-02-16'),
(5,'Conta de luz','conta_luz',150.00,'debito','2026-02-18'),
(5,'Conta de água','conta_agua',82.00,'debito','2026-02-19'),
(5,'Cinema','lazer',190.00,'debito','2026-02-23'),

(5,'Salário mensal','salario',7000.00,'credito','2026-03-05'),
(5,'Aulas particulares','renda_extra',1300.00,'credito','2026-03-11'),
(5,'Aluguel','aluguel',2000.00,'debito','2026-03-08'),
(5,'Supermercado','supermercado',640.00,'debito','2026-03-10'),
(5,'Combustível','combustivel',270.00,'debito','2026-03-14'),
(5,'Farmácia','farmacia',160.00,'debito','2026-03-16'),
(5,'Conta de luz','conta_luz',165.00,'debito','2026-03-18'),
(5,'Conta de água','conta_agua',85.00,'debito','2026-03-19'),
(5,'Teatro','lazer',230.00,'debito','2026-03-25');

ALTER TABLE dio_bank.transacoes
ALTER COLUMN created_at TYPE TIMESTAMP;

-- =========================
-- Criação dos produstos financeiros
-- =========================
INSERT INTO produtos_financeiros 
(nome, categoria, risco, rentabilidade_descricao, aporte_minimo, liquidez, prazo_minimo_dias)
VALUES
('CDB Banco XPTO','Renda Fixa','baixo','110% do CDI',1000.00,'Diária',30),
('Tesouro Selic','Tesouro Direto','baixo','Selic + 0,10%',100.00,'D+1',1),
('Fundo Multimercado Alpha','Fundo','medio','CDI + 5%',5000.00,'D+30',90),
('Ações Tech Brasil','Renda Variável','alto','Variável conforme mercado',2000.00,'D+2',0),
('LCI Premium','Renda Fixa','baixo','95% do CDI',5000.00,'No vencimento',180),
('CDB Banco XPTO','Renda Fixa','baixo','110% do CDI',1000.00,'Diária',30),
('Tesouro Selic','Tesouro Direto','baixo','Selic + 0,10%',100.00,'D+1',1),
('Fundo Multimercado Alpha','Fundo','medio','CDI + 5%',5000.00,'D+30',90),
('Ações Tech Brasil','Renda Variável','alto','Variável conforme mercado',2000.00,'D+2',0),
('LCI Premium','Renda Fixa','baixo','95% do CDI',5000.00,'No vencimento',180),
('Tesouro IPCA+ 2035','Tesouro Direto','medio','IPCA + 5,5%',100.00,'D+1',30),
('ETF BOVA11','ETF','alto','Varia conforme Ibovespa',150.00,'D+2',0),
('ETF IVVB11','ETF','alto','Varia conforme S&P 500',200.00,'D+2',0),
('Fundo Imobiliário XPML11','FII','medio','Dividendos mensais + valorização',120.00,'D+2',0),
('CDB Banco Digital 120%','Renda Fixa','baixo','120% do CDI',1000.00,'Diária',30),
('Debênture Incentivada Infra','Renda Fixa','medio','IPCA + 6%',5000.00,'No vencimento',720),
('Fundo Previdência Balanceado','Previdência','medio','Carteira balanceada RF/RV',500.00,'D+30',180),
('CRI Imobiliário High Grade','Renda Fixa','medio','IPCA + 7%',10000.00,'No vencimento',1080),
('Ações Banco Brasil','Renda Variável','alto','Dividendos + valorização',500.00,'D+2',0),
('Fundo Multimercado Macro','Fundo','medio','Estratégia macro global',3000.00,'D+30',90);

INSERT INTO dio_bank.metas
(cliente_id, objetivo, valor_necessario, prazo)
VALUES
-- João Silva (35 anos, Engenheiro)
-- renda alta e foco em longo prazo
(1, 'Aposentadoria tranquila', 1200000.00, '2045-12-31'),

-- Maria Souza (28 anos, Marketing)
-- perfil conservador, foco em segurança
(2, 'Reserva de emergência (6 meses de renda)', 40000.00, '2026-12-31'),

-- Carlos Pereira (Empresário)
-- perfil arrojado e renda alta
(3, 'Aquisição de nova empresa', 800000.00, '2030-06-30'),

-- Ana Costa (Desenvolvedora)
-- objetivo imobiliário
(4, 'Entrada para apartamento', 120000.00, '2027-03-31'),

-- Fernanda Lima (Professora)
-- perfil conservador
(5, 'Viagem internacional e reserva financeira', 35000.00, '2027-07-15');
