import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from funciones import funciones


def secante(f, p0, p1, tol=1e-6, max_iter=100):
    hist_error = []
    for n in range(1, max_iter + 1):
        f0, f1 = f(p0), f(p1)
        if f1 - f0 == 0:
            return None, n, None, hist_error

        p = p1 - f1 * (p1 - p0) / (f1 - f0)
        err = abs(p - p1)
        hist_error.append(err)

        if err < tol or abs(f(p)) < tol:
            return p, n, err, hist_error

        p0, p1 = p1, p

    return p, max_iter, err, hist_error


if __name__ == "__main__":
    print("metodo de la secante:")
    print("-" * 55)
    for clave, item in funciones.items():
        raiz, it, err, _ = secante(item["f"], item["p0"], item["p1"])
        if raiz is not None:
            print(f"{clave:15} | iter: {it:2d} | raiz: {raiz:.7f} | err: {err:.2e}")
        else:
            print(f"{clave:15} | fallo por division por cero")