from sqlparse import tokens


KEYWORDS = {
    'ADD': tokens.Keyword,
    'AFTER': tokens.Keyword,
    'ALL': tokens.Keyword,
    'ALTER': tokens.Keyword.DDL,
    'ARRAY': tokens.Keyword,
    'AS': tokens.Keyword,
    'ATTACH': tokens.Keyword.DDL,
    'BY': tokens.Keyword,
    'CASE': tokens.Keyword,
    'CHECK': tokens.Keyword.DDL,
    'COLUMN': tokens.Keyword,
    'COORDINATE': tokens.Keyword,
    'COPY': tokens.Keyword,
    'CREATE': tokens.Keyword.DDL,
    'DATABASE': tokens.Keyword,
    'DATABASES': tokens.Keyword,
    'DESC': tokens.Keyword,
    'DESCRIBE': tokens.Keyword.DDL,
    'DETACH': tokens.Keyword.DDL,
    'DISTINCT': tokens.Keyword,
    'DROP': tokens.Keyword.DDL,
    'ELSE': tokens.Keyword,
    'END': tokens.Keyword,
    'EXISTS': tokens.Keyword,
    'FETCH': tokens.Keyword,
    'FINAL': tokens.Keyword,
    'FORMAT': tokens.Keyword,
    'FREEZE': tokens.Keyword,
    'FROM': tokens.Keyword,
    'FULL': tokens.Keyword,
    'GLOBAL': tokens.Keyword,
    'GROUP': tokens.Keyword,
    'HAVING': tokens.Keyword,
    'INNER': tokens.Keyword,
    'INSERT': tokens.Keyword.DML,
    'INTO': tokens.Keyword,
    'JOIN': tokens.Keyword,
    'KEY': tokens.Keyword,
    'LEFT': tokens.Keyword,
    'LIKE': tokens.Keyword,
    'LIMIT': tokens.Keyword,
    'MATERIALIZED': tokens.Keyword,
    'MODIFY': tokens.Keyword,
    'NAME': tokens.Keyword,
    'NOT': tokens.Keyword,
    'ON': tokens.Keyword,
    'OPTIMIZE': tokens.Keyword.DDL,
    'ORDER': tokens.Keyword,
    'OUTER': tokens.Keyword,
    'PART': tokens.Keyword,
    'PARTITION': tokens.Keyword,
    'POPULATE': tokens.Keyword,
    'PREWHERE': tokens.Keyword,
    'PRIMARY': tokens.Keyword,
    'RENAME': tokens.Keyword.DDL,
    'RESHARD': tokens.Keyword,
    'SELECT': tokens.Keyword.DML,
    'SETTINGS': tokens.Keyword,
    'SHOW': tokens.Keyword.DDL,
    'TABLE': tokens.Keyword,
    'TABLES': tokens.Keyword,
    'TEMPORARY': tokens.Keyword,
    'THEN': tokens.Keyword,
    'TO': tokens.Keyword,
    'TOTALS': tokens.Keyword,
    'UNION': tokens.Keyword,
    'UNREPLICATED': tokens.Keyword,
    'USING': tokens.Keyword,
    'VALUES': tokens.Keyword,
    'VIEW': tokens.Keyword,
    'WHEN': tokens.Keyword,
    'WHERE': tokens.Keyword,
    'WITH': tokens.Keyword,
}
