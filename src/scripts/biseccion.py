import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from funciones import funciones


def biseccion(f, a, b, tol=1e-6, max_iter=100):
    # verificar cambio de signo (teorema de bolzano)
    if f(a) * f(b) >= 0:
        return None, 0, None, []

    hist_error = []
    p_ant = None
    for n in range(1, max_iter + 1):
        p = (a + b) / 2.0
        fp = f(p)
        err = abs(p - p_ant) if p_ant is not None else abs(b - a)
        hist_error.append(err)

        if abs(fp) < tol or err < tol:
            return p, n, err, hist_error

        if f(a) * fp < 0:
            b = p
        else:
            a = p
        p_ant = p

    return p, max_iter, err, hist_error


if __name__ == "__main__":
    print("metodo de biseccion:")
    print("-" * 55)
    for clave, item in funciones.items():
        raiz, it, err, _ = biseccion(item["f"], item["a"], item["b"])
        if raiz is not None:
            print(f"{clave:15} | iter: {it:2d} | raiz: {raiz:.7f} | err: {err:.2e}")
        else:
            print(f"{clave:15} | no aplica (no hay cambio de signo)")