import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from funciones import funciones


def punto_fijo(g, f, p0, tol=1e-6, max_iter=100):
    p = p0
    hist_error = []
    for n in range(1, max_iter + 1):
        p_sig = g(p)
        err = abs(p_sig - p)
        hist_error.append(err)

        if err < tol or abs(f(p_sig)) < tol:
            return p_sig, n, err, hist_error

        # control de divergencia
        if abs(p_sig) > 1e10:
            return None, n, err, hist_error

        p = p_sig

    return p, max_iter, err, hist_error


if __name__ == "__main__":
    print("metodo de punto fijo:")
    print("-" * 55)
    for clave, item in funciones.items():
        raiz, it, err, _ = punto_fijo(item["g"], item["f"], item["p0"])
        if raiz is not None and it < 100:
            print(f"{clave:15} | iter: {it:2d} | raiz: {raiz:.7f} | err: {err:.2e}")
        elif raiz is not None:
            print(f"{clave:15} | no converge (llego al tope de iteraciones)")
        else:
            print(f"{clave:15} | diverge")