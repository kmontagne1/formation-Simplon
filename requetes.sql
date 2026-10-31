SELECT
    SUM(CAST(c3 AS REAL) * CAST(c4 AS INTEGER))
    AS chiffre_affaires_total
FROM ventes
WHERE c1 != 'date';

SELECT c2,
    SUM(CAST(c4 AS INTEGER)) AS quantite_totale,
    SUM(CAST(c3 AS REAL) * CAST(c4 AS INTEGER))
        AS chiffre_affaires
FROM ventes
WHERE c1 != 'date'
GROUP BY c2
ORDER BY chiffre_affaires DESC;

SELECT c5 as Region, 
	SUM(Cast(c4 as INTEGER)) as quantite_totale,
    SUM(Cast(c3 as REAL)* CAST(c4 as INTEGER)) as ca
FROM ventes 
where c1 != 'date'
GROUP BY c5