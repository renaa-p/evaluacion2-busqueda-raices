import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from funciones import funciones


def newton_mejorado(f, df, d2f, p0, tol=1e-6, max_iter=100):
    # formula para raices multiples: x - (f*df)/(df^2 - f*d2f)
    p = p0
    hist_error = []
    for n in range(1, max_iter + 1):
        fp = f(p)
        dfp = df(p)
        d2fp = d2f(p)
        den = dfp**2 - fp * d2fp

        if den == 0:
            return None, n, None, hist_error

        p_sig = p - (fp * dfp) / den
        err = abs(p_sig - p)
        hist_error.append(err)

        if err < tol or abs(f(p_sig)) < tol:
            return p_sig, n, err, hist_error

        p = p_sig

    return p, max_iter, err, hist_error


if __name__ == "__main__":
    print("metodo de newton-raphson mejorado:")
    print("-" * 55)
    for clave, item in funciones.items():
        raiz, it, err, _ = newton_mejorado(
            item["f"], item["df"], item["d2f"], item["p0"]
        )
        if raiz is not None:
            print(f"{clave:15} | iter: {it:2d} | raiz: {raiz:.7f} | err: {err:.2e}")
        else:
            print(f"{clave:15} | fallo por denominador nulo")