$API_URL = "http://tuserver:5000/api"
$TOKEN = "SECRET_CLIENT_TOKEN"

# Registrar cliente
$hostname = $env:COMPUTERNAME
$ip = (Get-NetIPAddress | Where-Object {
    $_.AddressFamily -eq 'IPv4' -and $_.PrefixOrigin -ne 'WellKnown'
}).IPAddress | Select-Object -First 1

$body = @{
    name = $hostname
    ip = $ip
    os = "Windows"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "$API_URL/clients/register" `
    -Method POST `
    -Headers @{"Authorization" = "Bearer $TOKEN"} `
    -ContentType "application/json" `
    -Body $body

$clientId = $response.client_id

# Polling
while ($true) {
    $response = Invoke-RestMethod -Uri "$API_URL/deployments/$clientId" `
        -Headers @{"Authorization" = "Bearer $TOKEN"}
    
    if ($response.playbook) {
        # Descargar y ejecutar playbook
        Invoke-WebRequest -Uri "$API_URL/playbooks/$($response.playbook)" `
            -OutFile "$env:TEMP\deploy.yml"
        ansible-playbook -i "localhost," "$env:TEMP\deploy.yml"
    }
    
    Start-Sleep -Seconds 300  # Espera 5 minutos
}