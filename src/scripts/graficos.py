import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from biseccion import biseccion
from falsa_posicion import falsa_posicion
from funciones import funciones
from newton_mejorado import newton_mejorado
from newton_raphson import newton_raphson
from punto_fijo import punto_fijo
from secante import secante

script_dir = os.path.dirname(os.path.abspath(__file__))
raiz_dir = os.path.dirname(script_dir)
assets_dir = os.path.join(raiz_dir, "assets")


def main():
    os.makedirs(assets_dir, exist_ok=True)

    # 1. graficos de funciones con raices marcadas
    for clave, item in funciones.items():
        x_min, x_max = item["rango"]
        xs = np.linspace(x_min, x_max, 300)
        ys = item["f"](xs)

        plt.figure(figsize=(7, 4.5))
        plt.plot(xs, ys, label=f"f(x) = {item['expr']}", color="#1f77b4")
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
        plt.axvline(0, color="gray", linewidth=0.6)

        rz = item["raiz_esperada"]
        if item["es_raiz_doble"]:
            plt.plot(rz, item["f"](rz), "o", color="#d62728", markersize=7, label=f"tangencia x={rz}")
        else:
            plt.plot(rz, item["f"](rz), "o", color="#d62728", markersize=7, label=f"raiz x={rz:.4f}")

        plt.title(f"funcion {clave}: f(x) = {item['expr']}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(assets_dir, f"funcion_{clave}.png"), dpi=120)
        plt.close()

    # 2. graficos de convergencia |error| vs iteracion
    metodos = [
        ("biseccion", lambda itm: biseccion(itm["f"], itm["a"], itm["b"])),
        ("falsa_posicion", lambda itm: falsa_posicion(itm["f"], itm["a"], itm["b"])),
        ("punto_fijo", lambda itm: punto_fijo(itm["g"], itm["f"], itm["p0"])),
        ("secante", lambda itm: secante(itm["f"], itm["p0"], itm["p1"])),
        ("newton_raphson", lambda itm: newton_raphson(itm["f"], itm["df"], itm["p0"])),
        ("newton_mejorado", lambda itm: newton_mejorado(itm["f"], itm["df"], itm["d2f"], itm["p0"])),
    ]

    for clave, item in funciones.items():
        plt.figure(figsize=(8, 5))
        for nombre, fn in metodos:
            _, it, _, hist = fn(item)
            if hist and it > 0:
                plt.plot(range(1, len(hist) + 1), hist, marker="o", markersize=3, label=nombre)

        plt.yscale("log")
        plt.title(f"convergencia |error| vs iteracion - {clave}")
        plt.xlabel("iteracion")
        plt.ylabel("|error| (escala log)")
        plt.grid(True, which="both", alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(assets_dir, f"convergencia_{clave}.png"), dpi=120)
        plt.close()

    # 3. grafico resumen de iteraciones por metodo
    nombres_f = list(funciones.keys())
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x_indices = np.arange(len(nombres_f))
    ancho = 0.13

    for idx, (nombre, fn) in enumerate(metodos):
        iteraciones_lista = []
        for clave in nombres_f:
            item = funciones[clave]
            raiz, it, _, _ = fn(item)
            iteraciones_lista.append(it if raiz is not None else 0)
        ax.bar(x_indices + idx * ancho, iteraciones_lista, ancho, label=nombre)

    ax.set_title("resumen de iteraciones por metodo y funcion")
    ax.set_xlabel("funcion")
    ax.set_ylabel("iteraciones")
    ax.set_xticks(x_indices + ancho * 2.5)
    ax.set_xticklabels(nombres_f)
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, "resumen_iteraciones.png"), dpi=120)
    plt.close()
    print("graficos generados en assets/")


if __name__ == "__main__":
    main()