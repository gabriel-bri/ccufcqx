--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- Started on 2023-07-31 21:33:09

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3390 (class 1262 OID 16564)
-- Name: projeto_final; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE projeto_final WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';


ALTER DATABASE projeto_final OWNER TO postgres;

\connect projeto_final

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 212 (class 1259 OID 16575)
-- Name: alongamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alongamento (
    codigo_de_plano integer NOT NULL,
    alongamento_partesuperior_do_corpo boolean,
    alongamento_dor_nas_costas boolean,
    alongamento_parte_inferior_do_corpo boolean,
    postura_de_crianca boolean,
    alongamento_peito boolean,
    alongamento_de_ombros boolean,
    alongamento_cobra boolean,
    alongamento_triceps boolean,
    alongamento_panturrilha boolean,
    quem_pratica integer
);


ALTER TABLE public.alongamento OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16574)
-- Name: alongamento_codigo_de_plano_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alongamento_codigo_de_plano_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.alongamento_codigo_de_plano_seq OWNER TO postgres;

--
-- TOC entry 3391 (class 0 OID 0)
-- Dependencies: 211
-- Name: alongamento_codigo_de_plano_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alongamento_codigo_de_plano_seq OWNED BY public.alongamento.codigo_de_plano;


--
-- TOC entry 220 (class 1259 OID 16625)
-- Name: lembretes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lembretes (
    id_lembrete integer NOT NULL,
    notificacao_atividade character varying,
    "monitoramento_de_ingestão_de_agua" boolean,
    qual_usuario integer
);


ALTER TABLE public.lembretes OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16611)
-- Name: relatorio_semana; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.relatorio_semana (
    id_relatorio integer NOT NULL,
    duracao_em_horas integer,
    historico character varying,
    qual_usuario integer
);


ALTER TABLE public.relatorio_semana OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16650)
-- Name: aluno_ativo; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.aluno_ativo AS
 SELECT r.qual_usuario AS id_usuario
   FROM public.relatorio_semana r,
    public.lembretes l
  WHERE ((r.qual_usuario = l.qual_usuario) AND (r.duracao_em_horas > 5) AND (l."monitoramento_de_ingestão_de_agua" = true))
  ORDER BY r.duracao_em_horas
  WITH NO DATA;


ALTER TABLE public.aluno_ativo OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16587)
-- Name: yoga; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.yoga (
    codigo_de_plano integer NOT NULL,
    concentracao_mental boolean,
    aprimoramento_mental boolean,
    encolhimento_dos_ombros boolean,
    inclinacao_para_os_lados boolean,
    postura_da_esfinge boolean,
    ponte boolean,
    bananeira boolean,
    estocada_crescente boolean,
    quem_pratica integer
);


ALTER TABLE public.yoga OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16654)
-- Name: aluno_de_atividadeintensa; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.aluno_de_atividadeintensa AS
 SELECT a.quem_pratica AS id_usuario
   FROM public.alongamento a,
    public.yoga y
  WHERE ((a.quem_pratica = y.quem_pratica) AND a.alongamento_partesuperior_do_corpo AND a.alongamento_parte_inferior_do_corpo AND a.alongamento_cobra AND a.postura_de_crianca AND y.ponte AND y.bananeira AND (y.postura_da_esfinge = true))
  GROUP BY a.quem_pratica;


ALTER TABLE public.aluno_de_atividadeintensa OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16639)
-- Name: configuracoes_gerais; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.configuracoes_gerais (
    codigo_versao integer NOT NULL,
    modo_noturno boolean,
    qual_usuario integer
);


ALTER TABLE public.configuracoes_gerais OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16638)
-- Name: configuracoes_gerais_codigo_versao_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.configuracoes_gerais_codigo_versao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.configuracoes_gerais_codigo_versao_seq OWNER TO postgres;

--
-- TOC entry 3392 (class 0 OID 0)
-- Dependencies: 221
-- Name: configuracoes_gerais_codigo_versao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.configuracoes_gerais_codigo_versao_seq OWNED BY public.configuracoes_gerais.codigo_versao;


