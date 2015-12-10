import ctypes
from math import sqrt
from operator import itemgetter


def _norm_tau(x, R):
    return sqrt(productRS_c(x, x, R.values()))


def _rank_tau(r, s):
    L = tuple(range(0, len(r)))
    S = [None]*len(r)
    for i, item in enumerate(S):
        S[i] = (L[i], r[i], s[i])
    S = sorted(S, key=itemgetter(1, 2), reverse=True)
    rank = {}
    for i, item in enumerate(S):
        rank[item[0]] = i
    return rank


def weightedTau(r, s):
    rs = _rank_tau(r, s)
    sr = _rank_tau(s, r)
    a = productRS_c(r, s, rs.values())/(_norm_tau(r, rs)*_norm_tau(s, rs))
    b = productRS_c(r, s, sr.values())/(_norm_tau(r, sr)*_norm_tau(s, sr))
    return round((a+b)/2, 10)


def createCarray(pyArray):
    cArrayConstructor = ctypes.c_int * len(pyArray)
    cArray = cArrayConstructor()

    for idx, item in enumerate(pyArray):
        cArray[idx] = item

    return cArray


def productRS_c(r, s, R):
    arrayLength = len(r)

    # double productRS(int r[], int s[], int R[], int N)
    try:
        clib = ctypes.CDLL("./productRS.so")
    except OSError:
        clib = ctypes.CDLL("./weightedTau/productRS.so")

    r_c = createCarray(r)
    s_c = createCarray(s)
    R_c = createCarray(R)

    flt = ctypes.c_double(0)
    res = clib.productRS(ctypes.byref(r_c), ctypes.byref(s_c
        ), ctypes.byref(R_c), arrayLength, ctypes.byref(flt))

    return flt.value
