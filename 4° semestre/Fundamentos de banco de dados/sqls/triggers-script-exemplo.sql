create table Estudante(mat SERIAL primary key, nome varchar(20), 
maior_media integer default 0, 
menor_media integer default 0);


create table Exame(mat integer , 
     nota integer,
     disciplina integer,
	 primary key(mat,disciplina),
	 foreign key (mat) references Estudante(mat));

INSERT INTO ESTUDANTE(NOME) VALUES
('Alexandre Silva' ), 
('Bruna Sousa'), 
('Sofia Maria'), 
('Guilherme Nunes');

CREATE or replace FUNCTION verifica_nota_exame() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL

AS $$
   DECLARE 
   		estudantes RECORD;
BEGIN
   	IF NEW.NOTA <0 or NEW.NOTA>10 THEN
		RAISE NOTICE 'Nota inválida! %', NEW.nota;
		RETURN NULL;
	ELSE 
		RETURN NEW;
	END IF;
END;
$$;

CREATE TRIGGER verifica_nota_trigger
BEFORE INSERT ON Exame
FOR EACH ROW
EXECUTE PROCEDURE verifica_nota_exame();


CREATE or replace FUNCTION atualiza_notas_exame() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL
AS $$

BEGIN
   	IF NEW.NOTA >= 7 THEN
		UPDATE ESTUDANTE
		SET MAIOR_MEDIA = MAIOR_MEDIA+1
		WHERE MAT = NEW.MAT;
		RETURN NEW;
	ELSE 
		UPDATE ESTUDANTE
		SET MENOR_MEDIA = MENOR_MEDIA+1
		WHERE MAT = NEW.MAT;
		RETURN NEW;
	END IF;
END;
$$;

CREATE TRIGGER atualiza_notas_trigger
AFTER INSERT ON Exame
FOR EACH ROW
EXECUTE PROCEDURE atualiza_notas_exame();





