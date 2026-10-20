#!/usr/bin/env python3
"""Finite verification for the continuation quotient in D-ND Paper v1.0.

Exact finite models only. This is not evidence about D-ND metaphysics,
physical dynamics, cognition, or the empirical effectiveness of a method.
Uses the Python standard library; no network or external services.
"""
from __future__ import annotations
from collections import deque
from itertools import product
import json
from pathlib import Path
from typing import Hashable, Iterable

Partition = tuple[tuple[int, ...], ...]


def canonical(blocks: Iterable[Iterable[int]]) -> Partition:
    return tuple(sorted(tuple(sorted(b)) for b in blocks))


def partitions(xs: tuple[int, ...]) -> Iterable[Partition]:
    if not xs:
        yield ()
        return
    first, rest = xs[0], xs[1:]
    for p in partitions(rest):
        yield canonical(((first,), *p))
        for i in range(len(p)):
            q = list(p)
            q[i] = (*q[i], first)
            yield canonical(q)


def partition_of(values: tuple[Hashable, ...]) -> Partition:
    groups: dict[Hashable, list[int]] = {}
    for i, v in enumerate(values):
        groups.setdefault(v, []).append(i)
    return canonical(groups.values())


def labels(p: Partition) -> dict[int, int]:
    return {x: i for i, block in enumerate(p) for x in block}


def refines(p: Partition, q: Partition) -> bool:
    lab = labels(q)
    return all(len({lab[x] for x in block}) == 1 for block in p)


def stable(p: Partition, operations: tuple[tuple[int, ...], ...]) -> bool:
    lab = labels(p)
    return all(len({lab[u[x]] for x in block}) == 1
               for block in p for u in operations)


def quotient(h: tuple[Hashable, ...], operations: tuple[tuple[int, ...], ...]):
    n = len(h)
    if n < 1 or any(len(u) != n or any(y not in range(n) for y in u) for u in operations):
        raise ValueError('Require nonempty finite states and total endomaps.')
    p = partition_of(h)
    history = [p]
    while True:
        lab = labels(p)
        q = partition_of(tuple((lab[x], *(lab[u[x]] for u in operations)) for x in range(n)))
        if q == p:
            return p, history
        if len(q) <= len(p):
            raise AssertionError('A strict refinement must increase block count.')
        history.append(q)
        if len(history) - 1 > n - len(history[0]):
            raise AssertionError('Finite refinement bound violated.')
        p = q


def equivalent_pair(a: int, b: int, h: tuple[Hashable, ...], operations: tuple[tuple[int, ...], ...]) -> bool:
    """Independent product-graph reachability, covers every finite word."""
    seen = {(a, b)}
    queue = deque([(a, b)])
    while queue:
        i, j = queue.popleft()
        if h[i] != h[j]:
            return False
        for u in operations:
            pair = (u[i], u[j])
            if pair not in seen:
                seen.add(pair)
                queue.append(pair)
    return True


def verify_case(name, h, operations):
    n = len(h)
    p, history = quotient(h, operations)
    all_p = set(partitions(tuple(range(n))))
    admissible = [q for q in all_p if refines(q, partition_of(h)) and stable(q, operations)]
    assert p in admissible
    assert all(refines(q, p) for q in admissible)
    lab = labels(p)
    for a, b in product(range(n), repeat=2):
        assert (lab[a] == lab[b]) == equivalent_pair(a, b, h, operations)
    return {
        'name': name, 'observations': h, 'operations': operations,
        'quotient': p, 'refinement_history': history,
        'partitions_enumerated': len(all_p), 'admissible_partitions': len(admissible),
        'coarsest_verified': True, 'product_graph_agrees': True,
    }


def main():
    # Integers 0,1,2,3 encode support membership bits s1,s2.
    c = (0, 1, 1, 1)
    u1 = (0, 0, 2, 2)
    u2 = (0, 1, 0, 1)
    rotation = (1, 2, 3, 0)
    parity = (0, 1, 0, 1)
    enriched = ((0, 1), (1, 0), (0, 0), (1, 0))
    cases = [
        verify_case('supports_remove_s1', c, (u1,)),
        verify_case('supports_remove_s1_s2', c, (u1, u2)),
        verify_case('cycle_parity', parity, (rotation,)),
        verify_case('cycle_parity_and_is_zero', enriched, (rotation,)),
    ]
    assert cases[0]['quotient'] == ((0,), (1,), (2, 3))
    assert cases[1]['quotient'] == ((0,), (1,), (2,), (3,))
    assert cases[2]['quotient'] == ((0, 2), (1, 3))
    assert cases[3]['quotient'] == ((0,), (1,), (2,), (3,))
    # Enriched representation determines all selected parity observations but
    # is not stable as a representation of its own complete future.
    assert refines(partition_of(enriched), cases[2]['quotient'])
    assert not stable(partition_of(enriched), (rotation,))
    result = {
        'manuscript': 'DND_Paper_v1.0',
        'status': 'all_finite_checks_passed',
        'cases': cases,
        'sufficient_for_outputs_does_not_imply_self_closed': True,
        'scope': 'Four fully specified finite cases; not a proof by enumeration of the general proposition.',
    }
    path = Path(__file__).with_name('risultati_quoziente_continuazioni.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
