from coordenada import bin_packing
from solution import combinar_coordenadas
from flask import Flask, request, render_template
from graph import plot_multiple_3d_graphs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    solution = None
    if request.method == 'POST':
        altura_bin = float(request.form.get('altura_bin'))
        largura_bin = float(request.form.get('largura_bin'))
        profundidade_bin = float(request.form.get('profundidade_bin'))

        bin_data = {
            "altura": altura_bin,
            "largura": largura_bin,
            "profundidade": profundidade_bin,

        }

        num_caixas = int(request.form.get('num_caixas'))
        caixas = []

        for i in range(1, num_caixas + 1):
            altura_cx = float(request.form.get(f'altura_cx{i}'))
            largura_cx = float(request.form.get(f'largura_cx{i}'))
            profundidade_cx = float(request.form.get(f'profundidade_cx{i}'))
            peso_cx = float(request.form.get(f'peso_cx{i}'))

            caixa_data = {
                "altura": altura_cx,
                "largura": largura_cx,
                "profundidade": profundidade_cx,
                "peso": peso_cx,
            }

            caixas.append(caixa_data)

        solution = bin_packing(bin_data, caixas)
        data_list = combinar_coordenadas(solution, caixas)
        plot_file = plot_multiple_3d_graphs(data_list)
        return render_template('index.html', solution=solution, plot_file=plot_file)
    else:
        return render_template('index.html', solution=solution)

if __name__ == '__main__':
    app.run(debug=True)



