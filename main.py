import re 
import matplotlib.pyplot as plt

def read(file):

    with open (file, "r") as f:
        result = f.readlines()
    return result

def get_bandwidth(dados):

    bandwidths = []

    for line in dados:

        match = re.search(r'(\d+\.\d+)\s*Mbits/sec', line)

        if match:
            bandwidth = float(match.group(1))
            bandwidths.append(bandwidth)

    return bandwidths

def grafico(bandwidths):
    plt.figure(figsize=(10, 5))
    plt.plot(bandwidths, marker='o')
    plt.title('Largura de Banda ao Longo do Tempo')
    plt.xlabel('Intervalo de Tempo (segundos)')
    plt.ylabel('Largura de Banda (Mbits/sec)')
    plt.grid()
    plt.xticks(range(len(bandwidths)))  # Marcar cada ponto no eixo x
    plt.show()


if __name__ == "__main__":

    path = "iperf3.txt"

    dados = read(path)

    bandwidths = get_bandwidth(dados)

    grafico(bandwidths)