# Python Modules
import re

# External Modules
import wmi


def list_adapters(config: dict) -> list:
    """
    Lists all adapters not excluded.
    :param config: The program configuration.
    :return: A List of adapters.
    """
    c = wmi.WMI()
    all_adapters = c.Win32_NetworkAdapter(PhysicalAdapter=True)
    adapters = []

    for adapter in all_adapters:

        is_excluded = any(word in (adapter.Name + adapter.Description).lower()
                         for word in config["excludedAdapters"])


        if adapter.NetConnectionID and not is_excluded:
            adapters.append(adapter)
    return adapters


def get_adapter_details(adapter: wmi.WMIObject) -> dict | None:
    """
    Gets the details of an adapter.
    :param adapter: The adapter.
    :return: The details of the adapter or None if not found.
    """
    c = wmi.WMI()

    configs = c.Win32_NetworkAdapterConfiguration(Index=adapter.Index)

    if not configs:
        return None

    config = configs[0]

    return {
        "IP": config.IPAddress[0] if config.IPAddress else "N/A",
        "Subnet": config.IPSubnet[0] if config.IPSubnet else "N/A",
        "Gateway": config.DefaultIPGateway[
            0] if config.DefaultIPGateway else "N/A",
        "DNS": ", ".join(
            config.DNSServerSearchOrder) if config.DNSServerSearchOrder else "N/A",
        "DHCP": "Enabled (Dynamic)" if config.DHCPEnabled else "Disabled (Static)"
    }


def verify_ip(ip: str) -> bool:
    """
    Verifies if an IP is valid.
    :param ip: The IP to verify.
    :return: True if the IP is valid, False otherwise.
    """
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, ip) is not None


def verify_configuration(config: dict) -> bool:
    """
    Validates the network configuration settings.
    :param config: The configuration dictionary to verify.
    :return: True if the configuration is valid, False otherwise.
    """
    if config["DHCP"] is True:
        return True

    if not isinstance(config["IP"], str) or not verify_ip(config["IP"]):
        return False

    if not isinstance(config["Mask"], str) or not verify_ip(config["Mask"]):
        return False

    if config["Gateway"] is not None:
        if not verify_ip(config["Gateway"]):
            return False

    for dns_ip in config["DNS"]:
        if not isinstance(dns_ip, str) or not verify_ip(dns_ip):
            return False

    return True