--
-- TOC entry 219 (class 1259 OID 16624)
-- Name: lembretes_id_lembrete_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lembretes_id_lembrete_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lembretes_id_lembrete_seq OWNER TO postgres;

--
-- TOC entry 3393 (class 0 OID 0)
-- Dependencies: 219
-- Name: lembretes_id_lembrete_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lembretes_id_lembrete_seq OWNED BY public.lembretes.id_lembrete;


--
-- TOC entry 216 (class 1259 OID 16599)
-- Name: meditacao_guiada; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.meditacao_guiada (
    codigo_de_plano integer NOT NULL,
    concentracao boolean,
    emocoes boolean,
    estresse boolean,
    quem_pratica integer
);


ALTER TABLE public.meditacao_guiada OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16598)
-- Name: meditacao_guiada_codigo_de_plano_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.meditacao_guiada_codigo_de_plano_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meditacao_guiada_codigo_de_plano_seq OWNER TO postgres;

--
-- TOC entry 3394 (class 0 OID 0)
-- Dependencies: 215
-- Name: meditacao_guiada_codigo_de_plano_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.meditacao_guiada_codigo_de_plano_seq OWNED BY public.meditacao_guiada.codigo_de_plano;


--
-- TOC entry 217 (class 1259 OID 16610)
-- Name: relatorio_semana_id_relatorio_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.relatorio_semana_id_relatorio_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relatorio_semana_id_relatorio_seq OWNER TO postgres;

--
-- TOC entry 3395 (class 0 OID 0)
-- Dependencies: 217
-- Name: relatorio_semana_id_relatorio_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.relatorio_semana_id_relatorio_seq OWNED BY public.relatorio_semana.id_relatorio;


--
-- TOC entry 210 (class 1259 OID 16566)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nome character varying,
    peso double precision,
    altura double precision
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16565)
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_id_seq OWNER TO postgres;

--
-- TOC entry 3396 (class 0 OID 0)
-- Dependencies: 209
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- TOC entry 213 (class 1259 OID 16586)
-- Name: yoga_codigo_de_plano_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.yoga_codigo_de_plano_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yoga_codigo_de_plano_seq OWNER TO postgres;

--
-- TOC entry 3397 (class 0 OID 0)
-- Dependencies: 213
-- Name: yoga_codigo_de_plano_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.yoga_codigo_de_plano_seq OWNED BY public.yoga.codigo_de_plano;


--
-- TOC entry 3203 (class 2604 OID 16578)
-- Name: alongamento codigo_de_plano; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alongamento ALTER COLUMN codigo_de_plano SET DEFAULT nextval('public.alongamento_codigo_de_plano_seq'::regclass);


--
-- TOC entry 3208 (class 2604 OID 16642)
-- Name: configuracoes_gerais codigo_versao; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.configuracoes_gerais ALTER COLUMN codigo_versao SET DEFAULT nextval('public.configuracoes_gerais_codigo_versao_seq'::regclass);


--
-- TOC entry 3207 (class 2604 OID 16628)
-- Name: lembretes id_lembrete; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lembretes ALTER COLUMN id_lembrete SET DEFAULT nextval('public.lembretes_id_lembrete_seq'::regclass);


--
-- TOC entry 3205 (class 2604 OID 16602)
-- Name: meditacao_guiada codigo_de_plano; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meditacao_guiada ALTER COLUMN codigo_de_plano SET DEFAULT nextval('public.meditacao_guiada_codigo_de_plano_seq'::regclass);


--
-- TOC entry 3206 (class 2604 OID 16614)
-- Name: relatorio_semana id_relatorio; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relatorio_semana ALTER COLUMN id_relatorio SET DEFAULT nextval('public.relatorio_semana_id_relatorio_seq'::regclass);


