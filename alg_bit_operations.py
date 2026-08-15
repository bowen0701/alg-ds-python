"""Bit manipulation utility class and common algorithms.

This module provides a BitOperations class that implements various bitwise 
algorithms, including a plugin-based system for parity computation.
"""


from typing import Callable, Dict


class BitOperations:
    """
    Bit manipulation utility class.

    Design:
    - REGISTRIES: namespaced plugin system (currently parity only)
    - staticmethods: stable bit primitives and implementations
    - bit_parity: dispatch via registry with optional auto strategy
    - register: classmethod for extending the registry
    """

    # =========================================================
    # 1. Implementation Details (Internal)
    # =========================================================

    @staticmethod
    def _parity_iter(x: int) -> int:
        """Compute parity by scanning bits one by one."""
        result = 0
        while x:
            result ^= x & 1
            x >>= 1
        return result

    @staticmethod
    def _parity_drop(x: int) -> int:
        """Compute parity by repeatedly removing the lowest set bit."""
        result = 0
        while x:
            result ^= 1
            x &= (x - 1)
        return result

    @staticmethod
    def _parity_xor(x: int) -> int:
        """Compute parity using XOR folding reduction."""
        x ^= (x >> 32)
        x ^= (x >> 16)
        x ^= (x >> 8)
        x ^= (x >> 4)
        x ^= (x >> 2)
        x ^= (x >> 1)
        return x & 1

    @staticmethod
    def _parity_builtin(x: int) -> int:
        """Compute parity using Python's bit_count() or bin().count()."""
        if hasattr(x, "bit_count"):
            return x.bit_count() & 1
        return bin(x).count("1") & 1

    # =========================================================
    # 2. Namespaced registry & Registration API
    # =========================================================
    
    REGISTRIES: Dict[str, Dict[str, Callable[[int], int]]] = {
        "parity": {
            "iter": _parity_iter.__func__,     # type: ignore
            "drop": _parity_drop.__func__,     # type: ignore
            "xor": _parity_xor.__func__,       # type: ignore
            "builtin": _parity_builtin.__func__ # type: ignore
        }
    }

    @classmethod
    def register(cls, domain: str, name: str):
        """
        Register a bit-operation implementation to BitOperations.REGISTRIES.

        Usage:
            @BitOperations.register("parity", "custom")
            def my_parity(x: int) -> int:
                ...

            # Or using the module-level alias:
            @register_bitop("parity", "custom")
            def my_parity(x: int) -> int:
                ...
        """
        def decorator(fn):
            if domain not in cls.REGISTRIES:
                raise ValueError(f"Unknown domain '{domain}'")

            registry = cls.REGISTRIES[domain]

            if name in registry:
                raise ValueError(f"Duplicate registration: {domain}.{name}")

            registry[name] = fn
            return fn

        return decorator

    # =========================================================
    # 3. Public API: bitwise algorithms
    # =========================================================

    @classmethod
    def bit_parity(cls, x: int, method: str = "auto") -> int:
        """
        Compute parity (number of 1-bits mod 2).

        Supported methods:
            - "iter"     : scan bits one by one
            - "drop"     : remove lowest set bit repeatedly
            - "xor"      : XOR folding reduction
            - "builtin"  : Python bit_count()
            - "auto"     : heuristic selection

        Usage:
            BitOperations.bit_parity(13)
            BitOperations.bit_parity(13, method="iter")
            BitOperations.bit_parity(13, method="drop")
            BitOperations.bit_parity(13, method="xor")
            BitOperations.bit_parity(13, method="builtin")
            BitOperations.bit_parity(13, method="auto")
        """
        registry = cls.REGISTRIES["parity"]

        if method == "auto":
            return cls._select_parity_strategy(x)

        if method not in registry:
            raise ValueError(
                f"Unknown method '{method}'. "
                f"Available: {list(registry.keys())}"
            )

        return registry[method](x)

    @classmethod
    def _select_parity_strategy(cls, x: int) -> int:
        """
        Select the parity implementation to use for method="auto".

        Usage:
            BitOperations.bit_parity(x, method="auto")
        """
        registry = cls.REGISTRIES["parity"]

        # Small x (< 2^64) -> builtin
        if x < (1 << 64):
            return registry["builtin"](x)

        # If sparse pattern (power of 2): parity 
        if x > 0 and (x & (x - 1) == 0):
            return 1

        # Fallback to drop method
        return registry["drop"](x)

    @staticmethod
    def bit_right_propagate(x: int) -> int:
        """
        Propagate rightmost set bit to all lower bits.

        Usage:
            BitOperations.bit_right_propagate(0b00101100)
            # ->      x = 0b00101100 = 44
            #       x-1 = 0b00101011: int.from_bytes([x-1], signed=True) = 43
            # x | (x-1) = 0b00101111
        """
        if x == 0:
            return 0
        return x | (x - 1)

    @staticmethod
    def bit_isolate_lowest_set_bit(x: int) -> int:
        """
        Extract lowest set bit by x & -x.
        Note: -x = ~x + 1

        Usage:
            BitOperations.bit_isolate_lowest_set_bit(0b00101100)
            # ->      x = 0b00101100 = 44
            #        ~x = 0b11010011
            # -x = ~x+1 = 0b11010100: int.from_bytes([~x+1], signed=True) = -44
            #    x & -x = 0b00000100
        """
        return x & -x

    @staticmethod
    def bit_remove_lowest_set_bit(x: int) -> int:
        """
        Remove lowest set bit.

        Usage:
            BitOperations.bit_remove_lowest_set_bit(0b00101100)
            # ->      x = 0b00101100 = 44
            #       x-1 = 0b00101011: int.from_bytes([x-1], signed=True) = 43
            # x & (x-1) = 0b00101000
        """
        return x & (x - 1)

    @staticmethod
    def bit_is_power_of_two(x: int) -> bool:
        """
        Check if x is a power of two.

        Usage:
            BitOperations.bit_is_power_of_two(8)   # True
            # BitOperations.bit_remove_lowest_set_bit(0b00001000)
            # ->      x = 0b00001000 = 8
            #       x-1 = 0b00000111: int.from_bytes([x-1], signed=True) = 7
            # x & (x-1) = 0b00000000
            BitOperations.bit_is_power_of_two(10)  # False
            # BitOperations.bit_remove_lowest_set_bit(0b00001010)
            # ->      x = 0b00001010 = 10
            #       x-1 = 0b00001001: int.from_bytes([x-1], signed=True) = 9
            # x & (x-1) = 0b00001000 = 8 != 0 -> not power of 2
        """
        return x > 0 and (x & (x - 1)) == 0


