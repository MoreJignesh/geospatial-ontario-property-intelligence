
import fiona


def inspect_gdb(gdb_path):

    print("\n========== GDB CONTENTS ==========")

    layers = fiona.listlayers(gdb_path)

    for i, layer in enumerate(layers):
        print(f"{i+1}. {layer}")

    return layers