
-- ================================
-- SCHEMA
-- ================================

CREATE SCHEMA IF NOT EXISTS dio_bank;

-- ================================
-- SEQUENCE
-- ================================

CREATE SEQUENCE IF NOT EXISTS dio_bank.seq_cod_conta START 10000;

-- ================================
-- CLIENTES
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.clientes (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    idade INT,
    profissao VARCHAR(100),
    renda_mensal NUMERIC(15,2),
    perfil_investidor VARCHAR(50) 
        CHECK (perfil_investidor IN ('conservador', 'moderado', 'arrojado')),
    objetivo_principal VARCHAR(150),
    aceita_risco BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);

-- ================================
-- CONTAS CORRENTES
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.contas_correntes (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT NOT NULL,

    cod_conta_corrente INTEGER NOT NULL 
        DEFAULT nextval('dio_bank.seq_cod_conta')
        UNIQUE
        CHECK (cod_conta_corrente BETWEEN 10000 AND 99999),

    saldo_atual NUMERIC(15,2) NOT NULL DEFAULT 0,
    limite_conta NUMERIC(15,2) NOT NULL DEFAULT 1500,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,

    CONSTRAINT fk_conta_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES dio_bank.clientes(id)
        ON DELETE CASCADE
);

-- ================================
-- TRANSACOES
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.transacoes (
    id BIGSERIAL PRIMARY KEY,
    conta_corrente_id BIGINT NOT NULL,
    descricao VARCHAR(100),
    categoria VARCHAR(100),
    valor NUMERIC(15,2) NOT NULL,
    tipo_operacao VARCHAR(10) NOT NULL 
        CHECK (tipo_operacao IN ('debito', 'credito')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_transection_conta
        FOREIGN KEY (conta_corrente_id)
        REFERENCES dio_bank.contas_correntes(id)
        ON DELETE CASCADE
);

-- ================================
-- PRODUTOS FINANCEIROS
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.produtos_financeiros (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    categoria VARCHAR(100),
    risco VARCHAR(20) 
        CHECK (risco IN ('baixo','medio','alto')),
    rentabilidade_descricao TEXT,
    aporte_minimo NUMERIC(15,2),
    liquidez VARCHAR(50),
    prazo_minimo_dias INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ================================
-- CONTAS INVESTIMENTO
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.contas_investimento (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT NOT NULL,
    produto_financeiro_id BIGINT NOT NULL,
    saldo NUMERIC(15,2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_invest_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES dio_bank.clientes(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_invest_produto
        FOREIGN KEY (produto_financeiro_id)
        REFERENCES dio_bank.produtos_financeiros(id)
        ON DELETE CASCADE
);

-- ================================
-- METAS
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.metas (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT NOT NULL,
    objetivo VARCHAR(150) NOT NULL,
    valor_necessario NUMERIC(15,2) NOT NULL,
    prazo DATE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_meta_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES dio_bank.clientes(id)
        ON DELETE CASCADE
);

-- ================================
-- HISTORICO ATENDIMENTOS
-- ================================

CREATE TABLE IF NOT EXISTS dio_bank.historico_atendimentos (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT,
    data DATE NOT NULL,
    canal VARCHAR(50),
    tema VARCHAR(100),
    resumo TEXT,
    resolvido BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_hist_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES dio_bank.clientes(id)
        ON DELETE SET NULL
);

-- ================================
-- TRIGGER SALDO AUTOMATICO
-- ================================

DROP TRIGGER IF EXISTS trg_atualiza_saldo ON dio_bank.transacoes;
DROP FUNCTION IF EXISTS dio_bank.fn_atualiza_saldo;

CREATE OR REPLACE FUNCTION dio_bank.fn_atualiza_saldo()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
DECLARE
    saldo_atual_conta NUMERIC;
    limite_conta_valor NUMERIC;
BEGIN

    SELECT saldo_atual, limite_conta
    INTO saldo_atual_conta, limite_conta_valor
    FROM dio_bank.contas_correntes
    WHERE id = NEW.conta_corrente_id;

    IF NEW.tipo_operacao = 'credito' THEN

        UPDATE dio_bank.contas_correntes
        SET saldo_atual = saldo_atual + NEW.valor
        WHERE id = NEW.conta_corrente_id;

    ELSIF NEW.tipo_operacao = 'debito' THEN

        IF saldo_atual_conta + limite_conta_valor < NEW.valor THEN
            RAISE EXCEPTION 'Saldo insuficiente para realizar o débito';
        END IF;

        UPDATE dio_bank.contas_correntes
        SET saldo_atual = saldo_atual - NEW.valor
        WHERE id = NEW.conta_corrente_id;

    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_atualiza_saldo
AFTER INSERT ON dio_bank.transacoes
FOR EACH ROW
EXECUTE FUNCTION dio_bank.fn_atualiza_saldo();

CREATE OR REPLACE FUNCTION dio_bank.criar_conta_corrente()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO dio_bank.contas_correntes(cliente_id)
    VALUES (NEW.id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_criar_conta_corrente
AFTER INSERT ON dio_bank.clientes
FOR EACH ROW
EXECUTE FUNCTION dio_bank.criar_conta_corrente();
