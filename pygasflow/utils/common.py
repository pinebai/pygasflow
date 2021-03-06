import numpy as np

def convert_to_ndarray(x):
    """
    Check if the input parameter is of type np.ndarray.
    If not, convert it to np.ndarray and make sure it is at least 
    1 dimensional.
    """
    if not isinstance(x, np.ndarray):
        return np.atleast_1d(np.array(x, copy=False, dtype=np.float64))
    if x.ndim == 0:
        return np.atleast_1d(np.array(x, copy=False, dtype=np.float64))
    return x

class Ideal_Gas(object):
    def __init__(self, R=287.058, gamma=1.4):
        self._R = R
        self._gamma = gamma
        self._cp = self._gamma * self._R / (self._gamma - 1)
        self._cv = self._cp - R
    
    @property
    def R(self):
        return self._R
    
    @property
    def gamma(self):
        return self._gamma
    
    @property
    def cp(self):
        return self._cp
    
    @property
    def cv(self):
        return self._cv    
    
    def solve(self, **args):
        assert args, "Need some input arguments."

        P, T, rho = None, None, None
        # convert all keywords to lower case
        args = {k.lower(): v for k,v in args.items()}

        if "p" in args.keys():
            P = np.asarray(args["p"])
        if "t" in args.keys():
            T = np.asarray(args["t"])
        if "rho" in args.keys():
            rho = np.asarray(args["rho"])

        
        if P != None and T != None and rho != None:
            assert P.size == T.size and P.size == rho.size, "P, T, rho must have the same number of elements"
            assert np.all(np.abs(P - rho * self.R * T) > 1e-08), "The input arguments appear not to follow ideal gas low"
            return None
        
        if P != None and T != None:
            assert P.size == T.size, "P, T must have the same number of elements"
            return P / self.R / T
        
        if P != None and rho != None:
            assert P.size == rho.size, "P, rho must have the same number of elements"
            return P / self.R / rho
        
        if T != None and rho != None:
            assert T.size == rho.size, "T, rho must have the same number of elements"
            return rho * self.R * T

class Flow_State(object):
    # def __init__(self, gas, M=1, P=101325, T=298.15, rho=1, T0=0, P0=0, name=""):
    # def __init__(self, gas, **args):
    def __init__(self, **args):
        # self.gas = gas

        assert args, "Must be arguments to create a flow!!!"

        self._name = ""
        self._mach = 0
        self._normal_mach = 0
        self._pressure = 0
        self._static_temperature = 0
        self._density = 0
        self._total_pressure = 0
        self._total_temperature = 0

        # self.name = ""
        # self.Mach = None
        # self.Normal_Mach = None
        # self.pressure = None
        # self.static_temperature = None
        # self.density = None
        # self.total_pressure = None
        # self.total_temperature = None

        # convert all keywords to lower case
        args = {k.lower(): v for k,v in args.items()}
        

        if "name" in args.keys(): self.name = args["name"]
        if "m" in args.keys(): self.mach = args["m"]
        if "mn" in args.keys(): self.normal_mach = args["mn"]
        if "p" in args.keys(): self.pressure = args["p"]
        if "t" in args.keys(): self.static_temperature = args["t"]
        if "rho" in args.keys(): self.density = args["rho"]
        if "p0" in args.keys(): self.total_pressure = args["p0"]
        if "t0" in args.keys(): self.total_temperature = args["t0"]
        
        # if self.total_pressure and self.total_temperature and not self.density
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def mach(self):
        return self._mach
    
    @mach.setter
    def mach(self, mach):
        self._mach = mach
    
    @property
    def normal_mach(self):
        return self._normal_mach
    
    @normal_mach.setter
    def normal_mach(self, normal_mach):
        self._normal_mach = normal_mach
    
    @property
    def pressure(self):
        return self._pressure
    
    @pressure.setter
    def pressure(self, pressure):
        self._pressure = pressure
    
    @property
    def density(self):
        return self._density
    
    @density.setter
    def density(self, density):
        self._density = density
    
    @property
    def static_temperature(self):
        return self._static_temperature
    
    @static_temperature.setter
    def static_temperature(self, static_temperature):
        self._static_temperature = static_temperature
    
    @property
    def total_temperature(self):
        return self._total_temperature
    
    @total_temperature.setter
    def total_temperature(self, total_temperature):
        self._total_temperature = total_temperature
    
    @property
    def total_pressure(self):
        return self._total_pressure
    
    @total_pressure.setter
    def total_pressure(self, total_pressure):
        self._total_pressure = total_pressure
    
    def __str__(self):
        s = "State {}\n".format(self.name)
        s += "\tM\t{}\n".format(self.mach)
        s += "\tP\t{}\n".format(self.pressure)
        s += "\tT\t{}\n".format(self.static_temperature)
        s += "\trho\t{}\n".format(self.density)
        s += "\tP0\t{}\n".format(self.total_pressure)
        s += "\tT0\t{}\n".format(self.total_temperature)
        return s
    
    def __mul__(self, a):
        # new values
        m, pn, rn, tn, p0n, t0n = None, None, None, None, None, None
        # print(a)
        # print("self.pressure", self.pressure, type(self.pressure))
        # print("a['pressure_ratio']", a["pressure_ratio"], type(a["pressure_ratio"]))
        # print("pn", pn, type(pn))
        if "m" in a.keys():
            m = a["m"]
        if "pressure_ratio" in a.keys():
            pn = self.pressure * a["pressure_ratio"]
        if "density_ratio" in a.keys():
            rn = self.density * a["density_ratio"]
        if "temperature_ratio" in a.keys():
            tn = self.static_temperature * a["temperature_ratio"]
        if "total_pressure_ratio" in a.keys():
            p0n = self.total_pressure * a["total_pressure_ratio"]
        if "total_temperature_ratio" in a.keys():
            t0n = self.total_temperature * a["total_temperature_ratio"]
        # print("pn", pn, type(pn))
        # print(self.pressure * a["pressure_ratio"])
        
        b = Flow_State(
            name = "",
            m = m,
            p = pn,
            rho = rn,
            t = tn,
            p0 = p0n,
            t0 = t0n,
        )
        
        return b

if __name__ == "__main__":
    gas = Ideal_Gas(287, 1.4)

    a = Flow_State(
        M=6.8, 
        P=1000, 
        T=220, 
        rho=gas.solve(p=1000, t=220),
        name=1
    )
    print(a)
    # print(a.to_string())