# FrekvensregisteretDK
Scripts og filer til analyse af frekvensregisteret, der ligger på ens.dk (Energistyrfelsens hjemmeside). 
En ods fil med brutto registeroplysninger er Frekvensregisteret29112023.ods, medens 
Frekvensregisteret29112023_stacked.ods er en del af denne fil baseret på Tilladelsestype og ikke Tilladelsesgruppe, hvor der er mere ufuldstændige oplysninger. Sidstnævnte fil kan benyttes i sammenhæng med python scriptet stackODSsheet.py til at samle ark med samme tabelformat til en tabel, hvilket er input til første anvendelse af skriptet frekvensregisterFrekvensOpslag.py nedenfor. (python stackODSsheets Frekvensregisteret29112023_stacked.ods Frekvensreg.ods)

Scriptet 
python frekvensregisterFrekvensOpslag.py Frekvensreg.ods Opslag805.ods 805.0

Skulle gerne give det samme resultat, som skriptet
python frekvensregisterFrekvensOpslag.py Frekvensregisteret29112023_stacked.ods Opslag805_2.ods 805.0
