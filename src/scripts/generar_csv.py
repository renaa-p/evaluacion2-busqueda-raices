import csv
import os
import sys

import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from biseccion import biseccion
from falsa_posicion import falsa_posicion
from funciones import funciones
from newton_mejorado import newton_mejorado
from newton_raphson import newton_raphson
from punto_fijo import punto_fijo
from secante import secante

# resolucion de directorios
script_dir = os.path.dirname(os.path.abspath(__file__))
raiz_dir = os.path.dirname(script_dir)
data_dir = os.path.join(raiz_dir, "data")


def main():
    os.makedirs(data_dir, exist_ok=True)

    # 1. generar csv con x, f(x) por funcion
    for clave, item in funciones.items():
        x_min, x_max = item["rango"]
        xs = np.linspace(x_min, x_max, 100)
        archivo_csv = os.path.join(data_dir, f"{clave}.csv")
        with open(archivo_csv, "w", newline="", encoding="utf-8") as f_out:
            escritor = csv.writer(f_out)
            escritor.writerow(["x", "f(x)"])
            for x in xs:
                escritor.writerow([f"{x:.6f}", f"{item['f'](x):.6f}"])
        print(f"csv generado: {clave}.csv")

    # 2. generar csv resumen de convergencia
    resumen_path = os.path.join(data_dir, "resumen_convergencia.csv")
    metodos = [
        ("biseccion", lambda item: biseccion(item["f"], item["a"], item["b"])),
        ("falsa_posicion", lambda item: falsa_posicion(item["f"], item["a"], item["b"])),
        ("punto_fijo", lambda item: punto_fijo(item["g"], item["f"], item["p0"])),
        ("secante", lambda item: secante(item["f"], item["p0"], item["p1"])),
        ("newton_raphson", lambda item: newton_raphson(item["f"], item["df"], item["p0"])),
        ("newton_mejorado", lambda item: newton_mejorado(item["f"], item["df"], item["d2f"], item["p0"])),
    ]

    with open(resumen_path, "w", newline="", encoding="utf-8") as f_out:
        escritor = csv.writer(f_out)
        escritor.writerow(["funcion", "metodo", "iteraciones", "raiz", "error", "estado"])

        for clave, item in funciones.items():
            for nombre_metodo, ejecutar in metodos:
                raiz, it, err, _ = ejecutar(item)
                if raiz is None and it == 0:
                    estado = "no aplica"
                    r_str, err_str = "n/a", "n/a"
                elif raiz is None:
                    estado = "diverge"
                    r_str, err_str = "n/a", f"{err:.2e}" if err else "n/a"
                elif it >= 100:
                    estado = "tope maximo"
                    r_str, err_str = f"{raiz:.7f}", f"{err:.2e}"
                else:
                    estado = "converge"
                    r_str, err_str = f"{raiz:.7f}", f"{err:.2e}"

                escritor.writerow([clave, nombre_metodo, it, r_str, err_str, estado])

    print("csv resumen generado: resumen_convergencia.csv")


if __name__ == "__main__":
    main()