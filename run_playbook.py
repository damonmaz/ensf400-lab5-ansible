import ansible_runner

def run_playbook():
    
    runner = ansible_runner.interface.run(
        playbook="/workspaces/ensf400-lab5-ansible/hello.yml", 
        envvars={'ANSIBLE_CONFIG': './ansible.cfg'},
        inventory="/workspaces/ensf400-lab5-ansible/hosts.yml",
        # ssh_key="/workspaces/ensf400-lab5-ansible/secrets/id_rsa",
        )
        
if __name__ == "__main__":
    run_playbook()
