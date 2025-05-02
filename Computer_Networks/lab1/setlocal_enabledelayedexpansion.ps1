chcp 65001
# Определение функции для отображения текущих настроек
function PrivateSettings {
    Write-Host "Текущие настройки:"
    ipconfig /all | Select-String -Pattern "Имя сетевого адаптера", "IPv4-адрес", "Маска подсети", "Шлюз по умолчанию", "DNS-сервер" | ForEach-Object { $_.ToString().Trim() }
    
    # Получение информации о сетевой карте
    $wmiInfo = Get-WmiObject -Class Win32_NetworkAdapter | Select-Object Name, AdapterType, MACAddress
    #  Get-NetAdapter | Select-Object -Property Name, InterfaceDescription
    # Получение информации о подключении и скорости работы адаптера
    # Get-NetAdapterAdvancedProperty -Name "Беспроводная сеть" | Select-Object -ExpandProperty DisplayValue
    $netInfo = Get-NetAdapter | Select-Object -Property Name, LinkSpeed, Duplex

    $wmiInfo | Format-Table
    $netInfo | Format-Table
}

# Основной код скрипта
Write-Host "Выберите режим настройки сетевого интерфейса:"
Write-Host "1. Получение настроек через DHCP"
Write-Host "2. Ввод настроек вручную"

$choice = Read-Host "Введите номер режима (1 или 2): "

if ($choice -eq "1") {
    # Получение настроек через DHCP
    netsh interface ipv4 set address name="Беспроводная сеть" dhcp
    netsh interface ipv4 set dns name="Беспроводная сеть" dhcp
    netsh interface set interface "Беспроводная сеть" disable
    netsh interface set interface "Беспроводная сеть" enable
    Write-Host "DHCP-настройки успешно применены."
    PrivateSettings
} elseif ($choice -eq "2") {
    # Вывод актуального IP и DNS
    Write-Host IP адреса:
    netsh interface ipv4 show ipaddresses "Беспроводная сеть" normal
    Write-Host DNS адреса:
    netsh interface ipv4 show dnsservers "Беспроводная сеть"
    # Ввод настроек вручную
    $ip = Read-Host "Введите IP-адрес: "
    $mask = Read-Host "Введите маску подсети: "
    $gateway = Read-Host "Введите шлюз по умолчанию: "
    $dns = Read-Host "Введите адрес DNS-сервера: "
    netsh interface ipv4 set address name="Беспроводная сеть" static $ip $mask $gateway
    netsh interface ipv4 set dns "Беспроводная сеть" static $dns
    Write-Host "Статические настройки успешно применены."
    PrivateSettings
} else {
    Write-Host "Неверный выбор."
}