# Module-level alias for cleaner decorator usage
register_bitop = BitOperations.register


def main():
    """Run tests for BitOperations."""
    parity_cases = [
        (0, 0),
        (1, 1),
        (0b1011, 1),
        (0b1010, 0),
    ]

    for x, expected in parity_cases:
        assert BitOperations.bit_parity(x, method="iter") == expected
        assert BitOperations.bit_parity(x, method="drop") == expected
        assert BitOperations.bit_parity(x, method="xor") == expected
        assert BitOperations.bit_parity(x, method="builtin") == expected
        assert BitOperations.bit_parity(x, method="auto") == expected

    # Test custom registration using the decorator (as shown in docstrings)
    @register_bitop("parity", "custom")
    def my_parity(x: int) -> int:
        return bin(x).count("1") % 2

    assert BitOperations.bit_parity(0b1011, method="custom") == 1
    assert BitOperations.bit_parity(0b1010, method="custom") == 0

    assert BitOperations.bit_right_propagate(0b01010000) == 0b01011111
    assert BitOperations.bit_right_propagate(0b01010010) == 0b01010011
    assert BitOperations.bit_right_propagate(0) == 0

    assert BitOperations.bit_isolate_lowest_set_bit(0b101100) == 0b000100
    assert BitOperations.bit_isolate_lowest_set_bit(0) == 0

    assert BitOperations.bit_remove_lowest_set_bit(0b101100) == 0b101000
    assert BitOperations.bit_remove_lowest_set_bit(0b1000) == 0

    assert BitOperations.bit_is_power_of_two(1)
    assert BitOperations.bit_is_power_of_two(8)
    assert not BitOperations.bit_is_power_of_two(0)
    assert not BitOperations.bit_is_power_of_two(10)

    print("All basic bit operation tests passed.")


if __name__ == "__main__":
    main()
