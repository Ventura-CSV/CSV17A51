def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping
    ##################################################
    """
    pass


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping
    ##################################################
    """
    pass


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping, target
    ##################################################
    """
    pass


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping
    ##################################################
    """
    pass


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping, target
    ##################################################
    """
    pass


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping, target
    ##################################################
    """
    pass


def get_inverse(mapping: dict, target: set) -> dict:
    """Return f⁻¹ as a dict. Raise ValueError if f is not bijective."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping, target
    ##################################################
    """
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    pass


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping
    ##################################################
    """
    pass


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None."""
    """
    ##################################################
    # Complete your code here
    Use the same variables: mapping, target
    ##################################################
    """
    pass
