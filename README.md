# FrekvensregisteretDK
Scripts og filer til analyse af frekvensregisteret, der ligger på ens.dk (Energistyrfelsens hjemmeside). 
En ods fil med brutto registeroplysninger er Frekvensregisteret29112023.ods, medens 
Frekvensregisteret29112023_stacked.ods er en del af denne fil baseret på Tilladelsestype og ikke Tilladelsesgruppe, hvor der er mere ufuldstændige oplysninger. Sidstnævnte fil kan benyttes i sammenhæng med python scriptet stackODSsheet.py til at samle ark med samme tabelformat til en tabel, hvilket er input til første anvendelse af skriptet frekvensregisterFrekvensOpslag.py nedenfor. (python stackODSsheets Frekvensregisteret29112023_stacked.ods Frekvensreg.ods)

Scriptet 
python frekvensregisterFrekvensOpslag.py Frekvensreg.ods Opslag805.ods 805.0

Skulle gerne give det samme resultat, som skriptet
python frekvensregisterFrekvensOpslag.py Frekvensregisteret29112023_stacked.ods Opslag805_2.ods 805.0

Dette opslag fortæller, at frekvensen 805MHz er registreret på 5 tilladelser (alle private licenser) 

Tilladelsesnummer / Kaldesignal	Frekvenser(sende) in MHz	Frekvenser(modtage) in MHz	Navn	Tilladelsestype	Bynavn

H101666 - 1	791 - 811	832 - 852	TotalEnergies EP Danmark A/S	Tjeneste- og teknologineutra-letilladelser	Nordsøen

H101666 - 2	791 - 811	832 - 852	TotalEnergies EP Danmark A/S	Tjeneste- og teknologineutra-letilladelser	Nordsøen

H101666 - 3	791 - 811	832 - 852	TotalEnergies EP Danmark A/S	Tjeneste- og teknologineutra-letilladelser	Nordsøen

H100620 - 1	801 - 821	842 - 862	TDC NET A/S	                  Tjeneste- og teknologineutra-letilladelser	

H102130 - 1	801 - 811	842 - 852	Tampnet AS	                  Tjeneste- og teknologineutra-letilladelser	Nordsøen

