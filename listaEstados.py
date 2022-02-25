# [0] -> Sigla
# [1] -> Estado
# [2] -> Habitantes
# [3] -> PIB
lista = [
          ["AC","Acre","732.793","8.477.000"],
          ["AL","Alagoas","3.120.922","24.575.000"],
          ["AP","Amapá","668.689","8.266.000"],
          ["AM","Amazonas","3.480.937","59.779.000"],
          ["BA","Bahia","14.021.432","154.340.000"],
          ["CE","Ceara","8.448.055","77.865.000"],
          ["DF","Distrito Federal","2.562.963","149.906.000"],
          ["ES","Espírito Santo","3.512.672","82.122.000"],
          ["GO","Goiás","6.004.045","97.576.000"],
          ["MA","Maranhão","6.569.683","45.256.000"],
          ["MT","Mato Grosso","3.033.991","59.600.000"],
          ["MS","Mato Grosso do Sul","2.449.341","43.514.000"],
          ["MG","Minas Gerais","19.595.309","351.381.000"],
          ["PA","Pará","7.588.078","77.848.000"],
          ["PB","Paraíba","3.766.834","31.947.000"],
          ["PR","Paraná","10.439.601","217.290.000"],
          ["PE","Pernambuco","8.796.032","95.187.000"],
          ["PI","Piauí","3.119.015","22.060.000"],
          ["RJ","Rio de Janeiro","15.993.583","407.123.000"],
          ["RN","Rio Grande do Norte","3.168.133","32.339.000"],
          ["RS","Rio Grande do Sul","10.695.532","252.483.000"],
          ["RO","Rondônia","1.560.501","23.561.000"],
          ["RR","Roraima","451.227","6.341.000"],
          ["SC","Santa Catarina","6.249.682","152.482.000"],
          ["SP","São Paulo","41.252.160","1.247.596.000"],
          ["SE","Sergipe","2.068.031","23.932.000"],
          ["TO","Tocantins","1.383.453","17.240.000"]
        ]

listaOrdenada = []
for x in range(0, len(lista)):
  maiorValor = ["0","0","0","0"]
  for estado in lista:
    populacao = int(estado[2].replace(".",""))
    maiorPopulacao = int(maiorValor[2].replace(".",""))
    if populacao > maiorPopulacao:
      maiorValor = estado
  listaOrdenada.append(maiorValor)
  lista.remove(maiorValor)
print(*listaOrdenada, sep="\n")