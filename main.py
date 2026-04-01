from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    # === TODO START ===
    return set(mapping.keys())
    # === TODO END ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    # === TODO START ===
    return set(mapping.values())
    # === TODO END ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # === TODO START ===
    return all(v in target for v in mapping.values())
    # === TODO END ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # === TODO START ===
    values = list(mapping.values())
    return len(values) == len(set(values))
    # === TODO END ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    # === TODO START ===
    return get_range(mapping) == target
    # === TODO END ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    # === TODO START ===
    return is_injective(mapping) and is_surjective(mapping, target)
    # === TODO END ===
