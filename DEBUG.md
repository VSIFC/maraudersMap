# WiFi Scanner Tool

This tool scans a WiFi network to list connected devices using API or SNMP. Below are instructions for determining the API endpoint and OID for ARP tables if they are not readily available.

---

## Determining the API Endpoint (`API_URL`)

### 1. Network Scanning
- Use `nmap` to scan the router for open ports and services:
  ```bash
  nmap -sV -p- 192.168.1.1
  ```
- Look for HTTP/HTTPS services (e.g., ports 80, 443, or custom ports). These often host the router's API.

### 2. Directory Bruteforcing
- Use tools like `ffuf` or `dirb` to brute-force common API paths:
  ```bash
  ffuf -u http://192.168.1.1/FUZZ -w /usr/share/wordlists/dirb/common.txt
  ```
- Replace `192.168.1.1` with the router's IP address. Look for paths like `/api/devices`, `/status`, or `/connected_devices`.

### 3. Intercept Router Web Interface
- Log in to the router's admin panel (e.g., `http://192.168.1.1`) and use a proxy tool like [Burp Suite](https://portswigger.net/burp) or [OWASP ZAP](https://owasp.org/www-project-zap/) to intercept HTTP requests.
- Look for API calls made by the web interface, such as:
  ```
  GET /api/devices HTTP/1.1
  Host: 192.168.1.1
  ```

### 4. Default API Patterns
- Test common API paths manually:
  ```bash
  curl -u admin:password http://192.168.1.1/api/devices
  curl -u admin:password http://192.168.1.1/connected_devices
  curl -u admin:password http://192.168.1.1/status
  ```
- Replace `admin` and `password` with default or known credentials.

---

## Determining the OID for ARP Table

### 1. SNMP Walk
- Use `snmpwalk` to enumerate all available OIDs:
  ```bash
  snmpwalk -v 2c -c public 192.168.1.1
  ```
- Replace `public` with the SNMP community string (default is often `public`).

### 2. Focus on ARP Table OIDs
- Common OIDs for ARP tables include:
  - `1.3.6.1.2.1.4.22.1.2` (MAC addresses)
  - `1.3.6.1.2.1.4.22.1.3` (IP addresses)
- Test these directly:
  ```bash
  snmpwalk -v 2c -c public 192.168.1.1 1.3.6.1.2.1.4.22.1.2
  ```

### 3. MIB Exploration
- Use an SNMP MIB browser (e.g., [iReasoning MIB Browser](https://www.ireasoning.com/mibbrowser.shtml)) to explore the router's SNMP data.
- Load standard MIB files (e.g., `RFC1213-MIB`) to identify OIDs for connected devices.

### 4. Brute-Force OIDs
- Use tools like `onesixtyone` or custom scripts to brute-force OIDs:
  ```bash
  onesixtyone -c public 192.168.1.1
  ```

---

## Exploiting Default Configurations
- Many routers use default credentials and configurations. Test common credentials (e.g., `admin:admin`, `admin:password`) to access the API or SNMP data.
- Use tools like `hydra` or `medusa` to brute-force credentials if necessary.

---

## Automating Discovery

### API Discovery
- Use tools like [Postman](https://www.postman.com/) or [Swagger Inspector](https://swagger.io/tools/swagger-inspector/) to scan for API endpoints.

### SNMP Enumeration
- Use tools like `snmp-check` or `snmpenum` to automate SNMP enumeration:
  ```bash
  snmp-check -t 192.168.1.1 -c public
  ```

---

## Leveraging Public Databases
- Search for your router model in public vulnerability databases or forums. Other pentesters may have already documented the API endpoints or OIDs:
  - [Exploit-DB](https://www.exploit-db.com/)
  - [CVE Details](https://www.cvedetails.com/)
  - [RouterPasswords](https://www.routerpasswords.com/)

---

## Example Workflow
1. **Scan for Open Ports**:
   ```bash
   nmap -sV -p- -Pn 192.168.1.1
   ```
2. **Intercept Web Traffic**:
   - Use Burp Suite to capture API calls.
3. **Enumerate SNMP**:
   ```bash
   snmpwalk -v 2c -c public 192.168.1.1
   ```
4. **Test Common API Paths**:
   ```bash
   curl -u admin:password http://192.168.1.1/api/devices
   ```

By combining these techniques, you can often determine the API endpoint and OID without needing external support.