# SELECT/INSERT from nao_portados

INSERT INTO prefixo_novo (operadora,tipo,prefixo,rn1,ddd)
SELECT operadora,tipo,prefixo,rn1,SUBSTRING(prefixo,1,2)  FROM nao_portados;


# Atualiza  ESTADO
UPDATE prefixo_novo rt,
	(
	SELECT estado,prefixo,ddd FROM prefixo
	) rs
	SET
	rt.estado = rs.estado
	WHERE rt.ddd = rs.ddd

# Atualizar CIDADE

UPDATE prefixo_novo rt,
	(
	SELECT cidade,prefixo,ddd FROM prefixo
	) rs
	SET
	rt.cidade = rs.cidade
	WHERE rt.prefixo = rs.prefixo

-- # Junta DDD com prefixo
-- UPDATE prefixo_novo SET prefixo2 = CONCAT(ddd,prefixo)

-- # remove duplicados
-- alter ignore table prefixo_novo add unique idx_prefixo_novo(prefixo)

-- # Atualiza RN1

-- UPDATE prefixo_novo rt,
-- 	(
-- 	SELECT rn1,operadora FROM prefixo
-- 	WHERE tipo = 'MOVEL'
-- 	) rs
-- 	SET
-- 	rt.rn1 = rs.rn1
-- 	WHERE rt.operadora = rs.operadora

-- # Atualiza TIPO
-- UPDATE prefixo_novo SET tipo = 'MOVEL'

-- DELETE FROM prefixo WHERE tipo = 'MOVEL'