# Docker ClamAV

## Usage
Below are two examples of how to start the ClamAV container and send files to it. The first example sends the `EICAR.txt` file. This is a well-known file used to verify anti-virus programs are working. The second file is Mimikatz, a well-known credential dumper. It should trigger most anti-virus programs (e.g., Windows Defender and ClamAV). 

### Example 1
**Step 1.** Start the container from the root of the repository using Docker Compose. 
```bash
docker compose -f compose.yml up --build
```

**Step 2.** Send a file to the `api/v1/scan` endpoint using a HTTP POST request.
```bash
curl -X POST http://localhost:8000/api/v1/scan -F "file=@tests/EICAR.txt"
```

You should get output similar to below. 
```json
{"args":["clamdscan","EICAR.txt"],"returncode":1,"stdout":"/run/clamav/EICAR.txt: Win.Test.EICAR_HDB-1 FOUND\n\n----------- SCAN SUMMARY -----------\nInfected files: 1\nTime: 0.003 sec (0 m 0 s)\nStart Date: 2024:06:25 02:09:35\nEnd Date:   2024:06:25 02:09:35\n","stderr":null}
```

### Example 2
**Step 1.** Download Mimikatz.
```bash
bash tests/get-mimikatz.sh
```

**Step 2.** Send Mimikatz to the `api/v1/scan` endpoint using a HTTP POST request.
```bash
curl -X POST http://localhost:8000/api/v1/scan -F "file=@tests/mimikatz.exe"
```

You should get output similar to below.
```json
{"args":["clamdscan","mimikatz.exe"],"returncode":1,"stdout":"/run/clamav/mimikatz.exe: Win.Dropper.Mimikatz-9778171-1 FOUND\n\n----------- SCAN SUMMARY -----------\nInfected files: 1\nTime: 1.172 sec (0 m 1 s)\nStart Date: 2024:06:25 02:08:30\nEnd Date:   2024:06:25 02:08:32\n","stderr":null}
```

## Copyright
This project is licensed under the terms of the [MIT license](/LICENSE).
