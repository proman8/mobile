import csv, sys, subprocess
import plotly.graph_objects as go
from io import StringIO

def calculate(dump, ip):
    traffic = 0
    for elem in dump:
        if elem[1].find(ip) != -1: traffic_str = elem[2]
        if traffic_str.find('M') == -1: traffic += int(traffic_str)
        else: traffic += float(traffic_str[:traffic_str.find('M')]) * 1024 * 1024
    traffic = traffic / 1024
    traffic -= 1000 if traffic >= 1000 else traffic
    
    return '%.2f' % (traffic * 0.5)     

def main():
    if len(sys.argv) != 3: exit()
    
    dump = subprocess.check_output(f"nfdump -r {sys.argv[1]} -o 'fmt:%ts,%sap,%ibyt' 'src ip {sys.argv[2]}'",shell=True)
    
    file_csv = StringIO(dump.decode("ascii"))
    csv_list = list(csv.reader(file_csv,delimiter=","))[1:-4]
    cost = calculate(csv_list,sys.argv[2])
    print(cost)

    ts = [elem[0] for elem in csv_list]
    ibyt = [elem[2] for elem in csv_list]

    fig = go.Figure(data=go.Scatter(x=ts, y=ibyt,mode='markers'))    
    fig.show()

if __name__ == '__main__':
    main()