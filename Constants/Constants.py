# Constants Command DML´s 
SELECT_REGISTERS         = 'SELECT * FROM t_logredo ORDER BY ID'
CREATE_TABLE             = 'CREATE TABLE t_logredo (ID INTEGER PRIMARY KEY, A INTEGER NULL, B INTEGER NULL)'
DROP_TABLE               = 'DROP TABLE IF EXISTS t_logredo'

# Directory Files
DIRECTORY_METADADO       = 'C:\metadado.json'
DIRECTORY_ARCHIVE_LOG    = 'C:\entradaLog'

# Search and remove Strings
STRING_COMMIT            = '^<commit .+>'
STRING_COMMIT_REMOVE     = '<commit|>'

STRING_CHECKPOINT        = '^<CKPT\s*\\(.*\\)\s*>'
STRING_CHECKPOINT_REMOVE = '<CKPT\s*\\(|\\)\s*>|'

STRING_START             = '^<start .+>'
STRING_START_REMOVE      = '<start|>'

STRING_VALUES            = '^<.+,.+,.+,.+,.+>'
STRING_VALUES_REMOVE     = '<|>|'

# Compare String
global TRANSACTION
TRANSACTION = ''

global FALSE
FALSE = False