--
-- TOC entry 3202 (class 2604 OID 16569)
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- TOC entry 3204 (class 2604 OID 16590)
-- Name: yoga codigo_de_plano; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yoga ALTER COLUMN codigo_de_plano SET DEFAULT nextval('public.yoga_codigo_de_plano_seq'::regclass);


--
-- TOC entry 3373 (class 0 OID 16575)
-- Dependencies: 212
-- Data for Name: alongamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alongamento (codigo_de_plano, alongamento_partesuperior_do_corpo, alongamento_dor_nas_costas, alongamento_parte_inferior_do_corpo, postura_de_crianca, alongamento_peito, alongamento_de_ombros, alongamento_cobra, alongamento_triceps, alongamento_panturrilha, quem_pratica) VALUES (1, true, false, true, false, true, false, true, false, true, 1);
INSERT INTO public.alongamento (codigo_de_plano, alongamento_partesuperior_do_corpo, alongamento_dor_nas_costas, alongamento_parte_inferior_do_corpo, postura_de_crianca, alongamento_peito, alongamento_de_ombros, alongamento_cobra, alongamento_triceps, alongamento_panturrilha, quem_pratica) VALUES (5, true, true, true, true, true, false, false, false, true, 5);
INSERT INTO public.alongamento (codigo_de_plano, alongamento_partesuperior_do_corpo, alongamento_dor_nas_costas, alongamento_parte_inferior_do_corpo, postura_de_crianca, alongamento_peito, alongamento_de_ombros, alongamento_cobra, alongamento_triceps, alongamento_panturrilha, quem_pratica) VALUES (8, true, false, true, false, true, false, true, false, true, 8);
INSERT INTO public.alongamento (codigo_de_plano, alongamento_partesuperior_do_corpo, alongamento_dor_nas_costas, alongamento_parte_inferior_do_corpo, postura_de_crianca, alongamento_peito, alongamento_de_ombros, alongamento_cobra, alongamento_triceps, alongamento_panturrilha, quem_pratica) VALUES (3, true, true, true, true, true, true, true, true, true, 3);
INSERT INTO public.alongamento (codigo_de_plano, alongamento_partesuperior_do_corpo, alongamento_dor_nas_costas, alongamento_parte_inferior_do_corpo, postura_de_crianca, alongamento_peito, alongamento_de_ombros, alongamento_cobra, alongamento_triceps, alongamento_panturrilha, quem_pratica) VALUES (12, true, true, true, true, true, true, true, true, true, 15);


--
-- TOC entry 3383 (class 0 OID 16639)
-- Dependencies: 222
-- Data for Name: configuracoes_gerais; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (1, true, 1);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (2, false, 2);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (3, false, 3);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (5, true, 5);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (6, false, 6);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (7, true, 7);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (8, true, 8);
INSERT INTO public.configuracoes_gerais (codigo_versao, modo_noturno, qual_usuario) VALUES (10, false, 10);


--
-- TOC entry 3381 (class 0 OID 16625)
-- Dependencies: 220
-- Data for Name: lembretes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (1, 'Yoga', true, 1);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (2, 'Meditação Guiada', false, 2);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (3, 'Yoga', true, 3);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (5, 'Meditação Guiada', true, 5);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (6, 'Yoga', false, 6);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (7, 'Meditação Guiada', true, 7);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (8, 'Alongamento', false, 8);
INSERT INTO public.lembretes (id_lembrete, notificacao_atividade, "monitoramento_de_ingestão_de_agua", qual_usuario) VALUES (10, 'Meditação Guiada', false, 10);


