from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    return set(mapping.keys())


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    return set(mapping.values())


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    return all(v in target for v in mapping.values())


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    values = list(mapping.values())
    return len(values) == len(set(values))


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    return get_range(mapping) == target


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    return is_injective(mapping) and is_surjective(mapping, target)


def get_inverse(mapping: dict, target: set) -> dict:
    """Return f⁻¹ as a dict. Raise ValueError if f is not bijective."""
    if not is_bijective(mapping, target):
        raise ValueError("Function is not bijective — inverse is not well-defined.")
    return {v: k for k, v in mapping.items()}


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None."""
    seen = {}
    for k, v in mapping.items():
        if v in seen:
            return (seen[v], k)
        seen[v] = k
    return None


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None."""
    for elem in target:
        if elem not in get_range(mapping):
            return elem
    return None
