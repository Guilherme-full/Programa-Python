import platform

resp = 'SIM'
while resp == 'SIM':
    resp = input('Deseja verificar informações de seu computador?[Sim][Não]: ').upper()
    print('Nome Maquina...................', platform.node())
    print('Arquitetura....................', platform.architecture())
    print('Sistema Operacional............', platform.system())
    print('Versao do SO..................', platform.release())
    print('Processador...................', platform.processor())
    print('Versão do Python .............', platform.python_version())
