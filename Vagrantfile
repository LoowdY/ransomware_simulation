Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "Simulacao-Ransomware"
    vb.memory = 2048
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    echo "Configurando ambiente de simulação..."
    sudo apt update
    sudo apt install -y python3 python3-pip mailutils
    pip3 install cryptography
    echo "Ambiente pronto."
  SHELL

  config.vm.post_up_message = "Snapshot será salvo após boot inicial."

  # Automatiza o snapshot pós-criação da VM
  config.trigger.after :up do |trigger|
    trigger.name = "Snapshot inicial"
    trigger.run = {
      inline: "VBoxManage snapshot Simulacao-Ransomware take snapshot_inicial --description 'Snapshot antes da simulação'"
    }
  end
end
