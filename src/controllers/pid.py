class PID:
    def __init__(self,kp,ki,kd):
        self.kp=kp; self.ki=ki; self.kd=kd
        self.i=0; self.prev=0

    def compute(self,x,ref,dt):
        err = ref - x[0]
        self.i += err*dt
        d = (err-self.prev)/dt

        u = self.kp*err + self.ki*self.i + self.kd*d
        self.prev = err
        return u