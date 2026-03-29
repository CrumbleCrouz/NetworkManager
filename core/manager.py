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
    print(f"{'Index':<7} {'Name'}")
    print("-" * 40)

    for adapter in all_adapters:
        pnp_id = adapter.PNPDeviceID or ""

        is_virtual = any(word in (adapter.Name + adapter.Description).lower()
                         for word in config["excludedAdapters"])


        if adapter.NetConnectionID and not is_virtual and pnp_id.startswith(("PCI\\", "USB\\")):
            # print(f"[{adapter.Index:<5}] {adapter.NetConnectionID:<25} ({adapter.Name})")
            real_adapters.append(adapter)

    return real_adapters
        