--
-- TOC entry 3377 (class 0 OID 16599)
-- Dependencies: 216
-- Data for Name: meditacao_guiada; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.meditacao_guiada (codigo_de_plano, concentracao, emocoes, estresse, quem_pratica) VALUES (1, true, false, true, 1);
INSERT INTO public.meditacao_guiada (codigo_de_plano, concentracao, emocoes, estresse, quem_pratica) VALUES (2, false, false, true, 2);
INSERT INTO public.meditacao_guiada (codigo_de_plano, concentracao, emocoes, estresse, quem_pratica) VALUES (3, false, false, true, 3);
INSERT INTO public.meditacao_guiada (codigo_de_plano, concentracao, emocoes, estresse, quem_pratica) VALUES (5, false, false, true, 5);
INSERT INTO public.meditacao_guiada (codigo_de_plano, concentracao, emocoes, estresse, quem_pratica) VALUES (7, true, false, true, 7);
INSERT INTO public.meditacao_guiada (codigo_de_plano, concentracao, emocoes, estresse, quem_pratica) VALUES (6, false, false, false, 6);


--
-- TOC entry 3379 (class 0 OID 16611)
-- Dependencies: 218
-- Data for Name: relatorio_semana; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (1, 8, 'Necessita realizar o fortalecimento das emoções', 1);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (2, 5, 'Necessita realizar os exercícios de yoga com mais precisão', 2);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (3, 4, 'Necessita realizar o fortalecimento das emoções', 3);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (5, 10, 'Necessita realizar aulas de yoga', 5);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (6, 6, 'Aluno sem nenhuma observação', 6);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (7, 6, 'Aluno sem nenhuma observação', 7);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (8, 4, 'Aluno sem nenhuma observação', 8);
INSERT INTO public.relatorio_semana (id_relatorio, duracao_em_horas, historico, qual_usuario) VALUES (10, 1, 'Aluno sem nenhuma observação', 10);


--
-- TOC entry 3371 (class 0 OID 16566)
-- Dependencies: 210
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (2, 'Marcos', 70, 1.8);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (5, 'Francisco', 55, 1.65);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (6, 'Silva', 68.5, 1.5);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (10, 'Peter', 85, 1.75);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (8, 'Marina Silva Marques', 10, 10);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (12, 'Aristides', 40, 40);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (13, 'Aristides', 40, 40);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (3, 'Livia', 10, 10);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (17, '', 100, 100);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (1, '', 1, 1);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (15, 'gabriel brito da cruz', 100, 100);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (19, 'gabriel hacker', 1, 1);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (7, 'Afnso', 60, 1.8);
INSERT INTO public.usuarios (id, nome, peso, altura) VALUES (20, 'teste', 1, 1);


--
-- TOC entry 3375 (class 0 OID 16587)
-- Dependencies: 214
-- Data for Name: yoga; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (1, true, false, true, false, false, true, true, false, 1);
INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (2, false, false, true, true, false, true, false, false, 2);
INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (3, false, true, false, true, false, true, true, true, 3);
INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (5, false, false, true, false, true, true, true, false, 5);
INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (6, false, false, true, false, true, true, false, false, 6);
INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (7, true, false, true, false, false, true, true, false, 7);
INSERT INTO public.yoga (codigo_de_plano, concentracao_mental, aprimoramento_mental, encolhimento_dos_ombros, inclinacao_para_os_lados, postura_da_esfinge, ponte, bananeira, estocada_crescente, quem_pratica) VALUES (8, true, true, true, true, true, true, true, false, 8);


--
-- TOC entry 3398 (class 0 OID 0)
-- Dependencies: 211
-- Name: alongamento_codigo_de_plano_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alongamento_codigo_de_plano_seq', 16, true);


--
-- TOC entry 3399 (class 0 OID 0)
-- Dependencies: 221
-- Name: configuracoes_gerais_codigo_versao_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.configuracoes_gerais_codigo_versao_seq', 10, true);


--
-- TOC entry 3400 (class 0 OID 0)
-- Dependencies: 219
-- Name: lembretes_id_lembrete_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lembretes_id_lembrete_seq', 10, true);


--
-- TOC entry 3401 (class 0 OID 0)
-- Dependencies: 215
-- Name: meditacao_guiada_codigo_de_plano_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.meditacao_guiada_codigo_de_plano_seq', 14, true);


