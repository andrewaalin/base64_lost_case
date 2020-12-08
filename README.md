# base64_lost_case

Decodes Base64 strings that had their case thrown away (all uppercase was set to lowercase), but with some knowledge about the plaintext (e.g. plaintext was in Title Case with no special characters).
So Python cycles through possibilities to produce multiple possible plaintexts for each string.
