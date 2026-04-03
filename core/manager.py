# External Modules
import wmi


def list_physical_adapters(config: dict) -> list:
    """
    Lists all physical adapters.
    :param config: The program configuration.
    :return: A List of physical adapters.
    """
    c = wmi.WMI()
    all_adapters = c.Win32_NetworkAdapter(PhysicalAdapter=True)
    real_adapters = []

    for adapter in all_adapters:
        pnp_id = adapter.PNPDeviceID or ""

        is_virtual = any(word in (adapter.Name + adapter.Description).lower()
                         for word in config["excludedAdapters"])


        if adapter.NetConnectionID and not is_virtual and pnp_id.startswith(("PCI\\", "USB\\")):
            real_adapters.append(adapter)
    return real_adapters


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
