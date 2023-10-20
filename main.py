from coordenada import bin_packing
from solution import combinar_coordenadas
from flask import Flask, request, render_template
from graph import plot_multiple_3d_graphs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    solution = None
    if request.method == 'POST':
      altura_bin  = float(request.form.get('altura_bin'))
      largura_bin  = float(request.form.get('largura_bin'))
      profundidade_bin  = float(request.form.get('profundidade_bin'))
      peso_bin  = float(request.form.get('peso_bin'))
      bin = {"altura": altura_bin,
             "largura": largura_bin,
             "profundidade": profundidade_bin,
             "peso": peso_bin,
             }

      altura_cx1  = float(request.form.get('altura_cx1'))
      largura_cx1  = float(request.form.get('largura_cx1'))
      profundidade_cx1  = float(request.form.get('profundidade_cx1'))
      peso_cx1  = float(request.form.get('peso_cx1'))
      cx1 = {
            "altura": float(altura_cx1),
            "largura": float(largura_cx1),
            "profundidade": float(profundidade_cx1),
            "peso": float(peso_cx1),
        }

      altura_cx2  = float(request.form.get('altura_cx2'))
      largura_cx2  = float(request.form.get('largura_cx2'))
      profundidade_cx2  = float(request.form.get('profundidade_cx2'))
      peso_cx2  = float(request.form.get('peso_cx2'))
      cx2 = {
            "altura": float(altura_cx2),
            "largura": float(largura_cx2),
            "profundidade": float(profundidade_cx2),
            "peso": float(peso_cx2),
        }
      caixas = [cx1, cx2]
      solution = bin_packing(bin,caixas)
      data_list = combinar_coordenadas(solution, caixas)
      plot_file = plot_multiple_3d_graphs(data_list)
      return render_template('index.html', solution=solution, plot_file=plot_file)
    else:
        return render_template('index.html', solution=solution)
if __name__ == '__main__':
    app.run(debug=True)