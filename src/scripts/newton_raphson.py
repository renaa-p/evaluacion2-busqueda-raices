import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from funciones import funciones


def newton_raphson(f, df, p0, tol=1e-6, max_iter=100):
    p = p0
    hist_error = []
    for n in range(1, max_iter + 1):
        dfp = df(p)
        if dfp == 0:
            return None, n, None, hist_error

        p_sig = p - f(p) / dfp
        err = abs(p_sig - p)
        hist_error.append(err)

        if err < tol or abs(f(p_sig)) < tol:
            return p_sig, n, err, hist_error

        p = p_sig

    return p, max_iter, err, hist_error


if __name__ == "__main__":
    print("metodo de newton-raphson:")
    print("-" * 55)
    for clave, item in funciones.items():
        raiz, it, err, _ = newton_raphson(item["f"], item["df"], item["p0"])
        if raiz is not None:
            print(f"{clave:15} | iter: {it:2d} | raiz: {raiz:.7f} | err: {err:.2e}")
        else:
            print(f"{clave:15} | fallo por derivada nula")