from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
import ansible_runner

def load_inventory():
    
    # Initialize data loader
    loader = DataLoader()

    # Load inventory from hosts.yml file
    im = InventoryManager(loader=loader, sources=['hosts.yml'])
    vm = VariableManager(loader=loader, inventory=im)
    hosts = im.get_hosts()
    
    for host in hosts:
        host_info = vm.get_vars(host=im.get_host(f'{host}'))
        print(f"\nHost Name: {host}")
        print(f"IP Address: {host_info['ansible_host']}")
        print(f"Ansible Port: {host_info['ansible_port']}")
        print(f"Group names: {host_info['group_names']}")

    print("\nPing hosts:\n")
    ansible_runner.interface.run_command(
        executable_cmd=f"ansible all -i {vm.get_vars(host=im.get_host(f'{hosts[0]}'))['inventory_file']} -m ping",
        envvars={'ANSIBLE_CONFIG': './ansible.cfg'}
        )

if __name__ == "__main__":
    load_inventory()
