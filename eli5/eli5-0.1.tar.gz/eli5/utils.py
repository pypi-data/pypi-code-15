# -*- coding: utf-8 -*-
import numpy as np
from scipy import sparse as sp


def argsort_k_largest(x, k):
    """ Return no more than ``k`` indices of largest values. """
    if k == 0:
        return np.array([])
    if k is None or k >= len(x):
        return np.argsort(x)[::-1]
    indices = np.argpartition(x, -k)[-k:]
    values = x[indices]
    return indices[np.argsort(-values)]


def argsort_k_smallest(x, k):
    """ Return no more than ``k`` indices of smallest values. """
    if k == 0:
        return np.array([])
    if k is None or k >= len(x):
        return np.argsort(x)
    indices = np.argpartition(x, k)[:k]
    values = x[indices]
    return indices[np.argsort(values)]


def mask(x, indices):
    """
    The same as x[indices], but return an empty array if indices are empty,
    instead of returning all x elements.
    """
    if not indices.shape[0]:
        return np.array([])
    return x[indices]


def vstack(blocks, format=None, dtype=None):
    if any(sp.issparse(b) for b in blocks):
        return sp.vstack(blocks, format=format, dtype=dtype)
    else:
        return np.vstack(blocks)


def get_display_names(original_names=None, target_names=None, targets=None):
    """
    Return a list of (class_id, display_name) tuples.

    ``targets`` can be written using both names from ``target_names` and
    from ``original_names``:
    >>> get_display_names(['x', 'y'], targets=['y', 'X'],
    ...                   target_names={'x': 'X'})
    [(1, 'y'), (0, 'X')]

    Provide display names:
    >>> get_display_names([0, 2], target_names=['foo', 'bar'])
    [(0, 'foo'), (1, 'bar')]

    Change order of labels:
    >>> get_display_names(['x', 'y'], targets=['y', 'x'])
    [(1, 'y'), (0, 'x')]

    Provide display names, choose only a subset of labels:
    >>> get_display_names([0, 2], target_names=['foo', 'bar'], targets=[2])
    [(1, 'bar')]

    target_names can be a dictionary with {old_name: new_name} labels:
    >>> get_display_names(['x', 'y'], targets=['y', 'x'],
    ...                   target_names={'x': 'X'})
    [(1, 'y'), (0, 'X')]

    Error is raised when target_names format is invalid:
    >>> get_display_names(['x', 'y'], target_names=['foo'])
    Traceback (most recent call last):
    ...
    ValueError: target_names must have the same length as original names (expected 2, got 1)
    """
    if isinstance(target_names, (list, tuple, np.ndarray)):
        if original_names is not None:
            if len(target_names) != len(original_names):
                raise ValueError("target_names must have the same length as "
                                 "original names (expected {}, got {})".format(
                                     len(original_names), len(target_names)
                                 ))
        display_names = target_names
    elif isinstance(target_names, dict):
        display_names = [target_names.get(name, name)
                         for name in original_names]
    else:
        display_names = original_names

    if targets is None:
        targets = original_names

    class_indices = _get_value_indices(original_names, display_names,
                                       targets)
    names = [display_names[i] for i in class_indices]
    return list(zip(class_indices, names))


def _get_value_indices(names1, names2, lookups):
    """
    >>> _get_value_indices(['foo', 'bar', 'baz'], ['foo', 'bar', 'baz'],
    ...                    ['bar', 'foo'])
    [1, 0]
    >>> _get_value_indices(['foo', 'bar', 'baz'], ['FOO', 'bar', 'baz'],
    ...                    ['bar', 'FOO'])
    [1, 0]
    >>> _get_value_indices(['foo', 'bar', 'BAZ'], ['foo', 'BAZ', 'baz'],
    ...                    ['BAZ', 'foo'])
    [2, 0]
    >>> _get_value_indices(['foo', 'bar', 'baz'], ['foo', 'bar', 'baz'],
    ...                    ['spam'])
    Traceback (most recent call last):
    ...
    KeyError: 'spam'
    """
    positions = {name: idx for idx, name in enumerate(names2)}
    positions.update({name: idx for idx, name in enumerate(names1)})
    return [positions[name] for name in lookups]
