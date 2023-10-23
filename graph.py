import plotly.graph_objects as go
import plotly.offline as offline
import random
import os
def plot_multiple_3d_graphs(data_list):
    # Criar a figura
    fig = go.Figure()

    for data in data_list:
        x, y, z, arestas = data
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Adicionar os vértices
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers+text',
            marker=dict(size=4, color=color),
            showlegend=False
        ))

        # Adicionar as arestas
        for aresta in arestas:
            fig.add_trace(go.Scatter3d(
                x=[x[i] for i in aresta],
                y=[y[i] for i in aresta],
                z=[z[i] for i in aresta],
                mode='lines',
                line=dict(color=color, width=3),
                showlegend=False
            ))

    # Definir os intervalos dos eixos (ajuste conforme necessário)
    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-1, 5]),
            yaxis=dict(range=[-1, 4]),
            zaxis=dict(range=[-1, 4]),
        )
    )

    # Definir os intervalos dos eixos
    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[0, 30]),
            yaxis=dict(range=[0, 40]),
            zaxis=dict(range=[0, 50])
        )
    )

    template_dir = os.path.join(os.getcwd(), 'static')
    plot_file = "plot.html"  # Apenas o nome do arquivo, não o caminho absoluto
    plot_path = os.path.join(template_dir, plot_file)
    offline.plot(fig, filename=plot_path, auto_open=False)

    return plot_file
    