#!/usr/bin/env python3
"""Exact finite illustrations for SSK's 22 October 2026 research supplement.

Python standard library only. No network, provider, runtime or private data.
Run without -O: assertions are the checks. JSON is written to standard output.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import json


@dataclass(frozen=True)
class Rule:
    premises: frozenset[str]
    conclusion: str


def subsets(universe: frozenset[str]) -> tuple[frozenset[str], ...]:
    atoms = sorted(universe)
    return tuple(frozenset(c) for n in range(len(atoms) + 1)
                 for c in combinations(atoms, n))


def trace(universe: frozenset[str], rules: tuple[Rule, ...],
          initial: frozenset[str]) -> tuple[frozenset[str], ...]:
    if not initial <= universe:
        raise ValueError('Initial statements outside the declared universe.')
    if any(not r.premises or not r.premises <= universe
           or r.conclusion not in universe for r in rules):
        raise ValueError('Rules must have nonempty premises in the finite universe.')
    current = initial
    states = [current]
    for _ in range(len(universe) + 1):
        following = current | frozenset(r.conclusion for r in rules
                                        if r.premises <= current)
        if following == current:
            return tuple(states)
        states.append(following)
        current = following
    raise AssertionError('The finite positive-rule bound was exceeded.')


def serial(states: tuple[frozenset[str], ...]) -> list[list[str]]:
    return [sorted(s) for s in states]


def main() -> dict[str, object]:
    u = frozenset('abcde')
    joint = (Rule(frozenset('ab'), 'c'), Rule(frozenset('c'), 'd'))
    single = (Rule(frozenset('a'), 'c'), Rule(frozenset('c'), 'd'))
    projected = tuple(Rule(frozenset({p}), r.conclusion)
                      for r in joint for p in sorted(r.premises))
    all_seeds = subsets(u)
    closed = {s: trace(u, joint, s)[-1] for s in all_seeds}
    closed_sets = [s for s in all_seeds if closed[s] == s]
    ordered_pairs = 0
    for s in all_seeds:
        assert s <= closed[s]
        assert closed[closed[s]] == closed[s]
        assert len(trace(u, joint, s)) - 1 <= len(u - s)
        assert all(closed[s] <= z for z in closed_sets if s <= z)
        for t in all_seeds:
            if s <= t:
                assert closed[s] <= closed[t]
                ordered_pairs += 1
    assert ordered_pairs == 243
    assert closed[frozenset('a')] == frozenset('a')
    assert closed[frozenset('b')] == frozenset('b')
    assert closed[frozenset('ab')] == frozenset('abcd')
    assert closed[frozenset('a')] | closed[frozenset('b')] < closed[frozenset('ab')]
    assert trace(u, projected, frozenset('a'))[-1] == frozenset('acd')
    observed_joint = trace(u, joint, frozenset('ab'))
    observed_single = trace(u, single, frozenset('ab'))
    assert observed_joint == observed_single
    assert observed_joint == (frozenset('ab'), frozenset('abc'), frozenset('abcd'))
    contrast_joint = trace(u, joint, frozenset('a'))
    contrast_single = trace(u, single, frozenset('a'))
    assert contrast_joint == (frozenset('a'),)
    assert contrast_single == (frozenset('a'), frozenset('ac'), frozenset('acd'))
    expanded = joint + (Rule(frozenset('d'), 'e'),)
    assert trace(u, expanded, frozenset('ab'))[-1] == u
    cycle = (Rule(frozenset('a'), 'b'), Rule(frozenset('b'), 'a'))
    assert trace(u, cycle, frozenset()) == (frozenset(),)
    weights = (Fraction(1, len(closed[frozenset('a')])),
               Fraction(1, len(closed[frozenset('ab')])))
    assert weights == (Fraction(1), Fraction(1, 4))
    return {
        'scope': 'Fixed positive rules on a finite declared universe; not a cognitive experiment.',
        'closure_checks': {'seed_sets': len(all_seeds), 'inclusion_pairs': ordered_pairs,
                           'extensive': True, 'monotone': True, 'idempotent': True,
                           'minimal': True, 'finite_bound': True},
        'shared_trace_from_ab': serial(observed_joint),
        'joint_trace_from_a': serial(contrast_joint),
        'single_trace_from_a': serial(contrast_single),
        'naive_graph_closure_from_a': sorted(trace(u, projected, frozenset('a'))[-1]),
        'changed_rules_closure_from_ab': sorted(trace(u, expanded, frozenset('ab'))[-1]),
        'uniform_selection_weight_a': [str(w) for w in weights],
        'all_assertions_passed': True,
    }


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Run without -O so that the verification assertions execute.')
    print(json.dumps(main(), ensure_ascii=False, indent=2, sort_keys=True))
