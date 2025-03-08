from datetime import date, time, datetime
from subprocess import Popen, run
from tkinter import *

agora = datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second

#A variável code deve ser uma lista que contém, no primeiro item, uma variável booleana que decide se o código será executado como se fosse
#parte do código Main.py, ou se será executado em uma janela separada, no segundo item, o nome do arquivo a ser executado e, no terceiro item,
#o caminho para o arquivo em questão.
def runcode(code):
    pypath = r"C:\Caminho\Para\python.exe"
    if code[0]:
        Popen([pypath] + [f"{code[1]}"], cwd=fr"{code[2]}")
    else:
        run([pypath] + [f"{code[1]}"], cwd=fr"{code[2]}")

#Calcula o delta em segundos de um horário do dia em relação ao início do dia.
def timetint(h, m, s):
    momento = time(h, m, s).hour * 3600 + time(h, m, s).minute * 60 + time(h, m, s).second
    return momento

#Cancela o desligamento automático do computador
def cancel():
    run('shutdown /a')
    interface.destroy()


#Define hoje
hoje = date.today()

#Lê o último dia em que o código foi executado
with open('Dados/last.txt', 'r') as arquivo:
    ultima = arquivo.read()
ultima = datetime.strptime(ultima, "%Y-%m-%d").date()

#Define o último dia como hoje
with open('Dados/last.txt', 'w') as arquivo:
    arquivo.write(f"{hoje}")

#Verificar tarefas a executar, com base nos dias da semana e no último dia em que o código foi executado.
days = [0, 1, 2, 3, 4, 5, 6]
delta = (hoje - ultima).days

diasemana = hoje.weekday()

if delta >= 7:
    pass

else:
    if delta>diasemana: days = days[diasemana::-1][0:delta] + days[:diasemana-delta:-1]
    else: days = days[diasemana::-1][0:delta]

#Executa os códigos

#Executa um código diariamente
if hoje != ultima:
    pass

#Executa um código semanalmente, na segunda-feira
if 0 in days:
    pass
    # Exemplo de linha de comando que substituiria o pass abaixo:
    #runcode([False, "arquivo.py",r"C:\Caminho\Para\Arquivo"])

#Executa um código semanalmente, na terça-feira
if 1 in days:
    pass

#Executa um código semanalmente, na quarta-feira
if 2 in days:
    pass

#Executa um código semanalmente, na quinta-feira
if 3 in days:
    pass

#Executa um código semanalmente, na sexta-feira
if 4 in days:
    pass

#Executa um código semanalmente, no sábado
if 5 in days:
    pass

#Executa um código semanalmente, no domingo
if 6 in days:
    pass

#Se agora for antes das 8h30, será programado um timer de cinco minutos que desligará o computador, mas, enquanto o computador não desligar,
#haverá um botão com a opção de cancelar o desligamento.
if agora < timetint(8, 30, 0):
    run('shutdown /s /t 300')
    interface = Tk()
    botao = Button(interface, text=f"Não desligar", command=cancel)
    botao.grid(column=0, row=2, pady=20, padx=50)
    interface.mainloop()
