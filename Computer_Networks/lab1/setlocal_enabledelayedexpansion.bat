setlocal enabledelayedexpansion
@echo off
chcp 65001
set /p choice="Выберите способ настройки сетевого интерфейса (1 - автоматически, 2 - статически): "

if %choice%==1 (
    netsh interface ipv4 set address name="Беспроводная сеть" dhcp
    netsh interface ipv4 set dns name="Беспроводная сеть" dhcp
) else if %choice%==2 (
    echo IP адреса:
    netsh interface ipv4 show ipaddresses "Беспроводная сеть" normal
    echo DNS адреса:
    netsh interface ipv4 show dnsservers "Беспроводная сеть"
    echo ------------------------------

    set /p ip="Введите IP адрес: "
    set /p mask="Введите маску подсети: "
    set /p gateway="Введите шлюз: "
    set /p dns="Введите DNS сервер: "

    netsh interface ipv4 set address name="Беспроводная сеть" static !ip! !mask! !gateway!
    netsh interface ipv4 set dnsservers name="Беспроводная сеть" static address=!dns!
    echo IP адреса:
    netsh interface ipv4 show ipaddresses "Беспроводная сеть" normal
    echo DNS адреса:
    netsh interface ipv4 show dnsservers "Беспроводная сеть"
    echo ------------------------------
) else (
    echo Некорректный выбор
)

pause