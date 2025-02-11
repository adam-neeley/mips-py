from mips.console import Console


def syscall(m):
    v = m.get_value("$v0")
    a = m.get_value("$a0")
    match v:
        case 4:
            Console.log(a)
        case 10:
            exit()


"R Format"


def movz(m, rd, rs, rt):
    if m.get_value(rt) == 0:
        m.set_value(rd, rs)


def movn(m, rd, rs, rt):
    if m.get_value(rt) != 0:
        m.set_value(rd, rs)


"I Format"


def li(m, rt, imm):
    "fake"
    # lui $at, 0x0003
    # ori $8, $at, 0xBF20
    m.set_value(rt, int(imm))


def ori(m, rt, rs, imm):
    s = m.get_value(rs)
    m.set_value(rt, s & int(imm))


# lui
# I Type
# Loads the upper 16 bits of the rt with the imm and fills the lower 16 bits with zeros. Used with ori, which doesn't sign-extend the immediate, these two instructions can be used to fill a register with a 32-bit constant.

# li
# I Type
# A pseudoinstruction that loads a 32-bit constant into the target register. Assemblers will translate this into a lui/ori combination.


def addi(m, rt, rs, imm):
    s = m.get_value(rs)
    m.set_value(rt, s + int(imm))


def add(m, rd, rs, rt):
    s = m.get_value(rs)
    t = m.get_value(rt)
    m.set_value(rd, s + t)


def la(m, rd, rs):
    s = m.get_value(rs)
    m.set_value(rd, s)


"J Format"


def j(m, pa):
    a = m.get_value(pa)
    m.set_value("$pc", a)


"Helpers"

Methods = locals()


def get(method_name):
    if method_name in Methods.keys():
        return Methods[method_name]


def run(machine, method_name, *args):
    method = get(method_name)
    if method:
        method(machine, *args)
    else:
        raise ValueError(f"Method not found: {method_name}")