--
-- TOC entry 3402 (class 0 OID 0)
-- Dependencies: 217
-- Name: relatorio_semana_id_relatorio_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.relatorio_semana_id_relatorio_seq', 10, true);


--
-- TOC entry 3403 (class 0 OID 0)
-- Dependencies: 209
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 25, true);


--
-- TOC entry 3404 (class 0 OID 0)
-- Dependencies: 213
-- Name: yoga_codigo_de_plano_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.yoga_codigo_de_plano_seq', 13, true);


--
-- TOC entry 3212 (class 2606 OID 16580)
-- Name: alongamento alongamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alongamento
    ADD CONSTRAINT alongamento_pkey PRIMARY KEY (codigo_de_plano);


--
-- TOC entry 3222 (class 2606 OID 16644)
-- Name: configuracoes_gerais configuracoes_gerais_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.configuracoes_gerais
    ADD CONSTRAINT configuracoes_gerais_pkey PRIMARY KEY (codigo_versao);


--
-- TOC entry 3220 (class 2606 OID 16632)
-- Name: lembretes lembretes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lembretes
    ADD CONSTRAINT lembretes_pkey PRIMARY KEY (id_lembrete);


--
-- TOC entry 3216 (class 2606 OID 16604)
-- Name: meditacao_guiada meditacao_guiada_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meditacao_guiada
    ADD CONSTRAINT meditacao_guiada_pkey PRIMARY KEY (codigo_de_plano);


--
-- TOC entry 3218 (class 2606 OID 16618)
-- Name: relatorio_semana relatorio_semana_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relatorio_semana
    ADD CONSTRAINT relatorio_semana_pkey PRIMARY KEY (id_relatorio);


--
-- TOC entry 3210 (class 2606 OID 16573)
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- TOC entry 3214 (class 2606 OID 16592)
-- Name: yoga yoga_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yoga
    ADD CONSTRAINT yoga_pkey PRIMARY KEY (codigo_de_plano);


--
-- TOC entry 3223 (class 2606 OID 16581)
-- Name: alongamento alongamento_quem_pratica_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alongamento
    ADD CONSTRAINT alongamento_quem_pratica_fkey FOREIGN KEY (quem_pratica) REFERENCES public.usuarios(id);


--
-- TOC entry 3228 (class 2606 OID 16645)
-- Name: configuracoes_gerais configuracoes_gerais_qual_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.configuracoes_gerais
    ADD CONSTRAINT configuracoes_gerais_qual_usuario_fkey FOREIGN KEY (qual_usuario) REFERENCES public.usuarios(id);


--
-- TOC entry 3227 (class 2606 OID 16633)
-- Name: lembretes lembretes_qual_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lembretes
    ADD CONSTRAINT lembretes_qual_usuario_fkey FOREIGN KEY (qual_usuario) REFERENCES public.usuarios(id);


--
-- TOC entry 3225 (class 2606 OID 16605)
-- Name: meditacao_guiada meditacao_guiada_quem_pratica_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meditacao_guiada
    ADD CONSTRAINT meditacao_guiada_quem_pratica_fkey FOREIGN KEY (quem_pratica) REFERENCES public.usuarios(id);


--
-- TOC entry 3226 (class 2606 OID 16619)
-- Name: relatorio_semana relatorio_semana_qual_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.relatorio_semana
    ADD CONSTRAINT relatorio_semana_qual_usuario_fkey FOREIGN KEY (qual_usuario) REFERENCES public.usuarios(id);


--
-- TOC entry 3224 (class 2606 OID 16593)
-- Name: yoga yoga_quem_pratica_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yoga
    ADD CONSTRAINT yoga_quem_pratica_fkey FOREIGN KEY (quem_pratica) REFERENCES public.usuarios(id);


--
-- TOC entry 3384 (class 0 OID 16650)
-- Dependencies: 223 3386
-- Name: aluno_ativo; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.aluno_ativo;


-- Completed on 2023-07-31 21:33:09

--
-- PostgreSQL database dump complete
--

